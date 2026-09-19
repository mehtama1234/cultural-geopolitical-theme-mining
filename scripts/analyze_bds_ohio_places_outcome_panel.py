#!/usr/bin/env python3
"""Add retained CDC PLACES modeled outcomes to the bounded Ohio BDS panel."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import statistics
from pathlib import Path

from analyze_bds_ohio_mobility_panel import SECTORS, numeric, read_table


MEASURES = {
    "routine_checkup": "Visits to doctor for routine checkup within the past year among adults",
    "transportation_insecurity": "Lack of reliable transportation in the past 12 months among adults",
    "food_insecurity": "Food insecurity in the past 12 months among adults",
    "frequent_mental_distress": "Frequent mental distress among adults",
    "lack_health_insurance": "Current lack of health insurance among adults aged 18-64 years",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bds-suffix", type=Path, required=True)
    parser.add_argument("--vehicle", type=Path, required=True)
    parser.add_argument("--commute", type=Path, required=True)
    parser.add_argument("--places", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    vehicle, commute = read_table(args.vehicle, "B08201"), read_table(args.commute, "B08303")
    mobility: dict[str, dict[str, float]] = {}
    for fips in sorted(set(vehicle) & set(commute)):
        v, c = vehicle[fips], commute[fips]
        households, workers = v.get("B08201_E001"), c.get("B08303_E001")
        if not households or not workers:
            continue
        mobility[fips] = {
            "zero_vehicle_pct": 100 * v.get("B08201_E002", 0) / households,
            "long_commute_pct": 100 * sum(c.get(f"B08303_E{i:03d}", 0) for i in range(8, 14)) / workers,
        }

    bds: dict[str, dict[str, float]] = {}
    with args.bds_suffix.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle):
            if len(row) < 28 or row[0] != "2023" or row[1] != "39" or row[3] not in SECTORS:
                continue
            fips = row[1] + row[2]
            if fips not in mobility:
                continue
            net = numeric(row[23])
            if net is not None:
                bds.setdefault(fips, {})[row[3]] = net

    places: dict[str, dict[str, float]] = {}
    with args.places.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            if row.get("stateabbr") != "OH" or row.get("data_value_type") != "Age-adjusted prevalence":
                continue
            key = next((name for name, label in MEASURES.items() if row.get("measure") == label), None)
            fips, value = row.get("locationid", ""), numeric(row.get("data_value", ""))
            if key and len(fips) == 5 and value is not None:
                places.setdefault(fips, {})[key] = value

    counties = sorted(f for f in set(mobility) & set(bds) & set(places) if len(bds[f]) == len(SECTORS) and len(places[f]) == len(MEASURES))
    cut = statistics.median(mobility[f]["zero_vehicle_pct"] for f in counties)
    groups = {
        "low_zero_vehicle": [f for f in counties if mobility[f]["zero_vehicle_pct"] < cut],
        "high_zero_vehicle": [f for f in counties if mobility[f]["zero_vehicle_pct"] >= cut],
    }

    def medians(fips_list: list[str]) -> dict[str, float | int]:
        out: dict[str, float | int] = {"county_count": len(fips_list)}
        for key in MEASURES:
            out[key] = round(statistics.median(places[f][key] for f in fips_list), 3) if fips_list else None
        return out

    interaction: dict[str, dict[str, float | int]] = {}
    for mobility_group, fips_list in groups.items():
        for flow_group, selected in {
            "negative_health_flow": [f for f in fips_list if bds[f]["62"] < 0],
            "nonnegative_health_flow": [f for f in fips_list if bds[f]["62"] >= 0],
        }.items():
            interaction[f"{mobility_group}__{flow_group}"] = medians(selected)

    output = {
        "audit_type": "bds-ohio-places-outcome-panel-v1",
        "checked": "2026-09-18",
        "unit": "Ohio county, 2023 BDS sector flow + 2023 ACS mobility context + CDC PLACES 2025 modeled county estimates (data year 2023)",
        "geography": "Ohio counties (state FIPS 39)",
        "selected_sectors": SECTORS,
        "selected_places_measures": MEASURES,
        "sources": {
            "bds_url": "https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv",
            "acs_vehicle_url": "https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08201.dat",
            "acs_commute_url": "https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08303.dat",
            "places_url": "https://data.cdc.gov/d/swc5-untb",
        },
        "retrieval": {
            "bds_suffix_sha256": hashlib.sha256(args.bds_suffix.read_bytes()).hexdigest(),
            "acs_vehicle_sha256": hashlib.sha256(args.vehicle.read_bytes()).hexdigest(),
            "acs_commute_sha256": hashlib.sha256(args.commute.read_bytes()).hexdigest(),
            "places_sha256": hashlib.sha256(args.places.read_bytes()).hexdigest(),
        },
        "matched_counties": len(counties),
        "zero_vehicle_median_cut_pct": round(cut, 3),
        "mobility_groups": {group: {"county_count": len(fips_list), **medians(fips_list)} for group, fips_list in groups.items()},
        "health_flow_mobility_interaction": interaction,
        "counterexample_county": {"fips": "39089", "health_net_job_creation_rate": bds.get("39089", {}).get("62"), "zero_vehicle_pct": round(mobility.get("39089", {}).get("zero_vehicle_pct", 0), 3), "places": places.get("39089", {})},
        "boundary": "PLACES values are modeled county estimates and are not patient episodes, provider availability, completed care, or causal outcomes. BDS and ACS are county aggregates; this is a same-year ecological comparison with no same-resident linkage. Disclosure values and unavailable estimates are excluded, not treated as zero.",
        "raw_storage": "BDS and ACS inputs were transient; retained PLACES file was read locally",
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
