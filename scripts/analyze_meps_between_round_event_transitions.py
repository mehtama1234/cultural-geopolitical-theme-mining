#!/usr/bin/env python3
"""Estimate MEPS health/work transitions for events between two round endpoints."""

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


def estimate(frame: pd.DataFrame, mask: pd.Series, value: pd.Series) -> dict[str, float | int | None]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = mask & weights.gt(0) & value.notna()
    if not valid.any():
        return {"valid_records": 0, "share_percent": None, "brr_se_percentage_points": None, "ci95_low": None, "ci95_high": None}
    point = float(np.average(value[valid], weights=weights[valid]) * 100)
    reps = []
    for flag in FLAGS:
        rw = weights[valid] * 2 * frame.loc[valid, flag]
        reps.append(float(np.average(value[valid], weights=rw) * 100))
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

    person_fields = ["DUPERSID", "PANEL", "PERWT24F", "ENDRFY31", "ENDRFM31", "ENDRFY42", "ENDRFM42", "EMPST31", "EMPST42", "RTHLTH31", "RTHLTH42", "PROBPY42"]
    person, _ = pyreadstat.read_dta(args.hc256_file, usecols=person_fields)
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS])
    person["KEY"] = person["DUPERSID"].astype(str) + "|" + person["PANEL"].astype(str)
    brr["KEY"] = brr["DUPERSID"].astype(str) + "|" + brr["PANEL"].round().astype(int).astype(str)
    person = person.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    r3 = pd.to_numeric(person["ENDRFY31"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM31"], errors="coerce")
    r4 = pd.to_numeric(person["ENDRFY42"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM42"], errors="coerce")
    round_valid = r3.between(1900 * 12, 2030 * 12) & r4.between(1900 * 12, 2030 * 12) & r4.gt(r3)
    baseline_health = person["RTHLTH31"].isin([1, 2, 3, 4, 5])
    follow_health = person["RTHLTH42"].isin([1, 2, 3, 4, 5])
    baseline_employment = person["EMPST31"].isin([1, 2, 3, 4])
    follow_employment = person["EMPST42"].isin([1, 2, 3, 4])
    output: dict[str, object] = {
        "schema": "us-meps-2024-between-round-event-transitions-v1",
        "method": "A person's first valid event month must be strictly after the R3/1 endpoint and strictly before the R4/2 endpoint. Baseline is R3/1; follow-up is R4/2. Same-month boundary cases are excluded. Standard BRR uses 128 replicate flags.",
        "person_records": len(person),
        "round_order_valid_records": int(round_valid.sum()),
        "events": {},
        "limitation": "Month-level ordering excludes boundary ambiguity but does not reveal event day, exact interview day, care choice, or unmeasured confounding. Transitions are descriptive and not causal recovery estimates.",
    }
    paths = {"office": args.office_file, "emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}
    for name, path in paths.items():
        event_id, year_field, month_field = EVENTS[name]
        event, _ = pyreadstat.read_dta(path, usecols=["DUPERSID", "PANEL", event_id, year_field, month_field])
        event["KEY"] = event["DUPERSID"].astype(str) + "|" + event["PANEL"].round().astype(int).astype(str)
        year = pd.to_numeric(event[year_field], errors="coerce")
        month = pd.to_numeric(event[month_field], errors="coerce")
        event_valid = year.between(1900, 2024) & month.between(1, 12)
        event["EVENT_MONTH"] = year * 12 + month
        first = event.loc[event_valid].groupby("KEY")["EVENT_MONTH"].min()
        joined = person.join(first.rename("FIRST_EVENT_MONTH"), on="KEY")
        first_month = joined["FIRST_EVENT_MONTH"]
        in_window = round_valid & first_month.gt(r3) & first_month.lt(r4)
        no_event_window = round_valid & ~in_window
        health_valid = baseline_health & follow_health
        employment_valid = baseline_employment & follow_employment
        health_base = person["RTHLTH31"].ge(4).astype(float)
        health_follow = person["RTHLTH42"].ge(4).astype(float)
        employed_base = person["EMPST31"].isin([1, 2, 3])
        employed_follow = person["EMPST42"].isin([1, 2, 3])
        health_worsened = (person["RTHLTH42"] > person["RTHLTH31"]).astype(float)
        health_improved = (person["RTHLTH42"] < person["RTHLTH31"]).astype(float)
        employment_loss = (employed_base & ~employed_follow).astype(float)
        employment_gain = (~employed_base & employed_follow).astype(float)
        event_output: dict[str, object] = {
            "event_records": len(event),
            "valid_event_date_records": int(event_valid.sum()),
            "event_people_in_inter_round_window": int(in_window.sum()),
            "comparison_people_without_event_in_window": int(no_event_window.sum()),
            "event_window_date_rule": "first event month > R3/1 endpoint month and < R4/2 endpoint month",
            "transitions": {
                "fair_or_poor_health_at_r4_2": {"event_window": estimate(joined, in_window & health_valid, person["RTHLTH42"].ge(4).where(health_valid, np.nan)), "no_event_window": estimate(joined, no_event_window & health_valid, person["RTHLTH42"].ge(4).where(health_valid, np.nan))},
                "fair_or_poor_health_at_r3_1": {"event_window": estimate(joined, in_window & health_valid, person["RTHLTH31"].ge(4).where(health_valid, np.nan)), "no_event_window": estimate(joined, no_event_window & health_valid, person["RTHLTH31"].ge(4).where(health_valid, np.nan))},
                "health_worsened": {"event_window": estimate(joined, in_window & health_valid, health_worsened.where(health_valid, np.nan)), "no_event_window": estimate(joined, no_event_window & health_valid, health_worsened.where(health_valid, np.nan))},
                "health_improved": {"event_window": estimate(joined, in_window & health_valid, health_improved.where(health_valid, np.nan)), "no_event_window": estimate(joined, no_event_window & health_valid, health_improved.where(health_valid, np.nan))},
                "employment_loss": {"event_window": estimate(joined, in_window & employment_valid, employment_loss.where(employment_valid, np.nan)), "no_event_window": estimate(joined, no_event_window & employment_valid, employment_loss.where(employment_valid, np.nan))},
                "employment_gain": {"event_window": estimate(joined, in_window & employment_valid, employment_gain.where(employment_valid, np.nan)), "no_event_window": estimate(joined, no_event_window & employment_valid, employment_gain.where(employment_valid, np.nan))},
                "not_employed_at_r3_1": {"event_window": estimate(joined, in_window & employment_valid, (~employed_base).where(employment_valid, np.nan)), "no_event_window": estimate(joined, no_event_window & employment_valid, (~employed_base).where(employment_valid, np.nan))},
                "not_employed_at_r4_2": {"event_window": estimate(joined, in_window & employment_valid, (~employed_follow).where(employment_valid, np.nan)), "no_event_window": estimate(joined, no_event_window & employment_valid, (~employed_follow).where(employment_valid, np.nan))},
                "medical_bill_problem_at_r4_2": {"event_window": estimate(joined, in_window, (person["PROBPY42"] == 1).where(person["PROBPY42"].isin([1, 2]), np.nan)), "no_event_window": estimate(joined, no_event_window, (person["PROBPY42"] == 1).where(person["PROBPY42"].isin([1, 2]), np.nan))},
            },
        }
        output["events"][name] = event_output
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
