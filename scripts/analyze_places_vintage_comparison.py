#!/usr/bin/env python3
"""Compare selected CDC PLACES county measures across the 2024 and 2025 releases."""

from __future__ import annotations

import argparse
import csv
import io
import json
import statistics
from pathlib import Path
from zipfile import ZipFile


MEASURES = [
    "Lack of reliable transportation in the past 12 months among adults",
    "Food insecurity in the past 12 months among adults",
    "Housing insecurity in the past 12 months among adults",
    "Utility services shut-off threat in the past 12 months among adults",
    "Frequent mental distress among adults",
    "Current lack of health insurance among adults aged 18-64 years",
    "Visits to doctor for routine checkup within the past year among adults",
]


def value(raw: str) -> float | None:
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


def read_places(path: Path) -> dict[str, dict[str, float]]:
    result: dict[str, dict[str, float]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            measure = row.get("measure", "")
            if measure not in MEASURES:
                continue
            number = value(row.get("data_value", ""))
            fips = row.get("locationid", "")
            if number is not None and len(fips) == 5:
                result.setdefault(fips, {})[measure] = number
    return result


def median(rows: list[dict[str, float]], measure: str) -> float | None:
    vals = [row[measure] for row in rows if measure in row]
    return round(statistics.median(vals), 3) if vals else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--places-2024", type=Path, required=True)
    parser.add_argument("--places-2025", type=Path, required=True)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    population = {}
    with args.population.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row.get("SUMLEV") == "050" and row.get("POPESTIMATE2023"):
                population[row["STATE"] + row["COUNTY"]] = value(row["POPESTIMATE2023"])

    capacity = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                if row.get("naics") != "62----":
                    continue
                fips = row.get("fipstate", "") + row.get("fipscty", "")
                est = value(row.get("est", ""))
                if fips in population and est is not None and population[fips]:
                    capacity[fips] = 10000 * est / population[fips]

    old, new = read_places(args.places_2024), read_places(args.places_2025)
    common = sorted(set(old) & set(new) & set(capacity))
    cap_values = sorted(capacity[fips] for fips in common)
    p25 = cap_values[int((len(cap_values) - 1) * 0.25)]
    p75 = cap_values[int((len(cap_values) - 1) * 0.75)]
    groups = {
        "all_common_counties": common,
        "low_capacity": [fips for fips in common if capacity[fips] <= p25],
        "high_capacity": [fips for fips in common if capacity[fips] >= p75],
    }
    summary = {}
    for group, fips_list in groups.items():
        summary[group] = {"counties": len(fips_list), "measures": {}}
        for measure in MEASURES:
            old_rows = [old[fips] for fips in fips_list]
            new_rows = [new[fips] for fips in fips_list]
            old_median, new_median = median(old_rows, measure), median(new_rows, measure)
            summary[group]["measures"][measure] = {
                "2024_median": old_median,
                "2025_median": new_median,
                "median_change": round(new_median - old_median, 3) if old_median is not None and new_median is not None else None,
                "2024_available": sum(measure in row for row in old_rows),
                "2025_available": sum(measure in row for row in new_rows),
            }

    result = {
        "format": "us-places-vintage-comparison-v1",
        "source_unit": "Same county FIPS where present in both selected PLACES releases, with CBP health-establishment capacity context",
        "matched_counties": len(common),
        "capacity_cutpoints": {"p25_health_est_per_10k": round(p25, 3), "p75_health_est_per_10k": round(p75, 3)},
        "release_context": {"2024": "2022 BRFSS-based release, with selected measures using 2022 BRFSS", "2025": "2023 BRFSS-based release for the selected measures, using Census 2023 population estimates"},
        "summary": summary,
        "method": "FIPS intersection; capacity groups defined on common counties; unweighted county medians, paired by county for availability but not treated as a panel of people. PLACES small-area estimates and measure definitions/releases are not assumed identical without review.",
        "boundary": "This is a descriptive vintage comparison. It does not estimate change for the same residents, effects of capacity, or health-policy impact. The 2024/2025 releases use different BRFSS and Census inputs, and PLACES documentation warns that the small-area model cannot detect effects of local interventions.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"matched_counties": len(common), "summary": summary}, indent=2))


if __name__ == "__main__":
    main()
