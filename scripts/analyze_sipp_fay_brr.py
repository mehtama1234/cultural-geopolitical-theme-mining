#!/usr/bin/env python3
"""Estimate person-weighted SIPP proportions with Fay BRR replicate weights.

The primary slice and replicate-weight CSV are joined in their documented
person-month order and checked by SSUID/PNUM/SPANEL/SWAVE/MONTHCODE. Results
are code-1 shares among nonblank selected records; official universes still
need to be applied by the caller.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from pathlib import Path

import numpy as np


LABELS = {
    "EAWBMORT": "unable to pay rent or mortgage",
    "EAWBGAS": "unable to pay utility bills",
    "RFOODS": "high or marginal food security",
    "EFOOD6": "hungry but did not eat because of money",
    "RMNUMJOBS": "one job",
}
GROUP_LABELS = {
    "ERACE": {"1": "White alone", "2": "Black alone", "3": "Asian alone", "4": "Residual"},
    "ETENURE": {"1": "owned or being bought", "2": "rented",
                 "3": "occupied without payment of rent"},
    "TEHC_REGION": {"1": "Northeast", "2": "Midwest", "3": "South", "4": "West"},
    "THINCPOV": {"below_1x": "below 1.00x poverty threshold",
                 "1_to_2x": "1.00–1.99x poverty threshold",
                 "2_to_4x": "2.00–3.99x poverty threshold",
                 "4x_or_more": "4.00x poverty threshold or more"},
}
GROUP_FIELDS = {
    "ERACE": ("ERACE",),
    "ETENURE": ("ETENURE",),
    "TEHC_REGION": ("TEHC_REGION",),
    "THINCPOV": ("THINCPOV",),
    "ETENURE_THINCPOV": ("ETENURE", "THINCPOV"),
    "ERACE_THINCPOV": ("ERACE", "THINCPOV"),
}
KEYS = ("SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE")


def estimate(numerator: float, denominator: float) -> float | None:
    return numerator / denominator if denominator else None


def normalized_group(field: str, value: str) -> str:
    if field != "THINCPOV":
        return value
    try:
        ratio = float(value)
    except (TypeError, ValueError):
        return ""
    if ratio < 1:
        return "below_1x"
    if ratio < 2:
        return "1_to_2x"
    if ratio < 4:
        return "2_to_4x"
    return "4x_or_more"


def group_key(group_by: str | None, row: dict[str, str]) -> str:
    if not group_by:
        return ""
    values = [normalized_group(field, row.get(field, ""))
              for field in GROUP_FIELDS[group_by]]
    return "|".join(values) if all(values) else ""


def new_accumulators(fields: list[str]) -> dict:
    return {"full_num": {field: 0.0 for field in fields},
            "full_den": {field: 0.0 for field in fields},
            "rep_num": {field: np.zeros(240, dtype=np.float64) for field in fields},
            "rep_den": {field: np.zeros(240, dtype=np.float64) for field in fields}}


def summarize(acc: dict, fields: list[str]) -> dict:
    results = {}
    for field in fields:
        theta0 = estimate(acc["full_num"][field], acc["full_den"][field])
        replicate_estimates = np.divide(acc["rep_num"][field], acc["rep_den"][field],
                                        out=np.full(240, np.nan), where=acc["rep_den"][field] != 0)
        valid = ~np.isnan(replicate_estimates)
        if theta0 is None or not valid.all():
            standard_error = None
        else:
            variance = float(np.sum((replicate_estimates - theta0) ** 2) / (240 * 0.5 ** 2))
            standard_error = float(np.sqrt(variance))
        results[field] = {
            "code1_label": LABELS[field],
            "numerator_weight": acc["full_num"][field],
            "nonblank_denominator_weight": acc["full_den"][field],
            "estimate_percent": 100 * theta0 if theta0 is not None else None,
            "standard_error_percentage_points": 100 * standard_error if standard_error is not None else None,
            "approx_95_percent_ci": ([max(0.0, 100 * theta0 - 1.96 * 100 * standard_error),
                                       min(100.0, 100 * theta0 + 1.96 * 100 * standard_error)]
                                      if theta0 is not None and standard_error is not None else None),
        }
    return results


def analyze(primary_path: Path, replicate_zip: Path, fields: list[str], group_by: str | None = None) -> dict:
    overall = new_accumulators(fields)
    grouped = {}
    full_num = {field: 0.0 for field in fields}
    full_den = {field: 0.0 for field in fields}
    rep_num = {field: np.zeros(240, dtype=np.float64) for field in fields}
    rep_den = {field: np.zeros(240, dtype=np.float64) for field in fields}
    rows_read = 0
    replicate_rows_read = 0
    matched_rows = 0
    with primary_path.open(encoding="utf-8", newline="") as primary_file:
        primary = csv.DictReader(primary_file)
        required = {"WPFINWGT", *KEYS, *fields}
        if group_by:
            required.update(GROUP_FIELDS[group_by])
        missing = sorted(required - set(primary.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        primary_by_key = {}
        for prow in primary:
            rows_read += 1
            pkey = tuple(prow[key] for key in KEYS)
            if pkey in primary_by_key:
                raise ValueError(f"duplicate person-month key in primary slice: {pkey}")
            group = group_key(group_by, prow) if group_by else None
            primary_by_key[pkey] = (prow.get("WPFINWGT", ""),
                                    {field: prow.get(field, "") for field in fields}, group)

    with zipfile.ZipFile(replicate_zip) as archive:
            names = archive.namelist()
            if names != ["rw2025.csv"]:
                raise ValueError(f"unexpected replicate archive members: {names}")
            with archive.open("rw2025.csv") as raw:
                replicate = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
                rep_fields = set(replicate.fieldnames or [])
                required_rep = {key.lower() for key in KEYS} | {f"repwgt{i}" for i in range(241)}
                missing_rep = sorted(required_rep - rep_fields)
                if missing_rep:
                    raise ValueError("replicate file is missing fields: " + ", ".join(missing_rep[:8]))
                for rrow in replicate:
                    replicate_rows_read += 1
                    rkey = tuple(rrow[key.lower()] for key in KEYS)
                    primary_item = primary_by_key.pop(rkey, None)
                    if primary_item is None:
                        raise ValueError(f"replicate person-month key not found in primary slice: {rkey}")
                    primary_weight_text, primary_values, group = primary_item
                    try:
                        primary_weight = float(primary_weight_text)
                    except (TypeError, ValueError):
                        continue
                    if primary_weight <= 0:
                        continue
                    matched_rows += 1
                    rep_weights = np.fromiter((float(rrow[f"repwgt{i}"]) for i in range(1, 241)),
                                              dtype=np.float64, count=240)
                    accumulators = [overall]
                    if group_by and group:
                        grouped.setdefault(group, new_accumulators(fields))
                        accumulators.append(grouped[group])
                    for field in fields:
                        if not primary_values[field]:
                            continue
                        for acc in accumulators:
                            acc["full_den"][field] += primary_weight
                            acc["rep_den"][field] += rep_weights
                            if primary_values[field] == "1":
                                acc["full_num"][field] += primary_weight
                                acc["rep_num"][field] += rep_weights
    return {
        "format": "us-sipp-fay-brr-person-proportions-v1",
        "source_unit": "person record by reference month",
        "weight": "WPFINWGT / REPWGT1-REPWGT240",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "positive_weight_rows_matched": matched_rows,
        "fields": fields,
        "group_by": group_by,
        "group_value_labels": ({field: GROUP_LABELS[field] for field in GROUP_FIELDS[group_by]}
                               if group_by else {}),
        "results": summarize(overall, fields),
        "by_group": {group: summarize(acc, fields) for group, acc in sorted(grouped.items())},
        "household_weight_used": False,
        "official_universes_constructed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fields", nargs="+", choices=sorted(LABELS), default=list(LABELS))
    parser.add_argument("--group-by", choices=sorted(GROUP_FIELDS), default=None)
    args = parser.parse_args()
    result = analyze(args.primary, args.replicate_zip, args.fields, args.group_by)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
