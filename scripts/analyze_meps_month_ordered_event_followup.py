#!/usr/bin/env python3
"""Screen month-ordered MEPS event exposure against R4/2 context fields."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


FLAGS = [f"BRR{i}" for i in range(1, 129)]
EVENTS = {
    "office": ("EVNTIDX", "OBDATEYR", "OBDATEMM"),
    "emergency_room": ("EVNTIDX", "ERDATEYR", "ERDATEMM"),
    "inpatient": ("EVNTIDX", "IPBEGYR", "IPBEGMM"),
}
OUTCOMES = {
    "medical_bill_problem": ("PROBPY42", lambda s: s == 1, [1, 2]),
    "fair_or_poor_perceived_health": ("RTHLTH42", lambda s: s >= 4, [1, 2, 3, 4, 5]),
    "not_employed_r4_2": ("EMPST42", lambda s: s == 4, [1, 2, 3, 4]),
}
GROUPS = ["no_event", "first_event_before_r4_2_end", "first_event_same_month_r4_2_end", "first_event_after_r4_2_end"]


def estimate(frame: pd.DataFrame, group: pd.Series, target_group: str, field: str, fn, valid_codes: list[int]) -> dict[str, float | int | None]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = weights.gt(0) & group.eq(target_group) & frame[field].isin(valid_codes)
    if not valid.any():
        return {"valid_records": 0, "share_percent": None, "brr_se_percentage_points": None, "ci95_low": None, "ci95_high": None}
    values = fn(frame[field]).astype(float)
    point = float(np.average(values[valid], weights=weights[valid]) * 100)
    reps = []
    for flag in FLAGS:
        rw = weights[valid] * 2 * frame.loc[valid, flag]
        reps.append(float(np.average(values[valid], weights=rw) * 100))
    se = float(np.sqrt(np.mean((np.asarray(reps) - point) ** 2)))
    return {"valid_records": int(valid.sum()), "share_percent": point, "brr_se_percentage_points": se, "ci95_low": point - 1.96 * se, "ci95_high": point + 1.96 * se}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person_fields = ["DUPERSID", "PANEL", "PERWT24F", "ENDRFY42", "ENDRFM42", "PROBPY42", "RTHLTH42", "EMPST42"]
    person, _ = pyreadstat.read_dta(args.hc256_file, usecols=person_fields)
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS])
    person["KEY"] = person["DUPERSID"].astype(str) + "|" + person["PANEL"].astype(str)
    brr["KEY"] = brr["DUPERSID"].astype(str) + "|" + brr["PANEL"].round().astype(int).astype(str)
    person = person.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    endpoint = pd.to_numeric(person["ENDRFY42"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM42"], errors="coerce")
    paths = {"office": args.office_file, "emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}
    output: dict[str, object] = {
        "schema": "us-meps-2024-month-ordered-event-followup-v1",
        "method": "For each person and event family, the first valid event month is compared with the person-specific R4/2 reference-period end month. Outcomes are R4/2 fields; standard BRR uses 128 replicate flags.",
        "person_records": len(person),
        "positive_weight_records": int(pd.to_numeric(person["PERWT24F"], errors="coerce").gt(0).sum()),
        "events": {},
        "limitation": "Month ordering is not exact-day ordering. Same-period fields may include the event period, and event presence is selected. Results are descriptive, not causal recovery estimates.",
    }
    for name, path in paths.items():
        event_id, year_field, month_field = EVENTS[name]
        event, _ = pyreadstat.read_dta(path, usecols=["DUPERSID", "PANEL", event_id, year_field, month_field])
        event["KEY"] = event["DUPERSID"].astype(str) + "|" + event["PANEL"].round().astype(int).astype(str)
        year = pd.to_numeric(event[year_field], errors="coerce")
        month = pd.to_numeric(event[month_field], errors="coerce")
        valid_date = year.between(1900, 2024) & month.between(1, 12)
        event["EVENT_MONTH"] = year * 12 + month
        first = event.loc[valid_date].groupby("KEY", as_index=True)["EVENT_MONTH"].min()
        first.name = "FIRST_EVENT_MONTH"
        joined = person.join(first, on="KEY")
        event_month = joined["FIRST_EVENT_MONTH"]
        group = pd.Series("no_event", index=joined.index, dtype="object")
        has_event = event_month.notna() & endpoint.notna()
        group.loc[has_event & event_month.lt(endpoint)] = "first_event_before_r4_2_end"
        group.loc[has_event & event_month.eq(endpoint)] = "first_event_same_month_r4_2_end"
        group.loc[has_event & event_month.gt(endpoint)] = "first_event_after_r4_2_end"
        outcomes: dict[str, object] = {}
        for outcome_name, (field, fn, valid_codes) in OUTCOMES.items():
            outcomes[outcome_name] = {g: estimate(joined, group, g, field, fn, valid_codes) for g in GROUPS}
        output["events"][name] = {
            "event_records": len(event),
            "valid_event_date_records": int(valid_date.sum()),
            "unique_people_with_valid_event": int(first.index.nunique()),
            "group_counts": {g: int((group == g).sum()) for g in GROUPS},
            "outcomes": outcomes,
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
