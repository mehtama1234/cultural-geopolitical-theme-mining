#!/usr/bin/env python3
"""Stream a weighted CCES material-proxy × trust/action comparison."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


ACTION_FIELDS = [f"CC24_430a_{i}" for i in range(1, 7)]


def yes(value: str) -> bool:
    return value == "1"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = {"commonpostweight", "gigwork", "edloan", "CC24_423", "CC24_424", "CC24_401", *ACTION_FIELDS}
    cells = defaultdict(lambda: {"base_weight": 0.0, "base_records": 0,
                                 "outcomes": defaultdict(lambda: {"weight": 0.0,
                                                                    "numerator": 0.0,
                                                                    "records": 0})})
    rows = 0
    valid = 0
    with args.input.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("missing required fields: " + ", ".join(missing))
        for row in reader:
            rows += 1
            try:
                weight = float(row["commonpostweight"])
            except (TypeError, ValueError):
                continue
            if weight <= 0 or row["gigwork"] not in {"1", "2"} or row["edloan"] not in {"1", "2"}:
                continue
            if row["CC24_423"] not in {"1", "2", "3"} or row["CC24_424"] not in {"1", "2", "3"}:
                continue
            key = f"gigwork_{'yes' if yes(row['gigwork']) else 'no'}|student_debt_{'yes' if yes(row['edloan']) else 'no'}"
            cell = cells[key]
            cell["base_records"] += 1
            cell["base_weight"] += weight
            outcomes = {
                "federal_trust": (row["CC24_423"] in {"1", "2"}),
                "state_trust": (row["CC24_424"] in {"1", "2"}),
            }
            if all(row[field] in {"1", "2"} for field in ACTION_FIELDS):
                outcomes["any_civic_action"] = any(yes(row[field]) for field in ACTION_FIELDS)
            if row["CC24_401"] in {"1", "2", "3", "4", "5"}:
                outcomes["voted"] = row["CC24_401"] == "5"
            for measure, positive in outcomes.items():
                cell["outcomes"][measure]["records"] += 1
                cell["outcomes"][measure]["weight"] += weight
                cell["outcomes"][measure]["numerator"] += weight * (1 if positive else 0)
            valid += 1

    for cell in cells.values():
        for measure, outcome in cell["outcomes"].items():
            outcome["percent"] = (100 * outcome["numerator"] / outcome["weight"]
                                   if outcome["weight"] else None)

    result = {
        "format": "us-cces-material-trust-action-v1",
        "source_unit": "CCES 2024 post-election respondent",
        "weight": "commonpostweight",
        "rows_read": rows,
        "valid_records": valid,
        "cells": dict(sorted(cells.items())),
        "causal_estimation": False,
        "boundary": "Gig work and student debt are material/work proxies; trust and action are respondent measures; this is descriptive and not a causal event study.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
