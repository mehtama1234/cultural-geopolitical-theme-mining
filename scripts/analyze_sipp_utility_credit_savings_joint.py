#!/usr/bin/env python3
"""Build a reproducible SIPP joint diagnostic for utility hardship and buffers."""

from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from collections import defaultdict
from pathlib import Path

import numpy as np


def poverty_band(value: str) -> str:
    try:
        ratio = float(value)
    except (TypeError, ValueError):
        return "unknown"
    if ratio < 1:
        return "below_1x"
    if ratio < 2:
        return "1_to_2x"
    if ratio < 4:
        return "2_to_4x"
    return "4x_or_more"


def empty() -> dict[str, float]:
    return {"weight": 0.0, "credit_valid_weight": 0.0, "credit_yes_weight": 0.0,
            "savings_valid_weight": 0.0, "savings_yes_weight": 0.0, "rows": 0}


def add(bucket: dict[str, float], row: dict[str, str], weight: float) -> None:
    bucket["weight"] += weight
    bucket["rows"] += 1
    if row.get("EDEBT_CC", "") != "":
        bucket["credit_valid_weight"] += weight
        if row["EDEBT_CC"] == "1":
            bucket["credit_yes_weight"] += weight
    if row.get("EOWN_SAV", "") != "":
        bucket["savings_valid_weight"] += weight
        if row["EOWN_SAV"] == "1":
            bucket["savings_yes_weight"] += weight


def finish(bucket: dict[str, float]) -> dict[str, float | None]:
    out = dict(bucket)
    out["credit_card_balance_share_percent"] = (
        100 * bucket["credit_yes_weight"] / bucket["credit_valid_weight"]
        if bucket["credit_valid_weight"] else None
    )
    out["savings_account_share_percent"] = (
        100 * bucket["savings_yes_weight"] / bucket["savings_valid_weight"]
        if bucket["savings_valid_weight"] else None
    )
    return out


KEYS = ("SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE")
GROUPS = ("all", "below_1x", "1_to_2x", "2_to_4x", "4x_or_more")
STATES = ("utility_difficulty", "no_utility_difficulty")


def analyze(path: Path, replicate_zip: Path | None = None) -> dict:
    cells: dict[str, dict[str, dict[str, float]]] = defaultdict(lambda: defaultdict(empty))
    primary_by_key: dict[tuple[str, ...], tuple[dict[str, str], float, str, str]] = {}
    rows_read = 0
    positive_weight_rows = 0
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"WPFINWGT", "THHLDSTATUS", "AAWBGAS", "EAWBGAS", "THINCPOV", "EDEBT_CC", "EOWN_SAV"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if weight <= 0 or row.get("THHLDSTATUS") not in {"1", "2", "3", "4"}:
                continue
            if row.get("AAWBGAS") in {"", "0"} or row.get("EAWBGAS") not in {"1", "2"}:
                continue
            positive_weight_rows += 1
            state = "utility_difficulty" if row["EAWBGAS"] == "1" else "no_utility_difficulty"
            add(cells[state]["all"], row, weight)
            band = poverty_band(row.get("THINCPOV", ""))
            if band != "unknown":
                add(cells[state][band], row, weight)
            if replicate_zip is not None:
                key = tuple(row.get(field, "") for field in KEYS)
                if key in primary_by_key:
                    raise ValueError(f"duplicate person-month key: {key}")
                primary_by_key[key] = (row, weight, state, band)
    replicate_rows_read = 0
    matched_rows = 0
    variance: dict[str, dict[str, dict[str, dict[str, np.ndarray]]]] = defaultdict(
        lambda: defaultdict(lambda: {
            "credit": {"num": np.zeros(240), "den": np.zeros(240)},
            "savings": {"num": np.zeros(240), "den": np.zeros(240)},
        })
    )
    if replicate_zip is not None:
        with zipfile.ZipFile(replicate_zip) as archive:
            if archive.namelist() != ["rw2025.csv"]:
                raise ValueError(f"unexpected replicate archive members: {archive.namelist()}")
            with archive.open("rw2025.csv") as raw:
                replicate = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
                required_rep = {field.lower() for field in KEYS} | {f"repwgt{i}" for i in range(241)}
                missing_rep = sorted(required_rep - set(replicate.fieldnames or []))
                if missing_rep:
                    raise ValueError("replicate file is missing fields: " + ", ".join(missing_rep[:8]))
                for rrow in replicate:
                    replicate_rows_read += 1
                    key = tuple(rrow[field.lower()] for field in KEYS)
                    item = primary_by_key.pop(key, None)
                    if item is None:
                        # The official replicate archive contains more panels
                        # and rows than this bounded primary slice. Ignore
                        # replicate rows outside the selected primary keys.
                        continue
                    row, weight, state, band = item
                    matched_rows += 1
                    rep_weights = np.fromiter((float(rrow[f"repwgt{i}"]) for i in range(1, 241)), dtype=float, count=240)
                    groups = ["all"] + ([band] if band != "unknown" else [])
                    for group in groups:
                        if row.get("EDEBT_CC", "") != "":
                            variance[state][group]["credit"]["den"] += rep_weights
                            if row["EDEBT_CC"] == "1":
                                variance[state][group]["credit"]["num"] += rep_weights
                        if row.get("EOWN_SAV", "") != "":
                            variance[state][group]["savings"]["den"] += rep_weights
                            if row["EOWN_SAV"] == "1":
                                variance[state][group]["savings"]["num"] += rep_weights
    if primary_by_key:
        raise ValueError(f"{len(primary_by_key)} positive-weight primary keys were absent from replicate file")

    def add_variance(state: str, group: str, outcome: str, point: float) -> dict[str, float | None]:
        if replicate_zip is None:
            return {"standard_error_percentage_points": None, "approx_95_ci_percentage_points": None}
        vals = variance[state][group][outcome]
        estimates = np.divide(vals["num"], vals["den"], out=np.full(240, np.nan), where=vals["den"] != 0)
        if np.isnan(estimates).any():
            return {"standard_error_percentage_points": None, "approx_95_ci_percentage_points": None}
        se = float(np.sqrt(np.sum((estimates - point / 100) ** 2) / (240 * 0.5 ** 2)) * 100)
        return {"standard_error_percentage_points": se, "approx_95_ci_percentage_points": [max(0, point - 1.96 * se), min(100, point + 1.96 * se)]}

    result_cells = {state: {group: finish(bucket) for group, bucket in groups.items()} for state, groups in cells.items()}
    for state, groups in result_cells.items():
        for group, result in groups.items():
            result.update({"credit_card_balance_variance": add_variance(state, group, "credit", result["credit_card_balance_share_percent"]),
                           "savings_account_variance": add_variance(state, group, "savings", result["savings_account_share_percent"])})
    return {
        "format": "us-sipp-utility-credit-savings-joint-v1",
        "source_unit": "SIPP person record by reference month; household fields repeated on person records",
        "weight": "WPFINWGT final person weight",
        "rows_read": rows_read,
        "positive_weight_rows_in_joint_universe": positive_weight_rows,
        "variance_estimation": replicate_zip is not None,
        "variance_method": "Fay BRR, 240 replicate weights, G=240, perturbation factor 0.5" if replicate_zip is not None else None,
        "official_utility_universe": "THHLDSTATUS valid and AAWBGAS valid; EAWBGAS code 1 versus 2",
        "replicate_rows_read": replicate_rows_read,
        "positive_weight_rows_matched": matched_rows,
        "cells": result_cells,
        "boundary": "Joint person-weighted descriptive diagnostic; utility hardship is the conditioning outcome, while credit-card and savings fields have their own nonblank universes. Household fields are not household-weighted and no causal ordering is identified."
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.input, args.replicate_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
