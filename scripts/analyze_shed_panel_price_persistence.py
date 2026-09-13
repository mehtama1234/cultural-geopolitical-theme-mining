#!/usr/bin/env python3
"""Weighted descriptive transitions in the 2024-2025 SHED recontact panel."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

METRICS = {
    "switched_cheaper_products": ("INF3_a", "Yes"),
    "used_less_or_stopped": ("INF3_b", "Yes"),
    "reduced_savings": ("INF3_c", "Yes"),
    "increased_borrowing": ("INF3_d", "Yes"),
    "delayed_major_purchase": ("INF3_e", "Yes"),
    "worked_more_or_got_job": ("INF3_f", "Yes"),
    "three_month_emergency_funds": ("EF1", "Yes"),
}
ORDERS = {
    "B2": ["Finding it difficult to get by", "Just getting by", "Doing okay", "Living comfortably"],
    "B3": ["Much worse off", "Somewhat worse off", "About the same", "Somewhat better off", "Much better off"],
    "INF4": ["Much worse", "Somewhat worse", "Little or no effect", "Somewhat better", "Much better"],
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


def weighted_transition(rows: list[tuple[str, str, float]], labels: list[str] | None = None) -> dict:
    counts: Counter[tuple[str, str]] = Counter()
    weights: defaultdict[tuple[str, str], float] = defaultdict(float)
    for before, after, weight in rows:
        counts[(before, after)] += 1
        weights[(before, after)] += weight
    denominator = sum(weights.values())
    result = {}
    before_labels = labels or sorted({before for before, _ in counts})
    after_labels = labels or sorted({after for _, after in counts})
    for before in before_labels:
        result[before] = {}
        for after in after_labels:
            value = weights[(before, after)]
            result[before][after] = {
                "pairs": counts[(before, after)],
                "weighted_share_percent": 100 * value / denominator if denominator else None,
                "weighted_row_share_percent": (100 * value /
                                                sum(weights[(before, x)] for x in after_labels)
                                                if sum(weights[(before, x)] for x in after_labels) else None),
            }
    return {"paired_rows": len(rows), "weighted_denominator": denominator, "cells": result}


def binary_transition(rows: list[tuple[str, str, float]]) -> dict:
    result = weighted_transition(rows, ["No", "Yes"])
    cells = result["cells"]
    for state in ["No", "Yes"]:
        result[f"{state.lower()}_2024_to_yes_2025_percent"] = cells[state]["Yes"]["weighted_row_share_percent"]
    return result


def load_panel(old_path: Path, new_path: Path) -> tuple[list[dict[str, str]], int, int]:
    old = {clean(row.get("shedid")): row for row in read_zip(old_path)}
    new_rows = read_zip(new_path)
    pairs = []
    missing = 0
    for row in new_rows:
        identifier = clean(row.get("shedid"))
        panel_weight = clean(row.get("panel_weight"))
        if not panel_weight:
            continue
        if identifier not in old:
            missing += 1
            continue
        pairs.append({"old": old[identifier], "new": row, "panel_weight": float(panel_weight)})
    return pairs, len(old), len(new_rows)


def analyze(old_path: Path, new_path: Path) -> dict:
    pairs, old_rows, new_rows = load_panel(old_path, new_path)
    required = {"B2", "B3", "INF4", "EF1"} | {field for field, _ in METRICS.values()}
    results = {}
    for name, field in [("financial_condition", "B2"),
                        ("year_over_year_financial_change", "B3"),
                        ("price_financial_effect", "INF4")]:
        rows = [(clean(pair["old"].get(field)), clean(pair["new"].get(field)), pair["panel_weight"])
                for pair in pairs
                if clean(pair["old"].get(field)) and clean(pair["new"].get(field))]
        results[name] = weighted_transition(rows, ORDERS[field])
    for name, (field, _) in METRICS.items():
        rows = [("Yes" if clean(pair["old"].get(field)) == "Yes" else "No",
                 "Yes" if clean(pair["new"].get(field)) == "Yes" else "No",
                 pair["panel_weight"])
                for pair in pairs
                if clean(pair["old"].get(field)) in {"Yes", "No"} and
                   clean(pair["new"].get(field)) in {"Yes", "No"}]
        results[name] = binary_transition(rows)
    return {
        "format": "us-shed-panel-price-persistence-v1",
        "source_unit": "SHED respondent recontact panel, 2024 to 2025",
        "weight": "2025 panel_weight (main recontact weight)",
        "old_rows": old_rows,
        "new_rows": new_rows,
        "panel_pairs_with_weight_and_shared_id": len(pairs),
        "results": results,
        "variance_estimation": False,
        "causal_estimation": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", type=Path, required=True)
    parser.add_argument("--new", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.old, args.new)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
