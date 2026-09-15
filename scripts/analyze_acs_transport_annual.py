#!/usr/bin/env python3
"""Read national ACS table-based summary files for vehicle access and commute time."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def national_row(path: Path) -> dict[str, str]:
    with path.open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source, delimiter="|"):
            if row.get("GEO_ID") == "0100000US":
                return row
    raise ValueError(f"national GEO_ID 0100000US not found in {path}")


def estimate(year_dir: Path) -> dict:
    vehicle = national_row(year_dir / "b08201.dat")
    commute = national_row(year_dir / "b08303.dat")
    households = int(vehicle["B08201_E001"])
    zero_vehicle = int(vehicle["B08201_E002"])
    workers = int(commute["B08303_E001"])
    thirty_plus = sum(int(commute[f"B08303_E{i:03d}"]) for i in range(8, 14))
    return {
        "households": households,
        "zero_vehicle_households": {"estimate": zero_vehicle, "share_percent": round(100 * zero_vehicle / households, 2)},
        "workers_not_working_from_home": workers,
        "commute_30_minutes_or_more": {"estimate": thirty_plus, "share_percent": round(100 * thirty_plus / workers, 2)},
        "tables": {"vehicle_access": "B08201", "travel_time_to_work": "B08303"},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--year-dir", action="append", required=True, help="YEAR=directory containing b08201.dat and b08303.dat")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    years = {}
    for item in args.year_dir:
        year_text, directory = item.split("=", 1)
        years[year_text] = estimate(Path(directory))
    result = {
        "format": "us-acs-transport-annual-national-v1",
        "source": "ACS 1-year table-based summary files",
        "unit": "national household estimate for B08201; national worker estimate not working from home for B08303",
        "years": years,
        "method": "Direct national rows from official table-based summary files; no API query, imputation, or cross-year person matching.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
