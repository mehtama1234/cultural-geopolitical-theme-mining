#!/usr/bin/env python3
"""Estimate next-month SIPP work changes by utility difficulty and tenure."""

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


def number(value: str) -> float | None:
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    return value if value >= 0 else None


def estimate(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray) -> dict[str, object]:
    if not den:
        return {"share_percent": None, "standard_error_percentage_points": None, "approx_95_ci_percentage_points": None}
    point = 100 * num / den
    ratios = np.divide(rep_num, rep_den, out=np.full(REPS, np.nan), where=rep_den != 0)
    if np.isnan(ratios).any():
        return {"share_percent": point, "standard_error_percentage_points": None, "approx_95_ci_percentage_points": None}
    se = float(np.sqrt(np.sum((ratios - point / 100) ** 2) / (REPS * FAY**2)) * 100)
    return {
        "share_percent": point,
        "standard_error_percentage_points": se,
        "approx_95_ci_percentage_points": [max(0, point - 1.96 * se), min(100, point + 1.96 * se)],
    }


def analyze(primary: Path, replicate_zip: Path) -> dict[str, object]:
    people: dict[tuple[str, str, str, str], dict[int, dict[str, object]]] = defaultdict(dict)
    rows_read = 0
    with primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "THHLDSTATUS", "AAWBGAS", "EAWBGAS", "ETENURE", "TPEARN", "TMWKHRS"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice missing: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                month, weight = int(row["MONTHCODE"]), float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if not 1 <= month <= 12 or weight <= 0:
                continue
            if row.get("THHLDSTATUS") not in {"1", "2", "3", "4"} or row.get("AAWBGAS") not in {"1", "2"}:
                continue
            utility = {"1": "utility_difficulty", "2": "no_utility_difficulty"}.get(row.get("EAWBGAS", ""))
            tenure = {"1": "owned_or_bought", "2": "rented"}.get(row.get("ETENURE", ""))
            if not utility or not tenure:
                continue
            group = utility + "__" + tenure
            people[tuple(row[k] for k in KEYS[:-1])][month] = {
                "weight": weight,
                "earnings": row["TPEARN"],
                "hours": row["TMWKHRS"],
                "group": group,
            }

    groups = tuple(
        f"{utility}__{tenure}"
        for utility in ("utility_difficulty", "no_utility_difficulty")
        for tenure in ("owned_or_bought", "rented")
    )
    cells = {
        group: {"eligible_pairs": 0, "earnings_valid_n": 0, "hours_valid_n": 0, "earnings_valid_weight": 0.0, "hours_valid_weight": 0.0, "earnings_changed_weight": 0.0, "hours_changed_weight": 0.0}
        for group in groups
    }
    pairs: dict[tuple[str, str, str, str, str], list[tuple[str, str, bool]]] = {}
    for person, months in people.items():
        for month in range(1, 12):
            current, following = months.get(month), months.get(month + 1)
            if not current or not following:
                continue
            group = str(current["group"])
            cells[group]["eligible_pairs"] += 1
            outcomes = []
            for metric, field in (("earnings", "earnings"), ("hours", "hours")):
                before, after = number(str(current[field])), number(str(following[field]))
                if before is None or after is None:
                    continue
                changed = before != after
                cells[group][f"{metric}_valid_n"] += 1
                cells[group][f"{metric}_valid_weight"] += float(current["weight"])
                cells[group][f"{metric}_changed_weight"] += float(current["weight"]) * changed
                outcomes.append((group, metric, changed))
            if outcomes:
                pairs[person + (str(month),)] = outcomes

    rep_num = {group: {metric: np.zeros(REPS) for metric in ("earnings", "hours")} for group in groups}
    rep_den = {group: {metric: np.zeros(REPS) for metric in ("earnings", "hours")} for group in groups}
    replicate_rows = matched_rows = 0
    with zipfile.ZipFile(replicate_zip) as archive, archive.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for row in reader:
            replicate_rows += 1
            key = tuple(row[k.lower()] for k in KEYS)
            outcomes = pairs.get(key)
            if not outcomes:
                continue
            matched_rows += 1
            weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPS + 1)), dtype=float, count=REPS)
            for group, metric, changed in outcomes:
                rep_den[group][metric] += weights
                if changed:
                    rep_num[group][metric] += weights

    result_cells = {}
    for group, cell in cells.items():
        result_cells[group] = {
            "eligible_pairs": cell["eligible_pairs"],
            "earnings_change": {"valid_pair_n": cell["earnings_valid_n"], **estimate(cell["earnings_changed_weight"], cell["earnings_valid_weight"], rep_num[group]["earnings"], rep_den[group]["earnings"])},
            "hours_change": {"valid_pair_n": cell["hours_valid_n"], **estimate(cell["hours_changed_weight"], cell["hours_valid_weight"], rep_num[group]["hours"], rep_den[group]["hours"])},
        }
    return {
        "format": "us-sipp-utility-work-tenure-v1",
        "source_unit": "identified SIPP person, utility-payment screen and tenure at month t to valid earnings/hours change at month t+1",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for Fay-BRR",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_persons": len(people),
        "replicate_rows_read": replicate_rows,
        "matched_pair_rows": matched_rows,
        "cells": result_cells,
        "boundary": "Descriptive same-person monthly transition conditioned on reported utility-payment difficulty and tenure. It does not establish a dated bill shock, tenure effect, utility causation, desired hours, job quality, care substitution, recovery, trust, political action, or household prevalence.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
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
