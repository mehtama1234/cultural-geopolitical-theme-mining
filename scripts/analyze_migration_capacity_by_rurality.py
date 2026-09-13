#!/usr/bin/env python3
"""Stratify migration-proxy/capacity comparisons by USDA rurality."""

from __future__ import annotations

import argparse
import csv
import io
import math
import re
import statistics
from pathlib import Path
from zipfile import ZipFile

SECTORS = {"44----": "retail", "62----": "health_social", "72----": "food"}


def pearson(xs: list[float], ys: list[float]) -> float:
    xbar, ybar = statistics.mean(xs), statistics.mean(ys)
    numerator = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    denominator = math.sqrt(sum((x - xbar) ** 2 for x in xs) * sum((y - ybar) ** 2 for y in ys))
    return numerator / denominator if denominator else float("nan")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--nativity", type=Path, required=True)
    parser.add_argument("--rucc", type=Path, required=True)
    parser.add_argument("--min-population", type=int, default=100_000)
    args = parser.parse_args()

    population = {}
    with args.population.open(newline="", encoding="latin1") as source:
        for row in csv.DictReader(source):
            if row.get("SUMLEV") == "050" and row.get("POPESTIMATE2020") and row.get("POPESTIMATE2023"):
                key = row["STATE"] + row["COUNTY"]
                population[key] = (int(row["POPESTIMATE2020"]), int(row["POPESTIMATE2023"]))

    nativity = {}
    with args.nativity.open(newline="", encoding="latin1") as source:
        for row in csv.DictReader(source, delimiter="|"):
            match = re.fullmatch(r"0500000US(\d{5})", row.get("GEO_ID", ""))
            if match and row.get("B05002_E001", "").isdigit() and row.get("B05002_E002", "").isdigit():
                total, native = int(row["B05002_E001"]), int(row["B05002_E002"])
                if total:
                    nativity[match.group(1)] = 100 * (total - native) / total

    rucc = {}
    with args.rucc.open(newline="", encoding="latin1") as source:
        for row in csv.DictReader(source):
            if row.get("Attribute") == "RUCC_2023":
                rucc[row["FIPS"]] = int(row["Value"])

    capacity = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                code = row.get("naics")
                if code not in SECTORS:
                    continue
                key = row["fipstate"] + row["fipscty"]
                est = int(row["est"]) if row.get("est", "").isdigit() else None
                emp = int(row["emp"]) if row.get("emp", "").isdigit() else None
                capacity.setdefault(key, {})[code] = (est, emp)

    records = []
    for key, (pop20, pop23) in population.items():
        if pop23 < args.min_population or key not in nativity or key not in rucc or key not in capacity:
            continue
        records.append({"growth": 100 * (pop23 / pop20 - 1), "foreign_born": nativity[key], "pop": pop23, "rucc": rucc[key], "capacity": capacity[key]})

    print("place_group\tcounties\tsector\tmeasure\taxis\tpearson\tlow_quartile_median\thigh_quartile_median")
    for place_group, predicate in (("metro", lambda code: code <= 3), ("nonmetro", lambda code: code >= 4)):
        group = [row for row in records if predicate(row["rucc"])]
        print(f"# {place_group}\t{len(group)}")
        for code, name in SECTORS.items():
            for measure, index in (("establishments", 0), ("employment", 1)):
                usable = [row for row in group if code in row["capacity"] and row["capacity"][code][index] is not None]
                for axis, axis_key in (("population_growth", "growth"), ("foreign_born_share", "foreign_born")):
                    axis_rows = sorted(usable, key=lambda row: row[axis_key])
                    xs = [row[axis_key] for row in axis_rows]
                    ys = [10_000 * row["capacity"][code][index] / row["pop"] for row in axis_rows]
                    split = len(axis_rows) // 4
                    low = [10_000 * row["capacity"][code][index] / row["pop"] for row in axis_rows[:split]]
                    high = [10_000 * row["capacity"][code][index] / row["pop"] for row in axis_rows[-split:]]
                    print(f"{place_group}\t{len(axis_rows)}\t{name}\t{measure}\t{axis}\t{pearson(xs, ys):.4f}\t{statistics.median(low):.2f}\t{statistics.median(high):.2f}")


if __name__ == "__main__":
    main()
