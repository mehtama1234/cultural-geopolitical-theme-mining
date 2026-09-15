#!/usr/bin/env python3
"""Audit MEPS round reference periods against dated event records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import pyreadstat


ROUND_FIELDS = {
    "R3_1": ("ENDRFY31", "ENDRFM31", "EMPST31", "RTHLTH31"),
    "R4_2": ("ENDRFY42", "ENDRFM42", "EMPST42", "RTHLTH42"),
    "R5_3": ("ENDRFY53", "ENDRFM53", "EMPST53", "RTHLTH53"),
    "FULL_YEAR": ("ENDRFY24", "ENDRFM24", "EMPST53", "RTHLTH53"),
}

EVENTS = {
    "office": ("EVNTIDX", "OBDATEYR", "OBDATEMM"),
    "emergency_room": ("EVNTIDX", "ERDATEYR", "ERDATEMM"),
    "inpatient": ("EVNTIDX", "IPBEGYR", "IPBEGMM"),
}


def read(path: Path, columns: list[str]) -> pd.DataFrame:
    frame, _ = pyreadstat.read_dta(path, usecols=columns)
    return frame


def key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def valid_month(year: pd.Series, month: pd.Series) -> pd.Series:
    return year.between(1900, 2030) & month.between(1, 12)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person_columns = ["DUPERSID", "PANEL"]
    for fields in ROUND_FIELDS.values():
        person_columns.extend(fields)
    person = read(args.hc256_file, list(dict.fromkeys(person_columns)))
    person["PERSON_KEY"] = key(person)
    lookup = person.set_index("PERSON_KEY")
    output: dict[str, object] = {
        "schema": "us-meps-2024-round-timing-audit-v1",
        "method": "Event month is compared with HC-256 round reference-period end month after exact DUPERSID + PANEL linkage. This is temporal context, not interview-date or causal follow-up.",
        "person_records": len(person),
        "rounds": {},
        "events": {},
    }

    for round_name, fields in ROUND_FIELDS.items():
        year_field, month_field, employment_field, health_field = fields
        year = pd.to_numeric(person[year_field], errors="coerce")
        month = pd.to_numeric(person[month_field], errors="coerce")
        valid = valid_month(year, month)
        output["rounds"][round_name] = {
            "year_field": year_field,
            "month_field": month_field,
            "valid_date_records": int(valid.sum()),
            "valid_date_percent": round(100 * float(valid.mean()), 6),
            "year_min": int(year[valid].min()) if valid.any() else None,
            "year_max": int(year[valid].max()) if valid.any() else None,
            "employment_field": employment_field,
            "health_field": health_field,
        }

    for name, path in {
        "office": args.office_file,
        "emergency_room": args.emergency_room_file,
        "inpatient": args.inpatient_file,
    }.items():
        event_id, year_field, month_field = EVENTS[name]
        event = read(path, ["DUPERSID", "PANEL", event_id, year_field, month_field])
        event["PERSON_KEY"] = key(event)
        merged = event.merge(lookup, left_on="PERSON_KEY", right_index=True, how="left", validate="many_to_one")
        event_year = pd.to_numeric(merged[year_field], errors="coerce")
        event_month = pd.to_numeric(merged[month_field], errors="coerce")
        event_valid = valid_month(event_year, event_month)
        event_month_index = event_year * 12 + event_month
        comparison: dict[str, object] = {}
        for round_name, fields in ROUND_FIELDS.items():
            round_year = pd.to_numeric(merged[fields[0]], errors="coerce")
            round_month = pd.to_numeric(merged[fields[1]], errors="coerce")
            round_valid = valid_month(round_year, round_month)
            usable = event_valid & round_valid
            delta = event_month_index - (round_year * 12 + round_month)
            comparison[round_name] = {
                "round_date_valid_records": int(round_valid.sum()),
                "both_event_and_round_date_records": int(usable.sum()),
                "event_before_round_end": int((delta < 0)[usable].sum()),
                "event_same_month_as_round_end": int((delta == 0)[usable].sum()),
                "event_after_round_end": int((delta > 0)[usable].sum()),
            }
        output["events"][name] = {
            "event_records": len(event),
            "unique_event_keys": int((key(event) + "|" + event[event_id].astype(str)).nunique()),
            "valid_event_date_records": int(event_valid.sum()),
            "valid_event_date_percent": round(100 * float(event_valid.mean()), 6),
            "round_comparisons": comparison,
            "limitation": "Round reference-period end dates do not establish an interview date, event-trigger date, or post-event outcome window.",
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
