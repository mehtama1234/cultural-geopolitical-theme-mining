#!/usr/bin/env python3
"""Cross CES local trust/action context by growth and foreign-born quartiles."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import pandas as pd

from analyze_ces_local_trust_action_by_growth import ACTION_COLUMNS, USE_COLUMNS, read_population


METRICS = [
    ("federal_trust", "CC24_423", [1, 2, 3, 8], [1, 2]),
    ("state_trust", "CC24_424", [1, 2, 3, 8], [1, 2]),
    ("voted", "CC24_401", [1, 2, 3, 4, 5], [5]),
]


def read_nativity(path: Path) -> dict[str, float]:
    values = {}
    with path.open(newline="", encoding="latin1") as handle:
        for row in csv.DictReader(handle, delimiter="|"):
            match = re.search(r"(\d{5})$", row.get("GEO_ID", ""))
            try:
                total = int(row["B05002_E001"])
                foreign_born = int(row["B05002_E003"])
            except (KeyError, TypeError, ValueError):
                continue
            if match and total > 0:
                values[match.group(1)] = 100 * foreign_born / total
    return values


def add_metrics(target: dict, part: pd.DataFrame) -> None:
    target["unweighted_n"] = target.get("unweighted_n", 0) + len(part)
    for metric, column, valid_codes, yes_codes in METRICS:
        valid = part[column].isin(valid_codes)
        valid_part = part[valid]
        target[f"{metric}_valid_n"] = target.get(f"{metric}_valid_n", 0) + len(valid_part)
        target[f"{metric}_weight"] = target.get(f"{metric}_weight", 0.0) + valid_part["weight"].sum()
        target[f"{metric}_yes_weight"] = target.get(f"{metric}_yes_weight", 0.0) + valid_part.loc[valid_part[column].isin(yes_codes), "weight"].sum()

    action_valid = part[ACTION_COLUMNS].isin([1, 2]).all(axis=1)
    action_part = part[action_valid]
    target["civic_action_valid_n"] = target.get("civic_action_valid_n", 0) + len(action_part)
    target["civic_action_weight"] = target.get("civic_action_weight", 0.0) + action_part["weight"].sum()
    target["civic_action_yes_weight"] = target.get("civic_action_yes_weight", 0.0) + action_part.loc[action_part[ACTION_COLUMNS].eq(1).any(axis=1), "weight"].sum()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cces", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--nativity", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--minimum-population", type=int, default=100_000)
    args = parser.parse_args()

    places = read_population(args.population, args.minimum_population)
    nativity = read_nativity(args.nativity)
    places["foreign_born_pct"] = places["fips"].map(nativity)
    places = places[places["foreign_born_pct"].notna()].copy()
    places["nativity_quartile"] = pd.qcut(
        places["foreign_born_pct"], 4, labels=["Q1 lowest", "Q2", "Q3", "Q4 highest"]
    )
    place_lookup = places.set_index("fips")["growth_quartile"].astype(str).to_dict()
    nativity_lookup = places.set_index("fips")["nativity_quartile"].astype(str).to_dict()

    counts = {}
    for chunk in pd.read_csv(args.cces, usecols=USE_COLUMNS, chunksize=100_000):
        chunk["fips"] = chunk["countyfips"].map(lambda value: str(int(value)).zfill(5) if pd.notna(value) else "")
        chunk["growth_quartile"] = chunk["fips"].map(place_lookup)
        chunk["nativity_quartile"] = chunk["fips"].map(nativity_lookup)
        chunk = chunk[chunk["growth_quartile"].notna() & chunk["nativity_quartile"].notna()].copy()
        chunk = chunk[chunk["commonpostweight"].notna() & (chunk["commonpostweight"] > 0)]
        chunk["weight"] = chunk["commonpostweight"]
        for key, part in chunk.groupby(["growth_quartile", "nativity_quartile"], observed=True):
            add_metrics(counts.setdefault((str(key[0]), str(key[1])), {}), part)

    rows = []
    for growth in ["Q1 lowest", "Q2", "Q3", "Q4 highest"]:
        for nativity_q in ["Q1 lowest", "Q2", "Q3", "Q4 highest"]:
            group = places[(places["growth_quartile"].astype(str) == growth) & (places["nativity_quartile"].astype(str) == nativity_q)]
            entry = counts.get((growth, nativity_q), {})
            row = {
                "growth_quartile": growth,
                "nativity_quartile": nativity_q,
                "place_count": len(group),
                "ces_unweighted_n": entry.get("unweighted_n", 0),
                "median_pop_change_pct": group["pop_change_pct"].median(),
                "median_foreign_born_pct": group["foreign_born_pct"].median(),
            }
            for metric in ["federal_trust", "state_trust", "civic_action", "voted"]:
                denominator = entry.get(f"{metric}_weight", 0.0)
                row[f"{metric}_valid_n"] = entry.get(f"{metric}_valid_n", 0)
                row[f"{metric}_weighted_pct"] = 100 * entry.get(f"{metric}_yes_weight", 0.0) / denominator if denominator else ""
            rows.append(row)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(args.output, sep="\t", index=False, float_format="%.3f")


if __name__ == "__main__":
    main()
