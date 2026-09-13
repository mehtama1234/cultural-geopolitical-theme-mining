#!/usr/bin/env python3
"""Build a small population-change proxy and local-capacity comparison."""

from __future__ import annotations

import argparse
import csv
import io
import re
from pathlib import Path
from zipfile import ZipFile


SECTORS = {
    "44----": "retail",
    "62----": "health_social",
    "72----": "food",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--hpsa", type=Path, required=True)
    parser.add_argument("--rucc", type=Path, required=True)
    parser.add_argument("--nativity", type=Path, help="ACS table-based B05002 pipe file")
    parser.add_argument("--min-population", type=int, default=100_000)
    parser.add_argument("--n", type=int, default=10)
    args = parser.parse_args()

    population = {}
    names = {}
    with args.population.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row["SUMLEV"] == "050" and row["POPESTIMATE2020"] and row["POPESTIMATE2023"]:
                key = row["STATE"] + row["COUNTY"]
                population[key] = (int(row["POPESTIMATE2020"]), int(row["POPESTIMATE2023"]))
                names[key] = row["CTYNAME"]

    rucc = {}
    with args.rucc.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            if row["Attribute"] == "RUCC_2023":
                rucc[row["FIPS"]] = int(row["Value"])

    hpsa = set()
    with args.hpsa.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle):
            key = row["State and County Federal Information Processing Standard Code"]
            if row["HPSA Status"] == "Designated" and re.fullmatch(r"\d{5}", key):
                hpsa.add(key)

    nativity = {}
    if args.nativity:
        with args.nativity.open(newline="", encoding="latin1") as handle:
            reader = csv.DictReader(handle, delimiter="|")
            for row in reader:
                match = re.fullmatch(r"0500000US(\d{5})", row["GEO_ID"])
                if match and row["B05002_E001"].isdigit() and row["B05002_E002"].isdigit():
                    total = int(row["B05002_E001"])
                    native = int(row["B05002_E002"])
                    nativity[match.group(1)] = 100 * (total - native) / total if total else None

    capacity = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                if row["naics"] not in SECTORS:
                    continue
                key = row["fipstate"] + row["fipscty"]
                item = capacity.setdefault(key, {})
                item[f"{row['naics']}_est"] = int(row["est"]) if row["est"].isdigit() else None
                item[f"{row['naics']}_emp"] = int(row["emp"]) if row["emp"].isdigit() else None

    eligible = []
    for key, (pop20, pop23) in population.items():
        if pop23 < args.min_population or key not in capacity or key not in rucc:
            continue
        eligible.append((100 * (pop23 / pop20 - 1), key))
    selected = sorted(eligible)[: args.n] + sorted(eligible, reverse=True)[: args.n]

    print("group\tcounty\tfips\tpop2020\tpop2023\tpop_change_pct\tforeign_born_pct_acs5_2023\trucc\thpsa\tretail_est_per_10k\thealth_est_per_10k\tfood_est_per_10k")
    for group, rows in (("lower_change", selected[: args.n]), ("higher_change", selected[args.n :])):
        for change, key in rows:
            pop20, pop23 = population[key]
            values = []
            for code in SECTORS:
                est = capacity[key].get(f"{code}_est") or 0
                values.append(f"{10_000 * est / pop23:.2f}")
            foreign_born = "" if key not in nativity else f"{nativity[key]:.2f}"
            print("\t".join([group, names[key], key, str(pop20), str(pop23), f"{change:.2f}", foreign_born, str(rucc[key]), "yes" if key in hpsa else "no", *values]))


if __name__ == "__main__":
    main()
