#!/usr/bin/env python3
"""Summarize numeric CBP 2-digit sector employment per county capita."""

from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path
from zipfile import ZipFile

from analyze_cbp_county_all_sector_capacity import SECTORS, quartiles


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    args = parser.parse_args()

    population: dict[str, int] = {}
    with args.population.open(newline="", encoding="latin1") as source:
        for row in csv.DictReader(source):
            if row.get("SUMLEV") == "050" and row.get("POPESTIMATE2023"):
                population[row["STATE"] + row["COUNTY"]] = int(row["POPESTIMATE2023"])

    employment: dict[str, dict[str, int]] = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                code = row.get("naics")
                value = row.get("emp", "")
                if code not in SECTORS or not value.isdigit():
                    continue
                key = row["fipstate"] + row["fipscty"]
                employment.setdefault(key, {})[code] = int(value)

    keys = sorted(set(population) & set(employment))
    print("sector\tnumeric_count\tmedian_per_10000\tp25_per_10000\tp75_per_10000")
    for code, name in SECTORS.items():
        values = [10000 * employment[key][code] / population[key] for key in keys if code in employment[key]]
        median, q25, q75 = quartiles(values)
        print(f"{name}\t{len(values)}\t{median:.2f}\t{q25:.2f}\t{q75:.2f}")


if __name__ == "__main__":
    main()
