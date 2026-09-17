#!/usr/bin/env python3
"""Estimate SIPP earnings/hours direction by resource band and subgroup."""

from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from collections import defaultdict
from pathlib import Path

import numpy as np

KEYS = ("SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE")
REPS = 240
FAY = 0.5
GROUPS = ("children_present", "no_children", "snap_receipt", "no_snap")
RESOURCE_BANDS = ("below_1x", "1_to_2x", "2_to_4x", "4x_or_more")
METRICS = ("earnings", "hours")
DIRECTIONS = ("increase", "decrease", "same")


def number(value: str) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if parsed >= 0 else None


def band(value: str) -> str | None:
    parsed = number(value)
    if parsed is None:
        return None
    if parsed < 1:
        return "below_1x"
    if parsed < 2:
        return "1_to_2x"
    if parsed < 4:
        return "2_to_4x"
    return "4x_or_more"


def direction(before: float, after: float) -> str:
    return "increase" if after > before else "decrease" if after < before else "same"


def estimate(cell: dict[str, float], rep_num: np.ndarray, rep_den: np.ndarray) -> dict[str, object]:
    if not cell["denominator"]:
        return {"valid_pair_n": 0, "share_percent": None, "standard_error_percentage_points": None, "approx_95_ci_percentage_points": None}
    point = 100 * cell["numerator"] / cell["denominator"]
    ratios = np.divide(rep_num, rep_den, out=np.full(REPS, np.nan), where=rep_den != 0)
    se = float(np.sqrt(np.nansum((ratios - point / 100) ** 2) / (REPS * FAY**2)) * 100)
    return {"valid_pair_n": int(cell["pairs"]), "share_percent": point, "standard_error_percentage_points": se, "approx_95_ci_percentage_points": [max(0, point - 1.96 * se), min(100, point + 1.96 * se)]}


def analyze(primary: Path, replicate: Path) -> dict[str, object]:
    people: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "THINCPOV", "TPEARN", "TMWKHRS", "RHNUMU18", "RSNAP_MNYN"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice missing: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                month, weight = int(row["MONTHCODE"]), float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if 1 <= month <= 12 and weight > 0:
                people[tuple(row[k] for k in KEYS[:-1])][month] = row

    group_names = tuple(f"{group}__{resource}" for group in GROUPS for resource in RESOURCE_BANDS)
    cells = {metric: {group: {d: {"denominator": 0.0, "numerator": 0.0, "pairs": 0} for d in DIRECTIONS} for group in group_names} for metric in METRICS}
    pair_rows: dict[tuple[str, str, str, str, str], list[tuple[str, str, str]]] = {}
    for person, months in people.items():
        for month in range(1, 12):
            before, after = months.get(month), months.get(month + 1)
            if before is None or after is None:
                continue
            resource = band(before["THINCPOV"])
            if resource is None:
                continue
            child_value = number(before["RHNUMU18"])
            child_group = "children_present" if child_value is not None and child_value > 0 else "no_children" if child_value == 0 else None
            snap_group = "snap_receipt" if before["RSNAP_MNYN"] == "1" else "no_snap" if before["RSNAP_MNYN"] == "2" else None
            groups = tuple(g for g in (child_group, snap_group) if g)
            if not groups:
                continue
            outcomes = []
            for metric in METRICS:
                before_value, after_value = number(before["TPEARN"] if metric == "earnings" else before["TMWKHRS"]), number(after["TPEARN"] if metric == "earnings" else after["TMWKHRS"])
                if before_value is None or after_value is None:
                    continue
                category = direction(before_value, after_value)
                selected = []
                for subgroup in groups:
                    group = f"{subgroup}__{resource}"
                    selected.append(group)
                    for candidate in DIRECTIONS:
                        cell = cells[metric][group][candidate]
                        cell["denominator"] += float(before["WPFINWGT"])
                        cell["numerator"] += float(before["WPFINWGT"]) * (candidate == category)
                        cell["pairs"] += 1
                outcomes.append((metric, selected, category))
            if outcomes:
                pair_rows[person + (str(month),)] = [(metric, "|".join(groups), category) for metric, groups, category in outcomes]

    rep_num = {metric: {group: {d: np.zeros(REPS) for d in DIRECTIONS} for group in group_names} for metric in METRICS}
    rep_den = {metric: {group: {d: np.zeros(REPS) for d in DIRECTIONS} for group in group_names} for metric in METRICS}
    replicate_rows = matched_rows = 0
    with zipfile.ZipFile(replicate) as archive, archive.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for row in reader:
            replicate_rows += 1
            key = tuple(row[k.lower()] for k in KEYS)
            outcomes = pair_rows.get(key)
            if not outcomes:
                continue
            matched_rows += 1
            weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPS + 1)), dtype=float, count=REPS)
            for metric, subgroup_text, category in outcomes:
                for selected_group in subgroup_text.split("|"):
                    for candidate in DIRECTIONS:
                        rep_den[metric][selected_group][candidate] += weights
                        if candidate == category:
                            rep_num[metric][selected_group][candidate] += weights

    results = {metric: {group: {d: estimate(cells[metric][group][d], rep_num[metric][group][d], rep_den[metric][group][d]) for d in DIRECTIONS} for group in group_names} for metric in METRICS}
    return {"format": "us-sipp-resource-work-direction-subgroups-v1", "source_unit": "identified SIPP person, month t to t+1 valid earnings/hours direction, grouped by resource band and children/SNAP status at month t", "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for Fay-BRR", "variance_method": "Fay BRR, G=240, perturbation factor 0.5", "rows_read": rows_read, "identified_persons": len(people), "replicate_rows_read": replicate_rows, "matched_pair_rows": matched_rows, "results": results, "household_weight_used": False, "boundary": "Descriptive same-person monthly transition. Children and SNAP groups are separate conditioning screens; earnings and hours have separate valid universes. This does not establish causality, desired hours, household prevalence, job quality, care mechanism, remedy, trust, political action, or exit."}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.primary, args.replicate_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
