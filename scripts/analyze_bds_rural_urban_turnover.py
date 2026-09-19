#!/usr/bin/env python3
"""Summarize 2023 BDS county-sector turnover by USDA metro status."""

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


def number(value: str) -> float | None:
    if value in {"", "D", "N", "S"}:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bds-suffix", type=Path, required=True)
    parser.add_argument("--rucc", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rucc: dict[str, int] = {}
    with args.rucc.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row.get("Attribute") == "RUCC_2023":
                try:
                    rucc[row["FIPS"].zfill(5)] = int(row["Value"])
                except (KeyError, ValueError):
                    pass

    cells: dict[str, dict[str, list[dict[str, float]]]] = {
        group: {sector: [] for sector in SECTORS} for group in ("metro", "nonmetro")
    }
    rows_2023 = 0
    with args.bds_suffix.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle):
            if len(row) < 28 or row[0] != "2023" or row[3] not in SECTORS:
                continue
            rows_2023 += 1
            fips = f"{row[1]}{row[2]}"
            code = rucc.get(fips)
            group = "metro" if code is not None and code <= 3 else "nonmetro" if code is not None and code >= 4 else None
            if group is None:
                continue
            entry = number(row[9])
            exit_rate = number(row[11])
            net = number(row[23])
            if entry is None or exit_rate is None or net is None:
                continue
            cells[group][row[3]].append({"entry": entry, "exit": exit_rate, "net": net})

    summary: dict[str, dict[str, dict[str, float | int]]] = {}
    for group, sector_cells in cells.items():
        summary[group] = {}
        for sector, values in sector_cells.items():
            summary[group][sector] = {
                "label": SECTORS[sector],
                "comparable_rows": len(values),
                "median_entry_rate": round(statistics.median(v["entry"] for v in values), 3) if values else None,
                "median_exit_rate": round(statistics.median(v["exit"] for v in values), 3) if values else None,
                "median_net_job_creation_rate": round(statistics.median(v["net"] for v in values), 3) if values else None,
                "negative_net_job_rows": sum(v["net"] < 0 for v in values),
                "exit_greater_than_entry_rows": sum(v["exit"] > v["entry"] for v in values),
            }

    record = {
        "audit_type": "bds-rural-urban-turnover-layer-v1",
        "checked": "2026-09-18",
        "unit": "2023 county-sector aggregate, grouped by USDA 2023 RUCC metro status",
        "source_url": "https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv",
        "source_last_modified": "2025-09-25",
        "source_size_bytes": 274770797,
        "rucc_source_url": "https://www.ers.usda.gov/media/5768/2023-rural-urban-continuum-codes.csv?v=94035",
        "retrieval": {
            "method": "transient HTTP suffix retrieval",
            "suffix_bytes": args.bds_suffix.stat().st_size,
            "suffix_sha256": hashlib.sha256(args.bds_suffix.read_bytes()).hexdigest(),
            "rows_2023_in_suffix": rows_2023,
            "rucc_rows": len(rucc),
        },
        "selected_sectors": SECTORS,
        "groups": summary,
        "boundary": "This is a descriptive 2023 county-sector flow comparison by metro status. It does not measure household access, travel, prices, wages, service quality, use, causation, trust, political action, or geopolitical consequence; missing BDS disclosure values are excluded rather than treated as zero.",
        "raw_storage": "not retained; official BDS suffix and RUCC file were retrieved transiently",
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
