#!/usr/bin/env python3
"""Estimate direction of SIPP month-to-month earnings and hours movement."""

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
GROUPS = ("below_1x", "1_to_2x", "2_to_4x", "4x_or_more")
STATUSES = ("yes", "no")
METRICS = ("earnings", "hours")
DIRECTIONS = ("increase", "decrease", "same")


def band(x: str) -> str | None:
    try:
        value = float(x)
    except (TypeError, ValueError):
        return None
    return "below_1x" if value < 1 else "1_to_2x" if value < 2 else "2_to_4x" if value < 4 else "4x_or_more"


def numeric(x: str) -> float | None:
    try:
        value = float(x)
    except (TypeError, ValueError):
        return None
    return value if value >= 0 else None


def status(x: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(x)


def direction(before: float, after: float) -> str:
    if after > before:
        return "increase"
    if after < before:
        return "decrease"
    return "same"


def estimate(cell: dict[str, float], numerators: np.ndarray, denominators: np.ndarray) -> dict[str, object]:
    point = 100 * cell["numerator"] / cell["denominator"] if cell["denominator"] else None
    if point is None:
        se = None
    else:
        ratios = np.divide(numerators, denominators, out=np.full(REPS, np.nan), where=denominators != 0)
        se = float(np.sqrt(np.nansum((ratios - point / 100) ** 2) / (REPS * FAY**2)) * 100)
    return {
        "valid_pair_n": int(cell["pairs"]),
        "share_percent": point,
        "standard_error_percentage_points": se,
        "approx_95_ci_percentage_points": ([max(0, point - 1.96 * se), min(100, point + 1.96 * se)] if point is not None and se is not None else None),
    }


def analyze(primary: Path, replicate: Path) -> dict[str, object]:
    people: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "THINCPOV", "EDISABL", "TPEARN", "TMWKHRS"}
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
                people[tuple(row[k] for k in KEYS[:-1])][month] = {
                    "resource": row["THINCPOV"], "status": row["EDISABL"],
                    "earnings": row["TPEARN"], "hours": row["TMWKHRS"], "weight": row["WPFINWGT"]}

    cells = {
        metric: {group: {state: {d: {"denominator": 0.0, "numerator": 0.0, "pairs": 0} for d in DIRECTIONS} for state in STATUSES} for group in GROUPS}
        for metric in METRICS
    }
    pair_rows: dict[tuple[str, str, str, str, str], list[tuple[str, str, str, str, bool]]] = {}
    for person, months in people.items():
        for month in range(1, 12):
            current, following = months.get(month), months.get(month + 1)
            if not current or not following:
                continue
            group, state = band(current["resource"]), status(current["status"])
            if not group or not state:
                continue
            outcomes = []
            for metric in METRICS:
                before, after = numeric(current[metric]), numeric(following[metric])
                if before is None or after is None:
                    continue
                category = direction(before, after)
                for candidate in DIRECTIONS:
                    cell = cells[metric][group][state][candidate]
                    cell["denominator"] += float(current["weight"])
                    cell["numerator"] += float(current["weight"]) * (candidate == category)
                    cell["pairs"] += 1
                outcomes.append((metric, group, state, category, True))
            if outcomes:
                pair_rows[person + (str(month),)] = outcomes

    rep_num = {m: {g: {s: {d: np.zeros(REPS) for d in DIRECTIONS} for s in STATUSES} for g in GROUPS} for m in METRICS}
    rep_den = {m: {g: {s: {d: np.zeros(REPS) for d in DIRECTIONS} for s in STATUSES} for g in GROUPS} for m in METRICS}
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
            for metric, group, state, category, _ in outcomes:
                for candidate in DIRECTIONS:
                    rep_den[metric][group][state][candidate] += weights
                    if candidate == category:
                        rep_num[metric][group][state][candidate] += weights

    results = {}
    for metric in METRICS:
        results[metric] = {}
        for group in GROUPS:
            results[metric][group] = {}
            for state in STATUSES:
                results[metric][group][state] = {
                    category: estimate(cells[metric][group][state][category], rep_num[metric][group][state][category], rep_den[metric][group][state][category])
                    for category in DIRECTIONS
                }
    return {
        "format": "us-sipp-resource-worklimitation-direction-v1",
        "source_unit": "identified SIPP person, resource band at month t to direction of valid earnings/hours at month t+1, conditioned on EDISABL",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for Fay-BRR",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_persons": len(people),
        "replicate_rows_read": replicate_rows,
        "matched_pair_rows": matched_rows,
        "cells": results,
        "household_weight_used": False,
        "boundary": "Descriptive same-person monthly transition by direction of nonnegative numeric TPEARN and TMWKHRS, conditioned on EDISABL; does not establish causality, job quality, desired hours, household prevalence, accommodation, care, trust, or political action."
    }


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
