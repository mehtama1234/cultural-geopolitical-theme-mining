#!/usr/bin/env python3
"""Stream weighted CCES material-proxy/trust/action results by subgroups."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


ACTION_FIELDS = [f"CC24_430a_{i}" for i in range(1, 7)]


def income_band(value: str) -> str | None:
    # faminc_new is an ordered 16-category CCES family-income measure.
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
    labels = {"1": "white", "2": "black", "3": "hispanic"}
    if value in labels:
        return labels[value]
    if value in {"4", "5", "6", "7", "8"}:
        return "other_or_multiracial"
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = {
        "commonpostweight", "faminc_new", "race", "gigwork", "edloan",
        "CC24_423", "CC24_424", *ACTION_FIELDS,
    }
    cells = defaultdict(lambda: {
        "records": 0, "weight": 0.0,
        "outcomes": defaultdict(lambda: {"records": 0, "weight": 0.0, "numerator": 0.0}),
    })
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
            if weight <= 0 or iband is None or rgroup is None:
                continue
            if row["gigwork"] not in {"1", "2"} or row["edloan"] not in {"1", "2"}:
                continue
            if row["CC24_423"] not in {"1", "2", "3"} or row["CC24_424"] not in {"1", "2", "3"}:
                continue
            if not all(row[field] in {"1", "2"} for field in ACTION_FIELDS):
                continue
            proxy = f"gigwork_{'yes' if row['gigwork'] == '1' else 'no'}|student_debt_{'yes' if row['edloan'] == '1' else 'no'}"
            key = f"income_{iband}|race_{rgroup}|{proxy}"
            cell = cells[key]
            cell["records"] += 1
            cell["weight"] += weight
            outcomes = {
                "federal_trust": row["CC24_423"] in {"1", "2"},
                "state_trust": row["CC24_424"] in {"1", "2"},
                "any_civic_action": any(row[field] == "1" for field in ACTION_FIELDS),
            }
            for measure, positive in outcomes.items():
                outcome = cell["outcomes"][measure]
                outcome["records"] += 1
                outcome["weight"] += weight
                outcome["numerator"] += weight * int(positive)
            valid += 1

    for cell in cells.values():
        for outcome in cell["outcomes"].values():
            outcome["percent"] = 100 * outcome["numerator"] / outcome["weight"] if outcome["weight"] else None
    result = {
        "format": "us-cces-material-trust-action-subgroups-v1",
        "source_unit": "CCES 2024 post-election respondent",
        "weight": "commonpostweight",
        "rows_read": rows,
        "valid_records": valid,
        "cells": dict(sorted(cells.items())),
        "income_band_definition": "ordered faminc_new codes grouped 1-4, 5-9, and 10-16; 97/other excluded",
        "race_definition": "codes 1, 2, and 3 retained; codes 4, 5, 6, 7, and 8 combined as other_or_multiracial",
        "causal_estimation": False,
        "boundary": "Subgroup estimates are descriptive weighted comparisons of material/work proxies, trust, and civic action; no timing, complex-design variance, or causal claim is made.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows, "valid_records": valid, "cells": len(cells)}, indent=2))


if __name__ == "__main__":
    main()
