#!/usr/bin/env python3
"""Compare county population change with selected CBP capacity measures."""

from __future__ import annotations

import argparse
import csv
import io
import math
import statistics
from pathlib import Path
from zipfile import ZipFile


SECTORS = {
    "44----": "retail",
    "62----": "health_social",
    "72----": "food",
}


def pearson(xs: list[float], ys: list[float]) -> float:
    xbar, ybar = statistics.mean(xs), statistics.mean(ys)
    numerator = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    denominator = math.sqrt(sum((x - xbar) ** 2 for x in xs) * sum((y - ybar) ** 2 for y in ys))
    return numerator / denominator if denominator else float("nan")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--min-population", type=int, default=100_000)
    args = parser.parse_args()

    population: dict[str, tuple[int, int]] = {}
    with args.population.open(newline="", encoding="latin1") as source:
        for row in csv.DictReader(source):
            if row.get("SUMLEV") == "050" and row.get("POPESTIMATE2020") and row.get("POPESTIMATE2023"):
                population[row["STATE"] + row["COUNTY"]] = (int(row["POPESTIMATE2020"]), int(row["POPESTIMATE2023"]))

    capacity: dict[str, dict[str, tuple[int | None, int | None]]] = {}
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
        if pop23 >= args.min_population and key in capacity:
            records.append({"key": key, "growth": 100 * (pop23 / pop20 - 1), "pop": pop23})
    records.sort(key=lambda row: row["growth"])
    print(f"counties={len(records)}\tmin_population={args.min_population}")
    print("sector\tmeasure\tpearson_growth\tq1_n\tq1_median\tq2_n\tq2_median\tq3_n\tq3_median\tq4_n\tq4_median")
    for code, name in SECTORS.items():
        for measure, index in (("establishments", 0), ("employment", 1)):
            usable = [row for row in records if capacity[row["key"]].get(code, (None, None))[index] is not None]
            xs = [row["growth"] for row in usable]
            ys = [10_000 * capacity[row["key"]][code][index] / row["pop"] for row in usable]
            groups = [usable[i * len(usable) // 4:(i + 1) * len(usable) // 4] for i in range(4)]
            medians = []
            for group in groups:
                values = [10_000 * capacity[row["key"]][code][index] / row["pop"] for row in group]
                medians.append((len(group), statistics.median(values)))
            fields = [name, measure, f"{pearson(xs, ys):.4f}"]
            for n, median in medians:
                fields.extend((str(n), f"{median:.2f}"))
            print("\t".join(fields))


if __name__ == "__main__":
    main()
