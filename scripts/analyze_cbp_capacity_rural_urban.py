#!/usr/bin/env python3
"""Compare CBP essential-sector capacity in metro and nonmetro counties."""

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
    parser.add_argument("--rucc", type=Path, required=True)
    args = parser.parse_args()

    population = {}
    with args.population.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row["SUMLEV"] == "050" and row["POPESTIMATE2023"]:
                population[row["STATE"] + row["COUNTY"]] = int(row["POPESTIMATE2023"])

    rucc = {}
    with args.rucc.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row["Attribute"] == "RUCC_2023":
                rucc[row["FIPS"]] = int(row["Value"])

    counties = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                if row["naics"] in SECTORS and row["est"].isdigit():
                    counties.setdefault(row["fipstate"] + row["fipscty"], {})[row["naics"]] = int(row["est"])

    for label, predicate in (("metro", lambda code: code <= 3), ("nonmetro", lambda code: code >= 4)):
        keys = sorted(key for key in set(population) & set(rucc) & set(counties) if predicate(rucc[key]))
        total_population = sum(population[key] for key in keys)
        print(f"{label}\tcounties={len(keys)}\tpopulation={total_population}")
        for code, sector in SECTORS.items():
            values = [10000 * counties[key].get(code, 0) / population[key] for key in keys]
            weighted = 10000 * sum(counties[key].get(code, 0) for key in keys) / total_population
            print(f"{label}_{sector}\tmedian={statistics.median(values):.2f}\tpopulation_weighted={weighted:.2f}\tzero_count={sum(value == 0 for value in values)}")


if __name__ == "__main__":
    main()
