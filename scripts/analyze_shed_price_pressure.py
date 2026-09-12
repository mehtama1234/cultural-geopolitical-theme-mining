#!/usr/bin/env python3
"""Weighted descriptive layer for the 2025 Federal Reserve SHED CSV."""

import argparse
import csv
import json
import zipfile
from collections import defaultdict


METRICS = {
    "price_worsened_finances": ("INF4", {"Much worse", "Somewhat worse"}),
    "switched_cheaper_products": ("INF3_a", {"Yes"}),
    "used_less_or_stopped": ("INF3_b", {"Yes"}),
    "reduced_savings": ("INF3_c", {"Yes"}),
    "increased_borrowing": ("INF3_d", {"Yes"}),
    "delayed_major_purchase": ("INF3_e", {"Yes"}),
    "worked_more_or_got_job": ("INF3_f", {"Yes"}),
    "moved_purchase_earlier": ("INF5", {"Yes"}),
    "three_month_emergency_funds": ("EF1", {"Yes"}),
    "outside_help_general_expenses": ("FS21_g", {"Yes"}),
    "outside_help_medical_or_health": ("FS21_c", {"Yes"}),
    "outside_help_car": ("FS21_d", {"Yes"}),
}

GROUPS = {
    "financial_condition": "B2",
    "year_change": "B3",
    "income": "ppinc7",
    "age": "ppagecat",
    "ethnicity": "ppethm",
    "employment": "ppemploy",
}


def clean(value):
    return (value or "").strip()


def metric_share(rows, metric):
    field, yes_values = METRICS[metric]
    numerator = denominator = 0.0
    for row in rows:
        value = clean(row.get(field))
        if not value:
            continue
        weight = float(row.get("weight") or 0)
        denominator += weight
        if value in yes_values:
            numerator += weight
    return {"percent": None if not denominator else round(100 * numerator / denominator, 3),
            "weighted_n": round(denominator, 1),
            "nonmissing_rows": sum(bool(clean(row.get(field))) for row in rows)}


def summarize(rows):
    result = {
        "rows": len(rows),
        "metrics": {name: metric_share(rows, name) for name in METRICS},
        "groups": {},
    }
    for group_name, field in GROUPS.items():
        buckets = defaultdict(list)
        for row in rows:
            value = clean(row.get(field))
            if value:
                buckets[value].append(row)
        result["groups"][group_name] = {
            label: {name: metric_share(bucket, name) for name in METRICS}
            for label, bucket in sorted(buckets.items())
        }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Official SHED CSV or CSV zip")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.input.lower().endswith(".zip"):
        with zipfile.ZipFile(args.input) as archive:
            names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
            if len(names) != 1:
                raise SystemExit(f"expected one CSV in archive, found {names}")
            with archive.open(names[0]) as handle:
                rows = list(csv.DictReader((line.decode("utf-8-sig") for line in handle)))
    else:
        with open(args.input, newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
    required = {"weight"} | {field for field, _ in METRICS.values()} | set(GROUPS.values())
    missing = sorted(required - set(rows[0])) if rows else sorted(required)
    if missing:
        raise SystemExit(f"missing required fields: {missing}")
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(summarize(rows), handle, indent=2, sort_keys=True)
        handle.write("\n")


if __name__ == "__main__":
    main()
