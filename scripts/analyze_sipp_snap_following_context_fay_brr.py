#!/usr/bin/env python3
"""Estimate Fay-BRR context in the month following a SNAP transition."""

from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from collections import defaultdict
from pathlib import Path

import numpy as np

from analyze_sipp_snap_transition_context_fay_brr import (
    CHANGE_CATEGORIES,
    FAY_FACTOR,
    KEYS,
    REPLICATES,
    TRANSITIONS,
    change,
    snap_label,
    summary,
)

KINDS = ("resource", "earnings", "hours", "jobs")
FIELDS = {"RSNAP_MNYN": "snap", "THINCPOV": "resource", "TPEARN": "earnings", "TMWKHRS": "hours", "RMNUMJOBS": "jobs"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    months: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", *FIELDS}
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
                months[person][month] = {dest: row.get(source, "") for source, dest in FIELDS.items()}
                months[person][month]["weight"] = row["WPFINWGT"]

    pair_data: dict[tuple[str, str, str, str, str], tuple[str, dict[str, str | None]]] = {}
    full_den = {t: {k: 0.0 for k in KINDS} for t in TRANSITIONS}
    full_num = {t: {k: {c: 0.0 for c in CHANGE_CATEGORIES} for k in KINDS} for t in TRANSITIONS}
    record_den = {t: {k: 0 for k in KINDS} for t in TRANSITIONS}
    record_num = {t: {k: {c: 0 for c in CHANGE_CATEGORIES} for k in KINDS} for t in TRANSITIONS}

    for person, records in months.items():
        for month in range(1, 11):
            if month not in records or month + 1 not in records or month + 2 not in records:
                continue
            first, second, third = records[month], records[month + 1], records[month + 2]
            transition = f"{snap_label(first['snap'])} -> {snap_label(second['snap'])}"
            if transition not in TRANSITIONS:
                continue
            outcomes = {
                kind: change(second[kind], third[kind], integer=(kind == "jobs"))
                for kind in KINDS
            }
            key = person + (str(month),)
            pair_data[key] = (transition, outcomes)
            weight = float(first["weight"])
            for kind, category in outcomes.items():
                if category is None:
                    continue
                full_den[transition][kind] += weight
                full_num[transition][kind][category] += weight
                record_den[transition][kind] += 1
                record_num[transition][kind][category] += 1

    rep_num = {t: {k: {c: np.zeros(REPLICATES) for c in CHANGE_CATEGORIES} for k in KINDS} for t in TRANSITIONS}
    rep_den = {t: {k: np.zeros(REPLICATES) for k in KINDS} for t in TRANSITIONS}
    replicate_rows_read = 0
    matched = 0
    with zipfile.ZipFile(args.replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            for row in reader:
                replicate_rows_read += 1
                key = tuple(row[key.lower()] for key in KEYS)
                item = pair_data.get(key)
                if item is None:
                    continue
                matched += 1
                transition, outcomes = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)), dtype=np.float64, count=REPLICATES)
                for kind, category in outcomes.items():
                    if category is None:
                        continue
                    rep_den[transition][kind] += weights
                    rep_num[transition][kind][category] += weights

    results = {}
    for transition in TRANSITIONS:
        results[transition] = {}
        for kind in KINDS:
            results[transition][kind] = {
                category: summary(full_num[transition][kind][category], full_den[transition][kind], rep_num[transition][kind][category], rep_den[transition][kind], record_num[transition][kind][category])
                for category in CHANGE_CATEGORIES
            }
            results[transition][kind]["valid_records"] = record_den[transition][kind]
            results[transition][kind]["valid_weight"] = full_den[transition][kind]

    output = {
        "format": "us-sipp-snap-following-context-fay-brr-v1",
        "source_unit": "identified person, SNAP transition at month t -> t+1, following context change at t+1 -> t+2",
        "weight": "WPFINWGT from transition-start month; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "following_transition_pairs_matched": matched,
        "results": results,
        "causal_estimation": False,
        "household_weight_used": False,
        "boundary": "Following context is descriptive and selected. It does not estimate SNAP effects, benefit adequacy, notice, effort, remedy, or recovery; fields retain separate person, household, job-holder, and job-count universes."
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "replicate_rows_read": replicate_rows_read, "matched": matched}, indent=2))


if __name__ == "__main__":
    main()
