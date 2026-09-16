#!/usr/bin/env python3
"""Estimate childcare-related work time lost by prior utility difficulty/tenure."""

from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from collections import OrderedDict, defaultdict
from pathlib import Path

import numpy as np

KEY_FIELDS = ("SSUID", "PNUM", "SPANEL", "SWAVE")
MONTH_KEY = KEY_FIELDS + ("MONTHCODE",)
REPLICATES = 240
FAY_FACTOR = 0.5


def numeric_hours(value: str) -> float | None:
    try:
        hours = float(value)
    except (TypeError, ValueError):
        return None
    return hours if 0 <= hours <= 168 else None


def valid(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def mean_summary(total: float, weight: float, rep_total: np.ndarray,
                 rep_weight: np.ndarray, records: int) -> dict:
    mean = total / weight if weight else None
    estimates = np.divide(rep_total, rep_weight, out=np.full(REPLICATES, np.nan),
                          where=rep_weight != 0)
    se = None
    if mean is not None and not np.isnan(estimates).any():
        se = float(np.sqrt(np.sum((estimates - mean) ** 2) /
                           (REPLICATES * FAY_FACTOR**2)))
    return {
        "records": records,
        "weighted_denominator": weight,
        "mean_hours": mean,
        "standard_error_hours": se,
        "approx_95_percent_ci_hours": ([
            max(0.0, mean - 1.96 * se), mean + 1.96 * se
        ] if se is not None else None),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    by_person: dict[tuple[str, ...], dict[str, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    required = {
        "SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE", "WPFINWGT",
        "EAWBGAS", "AAWBGAS", "ETENURE", "EWORKMORE", "AWORKMORE",
        "ETIMELOST", "ATIMELOST",
    }
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            if row["MONTHCODE"] in {"11", "12"}:
                by_person[tuple(row[k] for k in KEY_FIELDS)][row["MONTHCODE"]] = row

    pairs: dict[tuple[str, ...], tuple[str, float, float]] = {}
    groups: OrderedDict[str, dict[str, float]] = OrderedDict()
    for months in by_person.values():
        before, after = months.get("11"), months.get("12")
        if before is None or after is None:
            continue
        if not valid(before["EAWBGAS"], before["AAWBGAS"]):
            continue
        if before["ETENURE"] not in {"1", "2"}:
            continue
        if not valid(after["EWORKMORE"], after["AWORKMORE"]):
            continue
        if after["EWORKMORE"] != "1" or not valid(after["ETIMELOST"], after["ATIMELOST"]):
            continue
        hours = numeric_hours(after["ETIMELOST"])
        if hours is None:
            continue
        try:
            weight = float(before["WPFINWGT"])
        except (TypeError, ValueError):
            continue
        if weight <= 0:
            continue
        group = "{}__{}".format(
            "difficulty" if before["EAWBGAS"] == "1" else "no_difficulty",
            "owner_buyer" if before["ETENURE"] == "1" else "renter",
        )
        groups.setdefault(group, {"total": 0.0, "weight": 0.0, "records": 0})
        pairs[tuple(before[k] for k in MONTH_KEY)] = (group, hours, weight)

    rep_total = {group: np.zeros(REPLICATES) for group in groups}
    rep_weight = {group: np.zeros(REPLICATES) for group in groups}
    matched_keys: set[tuple[str, ...]] = set()
    with zipfile.ZipFile(args.replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            for row in reader:
                key = tuple(row[k.lower()] for k in MONTH_KEY)
                item = pairs.get(key)
                if item is None:
                    continue
                matched_keys.add(key)
                group, hours, _ = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                                      dtype=np.float64, count=REPLICATES)
                rep_weight[group] += weights
                rep_total[group] += weights * hours
    unmatched = sorted(set(pairs) - matched_keys)
    if unmatched:
        raise ValueError(f"{len(unmatched)} selected time-loss keys absent from replicate archive; first={unmatched[0]}")

    for group, hours, weight in pairs.values():
        groups[group]["total"] += weight * hours
        groups[group]["weight"] += weight
        groups[group]["records"] += 1
    output = {
        "format": "us-sipp-utility-time-loss-following-fay-brr-v1",
        "source_unit": "positive-weight November-to-December person pairs; utility difficulty and tenure at month t, EWORKMORE and ETIMELOST at month t+1",
        "reference_period": "2024 reference year in 2025 SIPP public-use file",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 from month t for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_pairs": len(pairs),
        "replicate_pairs_matched": len(matched_keys),
        "results": {
            group: mean_summary(values["total"], values["weight"], rep_total[group],
                                rep_weight[group], int(values["records"]))
            for group, values in groups.items()
        },
        "causal_estimation": False,
        "boundary": "ETIMELOST is conditional on EWORKMORE=1 and reports a fall-reference-year childcare-related work time-loss amount; it is not a monthly loss caused by utility difficulty. No no-prevention comparison is defined.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "identified_pairs": len(pairs),
                      "replicate_pairs_matched": len(matched_keys)}, indent=2))


if __name__ == "__main__":
    main()
