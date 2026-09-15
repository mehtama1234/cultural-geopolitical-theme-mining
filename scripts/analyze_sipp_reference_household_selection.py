#!/usr/bin/env python3
"""Compare SIPP person-record and one-reference-person household-context scans.

The 2025 SIPP public-use slice repeats household fields on person records but
only supplies WPFINWGT in the extracted surface.  This diagnostic therefore
does not manufacture a household weight.  It reports the ordinary
person-record estimate beside a deterministic one-record-per-household-month
selection, using the selected person's weight and Fay-BRR replicate weights
only as a sensitivity diagnostic.
"""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from pathlib import Path

import numpy as np


KEYS = ("SSUID", "SHHADID", "SPANEL", "SWAVE", "MONTHCODE")
REPLICATE_KEYS = ("SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE")
OUTCOMES = {
    "EAWBMORT": ("AAWBMORT", "unable to pay rent or mortgage"),
    "EAWBGAS": ("AAWBGAS", "unable to pay utility bills"),
    "RFOODS": ("AFOODS", "high or marginal food security"),
}


def valid(row: dict[str, str], field: str) -> bool:
    value = row.get(field, "")
    if value == "":
        return False
    flag, _ = OUTCOMES[field]
    return row.get(flag, "") not in {"", "0"}


def selected_better(candidate: dict[str, str], current: dict[str, str]) -> bool:
    """Prefer the reference person, then the lowest numeric PNUM."""
    candidate_ref = candidate.get("ERP") == "1"
    current_ref = current.get("ERP") == "1"
    if candidate_ref != current_ref:
        return candidate_ref
    try:
        return int(candidate.get("PNUM", "999999")) < int(current.get("PNUM", "999999"))
    except ValueError:
        return candidate.get("PNUM", "") < current.get("PNUM", "")


def ratio(num: float, den: float) -> float | None:
    return num / den if den else None


def new_acc() -> dict:
    return {
        field: {
            "num": 0.0,
            "den": 0.0,
            "valid_rows": 0,
            "rep_num": np.zeros(240),
            "rep_den": np.zeros(240),
        }
        for field in OUTCOMES
    }


def add_full(acc: dict, row: dict[str, str], weight: float, reps: np.ndarray | None) -> None:
    for field in OUTCOMES:
        if not valid(row, field):
            continue
        cell = acc[field]
        cell["valid_rows"] += 1
        cell["den"] += weight
        if reps is not None:
            cell["rep_den"] += reps
        if row[field] == "1":
            cell["num"] += weight
            if reps is not None:
                cell["rep_num"] += reps


def summarize(acc: dict) -> dict:
    result = {}
    for field, (_, label) in OUTCOMES.items():
        cell = acc[field]
        estimate = ratio(cell["num"], cell["den"])
        rep_est = np.divide(cell["rep_num"], cell["rep_den"],
                            out=np.full(240, np.nan), where=cell["rep_den"] != 0)
        if estimate is not None and not np.isnan(rep_est).any():
            se = float(np.sqrt(np.sum((rep_est - estimate) ** 2) / (240 * 0.5 ** 2)))
        else:
            se = None
        result[field] = {
            "label": label,
            "valid_rows": cell["valid_rows"],
            "weighted_denominator": cell["den"],
            "estimate_percent": 100 * estimate if estimate is not None else None,
            "fay_brr_se_percentage_points": 100 * se if se is not None else None,
            "approx_95_ci": ([max(0.0, 100 * estimate - 1.96 * 100 * se),
                               min(100.0, 100 * estimate + 1.96 * 100 * se)]
                              if estimate is not None and se is not None else None),
        }
    return result


def analyze(primary: Path, replicate_zip: Path) -> dict:
    required = set(KEYS) | {"PNUM", "ERP", "WPFINWGT"}
    required |= {field for field in OUTCOMES}
    required |= {flag for flag, _ in OUTCOMES.values()}
    all_acc = new_acc()
    selected: dict[tuple[str, ...], dict[str, str]] = {}
    rows_read = 0
    positive_rows = 0
    with primary.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if weight <= 0:
                continue
            positive_rows += 1
            add_full(all_acc, row, weight, None)
            key = tuple(row[key] for key in KEYS)
            if key not in selected or selected_better(row, selected[key]):
                selected[key] = row

    selected_replicate_keys: dict[tuple[str, ...], dict[str, str]] = {}
    for row in selected.values():
        replicate_key = (row["SSUID"], row["PNUM"], row["SPANEL"],
                         row["SWAVE"], row["MONTHCODE"])
        if replicate_key in selected_replicate_keys:
            raise ValueError("selected household rule produced duplicate replicate key: "
                             + repr(replicate_key))
        selected_replicate_keys[replicate_key] = row
    household_acc = new_acc()
    replicate_rows = 0
    matched_selected = 0
    with zipfile.ZipFile(replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader((line.decode("utf-8") for line in raw), delimiter="|")
            for rrow in reader:
                replicate_rows += 1
                key = tuple(rrow[key.lower()] for key in REPLICATE_KEYS)
                if key not in selected_replicate_keys:
                    continue
                row = selected_replicate_keys[key]
                try:
                    weight = float(row["WPFINWGT"])
                    reps = np.array([float(rrow[f"repwgt{i}"]) for i in range(1, 241)])
                except (TypeError, ValueError):
                    continue
                if weight <= 0:
                    continue
                matched_selected += 1
                add_full(household_acc, row, weight, reps)

    person_summary = summarize(all_acc)
    selected_summary = summarize(household_acc)
    comparison = {}
    for field in OUTCOMES:
        p = person_summary[field]["estimate_percent"]
        h = selected_summary[field]["estimate_percent"]
        comparison[field] = {
            "person_record_percent": p,
            "reference_person_selected_percent": h,
            "difference_percentage_points": h - p if p is not None and h is not None else None,
        }
    return {
        "format": "us-sipp-reference-person-household-selection-diagnostic-v1",
        "reference_period": "2024 reference year in the 2025 SIPP public-use file",
        "primary_unit": "person record by household-month",
        "selection_unit": "one selected person per SSUID/SHHADID/SPANEL/SWAVE/MONTHCODE; ERP=1 preferred, then lowest PNUM",
        "replicate_join_unit": "SSUID/PNUM/SPANEL/SWAVE/MONTHCODE; SHHADID is absent from rw2025.csv and is not used in the replicate join",
        "weight": "WPFINWGT for both views; no official household weight was used",
        "variance_method": "Fay BRR, 240 replicates, perturbation factor 0.5; selected view is a sensitivity diagnostic, not an official household estimator",
        "rows_read": rows_read,
        "positive_person_rows": positive_rows,
        "selected_household_months": len(selected),
        "replicate_rows_read": replicate_rows,
        "selected_rows_matched_to_replicates": matched_selected,
        "person_record_view": person_summary,
        "reference_person_selected_view": selected_summary,
        "comparison": comparison,
        "interpretation_boundary": "The selected view makes household selection explicit and prevents household fields from being counted once per person, but reusing a person weight does not create a household-prevalence estimate. Differences are selection sensitivity, not evidence of a household trend or causal effect.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
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
