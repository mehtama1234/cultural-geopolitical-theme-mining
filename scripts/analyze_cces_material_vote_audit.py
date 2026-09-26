#!/usr/bin/env python3
"""Audit self-reported definite voting separately from the CCES action screen."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def income_band(value: str) -> str | None:
    try:
        code = int(value)
    except (TypeError, ValueError):
        return None
    if 1 <= code <= 4:
        return "lower_income_codes_1_4"
    if 5 <= code <= 9:
        return "middle_income_codes_5_9"
    if 10 <= code <= 16:
        return "higher_income_codes_10_16"
    return None


def race_group(value: str) -> str | None:
    if value == "1":
        return "white"
    if value == "2":
        return "black"
    if value == "3":
        return "hispanic"
    if value in {"4", "5", "6", "7", "8"}:
        return "other_or_multiracial"
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = {"commonpostweight", "faminc_new", "race", "gigwork", "edloan", "CC24_401"}
    cells = defaultdict(lambda: {"records": 0, "weight": 0.0, "definitely_voted": 0.0})
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
            iband = income_band(row["faminc_new"])
            rgroup = race_group(row["race"])
            vote = row["CC24_401"]
            if weight <= 0 or iband is None or rgroup is None:
                continue
            if row["gigwork"] not in {"1", "2"} or row["edloan"] not in {"1", "2"}:
                continue
            if vote not in {"1", "2", "3", "4", "5"}:
                continue
            key = f"income_{iband}|race_{rgroup}|gigwork_{'yes' if row['gigwork'] == '1' else 'no'}|student_debt_{'yes' if row['edloan'] == '1' else 'no'}"
            cell = cells[key]
            cell["records"] += 1
            cell["weight"] += weight
            cell["definitely_voted"] += weight * int(vote == "5")
            valid += 1

    for cell in cells.values():
        cell["percent_definitely_voted"] = 100 * cell["definitely_voted"] / cell["weight"] if cell["weight"] else None
    result = {
        "format": "us-cces-material-vote-audit-v1",
        "source_unit": "CCES 2024 post-election respondent with valid CC24_401 vote answer",
        "weight": "commonpostweight",
        "vote_field": "CC24_401 == 5 means definitely voted; codes 1-4 are retained in the valid-answer denominator",
        "rows_read": rows,
        "valid_records": valid,
        "cells": dict(sorted(cells.items())),
        "income_band_definition": "ordered faminc_new codes grouped 1-4, 5-9, and 10-16; 97/other excluded",
        "race_definition": "codes 1, 2, and 3 retained; codes 4, 5, 6, 7, and 8 combined as other_or_multiracial",
        "causal_estimation": False,
        "boundary": "This is a separate descriptive vote-answer audit. Its valid universe is not the 21,560-record material/trust/action universe, and CC24_401 is not treated as a validated turnout record or causal political outcome.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows, "valid_records": valid, "cells": len(cells)}, indent=2))


if __name__ == "__main__":
    main()
