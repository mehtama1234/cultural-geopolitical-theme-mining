#!/usr/bin/env python3
"""Compare annual state BFS applications with same-year BDS dynamics.

This is a descriptive stage comparison. It is not a conversion or causal rate.
"""

from __future__ import annotations

import argparse
import csv
import statistics
from collections import defaultdict
from pathlib import Path


FIPS_TO_STATE = {
    "01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO",
    "09": "CT", "10": "DE", "11": "DC", "12": "FL", "13": "GA", "15": "HI",
    "16": "ID", "17": "IL", "18": "IN", "19": "IA", "20": "KS", "21": "KY",
    "22": "LA", "23": "ME", "24": "MD", "25": "MA", "26": "MI", "27": "MN",
    "28": "MS", "29": "MO", "30": "MT", "31": "NE", "32": "NV", "33": "NH",
    "34": "NJ", "35": "NM", "36": "NY", "37": "NC", "38": "ND", "39": "OH",
    "40": "OK", "41": "OR", "42": "PA", "44": "RI", "45": "SC", "46": "SD",
    "47": "TN", "48": "TX", "49": "UT", "50": "VT", "51": "VA", "53": "WA",
    "54": "WV", "55": "WI", "56": "WY",
}


def correlation(left: list[float], right: list[float]) -> float:
    left_mean = statistics.mean(left)
    right_mean = statistics.mean(right)
    numerator = sum((a - left_mean) * (b - right_mean) for a, b in zip(left, right))
    denominator = (sum((a - left_mean) ** 2 for a in left) * sum((b - right_mean) ** 2 for b in right)) ** 0.5
    return numerator / denominator


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bfs", type=Path, required=True)
    parser.add_argument("--bds", type=Path, required=True)
    parser.add_argument("--year", type=int, default=2023)
    args = parser.parse_args()

    applications: defaultdict[str, int] = defaultdict(int)
    with args.bfs.open(newline="") as handle:
        for row in csv.DictReader(handle):
            if int(row["Year"]) == args.year:
                applications[row["State"]] += int(row["BA_NSA"])

    dynamics = {}
    with args.bds.open(newline="") as handle:
        for row in csv.DictReader(handle):
            if int(row["year"]) == args.year and row["st"] in FIPS_TO_STATE:
                dynamics[FIPS_TO_STATE[row["st"]]] = row

    states = sorted(set(applications) & set(dynamics))
    normalized = [100 * applications[state] / int(dynamics[state]["estabs"]) for state in states]
    print(f"matched_states={len(states)}")
    print(f"median_applications_per_100_establishments={statistics.median(normalized):.3f}")
    for field in ("estabs_entry_rate", "estabs_exit_rate", "net_job_creation_rate", "reallocation_rate"):
        print(f"correlation_normalized_applications_{field}={correlation(normalized, [float(dynamics[state][field]) for state in states]):.3f}")
    for value, state in sorted(zip(normalized, states), reverse=True)[:5]:
        print(f"qa_high_normalized={state},applications_per_100_establishments={value:.2f}")


if __name__ == "__main__":
    main()
