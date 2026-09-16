#!/usr/bin/env python3
"""Cross-tab recorded SNAP transition reasons with following hardship."""

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
OUTCOMES = {"EAWBMORT": "unable to pay rent or mortgage",
            "EAWBGAS": "unable to pay utility bills",
            "RFOODS": "low or very low food security"}
COMPOUND_OUTCOME = "BOTH_HARDSHIPS"
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


def snap(value: str) -> str | None:
    return {"1": "yes", "2": "no"}.get(value)


def transition(before: str, after: str) -> str | None:
    if before == "2" and after == "1":
        return "no -> yes"
    if before == "1" and after == "2":
        return "yes -> no"
    return None


def valid(value: str, flag: str) -> bool:
    return value in {"1", "2"} and flag not in {"", "0"}


def summarize(numerator: float, denominator: float, rep_num: np.ndarray,
             rep_den: np.ndarray, records: int) -> dict:
    theta = numerator / denominator if denominator else None
    estimates = np.divide(rep_num, rep_den, out=np.full(REPLICATES, np.nan), where=rep_den != 0)
    se = None
    if theta is not None and not np.isnan(estimates).any():
        se = float(np.sqrt(np.sum((estimates - theta) ** 2) /
                           (REPLICATES * FAY_FACTOR ** 2)))
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--replicate-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = set(KEYS) | {
        "WPFINWGT", "RSNAP_MNYN", "ESNAP_BRSN", "ASNAP_BRSN",
        "ESNAP_ERSN", "ASNAP_ERSN", "EAWBMORT", "EAWBGAS", "RFOODS",
        "AAWBMORT", "AAWBGAS", "AFOODS",
    }
    people: dict[tuple[str, str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with args.primary.open(encoding="utf-8", newline="") as source:
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
            if not 1 <= month <= 12 or weight <= 0:
                continue
            person = tuple(row[key] for key in KEYS[:-1])
            people[person][month] = {field: row.get(field, "") for field in required}

    labels_by_transition = {"no -> yes": START_REASONS, "yes -> no": END_REASONS}
    buckets = [(transition_name, code)
               for transition_name, labels in labels_by_transition.items()
               for code in labels]
    outcome_names = (*OUTCOMES, COMPOUND_OUTCOME)
    full_num = {(bucket, outcome): 0.0 for bucket in buckets for outcome in outcome_names}
    full_den = {(bucket, outcome): 0.0 for bucket in buckets for outcome in outcome_names}
    records = {(bucket, outcome): 0 for bucket in buckets for outcome in outcome_names}
    pair_map: dict[tuple[str, str, str, str, str], tuple[tuple[str, str], dict[str, bool], dict[str, str]]] = {}
    all_transitions = defaultdict(int)
    classified_transitions = defaultdict(int)

    for person, months in people.items():
        for month in range(1, 12):
            if month not in months or month + 1 not in months:
                continue
            before, after = months[month], months[month + 1]
            transition_name = transition(before.get("RSNAP_MNYN", ""), after.get("RSNAP_MNYN", ""))
            if transition_name is None:
                continue
            all_transitions[transition_name] += 1
            if transition_name == "no -> yes":
                reason = after.get("ESNAP_BRSN", "")
                known = after.get("ASNAP_BRSN", "") not in {"", "0"} and reason in START_REASONS
            else:
                reason = before.get("ESNAP_ERSN", "")
                known = before.get("ASNAP_ERSN", "") not in {"", "0"} and reason in END_REASONS
            if not known:
                continue
            classified_transitions[transition_name] += 1
            bucket = (transition_name, reason)
            outcomes = {field: valid(after.get(field, ""), after.get("A" + field[1:], ""))
                        for field in OUTCOMES}
            outcomes[COMPOUND_OUTCOME] = all(outcomes.values())
            key = person + (str(month),)
            pair_map[key] = (bucket, outcomes, after)
            for outcome, is_valid in outcomes.items():
                if not is_valid:
                    continue
                records[(bucket, outcome)] += 1
                full_den[(bucket, outcome)] += float(before["WPFINWGT"])
                positive = (
                    after[outcome] in {"2", "3"} if outcome == "RFOODS"
                    else after["EAWBMORT"] == "1" and after["EAWBGAS"] == "1"
                    if outcome == COMPOUND_OUTCOME else after[outcome] == "1"
                )
                if positive:
                    full_num[(bucket, outcome)] += float(before["WPFINWGT"])

    rep_num = {(bucket, outcome): np.zeros(REPLICATES) for bucket in buckets for outcome in outcome_names}
    rep_den = {(bucket, outcome): np.zeros(REPLICATES) for bucket in buckets for outcome in outcome_names}
    replicate_rows_read = 0
    matched = 0
    with zipfile.ZipFile(args.replicate_zip) as archive:
        with archive.open("rw2025.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""), delimiter="|")
            required_rep = {key.lower() for key in KEYS} | {f"repwgt{i}" for i in range(1, REPLICATES + 1)}
            missing = sorted(required_rep - set(reader.fieldnames or []))
            if missing:
                raise ValueError("replicate file is missing fields: " + ", ".join(missing[:8]))
            for row in reader:
                replicate_rows_read += 1
                key = tuple(row[key.lower()] for key in KEYS)
                item = pair_map.get(key)
                if item is None:
                    continue
                matched += 1
                bucket, outcomes, after = item
                weights = np.fromiter((float(row[f"repwgt{i}"]) for i in range(1, REPLICATES + 1)),
                                      dtype=np.float64, count=REPLICATES)
                for outcome, is_valid in outcomes.items():
                    if not is_valid:
                        continue
                    rep_den[(bucket, outcome)] += weights
                    positive = (
                        after[outcome] in {"2", "3"} if outcome == "RFOODS"
                        else after["EAWBMORT"] == "1" and after["EAWBGAS"] == "1"
                        if outcome == COMPOUND_OUTCOME else after[outcome] == "1"
                    )
                    if positive:
                        rep_num[(bucket, outcome)] += weights

    results = {}
    for transition_name, labels in labels_by_transition.items():
        results[transition_name] = {}
        for code, reason_label in labels.items():
            results[transition_name][code] = {"reason": reason_label}
            for outcome in outcome_names:
                bucket = (transition_name, code)
                results[transition_name][code][outcome] = summarize(
                    full_num[(bucket, outcome)], full_den[(bucket, outcome)],
                    rep_num[(bucket, outcome)], rep_den[(bucket, outcome)],
                    records[(bucket, outcome)])

    result = {
        "format": "us-sipp-snap-reason-outcome-fay-brr-v1",
        "source_unit": "identified person, adjacent reference-month transition pair",
        "transition": "SNAP receipt in month t -> month t+1",
        "reason": "recorded transition reason from the relevant SIPP month",
        "outcome": "valid following-month rent/mortgage, utility, or low/very-low food-security report",
        "weight": "WPFINWGT from month t; REPWGT1-REPWGT240 for variance",
        "variance_method": "Fay BRR, G=240, perturbation factor 0.5",
        "rows_read": rows_read,
        "replicate_rows_read": replicate_rows_read,
        "classified_transition_pairs_matched": matched,
        "all_transition_pairs": dict(all_transitions),
        "classified_transition_pairs": dict(classified_transitions),
        "results": results,
        "causal_estimation": False,
        "boundary": "Reason categories and following-month hardship/food-security measures are observed in an adjacent-month record but do not establish notice, effort, benefit amount, remedy, or program impact. RFOODS=2/3 is treated as low or very low food security; it is not a measure of hunger caused by the transition.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
