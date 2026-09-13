#!/usr/bin/env python3
"""Weighted SHED 2024-2025 panel health and care transitions by money path."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from pathlib import Path

CONDITIONS = [
    "Finding it difficult to get by",
    "Just getting by",
    "Doing okay",
    "Living comfortably",
]
HEALTH = ["Poor", "Fair", "Good", "Very good", "Excellent"]


def read_zip(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"expected one CSV in {path}, found {names}")
        with archive.open(names[0]) as handle:
            return list(csv.DictReader((line.decode("utf-8-sig") for line in handle)))


def clean(value: str | None) -> str:
    return (value or "").strip()


def direction(before: str, after: str, scale: list[str]) -> str:
    before_i, after_i = scale.index(before), scale.index(after)
    if after_i < before_i:
        return "worsened"
    if after_i > before_i:
        return "improved"
    return "same"


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
        if identifier not in old or not clean(row.get("panel_weight")):
            continue
        before, after = clean(old[identifier].get("B2")), clean(row.get("B2"))
        health_before, health_after = clean(old[identifier].get("pph10001")), clean(row.get("pph10001"))
        if before not in CONDITIONS or after not in CONDITIONS:
            continue
        pairs.append((old[identifier], row, float(row["panel_weight"]),
                      direction(before, after, CONDITIONS),
                      direction(health_before, health_after, HEALTH)
                      if health_before in HEALTH and health_after in HEALTH else None))

    result: dict[str, object] = {
        "format": "us-shed-panel-health-care-paths-v1",
        "source_unit": "SHED respondent recontact panel, 2024 to 2025",
        "weight": "2025 panel_weight",
        "paired_rows_with_condition_path": len(pairs),
        "variance_estimation": False,
        "causal_estimation": False,
        "financial_paths": {},
    }

    for path_name in ["worsened", "same", "improved"]:
        path_pairs = [item for item in pairs if item[3] == path_name]
        entry: dict[str, object] = {"paired_rows": len(path_pairs), "outcomes": {}}
        valid_health = [item for item in path_pairs if item[4] is not None]
        entry["outcomes"]["health_direction"] = {
            label: {
                "pairs": sum(1 for item in valid_health if item[4] == label),
                "weighted_share_percent": round(100 * sum(item[2] for item in valid_health if item[4] == label) / sum(item[2] for item in valid_health), 3)
                if valid_health else None,
            }
            for label in ["worsened", "same", "improved"]
        }
        for label, field in [("adult_care_entry", "CG4"), ("adult_care_exit", "CG4")]:
            valid = [item for item in path_pairs if clean(item[0].get(field)) in {"Yes", "No"} and clean(item[1].get(field)) in {"Yes", "No"}]
            if label == "adult_care_entry":
                selected = [item for item in valid if clean(item[0].get(field)) == "No"]
                numerator = [item for item in selected if clean(item[1].get(field)) == "Yes"]
            else:
                selected = [item for item in valid if clean(item[0].get(field)) == "Yes"]
                numerator = [item for item in selected if clean(item[1].get(field)) == "No"]
            denominator = sum(item[2] for item in selected)
            entry["outcomes"][label] = {
                "pairs": len(selected),
                "weighted_share_percent": round(100 * sum(item[2] for item in numerator) / denominator, 3) if denominator else None,
                "weighted_denominator": round(denominator, 1),
            }
        result["financial_paths"][path_name] = entry

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
