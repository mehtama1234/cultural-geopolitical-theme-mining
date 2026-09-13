#!/usr/bin/env python3
"""Summarize CBP essential-sector establishments per 10,000 residents."""

from __future__ import annotations

import argparse
import csv
import io
import statistics
from pathlib import Path
from zipfile import ZipFile


SECTORS = {
    "31----": "manufacturing",
    "44----": "retail",
    "62----": "health_social_assistance",
    "72----": "accommodation_food",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--year", type=int, default=2023)
    args = parser.parse_args()

    population = {}
    with args.population.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row["SUMLEV"] == "050" and row[f"POPESTIMATE{args.year}"]:
                population[(row["STATE"], row["COUNTY"])] = int(row[f"POPESTIMATE{args.year}"])

    counties = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                if row["naics"] in ("------", *SECTORS):
                    county = counties.setdefault((row["fipstate"], row["fipscty"]), {})
                    if row["est"].isdigit():
                        county[f"{row['naics']}_est"] = int(row["est"])
                    if row["emp"].isdigit():
                        county[f"{row['naics']}_emp"] = int(row["emp"])

    keys = sorted(set(population) & set(counties))
    print(f"matched_counties={len(keys)}")
    for code, label in SECTORS.items():
        values = [10000 * counties[key].get(f"{code}_est", 0) / population[key] for key in keys]
        quartiles = statistics.quantiles(values, n=4, method="inclusive")
        print(
            f"{label}\tmedian={statistics.median(values):.2f}"
            f"\tp25={quartiles[0]:.2f}\tp75={quartiles[2]:.2f}"
            f"\tzero_count={sum(value == 0 for value in values)}"
        )
        employment_keys = [key for key in keys if f"{code}_emp" in counties[key]]
        employment = [10000 * counties[key][f"{code}_emp"] / population[key] for key in employment_keys]
        quartiles = statistics.quantiles(employment, n=4, method="inclusive")
        print(
            f"{label}_employment_per_10000\tmatched_counties={len(employment_keys)}"
            f"\tmedian={statistics.median(employment):.2f}"
            f"\tp25={quartiles[0]:.2f}\tp75={quartiles[2]:.2f}"
            f"\tzero_count={sum(value == 0 for value in employment)}"
        )


if __name__ == "__main__":
    main()
