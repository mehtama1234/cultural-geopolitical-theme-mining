#!/usr/bin/env python3
"""Estimate a SIPP utility/care/tenure cross-tab for a selected outcome."""

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
REPLICATES = 240
FAY_FACTOR = 0.5


def valid(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def summary(
    numerator: float,
    denominator: float,
    replicate_numerator: np.ndarray,
    replicate_denominator: np.ndarray,
    records: int,
) -> dict:
    share = numerator / denominator if denominator else None
    replicate_shares = np.divide(
        replicate_numerator,
        replicate_denominator,
        out=np.full(REPLICATES, np.nan),
        where=replicate_denominator != 0,
    )
    standard_error = None
    if share is not None and not np.isnan(replicate_shares).any():
        standard_error = float(
            np.sqrt(
                np.sum((replicate_shares - share) ** 2)
                / (REPLICATES * FAY_FACTOR**2)
            )
        )
    return {
        "records": records,
        "weighted_denominator": denominator,
        "share_percent": 100 * share if share is not None else None,
        "standard_error_percentage_points": (
            100 * standard_error if standard_error is not None else None
        ),
        "approx_95_percent_ci": (
            [
                max(0.0, 100 * share - 1.96 * 100 * standard_error),
                min(100.0, 100 * share + 1.96 * 100 * standard_error),
            ]
            if standard_error is not None
            else None
        ),
    }


def contrast_summary(
    higher: float,
    lower: float,
    replicate_higher: np.ndarray,
    replicate_lower: np.ndarray,
) -> dict:
    """Return a percentage-point contrast with Fay-BRR variance."""
    point = 100 * (higher - lower)
    replicate_difference = 100 * (replicate_higher - replicate_lower)
    standard_error = float(
        np.sqrt(
            np.sum((replicate_difference - point) ** 2)
            / (REPLICATES * FAY_FACTOR**2)
        )
    )
    return {
        "difference_percentage_points": point,
        "standard_error_percentage_points": standard_error,
        "approx_95_percent_ci": [
            point - 1.96 * standard_error,
            point + 1.96 * standard_error,
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--outcome",
        choices=("mortgage_hardship", "food_insecurity"),
        default="mortgage_hardship",
        help="Outcome to estimate; food insecurity means low or very low RFOODS.",
    )
    args = parser.parse_args()

    groups = OrderedDict()
    records_by_key = {}
    rows_read = 0
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {
            "WPFINWGT",
            "ETENURE",
            "EAWBGAS",
            "AAWBGAS",
            "EWORKMORE",
            "AWORKMORE",
        }
        if args.outcome == "mortgage_hardship":
            required |= {"EAWBMORT", "AAWBMORT"}
        else:
            required |= {"RFOODS", "AFOODS"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            if row["MONTHCODE"] != "12":
                continue
            if not valid(row["EAWBGAS"], row["AAWBGAS"]):
                continue
            if not valid(row["EWORKMORE"], row["AWORKMORE"]):
                continue
            if not row["ETENURE"] in {"1", "2"}:
                continue
            if args.outcome == "mortgage_hardship":
                if not valid(row["EAWBMORT"], row["AAWBMORT"]):
                    continue
                positive = row["EAWBMORT"] == "1"
            else:
                if row["RFOODS"] not in {"1", "2", "3"} or row["AFOODS"] in {"", "0"}:
                    continue
                positive = row["RFOODS"] in {"2", "3"}
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            utility = "difficulty" if row["EAWBGAS"] == "1" else "no_difficulty"
            care = "prevented" if row["EWORKMORE"] == "1" else "not_prevented"
            tenure = "owner_buyer" if row["ETENURE"] == "1" else "renter"
            group = f"{utility}__{care}__{tenure}"
            groups.setdefault(group, {"numerator": 0.0, "denominator": 0.0, "records": 0})
            key = tuple(row[k] for k in KEYS)
            # The selected slice should have one December record per key. Keep
            # the first and make duplicate handling visible rather than silently
            # double-counting an identified person-month.
            if key in records_by_key:
                continue
            records_by_key[key] = (group, positive, weight)

    replicate_numerator = {group: np.zeros(REPLICATES) for group in groups}
    replicate_denominator = {group: np.zeros(REPLICATES) for group in groups}
    matched = 0
    with zipfile.ZipFile(args.replicate_zip) as archive:
        names = archive.namelist()
        if "rw2025.csv" not in names:
            raise ValueError(f"rw2025.csv missing from replicate archive: {names[:5]}")
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            required_replicates = {k.lower() for k in KEYS} | {
                f"repwgt{i}" for i in range(1, REPLICATES + 1)
            }
            missing = sorted(required_replicates - set(reader.fieldnames or []))
            if missing:
                raise ValueError("replicate file is missing fields: " + ", ".join(missing[:8]))
            for row in reader:
                key = tuple(row[k.lower()] for k in KEYS)
                item = records_by_key.get(key)
                if item is None:
                    continue
                matched += 1
                group, positive, _ = item
                weights = np.fromiter(
                    (float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                    dtype=np.float64,
                    count=REPLICATES,
                )
                replicate_denominator[group] += weights
                if positive:
                    replicate_numerator[group] += weights

    for group, positive, weight in records_by_key.values():
        groups[group]["denominator"] += weight
        groups[group]["records"] += 1
        if positive:
            groups[group]["numerator"] += weight

    result_rows = {
        group: summary(
            values["numerator"],
            values["denominator"],
            replicate_numerator[group],
            replicate_denominator[group],
            values["records"],
        )
        for group, values in groups.items()
    }
    replicate_shares = {
        group: np.divide(
            replicate_numerator[group],
            replicate_denominator[group],
            out=np.full(REPLICATES, np.nan),
            where=replicate_denominator[group] != 0,
        )
        for group in groups
    }
    contrast_pairs = {
        "difficulty__renter__prevented_minus_not_prevented": (
            "difficulty__prevented__renter",
            "difficulty__not_prevented__renter",
        ),
        "difficulty__owner_buyer__prevented_minus_not_prevented": (
            "difficulty__prevented__owner_buyer",
            "difficulty__not_prevented__owner_buyer",
        ),
        "no_difficulty__renter__prevented_minus_not_prevented": (
            "no_difficulty__prevented__renter",
            "no_difficulty__not_prevented__renter",
        ),
        "no_difficulty__owner_buyer__prevented_minus_not_prevented": (
            "no_difficulty__prevented__owner_buyer",
            "no_difficulty__not_prevented__owner_buyer",
        ),
    }
    contrasts = {
        name: contrast_summary(
            result_rows[higher]["share_percent"] / 100,
            result_rows[lower]["share_percent"] / 100,
            replicate_shares[higher],
            replicate_shares[lower],
        )
        for name, (higher, lower) in contrast_pairs.items()
    }

    output = {
        "format": f"us-sipp-utility-care-mortgage-three-way-fay-brr-v1-{args.outcome}",
        "outcome": args.outcome,
        "source_unit": "December identified person records with valid utility difficulty, annual fall child-care work-prevention status, tenure, and the selected outcome",
        "reference_period": "2024 reference year in 2025 SIPP public-use file",
        "weight": "WPFINWGT; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_records": len(records_by_key),
        "replicate_rows_matched": matched,
        "results": result_rows,
        "contrasts": contrasts,
        "causal_estimation": False,
        "boundary": "Utility difficulty and the selected outcome are December fields; EWORKMORE is an annual fall reference-parent measure. This is a descriptive same-record interaction, not a dated bill-to-care episode or causal estimate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "rows_read": rows_read,
        "identified_records": len(records_by_key),
        "replicate_rows_matched": matched,
    }, indent=2))


if __name__ == "__main__":
    main()
