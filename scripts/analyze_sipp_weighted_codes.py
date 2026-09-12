#!/usr/bin/env python3
"""Create weighted raw-code distributions from a selected SIPP slice.

The output is deliberately code-level. It does not guess labels for SIPP
special codes and treats the final person weight as a person-record weight,
not a household weight.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


DEFAULT_FIELDS = [
    "ETENURE", "EUTILITIES", "EENERGY_ASST", "EAWBMORT", "EAWBGAS",
    "EOWN_SAV", "EDEBT_CC", "RFOODS", "RFOODR", "EFOOD1", "EFOOD3",
    "EFOOD6", "EPAY", "EPAYHELP", "EWORKMORE", "RMNUMJOBS",
]


def empty_bucket() -> dict:
    return {"records": 0, "weight": 0.0, "blank_records": 0,
            "blank_weight": 0.0, "codes": {}}


def add_code(bucket: dict, code: str, weight: float) -> None:
    bucket["records"] += 1
    bucket["weight"] += weight
    if code == "":
        bucket["blank_records"] += 1
        bucket["blank_weight"] += weight
    else:
        item = bucket["codes"].setdefault(code, {"records": 0, "weight": 0.0})
        item["records"] += 1
        item["weight"] += weight


def analyze(path: Path, fields: list[str]) -> dict:
    overall = {field: empty_bucket() for field in fields}
    by_month = defaultdict(lambda: {field: empty_bucket() for field in fields})
    rows = 0
    positive_weight_rows = 0
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"MONTHCODE", "WPFINWGT", *fields}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows += 1
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if weight <= 0:
                continue
            positive_weight_rows += 1
            month = row["MONTHCODE"]
            for field in fields:
                code = row.get(field, "")
                add_code(overall[field], code, weight)
                add_code(by_month[month][field], code, weight)
    return {
        "format": "us-household-calendar-sipp-weighted-code-scan-v1",
        "source_unit": "person record by reference month",
        "weight": "WPFINWGT (final person weight)",
        "rows_read": rows,
        "positive_weight_rows": positive_weight_rows,
        "fields": fields,
        "overall": dict(overall),
        "by_month": {month: values for month, values in sorted(by_month.items())},
        "household_weight_used": False,
        "labels_inferred": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fields", nargs="+", default=DEFAULT_FIELDS)
    args = parser.parse_args()
    result = analyze(args.input, args.fields)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
