#!/usr/bin/env python3
"""Classify adjacent SIPP SNAP receipt transitions by recorded reasons."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

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


def distribution(counter: Counter[str], weights: dict[str, float], labels: dict[str, str]) -> dict:
    total = sum(weights.values())
    return {
        "records": sum(counter.values()),
        "weight": total,
        "reasons": {
            code: {"label": labels[code], "records": counter[code],
                   "weight": weights[code],
                   "share_percent": 100 * weights[code] / total if total else None}
            for code in sorted(counter)
        },
    }


def analyze(path: Path) -> dict:
    required = {"SSUID", "SHHADID", "PNUM", "MONTHCODE", "WPFINWGT",
                "RSNAP_MNYN", "ESNAP_BRSN", "ASNAP_BRSN", "ESNAP_ERSN", "ASNAP_ERSN"}
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

    transitions = Counter()
    transition_weights: dict[str, float] = defaultdict(float)
    start = Counter()
    start_weights: dict[str, float] = defaultdict(float)
    end = Counter()
    end_weights: dict[str, float] = defaultdict(float)
    reason_coverage = Counter()
    for months in people.values():
        for month in range(1, 12):
            if month not in months or month + 1 not in months:
                continue
            first, second = months[month], months[month + 1]
            before, after = first.get("RSNAP_MNYN", ""), second.get("RSNAP_MNYN", "")
            if before not in {"1", "2"} or after not in {"1", "2"}:
                continue
            transition = f"{before} -> {after}"
            try:
                weight = float(first["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            transitions[transition] += 1
            transition_weights[transition] += weight
            if transition == "2 -> 1":
                reason_coverage["entry_transition"] += 1
                code = second.get("ESNAP_BRSN", "")
                if second.get("ASNAP_BRSN", "") not in {"", "0"} and code in START_REASONS:
                    add = (start, start_weights)
                    add[0][code] += 1
                    add[1][code] += weight
                    reason_coverage["entry_with_reason"] += 1
            elif transition == "1 -> 2":
                reason_coverage["exit_transition"] += 1
                code = first.get("ESNAP_ERSN", "")
                if first.get("ASNAP_ERSN", "") not in {"", "0"} and code in END_REASONS:
                    end[code] += 1
                    end_weights[code] += weight
                    reason_coverage["exit_with_reason"] += 1

    return {
        "format": "us-sipp-snap-transition-reasons-v1",
        "source_unit": "identified person, adjacent reference-month pair",
        "weight": "WPFINWGT from first month of pair",
        "rows_read": rows_read,
        "identified_people": len(people),
        "transitions": {
            transition: {"records": transitions[transition], "weight": transition_weights[transition]}
            for transition in sorted(transitions)
        },
        "reason_coverage": dict(reason_coverage),
        "entry_reasons": distribution(start, start_weights, START_REASONS),
        "exit_reasons": distribution(end, end_weights, END_REASONS),
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
