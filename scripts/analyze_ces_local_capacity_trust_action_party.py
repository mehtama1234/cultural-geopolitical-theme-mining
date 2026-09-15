#!/usr/bin/env python3
"""Estimate capacity-cell political context separately by broad CES party identity."""

from __future__ import annotations

import argparse
import statistics
from pathlib import Path

import pandas as pd

from analyze_ces_local_capacity_trust_action import read_capacity, read_population, read_vehicle


ACTION_COLUMNS = [f"CC24_430a_{i}" for i in range(1, 7)]


def party_group(value: object) -> str | None:
    try:
        code = int(float(value))
    except (TypeError, ValueError):
        return None
    if code in {1, 2, 3}:
        return "Democratic-leaning (pid7 1–3)"
    if code == 4:
        return "Independent (pid7 4)"
    if code in {5, 6, 7}:
        return "Republican-leaning (pid7 5–7)"
    return "Other/unknown"


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
            "health": 10_000 * capacity[key] / population[key]["population"],
            "vehicle": vehicle[key],
        })
    health_cut = statistics.median(row["health"] for row in counties)
    vehicle_cut = statistics.median(row["vehicle"] for row in counties)
    place = {}
    for row in counties:
        row["cell"] = f"{'high' if row['health'] >= health_cut else 'low'} health capacity / {'high' if row['vehicle'] >= vehicle_cut else 'low'} zero-vehicle share"
        place[row["fips"]] = row

    use = ["countyfips", "commonpostweight", "pid7", "CC24_423", "CC24_424", "CC24_401", *ACTION_COLUMNS]
    sums: dict[tuple[str, str], dict[str, float | int]] = {}
    for chunk in pd.read_csv(args.cces, usecols=use, chunksize=100_000):
        chunk["fips"] = chunk["countyfips"].map(lambda value: str(int(value)).zfill(5) if pd.notna(value) else "")
        chunk["place"] = chunk["fips"].map(place)
        chunk = chunk[chunk["place"].notna()].copy()
        chunk = chunk[chunk["commonpostweight"].notna() & (chunk["commonpostweight"] > 0)]
        chunk["party"] = chunk["pid7"].map(party_group)
        chunk = chunk[chunk["party"].notna()]
        if chunk.empty:
            continue
        chunk["cell"] = chunk["place"].map(lambda row: row["cell"])
        metrics = [
            ("federal_trust", chunk["CC24_423"].isin([1, 2, 3, 8]), chunk["CC24_423"].isin([1, 2])),
            ("state_trust", chunk["CC24_424"].isin([1, 2, 3, 8]), chunk["CC24_424"].isin([1, 2])),
            ("civic_action", chunk[ACTION_COLUMNS].isin([1, 2]).all(axis=1), chunk[ACTION_COLUMNS].eq(1).any(axis=1)),
            ("reported_voted", chunk["CC24_401"].isin([1, 2, 3, 4, 5]), chunk["CC24_401"].eq(5)),
        ]
        for metric, valid, yes in metrics:
            valid_part = chunk[valid]
            for (cell, party), part in valid_part.groupby(["cell", "party"], observed=True):
                entry = sums.setdefault((str(cell), str(party)), {"unweighted_n": 0})
                entry[f"{metric}_valid_n"] = int(entry.get(f"{metric}_valid_n", 0)) + len(part)
                entry[f"{metric}_weight"] = float(entry.get(f"{metric}_weight", 0.0)) + part["commonpostweight"].sum()
                entry[f"{metric}_yes_weight"] = float(entry.get(f"{metric}_yes_weight", 0.0)) + part.loc[yes[valid_part.index], "commonpostweight"].sum()
                if metric == "federal_trust":
                    entry["unweighted_n"] = int(entry.get("unweighted_n", 0)) + len(part)

    output = []
    for (cell, party), entry in sorted(sums.items()):
        selected = [row for row in counties if row["cell"] == cell]
        row = {"capacity_cell": cell, "party_group": party, "counties_in_capacity_frame": len(selected), "ces_unweighted_n": entry.get("unweighted_n", 0), "median_population_change_pct": statistics.median(row["growth"] for row in selected), "health_capacity_cut": health_cut, "zero_vehicle_cut": vehicle_cut}
        for metric in ["federal_trust", "state_trust", "civic_action", "reported_voted"]:
            denom = float(entry.get(f"{metric}_weight", 0.0))
            row[f"{metric}_valid_n"] = int(entry.get(f"{metric}_valid_n", 0))
            row[f"{metric}_weighted_pct"] = 100 * float(entry.get(f"{metric}_yes_weight", 0.0)) / denom if denom else ""
        output.append(row)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(output).to_csv(args.output, sep="\t", index=False, float_format="%.3f")


if __name__ == "__main__":
    main()
