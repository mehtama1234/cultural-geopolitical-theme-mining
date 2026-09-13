#!/usr/bin/env python3
"""Weighted descriptive SHED housing and homeowners-insurance pressure."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from collections import defaultdict
from pathlib import Path

OWNER_TENURES = {"Own with mortgage": "Own your home with a mortgage or loan", "Own free and clear": "Own your home free and clear (without a mortgage or loan)"}
INCOME_BANDS = {
    "under_50k": {"Less than $10,000", "$10,000 to $24,999", "$25,000 to $49,999"},
    "50k_to_99k": {"$50,000 to $74,999", "$75,000 to $99,999"},
    "100k_or_more": {"$100,000 to $149,999", "$150,000 or more"},
}
METRICS = {
    "has_insurance": ("GH12", {"Yes"}),
    "shopped_around": ("GH15", {"Yes"}),
    "struggles_to_afford_premiums": ("GH16_b", {"Agree"}),
    "cost_up_more_than_expected": ("GH16_c", {"Agree"}),
    "wants_more_coverage_cannot_afford": ("GH16_d", {"Agree"}),
    "satisfied_with_coverage": ("GH16_e", {"Agree"}),
    "lender_requires_insurance": ("GH16_f", {"Agree"}),
}


def clean(value: str | None) -> str:
    return (value or "").strip()


def read_rows(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"expected one CSV in {path}, found {names}")
        with archive.open(names[0]) as handle:
            return list(csv.DictReader((line.decode("utf-8-sig") for line in handle)))


def share(rows: list[dict[str, str]], field: str, yes_values: set[str]) -> dict[str, float | int | None]:
    selected = [row for row in rows if clean(row.get(field))]
    denominator = sum(float(row.get("weight") or 0) for row in selected)
    numerator = sum(float(row.get("weight") or 0) for row in selected if clean(row.get(field)) in yes_values)
    return {
        "percent": round(100 * numerator / denominator, 3) if denominator else None,
        "weighted_denominator": round(denominator, 1),
        "nonmissing_rows": len(selected),
    }


def summarize(rows: list[dict[str, str]]) -> dict[str, object]:
    owners = [row for row in rows if clean(row.get("GH1")) in OWNER_TENURES.values()]
    mortgage_owners = [row for row in owners if clean(row.get("GH1")) == OWNER_TENURES["Own with mortgage"]]
    result: dict[str, object] = {
        "owner_rows": len(owners),
        "mortgage_owner_rows": len(mortgage_owners),
        "owners": {metric: share(owners, field, yes_values) for metric, (field, yes_values) in METRICS.items()},
        "mortgage_owners": {metric: share(mortgage_owners, field, yes_values) for metric, (field, yes_values) in METRICS.items()},
        "income_bands": {},
    }
    for band, labels in INCOME_BANDS.items():
        band_owners = [row for row in owners if clean(row.get("ppinc7")) in labels]
        result["income_bands"][band] = {
            "owner_rows": len(band_owners),
            "metrics": {metric: share(band_owners, field, yes_values) for metric, (field, yes_values) in METRICS.items()},
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = read_rows(args.input)
    required = {"weight", "GH1", "ppinc7"} | {field for field, _ in METRICS.values()}
    missing = sorted(required - set(rows[0] if rows else {}))
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))
    result = {
        "format": "us-shed-housing-insurance-pressure-v1",
        "source_unit": "US adult respondent, 2025 SHED",
        "weight": "weight",
        "variance_estimation": False,
        "causal_estimation": False,
        "rows": len(rows),
        **summarize(rows),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
