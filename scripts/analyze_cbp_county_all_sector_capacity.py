#!/usr/bin/env python3
"""Summarize all CBP 2-digit sectors as county establishments per capita."""

from __future__ import annotations

import argparse
import csv
import io
import statistics
from pathlib import Path
from zipfile import ZipFile


SECTORS = {
    "11----": "agriculture_forestry_fishing_hunting",
    "21----": "mining_quarrying_oil_gas",
    "22----": "utilities",
    "23----": "construction",
    "31----": "manufacturing",
    "42----": "wholesale_trade",
    "44----": "retail_trade",
    "48----": "transportation_warehousing",
    "51----": "information",
    "52----": "finance_insurance",
    "53----": "real_estate_rental_leasing",
    "54----": "professional_scientific_technical",
    "55----": "management_companies",
    "56----": "administrative_support_waste",
    "61----": "educational_services",
    "62----": "health_social_assistance",
    "71----": "arts_entertainment_recreation",
    "72----": "accommodation_food",
    "81----": "other_services",
    "99----": "unclassified",
}


def quartiles(values: list[float]) -> tuple[float, float, float]:
    q25, q75 = statistics.quantiles(values, n=4, method="inclusive")[0::2]
    return statistics.median(values), q25, q75


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

    counties: dict[str, dict[str, int]] = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                code = row.get("naics")
                if code not in SECTORS or not row.get("est", "").isdigit():
                    continue
                key = row["fipstate"] + row["fipscty"]
                counties.setdefault(key, {})[code] = int(row["est"])

    keys = sorted(set(population) & set(counties))
    print("sector\tnumeric_count\tmedian_per_10000\tp25_per_10000\tp75_per_10000\tzero_numeric_count")
    for code, name in SECTORS.items():
        values = [10000 * counties[key][code] / population[key] for key in keys if code in counties[key]]
        median, q25, q75 = quartiles(values)
        print(f"{name}\t{len(values)}\t{median:.2f}\t{q25:.2f}\t{q75:.2f}\t{sum(value == 0 for value in values)}")


if __name__ == "__main__":
    main()
