#!/usr/bin/env python3
"""Compare following-month hardship by child-care work-prevention status."""

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
TRANSITIONS = ("no -> no", "yes -> yes")
GROUPS = ("care_work_prevented=no", "care_work_prevented=yes")
OUTCOMES = ("rent_mortgage_hardship", "utility_hardship")
REPLICATES = 240
FAY_FACTOR = 0.5


def snap(value: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(value)


def valid_binary(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def summarize(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray, records: int) -> dict:
    share = num / den if den else None
    estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    se = None
    if share is not None and not np.isnan(estimates).any():
        se = float(np.sqrt(np.sum((estimates - share) ** 2) / (REPLICATES * FAY_FACTOR**2)))
    return {"records": records, "weighted_denominator": den,
            "share_percent": 100 * share if share is not None else None,
            "standard_error_percentage_points": 100 * se if se is not None else None,
            "approx_95_percent_ci": ([max(0.0, 100 * share - 1.96 * 100 * se), min(100.0, 100 * share + 1.96 * 100 * se)] if se is not None else None)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    people = defaultdict(dict)
    rows_read = 0
    with args.primary.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = set(KEYS) | {"WPFINWGT", "RSNAP_MNYN", "EWORKMORE", "AWORKMORE", "EAWBMORT", "AAWBMORT", "EAWBGAS", "AAWBGAS"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            if row["MONTHCODE"] not in {"11", "12"}:
                continue
            try:
                float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            person = tuple(row[key] for key in KEYS[:-1])
            people[person][int(row["MONTHCODE"])] = {key: row.get(key, "") for key in ("RSNAP_MNYN", "WPFINWGT", "EWORKMORE", "AWORKMORE", "EAWBMORT", "AAWBMORT", "EAWBGAS", "AAWBGAS")}

    buckets = [f"{transition}|{group}" for transition in TRANSITIONS for group in GROUPS]
    num = {b: {o: 0.0 for o in OUTCOMES} for b in buckets}
    den = {b: {o: 0.0 for o in OUTCOMES} for b in buckets}
    records = {b: {o: 0 for o in OUTCOMES} for b in buckets}
    pairs = {}
    for person, months in people.items():
        if 11 not in months or 12 not in months:
            continue
        before, after = months[11], months[12]
        transition = f"{snap(before['RSNAP_MNYN'])} -> {snap(after['RSNAP_MNYN'])}"
        if transition not in TRANSITIONS or not valid_binary(after["EWORKMORE"], after["AWORKMORE"]):
            continue
        group = f"care_work_prevented={'yes' if after['EWORKMORE'] == '1' else 'no'}"
        bucket = f"{transition}|{group}"
        key = person + ("11",)
        outcomes = {
            "rent_mortgage_hardship": valid_binary(after["EAWBMORT"], after["AAWBMORT"]),
            "utility_hardship": valid_binary(after["EAWBGAS"], after["AAWBGAS"]),
        }
        pairs[key] = (bucket, outcomes, after["EAWBMORT"], after["EAWBGAS"])
        weight = float(before["WPFINWGT"])
        for outcome, is_valid in outcomes.items():
            if is_valid:
                den[bucket][outcome] += weight
                records[bucket][outcome] += 1
                if (outcome == "rent_mortgage_hardship" and after["EAWBMORT"] == "1") or (outcome == "utility_hardship" and after["EAWBGAS"] == "1"):
                    num[bucket][outcome] += weight

    rep_num = {b: {o: np.zeros(REPLICATES) for o in OUTCOMES} for b in buckets}
    rep_den = {b: {o: np.zeros(REPLICATES) for o in OUTCOMES} for b in buckets}
    matched = 0
    with zipfile.ZipFile(args.replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            for row in reader:
                key = tuple(row[key.lower()] for key in KEYS)
                item = pairs.get(key)
                if item is None:
                    continue
                matched += 1
                bucket, outcomes, mort, gas = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)), dtype=np.float64, count=REPLICATES)
                for outcome, is_valid in outcomes.items():
                    if not is_valid:
                        continue
                    rep_den[bucket][outcome] += weights
                    if (outcome == "rent_mortgage_hardship" and mort == "1") or (outcome == "utility_hardship" and gas == "1"):
                        rep_num[bucket][outcome] += weights

    output = {"format": "us-sipp-childcare-work-hardship-bridge-fay-brr-v1", "source_unit": "identified person with November-to-December stable SNAP pair and December hardship fields", "reference_period": "2024", "weight": "WPFINWGT from November; REPWGT1-REPWGT240 for variance", "variance_method": "Fay BRR, G=240, perturbation factor 0.5", "rows_read": rows_read, "replicate_pairs_matched": matched, "results": {b: {o: summarize(num[b][o], den[b][o], rep_num[b][o], rep_den[b][o], records[b][o]) for o in OUTCOMES} for b in buckets}, "causal_estimation": False, "boundary": "This is a descriptive same-person bridge between annual fall child-care work prevention and following-month hardship. It does not establish that child-care constraints caused hardship; outcome fields have separate universes and status flags."
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "replicate_pairs_matched": matched}, indent=2))


if __name__ == "__main__":
    main()
