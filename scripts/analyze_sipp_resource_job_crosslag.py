#!/usr/bin/env python3
"""Estimate adjacent-month cross-lags between SIPP resources and job count."""

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
        return str(int(value))
    except (TypeError, ValueError):
        return None


def empty() -> dict[str, object]:
    return {"den": 0.0, "num": 0.0, "pairs": 0}


def result(bucket: dict[str, object], rep_num: np.ndarray | None = None,
          rep_den: np.ndarray | None = None) -> dict[str, object]:
    point = 100 * float(bucket["num"]) / float(bucket["den"]) if bucket["den"] else None
    out: dict[str, object] = {**bucket, "share_percent": point}
    if rep_num is None or rep_den is None or point is None:
        out["standard_error_percentage_points"] = None
        out["approx_95_ci_percentage_points"] = None
        return out
    estimates = np.divide(rep_num, rep_den, out=np.full(240, np.nan), where=rep_den != 0)
    se = float(np.sqrt(np.sum((estimates - point / 100) ** 2) / (240 * 0.5 ** 2)) * 100)
    out["standard_error_percentage_points"] = se
    out["approx_95_ci_percentage_points"] = [max(0, point - 1.96 * se), min(100, point + 1.96 * se)]
    return out


def analyze(primary_path: Path, replicate_path: Path | None) -> dict:
    people: dict[tuple[str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary_path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE", "WPFINWGT", "THINCPOV", "RMNUMJOBS"}
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
                people[(row["SSUID"], row["SPANEL"], row["SWAVE"], row["PNUM"])][month] = row

    pairs: dict[tuple[str, ...], tuple[str, str, float]] = {}
    cells = {
        "resource_to_job_change": defaultdict(empty),
        "job_to_resource_change": defaultdict(empty),
    }
    for person_months in people.values():
        for month in range(1, 12):
            first, second = person_months.get(month), person_months.get(month + 1)
            if not first or not second:
                continue
            resource_first, resource_second = band(first.get("THINCPOV", "")), band(second.get("THINCPOV", ""))
            jobs_first, jobs_second = jobs(first.get("RMNUMJOBS", "")), jobs(second.get("RMNUMJOBS", ""))
            try:
                weight = float(first["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            key = tuple(first[field] for field in KEYS)
            if resource_first and jobs_second:
                bucket = cells["resource_to_job_change"][resource_first]
                bucket["den"] += weight; bucket["pairs"] += 1
                bucket["num"] += weight * (jobs_first is not None and jobs_first != jobs_second)
                pairs[key] = ("resource_to_job_change", resource_first, weight)
            if jobs_first and resource_second:
                bucket = cells["job_to_resource_change"][jobs_first]
                bucket["den"] += weight; bucket["pairs"] += 1
                bucket["num"] += weight * (resource_first is not None and resource_first != resource_second)
                pairs[key] = ("job_to_resource_change", jobs_first, weight)

    rep_num: dict[str, dict[str, np.ndarray]] = defaultdict(dict)
    rep_den: dict[str, dict[str, np.ndarray]] = defaultdict(dict)
    replicate_rows_read = matched_rows = 0
    if replicate_path is not None:
        rep_num = {state: {group: np.zeros(240) for group in groups} for state, groups in cells.items()}
        rep_den = {state: {group: np.zeros(240) for group in groups} for state, groups in cells.items()}
        pair_outcomes: dict[tuple[str, ...], list[tuple[str, str, bool]]] = {}
        for person_months in people.values():
            for month in range(1, 12):
                first, second = person_months.get(month), person_months.get(month + 1)
                if not first or not second:
                    continue
                r1, r2, j1, j2 = band(first.get("THINCPOV", "")), band(second.get("THINCPOV", "")), jobs(first.get("RMNUMJOBS", "")), jobs(second.get("RMNUMJOBS", ""))
                key = tuple(first[field] for field in KEYS)
                outcomes = []
                if r1 and j2:
                    outcomes.append(("resource_to_job_change", r1, j1 is not None and j1 != j2))
                if j1 and r2:
                    outcomes.append(("job_to_resource_change", j1, r1 is not None and r1 != r2))
                if outcomes:
                    pair_outcomes[key] = outcomes
        with zipfile.ZipFile(replicate_path) as archive:
            with archive.open("rw2025.csv") as raw:
                reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
                for row in reader:
                    replicate_rows_read += 1
                    key = tuple(row[field.lower()] for field in KEYS)
                    outcomes = pair_outcomes.get(key)
                    if not outcomes:
                        continue
                    matched_rows += 1
                    weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, 241)), dtype=float, count=240)
                    for state, group, changed in outcomes:
                        rep_den[state][group] += weights
                        if changed:
                            rep_num[state][group] += weights

    output_cells = {}
    for state, groups in cells.items():
        output_cells[state] = {}
        for group, bucket in groups.items():
            output_cells[state][group] = result(bucket, rep_num.get(state, {}).get(group), rep_den.get(state, {}).get(group))
    return {"format": "us-sipp-resource-job-crosslag-v1", "source_unit": "identified SIPP person record, adjacent reference months", "weight": "WPFINWGT from first month; REPWGT1–240 for Fay-BRR", "variance_method": "Fay BRR, G=240, perturbation factor 0.5" if replicate_path else None, "rows_read": rows_read, "identified_persons": len(people), "replicate_rows_read": replicate_rows_read, "matched_pair_rows": matched_rows, "cells": output_cells, "household_weight_used": False, "boundary": "Same-person monthly descriptive cross-lag for explicitly monthly THINCPOV and RMNUMJOBS fields; it does not establish causality, household prevalence, hours, pay, care, trust, or political action."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = analyze(args.primary, args.replicate_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
