#!/usr/bin/env python3
"""Audit person/event keys and time surfaces across 2024 MEPS files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import pyreadstat


EVENT_SPECS = {
    "office": {"id": "EVNTIDX", "date": ["OBDATEYR", "OBDATEMM"], "payment": "OBSF24X"},
    "prescription": {"id": "RXRECIDX", "date": ["RXBEGYRX", "RXBEGMM"], "payment": "RXSF24X"},
    "emergency_room": {"id": "EVNTIDX", "date": ["ERDATEYR", "ERDATEMM"], "payment": "ERFSF24X"},
    "inpatient": {"id": "EVNTIDX", "date": ["IPBEGYR", "IPBEGMM"], "payment": "IPFSF24X"},
}


def read_columns(path: Path, columns: list[str]) -> pd.DataFrame:
    frame, _ = pyreadstat.read_dta(path, usecols=columns)
    return frame


def key_frame(frame: pd.DataFrame, id_field: str | None = None) -> pd.Series:
    base = frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)
    if id_field:
        return base + "|" + frame[id_field].astype(str)
    return base


def finite_count(frame: pd.DataFrame, field: str) -> int:
    return int(pd.to_numeric(frame[field], errors="coerce").notna().sum())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("office_file", type=Path)
    parser.add_argument("prescription_file", type=Path)
    parser.add_argument("emergency_room_file", type=Path)
    parser.add_argument("inpatient_file", type=Path)
    args = parser.parse_args()

    hc = read_columns(args.hc256_file, ["DUPERSID", "PANEL", "DATAYEAR", "PERWT24F"])
    person_keys = set(key_frame(hc))
    result: dict[str, object] = {
        "hc256": {
            "records": len(hc),
            "unique_person_panel_keys": int(key_frame(hc).nunique()),
            "positive_weight_records": int((hc["PERWT24F"] > 0).sum()),
            "data_year_values": sorted(pd.to_numeric(hc["DATAYEAR"], errors="coerce").dropna().unique().tolist()),
        },
        "events": {},
        "method": "Exact linkage uses DUPERSID and PANEL; event uniqueness uses the file-specific event identifier.",
    }

    paths = {
        "office": args.office_file,
        "prescription": args.prescription_file,
        "emergency_room": args.emergency_room_file,
        "inpatient": args.inpatient_file,
    }
    for name, path in paths.items():
        spec = EVENT_SPECS[name]
        columns = ["DUPERSID", "PANEL", "PERWT24F", spec["id"], *spec["date"], spec["payment"]]
        frame = read_columns(path, columns)
        person_panel = key_frame(frame)
        event_keys = key_frame(frame, spec["id"])
        year = pd.to_numeric(frame[spec["date"][0]], errors="coerce")
        month = pd.to_numeric(frame[spec["date"][1]], errors="coerce")
        # MEPS uses negative special codes in some event date fields. A valid
        # calendar date must be a plausible year and a 1--12 month, not merely
        # a nonmissing numeric value.
        valid_date = year.between(1900, 2024) & month.between(1, 12)
        result["events"][name] = {
            "file": str(path),
            "records": len(frame),
            "unique_person_panel_keys": int(person_panel.nunique()),
            "unique_event_keys": int(event_keys.nunique()),
            "duplicate_event_key_records": int(len(frame) - event_keys.nunique()),
            "person_panel_keys_found_in_hc256": int(person_panel.isin(person_keys).sum()),
            "person_panel_linkage_percent": round(100 * float(person_panel.isin(person_keys).mean()), 6),
            "positive_weight_records": int((frame["PERWT24F"] > 0).sum()),
            "date_fields": spec["date"],
            "date_complete_records": int(valid_date.sum()),
            "date_complete_percent": round(100 * float(valid_date.mean()), 6),
            "date_year_min": int(year[valid_date].min()) if valid_date.any() else None,
            "date_year_max": int(year[valid_date].max()) if valid_date.any() else None,
            "date_month_min": int(month[valid_date].min()) if valid_date.any() else None,
            "date_month_max": int(month[valid_date].max()) if valid_date.any() else None,
            "payment_field": spec["payment"],
            "payment_nonmissing_records": finite_count(frame, spec["payment"]),
        }

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
