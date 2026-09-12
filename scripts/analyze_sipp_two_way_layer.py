#!/usr/bin/env python3
"""Create a two-way person-weighted SIPP descriptive layer.

The supported grouping is tenure crossed with monthly household
income-to-poverty ratio bands. Target fields are summarized as code 1 among
nonblank records. This is a descriptive diagnostic, not a causal or
household-weighted estimate.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

from analyze_sipp_population_layer import add, finish, FIELD_LABELS, GROUP_VALUE_LABELS, group_value


def analyze(path: Path, fields: list[str]) -> dict:
    groups = defaultdict(lambda: {field: {"records": 0, "weight": 0.0,
                                           "blank_records": 0, "blank_weight": 0.0,
                                           "code1_records": 0, "code1_weight": 0.0}
                                 for field in fields})
    rows_read = 0
    positive_weight_rows = 0
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"ETENURE", "THINCPOV", "WPFINWGT", *fields}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if weight <= 0:
                continue
            tenure = row.get("ETENURE", "")
            poverty = group_value("THINCPOV", row.get("THINCPOV", ""))
            if not tenure or not poverty:
                continue
            positive_weight_rows += 1
            group = f"{tenure}|{poverty}"
            for field in fields:
                add(groups[group][field], row.get(field, ""), weight)
    for values in groups.values():
        for bucket in values.values():
            finish(bucket)
    return {
        "format": "us-sipp-person-weighted-two-way-layer-v1",
        "source_unit": "person record by reference month",
        "weight": "WPFINWGT (final person weight)",
        "grouping": ["ETENURE", "THINCPOV"],
        "group_value_labels": {"ETENURE": GROUP_VALUE_LABELS["ETENURE"],
                               "THINCPOV": GROUP_VALUE_LABELS["THINCPOV"]},
        "rows_read": rows_read,
        "positive_weight_rows_with_groups": positive_weight_rows,
        "fields": fields,
        "code1_labels": {field: FIELD_LABELS[field] for field in fields},
        "by_group": {group: groups[group] for group in sorted(groups)},
        "household_weight_used": False,
        "official_universes_constructed": False,
        "variance_estimation": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fields", nargs="+", choices=sorted(FIELD_LABELS),
                        default=["EAWBMORT", "EAWBGAS", "RFOODS", "EFOOD6", "EDEBT_CC", "RMNUMJOBS"])
    args = parser.parse_args()
    result = analyze(args.input, args.fields)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
