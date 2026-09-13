#!/usr/bin/env python3
"""Weighted descriptive SHED panel adaptation by income and condition path."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from collections import defaultdict
from pathlib import Path

CONDITIONS = [
    "Finding it difficult to get by",
    "Just getting by",
    "Doing okay",
    "Living comfortably",
]
INCOME_BANDS = {
    "under_50k": {"Less than $10,000", "$10,000 to $24,999", "$25,000 to $49,999"},
    "50k_to_99k": {"$50,000 to $74,999", "$75,000 to $99,999"},
    "100k_or_more": {"$100,000 to $149,999", "$150,000 or more"},
}
METRICS = {
    "cheaper_products": "INF3_a",
    "used_less_or_stopped": "INF3_b",
    "reduced_savings": "INF3_c",
    "increased_borrowing": "INF3_d",
    "delayed_major_purchase": "INF3_e",
    "worked_more_or_got_job": "INF3_f",
    "emergency_funds": "EF1",
}


def read_zip(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"expected one CSV in {path}, found {names}")
        with archive.open(names[0]) as handle:
            return list(csv.DictReader((line.decode("utf-8-sig") for line in handle)))


def clean(value: str | None) -> str:
    return (value or "").strip()


def condition_path(before: str, after: str) -> str:
    before_i, after_i = CONDITIONS.index(before), CONDITIONS.index(after)
    if after_i < before_i:
        return "worsened"
    if after_i > before_i:
        return "improved"
    return "same broad condition"


def income_band(value: str) -> str | None:
    for band, labels in INCOME_BANDS.items():
        if value in labels:
            return band
    return None


def share(pairs: list[tuple[dict[str, str], dict[str, str], float]], field: str, prior: str | None) -> dict[str, float | int | None]:
    selected = [
        pair for pair in pairs
        if clean(pair[0].get(field)) in ({"Yes", "No"} if prior is None else {prior})
        and clean(pair[1].get(field)) in {"Yes", "No"}
    ]
    denominator = sum(pair[2] for pair in selected)
    yes_weight = sum(pair[2] for pair in selected if clean(pair[1].get(field)) == "Yes")
    return {
        "valid_pairs": len(selected),
        "weighted_share_yes_2025_percent": round(100 * yes_weight / denominator, 3) if denominator else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", type=Path, required=True)
    parser.add_argument("--new", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    old = {clean(row.get("shedid")): row for row in read_zip(args.old)}
    pairs: list[tuple[dict[str, str], dict[str, str], float, str, str]] = []
    for row in read_zip(args.new):
        identifier = clean(row.get("shedid"))
        if identifier not in old or not clean(row.get("panel_weight")):
            continue
        before, after = clean(old[identifier].get("B2")), clean(row.get("B2"))
        band = income_band(clean(row.get("ppinc7")))
        if before in CONDITIONS and after in CONDITIONS and band:
            pairs.append((old[identifier], row, float(row["panel_weight"]), condition_path(before, after), band))

    result: dict[str, object] = {
        "format": "us-shed-panel-adaptation-income-path-v1",
        "source_unit": "SHED respondent recontact panel, 2024 to 2025",
        "weight": "2025 panel_weight",
        "paired_rows_with_condition_path_and_income": len(pairs),
        "variance_estimation": False,
        "causal_estimation": False,
        "income_bands": {},
    }
    for band in INCOME_BANDS:
        band_pairs = [pair[:3] for pair in pairs if pair[4] == band]
        band_result: dict[str, object] = {"paired_rows": len(band_pairs), "paths": {}}
        for path_name in ["worsened", "same broad condition", "improved"]:
            path_pairs = [pair[:3] for pair in pairs if pair[4] == band and pair[3] == path_name]
            path_result: dict[str, object] = {"paired_rows": len(path_pairs), "adaptations": {}}
            for metric_name, field in METRICS.items():
                path_result["adaptations"][metric_name] = {
                    "prior_adopter_persistence": share(path_pairs, field, "Yes"),
                    "prior_nonadopter_reentry": share(path_pairs, field, "No"),
                }
            band_result["paths"][path_name] = path_result
        result["income_bands"][band] = band_result

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
