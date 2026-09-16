#!/usr/bin/env python3
"""Compare MEPS event-family context by insurance denial/prior-authorization friction.

This is a bounded descriptive join.  It identifies people with at least one
dated event in an event family, links them to HC-256 institutional-friction
and context fields, and retains only the first person in each event family.
It does not claim that the denial preceded the event or caused any outcome.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


EVENTS = {
    "office": ("OBDATEYR", "OBDATEMM"),
    "emergency_room": ("ERDATEYR", "ERDATEMM"),
    "inpatient": ("IPBEGYR", "IPBEGMM"),
}
OUTCOMES = {
    "cost_related_medical_care_delay": lambda frame: frame["DLAYCA42"].eq(1),
    "medical_debt": lambda frame: frame["MEDDEBT42"].between(1, 7),
    "debt_collector_contact": lambda frame: frame["FWDEBT42"].eq(1),
    "medical_bill_problem": lambda frame: frame["PROBPY42"].eq(1),
}
INSURANCE = {1: "any_private", 2: "public_only", 3: "uninsured"}
FINANCIAL_ROOM = {
    1: "not_at_all_confident",
    2: "not_too_confident",
    3: "somewhat_confident",
    4: "very_confident",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def weighted_share(frame: pd.DataFrame, predicate) -> float | None:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = weights.gt(0) & frame["EQDENY53"].isin([1, 2])
    if not valid.any():
        return None
    values = predicate(frame).astype(float)
    return float(100 * np.average(values[valid], weights=weights[valid]))


def summarize_group(frame: pd.DataFrame) -> dict[str, object]:
    valid = frame["EQDENY53"].isin([1, 2]) & frame["PERWT24F"].gt(0)
    frame = frame.loc[valid]
    return {
        "records": int(len(frame)),
        "weighted_denominator": float(frame["PERWT24F"].sum()),
        "outcomes_percent": {
            name: weighted_share(frame, predicate)
            for name, predicate in OUTCOMES.items()
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person_fields = [
        "DUPERSID", "PANEL", "PERWT24F", "EQDENY53", "DLAYCA42",
        "MEDDEBT42", "FWDEBT42", "PROBPY42", "INSCOV24", "FWUNEXP42",
    ]
    people, _ = pyreadstat.read_dta(args.hc256_file, usecols=person_fields, apply_value_formats=False, encoding="latin1")
    people["PERSON_KEY"] = key(people)
    people = people.set_index("PERSON_KEY")
    outputs: dict[str, object] = {
        "schema": "us-meps-2024-event-institutional-friction-v1",
        "method": "Select the first dated event per person and event family, exact-join to HC-256 by DUPERSID+PANEL, and compare EQDENY53 denial/prior-authorization-delay groups using positive PERWT24F; retain coverage and unexpected-expense confidence strata as descriptive intersections.",
        "causal_estimation": False,
        "inputs": {"hc256": {"path": str(args.hc256_file), "sha256": sha256(args.hc256_file)}},
        "events": {},
        "limitation": "EQDENY53 has no claim identifier, decision date, appeal, or resolution. It is collected in the annual person file and is not shown to precede the observed event; event presence is selected and outcomes are same-round context, not post-event effects. Coverage and unexpected-expense confidence are also annual/person-level context, not event-specific plan or cash measures.",
    }
    paths = {"office": args.office_file, "emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}
    for family, path in paths.items():
        year_field, month_field = EVENTS[family]
        fields = ["DUPERSID", "PANEL", year_field, month_field]
        events, _ = pyreadstat.read_dta(path, usecols=fields, apply_value_formats=False, encoding="latin1")
        events["PERSON_KEY"] = key(events)
        year = pd.to_numeric(events[year_field], errors="coerce")
        month = pd.to_numeric(events[month_field], errors="coerce")
        valid = year.between(1900, 2024) & month.between(1, 12)
        events = events.loc[valid].drop_duplicates("PERSON_KEY", keep="first")
        joined = events.join(people, on="PERSON_KEY", rsuffix="_person", how="inner")
        joined = joined[joined["EQDENY53"].isin([1, 2]) & joined["PERWT24F"].gt(0)]
        groups: dict[str, object] = {}
        for code, label in ((1, "denial_or_prior_authorization_delay"), (2, "no_denial_or_prior_authorization_delay")):
            group = joined[joined["EQDENY53"].eq(code)]
            groups[label] = summarize_group(group)
        friction_by_coverage: dict[str, object] = {}
        for code, label in INSURANCE.items():
            coverage = joined[joined["INSCOV24"].eq(code)]
            friction_by_coverage[label] = {
                "denial_or_prior_authorization_delay": summarize_group(coverage[coverage["EQDENY53"].eq(1)]),
                "no_denial_or_prior_authorization_delay": summarize_group(coverage[coverage["EQDENY53"].eq(2)]),
            }
        friction_by_financial_room: dict[str, object] = {}
        for code, label in FINANCIAL_ROOM.items():
            room = joined[joined["FWUNEXP42"].eq(code)]
            friction_by_financial_room[label] = {
                "denial_or_prior_authorization_delay": summarize_group(room[room["EQDENY53"].eq(1)]),
                "no_denial_or_prior_authorization_delay": summarize_group(room[room["EQDENY53"].eq(2)]),
            }
        outputs["inputs"][family] = {"path": str(path), "sha256": sha256(path)}
        outputs["events"][family] = {
            "dated_event_people": int(len(events)),
            "valid_friction_people": int(len(joined)),
            "groups": groups,
            "friction_by_coverage": friction_by_coverage,
            "friction_by_financial_room": friction_by_financial_room,
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(outputs, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(outputs, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
