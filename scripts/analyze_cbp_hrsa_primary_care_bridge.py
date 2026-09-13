#!/usr/bin/env python3
"""Compare CBP county health capacity with HRSA primary-care HPSA presence."""

from __future__ import annotations

import argparse
import csv
import io
import re
import statistics
from pathlib import Path
from zipfile import ZipFile


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--hpsa", type=Path, required=True)
    parser.add_argument("--rucc", type=Path, required=True)
    args = parser.parse_args()

    population = {
        row["STATE"] + row["COUNTY"]: int(row["POPESTIMATE2023"])
        for row in csv.DictReader(args.population.open(newline="", encoding="latin1"))
        if row["SUMLEV"] == "050" and row["POPESTIMATE2023"]
    }
    hpsa = set()
    with args.hpsa.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            key = row["State and County Federal Information Processing Standard Code"]
            if row["HPSA Status"] == "Designated" and re.fullmatch(r"\d{5}", key) and row["State Abbreviation"] not in {"PR", "VI", "GU", "AS", "MP"}:
                hpsa.add(key)

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
                if row["naics"] == "62----":
                    counties[row["fipstate"] + row["fipscty"]] = row

    keys = sorted(set(population) & set(counties))
    print(f"matched_counties={len(keys)}")
    print(f"designated_primary_care_hpsa_counties={len(set(keys) & hpsa)}")
    designated = set(keys) & hpsa & set(rucc)
    print(f"hpsa_nonmetro_share={sum(rucc[key] >= 4 for key in designated) / len(designated) * 100:.1f}")
    for label, selected in (("HPSA_component_present", [key for key in keys if key in hpsa]), ("No_HPSA_component_present", [key for key in keys if key not in hpsa])):
        rates = [10000 * int(counties[key]["est"]) / population[key] for key in selected]
        print(f"{label}\tcounties={len(selected)}\tmedian_health_establishments_per_10000={statistics.median(rates):.2f}\tpopulation_weighted={10000 * sum(int(counties[key]['est']) for key in selected) / sum(population[key] for key in selected):.2f}")


if __name__ == "__main__":
    main()
