#!/usr/bin/env python3
"""Estimate SIPP resource/job adjacent-month cross-lags by work limitation."""

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
REPLICATES = 240
FAY_FACTOR = 0.5


def band(value: str) -> str | None:
    try:
        x = float(value)
    except (TypeError, ValueError):
        return None
    if x < 1:
        return "below_1x"
    if x < 2:
        return "1_to_2x"
    if x < 4:
        return "2_to_4x"
    return "4x_or_more"


def jobs(value: str) -> str | None:
    try:
        return str(int(float(value)))
    except (TypeError, ValueError):
        return None


def limitation(value: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(value)


def empty() -> dict[str, float]:
    return {"den": 0.0, "num": 0.0, "pairs": 0}


def summarize(cell: dict[str, float], rep_num: np.ndarray,
              rep_den: np.ndarray) -> dict[str, object]:
    point = 100 * cell["num"] / cell["den"] if cell["den"] else None
    if point is None:
        se = None
    else:
        estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
        se = float(np.sqrt(np.nansum((estimates - point / 100) ** 2) /
                           (REPLICATES * FAY_FACTOR**2)) * 100)
    return {
        **cell,
        "share_percent": point,
        "standard_error_percentage_points": se,
        "approx_95_ci_percentage_points": (
            [max(0.0, point - 1.96 * se), min(100.0, point + 1.96 * se)]
            if point is not None and se is not None else None
        ),
    }


def analyze(primary_path: Path, replicate_path: Path) -> dict[str, object]:
    people: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary_path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "THINCPOV", "RMNUMJOBS", "EDISABL"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                month = int(row["MONTHCODE"])
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if 1 <= month <= 12 and weight > 0:
                person = tuple(row[key] for key in KEYS[:-1])
                people[person][month] = {
                    "resource": row.get("THINCPOV", ""),
                    "jobs": row.get("RMNUMJOBS", ""),
                    "limitation": row.get("EDISABL", ""),
                    "weight": row["WPFINWGT"],
                }

    states = ("resource_to_job_change", "job_to_resource_change")
    cells: dict[str, dict[str, dict[str, dict[str, float]]]] = {
        state: {group: {status: empty() for status in ("yes", "no")}
                for group in ("below_1x", "1_to_2x", "2_to_4x", "4x_or_more", "zero_jobs", "one_job", "two_jobs", "three_or_more_jobs")}
        for state in states
    }
    pair_info: dict[tuple[str, str, str, str, str], list[tuple[str, str, str, bool]]] = {}

    for person, records in people.items():
        for month in range(1, 12):
            first, second = records.get(month), records.get(month + 1)
            if not first or not second:
                continue
            status = limitation(first["limitation"])
            r1, r2 = band(first["resource"]), band(second["resource"])
            j1, j2 = jobs(first["jobs"]), jobs(second["jobs"])
            if not status:
                continue
            weight = float(first["weight"])
            key = person + (str(month),)
            outcomes: list[tuple[str, str, str, bool]] = []
            if r1 and j2:
                group = r1
                changed = j1 is not None and j1 != j2
                cell = cells["resource_to_job_change"][group][status]
                cell["den"] += weight; cell["pairs"] += 1; cell["num"] += weight * changed
                outcomes.append(("resource_to_job_change", group, status, changed))
            if j1 and r2:
                n = int(j1)
                group = "three_or_more_jobs" if n >= 3 else f"{['zero_jobs','one_job','two_jobs'][n]}"
                changed = r1 is not None and r1 != r2
                cell = cells["job_to_resource_change"][group][status]
                cell["den"] += weight; cell["pairs"] += 1; cell["num"] += weight * changed
                outcomes.append(("job_to_resource_change", group, status, changed))
            if outcomes:
                pair_info[key] = outcomes

    rep_num = {state: {group: {status: np.zeros(REPLICATES) for status in ("yes", "no")}
                       for group in cells[state]} for state in states}
    rep_den = {state: {group: {status: np.zeros(REPLICATES) for status in ("yes", "no")}
                       for group in cells[state]} for state in states}
    replicate_rows_read = matched_rows = 0
    with zipfile.ZipFile(replicate_path) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            for row in reader:
                replicate_rows_read += 1
                key = tuple(row[field.lower()] for field in KEYS)
                outcomes = pair_info.get(key)
                if not outcomes:
                    continue
                matched_rows += 1
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)), dtype=float, count=REPLICATES)
                for state, group, status, changed in outcomes:
                    rep_den[state][group][status] += weights
                    if changed:
                        rep_num[state][group][status] += weights

    results = {}
    for state, groups in cells.items():
        results[state] = {}
        for group, statuses in groups.items():
            results[state][group] = {
                status: summarize(cell, rep_num[state][group][status], rep_den[state][group][status])
                for status, cell in statuses.items()
            }
    return {
        "format": "us-sipp-resource-job-worklimitation-crosslag-v1",
        "source_unit": "identified SIPP person, adjacent reference-month pair, conditioned on work-limiting status at month t",
        "weight": "WPFINWGT from first month; REPWGT1-REPWGT240 for Fay-BRR",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_persons": len(people),
        "replicate_rows_read": replicate_rows_read,
        "matched_pair_rows": matched_rows,
        "cells": results,
        "household_weight_used": False,
        "boundary": "Same-person monthly descriptive cross-lag conditioned on the SIPP work-limiting status field; it does not establish causality, household prevalence, disability diagnosis, accommodation, job quality, pay, care, trust, or political action.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = analyze(args.primary, args.replicate_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
