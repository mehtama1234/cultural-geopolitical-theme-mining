#!/usr/bin/env python3
"""Join CDC PLACES county social-needs measures to CBP/HRSA context.

This is an ecological, cross-vintage diagnostic. It does not estimate whether
capacity or HPSA designation causes a county's modeled health/social-needs
measure.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import statistics
from pathlib import Path
from zipfile import ZipFile


MEASURES = {
    "transportation_insecurity": "Lack of reliable transportation in the past 12 months among adults",
    "food_insecurity": "Food insecurity in the past 12 months among adults",
    "housing_insecurity": "Housing insecurity in the past 12 months among adults",
    "utility_shutoff_threat": "Utility services shut-off threat in the past 12 months among adults",
    "frequent_mental_distress": "Frequent mental distress among adults",
    "lack_health_insurance": "Current lack of health insurance among adults aged 18-64 years",
    "routine_checkup": "Visits to doctor for routine checkup within the past year among adults",
}


def num(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def median(rows: list[dict[str, float]], key: str) -> float | None:
    values = [row[key] for row in rows if row.get(key) is not None]
    return round(statistics.median(values), 3) if values else None


def percentile(values: list[float], p: float) -> float:
    values = sorted(values)
    if not values:
        raise ValueError("no values")
    index = (len(values) - 1) * p
    low, high = int(index), min(int(index) + 1, len(values) - 1)
    return values[low] + (values[high] - values[low]) * (index - low)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--places", type=Path, required=True)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--hpsa", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    population = {}
    with args.population.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row.get("SUMLEV") == "050" and row.get("POPESTIMATE2023"):
                population[row["STATE"] + row["COUNTY"]] = num(row["POPESTIMATE2023"])

    hpsa = set()
    with args.hpsa.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            # HRSA's downloaded header spells out the FIPS concept as
            # "...Federal Information Processing Standard Code".
            fips = row.get("State and County Federal Information Processing Standard Code") or ""
            if row.get("HPSA Status") == "Designated" and len(fips) == 5 and fips.isdigit() and row.get("State Abbreviation") not in {"PR", "VI", "GU", "AS", "MP"}:
                hpsa.add(fips)

    capacity = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                if row.get("naics") != "62----":
                    continue
                fips = row.get("fipstate", "") + row.get("fipscty", "")
                est = num(row.get("est", ""))
                emp = num(row.get("emp", ""))
                if fips in population and est is not None and population[fips]:
                    capacity[fips] = {
                        "health_est_per_10k": 10000 * est / population[fips],
                        "health_emp_per_10k": 10000 * emp / population[fips] if emp is not None else None,
                    }

    rows_by_fips: dict[str, dict[str, float]] = {}
    with args.places.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            fips = row.get("locationid", "")
            key = next((key for key, label in MEASURES.items() if row.get("measure") == label), None)
            value = num(row.get("data_value", ""))
            if len(fips) != 5 or value is None or fips not in capacity:
                continue
            rows_by_fips.setdefault(fips, {"fips": fips})[key] = value

    rows = []
    for fips, row in rows_by_fips.items():
        row["hpsa_component_present"] = fips in hpsa
        row.update(capacity[fips])
        rows.append(row)

    cap_values = [row["health_est_per_10k"] for row in rows]
    cut1, cut3 = percentile(cap_values, 0.25), percentile(cap_values, 0.75)
    for row in rows:
        row["capacity_band"] = "low" if row["health_est_per_10k"] <= cut1 else "high" if row["health_est_per_10k"] >= cut3 else "middle"

    summaries = {}
    for label, selected in {
        "hpsa_component_present": [row for row in rows if row["hpsa_component_present"]],
        "no_hpsa_component_present": [row for row in rows if not row["hpsa_component_present"]],
        "low_health_establishment_capacity": [row for row in rows if row["capacity_band"] == "low"],
        "high_health_establishment_capacity": [row for row in rows if row["capacity_band"] == "high"],
    }.items():
        summaries[label] = {
            "counties": len(selected),
            "median_health_est_per_10k": median(selected, "health_est_per_10k"),
            "median_health_emp_per_10k": median(selected, "health_emp_per_10k"),
            "median_measures": {key: median(selected, key) for key in MEASURES},
        }

    result = {
        "format": "us-places-hpsa-outcomes-diagnostic-v1",
        "source_unit": "US county; CDC PLACES modeled county estimate joined to 2023 CBP health/social-assistance capacity, 2023 population, and current HRSA primary-care HPSA component presence",
        "places_year": "2022 BRFSS-based 2024 release",
        "matched_counties": len(rows),
        "hpsa_counties": sum(row["hpsa_component_present"] for row in rows),
        "capacity_quartile_cutpoints": {"p25_health_est_per_10k": round(cut1, 3), "p75_health_est_per_10k": round(cut3, 3)},
        "measure_labels": MEASURES,
        "summaries": summaries,
        "method": "County FIPS join; unweighted county medians within HPSA and visible-capacity groups. PLACES estimates are modeled small-area estimates; CBP is employer establishment stock; HRSA is a current designation file and may cover a component rather than a whole county.",
        "boundary": "Ecological and cross-vintage diagnostic only. It does not establish individual access, appointment wait, quality, accepted insurance, provider workload, travel, unmet need, causal HPSA/capacity effects, health outcomes, trust, political meaning, or household response. The health-insurance denominator differs from other adult measures and no pooled welfare index is constructed.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"matched_counties": len(rows), "hpsa_counties": result["hpsa_counties"], "summaries": summaries}, indent=2))


if __name__ == "__main__":
    main()
