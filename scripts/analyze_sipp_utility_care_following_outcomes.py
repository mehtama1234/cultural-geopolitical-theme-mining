#!/usr/bin/env python3
"""Estimate adjacent-month SIPP utility/care/outcome cross-tabs."""

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


def valid(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def summarize(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray, records: int) -> dict:
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
        "approx_95_percent_ci": ([
            max(0.0, 100 * share - 1.96 * 100 * se),
            min(100.0, 100 * share + 1.96 * 100 * se),
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
    fields = {
        "SSUID", "PNUM", "SPANEL", "SWAVE", "MONTHCODE", "WPFINWGT",
        "ETENURE", "EAWBGAS", "AAWBGAS", "EWORKMORE", "AWORKMORE",
        "EAWBMORT", "AAWBMORT", "RFOODS", "AFOODS",
    }
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        missing = sorted(fields - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            if row["MONTHCODE"] not in {"11", "12"}:
                continue
            person = tuple(row[k] for k in KEY_FIELDS)
            by_person[person][row["MONTHCODE"]] = row

    # Each selected pair is represented by the month-t key. It carries both
    # outcomes so the outcome-specific denominators stay separate below.
    pairs: dict[tuple[str, ...], tuple[str, bool, bool, float]] = {}
    group_state: OrderedDict[str, dict[str, float]] = OrderedDict()
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
        try:
            weight = float(before["WPFINWGT"])
        except (TypeError, ValueError):
            continue
        if weight <= 0:
            continue
        mortgage_valid = valid(after["EAWBMORT"], after["AAWBMORT"])
        food_valid = after["RFOODS"] in {"1", "2", "3"} and after["AFOODS"] not in {"", "0"}
        if not (mortgage_valid or food_valid):
            continue
        group = "{}__{}__{}".format(
            "difficulty" if before["EAWBGAS"] == "1" else "no_difficulty",
            "prevented" if after["EWORKMORE"] == "1" else "not_prevented",
            "owner_buyer" if before["ETENURE"] == "1" else "renter",
        )
        group_state.setdefault(group, {"mortgage_num": 0.0, "mortgage_den": 0.0,
                                       "food_num": 0.0, "food_den": 0.0, "records": 0})
        t_key = tuple(before[k] for k in MONTH_KEY)
        pairs[t_key] = (group, after["EAWBMORT"] == "1" if mortgage_valid else False,
                        after["RFOODS"] in {"2", "3"} if food_valid else False, weight)
        # Store validity separately via sentinel group keys in the tuple is
        # needlessly opaque; the outcome-valid maps below are keyed by t_key.

    mortgage_valid_keys: set[tuple[str, ...]] = set()
    food_valid_keys: set[tuple[str, ...]] = set()
    # Reconstruct validity from the person records without adding fields to
    # the compact pair tuple.
    for person, months in by_person.items():
        before, after = months.get("11"), months.get("12")
        if before is None or after is None:
            continue
        t_key = tuple(before[k] for k in MONTH_KEY)
        if t_key not in pairs:
            continue
        if valid(after["EAWBMORT"], after["AAWBMORT"]):
            mortgage_valid_keys.add(t_key)
        if after["RFOODS"] in {"1", "2", "3"} and after["AFOODS"] not in {"", "0"}:
            food_valid_keys.add(t_key)

    full = {group: {"mortgage_num": 0.0, "mortgage_den": 0.0,
                    "food_num": 0.0, "food_den": 0.0, "records": 0}
            for group in group_state}
    for key, (group, mortgage_positive, food_positive, weight) in pairs.items():
        full[group]["records"] += 1
        if key in mortgage_valid_keys:
            full[group]["mortgage_den"] += weight
            full[group]["mortgage_num"] += weight * mortgage_positive
        if key in food_valid_keys:
            full[group]["food_den"] += weight
            full[group]["food_num"] += weight * food_positive

    rep_num = {outcome: {group: np.zeros(REPLICATES) for group in full}
               for outcome in ("mortgage", "food")}
    rep_den = {outcome: {group: np.zeros(REPLICATES) for group in full}
               for outcome in ("mortgage", "food")}
    matched = 0
    matched_keys: set[tuple[str, ...]] = set()
    with zipfile.ZipFile(args.replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            for row in reader:
                key = tuple(row[k.lower()] for k in MONTH_KEY)
                item = pairs.get(key)
                if item is None:
                    continue
                matched += 1
                matched_keys.add(key)
                group, mortgage_positive, food_positive, _ = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                                      dtype=np.float64, count=REPLICATES)
                if key in mortgage_valid_keys:
                    rep_den["mortgage"][group] += weights
                    if mortgage_positive:
                        rep_num["mortgage"][group] += weights
                if key in food_valid_keys:
                    rep_den["food"][group] += weights
                    if food_positive:
                        rep_num["food"][group] += weights

    unmatched = sorted(set(pairs) - matched_keys)
    if unmatched:
        raise ValueError(
            f"{len(unmatched)} selected pair keys were absent from replicate archive; "
            f"first missing key: {unmatched[0]}"
        )

    results = {}
    for group, values in full.items():
        results[group] = {
            "mortgage_hardship": summarize(values["mortgage_num"], values["mortgage_den"],
                                             rep_num["mortgage"][group], rep_den["mortgage"][group],
                                             sum(1 for key, item in pairs.items() if item[0] == group and key in mortgage_valid_keys)),
            "food_insecurity": summarize(values["food_num"], values["food_den"],
                                           rep_num["food"][group], rep_den["food"][group],
                                           sum(1 for key, item in pairs.items() if item[0] == group and key in food_valid_keys)),
        }
    output = {
        "format": "us-sipp-utility-care-following-outcomes-fay-brr-v1",
        "source_unit": "identified November-to-December person pairs; utility difficulty and tenure at month t, child-care work prevention and outcomes at month t+1",
        "reference_period": "2024 reference year in 2025 SIPP public-use file",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 from month t for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_pairs": len(pairs),
        "replicate_pairs_matched": matched,
        "results": results,
        "causal_estimation": False,
        "boundary": "Adjacent-month ordering is descriptive. SIPP utility, food, mortgage, and annual fall child-care measures can be reference-period or repeated fields; this is not a dated bill shock, causal care effect, or household-weighted estimate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "identified_pairs": len(pairs),
                      "replicate_pairs_matched": matched}, indent=2))


if __name__ == "__main__":
    main()
