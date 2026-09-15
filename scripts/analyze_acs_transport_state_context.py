#!/usr/bin/env python3
"""Build an ACS state transportation context conditioned by state income."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_table(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as source:
        return {row["GEO_ID"]: row for row in csv.DictReader(source, delimiter="|") if row.get("GEO_ID", "").startswith("0400000US")}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vehicle", type=Path, required=True)
    parser.add_argument("--commute", type=Path, required=True)
    parser.add_argument("--income", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    vehicle, commute, income = map(read_table, (args.vehicle, args.commute, args.income))
    states = []
    for geo_id in sorted(vehicle.keys() & commute.keys() & income.keys()):
        try:
            households = int(vehicle[geo_id]["B08201_E001"])
            zero_vehicle = int(vehicle[geo_id]["B08201_E002"])
            workers = int(commute[geo_id]["B08303_E001"])
            long_commute = sum(int(commute[geo_id][f"B08303_E{i:03d}"]) for i in range(8, 14))
            median_income = int(income[geo_id]["B19013_E001"])
        except (KeyError, ValueError):
            continue
        if households and workers and median_income > 0:
            states.append({"geo_id": geo_id, "median_household_income": median_income, "households": households, "zero_vehicle": zero_vehicle, "workers": workers, "long_commute": long_commute})
    states.sort(key=lambda row: (row["median_household_income"], row["geo_id"]))
    for index, row in enumerate(states):
        row["income_quartile"] = min(4, index * 4 // len(states) + 1)
    summary = {}
    for quartile in range(1, 5):
        rows = [row for row in states if row["income_quartile"] == quartile]
        households = sum(row["households"] for row in rows)
        workers = sum(row["workers"] for row in rows)
        summary[str(quartile)] = {
            "states": len(rows),
            "median_income_range": [min(row["median_household_income"] for row in rows), max(row["median_household_income"] for row in rows)],
            "zero_vehicle_households_share_percent": round(100 * sum(row["zero_vehicle"] for row in rows) / households, 2),
            "commute_30_minutes_or_more_share_percent": round(100 * sum(row["long_commute"] for row in rows) / workers, 2),
            "households": households,
            "workers_not_working_from_home": workers,
        }
    result = {"format": "us-acs-transport-state-income-context-v1", "source": "2024 ACS 1-year table-based summary files", "state_count": len(states), "income_quartile_definition": "52 state/DC/PR geographic rows sorted by B19013 median household income; quartiles are four equal-count groups; pooled measures are weighted by table totals.", "quartiles": summary, "states": states}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
