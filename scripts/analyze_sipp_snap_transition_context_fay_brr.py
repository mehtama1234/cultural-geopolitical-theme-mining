#!/usr/bin/env python3
"""Estimate Fay-BRR uncertainty for resource/job changes around SNAP transitions."""

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
TRANSITIONS = ("no -> yes", "yes -> no")
CHANGE_CATEGORIES = ("down", "same", "up")
REPLICATES = 240
FAY_FACTOR = 0.5


def snap_label(value: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(value)


def numeric(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def change(before: str, after: str, integer: bool = False) -> str | None:
    left, right = numeric(before), numeric(after)
    if left is None or right is None:
        return None
    if integer:
        left, right = int(left), int(right)
    if right < left:
        return "down"
    if right > left:
        return "up"
    return "same"


def summary(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray,
            records: int) -> dict:
    theta = num / den if den else None
    reps = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    se = None
    if theta is not None and not np.isnan(reps).any():
        variance = np.sum((reps - theta) ** 2) / (REPLICATES * FAY_FACTOR**2)
        se = float(np.sqrt(variance))
    return {
        "records": records,
        "weight": den,
        "share_percent": 100 * theta if theta is not None else None,
        "standard_error_percentage_points": 100 * se if se is not None else None,
        "approx_95_percent_ci": ([max(0.0, 100 * theta - 1.96 * 100 * se),
                                   min(100.0, 100 * theta + 1.96 * 100 * se)]
                                  if theta is not None and se is not None else None),
    }


def analyze(primary_path: Path, replicate_zip: Path) -> dict:
    months: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary_path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "RSNAP_MNYN", "THINCPOV", "RMNUMJOBS"}
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
                months[person][month] = {
                    "snap": row.get("RSNAP_MNYN", ""),
                    "resource": row.get("THINCPOV", ""),
                    "jobs": row.get("RMNUMJOBS", ""),
                    "weight": row.get("WPFINWGT", ""),
                }

    pair_data: dict[tuple[str, str, str, str, str], tuple[str, str | None, str | None]] = {}
    full_den = {transition: {kind: 0.0 for kind in ("resource", "jobs")} for transition in TRANSITIONS}
    full_num = {transition: {kind: {cat: 0.0 for cat in CHANGE_CATEGORIES} for kind in ("resource", "jobs")}
                for transition in TRANSITIONS}
    record_den = {transition: {kind: 0 for kind in ("resource", "jobs")} for transition in TRANSITIONS}
    record_num = {transition: {kind: {cat: 0 for cat in CHANGE_CATEGORIES} for kind in ("resource", "jobs")}
                  for transition in TRANSITIONS}

    for person, records in months.items():
        for month in range(1, 12):
            if month not in records or month + 1 not in records:
                continue
            first, second = records[month], records[month + 1]
            transition = f"{snap_label(first['snap'])} -> {snap_label(second['snap'])}"
            if transition not in TRANSITIONS:
                continue
            resource_change = change(first["resource"], second["resource"])
            job_change = change(first["jobs"], second["jobs"], integer=True)
            key = person + (str(month),)
            pair_data[key] = (transition, resource_change, job_change)
            weight = float(first["weight"])
            for kind, category in (("resource", resource_change), ("jobs", job_change)):
                if category is None:
                    continue
                full_den[transition][kind] += weight
                full_num[transition][kind][category] += weight
                record_den[transition][kind] += 1
                record_num[transition][kind][category] += 1

    rep_num = {transition: {kind: {cat: np.zeros(REPLICATES, dtype=np.float64) for cat in CHANGE_CATEGORIES}
                            for kind in ("resource", "jobs")} for transition in TRANSITIONS}
    rep_den = {transition: {kind: np.zeros(REPLICATES, dtype=np.float64) for kind in ("resource", "jobs")}
               for transition in TRANSITIONS}
    replicate_rows_read = 0
    matched = 0
    with zipfile.ZipFile(replicate_zip) as archive:
        if archive.namelist() != ["rw2025.csv"]:
            raise ValueError(f"unexpected replicate archive members: {archive.namelist()}")
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            required = {key.lower() for key in KEYS} | {f"repwgt{i}" for i in range(1, REPLICATES + 1)}
            missing = sorted(required - set(reader.fieldnames or []))
            if missing:
                raise ValueError("replicate file is missing fields: " + ", ".join(missing[:8]))
            for row in reader:
                replicate_rows_read += 1
                key = tuple(row[key.lower()] for key in KEYS)
                item = pair_data.get(key)
                if item is None:
                    continue
                matched += 1
                transition, resource_change, job_change = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                                      dtype=np.float64, count=REPLICATES)
                for kind, category in (("resource", resource_change), ("jobs", job_change)):
                    if category is None:
                        continue
                    rep_den[transition][kind] += weights
                    rep_num[transition][kind][category] += weights

    results = {}
    for transition in TRANSITIONS:
        results[transition] = {}
        for kind in ("resource", "jobs"):
            results[transition][kind] = {
                category: summary(full_num[transition][kind][category], full_den[transition][kind],
                                  rep_num[transition][kind][category], rep_den[transition][kind],
                                  record_num[transition][kind][category])
                for category in CHANGE_CATEGORIES
            }
            results[transition][kind]["valid_records"] = record_den[transition][kind]
            results[transition][kind]["valid_weight"] = full_den[transition][kind]

    return {
        "format": "us-sipp-snap-transition-context-fay-brr-v1",
        "source_unit": "identified person, adjacent reference-month pair",
        "weight": "WPFINWGT from first month; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "positive_weight_transition_pairs_matched": matched,
        "results": results,
        "causal_estimation": False,
        "household_weight_used": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.primary, args.replicate_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
