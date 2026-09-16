#!/usr/bin/env python3
"""Estimate a bounded MEPS friction-to-later-panel persistence screen."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


FLAGS = [f"BRR{i}" for i in range(1, 129)]
EVENTS = {
    "office": ("OBDATEYR", "OBDATEMM"),
    "emergency_room": ("ERDATEYR", "ERDATEMM"),
    "inpatient": ("IPBEGYR", "IPBEGMM"),
}
GROUPS = {"denial_or_delay": 1, "no_denial_or_delay": 2}


def key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def estimate(frame: pd.DataFrame, mask: pd.Series, values: pd.Series) -> dict[str, float | int | None]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = mask & weights.gt(0) & values.notna()
    if not valid.any():
        return {"valid_records": 0, "share_percent": None, "brr_se_percentage_points": None,
                "ci95_low": None, "ci95_high": None}
    y = values[valid].astype(float)
    point = float(np.average(y, weights=weights[valid]) * 100)
    replicate = []
    for flag in FLAGS:
        replicate_weights = weights[valid] * 2 * pd.to_numeric(frame.loc[valid, flag], errors="coerce")
        if replicate_weights.sum() <= 0:
            return {"valid_records": int(valid.sum()), "share_percent": point,
                    "brr_se_percentage_points": None, "ci95_low": None, "ci95_high": None}
        replicate.append(float(np.average(y, weights=replicate_weights) * 100))
    se = float(np.sqrt(np.mean((np.asarray(replicate) - point) ** 2)))
    return {"valid_records": int(valid.sum()), "share_percent": point,
            "brr_se_percentage_points": se, "ci95_low": point - 1.96 * se,
            "ci95_high": point + 1.96 * se}


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
        "ENDRFY53", "ENDRFM53", "EQDENY53", "RTHLTH42", "RTHLTH53", "EMPST42", "EMPST53",
    ]
    person, _ = pyreadstat.read_dta(args.hc256_file, usecols=fields, apply_value_formats=False, encoding="latin1")
    person["KEY"] = key(person)
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS], apply_value_formats=False, encoding="latin1")
    brr["KEY"] = key(brr)
    person = person.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    person = person.loc[pd.to_numeric(person["PERWT24F"], errors="coerce").gt(0)].reset_index(drop=True)

    def month(year: pd.Series, month_value: pd.Series) -> pd.Series:
        return pd.to_numeric(year, errors="coerce") * 12 + pd.to_numeric(month_value, errors="coerce")

    r3 = month(person["ENDRFY31"], person["ENDRFM31"])
    r4 = month(person["ENDRFY42"], person["ENDRFM42"])
    r5 = month(person["ENDRFY53"], person["ENDRFM53"])
    round_valid = r3.notna() & r4.notna() & r5.notna() & r4.gt(r3) & r5.gt(r4)
    health_valid = person["RTHLTH42"].isin([1, 2, 3, 4, 5]) & person["RTHLTH53"].isin([1, 2, 3, 4, 5])
    employment_valid = person["EMPST42"].isin([1, 2, 3, 4]) & person["EMPST53"].isin([1, 2, 3, 4])
    values = {
        "fair_or_poor_health_r4": person["RTHLTH42"].isin([4, 5]).where(person["RTHLTH42"].isin([1, 2, 3, 4, 5])),
        "fair_or_poor_health_r5": person["RTHLTH53"].isin([4, 5]).where(person["RTHLTH53"].isin([1, 2, 3, 4, 5])),
        "health_worsened_r4_to_r5": (person["RTHLTH53"] > person["RTHLTH42"]).where(health_valid),
        "fair_or_poor_health_resolved": (person["RTHLTH42"].isin([4, 5]) & person["RTHLTH53"].isin([1, 2, 3])).where(health_valid & person["RTHLTH42"].isin([4, 5])),
        "fair_or_poor_health_onset": (person["RTHLTH42"].isin([1, 2, 3]) & person["RTHLTH53"].isin([4, 5])).where(health_valid & person["RTHLTH42"].isin([1, 2, 3])),
        "not_employed_r4": person["EMPST42"].eq(4).where(person["EMPST42"].isin([1, 2, 3, 4])),
        "not_employed_r5": person["EMPST53"].eq(4).where(person["EMPST53"].isin([1, 2, 3, 4])),
        "nonemployment_resolved": (person["EMPST42"].eq(4) & person["EMPST53"].isin([1, 2, 3])).where(employment_valid & person["EMPST42"].eq(4)),
        "nonemployment_onset": (person["EMPST42"].isin([1, 2, 3]) & person["EMPST53"].eq(4)).where(employment_valid & person["EMPST42"].isin([1, 2, 3])),
    }
    output: dict[str, object] = {
        "schema": "us-meps-2024-friction-later-panel-v1",
        "method": "Select first event strictly after R3/1 and before R4/2, retain EQDENY53=1 or 2, and compare R4/2 to R5/3 health/work levels and baseline-conditioned transitions. Standard BRR uses 128 replicate flags.",
        "person_records_positive_weight": int(len(person)),
        "round_order_valid_records": int(round_valid.sum()),
        "events": {},
        "limitation": "EQDENY53 is a round-level report without claim ID, denial date, appeal, remedy, or treatment continuity. The event may follow the initiating need; friction groups are descriptive and the no-denial group is not a counterfactual. Later health/work transitions are not verified recovery.",
    }
    for family, path in {"office": args.office_file, "emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}.items():
        year_field, month_field = EVENTS[family]
        event, _ = pyreadstat.read_dta(path, usecols=["DUPERSID", "PANEL", year_field, month_field], apply_value_formats=False, encoding="latin1")
        event["KEY"] = key(event)
        event_month = month(event[year_field], event[month_field])
        valid_date = event_month.notna()
        event["EVENT_MONTH"] = event_month
        first = event.loc[valid_date].groupby("KEY")["EVENT_MONTH"].min()
        first.name = "FIRST_EVENT_MONTH"
        joined = person.join(first, on="KEY")
        in_window = round_valid & joined["FIRST_EVENT_MONTH"].gt(r3) & joined["FIRST_EVENT_MONTH"].lt(r4)
        event_window = joined.loc[in_window].copy()
        friction = pd.to_numeric(event_window["EQDENY53"], errors="coerce")
        family_output: dict[str, object] = {
            "event_window_people": int(len(event_window)),
            "friction_groups": {},
        }
        for group_name, code in GROUPS.items():
            group = event_window.loc[friction.eq(code)]
            group_mask = pd.Series(True, index=group.index)
            family_output["friction_groups"][group_name] = {
                "records": int(len(group)),
                "outcomes": {name: estimate(group, group_mask, value.loc[group.index]) for name, value in values.items()},
            }
        output["events"][family] = family_output
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"schema": output["schema"], "events": {name: value["event_window_people"] for name, value in output["events"].items()}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
