#!/usr/bin/env python3
"""Weighted SHED price adaptations by medical concern, care, and health."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from collections import defaultdict
from pathlib import Path

METRICS = {
    "price_worsened_finances": ("INF4", {"Much worse", "Somewhat worse"}),
    "cheaper_products": ("INF3_a", {"Yes"}),
    "used_less_or_stopped": ("INF3_b", {"Yes"}),
    "reduced_savings": ("INF3_c", {"Yes"}),
    "increased_borrowing": ("INF3_d", {"Yes"}),
    "delayed_major_purchase": ("INF3_e", {"Yes"}),
    "worked_more_or_got_job": ("INF3_f", {"Yes"}),
    "three_month_emergency_funds": ("EF1", {"Yes"}),
}
GROUPS = {
    "medical_cost_concern": "X12_f",
    "unpaid_adult_care": "CG4",
    "health_status": "pph10001",
    "medical_outside_help": "FS21_c",
}


def clean(value: str | None) -> str:
    return (value or "").strip()


def read_rows(path: Path) -> list[dict[str, str]]:
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as archive:
            names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
            if len(names) != 1:
                raise ValueError(f"expected one CSV in {path}, found {names}")
            with archive.open(names[0]) as handle:
                return list(csv.DictReader((line.decode("utf-8-sig") for line in handle)))
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def metric_share(rows: list[dict[str, str]], field: str, yes_values: set[str]) -> dict[str, float | int | None]:
    selected = [row for row in rows if clean(row.get(field))]
    denominator = sum(float(row.get("weight") or 0) for row in selected)
    numerator = sum(float(row.get("weight") or 0) for row in selected if clean(row.get(field)) in yes_values)
    return {
        "percent": round(100 * numerator / denominator, 3) if denominator else None,
        "weighted_denominator": round(denominator, 1),
        "nonmissing_rows": len(selected),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = read_rows(args.input)
    required = {"weight"} | {field for field, _ in METRICS.values()} | set(GROUPS.values())
    missing = sorted(required - set(rows[0] if rows else {}))
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))

    result: dict[str, object] = {
        "format": "us-shed-price-pressure-care-health-v1",
        "source_unit": "US adult respondent, 2025 SHED",
        "weight": "weight",
        "variance_estimation": False,
        "causal_estimation": False,
        "rows": len(rows),
        "groups": {},
    }
    for group_name, field in GROUPS.items():
        buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            value = clean(row.get(field))
            if value:
                buckets[value].append(row)
        result["groups"][group_name] = {
            label: {metric: metric_share(bucket, metric_field, yes_values)
                    for metric, (metric_field, yes_values) in METRICS.items()}
            for label, bucket in sorted(buckets.items())
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
