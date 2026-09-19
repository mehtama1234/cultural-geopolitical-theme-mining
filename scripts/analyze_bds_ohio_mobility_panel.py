#!/usr/bin/env python3
"""Join a bounded 2023 Ohio BDS sector panel to ACS mobility context."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import statistics
from pathlib import Path


SECTORS = {
    "44-45": "retail trade",
    "48-49": "transportation and warehousing",
    "62": "health care and social assistance",
    "72": "accommodation and food services",
}


def numeric(value: str) -> float | None:
    if value in {"", "D", "N", "S"}:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def read_table(path: Path, prefix: str) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="|"):
            fips = row.get("GEO_ID", "")
            if not fips.startswith("0500000US39"):
                continue
            values: dict[str, int] = {}
            for key, value in row.items():
                if key.startswith(prefix + "_E"):
                    try:
                        values[key] = int(value)
                    except (TypeError, ValueError):
                        pass
            if values:
                result[fips[-5:]] = values
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bds-suffix", type=Path, required=True)
    parser.add_argument("--vehicle", type=Path, required=True)
    parser.add_argument("--commute", type=Path, required=True)
    parser.add_argument("--rucc", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    vehicle = read_table(args.vehicle, "B08201")
    commute = read_table(args.commute, "B08303")
    rucc: dict[str, int] = {}
    with args.rucc.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row.get("Attribute") == "RUCC_2023":
                try:
                    rucc[row["FIPS"].zfill(5)] = int(row["Value"])
                except (KeyError, ValueError):
                    pass

    mobility: dict[str, dict[str, float | int]] = {}
    for fips in sorted(set(vehicle) & set(commute) & set(rucc)):
        v, c = vehicle[fips], commute[fips]
        households = v.get("B08201_E001")
        workers = c.get("B08303_E001")
        if not households or not workers:
            continue
        long_commute = sum(c.get(f"B08303_E{i:03d}", 0) for i in range(8, 14))
        mobility[fips] = {
            "zero_vehicle_pct": 100 * v.get("B08201_E002", 0) / households,
            "long_commute_pct": 100 * long_commute / workers,
            "rucc": rucc[fips],
        }

    bds: dict[str, dict[str, list[dict[str, float]]]] = {}
    rows_2023 = 0
    with args.bds_suffix.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle):
            if len(row) < 28 or row[0] != "2023" or row[1] != "39" or row[3] not in SECTORS:
                continue
            fips = row[1] + row[2]
            if fips not in mobility:
                continue
            rows_2023 += 1
            entry, exit_rate, net = numeric(row[9]), numeric(row[11]), numeric(row[23])
            if entry is None or exit_rate is None or net is None:
                continue
            bds.setdefault(fips, {}).setdefault(row[3], []).append({"entry": entry, "exit": exit_rate, "net": net})

    counties = []
    for fips in sorted(set(mobility) & set(bds)):
        if all(sector in bds[fips] for sector in SECTORS):
            counties.append(fips)
    cut = statistics.median(mobility[fips]["zero_vehicle_pct"] for fips in counties)
    groups = {"low_zero_vehicle": [f for f in counties if mobility[f]["zero_vehicle_pct"] < cut], "high_zero_vehicle": [f for f in counties if mobility[f]["zero_vehicle_pct"] >= cut]}

    summary: dict[str, dict[str, dict[str, float | int]]] = {}
    for group, fips_list in groups.items():
        summary[group] = {"county_count": len(fips_list), "median_zero_vehicle_pct": round(statistics.median(mobility[f]["zero_vehicle_pct"] for f in fips_list), 3) if fips_list else None, "median_long_commute_pct": round(statistics.median(mobility[f]["long_commute_pct"] for f in fips_list), 3) if fips_list else None}
        for sector in SECTORS:
            values = [bds[f][sector][0] for f in fips_list]
            summary[group][sector] = {
                "label": SECTORS[sector],
                "comparable_rows": len(values),
                "median_entry_rate": round(statistics.median(v["entry"] for v in values), 3) if values else None,
                "median_exit_rate": round(statistics.median(v["exit"] for v in values), 3) if values else None,
                "median_net_job_creation_rate": round(statistics.median(v["net"] for v in values), 3) if values else None,
                "negative_net_job_rows": sum(v["net"] < 0 for v in values),
                "exit_greater_than_entry_rows": sum(v["exit"] > v["entry"] for v in values),
            }

    output = {
        "audit_type": "bds-ohio-mobility-panel-v1",
        "checked": "2026-09-18",
        "unit": "Ohio county-sector aggregate, 2023, joined to 2023 ACS 5-year county mobility context",
        "geography": "Ohio counties (state FIPS 39)",
        "selected_sectors": SECTORS,
        "sources": {
            "bds_url": "https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv",
            "bds_last_modified": "2025-09-25",
            "bds_file_size_bytes": 274770797,
            "acs_vehicle_url": "https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08201.dat",
            "acs_commute_url": "https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08303.dat",
            "rucc_url": "https://www.ers.usda.gov/media/5768/2023-rural-urban-continuum-codes.csv?v=94035",
        },
        "retrieval": {
            "bds_method": "transient 12 MB suffix retrieval",
            "bds_suffix_sha256": hashlib.sha256(args.bds_suffix.read_bytes()).hexdigest(),
            "bds_2023_ohio_rows_in_suffix": rows_2023,
            "acs_vehicle_sha256": hashlib.sha256(args.vehicle.read_bytes()).hexdigest(),
            "acs_commute_sha256": hashlib.sha256(args.commute.read_bytes()).hexdigest(),
            "rucc_sha256": hashlib.sha256(args.rucc.read_bytes()).hexdigest(),
        },
        "matched_counties_with_all_four_sectors": len(counties),
        "zero_vehicle_median_cut_pct": round(cut, 3),
        "groups": summary,
        "boundary": "This is a same-year, same-state descriptive comparison. It does not establish that mobility constraints caused sector turnover, that employer flow changed service access, or that any resident made a particular trip. ACS vehicle and commute measures are county aggregates; BDS values are county-sector aggregates; disclosure values are excluded rather than treated as zero.",
        "counterexample_county": {
            "fips": "39089",
            "zero_vehicle_pct": round(float(mobility.get("39089", {}).get("zero_vehicle_pct", 0)), 3),
            "long_commute_pct": round(float(mobility.get("39089", {}).get("long_commute_pct", 0)), 3),
            "rucc": mobility.get("39089", {}).get("rucc"),
            "sector_net_job_creation_rates": {sector: bds.get("39089", {}).get(sector, [{}])[0].get("net") for sector in SECTORS},
        },
        "raw_storage": "not retained; official BDS suffix, ACS table files, and RUCC file were retrieved transiently",
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
