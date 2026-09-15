#!/usr/bin/env python3
"""Compute bounded HC-256 subgroup means with standard HC-036BRR variance.

The script keeps the subgroup estimand explicit: each mean is among people in
the subgroup with a positive final person weight and a valid outcome field.
It is descriptive and is not a household-affordability or causal estimator.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pyreadstat


FLAGS = [f"BRR{i}" for i in range(1, 129)]
GROUPS = {
    "POVCAT24": {
        1: "poor_or_negative",
        2: "near_poor",
        3: "low_income",
        4: "middle_income",
        5: "high_income",
    },
    "INSURC24": {
        1: "under65_private",
        2: "under65_public_only",
        3: "under65_uninsured",
        4: "65plus_medicare_only",
        5: "65plus_medicare_private",
        6: "65plus_medicare_other_public",
        7: "65plus_uninsured",
        8: "65plus_no_medicare_any_coverage",
    },
}


def estimate(merged, field: str, group_field: str, group_code: int) -> dict[str, float | int]:
    weights = merged["PERWT24F"].to_numpy(float)
    values = merged[field].to_numpy(float)
    groups = merged[group_field].to_numpy(float)
    valid = np.isfinite(weights) & (weights > 0) & np.isfinite(values) & (groups == group_code)
    if not int(valid.sum()):
        return {"valid_records": 0, "mean": None, "brr_standard_error": None, "ci95_low": None, "ci95_high": None}
    point = float(np.sum(values[valid] * weights[valid]) / np.sum(weights[valid]))
    replicates = []
    for flag in FLAGS:
        replicate_weights = weights[valid] * 2 * merged.loc[valid, flag].to_numpy(float)
        replicates.append(float(np.sum(values[valid] * replicate_weights) / np.sum(replicate_weights)))
    se = float(np.sqrt(np.mean((np.asarray(replicates) - point) ** 2)))
    return {
        "valid_records": int(valid.sum()),
        "mean": point,
        "brr_standard_error": se,
        "ci95_low": point - 1.96 * se,
        "ci95_high": point + 1.96 * se,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    args = parser.parse_args()
    fields = ["DUPERSID", "PANEL", "PERWT24F", "TOTEXP24", "TOTSLF24", *GROUPS]
    hc, _ = pyreadstat.read_dta(args.hc256_file, usecols=fields)
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS])
    hc["PANELKEY"] = hc["PANEL"].astype(str)
    brr["PANELKEY"] = brr["PANEL"].round().astype(int).astype(str)
    hc["KEY"] = hc["DUPERSID"].astype(str) + "|" + hc["PANELKEY"]
    brr["KEY"] = brr["DUPERSID"].astype(str) + "|" + brr["PANELKEY"]
    merged = hc.merge(brr, on="KEY", how="left", validate="one_to_one")
    if int(merged["BRR1"].isna().sum()):
        raise SystemExit("HC-256 to HC-036BRR merge has missing flags")
    output: dict[str, object] = {
        "hc256_records": len(hc),
        "linked_records": len(merged),
        "brr_flags": len(FLAGS),
        "method": "standard BRR: replicate weight = BRR flag * 2 * PERWT24F; subgroup means normalize within each subgroup",
        "groups": {},
    }
    for group_field, labels in GROUPS.items():
        group_output = {}
        for code, label in labels.items():
            group_output[label] = {
                "code": code,
                "measures": {
                    field: estimate(merged, field, group_field, code)
                    for field in ["TOTEXP24", "TOTSLF24"]
                },
            }
        output["groups"][group_field] = group_output
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
