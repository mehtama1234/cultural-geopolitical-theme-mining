#!/usr/bin/env python3
"""Estimate SIPP earnings/hours direction by one additional condition at a time."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from collections import defaultdict
from pathlib import Path

import numpy as np

PERSON = ("SSUID", "PNUM", "SPANEL", "SWAVE")
REPS = 240
FAY = 0.5
RESOURCE_BANDS = ("below_1x", "1_to_2x", "2_to_4x", "4x_or_more")
STATUSES = ("yes", "no")
METRICS = ("earnings", "hours")
DIRECTIONS = ("increase", "decrease", "same")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def number(value: str) -> float | None:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if result >= 0 else None


def resource(value: str) -> str | None:
    value = number(value)
    if value is None:
        return None
    return "below_1x" if value < 1 else "1_to_2x" if value < 2 else "2_to_4x" if value < 4 else "4x_or_more"


def condition_label(row: dict[str, str], condition: str) -> str | None:
    if condition == "children":
        value = number(row.get("RHNUMU18", ""))
        return None if value is None else ("children_0" if value == 0 else "children_1plus")
    if condition == "tenure":
        return {"1": "owned_or_bought", "2": "rented"}.get(row.get("ETENURE", ""))
    if condition == "snap":
        return {"1": "snap_yes", "2": "snap_no"}.get(row.get("RSNAP_MNYN", ""))
    if condition == "food":
        return {"1": "high_or_marginal", "2": "low", "3": "very_low"}.get(row.get("RFOODS", ""))
    raise ValueError(f"unknown condition: {condition}")


def direction(before: float, after: float) -> str:
    return "increase" if after > before else "decrease" if after < before else "same"


def estimate(cell: dict[str, float], numerator: np.ndarray, denominator: np.ndarray) -> dict[str, object]:
    point = 100 * cell["numerator"] / cell["denominator"] if cell["denominator"] else None
    if point is None:
        se = None
    else:
        ratios = np.divide(numerator, denominator, out=np.full(REPS, np.nan), where=denominator != 0)
        se = float(np.sqrt(np.nansum((ratios - point / 100) ** 2) / (REPS * FAY**2)) * 100)
    return {
        "valid_pair_n": int(cell["pairs"]),
        "share_percent": point,
        "standard_error_percentage_points": se,
        "approx_95_ci_percentage_points": ([max(0, point - 1.96 * se), min(100, point + 1.96 * se)] if point is not None and se is not None else None),
    }


def analyze(primary: Path, replicate: Path, condition: str) -> dict[str, object]:
    people: dict[tuple[str, ...], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    required = set(PERSON) | {"MONTHCODE", "WPFINWGT", "THINCPOV", "EDISABL", "TPEARN", "TMWKHRS", "RHNUMU18", "ETENURE", "RSNAP_MNYN", "RFOODS"}
    with primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
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
            group = condition_label(row, condition)
            status = {"1": "yes", "2": "no"}.get(row.get("EDISABL", ""))
            band = resource(row.get("THINCPOV", ""))
            if group and status and band:
                people[tuple(row[k] for k in PERSON)][month] = {
                    "group": group, "status": status, "resource": band,
                    "earnings": row.get("TPEARN", ""), "hours": row.get("TMWKHRS", ""),
                    "weight": row["WPFINWGT"],
                }

    cell_keys = [(g, s, b, m, d) for g in sorted({v["group"] for p in people.values() for v in p.values()})
                 for s in STATUSES for b in RESOURCE_BANDS for m in METRICS for d in DIRECTIONS]
    cells = {key: {"denominator": 0.0, "numerator": 0.0, "pairs": 0} for key in cell_keys}
    pair_rows: dict[tuple[str, ...], list[tuple[tuple[str, ...], str]] ] = {}
    for person, months in people.items():
        for month in range(1, 12):
            current, following = months.get(month), months.get(month + 1)
            if not current or not following:
                continue
            outcomes = []
            for metric in METRICS:
                before, after = number(current[metric]), number(following[metric])
                if before is None or after is None:
                    continue
                category = direction(before, after)
                base = (current["group"], current["status"], current["resource"], metric)
                for candidate in DIRECTIONS:
                    key = base + (candidate,)
                    cells[key]["denominator"] += float(current["weight"])
                    cells[key]["numerator"] += float(current["weight"]) * (candidate == category)
                    cells[key]["pairs"] += 1
                outcomes.append((base, category))
            if outcomes:
                pair_rows[person + (str(month),)] = outcomes

    rep_num = {key: np.zeros(REPS) for key in cells}
    rep_den = {key: np.zeros(REPS) for key in cells}
    replicate_rows = matched_rows = 0
    with zipfile.ZipFile(replicate) as archive, archive.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for row in reader:
            replicate_rows += 1
            key = tuple(row[k.lower()] for k in PERSON) + (row["monthcode"],)
            outcomes = pair_rows.get(key)
            if not outcomes:
                continue
            matched_rows += 1
            weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPS + 1)), dtype=float, count=REPS)
            for base, category in outcomes:
                for candidate in DIRECTIONS:
                    cell_key = base + (candidate,)
                    rep_den[cell_key] += weights
                    if candidate == category:
                        rep_num[cell_key] += weights

    result_cells = {}
    for group in sorted({key[0] for key in cells}):
        result_cells[group] = {}
        for status in STATUSES:
            result_cells[group][status] = {}
            for band in RESOURCE_BANDS:
                result_cells[group][status][band] = {}
                for metric in METRICS:
                    result_cells[group][status][band][metric] = {
                        d: estimate(cells[(group, status, band, metric, d)], rep_num[(group, status, band, metric, d)], rep_den[(group, status, band, metric, d)])
                        for d in DIRECTIONS
                    }
    return {
        "format": "us-sipp-resource-worklimitation-conditioned-v1",
        "condition": condition,
        "source_unit": "identified SIPP person, resource band at month t to direction of valid earnings/hours at month t+1, conditioned on EDISABL and one additional current-month dimension",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for Fay-BRR",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_persons": len(people),
        "replicate_rows_read": replicate_rows,
        "matched_pair_rows": matched_rows,
        "cells": result_cells,
        "household_weight_used": False,
        "boundary": "Descriptive same-person monthly transition. Earnings and hours retain separate valid-pair universes; the additional condition is not a causal contrast and does not establish job quality, care substitution, recovery, trust, political action, or institutional remedy."
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--condition", choices=("children", "tenure", "snap", "food"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.primary, args.replicate_zip, args.condition)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
