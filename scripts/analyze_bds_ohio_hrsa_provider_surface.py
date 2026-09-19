#!/usr/bin/env python3
"""Add the current Ohio primary-care HPSA component surface to the county panel."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import statistics
from pathlib import Path

from analyze_bds_ohio_mobility_panel import read_table


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vehicle", type=Path, required=True)
    parser.add_argument("--commute", type=Path, required=True)
    parser.add_argument("--hrsa", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    vehicle, commute = read_table(args.vehicle, "B08201"), read_table(args.commute, "B08303")
    mobility: dict[str, dict[str, float]] = {}
    for fips in sorted(set(vehicle) & set(commute)):
        v, c = vehicle[fips], commute[fips]
        households, workers = v.get("B08201_E001"), c.get("B08303_E001")
        if households and workers:
            mobility[fips] = {
                "zero_vehicle_pct": 100 * v.get("B08201_E002", 0) / households,
                "long_commute_pct": 100 * sum(c.get(f"B08303_E{i:03d}", 0) for i in range(8, 14)) / workers,
            }

    components: dict[str, list[dict[str, object]]] = {fips: [] for fips in mobility}
    with args.hrsa.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            fips = row.get("Common State County FIPS Code", "")
            if fips not in components or row.get("HPSA Status") != "Designated":
                continue
            fte = None
            try:
                fte = float(row.get("HPSA FTE", ""))
            except (TypeError, ValueError):
                pass
            components[fips].append({
                "hpsa_id": row.get("HPSA ID"),
                "designation_type": row.get("Designation Type"),
                "component_type": row.get("HPSA Component Type Description"),
                "fte": fte,
                "population_type": row.get("HPSA Population Type"),
            })

    counties = sorted(mobility)
    cut = statistics.median(mobility[f]["zero_vehicle_pct"] for f in counties)
    groups = {"low_zero_vehicle": [f for f in counties if mobility[f]["zero_vehicle_pct"] < cut], "high_zero_vehicle": [f for f in counties if mobility[f]["zero_vehicle_pct"] >= cut]}

    def summarize(fips_list: list[str]) -> dict[str, object]:
        rows = [row for fips in fips_list for row in components[fips]]
        designated_counties = [f for f in fips_list if components[f]]
        ftes = [float(row["fte"]) for row in rows if row["fte"] is not None]
        return {
            "county_count": len(fips_list),
            "counties_with_designated_component": len(designated_counties),
            "designated_component_rows": len(rows),
            "distinct_hpsa_ids": len({row["hpsa_id"] for row in rows}),
            "component_type_rows": {key: sum(row["component_type"] == key for row in rows) for key in sorted({str(row["component_type"]) for row in rows})},
            "rows_with_reported_fte": len(ftes),
            "median_reported_fte_per_component": round(statistics.median(ftes), 4) if ftes else None,
            "median_zero_vehicle_pct": round(statistics.median(mobility[f]["zero_vehicle_pct"] for f in fips_list), 3),
            "median_long_commute_pct": round(statistics.median(mobility[f]["long_commute_pct"] for f in fips_list), 3),
        }

    all_rows = [row for fips in counties for row in components[fips]]
    output = {
        "audit_type": "bds-ohio-hrsa-provider-surface-v1",
        "checked": "2026-09-18",
        "unit": "Ohio county mobility context joined to current designated primary-care HPSA component records",
        "geography": "Ohio counties (state FIPS 39)",
        "sources": {
            "hrsa_url": "https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv",
            "hrsa_local_sha256": hashlib.sha256(args.hrsa.read_bytes()).hexdigest(),
            "acs_vehicle_url": "https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08201.dat",
            "acs_vehicle_sha256": hashlib.sha256(args.vehicle.read_bytes()).hexdigest(),
            "acs_commute_url": "https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08303.dat",
            "acs_commute_sha256": hashlib.sha256(args.commute.read_bytes()).hexdigest(),
        },
        "hrsa_file_create_date": "2026-09-14",
        "counties": len(counties),
        "zero_vehicle_median_cut_pct": round(cut, 3),
        "all_ohio": summarize(counties),
        "mobility_groups": {group: summarize(fips_list) for group, fips_list in groups.items()},
        "boundary": "HPSA rows are designated components, not county-wide provider inventories. Component rows can be tract-, population-, facility-, or county-based and can overlap; reported FTE is missing on some rows and is not summed into a county capacity total. This surface does not measure appointment availability, accepting providers, travel, wait, quality, completed use, or resident outcomes.",
        "raw_storage": "HRSA input was retained locally; ACS inputs were transient",
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
