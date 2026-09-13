#!/usr/bin/env python3
"""Summarize documented SIPP SNAP start and end reasons.

The file contains one row per person-month. Start and end reasons are defined
for the person who owns the SNAP benefit, so the analysis restricts each reason
to ``ESNAP_OWN == PNUM`` and a valid reason status flag. Results are weighted
descriptive distributions, not causal estimates.
"""

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


def band(value: str) -> str:
    try:
        ratio = float(value)
    except (TypeError, ValueError):
        return "unknown"
    if ratio < 1:
        return "below_1x"
    if ratio < 2:
        return "1_to_2x"
    if ratio < 4:
        return "2_to_4x"
    return "4x_or_more"


def valid_status(value: str) -> bool:
    return value not in {"", "0"}


def add(counter: Counter[str], weights: dict[str, float], code: str, weight: float) -> None:
    counter[code] += 1
    weights[code] += weight


def summarize(counter: Counter[str], weights: dict[str, float], labels: dict[str, str]) -> dict:
    total = sum(weights.values())
    return {
        "records": sum(counter.values()),
        "weight": total,
        "reasons": {
            code: {
                "label": labels.get(code, "unknown"),
                "records": counter[code],
                "weight": weights[code],
                "share_percent": 100 * weights[code] / total if total else None,
            }
            for code in sorted(counter)
        },
    }


def analyze(path: Path) -> dict:
    required = {
        "PNUM", "WPFINWGT", "THINCPOV", "ESNAP_OWN", "ASNAP_OWN",
        "ESNAP_BRSN", "ASNAP_BRSN", "ESNAP_ERSN", "ASNAP_ERSN",
    }
    starts: Counter[str] = Counter()
    start_weights: dict[str, float] = defaultdict(float)
    ends: Counter[str] = Counter()
    end_weights: dict[str, float] = defaultdict(float)
    by_band = defaultdict(lambda: {"start": Counter(), "start_weight": defaultdict(float),
                                    "end": Counter(), "end_weight": defaultdict(float)})
    rows_read = 0
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError("slice is missing fields: " + ", ".join(missing))
        for row in reader:
            rows_read += 1
            try:
                weight = float(row["WPFINWGT"])
            except (TypeError, ValueError):
                continue
            if weight <= 0 or row.get("ESNAP_OWN", "") != row.get("PNUM", ""):
                continue
            resource_band = band(row.get("THINCPOV", ""))
            if valid_status(row.get("ASNAP_BRSN", "")) and row.get("ESNAP_BRSN", "") in START_REASONS:
                code = row["ESNAP_BRSN"]
                add(starts, start_weights, code, weight)
                add(by_band[resource_band]["start"], by_band[resource_band]["start_weight"], code, weight)
            if valid_status(row.get("ASNAP_ERSN", "")) and row.get("ESNAP_ERSN", "") in END_REASONS:
                code = row["ESNAP_ERSN"]
                add(ends, end_weights, code, weight)
                add(by_band[resource_band]["end"], by_band[resource_band]["end_weight"], code, weight)
    return {
        "format": "us-sipp-snap-reason-distributions-v1",
        "source_unit": "SNAP-owning person-month record",
        "weight": "WPFINWGT",
        "rows_read": rows_read,
        "start_reasons": summarize(starts, start_weights, START_REASONS),
        "end_reasons": summarize(ends, end_weights, END_REASONS),
        "by_resource_band": {
            resource: {
                "start_reasons": summarize(values["start"], values["start_weight"], START_REASONS),
                "end_reasons": summarize(values["end"], values["end_weight"], END_REASONS),
            }
            for resource, values in sorted(by_band.items())
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
