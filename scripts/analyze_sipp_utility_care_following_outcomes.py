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


def poverty_band(value: str) -> int | None:
    try:
        ratio = float(value)
    except (TypeError, ValueError):
        return None
    if ratio < 1:
        return 0
    if ratio < 2:
        return 1
    if ratio < 4:
        return 2
    return 3


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


def contrast_summary(higher: float, lower: float,
                     replicate_higher: np.ndarray,
                     replicate_lower: np.ndarray) -> dict:
    point = 100 * (higher - lower)
    difference = 100 * (replicate_higher - replicate_lower)
    se = float(np.sqrt(np.sum((difference - point) ** 2) /
                       (REPLICATES * FAY_FACTOR**2)))
    return {
        "difference_percentage_points": point,
        "standard_error_percentage_points": se,
        "approx_95_percent_ci": [point - 1.96 * se, point + 1.96 * se],
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
        "EAWBMORT", "AAWBMORT", "RFOODS", "AFOODS", "THINCPOV",
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
        before_band = poverty_band(before["THINCPOV"])
        after_band = poverty_band(after["THINCPOV"])
        resource_valid = before_band is not None and after_band is not None
        if not (mortgage_valid or food_valid or resource_valid):
            continue
        group = "{}__{}__{}".format(
            "difficulty" if before["EAWBGAS"] == "1" else "no_difficulty",
            "prevented" if after["EWORKMORE"] == "1" else "not_prevented",
            "owner_buyer" if before["ETENURE"] == "1" else "renter",
        )
        group_state.setdefault(group, {"mortgage_num": 0.0, "mortgage_den": 0.0,
                                       "food_num": 0.0, "food_den": 0.0, "records": 0})
        t_key = tuple(before[k] for k in MONTH_KEY)
        pairs[t_key] = (
            group,
            after["EAWBMORT"] == "1" if mortgage_valid else False,
            after["RFOODS"] in {"2", "3"} if food_valid else False,
            before_band != after_band if resource_valid else False,
            after_band > before_band if resource_valid else False,
            after_band < before_band if resource_valid else False,
            weight,
        )
        # Store validity separately via sentinel group keys in the tuple is
        # needlessly opaque; the outcome-valid maps below are keyed by t_key.

    mortgage_valid_keys: set[tuple[str, ...]] = set()
    food_valid_keys: set[tuple[str, ...]] = set()
    resource_valid_keys: set[tuple[str, ...]] = set()
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
        if poverty_band(before["THINCPOV"]) is not None and poverty_band(after["THINCPOV"]) is not None:
            resource_valid_keys.add(t_key)

    full = {group: {"mortgage_num": 0.0, "mortgage_den": 0.0,
                    "food_num": 0.0, "food_den": 0.0,
                    "resource_changed_num": 0.0, "resource_changed_den": 0.0,
                    "resource_improved_num": 0.0, "resource_improved_den": 0.0,
                    "resource_worsened_num": 0.0, "resource_worsened_den": 0.0,
                    "records": 0}
            for group in group_state}
    for key, (group, mortgage_positive, food_positive, resource_changed,
              resource_improved, resource_worsened, weight) in pairs.items():
        full[group]["records"] += 1
        if key in mortgage_valid_keys:
            full[group]["mortgage_den"] += weight
            full[group]["mortgage_num"] += weight * mortgage_positive
        if key in food_valid_keys:
            full[group]["food_den"] += weight
            full[group]["food_num"] += weight * food_positive
        if key in resource_valid_keys:
            full[group]["resource_changed_den"] += weight
            full[group]["resource_changed_num"] += weight * resource_changed
            full[group]["resource_improved_den"] += weight
            full[group]["resource_improved_num"] += weight * resource_improved
            full[group]["resource_worsened_den"] += weight
            full[group]["resource_worsened_num"] += weight * resource_worsened

    rep_num = {outcome: {group: np.zeros(REPLICATES) for group in full}
               for outcome in ("mortgage", "food", "resource_changed",
                               "resource_improved", "resource_worsened")}
    rep_den = {outcome: {group: np.zeros(REPLICATES) for group in full}
               for outcome in ("mortgage", "food", "resource_changed",
                               "resource_improved", "resource_worsened")}
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
                (group, mortgage_positive, food_positive, resource_changed,
                 resource_improved, resource_worsened, _) = item
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
                if key in resource_valid_keys:
                    rep_den["resource_changed"][group] += weights
                    rep_den["resource_improved"][group] += weights
                    rep_den["resource_worsened"][group] += weights
                    if resource_changed:
                        rep_num["resource_changed"][group] += weights
                    if resource_improved:
                        rep_num["resource_improved"][group] += weights
                    if resource_worsened:
                        rep_num["resource_worsened"][group] += weights

    unmatched = sorted(set(pairs) - matched_keys)
    if unmatched:
        raise ValueError(
            f"{len(unmatched)} selected pair keys were absent from replicate archive; "
            f"first missing key: {unmatched[0]}"
        )

    results = {}
    for group, values in full.items():
        resource_records = sum(1 for key, item in pairs.items()
                               if item[0] == group and key in resource_valid_keys)
        results[group] = {
            "mortgage_hardship": summarize(values["mortgage_num"], values["mortgage_den"],
                                             rep_num["mortgage"][group], rep_den["mortgage"][group],
                                             sum(1 for key, item in pairs.items() if item[0] == group and key in mortgage_valid_keys)),
            "food_insecurity": summarize(values["food_num"], values["food_den"],
                                           rep_num["food"][group], rep_den["food"][group],
                                           sum(1 for key, item in pairs.items() if item[0] == group and key in food_valid_keys)),
            "resource_band_changed": summarize(values["resource_changed_num"], values["resource_changed_den"],
                                                rep_num["resource_changed"][group], rep_den["resource_changed"][group], resource_records),
            "resource_band_improved": summarize(values["resource_improved_num"], values["resource_improved_den"],
                                                 rep_num["resource_improved"][group], rep_den["resource_improved"][group], resource_records),
            "resource_band_worsened": summarize(values["resource_worsened_num"], values["resource_worsened_den"],
                                                 rep_num["resource_worsened"][group], rep_den["resource_worsened"][group], resource_records),
        }
    contrast_pairs = {
        "difficulty__renter__prevented_minus_not_prevented": (
            "difficulty__prevented__renter", "difficulty__not_prevented__renter"),
        "difficulty__owner_buyer__prevented_minus_not_prevented": (
            "difficulty__prevented__owner_buyer", "difficulty__not_prevented__owner_buyer"),
        "no_difficulty__renter__prevented_minus_not_prevented": (
            "no_difficulty__prevented__renter", "no_difficulty__not_prevented__renter"),
        "no_difficulty__owner_buyer__prevented_minus_not_prevented": (
            "no_difficulty__prevented__owner_buyer", "no_difficulty__not_prevented__owner_buyer"),
    }
    contrasts = {}
    for name, (higher, lower) in contrast_pairs.items():
        contrasts[name] = {}
        for outcome, rep_name in (("mortgage_hardship", "mortgage"),
                                  ("food_insecurity", "food")):
            high_share = results[higher][outcome]["share_percent"] / 100
            low_share = results[lower][outcome]["share_percent"] / 100
            high_rep = np.divide(rep_num[rep_name][higher], rep_den[rep_name][higher],
                                 out=np.full(REPLICATES, np.nan),
                                 where=rep_den[rep_name][higher] != 0)
            low_rep = np.divide(rep_num[rep_name][lower], rep_den[rep_name][lower],
                                out=np.full(REPLICATES, np.nan),
                                where=rep_den[rep_name][lower] != 0)
            if np.isnan(high_rep).any() or np.isnan(low_rep).any():
                raise ValueError(f"incomplete replicate contrast for {name}/{outcome}")
            contrasts[name][outcome] = contrast_summary(high_share, low_share,
                                                        high_rep, low_rep)
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
        "contrasts": contrasts,
        "causal_estimation": False,
        "boundary": "Adjacent-month ordering is descriptive. SIPP utility, food, mortgage, resource-band, and annual fall child-care measures can be reference-period or repeated fields; resource-band movement is not income recovery. This is not a dated bill shock, causal care effect, or household-weighted estimate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "identified_pairs": len(pairs),
                      "replicate_pairs_matched": matched}, indent=2))


if __name__ == "__main__":
    main()
