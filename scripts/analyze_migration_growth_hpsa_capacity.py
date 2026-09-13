#!/usr/bin/env python3
"""Compare county growth quartiles by HPSA status and visible capacity."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path


FIELDS = {
    "growth": "pop_change_pct",
    "health_establishments": "health_est_per_10k",
    "health_employment": "health_emp_per_10k",
    "retail_establishments": "retail_est_per_10k",
    "rent": "median_gross_rent_acs5_2023",
}


def median(rows: list[dict[str, str]], field: str) -> float | None:
    values = []
    for row in rows:
        try:
            values.append(float(row[field]))
        except (KeyError, TypeError, ValueError):
            continue
    return statistics.median(values) if values else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panel", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    by_fips = {}
    with args.panel.open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source, delimiter="\t"):
            by_fips[row["fips"]] = row
    rows = sorted(by_fips.values(), key=lambda row: float(row["pop_change_pct"]))
    for index, row in enumerate(rows):
        row["growth_quartile"] = str(index * 4 // len(rows) + 1)
    results = {}
    for quartile in range(1, 5):
        results[str(quartile)] = {}
        for hpsa in ("yes", "no"):
            group = [row for row in rows if row["growth_quartile"] == str(quartile)
                     and row.get("hpsa", "").lower() == hpsa]
            results[str(quartile)][hpsa] = {
                "counties": len(group),
                **{name: median(group, field) for name, field in FIELDS.items()},
            }
    result = {
        "format": "us-migration-growth-hpsa-capacity-v1",
        "source_unit": "US county with population >=100,000, 2020-2023 population estimates, ACS/CBP/HPSA context",
        "unique_counties": len(rows),
        "growth_quartiles": "equal-count quartiles of 2020-2023 population change",
        "results": results,
        "causal_estimation": False,
        "boundary": "HPSA is a designated shortage-context flag and CBP capacity is visible establishment/employment stock; neither is a complete service-access or unmet-need measure.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"unique_counties": len(rows), "growth_quartiles": 4}, indent=2))


if __name__ == "__main__":
    main()
