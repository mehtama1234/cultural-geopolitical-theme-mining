#!/usr/bin/env python3
"""Estimate a bounded SIPP monthly-assistance to next-month work screen.

This is a person-weighted descriptive cross-lag, not a causal housing or
recovery estimate.  The exposure is the genuinely monthly `EOTHAS_MNYN`
variable (other clothing or housing assistance), not the annual/reference-
period housing-assistance fields.  Each outcome keeps its own valid-pair
denominator and uses the first month's person weight.
"""

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
EXPOSURE_LABELS = {"1": "yes", "2": "no"}


def poverty_band(value: str) -> str | None:
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


def job_count(value: str) -> int | None:
    try:
        number = int(float(value))
    except (TypeError, ValueError):
        return None
    return number if number >= 0 else None


def tenure_group(value: str) -> str | None:
    return {
        "1": "owner_or_buyer",
        "2": "renter",
        "3": "no_rent",
    }.get(value)


def stratum(row: dict[str, str]) -> str | None:
    tenure = tenure_group(row.get("ETENURE", ""))
    resources = poverty_band(row.get("THINCPOV", ""))
    return f"{tenure}|{resources}" if tenure and resources else None


def empty_cell() -> dict[str, float]:
    return {"pairs": 0, "den": 0.0, "num": 0.0}


def summarize(cell: dict[str, float], rep_num: np.ndarray,
              rep_den: np.ndarray) -> dict[str, object]:
    point = 100.0 * cell["num"] / cell["den"] if cell["den"] else None
    if point is None:
        se = None
    else:
        estimates = np.divide(
            rep_num,
            rep_den,
            out=np.full(REPLICATES, np.nan),
            where=rep_den != 0,
        )
        se = float(np.sqrt(np.nansum((estimates - point / 100.0) ** 2) /
                           (REPLICATES * FAY_FACTOR ** 2)) * 100.0)
    return {
        **cell,
        "share_percent": point,
        "standard_error_percentage_points": se,
        "approx_95_ci_percentage_points": (
            [max(0.0, point - 1.96 * se), min(100.0, point + 1.96 * se)]
            if point is not None and se is not None else None
        ),
    }


def analyze(primary_path: Path, replicate_path: Path) -> dict[str, object]:
    people: dict[tuple[str, ...], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary_path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS[:-1]) | {
            "MONTHCODE", "EOTHAS_MNYN", "RMNUMJOBS", "THINCPOV",
            "EAWBMORT", "ETENURE", "WPFINWGT",
        }
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
                people[person][month] = row

    outcomes = ("job_count_changed", "poverty_band_changed", "housing_difficulty")
    cells = {outcome: {exposure: empty_cell() for exposure in ("yes", "no")}
             for outcome in outcomes}
    stratified_cells: dict[str, dict[str, dict[str, dict[str, float]]]] = defaultdict(
        lambda: {outcome: {exposure: empty_cell() for exposure in ("yes", "no")}
                 for outcome in outcomes}
    )
    pair_info: dict[tuple[str, ...], list[tuple[str, str, bool, str | None]]] = {}
    valid_pairs = {outcome: {exposure: 0 for exposure in ("yes", "no")}
                   for outcome in outcomes}

    for person, records in people.items():
        for month in range(1, 12):
            first, second = records.get(month), records.get(month + 1)
            if not first or not second:
                continue
            exposure = EXPOSURE_LABELS.get(first.get("EOTHAS_MNYN", ""))
            if not exposure:
                continue
            pair_stratum = stratum(first)
            pair_key = person + (str(month),)
            pair_outcomes: list[tuple[str, str, bool, str | None]] = []
            first_jobs, second_jobs = job_count(first.get("RMNUMJOBS", "")), job_count(second.get("RMNUMJOBS", ""))
            if first_jobs is not None and second_jobs is not None:
                changed = first_jobs != second_jobs
                cell = cells["job_count_changed"][exposure]
                cell["pairs"] += 1
                cell["den"] += float(first["WPFINWGT"])
                cell["num"] += float(first["WPFINWGT"]) * changed
                valid_pairs["job_count_changed"][exposure] += 1
                if pair_stratum:
                    stratified_cells[pair_stratum]["job_count_changed"][exposure]["pairs"] += 1
                    stratified_cells[pair_stratum]["job_count_changed"][exposure]["den"] += float(first["WPFINWGT"])
                    stratified_cells[pair_stratum]["job_count_changed"][exposure]["num"] += float(first["WPFINWGT"]) * changed
                pair_outcomes.append(("job_count_changed", exposure, changed, pair_stratum))
            first_band, second_band = poverty_band(first.get("THINCPOV", "")), poverty_band(second.get("THINCPOV", ""))
            if first_band is not None and second_band is not None:
                changed = first_band != second_band
                cell = cells["poverty_band_changed"][exposure]
                cell["pairs"] += 1
                cell["den"] += float(first["WPFINWGT"])
                cell["num"] += float(first["WPFINWGT"]) * changed
                valid_pairs["poverty_band_changed"][exposure] += 1
                if pair_stratum:
                    stratified_cells[pair_stratum]["poverty_band_changed"][exposure]["pairs"] += 1
                    stratified_cells[pair_stratum]["poverty_band_changed"][exposure]["den"] += float(first["WPFINWGT"])
                    stratified_cells[pair_stratum]["poverty_band_changed"][exposure]["num"] += float(first["WPFINWGT"]) * changed
                pair_outcomes.append(("poverty_band_changed", exposure, changed, pair_stratum))
            difficulty = second.get("EAWBMORT", "")
            if difficulty in {"1", "2"}:
                changed = difficulty == "1"
                cell = cells["housing_difficulty"][exposure]
                cell["pairs"] += 1
                cell["den"] += float(first["WPFINWGT"])
                cell["num"] += float(first["WPFINWGT"]) * changed
                valid_pairs["housing_difficulty"][exposure] += 1
                if pair_stratum:
                    stratified_cells[pair_stratum]["housing_difficulty"][exposure]["pairs"] += 1
                    stratified_cells[pair_stratum]["housing_difficulty"][exposure]["den"] += float(first["WPFINWGT"])
                    stratified_cells[pair_stratum]["housing_difficulty"][exposure]["num"] += float(first["WPFINWGT"]) * changed
                pair_outcomes.append(("housing_difficulty", exposure, changed, pair_stratum))
            if pair_outcomes:
                pair_info[pair_key] = pair_outcomes

    rep_num = {outcome: {exposure: np.zeros(REPLICATES) for exposure in ("yes", "no")}
               for outcome in outcomes}
    rep_den = {outcome: {exposure: np.zeros(REPLICATES) for exposure in ("yes", "no")}
               for outcome in outcomes}
    stratified_rep_num = defaultdict(lambda: {
        outcome: {exposure: np.zeros(REPLICATES) for exposure in ("yes", "no")}
        for outcome in outcomes
    })
    stratified_rep_den = defaultdict(lambda: {
        outcome: {exposure: np.zeros(REPLICATES) for exposure in ("yes", "no")}
        for outcome in outcomes
    })
    replicate_rows_read = matched_rows = 0
    with zipfile.ZipFile(replicate_path) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            for row in reader:
                replicate_rows_read += 1
                key = tuple(row[field.lower()] for field in KEYS)
                pair_outcomes = pair_info.get(key)
                if not pair_outcomes:
                    continue
                matched_rows += 1
                weights = np.fromiter(
                    (float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                    dtype=float,
                    count=REPLICATES,
                )
                for outcome, exposure, changed, pair_stratum in pair_outcomes:
                    rep_den[outcome][exposure] += weights
                    if changed:
                        rep_num[outcome][exposure] += weights
                    if pair_stratum:
                        stratified_rep_den[pair_stratum][outcome][exposure] += weights
                        if changed:
                            stratified_rep_num[pair_stratum][outcome][exposure] += weights

    result_cells = {
        outcome: {
            exposure: summarize(cells[outcome][exposure], rep_num[outcome][exposure], rep_den[outcome][exposure])
            for exposure in ("yes", "no")
        }
        for outcome in outcomes
    }
    result_stratified_cells = {
        label: {
            outcome: {
                exposure: summarize(
                    stratified_cells[label][outcome][exposure],
                    stratified_rep_num[label][outcome][exposure],
                    stratified_rep_den[label][outcome][exposure],
                )
                for exposure in ("yes", "no")
            }
            for outcome in outcomes
        }
        for label in sorted(stratified_cells)
    }
    return {
        "schema": "us-sipp-housing-assistance-work-screen-v1",
        "source_unit": "identified SIPP person, adjacent monthly pair, exposure at month t and outcomes at month t+1",
        "exposure": "EOTHAS_MNYN: other clothing or housing assistance received this month; 1=yes, 2=no",
        "weight": "WPFINWGT from month t",
        "variance_method": "240 Census Fay-BRR replicate weights; G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_people": len(people),
        "replicate_rows_read": replicate_rows_read,
        "matched_pair_rows": matched_rows,
        "valid_pair_counts": valid_pairs,
        "cells": result_cells,
        "stratification": "ETENURE at month t crossed with THINCPOV band at month t",
        "stratified_cells": result_stratified_cells,
        "household_weight_used": False,
        "boundary": "Descriptive person-weighted cross-lag only. Other clothing or housing assistance is not HUD program identity, amount, adequacy, or a dated housing exit. The screen does not establish causality, recovery, institutional response, trust, or political action.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = analyze(args.primary, args.replicate_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
