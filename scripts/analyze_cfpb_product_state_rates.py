#!/usr/bin/env python3
"""Normalize CFPB product-filtered complaint counts by Census state population."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import openpyxl


USPS = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI",
    "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
    "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
    "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
    "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
    "Wisconsin": "WI", "Wyoming": "WY",
}


def population(path: Path) -> dict[str, int]:
    ws = openpyxl.load_workbook(path, data_only=True, read_only=True).active
    result = {}
    for row in ws.iter_rows(min_row=9, values_only=True):
        name, value = row[0], row[6]
        if isinstance(name, str) and name.startswith(".") and isinstance(value, (int, float)):
            state = name[1:]
            if state in USPS:
                result[USPS[state]] = int(value)
    return result


def parse_slice(value: str) -> tuple[str, Path]:
    name, separator, path = value.partition("=")
    if not separator or not name or not path:
        raise argparse.ArgumentTypeError("slice must be NAME=JSON_PATH")
    return name, Path(path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--slice", dest="slices", type=parse_slice, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    pops = population(args.population)
    output = {"format": "us-cfpb-product-state-rates-v1", "population_year": 2024, "products": {}}
    for name, path in args.slices:
        data = json.loads(path.read_text(encoding="utf-8"))
        buckets = data["aggregations"]["state"]["state"]["buckets"]
        states = {}
        for bucket in buckets:
            state = bucket["key"]
            if state not in pops:
                continue
            count = int(bucket["doc_count"])
            states[state] = {
                "complaints": count,
                "population": pops[state],
                "per_100k": 100_000 * count / pops[state],
            }
        output["products"][name] = {
            "filtered_total": data["hits"]["total"]["value"],
            "matched_state_total": sum(item["complaints"] for item in states.values()),
            "states": states,
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
