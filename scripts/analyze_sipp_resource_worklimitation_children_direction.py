#!/usr/bin/env python3
"""SIPP monthly earnings/hours direction by resources, work limitation, and children."""
from __future__ import annotations

import argparse, csv, io, json, zipfile
from collections import defaultdict
from pathlib import Path
import numpy as np

KEYS = ("SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE")
REPS, FAY = 240, 0.5
GROUPS = ("below_1x", "4x_or_more")
STATUSES = ("yes", "no")
DIRECTIONS = ("increase", "decrease", "same")
METRICS = ("earnings", "hours")

def band(value):
    try: value = float(value)
    except (TypeError, ValueError): return None
    return "below_1x" if value < 1 else "4x_or_more" if value >= 4 else None

def binary(value): return {"1": "yes", "2": "no"}.get(value)

def nonnegative(value):
    try:
        value = float(value)
        return value if value >= 0 else None
    except (TypeError, ValueError): return None

def direction(before, after):
    return "increase" if after > before else "decrease" if after < before else "same"

def estimate(cell, nums, dens):
    if not cell["pairs"]: return {"valid_pair_n": 0, "share_percent": None, "standard_error_percentage_points": None, "approx_95_ci_percentage_points": None}
    point = 100 * cell["numerator"] / cell["denominator"]
    ratios = np.divide(nums, dens, out=np.full(REPS, np.nan), where=dens != 0)
    se = float(np.sqrt(np.nansum((ratios - point / 100) ** 2) / (REPS * FAY**2)) * 100)
    return {"valid_pair_n": cell["pairs"], "share_percent": point, "standard_error_percentage_points": se, "approx_95_ci_percentage_points": [max(0, point - 1.96 * se), min(100, point + 1.96 * se)]}

def analyze(primary: Path, replicate: Path):
    people = defaultdict(dict); rows_read = 0
    with primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "THINCPOV", "EDISABL", "RHNUMU18", "TPEARN", "TMWKHRS"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing: raise ValueError("primary slice missing: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try: month, weight = int(row["MONTHCODE"]), float(row["WPFINWGT"])
            except (TypeError, ValueError): continue
            if 1 <= month <= 12 and weight > 0:
                people[tuple(row[k] for k in KEYS[:-1])][month] = {"resource": row["THINCPOV"], "disabled": row["EDISABL"], "children": row["RHNUMU18"], "earnings": row["TPEARN"], "hours": row["TMWKHRS"], "weight": weight}

    shape = lambda: {d: {"numerator": 0.0, "denominator": 0.0, "pairs": 0} for d in DIRECTIONS}
    cells = {m: {g: {s: {c: shape() for c in STATUSES} for s in STATUSES} for g in GROUPS} for m in METRICS}
    pair_rows = {}
    for person, months in people.items():
        for month in range(1, 12):
            cur, nxt = months.get(month), months.get(month + 1)
            if not cur or not nxt: continue
            group, disabled, children = band(cur["resource"]), binary(cur["disabled"]), binary(cur["children"])
            if not group or not disabled or not children: continue
            outcomes = []
            for metric in METRICS:
                before, after = nonnegative(cur[metric]), nonnegative(nxt[metric])
                if before is None or after is None: continue
                category = direction(before, after)
                cell = cells[metric][group][disabled][children]
                for candidate in DIRECTIONS:
                    cell[candidate]["denominator"] += cur["weight"]
                    cell[candidate]["numerator"] += cur["weight"] * (candidate == category)
                    cell[candidate]["pairs"] += 1
                outcomes.append((metric, group, disabled, children, category))
            if outcomes: pair_rows[person + (str(month),)] = outcomes

    nums = {m: {g: {s: {c: {d: np.zeros(REPS) for d in DIRECTIONS} for c in STATUSES} for s in STATUSES} for g in GROUPS} for m in METRICS}
    dens = {m: {g: {s: {c: {d: np.zeros(REPS) for d in DIRECTIONS} for c in STATUSES} for s in STATUSES} for g in GROUPS} for m in METRICS}
    replicate_rows = matched_rows = 0
    with zipfile.ZipFile(replicate) as archive, archive.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for row in reader:
            replicate_rows += 1; key = tuple(row[k.lower()] for k in KEYS); outcomes = pair_rows.get(key)
            if not outcomes: continue
            matched_rows += 1; weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPS + 1)), dtype=float, count=REPS)
            for metric, group, disabled, children, category in outcomes:
                for candidate in DIRECTIONS:
                    dens[metric][group][disabled][children][candidate] += weights
                    if category == candidate: nums[metric][group][disabled][children][candidate] += weights
    result = {"format": "us-sipp-resource-worklimitation-children-direction-v1", "source_unit": "identified SIPP person, resource band at month t to direction of valid earnings/hours at month t+1, conditioned on work limitation and household member under 18", "weight": "WPFINWGT; REPWGT1-REPWGT240", "variance_method": "Fay BRR, G=240, perturbation factor 0.5", "rows_read": rows_read, "identified_persons": len(people), "replicate_rows_read": replicate_rows, "matched_pair_rows": matched_rows, "cells": {m: {g: {s: {c: {d: estimate(cells[m][g][s][c][d], nums[m][g][s][c][d], dens[m][g][s][c][d]) for d in DIRECTIONS} for c in STATUSES} for s in STATUSES} for g in GROUPS} for m in METRICS}, "household_weight_used": False, "boundary": "Descriptive same-person monthly direction screen; RHNUMU18 is household composition, not care responsibility. No causal, household-prevalence, accommodation, recovery, trust, political-action, or exit claim."
    }
    return result

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--primary", type=Path, required=True); parser.add_argument("--replicate-zip", type=Path, required=True); parser.add_argument("--output", type=Path, required=True); args = parser.parse_args()
    result = analyze(args.primary, args.replicate_zip); args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8"); print(json.dumps(result, indent=2))

if __name__ == "__main__": main()
