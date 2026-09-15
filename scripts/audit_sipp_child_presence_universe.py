#!/usr/bin/env python3
"""Audit monthly child presence against the SIPP reference-parent universe.

This is a diagnostic, not an estimator.  It keeps the person-month unit and
shows why RHNUMU18 (monthly household composition) must not be treated as the
ERP/reference-parent universe used by fall or December child-care questions.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


CARE_FIELDS = ("EPAY", "EPAYHELP", "EWORKMORE", "ETIMELOST")


def add(bucket: dict, row: dict[str, str], weight: float) -> None:
    bucket["rows"] += 1
    bucket["weight"] += weight
    if row.get("ERP", "") == "1":
        bucket["erp_yes_rows"] += 1
        bucket["erp_yes_weight"] += weight
    if row.get("RHNUMU18", "") not in {"", "0"}:
        bucket["monthly_under18_rows"] += 1
        bucket["monthly_under18_weight"] += weight
    for field in CARE_FIELDS:
        if row.get(field, ""):
            bucket.setdefault("care_nonblank_rows", {}).setdefault(field, 0)
            bucket["care_nonblank_rows"][field] += 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    overall = defaultdict(lambda: {"rows": 0, "weight": 0.0,
                                    "erp_yes_rows": 0, "erp_yes_weight": 0.0,
                                    "monthly_under18_rows": 0,
                                    "monthly_under18_weight": 0.0})
    by_month = defaultdict(lambda: defaultdict(lambda: {"rows": 0, "weight": 0.0,
                                                         "erp_yes_rows": 0, "erp_yes_weight": 0.0,
                                                         "monthly_under18_rows": 0,
                                                         "monthly_under18_weight": 0.0}))
    rows = positive = 0
    with args.input.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"MONTHCODE", "WPFINWGT", "ERP", "RHNUMU18", *CARE_FIELDS}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("input is missing fields: " + ", ".join(missing))
        for row in reader:
            rows += 1
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if weight <= 0:
                continue
            positive += 1
            month = row["MONTHCODE"]
            monthly_group = "under18_present" if row.get("RHNUMU18", "") not in {"", "0"} else "under18_zero"
            add(overall[monthly_group], row, weight)
            add(by_month[month][monthly_group], row, weight)
    report = {
        "format": "us-sipp-child-presence-reference-parent-audit-v1",
        "source_unit": "positive-weight SIPP person record by reference month",
        "rows_read": rows,
        "positive_weight_rows": positive,
        "groups": {group: dict(values) for group, values in overall.items()},
        "by_month": {month: {group: dict(values) for group, values in groups.items()}
                      for month, groups in sorted(by_month.items())},
        "interpretation_boundary": "RHNUMU18 is monthly household composition; ERP is an adult reference-parent indicator. Child-care fields use additional fall/December and child-age universes. This audit does not estimate household prevalence or causal care effects.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
