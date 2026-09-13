#!/usr/bin/env python3
"""Measure adjacent-month transitions for identified SIPP person records.

This is a descriptive person-level transition diagnostic. It uses the weight
from the first month of each adjacent pair, excludes pairs with blank values
for the target field, and does not estimate variance or causality.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


TARGETS = {
    "EAWBMORT": {"1": "yes", "2": "no"},
    "EAWBGAS": {"1": "yes", "2": "no"},
    "RFOODS": {"1": "high_or_marginal", "2": "low", "3": "very_low"},
    "EFOOD6": {"1": "yes", "2": "no"},
    "RMNUMJOBS": None,
    "THINCPOV": None,
    "RSNAP_MNYN": {"1": "yes", "2": "no"},
}


def classify(field: str, value: str) -> str | None:
    if field == "RMNUMJOBS":
        try:
            return str(int(value))
        except (TypeError, ValueError):
            return None
    if field == "THINCPOV":
        try:
            ratio = float(value)
        except (TypeError, ValueError):
            return None
        if ratio < 1:
            return "below_1x"
        if ratio < 2:
            return "1_to_2x"
        if ratio < 4:
            return "2_to_4x"
        return "4x_or_more"
    return TARGETS[field].get(value)


def analyze(path: Path, fields: list[str]) -> dict:
    people: dict[tuple[str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"SSUID", "SHHADID", "PNUM", "MONTHCODE", "WPFINWGT", *fields}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                month = int(row["MONTHCODE"])
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if not 1 <= month <= 12 or weight <= 0:
                continue
            key = (row["SSUID"], row["SHHADID"], row["PNUM"])
            people[key][month] = {"weight": str(weight), **{f: row.get(f, "") for f in fields}}

    result = {}
    adjacent_pairs = 0
    complete_persons = 0
    for months in people.values():
        if len(months) == 12 and all(m in months for m in range(1, 13)):
            complete_persons += 1
        for month in range(1, 12):
            if month not in months or month + 1 not in months:
                continue
            adjacent_pairs += 1
            first, second = months[month], months[month + 1]
            try:
                weight = float(first["weight"])
            except ValueError:
                continue
            for field in fields:
                before, after = classify(field, first[field]), classify(field, second[field])
                if before is None or after is None:
                    continue
                item = result.setdefault(field, {"pairs": 0, "weight": 0.0, "transitions": {}})
                item["pairs"] += 1
                item["weight"] += weight
                transition = item["transitions"].setdefault(f"{before} -> {after}", {"pairs": 0, "weight": 0.0})
                transition["pairs"] += 1
                transition["weight"] += weight

    for field, item in result.items():
        for transition in item["transitions"].values():
            transition["share_percent"] = 100 * transition["weight"] / item["weight"] if item["weight"] else None
    return {
        "format": "us-sipp-person-adjacent-transitions-v1",
        "source_unit": "identified person record, adjacent reference months",
        "weight": "WPFINWGT from first month of pair",
        "rows_read": rows_read,
        "identified_persons": len(people),
        "persons_with_all_12_months": complete_persons,
        "adjacent_month_pairs_available": adjacent_pairs,
        "fields": fields,
        "targets": TARGETS,
        "results": result,
        "household_weight_used": False,
        "variance_estimation": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fields", nargs="+", choices=sorted(TARGETS), default=list(TARGETS))
    args = parser.parse_args()
    result = analyze(args.input, args.fields)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
