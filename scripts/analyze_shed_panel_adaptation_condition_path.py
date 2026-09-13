#!/usr/bin/env python3
"""Descriptive SHED panel adaptation rates by financial-condition path."""

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


def path(before: str, after: str) -> str:
    before_i, after_i = CONDITIONS.index(before), CONDITIONS.index(after)
    if after_i < before_i:
        return "worsened"
    if after_i > before_i:
        return "improved"
    return "same broad condition"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", type=Path, required=True)
    parser.add_argument("--new", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    old = {clean(row.get("shedid")): row for row in read_zip(args.old)}
    pairs = []
    for row in read_zip(args.new):
        identifier = clean(row.get("shedid"))
        weight = clean(row.get("panel_weight"))
        if not weight or identifier not in old:
            continue
        before, after = clean(old[identifier].get("B2")), clean(row.get("B2"))
        if before in CONDITIONS and after in CONDITIONS:
            pairs.append((old[identifier], row, float(weight), path(before, after)))

    result: dict[str, object] = {
        "format": "us-shed-panel-adaptation-condition-path-v1",
        "source_unit": "SHED respondent recontact panel, 2024 to 2025",
        "weight": "2025 panel_weight",
        "paired_rows_with_condition_path": len(pairs),
        "variance_estimation": False,
        "causal_estimation": False,
        "paths": {},
    }
    for path_name in ["worsened", "same broad condition", "improved"]:
        path_pairs = [pair for pair in pairs if pair[3] == path_name]
        path_weight = sum(pair[2] for pair in path_pairs)
        path_result: dict[str, object] = {
            "paired_rows": len(path_pairs),
            "weighted_denominator": path_weight,
            "adaptations": {},
        }
        for metric_name, field in METRICS.items():
            cells: dict[str, dict[str, float | int | None]] = {}
            for state in ["No", "Yes"]:
                selected = [pair for pair in path_pairs if clean(pair[0].get(field)) == state and clean(pair[1].get(field)) in {"No", "Yes"}]
                denominator = sum(pair[2] for pair in selected)
                yes_weight = sum(pair[2] for pair in selected if clean(pair[1].get(field)) == "Yes")
                cells[state] = {
                    "valid_pairs": len(selected),
                    "weighted_share_yes_2025_percent": 100 * yes_weight / denominator if denominator else None,
                }
            path_result["adaptations"][metric_name] = cells
        result["paths"][path_name] = path_result

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
