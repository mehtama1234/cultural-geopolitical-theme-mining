#!/usr/bin/env python3
"""Estimate Fay-BRR uncertainty for adjacent-month SIPP SNAP transitions."""

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
TRANSITIONS = ("no -> no", "no -> yes", "yes -> no", "yes -> yes")
SNAP_LABELS = {"1": "yes", "2": "no"}
REPLICATES = 240
FAY_FACTOR = 0.5


def transition_label(before: str, after: str) -> str | None:
    if before not in SNAP_LABELS or after not in SNAP_LABELS:
        return None
    return f"{SNAP_LABELS[before]} -> {SNAP_LABELS[after]}"


def estimate(num: float, den: float) -> float | None:
    return num / den if den else None


def summarize(full_num: np.ndarray, full_den: float, rep_num: np.ndarray,
              rep_den: np.ndarray, pairs: int) -> dict:
    theta = estimate(float(full_num), full_den)
    reps = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    valid = ~np.isnan(reps)
    se = None
    if theta is not None and valid.all():
        variance = np.sum((reps - theta) ** 2) / (REPLICATES * FAY_FACTOR**2)
        se = float(np.sqrt(variance))
    return {
        "pairs": pairs,
        "weight": full_den,
        "share_percent": 100 * theta if theta is not None else None,
        "standard_error_percentage_points": 100 * se if se is not None else None,
        "approx_95_percent_ci": ([max(0.0, 100 * theta - 1.96 * 100 * se),
                                   min(100.0, 100 * theta + 1.96 * 100 * se)]
                                  if theta is not None and se is not None else None),
    }


def analyze(primary_path: Path, replicate_zip: Path) -> dict:
    months: dict[tuple[str, str, str, str], dict[int, tuple[str, float]]] = defaultdict(dict)
    rows_read = 0
    with primary_path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "RSNAP_MNYN"}
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
                months[person][month] = (row.get("RSNAP_MNYN", ""), weight)

    by_key: dict[tuple[str, str, str, str, str], str] = {}
    full_num = {label: 0.0 for label in TRANSITIONS}
    full_den = 0.0
    pair_counts = {label: 0 for label in TRANSITIONS}
    for person, records in months.items():
        for month in range(1, 12):
            if month not in records or month + 1 not in records:
                continue
            before, weight = records[month]
            after, _ = records[month + 1]
            label = transition_label(before, after)
            if label is None:
                continue
            key = person + (str(month),)
            by_key[key] = label
            full_den += weight
            full_num[label] += weight
            pair_counts[label] += 1

    rep_num = {label: np.zeros(REPLICATES, dtype=np.float64) for label in TRANSITIONS}
    rep_den = np.zeros(REPLICATES, dtype=np.float64)
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
                label = by_key.get(key)
                if label is None:
                    continue
                matched += 1
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                                      dtype=np.float64, count=REPLICATES)
                rep_den += weights
                rep_num[label] += weights

    return {
        "format": "us-sipp-snap-transition-fay-brr-v1",
        "source_unit": "identified person, adjacent reference-month pair",
        "weight": "WPFINWGT from first month; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "positive_weight_transition_pairs": matched,
        "valid_transition_pairs": sum(pair_counts.values()),
        "results": {
            label: summarize(np.array(full_num[label]), full_den,
                             rep_num[label], rep_den, pair_counts[label])
            for label in TRANSITIONS
        },
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
