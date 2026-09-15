#!/usr/bin/env python3
"""Build a reproducible NHTS mobility/material/work-and-daily-life screen."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


AREAS = {"01": "urban", "02": "rural"}
INCOME_BANDS = {
    "01-03": {"label": "under_35k", "codes": {"01", "02", "03"}},
    "04-05": {"label": "35k_to_74k", "codes": {"04", "05"}},
    "06-08": {"label": "75k_or_more", "codes": {"06", "07", "08"}},
}


def rows(path: Path):
    with path.open(encoding="utf-8", newline="") as source:
        yield from csv.DictReader(source)


def number(value: str):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def share(records, weight, predicate):
    valid = [(row, number(row[weight])) for row in records]
    valid = [(row, w) for row, w in valid if w is not None and w > 0]
    total = sum(w for _, w in valid)
    yes = sum(w for row, w in valid if predicate(row))
    return {"share_percent": round(100 * yes / total, 2) if total else None,
            "weighted_total": round(total, 2), "records": len(valid)}


def weighted_mean(records, weight, value_field, predicate=lambda row: True):
    pairs = []
    for row in records:
        weight_value = number(row[weight])
        value = number(row[value_field])
        if weight_value is not None and weight_value > 0 and value is not None and value >= 0 and predicate(row):
            pairs.append((weight_value, value))
    total = sum(w for w, _ in pairs)
    return {"mean": round(sum(w * value for w, value in pairs) / total, 2) if total else None,
            "weighted_total": round(total, 2), "records": len(pairs)}


def analyze(root: Path) -> dict:
    households = list(rows(root / "household-slice.csv"))
    people = list(rows(root / "person-slice.csv"))
    trips = list(rows(root / "trip-slice.csv"))
    household = {row["HOUSEID"]: row for row in households}
    result = {
        "format": "us-household-calendar-nhts-mobility-material-work-care-v1",
        "source": "2022 NHTS CSV V2.1 public-use archive",
        "weighting": "WTHHFIN for household measures; WTTRDFIN for recorded travel-day trip measures",
        "income_band_definition": "NHTS HHFAMINC codes 01-03, 04-05, and 06-08 are grouped as under $35k, $35k-$74k, and $75k or more; -7/-8 excluded.",
        "purpose_definition": "Work trips are WHYTRP90=01. Shopping trips are TRIPPURP=04; these are daily-life activity proxies, not a complete care measure.",
        "cells": {},
    }
    for area_code, area_name in AREAS.items():
        for band_code, band in INCOME_BANDS.items():
            key = f"{area_name}:{band['label']}"
            hh = [r for r in households if r["URBRUR"] == area_code and r["HHFAMINC"] in band["codes"]]
            ids = {r["HOUSEID"] for r in hh}
            p = [r for r in people if r["HOUSEID"] in ids and r["WORKER"] == "01"]
            t = [r for r in trips if r["HOUSEID"] in ids]
            work = [r for r in t if r["WHYTRP90"] == "01"]
            shopping = [r for r in t if r["TRIPPURP"] == "04"]
            result["cells"][key] = {
                "area": area_name,
                "income_band": band["label"],
                "households": len(hh),
                "zero_vehicle_households": share(hh, "WTHHFIN", lambda r: r["HHVEHCNT"] == "0"),
                "worker_households_with_fewer_vehicles_than_workers": share(hh, "WTHHFIN", lambda r: number(r["WRKCOUNT"]) is not None and number(r["HHVEHCNT"]) is not None and number(r["WRKCOUNT"]) > number(r["HHVEHCNT"])),
                "worker_count": len(p),
                "mean_worker_work_distance_miles": weighted_mean(p, "WTPERFIN", "GCDWORK"),
                "work_trip_mean_minutes": weighted_mean(work, "WTTRDFIN", "TRVLCMIN"),
                "work_trips_30_minutes_or_more": share(work, "WTTRDFIN", lambda r: number(r["TRVLCMIN"]) is not None and number(r["TRVLCMIN"]) >= 30),
                "shopping_trip_mean_minutes": weighted_mean(shopping, "WTTRDFIN", "TRVLCMIN"),
                "shopping_trips_30_minutes_or_more": share(shopping, "WTTRDFIN", lambda r: number(r["TRVLCMIN"]) is not None and number(r["TRVLCMIN"]) >= 30),
            }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slice-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.slice_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
