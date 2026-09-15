#!/usr/bin/env python3
"""Estimate following-month SNAP-transition hardship by resource band."""

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
TRANSITIONS = ("no -> no", "no -> yes", "yes -> no", "yes -> yes")
RESOURCE_LABELS = {
    "lt1": "below 1.00x poverty threshold",
    "1to2": "1.00–1.99x poverty threshold",
    "2to4": "2.00–3.99x poverty threshold",
    "ge4": "4.00x poverty threshold or more",
}


def resource_band(value: str) -> str | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number < 1:
        return "lt1"
    if number < 2:
        return "1to2"
    if number < 4:
        return "2to4"
    return "ge4"


def snap(value: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(value)


def valid(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def summarize(num: float, den: float, rep_num: np.ndarray,
              rep_den: np.ndarray, records: int) -> dict:
    theta = num / den if den else None
    estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    se = None
    if theta is not None and not np.isnan(estimates).any():
        variance = np.sum((estimates - theta) ** 2) / (REPLICATES * FAY_FACTOR ** 2)
        se = float(np.sqrt(variance))
    return {
        "records": records,
        "weight": den,
        "share_percent": 100 * theta if theta is not None else None,
        "standard_error_percentage_points": 100 * se if se is not None else None,
        "approx_95_percent_ci": (
            [max(0.0, 100 * theta - 1.96 * 100 * se),
             min(100.0, 100 * theta + 1.96 * 100 * se)]
            if theta is not None and se is not None else None
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    people = defaultdict(dict)
    rows_read = 0
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "RSNAP_MNYN", "THINCPOV",
                                 "EAWBMORT", "EAWBGAS", "AAWBMORT", "AAWBGAS"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                month = int(row["MONTHCODE"])
                float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if not 1 <= month <= 12:
                continue
            person = tuple(row[key] for key in KEYS[:-1])
            people[person][month] = {
                "snap": row["RSNAP_MNYN"],
                "resource": resource_band(row["THINCPOV"]),
                "mort": row["EAWBMORT"], "mort_flag": row["AAWBMORT"],
                "gas": row["EAWBGAS"], "gas_flag": row["AAWBGAS"],
                "weight": row["WPFINWGT"],
            }

    buckets = [f"{transition}|{resource}" for transition in TRANSITIONS
               for resource in RESOURCE_LABELS]
    num = {b: {o: 0.0 for o in ("mort", "gas")} for b in buckets}
    den = {b: {o: 0.0 for o in ("mort", "gas")} for b in buckets}
    records = {b: {o: 0 for o in ("mort", "gas")} for b in buckets}
    pair_data = {}
    for person, months in people.items():
        for month in range(1, 12):
            if month not in months or month + 1 not in months:
                continue
            before, after = months[month], months[month + 1]
            transition = f"{snap(before['snap'])} -> {snap(after['snap'])}"
            resource = before["resource"]
            if transition not in TRANSITIONS or resource not in RESOURCE_LABELS:
                continue
            bucket = f"{transition}|{resource}"
            outcomes = {
                "mort": valid(after["mort"], after["mort_flag"]),
                "gas": valid(after["gas"], after["gas_flag"]),
            }
            key = person + (str(month),)
            pair_data[key] = (bucket, outcomes)
            weight = float(before["weight"])
            for outcome, is_valid in outcomes.items():
                if not is_valid:
                    continue
                den[bucket][outcome] += weight
                records[bucket][outcome] += 1
                if after[outcome] == "1":
                    num[bucket][outcome] += weight

    rep_num = {b: {o: np.zeros(REPLICATES) for o in ("mort", "gas")} for b in buckets}
    rep_den = {b: {o: np.zeros(REPLICATES) for o in ("mort", "gas")} for b in buckets}
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
                bucket, outcomes = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                                      dtype=np.float64, count=REPLICATES)
                person = key[:-1]
                month = int(key[-1])
                after = people[person][month + 1]
                for outcome, is_valid in outcomes.items():
                    if not is_valid:
                        continue
                    rep_den[bucket][outcome] += weights
                    if after[outcome] == "1":
                        rep_num[bucket][outcome] += weights

    results = {}
    for bucket in buckets:
        transition, resource = bucket.split("|", 1)
        results[bucket] = {
            "transition": transition,
            "resource_band": resource,
            "resource_label": RESOURCE_LABELS[resource],
            "outcomes": {
                outcome: summarize(num[bucket][outcome], den[bucket][outcome],
                                   rep_num[bucket][outcome], rep_den[bucket][outcome],
                                   records[bucket][outcome])
                for outcome in ("mort", "gas")
            },
        }

    output = {
        "format": "us-sipp-snap-transition-resource-fay-brr-v1",
        "source_unit": "identified person, adjacent reference-month pair",
        "transition": "SNAP receipt in month t -> month t+1",
        "grouping": "THINCPOV at month t",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "transition_pairs_matched": matched,
        "results": results,
        "causal_estimation": False,
        "household_weight_used": False,
        "boundary": "Hardship fields have their own universes and may be reference-period measures; resource bands are descriptive context, not eligibility or program-effect estimates.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "matched_pairs": matched, "cells": len(results)}, indent=2))


if __name__ == "__main__":
    main()
