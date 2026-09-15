#!/usr/bin/env python3
"""Estimate SIPP resource-to-work-measure changes by work-limiting status."""

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


def band(x: str) -> str | None:
    try: v = float(x)
    except (TypeError, ValueError): return None
    return "below_1x" if v < 1 else "1_to_2x" if v < 2 else "2_to_4x" if v < 4 else "4x_or_more"


def num(x: str) -> float | None:
    try:
        v = float(x)
        return v if v >= 0 else None
    except (TypeError, ValueError): return None


def status(x: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(x)


def summary(cell: dict[str, float], rn: np.ndarray, rd: np.ndarray) -> dict[str, object]:
    point = 100 * cell["num"] / cell["den"] if cell["den"] else None
    se = None
    if point is not None:
        est = np.divide(rn, rd, out=np.full(REPS, np.nan), where=rd != 0)
        se = float(np.sqrt(np.nansum((est - point / 100) ** 2) / (REPS * FAY**2)) * 100)
    return {**cell, "share_percent": point,
            "standard_error_percentage_points": se,
            "approx_95_ci_percentage_points": ([max(0, point - 1.96 * se), min(100, point + 1.96 * se)]
                                                  if point is not None and se is not None else None)}


def analyze(primary: Path, replicate: Path) -> dict[str, object]:
    people: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows = 0
    with primary.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required = set(KEYS) | {"WPFINWGT", "THINCPOV", "EDISABL", "TPEARN", "TMWKHRS"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing: raise ValueError("primary slice missing: " + ", ".join(missing))
        for r in reader:
            rows += 1
            try: month, weight = int(r["MONTHCODE"]), float(r["WPFINWGT"])
            except (TypeError, ValueError): continue
            if 1 <= month <= 12 and weight > 0:
                people[tuple(r[k] for k in KEYS[:-1])][month] = {
                    "resource": r["THINCPOV"], "status": r["EDISABL"],
                    "earnings": r["TPEARN"], "hours": r["TMWKHRS"], "weight": r["WPFINWGT"]}

    groups = ("below_1x", "1_to_2x", "2_to_4x", "4x_or_more")
    metrics = ("earnings_change", "hours_change")
    cells = {m: {g: {s: {"den": 0.0, "num": 0.0, "pairs": 0} for s in ("yes", "no")} for g in groups} for m in metrics}
    pairs: dict[tuple[str, str, str, str, str], list[tuple[str, str, str, bool]]] = {}
    for person, months in people.items():
        for month in range(1, 12):
            a, b = months.get(month), months.get(month + 1)
            if not a or not b: continue
            g, s = band(a["resource"]), status(a["status"])
            if not g or not s: continue
            outcomes = []
            for metric, field in (("earnings_change", "earnings"), ("hours_change", "hours")):
                x, y = num(a[field]), num(b[field])
                if x is None or y is None: continue
                changed = x != y
                c = cells[metric][g][s]
                c["den"] += float(a["weight"]); c["num"] += float(a["weight"]) * changed; c["pairs"] += 1
                outcomes.append((metric, g, s, changed))
            if outcomes: pairs[person + (str(month),)] = outcomes

    rn = {m: {g: {s: np.zeros(REPS) for s in ("yes", "no")} for g in groups} for m in metrics}
    rd = {m: {g: {s: np.zeros(REPS) for s in ("yes", "no")} for g in groups} for m in metrics}
    rep_rows = matched = 0
    with zipfile.ZipFile(replicate) as z, z.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for r in reader:
            rep_rows += 1
            key = tuple(r[k.lower()] for k in KEYS); outcomes = pairs.get(key)
            if not outcomes: continue
            matched += 1
            weights = np.fromiter((float(r[f"repwgt{i}"]) for i in range(1, REPS + 1)), dtype=float, count=REPS)
            for m, g, s, changed in outcomes:
                rd[m][g][s] += weights
                if changed: rn[m][g][s] += weights
    result = {m: {g: {s: summary(c, rn[m][g][s], rd[m][g][s]) for s, c in ss.items()} for g, ss in gs.items()} for m, gs in cells.items()}
    return {"format": "us-sipp-resource-worklimitation-hours-earnings-v1", "source_unit": "identified SIPP person, resource band at month t to valid earnings/hours change at month t+1", "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for Fay-BRR", "variance_method": "Fay BRR, G=240, perturbation factor 0.5", "rows_read": rows, "identified_persons": len(people), "replicate_rows_read": rep_rows, "matched_pair_rows": matched, "cells": result, "household_weight_used": False, "boundary": "Descriptive same-person monthly transition for nonnegative numeric TPEARN and TMWKHRS values, conditioned on EDISABL; does not establish causality, job quality, desired hours, household prevalence, accommodation, care, trust, or political action."}


def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--primary", type=Path, required=True); p.add_argument("--replicate-zip", type=Path, required=True); p.add_argument("--output", type=Path, required=True)
    args = p.parse_args(); result = analyze(args.primary, args.replicate_zip); args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(result, indent=2) + "\n"); print(json.dumps(result, indent=2)); return 0


if __name__ == "__main__": raise SystemExit(main())
