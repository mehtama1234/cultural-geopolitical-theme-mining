#!/usr/bin/env python3
"""Compare the November-to-December SNAP transition with annual child-care constraints."""

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
TRANSITIONS = ("no -> no", "no -> yes", "yes -> no", "yes -> yes")
OUTCOMES = ("paid_childcare", "childcare_assistance", "care_prevented_work")
RAW_OUTCOME_FIELDS = {"paid_childcare": "EPAY", "childcare_assistance": "EPAYHELP", "care_prevented_work": "EWORKMORE"}


def snap(value: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(value)


def yes_no(value: str) -> bool:
    return value in {"1", "2"}


def summarize(num: float, den: float, rep_num: np.ndarray, rep_den: np.ndarray, records: int) -> dict:
    theta = num / den if den else None
    estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    se = None
    if theta is not None and not np.isnan(estimates).any():
        se = float(np.sqrt(np.sum((estimates - theta) ** 2) / (REPLICATES * FAY_FACTOR**2)))
    return {
        "records": records,
        "weighted_denominator": den,
        "share_percent": 100 * theta if theta is not None else None,
        "standard_error_percentage_points": 100 * se if se is not None else None,
        "approx_95_percent_ci": ([max(0.0, 100 * theta - 1.96 * 100 * se), min(100.0, 100 * theta + 1.96 * 100 * se)] if se is not None else None),
    }


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
        required = set(KEYS) | {"WPFINWGT", "RSNAP_MNYN", *RAW_OUTCOME_FIELDS.values(), "ETIMELOST"}
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
            month = int(row["MONTHCODE"])
            people[person][month] = {
                "snap": row["RSNAP_MNYN"],
                "weight": row["WPFINWGT"],
                "paid_childcare": row[RAW_OUTCOME_FIELDS["paid_childcare"]],
                "childcare_assistance": row[RAW_OUTCOME_FIELDS["childcare_assistance"]],
                "care_prevented_work": row[RAW_OUTCOME_FIELDS["care_prevented_work"]],
                "time_lost": row["ETIMELOST"],
            }

    pair_data = {}
    num = {t: {o: 0.0 for o in OUTCOMES} for t in TRANSITIONS}
    den = {t: {o: 0.0 for o in OUTCOMES} for t in TRANSITIONS}
    records = {t: {o: 0 for o in OUTCOMES} for t in TRANSITIONS}
    for person, months in people.items():
        if 11 not in months or 12 not in months:
            continue
        before, after = months[11], months[12]
        transition = f"{snap(before['snap'])} -> {snap(after['snap'])}"
        if transition not in TRANSITIONS:
            continue
        key = person + ("11",)
        outcomes = {o: yes_no(after[o]) for o in OUTCOMES}
        pair_data[key] = (transition, outcomes)
        weight = float(before["weight"])
        for outcome, valid in outcomes.items():
            if valid:
                den[transition][outcome] += weight
                records[transition][outcome] += 1
                if after[outcome] == "1":
                    num[transition][outcome] += weight

    rep_num = {t: {o: np.zeros(REPLICATES) for o in OUTCOMES} for t in TRANSITIONS}
    rep_den = {t: {o: np.zeros(REPLICATES) for o in OUTCOMES} for t in TRANSITIONS}
    replicate_rows_read = 0
    matched = 0
    with zipfile.ZipFile(args.replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            for row in reader:
                replicate_rows_read += 1
                key = tuple(row[key.lower()] for key in KEYS)
                item = pair_data.get(key)
                if item is None:
                    continue
                matched += 1
                transition, outcomes = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)), dtype=np.float64, count=REPLICATES)
                for outcome, valid in outcomes.items():
                    if not valid:
                        continue
                    rep_den[transition][outcome] += weights
                    if people[key[:-1]][12][outcome] == "1":
                        rep_num[transition][outcome] += weights

    results = {
        transition: {
            "transition": transition,
            "outcomes": {
                outcome: summarize(num[transition][outcome], den[transition][outcome], rep_num[transition][outcome], rep_den[transition][outcome], records[transition][outcome])
                for outcome in OUTCOMES
            },
        }
        for transition in TRANSITIONS
    }
    output = {
        "format": "us-sipp-snap-transition-childcare-bridge-fay-brr-v1",
        "source_unit": "identified person with November-to-December adjacent-month SNAP pair and December annual child-care fields",
        "reference_period": "2024",
        "transition": "SNAP receipt in November -> December",
        "weight": "WPFINWGT from November; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "transition_pairs": len(pair_data),
        "replicate_pairs_matched": matched,
        "results": results,
        "causal_estimation": False,
        "boundary": "EPAY, EPAYHELP, and EWORKMORE describe the reference-year fall child-care universe and are attached here to the December transition only as a same-person timing bridge. They do not measure November/December route effort, notice, benefit amount, monthly care change, or causality. ETIMELOST is retained in the source slice but not summarized because it is conditional on EWORKMORE=1 and has a separate type field not included in the selected slice.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_read": rows_read, "transition_pairs": len(pair_data), "matched_replicates": matched}, indent=2))


if __name__ == "__main__":
    main()
