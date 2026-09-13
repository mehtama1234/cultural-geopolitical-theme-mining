#!/usr/bin/env python3
"""Estimate Fay-BRR uncertainty for recorded reasons on SIPP SNAP transitions."""

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
START_REASONS = {
    "1": "new child/dependent or pregnancy",
    "2": "separation, divorce, or widowhood",
    "3": "job loss/layoff or wages reduced",
    "4": "loss or reduction of other income",
    "5": "became disabled or otherwise unable to work",
    "6": "no change—decided it was time",
    "7": "no change—heard about the program",
    "8": "needed to recertify",
    "9": "other",
}
END_REASONS = {
    "1": "ineligible because income increased",
    "2": "ineligible because of family changes",
    "3": "still eligible but could not/chose not to collect",
    "4": "requirements not met",
    "5": "time limit reached",
    "6": "benefits not worth the trouble",
    "7": "other",
}


def transition(before: str, after: str) -> str | None:
    if before == "2" and after == "1":
        return "no -> yes"
    if before == "1" and after == "2":
        return "yes -> no"
    return None


def analyze(primary_path: Path, replicate_zip: Path) -> dict:
    required = set(KEYS) | {"WPFINWGT", "RSNAP_MNYN", "ESNAP_BRSN", "ASNAP_BRSN",
                             "ESNAP_ERSN", "ASNAP_ERSN"}
    months: dict[tuple[str, str, str, str], dict[int, tuple[str, float, dict[str, str]]]] = defaultdict(dict)
    rows_read = 0
    with primary_path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
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
            if 1 <= month <= 12 and weight > 0:
                person = tuple(row[key] for key in KEYS[:-1])
                fields = {field: row.get(field, "") for field in required}
                months[person][month] = (row.get("RSNAP_MNYN", ""), weight, fields)

    # Each key identifies a transition pair whose reason is known and classified.
    by_key: dict[tuple[str, str, str, str, str], tuple[str, str]] = {}
    transitions = {"no -> yes": {"pairs": 0, "reason_pairs": 0, "weight": 0.0},
                   "yes -> no": {"pairs": 0, "reason_pairs": 0, "weight": 0.0}}
    full_num = {label: defaultdict(float) for label in transitions}
    full_den = defaultdict(float)
    pair_counts = {label: defaultdict(int) for label in transitions}
    for person, records in months.items():
        for month in range(1, 12):
            if month not in records or month + 1 not in records:
                continue
            before, weight, first = records[month]
            after, _, second = records[month + 1]
            label = transition(before, after)
            if label is None:
                continue
            transitions[label]["pairs"] += 1
            transitions[label]["weight"] += weight
            if label == "no -> yes":
                code = second.get("ESNAP_BRSN", "")
                known = second.get("ASNAP_BRSN", "") not in {"", "0"} and code in START_REASONS
                labels = START_REASONS
            else:
                code = first.get("ESNAP_ERSN", "")
                known = first.get("ASNAP_ERSN", "") not in {"", "0"} and code in END_REASONS
                labels = END_REASONS
            if not known:
                continue
            transitions[label]["reason_pairs"] += 1
            full_den[label] += weight
            full_num[label][code] += weight
            pair_counts[label][code] += 1
            by_key[person + (str(month),)] = (label, code)

    rep_num = {label: {code: np.zeros(REPLICATES, dtype=np.float64) for code in labels}
               for label, labels in (("no -> yes", START_REASONS), ("yes -> no", END_REASONS))}
    rep_den = {label: np.zeros(REPLICATES, dtype=np.float64) for label in transitions}
    replicate_rows_read = 0
    matched = 0
    with zipfile.ZipFile(replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            required_rep = {key.lower() for key in KEYS} | {f"repwgt{i}" for i in range(1, REPLICATES + 1)}
            missing = sorted(required_rep - set(reader.fieldnames or []))
            if missing:
                raise ValueError("replicate file is missing fields: " + ", ".join(missing[:8]))
            for row in reader:
                replicate_rows_read += 1
                key = tuple(row[key.lower()] for key in KEYS)
                found = by_key.get(key)
                if found is None:
                    continue
                matched += 1
                label, code = found
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                                      dtype=np.float64, count=REPLICATES)
                rep_den[label] += weights
                rep_num[label][code] += weights

    results = {}
    for label, labels in (("no -> yes", START_REASONS), ("yes -> no", END_REASONS)):
        theta = full_den[label]
        categories = {}
        for code in sorted(labels):
            value = full_num[label][code] / theta if theta else None
            reps = np.divide(rep_num[label][code], rep_den[label],
                             out=np.full(REPLICATES, np.nan), where=rep_den[label] != 0)
            se = None
            if value is not None and np.all(np.isfinite(reps)):
                se = float(np.sqrt(np.sum((reps - value) ** 2) /
                                   (REPLICATES * FAY_FACTOR**2)))
            categories[code] = {
                "label": labels[code],
                "classified_pairs": pair_counts[label][code],
                "weight": full_num[label][code],
                "share_percent": 100 * value if value is not None else None,
                "standard_error_percentage_points": 100 * se if se is not None else None,
                "approx_95_percent_ci": ([max(0.0, 100 * value - 1.96 * 100 * se),
                                           min(100.0, 100 * value + 1.96 * 100 * se)]
                                          if value is not None and se is not None else None),
            }
        results[label] = {
            "all_transition_pairs": transitions[label]["pairs"],
            "all_transition_weight": transitions[label]["weight"],
            "classified_pairs": transitions[label]["reason_pairs"],
            "classified_weight": theta,
            "categories": categories,
        }

    return {
        "format": "us-sipp-snap-transition-reason-fay-brr-v1",
        "source_unit": "identified person, adjacent reference-month pair",
        "weight": "WPFINWGT from first month; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "positive_weight_classified_pairs_matched": matched,
        "results": results,
        "causal_estimation": False,
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
