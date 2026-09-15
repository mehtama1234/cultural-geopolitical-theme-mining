#!/usr/bin/env python3
"""Estimate annual child-care work prevention by utility difficulty and tenure."""

from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from collections import OrderedDict
from pathlib import Path

import numpy as np

KEYS = ("SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE")
GROUPS = OrderedDict(
    (
        ("utility_difficulty__owned_or_bought", ("difficulty", "owned_or_bought")),
        ("utility_difficulty__rented", ("difficulty", "rented")),
        ("no_utility_difficulty__owned_or_bought", ("no_difficulty", "owned_or_bought")),
        ("no_utility_difficulty__rented", ("no_difficulty", "rented")),
    )
)
REPLICATES = 240
FAY_FACTOR = 0.5


def valid(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def summary(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray, records: int) -> dict:
    share = num / den if den else None
    estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    se = None
    if share is not None and not np.isnan(estimates).any():
        se = float(np.sqrt(np.sum((estimates - share) ** 2) / (REPLICATES * FAY_FACTOR**2)))
    return {
        "records": records,
        "weighted_denominator": den,
        "share_percent": 100 * share if share is not None else None,
        "standard_error_percentage_points": 100 * se if se is not None else None,
        "approx_95_percent_ci": ([max(0.0, 100 * share - 1.96 * 100 * se), min(100.0, 100 * share + 1.96 * 100 * se)] if se is not None else None),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    people = {}
    rows_read = 0
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "EWORKMORE", "AWORKMORE", "EAWBGAS", "AAWBGAS", "ETENURE"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            if row["MONTHCODE"] != "12" or not valid(row["EWORKMORE"], row["AWORKMORE"]):
                continue
            if not valid(row["EAWBGAS"], row["AAWBGAS"]) or row["ETENURE"] not in {"1", "2"}:
                continue
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            tenure = "owned_or_bought" if row["ETENURE"] == "1" else "rented"
            utility = "utility_difficulty" if row["EAWBGAS"] == "1" else "no_utility_difficulty"
            group = f"{utility}__{tenure}"
            key = tuple(row[k] for k in KEYS)
            people[key] = (group, row["EWORKMORE"], weight)

    num = {group: 0.0 for group in GROUPS}
    den = {group: 0.0 for group in GROUPS}
    records = {group: 0 for group in GROUPS}
    for group, outcome, weight in people.values():
        den[group] += weight
        records[group] += 1
        if outcome == "1":
            num[group] += weight

    rep_num = {group: np.zeros(REPLICATES) for group in GROUPS}
    rep_den = {group: np.zeros(REPLICATES) for group in GROUPS}
    matched = 0
    with zipfile.ZipFile(args.replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            for row in reader:
                key = tuple(row[k.lower()] for k in KEYS)
                item = people.get(key)
                if item is None:
                    continue
                matched += 1
                group, outcome, _ = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)), dtype=np.float64, count=REPLICATES)
                rep_den[group] += weights
                if outcome == "1":
                    rep_num[group] += weights

    output = {
        "format": "us-sipp-utility-tenure-childcare-fay-brr-v1",
        "source_unit": "December identified reference-parent person rows with valid annual fall child-care work-prevention status, utility-payment difficulty, and tenure",
        "reference_period": "2024",
        "weight": "WPFINWGT from December; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_records": len(people),
        "replicate_rows_matched": matched,
        "results": {group: summary(num[group], den[group], rep_num[group], rep_den[group], records[group]) for group in GROUPS},
        "causal_estimation": False,
        "boundary": "EWORKMORE describes annual fall child-care arrangements preventing work or additional work in the reference-parent universe. Utility difficulty and tenure are December conditions. This is a descriptive conditional bridge, not a dated bill shock, tenure effect, monthly care estimate, or causal result.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "identified_records": len(people), "replicate_rows_matched": matched}, indent=2))


if __name__ == "__main__":
    main()
