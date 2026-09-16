#!/usr/bin/env python3
"""Estimate a bounded same-person SIPP constraint-cascade screen."""

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


def number(value: str) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if parsed >= 0 else None


def valid(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def band(value: str) -> int | None:
    parsed = number(value)
    if parsed is None:
        return None
    if parsed < 1:
        return 0
    if parsed < 2:
        return 1
    if parsed < 4:
        return 2
    return 3


def estimate(numerator: float, denominator: float,
             rep_numerator: np.ndarray, rep_denominator: np.ndarray) -> dict[str, object]:
    if denominator <= 0:
        return {"share_percent": None, "standard_error_percentage_points": None,
                "approx_95_ci_percentage_points": None}
    share = numerator / denominator
    rep_share = np.divide(rep_numerator, rep_denominator,
                          out=np.full(REPLICATES, np.nan),
                          where=rep_denominator != 0)
    if np.isnan(rep_share).any():
        return {"share_percent": 100 * share,
                "standard_error_percentage_points": None,
                "approx_95_ci_percentage_points": None}
    se = float(np.sqrt(np.sum((rep_share - share) ** 2) /
                       (REPLICATES * FAY ** 2)) * 100)
    point = 100 * share
    return {
        "share_percent": point,
        "standard_error_percentage_points": se,
        "approx_95_ci_percentage_points": [
            max(0.0, point - 1.96 * se), min(100.0, point + 1.96 * se)
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = {
        *KEYS, "WPFINWGT", "AAWBGAS", "EAWBGAS", "ETENURE", "EWORKMORE",
        "AWORKMORE", "TPEARN", "TMWKHRS", "EAWBMORT", "AAWBMORT",
        "RFOODS", "AFOODS", "THINCPOV",
    }
    people: dict[tuple[str, ...], dict[str, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice missing: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            if row.get("MONTHCODE") not in {"11", "12"}:
                continue
            key = tuple(row[k] for k in KEYS[:-1])
            people[key][row["MONTHCODE"]] = row

    outcomes = ("earnings_changed", "hours_changed", "mortgage_hardship",
                "food_insecurity", "resource_band_changed")
    groups = tuple(
        f"{utility}__{tenure}__{care}"
        for utility in ("difficulty", "no_difficulty")
        for tenure in ("owner_buyer", "renter")
        for care in ("care_prevented", "care_not_prevented")
    )
    cells = {group: {"pairs": 0, **{
        outcome: {"records": 0, "numerator": 0.0, "denominator": 0.0}
        for outcome in outcomes
    }} for group in groups}
    pairs: dict[tuple[str, ...], tuple[str, dict[str, bool], float]] = {}

    for person, months in people.items():
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
        utility = "difficulty" if before["EAWBGAS"] == "1" else "no_difficulty"
        tenure = "owner_buyer" if before["ETENURE"] == "1" else "renter"
        care = "care_prevented" if after["EWORKMORE"] == "1" else "care_not_prevented"
        group = f"{utility}__{tenure}__{care}"

        before_earnings, after_earnings = number(before["TPEARN"]), number(after["TPEARN"])
        before_hours, after_hours = number(before["TMWKHRS"]), number(after["TMWKHRS"])
        mortgage_valid = valid(after["EAWBMORT"], after["AAWBMORT"])
        food_valid = after["RFOODS"] in {"1", "2", "3"} and after["AFOODS"] not in {"", "0"}
        before_band, after_band = band(before["THINCPOV"]), band(after["THINCPOV"])
        flags = {
            "earnings_changed": before_earnings is not None and after_earnings is not None and before_earnings != after_earnings,
            "hours_changed": before_hours is not None and after_hours is not None and before_hours != after_hours,
            "mortgage_hardship": mortgage_valid and after["EAWBMORT"] == "1",
            "food_insecurity": food_valid and after["RFOODS"] in {"2", "3"},
            "resource_band_changed": before_band is not None and after_band is not None and before_band != after_band,
        }
        valid_outcomes = {
            "earnings_changed": before_earnings is not None and after_earnings is not None,
            "hours_changed": before_hours is not None and after_hours is not None,
            "mortgage_hardship": mortgage_valid,
            "food_insecurity": food_valid,
            "resource_band_changed": before_band is not None and after_band is not None,
        }
        if not any(valid_outcomes.values()):
            continue
        key = tuple(before[k] for k in KEYS)
        if key in pairs:
            raise ValueError(f"duplicate selected pair key: {key}")
        pairs[key] = (group, flags, weight)
        cells[group]["pairs"] += 1
        for outcome in outcomes:
            if valid_outcomes[outcome]:
                cells[group][outcome]["records"] += 1
                cells[group][outcome]["denominator"] += weight
                cells[group][outcome]["numerator"] += weight * flags[outcome]

    # Re-read the compact primary-side validity for replicate accumulation.
    # Keeping this map separate makes outcome-specific denominators explicit.
    valid_map: dict[tuple[str, ...], dict[str, bool]] = {}
    for person, months in people.items():
        before, after = months.get("11"), months.get("12")
        if before is None or after is None:
            continue
        key = tuple(before[k] for k in KEYS)
        selected = pairs.get(key)
        if selected is None:
            continue
        before_earnings, after_earnings = number(before["TPEARN"]), number(after["TPEARN"])
        before_hours, after_hours = number(before["TMWKHRS"]), number(after["TMWKHRS"])
        valid_map[key] = {
            "earnings_changed": before_earnings is not None and after_earnings is not None,
            "hours_changed": before_hours is not None and after_hours is not None,
            "mortgage_hardship": valid(after["EAWBMORT"], after["AAWBMORT"]),
            "food_insecurity": after["RFOODS"] in {"1", "2", "3"} and after["AFOODS"] not in {"", "0"},
            "resource_band_changed": band(before["THINCPOV"]) is not None and band(after["THINCPOV"]) is not None,
        }

    rep_num = {group: {outcome: np.zeros(REPLICATES) for outcome in outcomes} for group in groups}
    rep_den = {group: {outcome: np.zeros(REPLICATES) for outcome in outcomes} for group in groups}
    replicate_rows_read = matched_pairs = 0
    matched_keys: set[tuple[str, ...]] = set()
    with zipfile.ZipFile(args.replicate_zip) as archive, archive.open("rw2025.csv") as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
        for row in reader:
            replicate_rows_read += 1
            key = tuple(row[k.lower()] for k in KEYS)
            selected = pairs.get(key)
            if selected is None:
                continue
            matched_pairs += 1
            matched_keys.add(key)
            group, flags, _ = selected
            weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                                  dtype=float, count=REPLICATES)
            for outcome in outcomes:
                if valid_map[key][outcome]:
                    rep_den[group][outcome] += weights
                    if flags[outcome]:
                        rep_num[group][outcome] += weights

    if matched_pairs != len(pairs):
        missing = sorted(set(pairs) - matched_keys)
        raise ValueError(f"{len(missing)} selected pair keys absent from replicate file")

    results = {}
    for group in groups:
        results[group] = {"pairs": cells[group]["pairs"]}
        for outcome in outcomes:
            cell = cells[group][outcome]
            results[group][outcome] = {
                "valid_records": cell["records"],
                **estimate(cell["numerator"], cell["denominator"],
                           rep_num[group][outcome], rep_den[group][outcome]),
            }

    observations = []
    for group, values in results.items():
        measures = {}
        for outcome in outcomes:
            estimate_value = values[outcome]
            measures[outcome] = {
                "value": estimate_value["share_percent"],
                "unit": "person-weighted percent",
                "value_type": "conditional_share",
                "valid_records": estimate_value["valid_records"],
                "standard_error_percentage_points": estimate_value["standard_error_percentage_points"],
                "approx_95_ci_percentage_points": estimate_value["approx_95_ci_percentage_points"],
            }
        observations.append({
            "period": "2024 reference year; November-to-December",
            "denominator": {
                "value": values["pairs"],
                "unit": "identified person pairs in utility/tenure/childcare cell",
                "value_type": "person_pairs",
            },
            "measures": measures,
            "method": "Same-person adjacent-month comparison using November WPFINWGT and 240 Fay-BRR replicate weights.",
            "uncertainty": "Outcome-specific valid records and approximate Fay-BRR intervals are retained; cells with childcare prevention and utility difficulty are sparse.",
            "subgroup": group,
            "counterinterpretation": "Utility, tenure, childcare, work, housing, food, and resource fields are observational and may reflect shared selection, season, health, family composition, or reporting.",
            "source_url": "https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html",
            "retrieval_hash": "sha256:4fe7395d4ecdb2f1a3f2879a394f47d1e809c9bdef3960b60543919b79a61eda; sha256:3bf35c17723de10697d581d1122fda4d7cdecb34c6f9e9dfcb18ddc561c7c6b6",
            "status": "compared",
        })

    output = {
        "format": "us-trend-observation-record-v1",
        "trend_id": "us-sipp-constraint-cascade-screen-2024",
        "title": "Utility difficulty, tenure, and childcare prevention beside next-month work and household-security outcomes",
        "theme_ids": ["cost", "time", "work", "energy"],
        "program_theme_ids": ["household_room_consumption", "time_hidden_price", "housing_place_mobility", "work_control_bargaining", "care_health_reproduction", "unequal_exposure_status"],
        "source_unit": "identified November-to-December SIPP person pairs; utility and tenure at month t, childcare status and outcomes at month t+1",
        "geography": "United States",
        "reference_period": "2024 reference year in 2025 SIPP public-use file",
        "weight": "WPFINWGT from November; REPWGT1-REPWGT240 for Fay-BRR variance",
        "variance_method": "Fay BRR, 240 replicate weights, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "identified_pairs": len(pairs),
        "replicate_rows_read": replicate_rows_read,
        "replicate_pairs_matched": matched_pairs,
        "observations": observations,
        "group_definitions": {
            "utility": "EAWBGAS code 1 versus 2 with valid AAWBGAS",
            "tenure": "ETENURE code 1 (owned/bought) versus 2 (rented)",
            "care": "December EWORKMORE code 1 versus 2 with valid AWORKMORE; annual fall childcare-work-prevention report",
            "earnings_hours": "numeric nonnegative TPEARN/TMWKHRS change from November to December",
            "mortgage": "December EAWBMORT code 1 versus 2 with valid AAWBMORT",
            "food": "December RFOODS code 2 or 3 among valid RFOODS/AFOODS",
            "resource": "any November-to-December THINCPOV four-band crossing",
        },
        "results": results,
        "source_url": "https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html",
        "related_sources": [
            "https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf",
            "https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip",
        ],
        "causal_estimation": False,
        "boundary": "This is a same-person adjacent-month descriptive screen. It does not identify a dated utility bill, shutoff, childcare event, causal effect, household-weighted prevalence, desired work, care hours, recovery, remedy, trust, political action, or exit. The annual fall childcare field and several household fields may be reference-period or repeated measures.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "identified_pairs": len(pairs),
                      "replicate_pairs_matched": matched_pairs}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
