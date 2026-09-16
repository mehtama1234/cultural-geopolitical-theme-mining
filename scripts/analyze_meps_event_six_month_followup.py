#!/usr/bin/env python3
"""Screen strict-window MEPS events against later R5/3 health and work outcomes."""

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
GROUPS = ("event_window", "no_event_in_window")


def key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def estimate(frame: pd.DataFrame, mask: pd.Series, values: pd.Series) -> dict[str, float | int | None]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = mask & weights.gt(0) & values.notna()
    if not valid.any():
        return {"valid_records": 0, "share_percent": None, "brr_se_percentage_points": None,
                "ci95_low": None, "ci95_high": None}
    point = float(np.average(values[valid].astype(float), weights=weights[valid]) * 100)
    replicate = []
    for flag in FLAGS:
        replicate_weights = weights[valid] * 2 * frame.loc[valid, flag]
        if replicate_weights.sum() <= 0:
            return {"valid_records": int(valid.sum()), "share_percent": point,
                    "brr_se_percentage_points": None, "ci95_low": None, "ci95_high": None}
        replicate.append(float(np.average(values[valid].astype(float), weights=replicate_weights) * 100))
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

    person_fields = [
        "DUPERSID", "PANEL", "PERWT24F", "ENDRFY31", "ENDRFM31",
        "ENDRFY42", "ENDRFM42", "ENDRFY53", "ENDRFM53", "RTHLTH42",
        "RTHLTH53", "EMPST42", "EMPST53",
    ]
    person, _ = pyreadstat.read_dta(args.hc256_file, usecols=person_fields)
    person["KEY"] = key(person)
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS])
    brr["KEY"] = key(brr)
    person = person.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")

    def month(year: pd.Series, month_value: pd.Series) -> pd.Series:
        year_numeric = pd.to_numeric(year, errors="coerce")
        month_numeric = pd.to_numeric(month_value, errors="coerce")
        return year_numeric * 12 + month_numeric

    r3 = month(person["ENDRFY31"], person["ENDRFM31"])
    r4 = month(person["ENDRFY42"], person["ENDRFM42"])
    r5 = month(person["ENDRFY53"], person["ENDRFM53"])
    round_valid = r3.notna() & r4.notna() & r5.notna() & r4.gt(r3) & r5.gt(r4)

    outcome_values = {
        "fair_or_poor_health_r4": person["RTHLTH42"].isin([4, 5]).where(person["RTHLTH42"].isin([1, 2, 3, 4, 5])),
        "fair_or_poor_health_r5": person["RTHLTH53"].isin([4, 5]).where(person["RTHLTH53"].isin([1, 2, 3, 4, 5])),
        "health_worsened_r4_to_r5": (person["RTHLTH53"] > person["RTHLTH42"]).where(
            person["RTHLTH42"].isin([1, 2, 3, 4, 5]) & person["RTHLTH53"].isin([1, 2, 3, 4, 5])
        ),
        "not_employed_r4": person["EMPST42"].eq(4).where(person["EMPST42"].isin([1, 2, 3, 4])),
        "not_employed_r5": person["EMPST53"].eq(4).where(person["EMPST53"].isin([1, 2, 3, 4])),
        "employment_status_changed_r4_to_r5": (person["EMPST53"] != person["EMPST42"]).where(
            person["EMPST42"].isin([1, 2, 3, 4]) & person["EMPST53"].isin([1, 2, 3, 4])
        ),
    }
    paths = {
        "office": args.office_file,
        "emergency_room": args.emergency_room_file,
        "inpatient": args.inpatient_file,
    }
    output: dict[str, object] = {
        "schema": "us-meps-2024-event-six-month-followup-v1",
        "method": "Select each person's first valid event strictly after R3/1 and strictly before R4/2, then compare R4/2 and R5/3 health/work outcomes. Standard BRR uses 128 replicate flags.",
        "person_records": int(len(person)),
        "positive_weight_records": int(pd.to_numeric(person["PERWT24F"], errors="coerce").gt(0).sum()),
        "round_order_valid_records": int(round_valid.sum()),
        "events": {},
        "limitation": "R5/3 is a later panel outcome, not verified recovery from the event. The no-event-in-window group is not a no-need control; event selection, baseline differences, exact event-day timing, treatment continuity, and attrition remain. Results are descriptive, not causal.",
    }

    for name, path in paths.items():
        year_field, month_field = EVENTS[name]
        event, _ = pyreadstat.read_dta(path, usecols=["DUPERSID", "PANEL", year_field, month_field])
        event["KEY"] = key(event)
        event_month = month(event[year_field], event[month_field])
        valid_date = event_month.notna()
        event["EVENT_MONTH"] = event_month
        first = event.loc[valid_date].groupby("KEY")["EVENT_MONTH"].min()
        first.name = "FIRST_EVENT_MONTH"
        joined = person.join(first, on="KEY")
        in_window = round_valid & joined["FIRST_EVENT_MONTH"].gt(r3) & joined["FIRST_EVENT_MONTH"].lt(r4)
        masks = {"event_window": in_window, "no_event_in_window": round_valid & ~in_window}
        outcomes = {
            outcome_name: {
                group: estimate(joined, mask, values)
                for group, mask in masks.items()
            }
            for outcome_name, values in outcome_values.items()
        }
        output["events"][name] = {
            "event_records": int(len(event)),
            "valid_event_date_records": int(valid_date.sum()),
            "unique_people_with_valid_event": int(first.index.nunique()),
            "group_counts": {group: int(mask.sum()) for group, mask in masks.items()},
            "outcomes": outcomes,
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
