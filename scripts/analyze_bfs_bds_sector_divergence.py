#!/usr/bin/env python3
"""Quantify divergence between BFS applications and BDS realized sector flows."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_bfs(path: Path, year: int) -> dict[str, dict[str, float | str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        result = {}
        for row in csv.DictReader(handle):
            values = [float(value or 0) for key, value in row.items()
                      if key.startswith(f"{year}w")]
            result[row["naics2"]] = {
                "description": row["description"],
                "applications": sum(values),
            }
        return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bfs", type=Path, required=True)
    parser.add_argument("--bds", type=Path, required=True)
    parser.add_argument("--year", type=int, default=2023)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    applications = read_bfs(args.bfs, args.year)
    with args.bds.open(newline="", encoding="utf-8") as handle:
        dynamics = {
            row["sector"]: row for row in csv.DictReader(handle)
            if int(row["year"]) == args.year
        }

    rows = []
    for sector, base in applications.items():
        if sector not in dynamics:
            continue
        row = dynamics[sector]
        apps = float(base["applications"])
        openings = float(row["estabs_entry"])
        closings = float(row["estabs_exit"])
        net_jobs = float(row["net_job_creation"])
        rows.append({
            "sector": sector,
            "description": base["description"],
            "applications": round(apps),
            "openings": round(openings),
            "closings": round(closings),
            "net_job_creation": round(net_jobs),
            "openings_per_100_applications": round(100 * openings / apps, 3) if apps else None,
            "net_jobs_per_100_applications": round(100 * net_jobs / apps, 3) if apps else None,
            "entry_minus_exit": round(openings - closings),
        })

    total_apps = sum(row["applications"] for row in rows)
    for row in rows:
        row["application_share_percent"] = round(100 * row["applications"] / total_apps, 3) if total_apps else None

    result = {
        "format": "us-bfs-bds-sector-divergence-v1",
        "source_unit": "national sector, annual BFS application flow and BDS realized establishment/job flow",
        "year": args.year,
        "rows": rows,
        "causal_estimation": False,
        "boundary": "BFS applications and BDS openings/closings use different constructions and timing; ratios are comparison metrics, not conversion or survival rates.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"sectors": len(rows), "total_applications": total_apps}, indent=2))


if __name__ == "__main__":
    main()
