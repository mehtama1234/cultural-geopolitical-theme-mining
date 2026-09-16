#!/usr/bin/env python3
"""Estimate a strict inter-round MEPS event-plus-friction cascade screen."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


FLAGS = [f"BRR{i}" for i in range(1, 129)]
EVENTS = {
    "office": ("OBDATEYR", "OBDATEMM", "OBSF24X"),
    "emergency_room": ("ERDATEYR", "ERDATEMM", "ERFSF24X"),
    "inpatient": ("IPBEGYR", "IPBEGMM", "IPFSF24X"),
}
OUTCOMES = {
    "cost_related_care_delay": ("DLAYCA42", lambda s: s.eq(1), lambda s: s.isin([1, 2])),
    "medical_bill_problem": ("PROBPY42", lambda s: s.eq(1), lambda s: s.isin([1, 2])),
    "medical_debt": ("MEDDEBT42", lambda s: s.between(1, 7), lambda s: s.between(0, 7)),
    "debt_collector_contact": ("FWDEBT42", lambda s: s.eq(1), lambda s: s.isin([1, 2])),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def estimate(frame: pd.DataFrame, values: pd.Series) -> dict[str, object]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = values.notna() & weights.gt(0)
    if not valid.any():
        return {"valid_records": 0, "share_percent": None, "brr_se_percentage_points": None, "approx_95_ci_percentage_points": None}
    y = values.astype(float)
    point = float(np.average(y[valid], weights=weights[valid]) * 100)
    replicates = []
    for flag in FLAGS:
        replicate_weights = weights[valid] * 2 * pd.to_numeric(frame.loc[valid, flag], errors="coerce")
        replicates.append(float(np.average(y[valid], weights=replicate_weights) * 100))
    se = float(np.sqrt(np.mean((np.asarray(replicates) - point) ** 2)))
    return {
        "valid_records": int(valid.sum()),
        "share_percent": point,
        "brr_se_percentage_points": se,
        "approx_95_ci_percentage_points": [point - 1.96 * se, point + 1.96 * se],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    fields = [
        "DUPERSID", "PANEL", "PERWT24F", "ENDRFY31", "ENDRFM31", "ENDRFY42", "ENDRFM42",
        "EQDENY53", *[field for field, _, _ in OUTCOMES.values()],
    ]
    person, _ = pyreadstat.read_dta(args.hc256_file, usecols=fields, apply_value_formats=False, encoding="latin1")
    person["KEY"] = key(person)
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS], apply_value_formats=False, encoding="latin1")
    brr["KEY"] = key(brr)
    person = person.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    if person["BRR1"].isna().any():
        raise SystemExit("HC-256 to HC-036BRR merge has missing replicate flags")
    person = person.loc[pd.to_numeric(person["PERWT24F"], errors="coerce").gt(0)].reset_index(drop=True)
    r3 = pd.to_numeric(person["ENDRFY31"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM31"], errors="coerce")
    r4 = pd.to_numeric(person["ENDRFY42"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM42"], errors="coerce")
    round_valid = r3.notna() & r4.notna() & r4.gt(r3)

    output: dict[str, object] = {
        "schema": "us-meps-dated-friction-cascade-v1",
        "method": "Select each person's first valid dated event per event family, retain only events strictly between R3/1 and R4/2 endpoint months, then compare EQDENY53=1 with EQDENY53=2 using PERWT24F and 128 standard BRR flags.",
        "person_records_positive_weight": int(len(person)),
        "round_order_valid_records": int(round_valid.sum()),
        "inputs": {
            "hc256": {"path": str(args.hc256_file), "sha256": sha256(args.hc256_file)},
            "brr": {"path": str(args.brr_file), "sha256": sha256(args.brr_file)},
        },
        "events": {},
        "limitation": "EQDENY53 and outcomes are round-level reported context without claim ID or denial date. Event presence is selected, the first event is not necessarily the trigger, and the friction comparison is descriptive rather than causal. The no-friction group is not a counterfactual for denial.",
    }
    for family, path in {"office": args.office_file, "emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}.items():
        year_field, month_field, payment_field = EVENTS[family]
        event, _ = pyreadstat.read_dta(path, usecols=["DUPERSID", "PANEL", year_field, month_field, payment_field], apply_value_formats=False, encoding="latin1")
        event["KEY"] = key(event)
        year = pd.to_numeric(event[year_field], errors="coerce")
        month = pd.to_numeric(event[month_field], errors="coerce")
        event["EVENT_MONTH"] = year * 12 + month
        valid_event = year.between(1900, 2024) & month.between(1, 12)
        first = event.loc[valid_event].sort_values(["KEY", "EVENT_MONTH"]).drop_duplicates("KEY", keep="first")
        first = first[["KEY", "EVENT_MONTH", payment_field]].rename(columns={payment_field: "EVENT_PAYMENT"})
        joined = person.merge(first, on="KEY", how="left", validate="one_to_one")
        in_window = round_valid & joined["EVENT_MONTH"].gt(r3) & joined["EVENT_MONTH"].lt(r4)
        window = joined.loc[in_window].copy()
        friction = pd.to_numeric(window["EQDENY53"], errors="coerce")
        family_output: dict[str, object] = {
            "valid_first_event_people": int(len(first)),
            "event_window_people": int(len(window)),
            "event_window_payment_field": payment_field,
            "friction_groups": {},
        }
        for group_name, code in (("denial_or_delay", 1), ("no_denial_or_delay", 2)):
            group = window.loc[friction.eq(code)].copy()
            group_output: dict[str, object] = {"records": int(len(group)), "outcomes": {}}
            for outcome, (field, positive, valid_field) in OUTCOMES.items():
                numeric = pd.to_numeric(group[field], errors="coerce")
                group_output["outcomes"][outcome] = estimate(group, positive(numeric).where(valid_field(numeric)))
            family_output["friction_groups"][group_name] = group_output
        output["events"][family] = family_output

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"schema": output["schema"], "events": {name: value["event_window_people"] for name, value in output["events"].items()}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
