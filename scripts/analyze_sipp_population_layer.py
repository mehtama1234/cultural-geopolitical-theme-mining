#!/usr/bin/env python3
"""Create labeled, person-weighted descriptive SIPP population diagnostics.

The input is the selected SIPP person-record/month slice. For each field the
script reports the share with code 1 among all positive-weight records and
among nonblank records. The latter is a diagnostic for the observed nonblank
universe; it is not a substitute for constructing the official universe or
using the survey replicate weights.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


FIELD_LABELS = {
    "ETENURE": "owned or being bought",
    "EUTILITIES": "yes",
    "EENERGY_ASST": "yes",
    "EAWBMORT": "yes",
    "EAWBGAS": "yes",
    "EOWN_SAV": "yes",
    "EDEBT_CC": "yes",
    "RFOODS": "high or marginal food security",
    "RFOODR": "one affirmative response",
    "EFOOD1": "often true",
    "EFOOD3": "yes",
    "EFOOD6": "yes",
    "EPAY": "yes",
    "EPAYHELP": "yes",
    "EWORKMORE": "yes",
    "RMNUMJOBS": "one job",
}

GROUP_VALUE_LABELS = {
    "ETENURE": {"1": "owned or being bought", "2": "rented",
                 "3": "occupied without payment of rent"},
    "RMNUMJOBS": {str(i): ("no jobs" if i == 0 else f"{i} job" if i == 1
                            else f"{i} jobs") for i in range(18)},
    "THINCPOV": {"lt1": "below 1.00x poverty threshold",
                 "1to2": "1.00–1.99x poverty threshold",
                 "2to4": "2.00–3.99x poverty threshold",
                 "ge4": "4.00x poverty threshold or more"},
    "TEHC_REGION": {"1": "Northeast", "2": "Midwest", "3": "South", "4": "West"},
}


def empty() -> dict:
    return {"records": 0, "weight": 0.0, "blank_records": 0,
            "blank_weight": 0.0, "code1_records": 0, "code1_weight": 0.0}


def add(bucket: dict, code: str, weight: float) -> None:
    bucket["records"] += 1
    bucket["weight"] += weight
    if not code:
        bucket["blank_records"] += 1
        bucket["blank_weight"] += weight
    elif code == "1":
        bucket["code1_records"] += 1
        bucket["code1_weight"] += weight


def finish(bucket: dict) -> dict:
    valid_weight = bucket["weight"] - bucket["blank_weight"]
    valid_records = bucket["records"] - bucket["blank_records"]
    bucket["valid_records"] = valid_records
    bucket["valid_weight"] = valid_weight
    bucket["code1_share_all_percent"] = (
        100.0 * bucket["code1_weight"] / bucket["weight"]
        if bucket["weight"] else None
    )
    bucket["code1_share_nonblank_percent"] = (
        100.0 * bucket["code1_weight"] / valid_weight
        if valid_weight else None
    )
    return bucket


def group_value(field: str, value: str) -> str:
    if field != "THINCPOV":
        return value
    try:
        ratio = float(value)
    except (TypeError, ValueError):
        return ""
    if ratio < 1:
        return "lt1"
    if ratio < 2:
        return "1to2"
    if ratio < 4:
        return "2to4"
    return "ge4"


def analyze(path: Path, fields: list[str], group_by: str | None = None) -> dict:
    overall = {field: empty() for field in fields}
    by_month = defaultdict(lambda: {field: empty() for field in fields})
    by_group = defaultdict(lambda: {field: empty() for field in fields})
    rows_read = 0
    positive_weight_rows = 0
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"MONTHCODE", "WPFINWGT", *fields}
        if group_by:
            required.add(group_by)
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
            positive_weight_rows += 1
            month = row["MONTHCODE"]
            group = group_value(group_by, row.get(group_by, "")) if group_by else None
            for field in fields:
                add(overall[field], row.get(field, ""), weight)
                add(by_month[month][field], row.get(field, ""), weight)
                if group_by and group:
                    add(by_group[group][field], row.get(field, ""), weight)
    for field in fields:
        finish(overall[field])
    for month in by_month:
        for field in fields:
            finish(by_month[month][field])
    for group in by_group:
        for field in fields:
            finish(by_group[group][field])
    return {
        "format": "us-sipp-person-weighted-population-layer-v1",
        "source_unit": "person record by reference month",
        "weight": "WPFINWGT (final person weight)",
        "rows_read": rows_read,
        "positive_weight_rows": positive_weight_rows,
        "fields": fields,
        "group_by": group_by,
        "group_value_labels": GROUP_VALUE_LABELS.get(group_by, {}) if group_by else {},
        "code1_labels": {field: FIELD_LABELS[field] for field in fields},
        "overall": overall,
        "by_month": {month: by_month[month] for month in sorted(by_month)},
        "by_group": {group: by_group[group] for group in sorted(by_group)},
        "household_weight_used": False,
        "official_universes_constructed": False,
        "variance_estimation": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fields", nargs="+", default=list(FIELD_LABELS))
    parser.add_argument("--group-by", choices=sorted(GROUP_VALUE_LABELS), default=None)
    args = parser.parse_args()
    unknown = sorted(set(args.fields) - set(FIELD_LABELS))
    if unknown:
        raise ValueError("no verified code-1 labels for: " + ", ".join(unknown))
    result = analyze(args.input, args.fields, args.group_by)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
