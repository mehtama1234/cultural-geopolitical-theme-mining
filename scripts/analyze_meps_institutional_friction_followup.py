#!/usr/bin/env python3
"""Estimate MEPS round-to-round outcomes by reported institutional friction."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pyreadstat


FLAGS = [f"BRR{i}" for i in range(1, 129)]


def share(mask: np.ndarray, outcome: np.ndarray, weight: np.ndarray, brr) -> dict:
    valid = mask & np.isfinite(outcome) & np.isfinite(weight) & (weight > 0)
    w = weight[valid]
    y = outcome[valid]
    point = float((w * y).sum() / w.sum())
    replicates = []
    for flag in FLAGS:
        rw = w * 2 * brr.loc[valid, flag].to_numpy(float)
        replicates.append(float((rw * y).sum() / rw.sum()))
    se = float(np.sqrt(np.mean((np.asarray(replicates) - point) ** 2)))
    return {
        "valid_records": int(valid.sum()),
        "estimate_percent": 100 * point,
        "brr_se_percentage_points": 100 * se,
        "ci95_percent": [
            max(0, 100 * point - 1.96 * 100 * se),
            min(100, 100 * point + 1.96 * 100 * se),
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    columns = [
        "DUPERSID", "PANEL", "EQDENY53", "RTHLTH42", "RTHLTH53",
        "EMPST42", "EMPST53", "PERWT24F",
    ]
    hc, _ = pyreadstat.read_dta(args.hc256_file, usecols=columns)
    brr, _ = pyreadstat.read_dta(
        args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS]
    )
    hc["KEY"] = hc["DUPERSID"].astype(str) + "|" + hc["PANEL"].astype(str)
    brr["KEY"] = (
        brr["DUPERSID"].astype(str)
        + "|"
        + brr["PANEL"].round().astype(int).astype(str)
    )
    data = hc.merge(
        brr[["KEY", *FLAGS]], on="KEY", how="left", validate="one_to_one"
    )
    if data["BRR1"].isna().any():
        raise ValueError("missing BRR person link")

    denial = data["EQDENY53"].to_numpy(float)
    before_health = data["RTHLTH42"].to_numpy(float)
    after_health = data["RTHLTH53"].to_numpy(float)
    before_employment = data["EMPST42"].to_numpy(float)
    after_employment = data["EMPST53"].to_numpy(float)
    weight = data["PERWT24F"].to_numpy(float)

    health_valid = (
        (before_health >= 1) & (before_health <= 5)
        & (after_health >= 1) & (after_health <= 5)
    )
    health_direction = np.full(len(data), np.nan)
    health_direction[health_valid] = np.where(
        after_health[health_valid] < before_health[health_valid], 1,
        np.where(after_health[health_valid] > before_health[health_valid], 2, 3),
    )

    employment_valid = np.isin(before_employment, [1, 2, 3, 4]) & np.isin(
        after_employment, [1, 2, 3, 4]
    )
    employed_before = before_employment == 1
    employed_after = after_employment == 1
    employment_valid &= np.isfinite(before_employment) & np.isfinite(after_employment)

    output = {
        "format": "us-meps-institutional-friction-followup-v1",
        "source_unit": (
            "MEPS 2024 HC-256 person with reported round-5/3 insurance "
            "denial or prior-approval delay and round-4/2 to round-5/3 endpoints"
        ),
        "variance_method": "standard BRR; replicate weight = BRR flag * 2 * PERWT24F",
        "hc256_records": len(data),
        "results": {},
    }
    for group, code in (("denial_or_delay_yes", 1), ("denial_or_delay_no", 2)):
        group_mask = denial == code
        output["results"][group] = {
            "health_improved": share(group_mask & health_valid, health_direction == 1, weight, data),
            "health_worsened": share(group_mask & health_valid, health_direction == 2, weight, data),
            "health_unchanged": share(group_mask & health_valid, health_direction == 3, weight, data),
            "employed_in_both_rounds": share(
                group_mask & employment_valid, employed_before & employed_after, weight, data
            ),
            "employed_to_not_employed": share(
                group_mask & employment_valid, employed_before & ~employed_after, weight, data
            ),
            "not_employed_to_employed": share(
                group_mask & employment_valid, ~employed_before & employed_after, weight, data
            ),
        }
        output["results"][group]["health_direction_by_baseline_health"] = {}
        for stratum, baseline_mask in (
            ("good_or_better_baseline", (before_health >= 1) & (before_health <= 3)),
            ("fair_or_poor_baseline", (before_health >= 4) & (before_health <= 5)),
        ):
            output["results"][group]["health_direction_by_baseline_health"][stratum] = {
                "health_improved": share(
                    group_mask & health_valid & baseline_mask,
                    health_direction == 1, weight, data
                ),
                "health_worsened": share(
                    group_mask & health_valid & baseline_mask,
                    health_direction == 2, weight, data
                ),
                "health_unchanged": share(
                    group_mask & health_valid & baseline_mask,
                    health_direction == 3, weight, data
                ),
            }
    output["boundary"] = (
        "This is a weighted longitudinal association, not a causal denial effect. "
        "EQDENY53 is a round-5/3 report without a claim identifier, decision date, "
        "appeal, remedy, or exact treatment episode; the round-4/2 values are a "
        "prior reference but may not predate the denial itself. Underlying "
        "need, severity, coverage, access, and selection can explain the transitions. "
        "The screen does not observe adherence, household substitution, recovery "
        "from a specific bill, trust, or political action."
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
