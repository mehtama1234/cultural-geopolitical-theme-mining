#!/usr/bin/env python3
"""Describe resource and job changes around monthly SIPP SNAP transitions."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


def resource(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def jobs(value: str) -> int | None:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def change(before, after) -> str:
    if before is None or after is None:
        return "unknown"
    if after > before:
        return "up"
    if after < before:
        return "down"
    return "same"


def summarize(counter: Counter[str], weights: dict[str, float]) -> dict:
    total = sum(weights.values())
    return {
        "records": sum(counter.values()),
        "weight": total,
        "shares": {key: {"records": counter[key], "weight": weights[key],
                          "share_percent": 100 * weights[key] / total if total else None}
                    for key in sorted(counter)},
    }


def analyze(path: Path) -> dict:
    required = {"SSUID", "SHHADID", "PNUM", "MONTHCODE", "WPFINWGT",
                "RSNAP_MNYN", "THINCPOV", "AHINCPOV", "RMNUMJOBS", "AMNUMJOBS"}
    people: dict[tuple[str, str, str], dict[int, dict[str, str]]] = defaultdict(dict)
    rows_read = 0
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                month = int(row["MONTHCODE"])
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if not 1 <= month <= 12 or weight <= 0:
                continue
            key = (row["SSUID"], row["SHHADID"], row["PNUM"])
            people[key][month] = {field: row.get(field, "") for field in required}

    by_transition = defaultdict(lambda: {
        "resource": Counter(), "resource_weight": defaultdict(float),
        "jobs": Counter(), "jobs_weight": defaultdict(float),
        "records": 0, "weight": 0.0,
    })
    transitions = Counter()
    transition_weights: dict[str, float] = defaultdict(float)
    for months in people.values():
        for month in range(1, 12):
            if month not in months or month + 1 not in months:
                continue
            first, second = months[month], months[month + 1]
            before, after = first.get("RSNAP_MNYN", ""), second.get("RSNAP_MNYN", "")
            if before not in {"1", "2"} or after not in {"1", "2"}:
                continue
            transition = f"{before} -> {after}"
            weight = float(first["WPFINWGT"])
            transitions[transition] += 1
            transition_weights[transition] += weight
            if transition not in {"2 -> 1", "1 -> 2"}:
                continue
            item = by_transition[transition]
            item["records"] += 1
            item["weight"] += weight
            resource_change = change(resource(first.get("THINCPOV", "")),
                                     resource(second.get("THINCPOV", "")))
            job_change = change(jobs(first.get("RMNUMJOBS", "")),
                                jobs(second.get("RMNUMJOBS", "")))
            item["resource"][resource_change] += 1
            item["resource_weight"][resource_change] += weight
            item["jobs"][job_change] += 1
            item["jobs_weight"][job_change] += weight

    return {
        "format": "us-sipp-snap-transition-context-v1",
        "source_unit": "identified person, adjacent reference-month pair",
        "weight": "WPFINWGT from first month of pair",
        "rows_read": rows_read,
        "identified_people": len(people),
        "transitions": {key: {"records": transitions[key], "weight": transition_weights[key]}
                        for key in sorted(transitions)},
        "context_by_transition": {
            key: {
                "records": value["records"], "weight": value["weight"],
                "resource_change": summarize(value["resource"], value["resource_weight"]),
                "job_change": summarize(value["jobs"], value["jobs_weight"]),
            }
            for key, value in sorted(by_transition.items())
        },
        "variance_estimation": False,
        "causal_estimation": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
