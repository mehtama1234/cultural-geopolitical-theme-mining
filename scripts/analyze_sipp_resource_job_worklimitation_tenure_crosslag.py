#!/usr/bin/env python3
"""Estimate SIPP adjacent-month resource/job cross-lags by tenure and work limitation."""

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
TENURES = {"1": "owned_or_being_bought", "2": "rented", "3": "occupied_without_rent"}
STATUSES = {"1": "work_limited", "2": "not_work_limited"}


def band(value: str) -> str | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number < 1:
        return "below_1x"
    if number < 2:
        return "1_to_2x"
    if number < 4:
        return "2_to_4x"
    return "4x_or_more"


def jobs(value: str) -> str | None:
    try:
        return str(int(float(value)))
    except (TypeError, ValueError):
        return None


def share(cell: dict[str, float], rep_num: np.ndarray, rep_den: np.ndarray) -> dict[str, object]:
    point = 100 * cell["num"] / cell["den"] if cell["den"] else None
    if point is None:
        se = None
    else:
        estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
        se = float(np.sqrt(np.nansum((estimates - point / 100) ** 2) / (REPLICATES * FAY_FACTOR**2)) * 100)
    return {
        **cell,
        "share_percent": point,
        "standard_error_percentage_points": se,
        "approx_95_ci_percentage_points": [max(0.0, point - 1.96 * se), min(100.0, point + 1.96 * se)] if point is not None and se is not None else None,
    }


def empty() -> dict[str, float]:
    return {"den": 0.0, "num": 0.0, "pairs": 0}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    people: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    atensure_counts: dict[str, int] = defaultdict(int)
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "THINCPOV", "RMNUMJOBS", "EDISABL", "ETENURE", "ATENURE"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            atensure_counts[row.get("ATENURE", "<blank>")] += 1
            try:
                month, weight = int(row["MONTHCODE"]), float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if 1 <= month <= 12 and weight > 0:
                person = tuple(row[key] for key in KEYS[:-1])
                people[person][month] = {field: row.get(field, "") for field in ("THINCPOV", "RMNUMJOBS", "EDISABL", "ETENURE", "ATENURE", "WPFINWGT")}

    states = ("resource_to_job_change", "job_to_resource_change")
    resource_groups = ("below_1x", "1_to_2x", "2_to_4x", "4x_or_more")
    job_groups = ("zero_jobs", "one_job", "two_jobs", "three_or_more_jobs")
    cells = {state: {} for state in states}
    for tenure in TENURES:
        for status in STATUSES.values():
            for group in resource_groups:
                cells["resource_to_job_change"][f"{tenure}|{status}|{group}"] = empty()
            for group in job_groups:
                cells["job_to_resource_change"][f"{tenure}|{status}|{group}"] = empty()

    pair_info: dict[tuple[str, str, str, str, str], list[tuple[str, str, bool]]] = {}
    for person, records in people.items():
        for month in range(1, 12):
            first, second = records.get(month), records.get(month + 1)
            if not first or not second or first["ATENURE"] in {"", "0"} or first["ETENURE"] not in TENURES:
                continue
            status = STATUSES.get(first["EDISABL"])
            tenure = first["ETENURE"]
            r1, r2 = band(first["THINCPOV"]), band(second["THINCPOV"])
            j1, j2 = jobs(first["RMNUMJOBS"]), jobs(second["RMNUMJOBS"])
            if not status:
                continue
            weight = float(first["WPFINWGT"])
            key = person + (str(month),)
            outcomes: list[tuple[str, str, bool]] = []
            if r1 and j2:
                group_key = f"{tenure}|{status}|{r1}"
                changed = j1 is not None and j1 != j2
                cells["resource_to_job_change"][group_key]["den"] += weight
                cells["resource_to_job_change"][group_key]["num"] += weight * changed
                cells["resource_to_job_change"][group_key]["pairs"] += 1
                outcomes.append(("resource_to_job_change", group_key, changed))
            if j1 and r2:
                n = int(j1)
                group = "three_or_more_jobs" if n >= 3 else ("zero_jobs", "one_job", "two_jobs")[n]
                group_key = f"{tenure}|{status}|{group}"
                changed = r1 is not None and r1 != r2
                cells["job_to_resource_change"][group_key]["den"] += weight
                cells["job_to_resource_change"][group_key]["num"] += weight * changed
                cells["job_to_resource_change"][group_key]["pairs"] += 1
                outcomes.append(("job_to_resource_change", group_key, changed))
            if outcomes:
                pair_info[key] = outcomes

    rep_num = {state: {key: np.zeros(REPLICATES) for key in cells[state]} for state in states}
    rep_den = {state: {key: np.zeros(REPLICATES) for key in cells[state]} for state in states}
    replicate_rows_read = matched_pair_rows = 0
    with zipfile.ZipFile(args.replicate_zip) as archive, archive.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for row in reader:
            replicate_rows_read += 1
            key = tuple(row[field.lower()] for field in KEYS)
            outcomes = pair_info.get(key)
            if not outcomes:
                continue
            matched_pair_rows += 1
            weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)), dtype=float, count=REPLICATES)
            for state, group_key, changed in outcomes:
                rep_den[state][group_key] += weights
                if changed:
                    rep_num[state][group_key] += weights

    results = {state: {} for state in states}
    for state in states:
        for key, cell in cells[state].items():
            tenure, status, group = key.split("|", 2)
            results[state].setdefault(TENURES[tenure], {}).setdefault(status, {})[group] = share(cell, rep_num[state][key], rep_den[state][key])
    output = {
        "format": "us-sipp-resource-job-worklimitation-tenure-crosslag-v1",
        "source_unit": "identified SIPP person, adjacent reference-month pair, conditioned on first-month tenure and work-limiting status",
        "weight": "WPFINWGT from first month; REPWGT1-REPWGT240 for Fay-BRR",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_persons": len(people),
        "replicate_rows_read": replicate_rows_read,
        "matched_pair_rows": matched_pair_rows,
        "ATENURE_counts": dict(sorted(atensure_counts.items())),
        "tenure_labels": TENURES,
        "status_labels": STATUSES,
        "cells": results,
        "household_weight_used": False,
        "boundary": "Same-person monthly descriptive cross-lag conditioned on official tenure category and reported work-limiting status; it does not establish causality, household prevalence, disability diagnosis, accommodation, job quality, pay, care, trust, political action, or recovery.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
