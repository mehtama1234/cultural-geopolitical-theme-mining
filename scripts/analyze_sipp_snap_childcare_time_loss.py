#!/usr/bin/env python3
"""Estimate child-care work-prevention and reported time-loss type by SNAP transition."""

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
REPLICATES = 240
FAY_FACTOR = 0.5


def snap(value: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(value)


def valid(value: str, flag: str = "") -> bool:
    return value in {"1", "2"} and (not flag or flag not in {"0"})


def summary(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray, records: int) -> dict:
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
        required = set(KEYS) | {"WPFINWGT", "RSNAP_MNYN", "EWORKMORE", "ETIMELOST", "ETIMELOST_TP"}
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("primary slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            if row["MONTHCODE"] not in {"11", "12"}:
                continue
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            person = tuple(row[key] for key in KEYS[:-1])
            people[person][int(row["MONTHCODE"])] = {key: row.get(key, "") for key in ("RSNAP_MNYN", "WPFINWGT", "EWORKMORE", "ETIMELOST", "ETIMELOST_TP", "AWORKMORE", "ATIMELOST", "ATIMELOST_TP")}

    metrics = ["care_prevented_work", "time_lost_any", "time_lost_hours", "time_lost_days", "time_lost_weeks"]
    num = {t: {m: 0.0 for m in metrics} for t in TRANSITIONS}
    den = {t: {m: 0.0 for m in metrics} for t in TRANSITIONS}
    records = {t: {m: 0 for m in metrics} for t in TRANSITIONS}
    pairs = {}
    for person, months in people.items():
        if 11 not in months or 12 not in months:
            continue
        before, after = months[11], months[12]
        transition = f"{snap(before['RSNAP_MNYN'])} -> {snap(after['RSNAP_MNYN'])}"
        if transition not in TRANSITIONS:
            continue
        key = person + ("11",)
        work_valid = valid(after["EWORKMORE"], after["AWORKMORE"])
        time_valid = after["ETIMELOST"] not in {"", "-1", "-2", "-3", "-9"} and after["ATIMELOST"] not in {"", "0"}
        type_valid = after["ETIMELOST_TP"] in {"1", "2", "3"} and after["ATIMELOST_TP"] not in {"", "0"}
        pairs[key] = (transition, work_valid, time_valid, type_valid, after["EWORKMORE"], after["ETIMELOST_TP"])
        weight = float(before["WPFINWGT"])
        if work_valid:
            den[transition]["care_prevented_work"] += weight
            records[transition]["care_prevented_work"] += 1
            if after["EWORKMORE"] == "1":
                num[transition]["care_prevented_work"] += weight
        if time_valid and type_valid:
            den[transition]["time_lost_any"] += weight
            records[transition]["time_lost_any"] += 1
            num[transition]["time_lost_any"] += weight
            metric = {"1": "time_lost_hours", "2": "time_lost_days", "3": "time_lost_weeks"}[after["ETIMELOST_TP"]]
            den[transition][metric] += weight
            records[transition][metric] += 1
            num[transition][metric] += weight

    rep_num = {t: {m: np.zeros(REPLICATES) for m in metrics} for t in TRANSITIONS}
    rep_den = {t: {m: np.zeros(REPLICATES) for m in metrics} for t in TRANSITIONS}
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
                transition, work_valid, time_valid, type_valid, work_value, time_type = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)), dtype=np.float64, count=REPLICATES)
                if work_valid:
                    rep_den[transition]["care_prevented_work"] += weights
                    if work_value == "1":
                        rep_num[transition]["care_prevented_work"] += weights
                if time_valid and type_valid:
                    rep_den[transition]["time_lost_any"] += weights
                    rep_num[transition]["time_lost_any"] += weights
                    metric = {"1": "time_lost_hours", "2": "time_lost_days", "3": "time_lost_weeks"}[time_type]
                    rep_den[transition][metric] += weights
                    rep_num[transition][metric] += weights

    for transition in TRANSITIONS:
        for metric in ("time_lost_hours", "time_lost_days", "time_lost_weeks"):
            den[transition][metric] = den[transition]["time_lost_any"]
            records[transition][metric] = records[transition]["time_lost_any"]
            rep_den[transition][metric] = rep_den[transition]["time_lost_any"]

    output = {"format": "us-sipp-snap-childcare-time-loss-fay-brr-v1", "source_unit": "identified person with November-to-December adjacent-month SNAP pair", "reference_period": "2024", "transition": "SNAP receipt in November -> December", "weight": "WPFINWGT from November; REPWGT1-REPWGT240 for variance", "variance_method": "Fay BRR, G=240, perturbation factor 0.5", "rows_read": rows_read, "replicate_pairs_matched": matched, "status_flag_limitation": "Status flags AWORKMORE, ATIMELOST, and ATIMELOST_TP are included and used; flags coded unavailable or not applicable are excluded.", "time_loss_type_denominator": "time_lost_any is the shared denominator for hours/days/weeks composition; care_prevented_work uses its own valid EWORKMORE denominator.", "results": {t: {m: summary(num[t][m], den[t][m], rep_num[t][m], rep_den[t][m], records[t][m]) for m in metrics} for t in TRANSITIONS}, "causal_estimation": False, "boundary": "ETIMELOST and ETIMELOST_TP describe reported fall-reference-year time lost from work due to child-care problems among reference parents for whom child-care arrangements prevented working or working more. The November-to-December SNAP transition is a same-person timing bridge, not evidence that SNAP caused child-care time loss."
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "replicate_pairs_matched": matched}, indent=2))


if __name__ == "__main__":
    main()
