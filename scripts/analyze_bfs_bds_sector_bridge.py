#!/usr/bin/env python3
"""Bridge national BFS sector applications to annual BDS sector dynamics."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_bfs(path: Path, year: int) -> dict[str, tuple[str, float]]:
    with path.open(newline="") as handle:
        rows = csv.DictReader(handle)
        result = {}
        for row in rows:
            values = [float(value or 0) for key, value in row.items() if key.startswith(f"{year}w")]
            result[row["naics2"]] = (row["description"], sum(values))
        return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bfs", type=Path, required=True)
    parser.add_argument("--bds", type=Path, required=True)
    parser.add_argument("--year", type=int, default=2023)
    args = parser.parse_args()

    applications = read_bfs(args.bfs, args.year)
    with args.bds.open(newline="") as handle:
        dynamics = {row["sector"]: row for row in csv.DictReader(handle) if int(row["year"]) == args.year}

    print("sector\tdescription\tapplications\testabs_entry\testabs_exit\tnet_job_creation")
    for sector in applications:
        if sector not in dynamics:
            continue
        description, count = applications[sector]
        row = dynamics[sector]
        print(f"{sector}\t{description}\t{count:.0f}\t{row['estabs_entry']}\t{row['estabs_exit']}\t{row['net_job_creation']}")


if __name__ == "__main__":
    main()
