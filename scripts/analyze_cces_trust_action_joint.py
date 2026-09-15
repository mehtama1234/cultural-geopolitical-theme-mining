#!/usr/bin/env python3
"""Stream CCES material/work proxy and joint trust/action quadrants."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

ACTION_FIELDS = [f"CC24_430a_{i}" for i in range(1, 7)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    required = {"commonpostweight", "gigwork", "edloan", "CC24_423", "CC24_424", *ACTION_FIELDS}
    cells = defaultdict(lambda: {"records": 0, "weight": 0.0, "quadrants": defaultdict(lambda: {"records": 0, "weight": 0.0})})
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
            if row["CC24_423"] not in {"1", "2", "3"} or row["CC24_424"] not in {"1", "2", "3"} or not all(row[x] in {"1", "2"} for x in ACTION_FIELDS):
                continue
            proxy = f"gigwork={'yes' if row['gigwork'] == '1' else 'no'}|student_debt={'yes' if row['edloan'] == '1' else 'no'}"
            federal = row["CC24_423"] in {"1", "2"}
            state = row["CC24_424"] in {"1", "2"}
            action = any(row[x] == "1" for x in ACTION_FIELDS)
            cell = cells[proxy]
            cell["records"] += 1
            cell["weight"] += weight
            for name, positive in (("federal_trust", federal), ("state_trust", state)):
                q = f"{name}={'yes' if positive else 'no'}|any_civic_action={'yes' if action else 'no'}"
                cell["quadrants"][q]["records"] += 1
                cell["quadrants"][q]["weight"] += weight
            valid += 1
    for cell in cells.values():
        for q in cell["quadrants"].values():
            q["share_percent"] = 100 * q["weight"] / cell["weight"] if cell["weight"] else None
    result = {"format": "us-cces-trust-action-joint-v1", "source_unit": "CCES 2024 post-election respondent", "weight": "commonpostweight", "rows_read": rows, "valid_records": valid, "cells": dict(sorted(cells.items())), "causal_estimation": False, "variance_estimate": "not computed; descriptive weighted comparison only", "boundary": "Trust and civic action are separate respondent outcomes. Gig work and student-loan responsibility are material/work proxies, not dated shocks. Joint quadrants show co-occurrence patterns and do not establish causation, persuasion, or political efficacy."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows, "valid_records": valid, "cells": len(cells)}, indent=2))


if __name__ == "__main__":
    main()
