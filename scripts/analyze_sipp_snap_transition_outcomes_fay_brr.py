#!/usr/bin/env python3
"""Estimate material hardship in the month after adjacent SNAP transitions.

This is a person-month descriptive diagnostic.  The transition is defined by
SNAP receipt in month t and t+1; the outcome is the valid code-1 hardship
report in month t+1.  Fay-BRR replicate weights are taken from month t.  The
result is time-ordered but is not a program-impact estimate: the hardship
fields have their own universes and may be reference-period measures.
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
TRANSITIONS = ("no -> no", "no -> yes", "yes -> no", "yes -> yes")
OUTCOMES = {
    "EAWBMORT": "unable to pay rent or mortgage",
    "EAWBGAS": "unable to pay utility bills",
}
REPLICATES = 240
FAY_FACTOR = 0.5


def snap(value: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(value)


def valid_binary(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def summarize(numerator: float, denominator: float, rep_num: np.ndarray,
             rep_den: np.ndarray, records: int) -> dict:
    theta = numerator / denominator if denominator else None
    estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    se = None
    if theta is not None and not np.isnan(estimates).any():
        variance = np.sum((estimates - theta) ** 2) / (REPLICATES * FAY_FACTOR ** 2)
        se = float(np.sqrt(variance))
    return {
        "records": records,
        "weight": denominator,
        "share_percent": 100 * theta if theta is not None else None,
        "standard_error_percentage_points": 100 * se if se is not None else None,
        "approx_95_percent_ci": (
            [max(0.0, 100 * theta - 1.96 * 100 * se),
             min(100.0, 100 * theta + 1.96 * 100 * se)]
            if theta is not None and se is not None else None
        ),
    }


def analyze(primary_path: Path, replicate_zip: Path) -> dict:
    people: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with primary_path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "RSNAP_MNYN", "AAWBMORT", "AAWBGAS",
                                "EAWBMORT", "EAWBGAS"}
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
            if not 1 <= month <= 12 or weight <= 0:
                continue
            person = tuple(row[key] for key in KEYS[:-1])
            people[person][month] = {
                "snap": row.get("RSNAP_MNYN", ""),
                "mort": row.get("EAWBMORT", ""),
                "mort_flag": row.get("AAWBMORT", ""),
                "gas": row.get("EAWBGAS", ""),
                "gas_flag": row.get("AAWBGAS", ""),
                "weight": row.get("WPFINWGT", ""),
            }

    # Each key is the first month of a pair. Outcomes come from the next month.
    pair_data: dict[tuple[str, str, str, str, str], tuple[str, dict[str, bool]]] = {}
    full_num = {t: {o: 0.0 for o in OUTCOMES} for t in TRANSITIONS}
    full_den = {t: {o: 0.0 for o in OUTCOMES} for t in TRANSITIONS}
    records = {t: {o: 0 for o in OUTCOMES} for t in TRANSITIONS}
    for person, months in people.items():
        for month in range(1, 12):
            if month not in months or month + 1 not in months:
                continue
            before, after = months[month], months[month + 1]
            transition = f"{snap(before['snap'])} -> {snap(after['snap'])}"
            if transition not in TRANSITIONS:
                continue
            outcomes = {
                "EAWBMORT": valid_binary(after["mort"], after["mort_flag"]),
                "EAWBGAS": valid_binary(after["gas"], after["gas_flag"]),
            }
            key = person + (str(month),)
            pair_data[key] = (transition, outcomes)
            weight = float(before["weight"])
            for outcome, is_valid in outcomes.items():
                if not is_valid:
                    continue
                full_den[transition][outcome] += weight
                records[transition][outcome] += 1
                if after["mort" if outcome == "EAWBMORT" else "gas"] == "1":
                    full_num[transition][outcome] += weight

    rep_num = {t: {o: np.zeros(REPLICATES) for o in OUTCOMES} for t in TRANSITIONS}
    rep_den = {t: {o: np.zeros(REPLICATES) for o in OUTCOMES} for t in TRANSITIONS}
    replicate_rows_read = 0
    matched = 0
    with zipfile.ZipFile(replicate_zip) as archive:
        if archive.namelist() != ["rw2025.csv"]:
            raise ValueError(f"unexpected replicate archive members: {archive.namelist()}")
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            required = {key.lower() for key in KEYS} | {f"repwgt{i}" for i in range(1, REPLICATES + 1)}
            missing = sorted(required - set(reader.fieldnames or []))
            if missing:
                raise ValueError("replicate file is missing fields: " + ", ".join(missing[:8]))
            for row in reader:
                replicate_rows_read += 1
                key = tuple(row[key.lower()] for key in KEYS)
                item = pair_data.get(key)
                if item is None:
                    continue
                matched += 1
                transition, outcomes = item
                weights = np.fromiter(
                    (float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                    dtype=np.float64, count=REPLICATES,
                )
                for outcome, is_valid in outcomes.items():
                    if not is_valid:
                        continue
                    rep_den[transition][outcome] += weights
                    # Recover the code-1 status from the stored pair outcome by
                    # retaining it in the key-level map below would be larger;
                    # use the primary pair lookup's second element as a bool map.
                    person = key[:-1]
                    month = int(key[-1])
                    after = people[person][month + 1]
                    if after["mort" if outcome == "EAWBMORT" else "gas"] == "1":
                        rep_num[transition][outcome] += weights

    results = {t: {o: summarize(full_num[t][o], full_den[t][o], rep_num[t][o],
                                  rep_den[t][o], records[t][o]) for o in OUTCOMES}
                for t in TRANSITIONS}
    return {
        "format": "us-sipp-snap-transition-outcome-fay-brr-v1",
        "source_unit": "identified person, adjacent reference-month pair",
        "transition": "SNAP receipt in month t -> month t+1",
        "outcome": "valid code-1 rent/mortgage or utility hardship report in month t+1",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "transition_pairs_matched": matched,
        "results": results,
        "causal_estimation": False,
        "household_weight_used": False,
        "boundary": "Hardship fields have their own universes and may be reference-period measures; this is not a program-impact or household-benefit estimate.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
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
