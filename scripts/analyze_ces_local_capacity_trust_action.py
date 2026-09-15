#!/usr/bin/env python3
"""Join county capacity/mobility context to CES trust and civic-action fields.

This is a descriptive place-context bridge. County capacity cells do not
measure each respondent's service exposure, and CES weights do not make every
county representative.
"""

from __future__ import annotations

import argparse
import csv
import io
import statistics
from pathlib import Path
from zipfile import ZipFile

import pandas as pd


ACTION_COLUMNS = [f"CC24_430a_{i}" for i in range(1, 7)]


def read_population(path: Path, minimum: int) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    with path.open(encoding="latin1", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("SUMLEV") != "050":
                continue
            try:
                pop20 = int(row["POPESTIMATE2020"])
                pop23 = int(row["POPESTIMATE2023"])
            except (KeyError, TypeError, ValueError):
                continue
            if pop23 < minimum or pop20 <= 0:
                continue
            key = str(row["STATE"]).zfill(2) + str(row["COUNTY"]).zfill(3)
            out[key] = {"population": pop23, "growth": 100 * (pop23 / pop20 - 1)}
    return out


def read_vehicle(path: Path) -> dict[str, float]:
    out: dict[str, float] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="|"):
            geo = row.get("GEO_ID", "")
            if not geo.startswith("0500000US"):
                continue
            try:
                total = int(row["B08201_E001"])
                zero = int(row["B08201_E002"])
            except (KeyError, TypeError, ValueError):
                continue
            if total:
                out[geo[-5:]] = 100 * zero / total
    return out


def read_capacity(path: Path) -> dict[str, int]:
    out: dict[str, int] = {}
    with ZipFile(path) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                if row.get("naics") != "62----":
                    continue
                key = row.get("fipstate", "") + row.get("fipscty", "")
                try:
                    out[key] = int(row.get("est", "0"))
                except ValueError:
                    out[key] = 0
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cces", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--vehicle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--minimum-population", type=int, default=100_000)
    args = parser.parse_args()

    population = read_population(args.population, args.minimum_population)
    vehicle = read_vehicle(args.vehicle)
    capacity = read_capacity(args.cbp)
    keys = set(population) & set(vehicle) & set(capacity)
    counties = []
    for key in sorted(keys):
        counties.append({
            "fips": key,
            "population": population[key]["population"],
            "growth": population[key]["growth"],
            "health_est_per_10k": 10_000 * capacity[key] / population[key]["population"],
            "zero_vehicle_pct": vehicle[key],
        })
    health_cut = statistics.median(row["health_est_per_10k"] for row in counties)
    vehicle_cut = statistics.median(row["zero_vehicle_pct"] for row in counties)
    for row in counties:
        row["cell"] = f"{'high' if row['health_est_per_10k'] >= health_cut else 'low'} health capacity / {'high' if row['zero_vehicle_pct'] >= vehicle_cut else 'low'} zero-vehicle share"
    place = {row["fips"]: row for row in counties}

    use = ["countyfips", "commonpostweight", "CC24_423", "CC24_424", "CC24_401", *ACTION_COLUMNS]
    sums: dict[str, dict[str, float | int]] = {}
    for chunk in pd.read_csv(args.cces, usecols=use, chunksize=100_000):
        chunk["fips"] = chunk["countyfips"].map(lambda value: str(int(value)).zfill(5) if pd.notna(value) else "")
        chunk["place"] = chunk["fips"].map(place)
        chunk = chunk[chunk["place"].notna()].copy()
        chunk = chunk[chunk["commonpostweight"].notna() & (chunk["commonpostweight"] > 0)]
        if chunk.empty:
            continue
        chunk["cell"] = chunk["place"].map(lambda row: row["cell"])
        for metric, valid, yes in [
            ("federal_trust", chunk["CC24_423"].isin([1, 2, 3, 8]), chunk["CC24_423"].isin([1, 2])),
            ("state_trust", chunk["CC24_424"].isin([1, 2, 3, 8]), chunk["CC24_424"].isin([1, 2])),
            ("civic_action", chunk[ACTION_COLUMNS].isin([1, 2]).all(axis=1), chunk[ACTION_COLUMNS].eq(1).any(axis=1)),
            ("reported_voted", chunk["CC24_401"].isin([1, 2, 3, 4, 5]), chunk["CC24_401"].eq(5)),
        ]:
            valid_part = chunk[valid]
            for cell, part in valid_part.groupby("cell", observed=True):
                entry = sums.setdefault(str(cell), {"unweighted_n": 0})
                entry[f"{metric}_valid_n"] = int(entry.get(f"{metric}_valid_n", 0)) + len(part)
                entry[f"{metric}_weight"] = float(entry.get(f"{metric}_weight", 0.0)) + part["commonpostweight"].sum()
                entry[f"{metric}_yes_weight"] = float(entry.get(f"{metric}_yes_weight", 0.0)) + part.loc[yes[valid], "commonpostweight"].sum()
                entry["unweighted_n"] = int(entry.get("unweighted_n", 0)) + len(part) if metric == "federal_trust" else entry.get("unweighted_n", 0)

    output = []
    for cell in sorted({row["cell"] for row in counties}):
        selected = [row for row in counties if row["cell"] == cell]
        entry = sums.get(cell, {})
        row = {
            "capacity_cell": cell,
            "counties_in_capacity_frame": len(selected),
            "ces_counties": sum(1 for key in place if place[key]["cell"] == cell),
            "ces_unweighted_n": entry.get("unweighted_n", 0),
            "median_population_change_pct": statistics.median(row["growth"] for row in selected),
            "health_capacity_cut": health_cut,
            "zero_vehicle_cut": vehicle_cut,
        }
        for metric in ["federal_trust", "state_trust", "civic_action", "reported_voted"]:
            denom = float(entry.get(f"{metric}_weight", 0.0))
            row[f"{metric}_valid_n"] = int(entry.get(f"{metric}_valid_n", 0))
            row[f"{metric}_weighted_pct"] = 100 * float(entry.get(f"{metric}_yes_weight", 0.0)) / denom if denom else ""
        output.append(row)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(output).to_csv(args.output, sep="\t", index=False, float_format="%.3f")


if __name__ == "__main__":
    main()
