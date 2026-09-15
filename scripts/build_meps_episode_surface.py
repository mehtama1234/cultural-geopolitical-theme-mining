#!/usr/bin/env python3
"""Build an aggregate, bounded MEPS 2024 person/event episode surface."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


EVENT_SPECS = {
    "office": {
        "id": "EVNTIDX",
        "date_year": "OBDATEYR",
        "date_month": "OBDATEMM",
        "self_payment": ["OBSF24X"],
        "total_payment": ["OBXP24X"],
    },
    "emergency_room": {
        "id": "EVNTIDX",
        "date_year": "ERDATEYR",
        "date_month": "ERDATEMM",
        "self_payment": ["ERFSF24X", "ERDSF24X"],
        "total_payment": ["ERFXP24X", "ERDXP24X"],
    },
    "inpatient": {
        "id": "EVNTIDX",
        "date_year": "IPBEGYR",
        "date_month": "IPBEGMM",
        "self_payment": ["IPFSF24X", "IPDSF24X"],
        "total_payment": ["IPFXP24X", "IPDXP24X"],
    },
}

PERSON_FIELDS = [
    "DUPERSID", "PANEL", "PERWT24F", "INSURC24", "POVCAT24", "FAMINC24",
    "EMPST53", "RTHLTH53", "PROBPY42",
]


def read(path: Path, columns: list[str]) -> pd.DataFrame:
    frame, _ = pyreadstat.read_dta(path, usecols=columns)
    return frame


def make_key(frame: pd.DataFrame, event_id: str | None = None) -> pd.Series:
    key = frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)
    if event_id:
        key = key + "|" + frame[event_id].astype(str)
    return key


def weighted_mean(values: pd.Series, weights: pd.Series) -> float | None:
    x = pd.to_numeric(values, errors="coerce").to_numpy(float)
    w = pd.to_numeric(weights, errors="coerce").to_numpy(float)
    valid = np.isfinite(x) & np.isfinite(w) & (w > 0)
    if not valid.any() or float(w[valid].sum()) == 0:
        return None
    return float(np.sum(x[valid] * w[valid]) / np.sum(w[valid]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person = read(args.hc256_file, PERSON_FIELDS)
    person["PERSON_KEY"] = make_key(person)
    person_lookup = person.set_index("PERSON_KEY")
    paths = {
        "office": args.office_file,
        "emergency_room": args.emergency_room_file,
        "inpatient": args.inpatient_file,
    }
    output: dict[str, object] = {
        "schema": "us-meps-2024-episode-surface-v1",
        "source": "AHRQ MEPS 2024 HC-256 and HC-254 event public-use files",
        "method": {
            "linkage": "exact DUPERSID + PANEL join from event record to HC-256 person record",
            "valid_event": "positive PERWT24F, valid date year 1900-2024/month 1-12, and nonmissing self/family payment",
            "weighting": "event-file PERWT24F for event payment means; counts remain unweighted record counts unless labeled weighted",
            "privacy": "aggregate output only; no person identifiers or row-level records are written",
        },
        "person_file": {
            "records": len(person),
            "unique_person_panel_keys": int(person["PERSON_KEY"].nunique()),
            "positive_weight_records": int((person["PERWT24F"] > 0).sum()),
        },
        "events": {},
    }

    for name, path in paths.items():
        spec = EVENT_SPECS[name]
        event_fields = [
            "DUPERSID", "PANEL", "PERWT24F", spec["id"], spec["date_year"],
            spec["date_month"], *spec["self_payment"], *spec["total_payment"],
        ]
        event = read(path, event_fields)
        event["PERSON_KEY"] = make_key(event)
        merged = event.merge(
            person_lookup.drop(columns=["DUPERSID", "PANEL", "PERWT24F"]),
            left_on="PERSON_KEY", right_index=True, how="left", validate="many_to_one",
            indicator=True,
        )
        year = pd.to_numeric(merged[spec["date_year"]], errors="coerce")
        month = pd.to_numeric(merged[spec["date_month"]], errors="coerce")
        self_payment = merged[spec["self_payment"]].apply(pd.to_numeric, errors="coerce").sum(axis=1, min_count=1)
        total_payment = merged[spec["total_payment"]].apply(pd.to_numeric, errors="coerce").sum(axis=1, min_count=1)
        valid = (
            (pd.to_numeric(merged["PERWT24F"], errors="coerce") > 0)
            & year.between(1900, 2024)
            & month.between(1, 12)
            & self_payment.notna()
            & (merged["_merge"] == "both")
        )
        context_fields = ["INSURC24", "POVCAT24", "EMPST53", "RTHLTH53", "PROBPY42"]
        context_counts = {
            field: int(merged.loc[valid, field].notna().sum()) for field in context_fields
        }
        valid_frame = merged.loc[valid]
        output["events"][name] = {
            "source_file": str(path),
            "event_records": len(event),
            "unique_event_keys": int(make_key(event, spec["id"]).nunique()),
            "exact_person_panel_matches": int((merged["_merge"] == "both").sum()),
            "exact_person_panel_match_percent": round(100 * float((merged["_merge"] == "both").mean()), 6),
            "valid_episode_surface_records": int(valid.sum()),
            "unique_people_in_valid_surface": int(valid_frame["PERSON_KEY"].nunique()),
            "date_complete_records": int((year.between(1900, 2024) & month.between(1, 12)).sum()),
            "payment_complete_records": int(self_payment.notna().sum()),
            "positive_weight_records": int((pd.to_numeric(event["PERWT24F"], errors="coerce") > 0).sum()),
            "date_year_min": int(year[valid].min()) if valid.any() else None,
            "date_year_max": int(year[valid].max()) if valid.any() else None,
            "weighted_mean_self_family_payment": weighted_mean(self_payment[valid], valid_frame["PERWT24F"]),
            "weighted_mean_total_payment": weighted_mean(total_payment[valid], valid_frame["PERWT24F"]),
            "zero_self_family_payment_records": int((self_payment[valid] == 0).sum()),
            "context_nonmissing_records": context_counts,
            "context_nonmissing_percent": {
                field: round(100 * value / int(valid.sum()), 6) if valid.any() else None
                for field, value in context_counts.items()
            },
            "coverage_code_counts": {
                str(int(code)): int(count)
                for code, count in valid_frame["INSURC24"].value_counts(dropna=False).items()
                if pd.notna(code)
            },
            "limitation": "Event records represent observed events and exclude people with no event in this file; annual context is not a dated causal follow-up.",
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
