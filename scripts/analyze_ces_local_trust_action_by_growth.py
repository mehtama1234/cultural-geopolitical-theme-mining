#!/usr/bin/env python3
"""Summarize CES local trust and civic action by county growth quartile.

This is a descriptive contextual layer. It does not estimate immigration
attitudes or a county-level causal effect. The CES common file supplies county
FIPS, trust/action items, and survey weights; Census population estimates
define the place-growth context.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import pandas as pd


ACTION_COLUMNS = [f"CC24_430a_{i}" for i in range(1, 7)]
USE_COLUMNS = [
    "countyfips",
    "commonpostweight",
    "CC24_423",
    "CC24_424",
    "CC24_401",
    *ACTION_COLUMNS,
]


def read_population(path: Path, minimum: int) -> pd.DataFrame:
    rows = []
    with path.open(newline="", encoding="latin1") as handle:
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
            fips = str(row["STATE"]).zfill(2) + str(row["COUNTY"]).zfill(3)
            rows.append(
                {
                    "fips": fips,
                    "county": row["CTYNAME"],
                    "pop_change_pct": 100 * (pop23 / pop20 - 1),
                }
            )
    frame = pd.DataFrame(rows).sort_values("pop_change_pct")
    frame["growth_quartile"] = pd.qcut(
        frame["pop_change_pct"], 4, labels=["Q1 lowest", "Q2", "Q3", "Q4 highest"]
    )
    return frame


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cces", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--minimum-population", type=int, default=100_000)
    args = parser.parse_args()

    places = read_population(args.population, args.minimum_population)
    place_lookup = places.set_index("fips")["growth_quartile"].to_dict()
    counts = {}
    for chunk in pd.read_csv(args.cces, usecols=USE_COLUMNS, chunksize=100_000):
        chunk["fips"] = chunk["countyfips"].map(
            lambda value: str(int(value)).zfill(5) if pd.notna(value) else ""
        )
        chunk["growth_quartile"] = chunk["fips"].map(place_lookup)
        chunk = chunk[chunk["growth_quartile"].notna()].copy()
        chunk = chunk[chunk["commonpostweight"].notna()]
        chunk = chunk[chunk["commonpostweight"] > 0]
        if chunk.empty:
            continue

        chunk["weight"] = chunk["commonpostweight"]
        chunk["trust_federal_valid"] = chunk["CC24_423"].isin([1, 2, 3, 8])
        chunk["trust_state_valid"] = chunk["CC24_424"].isin([1, 2, 3, 8])
        chunk["vote_valid"] = chunk["CC24_401"].isin([1, 2, 3, 4, 5])
        chunk["action_valid"] = chunk[ACTION_COLUMNS].isin([1, 2]).all(axis=1)
        chunk["trust_federal_yes"] = chunk["CC24_423"].isin([1, 2])
        chunk["trust_state_yes"] = chunk["CC24_424"].isin([1, 2])
        chunk["voted_yes"] = chunk["CC24_401"].eq(5)
        chunk["action_yes"] = chunk[ACTION_COLUMNS].eq(1).any(axis=1)

        for group, part in chunk.groupby("growth_quartile", observed=True):
            entry = counts.setdefault(str(group), {"unweighted_n": 0})
            entry["unweighted_n"] += len(part)
            for metric, valid, yes in [
                ("federal_trust", "trust_federal_valid", "trust_federal_yes"),
                ("state_trust", "trust_state_valid", "trust_state_yes"),
                ("civic_action", "action_valid", "action_yes"),
                ("voted", "vote_valid", "voted_yes"),
            ]:
                valid_part = part[part[valid]]
                entry[f"{metric}_valid_n"] = entry.get(f"{metric}_valid_n", 0) + len(valid_part)
                entry[f"{metric}_weight"] = entry.get(f"{metric}_weight", 0.0) + valid_part["weight"].sum()
                entry[f"{metric}_yes_weight"] = entry.get(f"{metric}_yes_weight", 0.0) + valid_part.loc[valid_part[yes], "weight"].sum()

    county_counts = (
        pd.read_csv(args.cces, usecols=["countyfips"], dtype={"countyfips": "string"})
        .assign(fips=lambda x: x["countyfips"].str.replace(r"\.0$", "", regex=True).str.zfill(5))
        .query("fips in @place_lookup")
        .assign(growth_quartile=lambda x: x["fips"].map(place_lookup))
        .groupby("growth_quartile")["fips"]
        .nunique()
        .to_dict()
    )

    output_rows = []
    order = ["Q1 lowest", "Q2", "Q3", "Q4 highest"]
    for group in order:
        entry = counts.get(group, {"unweighted_n": 0})
        row = {
            "growth_quartile": group,
            "place_count": int((places["growth_quartile"] == group).sum()),
            "ces_counties": int(county_counts.get(group, 0)),
            "ces_unweighted_n": entry.get("unweighted_n", 0),
            "median_pop_change_pct": float(places.loc[places["growth_quartile"] == group, "pop_change_pct"].median()),
        }
        for metric in ["federal_trust", "state_trust", "civic_action", "voted"]:
            denominator = entry.get(f"{metric}_weight", 0.0)
            row[f"{metric}_valid_n"] = entry.get(f"{metric}_valid_n", 0)
            row[f"{metric}_weighted_pct"] = 100 * entry.get(f"{metric}_yes_weight", 0.0) / denominator if denominator else ""
        output_rows.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(output_rows).to_csv(args.output, sep="\t", index=False, float_format="%.3f")


if __name__ == "__main__":
    main()
