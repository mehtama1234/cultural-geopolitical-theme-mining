#!/usr/bin/env python3
"""Extract selected year/sector rows from a Census BDS sector CSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


SECTORS = {
    "11": "Agriculture, forestry, fishing and hunting",
    "21": "Mining, quarrying, and oil and gas extraction",
    "23": "Construction",
    "31-33": "Manufacturing",
    "42": "Wholesale trade",
    "44-45": "Retail trade",
    "48-49": "Transportation and warehousing",
    "51": "Information",
    "52": "Finance and insurance",
    "53": "Real estate and rental and leasing",
    "54": "Professional, scientific, and technical services",
    "55": "Management of companies and enterprises",
    "56": "Administrative and support and waste management",
    "61": "Educational services",
    "62": "Health care and social assistance",
    "71": "Arts, entertainment, and recreation",
    "72": "Accommodation and food services",
    "81": "Other services (except public administration)",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--year", type=int, default=2023)
    args = parser.parse_args()

    with args.csv.open(newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if int(row["year"]) == args.year]
    for row in rows:
        label = SECTORS.get(row["sector"], row["sector"])
        print(
            f"{label}\tsector={row['sector']}\tfirms={row['firms']}"
            f"\testabs={row['estabs']}\temp={row['emp']}"
            f"\testabs_entry={row['estabs_entry']}"
            f"\testabs_exit={row['estabs_exit']}"
            f"\tjob_creation_births={row['job_creation_births']}"
            f"\tjob_destruction_deaths={row['job_destruction_deaths']}"
            f"\tnet_job_creation={row['net_job_creation']}"
        )


if __name__ == "__main__":
    main()
