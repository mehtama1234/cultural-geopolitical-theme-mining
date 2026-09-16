#!/usr/bin/env python3
"""Estimate next-month credit and savings states after a SIPP utility screen."""

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


def utility_group(value: str) -> str | None:
    return {"1": "utility_difficulty", "2": "no_utility_difficulty"}.get(value)


def valid_binary(value: str) -> bool:
    return value in {"1", "2"}


def empty_cell() -> dict[str, float]:
    return {
        "eligible_pairs": 0,
        "credit_valid_pairs": 0,
        "credit_yes_weight": 0.0,
        "credit_valid_weight": 0.0,
        "credit_changed_pairs": 0,
        "credit_changed_weight": 0.0,
        "savings_valid_pairs": 0,
        "savings_yes_weight": 0.0,
        "savings_valid_weight": 0.0,
        "savings_changed_pairs": 0,
        "savings_changed_weight": 0.0,
    }


def estimate(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray) -> dict[str, object]:
    point = 100 * num / den if den else None
    if point is None:
        return {"share_percent": None, "standard_error_percentage_points": None, "approx_95_ci_percentage_points": None}
    estimates = np.divide(rep_num, rep_den, out=np.full(REPS, np.nan), where=rep_den != 0)
    if np.isnan(estimates).any():
        return {"share_percent": point, "standard_error_percentage_points": None, "approx_95_ci_percentage_points": None}
    se = float(np.sqrt(np.sum((estimates - point / 100) ** 2) / (REPS * FAY**2)) * 100)
    return {
        "share_percent": point,
        "standard_error_percentage_points": se,
        "approx_95_ci_percentage_points": [max(0, point - 1.96 * se), min(100, point + 1.96 * se)],
    }


def analyze(primary: Path, replicate: Path) -> dict[str, object]:
    people: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "THHLDSTATUS", "AAWBGAS", "EAWBGAS", "EDEBT_CC", "EOWN_SAV"}
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
            group = utility_group(row.get("EAWBGAS", ""))
            if group:
                people[tuple(row[k] for k in KEYS[:-1])][month] = {
                    "weight": row["WPFINWGT"],
                    "group": group,
                    "credit": row.get("EDEBT_CC", ""),
                    "savings": row.get("EOWN_SAV", ""),
                }

    groups = ("utility_difficulty", "no_utility_difficulty")
    cells = {group: empty_cell() for group in groups}
    pair_outcomes: dict[tuple[str, str, str, str, str], list[tuple[str, str, bool]]] = {}
    for person, months in people.items():
        for month in range(1, 12):
            current, following = months.get(month), months.get(month + 1)
            if not current or not following:
                continue
            group = current["group"]
            cell = cells[group]
            cell["eligible_pairs"] += 1
            outcomes = []
            for metric in ("credit", "savings"):
                before, after = current[metric], following[metric]
                if not valid_binary(after):
                    continue
                cell[f"{metric}_valid_pairs"] += 1
                cell[f"{metric}_valid_weight"] += float(current["weight"])
                cell[f"{metric}_yes_weight"] += float(current["weight"]) * (after == "1")
                changed = valid_binary(before) and before != after
                if changed:
                    cell[f"{metric}_changed_pairs"] += 1
                    cell[f"{metric}_changed_weight"] += float(current["weight"])
                outcomes.append((metric, "next_yes", after == "1"))
                if valid_binary(before):
                    outcomes.append((metric, "changed", changed))
            if outcomes:
                pair_outcomes[person + (str(month),)] = outcomes

    rep_num: dict[str, dict[str, np.ndarray]] = {
        group: {f"{metric}_{outcome}": np.zeros(REPS) for metric in ("credit", "savings") for outcome in ("next_yes", "changed")}
        for group in groups
    }
    rep_den: dict[str, dict[str, np.ndarray]] = {
        group: {f"{metric}_{outcome}": np.zeros(REPS) for metric in ("credit", "savings") for outcome in ("next_yes", "changed")}
        for group in groups
    }
    replicate_rows = matched_rows = 0
    with zipfile.ZipFile(replicate) as archive, archive.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for row in reader:
            replicate_rows += 1
            key = tuple(row[k.lower()] for k in KEYS)
            outcomes = pair_outcomes.get(key)
            if not outcomes:
                continue
            matched_rows += 1
            weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPS + 1)), dtype=float, count=REPS)
            group = people[tuple(row[k.lower()] for k in KEYS[:-1])][int(row["monthcode"])]["group"]
            for metric, outcome, yes in outcomes:
                name = f"{metric}_{outcome}"
                rep_den[group][name] += weights
                if yes:
                    rep_num[group][name] += weights

    result_cells = {}
    for group, cell in cells.items():
        result_cells[group] = {
            "eligible_pairs": int(cell["eligible_pairs"]),
            "credit_next_month_yes": estimate(cell["credit_yes_weight"], cell["credit_valid_weight"], rep_num[group]["credit_next_yes"], rep_den[group]["credit_next_yes"]),
            "credit_next_month_changed": estimate(cell["credit_changed_weight"], cell["credit_valid_weight"], rep_num[group]["credit_changed"], rep_den[group]["credit_changed"]),
            "savings_next_month_yes": estimate(cell["savings_yes_weight"], cell["savings_valid_weight"], rep_num[group]["savings_next_yes"], rep_den[group]["savings_next_yes"]),
            "savings_next_month_changed": estimate(cell["savings_changed_weight"], cell["savings_valid_weight"], rep_num[group]["savings_changed"], rep_den[group]["savings_changed"]),
            "credit_valid_pairs": int(cell["credit_valid_pairs"]),
            "savings_valid_pairs": int(cell["savings_valid_pairs"]),
            "credit_changed_pairs": int(cell["credit_changed_pairs"]),
            "savings_changed_pairs": int(cell["savings_changed_pairs"]),
        }
    return {
        "format": "us-sipp-utility-buffer-following-v1",
        "source_unit": "identified SIPP person, utility screen at month t to credit/savings state at month t+1",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for Fay-BRR",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_persons": len(people),
        "replicate_rows_read": replicate_rows,
        "matched_pair_rows": matched_rows,
        "cells": result_cells,
        "boundary": "Descriptive same-person monthly transition conditioned on reported utility-payment difficulty. Credit and savings outcomes retain their own valid universes. The result does not establish a dated bill shock, causality, household prevalence, liquidity, balance amount, payment success, service continuity, recovery, trust, or political action.",
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
