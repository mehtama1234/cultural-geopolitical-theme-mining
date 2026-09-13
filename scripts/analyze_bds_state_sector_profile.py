#!/usr/bin/env python3
"""Summarize 2023 BDS entry, exit, and job dynamics across states by sector."""

from __future__ import annotations

import argparse
import csv
import statistics
from pathlib import Path


SECTORS = {
    "23": "Construction",
    "31-33": "Manufacturing",
    "44-45": "Retail trade",
    "48-49": "Transportation and warehousing",
    "62": "Health care and social assistance",
    "72": "Accommodation and food services",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--year", type=int, default=2023)
    args = parser.parse_args()

    with args.csv.open(newline="") as handle:
        rows = [
            row for row in csv.DictReader(handle)
            if int(row["year"]) == args.year and row["sector"] in SECTORS
        ]
    for sector, label in SECTORS.items():
        current = [row for row in rows if row["sector"] == sector]
        entry = [float(row["estabs_entry_rate"]) for row in current]
        exit_ = [float(row["estabs_exit_rate"]) for row in current]
        net = [float(row["net_job_creation_rate"]) for row in current]
        print(
            f"{label}\tstates={len(current)}"
            f"\tentry_median={statistics.median(entry):.2f}"
            f"\tentry_p25={statistics.quantiles(entry, n=4)[0]:.2f}"
            f"\tentry_p75={statistics.quantiles(entry, n=4)[2]:.2f}"
            f"\texit_median={statistics.median(exit_):.2f}"
            f"\tnet_job_rate_median={statistics.median(net):.2f}"
            f"\tnegative_net_states={sum(value < 0 for value in net)}"
            f"\texit_above_entry_states={sum(a < b for a, b in zip(entry, exit_))}"
        )


if __name__ == "__main__":
    main()
