#!/usr/bin/env python3
"""Estimate adjacent-month SIPP utility/energy-assistance to food security screens."""

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
FAY = 0.5


def valid_binary(value: str, flag: str | None = None) -> bool:
    return value in {"1", "2"} and (flag is None or flag not in {"", "0"})


def summarize(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray, n: int) -> dict[str, object]:
    share = num / den if den else None
    estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    se = None
    if share is not None and not np.isnan(estimates).any():
        se = float(np.sqrt(np.sum((estimates - share) ** 2) / (REPLICATES * FAY**2)))
    return {
        "valid_pair_n": n,
        "share_percent": 100 * share if share is not None else None,
        "standard_error_percentage_points": 100 * se if se is not None else None,
        "approx_95_ci_percentage_points": ([
            max(0.0, 100 * share - 1.96 * 100 * se),
            min(100.0, 100 * share + 1.96 * 100 * se),
        ] if se is not None else None),
    }


def analyze(primary: Path, replicate_zip: Path) -> dict[str, object]:
    people: dict[tuple[str, ...], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "EAWBGAS", "AAWBGAS", "EENERGY_ASST", "RFOODS", "AFOODS"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice missing: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                month = int(row["MONTHCODE"])
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if not 1 <= month <= 12 or weight <= 0:
                continue
            people[tuple(row[k] for k in KEYS[:-1])][month] = row

    groups = ("utility_difficulty", "no_utility_difficulty", "energy_assistance", "no_energy_assistance")
    joint_groups = (
        "utility_difficulty__energy_assistance",
        "utility_difficulty__no_energy_assistance",
        "no_utility_difficulty__energy_assistance",
        "no_utility_difficulty__no_energy_assistance",
    )
    all_groups = groups + joint_groups
    pairs: dict[tuple[str, ...], list[tuple[str, bool, str | None, float]]] = {}
    cells = {group: {"pairs": 0, "food_valid_n": 0, "food_den": 0.0, "food_num": 0.0, "food_category_num": {"high_or_marginal": 0.0, "low": 0.0, "very_low": 0.0}} for group in all_groups}
    food_valid_keys: set[tuple[str, ...]] = set()
    for person, months in people.items():
        for month in range(1, 12):
            before, after = months.get(month), months.get(month + 1)
            if before is None or after is None:
                continue
            try:
                weight = float(before["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if weight <= 0:
                continue
            exposure_groups = []
            utility_valid = valid_binary(before.get("EAWBGAS", ""), before.get("AAWBGAS", ""))
            assistance_valid = valid_binary(before.get("EENERGY_ASST", ""))
            utility_group = "utility_difficulty" if before.get("EAWBGAS") == "1" else "no_utility_difficulty"
            assistance_group = "energy_assistance" if before.get("EENERGY_ASST") == "1" else "no_energy_assistance"
            if utility_valid:
                exposure_groups.append(utility_group)
            if assistance_valid:
                exposure_groups.append(assistance_group)
            if utility_valid and assistance_valid:
                exposure_groups.append(f"{utility_group}__{assistance_group}")
            if not exposure_groups:
                continue
            food_valid = after.get("RFOODS", "") in {"1", "2", "3"} and after.get("AFOODS", "") not in {"", "0"}
            key = tuple(before[k] for k in KEYS)
            for group in exposure_groups:
                category = {
                    "1": "high_or_marginal",
                    "2": "low",
                    "3": "very_low",
                }.get(after.get("RFOODS", "")) if food_valid else None
                pairs[key + (group,)] = [(group, after.get("RFOODS") in {"2", "3"}, category, weight)]
                cells[group]["pairs"] += 1
                if food_valid:
                    food_valid_keys.add(key + (group,))
                    cells[group]["food_valid_n"] += 1
                    cells[group]["food_den"] += weight
                    cells[group]["food_num"] += weight * (after["RFOODS"] in {"2", "3"})
                    cells[group]["food_category_num"][category] += weight

    rep_num = {group: np.zeros(REPLICATES) for group in all_groups}
    rep_category_num = {group: {category: np.zeros(REPLICATES) for category in ("high_or_marginal", "low", "very_low")} for group in all_groups}
    rep_den = {group: np.zeros(REPLICATES) for group in all_groups}
    replicate_rows = matched_rows = 0
    with zipfile.ZipFile(replicate_zip) as archive, archive.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for row in reader:
            replicate_rows += 1
            base_key = tuple(row[k.lower()] for k in KEYS)
            for group in all_groups:
                item = pairs.get(base_key + (group,))
                if item is None:
                    continue
                matched_rows += 1
                if base_key + (group,) not in food_valid_keys:
                    continue
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)), dtype=np.float64, count=REPLICATES)
                rep_den[group] += weights
                if item[0][1]:
                    rep_num[group] += weights
                category = item[0][2]
                if category:
                    rep_category_num[group][category] += weights

    return {
        "format": "us-sipp-energy-assistance-food-following-v1",
        "source_unit": "identified SIPP person-month; utility/energy-assistance screen at month t to food-security status at month t+1",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for Fay-BRR",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_persons": len(people),
        "replicate_rows_read": replicate_rows,
        "matched_exposure_rows": matched_rows,
        "cells": {
            group: {
                "eligible_pairs": values["pairs"],
                "food_security_valid_pair_n": values["food_valid_n"],
                "food_insecurity": summarize(values["food_num"], values["food_den"], rep_num[group], rep_den[group], values["food_valid_n"]),
                "food_security_distribution": {
                    category: summarize(values["food_category_num"][category], values["food_den"], rep_category_num[group][category], rep_den[group], values["food_valid_n"])
                    for category in ("high_or_marginal", "low", "very_low")
                },
            }
            for group, values in cells.items()
        },
        "boundary": "Adjacent-file descriptive screen. SIPP utility and assistance fields may be reference-period or conditional household measures repeated on person-month rows; food security is not necessarily newly measured at t+1. The result does not establish a dated bill shock, assistance effect, food recovery, work/care substitution, trust, political action, or household prevalence.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.primary, args.replicate_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
