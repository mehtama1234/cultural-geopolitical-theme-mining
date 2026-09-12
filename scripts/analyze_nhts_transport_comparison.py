#!/usr/bin/env python3
"""Create the first weighted descriptive NHTS transport comparison."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


AREAS = {"01": "urban", "02": "rural"}
WORK_MODES = {
    "01": "car", "02": "van", "03": "suv", "04": "pickup",
    "08": "public bus", "09": "school bus", "10": "streetcar",
    "11": "subway", "12": "commuter rail", "13": "amtrak", "14": "airplane",
    "15": "taxi", "16": "rideshare", "17": "paratransit", "18": "bike",
    "19": "scooter", "20": "walk", "21": "other",
}


def rows(path: Path):
    with path.open(encoding="utf-8", newline="") as source:
        yield from csv.DictReader(source)


def weighted_share(records, weight, yes):
    denominator = sum(float(row[weight]) for row in records)
    numerator = sum(float(row[weight]) for row in records if yes(row))
    return {"weighted_yes": numerator, "weighted_total": denominator,
            "share_percent": round(100 * numerator / denominator, 2) if denominator else None,
            "records": len(records)}


def analyze(root: Path) -> dict:
    households = list(rows(root / "household-slice.csv"))
    people = list(rows(root / "person-slice.csv"))
    trips = list(rows(root / "trip-slice.csv"))
    household_area = {row["HOUSEID"]: row["URBRUR"] for row in households}

    result = {"format": "us-household-calendar-nhts-transport-comparison-v1",
              "source": "2022 NHTS CSV V2.1 public-use archive",
              "weighting": "final household/person/travel-day weights",
              "areas": {}}
    for area_code, area_name in AREAS.items():
        hh = [row for row in households if row["URBRUR"] == area_code]
        p = [row for row in people if household_area.get(row["HOUSEID"]) == area_code]
        valid_rideshare = [row for row in p if row["LAST30_RDSHR"] in {"01", "02"}]
        t = [row for row in trips if household_area.get(row["HOUSEID"]) == area_code and row["TRPTRANS"] in WORK_MODES]
        work = [row for row in t if row["WHYTRP90"] == "01"]
        all_ride = [row for row in t if row["TRPTRANS"] in {"15", "16"}]
        result["areas"][area_name] = {
            "household_count": len(hh),
            "zero_vehicle_households": weighted_share(hh, "WTHHFIN", lambda r: r["HHVEHCNT"] == "0"),
            "person_count": len(p),
            "used_rideshare_last_30_days": weighted_share(valid_rideshare, "WTPERFIN", lambda r: r["LAST30_RDSHR"] == "01"),
            "trip_count": len(t),
            "taxi_or_rideshare_all_trips": weighted_share(t, "WTTRDFIN", lambda r: r["TRPTRANS"] in {"15", "16"}),
            "work_trip_mode_share": {
                mode: weighted_share(work, "WTTRDFIN", lambda r, code=code: r["TRPTRANS"] == code)["share_percent"]
                for code, mode in WORK_MODES.items()
                if any(row["TRPTRANS"] == code for row in work)
            },
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

