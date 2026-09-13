#!/usr/bin/env python3
"""Compare county sector capacity with population growth and foreign-born share."""

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


def quartile_rows(records, key_name: str, code: str, measure_index: int):
    records = sorted(records, key=lambda row: row[key_name])
    groups = [records[i * len(records) // 4:(i + 1) * len(records) // 4] for i in range(4)]
    output = []
    for group in groups:
        values = [10_000 * row["capacity"][code][measure_index] / row["pop"] for row in group]
        output.extend((str(len(values)), f"{statistics.median(values):.2f}"))
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--nativity", type=Path, required=True)
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
        if pop23 < args.min_population or key not in nativity or key not in capacity:
            continue
        records.append({"growth": 100 * (pop23 / pop20 - 1), "foreign_born": nativity[key], "pop": pop23, "capacity": capacity[key]})
    print(f"counties={len(records)}\tmin_population={args.min_population}")
    print("sector\tmeasure\taxis\tpearson\tq1_n\tq1_median\tq2_n\tq2_median\tq3_n\tq3_median\tq4_n\tq4_median")
    for code, name in SECTORS.items():
        for measure, index in (("establishments", 0), ("employment", 1)):
            usable = [row for row in records if code in row["capacity"] and row["capacity"][code][index] is not None]
            for axis, axis_key in (("population_growth", "growth"), ("foreign_born_share", "foreign_born")):
                xs = [row[axis_key] for row in usable]
                ys = [10_000 * row["capacity"][code][index] / row["pop"] for row in usable]
                fields = [name, measure, axis, f"{pearson(xs, ys):.4f}"] + quartile_rows(usable, axis_key, code, index)
                print("\t".join(fields))


if __name__ == "__main__":
    main()
