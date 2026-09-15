#!/usr/bin/env python3
"""Condition PLACES county outcomes on HRSA primary-care HPSA component types."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path


MEASURES = {
    "transportation_insecurity": "Lack of reliable transportation in the past 12 months among adults",
    "food_insecurity": "Food insecurity in the past 12 months among adults",
    "housing_insecurity": "Housing insecurity in the past 12 months among adults",
    "utility_shutoff_threat": "Utility services shut-off threat in the past 12 months among adults",
    "frequent_mental_distress": "Frequent mental distress among adults",
    "lack_health_insurance": "Current lack of health insurance among adults aged 18-64 years",
    "routine_checkup": "Visits to doctor for routine checkup within the past year among adults",
}


def median(rows: list[dict[str, float]], key: str) -> float | None:
    values = [row[key] for row in rows if key in row]
    return round(statistics.median(values), 3) if values else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--places", type=Path, required=True)
    parser.add_argument("--hpsa", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    places: dict[str, dict[str, float]] = {}
    with args.places.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            key = next((key for key, label in MEASURES.items() if row.get("measure") == label), None)
            if key is None or len(row.get("locationid", "")) != 5:
                continue
            try:
                number = float(row["data_value"])
            except (KeyError, ValueError):
                continue
            places.setdefault(row["locationid"], {})[key] = number

    components: dict[str, dict[str, set[str]]] = {}
    row_counts: dict[str, int] = {}
    with args.hpsa.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row.get("HPSA Status") != "Designated" or row.get("HPSA Discipline Class") != "Primary Care":
                continue
            fips = row.get("State and County Federal Information Processing Standard Code", "")
            if fips not in places or len(fips) != 5:
                continue
            type_code = row.get("HPSA Type Code", "") or "Unknown"
            component_code = row.get("HPSA Component Type Code", "") or "Unknown"
            population_code = row.get("HPSA Population Type Code", "") or "Unknown"
            components.setdefault(fips, {"type": set(), "component": set(), "population": set()})
            components[fips]["type"].add(type_code)
            components[fips]["component"].add(component_code)
            components[fips]["population"].add(population_code)
            row_counts[fips] = row_counts.get(fips, 0) + 1

    groups = {
        "geographic_hpsa_type": {fips for fips, values in components.items() if "Hpsa Geo" in values["type"] or "Hpsa Geo HN" in values["type"]},
        "population_hpsa_type": {fips for fips, values in components.items() if "Hpsa Pop" in values["type"]},
        "facility_or_site_hpsa_type": {fips for fips, values in components.items() if values["type"] & {"RHC", "FQHC", "FQHC LAL", "ITU", "PRSN", "OFAC"}},
        "census_tract_component": {fips for fips, values in components.items() if "CT" in values["component"]},
        "single_county_or_subdivision_component": {fips for fips, values in components.items() if values["component"] & {"SCTY", "CSD"}},
        "low_income_population_code": {fips for fips, values in components.items() if values["population"] & {"LI", "LI-MFW", "LI-H-MFW"}},
        "migrant_or_seasonal_population_code": {fips for fips, values in components.items() if values["population"] & {"M", "MFW", "LI-MFW", "LI-H-MFW"}},
    }

    summaries = {}
    for group, fips_set in groups.items():
        rows = [places[fips] for fips in sorted(fips_set)]
        summaries[group] = {
            "counties": len(rows),
            "median_measures": {key: median(rows, key) for key in MEASURES},
            "median_designated_rows_per_county": round(statistics.median([row_counts[fips] for fips in fips_set]), 3) if fips_set else None,
        }

    result = {
        "format": "us-hpsa-component-places-diagnostic-v1",
        "source_unit": "US county with 2025 CDC PLACES modeled estimates and current HRSA designated primary-care HPSA component/type/population codes",
        "places_release": "2025 release; selected measures primarily based on 2023 BRFSS",
        "matched_counties_with_any_hpsa": len(components),
        "summaries": summaries,
        "method": "County FIPS association; a county can occur in multiple component/type/population groups. County medians are unweighted. HPSA rows and components are not summed into a county-wide resident exposure.",
        "boundary": "This is a component-level ecological diagnostic. HPSA component/type/population presence does not establish that all county residents are underserved, that a provider is reachable or accepts insurance, or that the designation caused PLACES outcomes. PLACES is modeled and HRSA is a current-vintage designation file.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"matched_counties_with_any_hpsa": len(components), "summaries": summaries}, indent=2))


if __name__ == "__main__":
    main()
