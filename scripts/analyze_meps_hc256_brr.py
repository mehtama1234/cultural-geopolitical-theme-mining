#!/usr/bin/env python3
"""Compute bounded HC-256 weighted means with standard HC-036BRR variance."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pyreadstat


FLAGS = [f"BRR{i}" for i in range(1, 129)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    args = parser.parse_args()
    hc, _ = pyreadstat.read_dta(
        args.hc256_file,
        usecols=["DUPERSID", "PANEL", "PERWT24F", "TOTEXP24", "TOTSLF24"],
    )
    brr, _ = pyreadstat.read_dta(
        args.brr_file,
        usecols=["DUPERSID", "PANEL", *FLAGS],
    )
    hc["PANELKEY"] = hc["PANEL"].astype(str)
    brr["PANELKEY"] = brr["PANEL"].round().astype(int).astype(str)
    hc["KEY"] = hc["DUPERSID"].astype(str) + "|" + hc["PANELKEY"]
    brr["KEY"] = brr["DUPERSID"].astype(str) + "|" + brr["PANELKEY"]
    merged = hc.merge(brr, on="KEY", how="left", validate="one_to_one")
    if int(merged["BRR1"].isna().sum()):
        raise SystemExit("HC-256 to HC-036BRR merge has missing flags")
    weights = merged["PERWT24F"].to_numpy(float)
    output: dict[str, object] = {
        "hc256_records": len(hc),
        "brr_flags": len(FLAGS),
        "linked_records": len(merged),
        "method": "standard BRR: replicate weight = BRR flag * 2 * PERWT24F; variance = mean squared replicate deviations",
        "estimates": {},
    }
    for field in ["TOTEXP24", "TOTSLF24"]:
        values = merged[field].to_numpy(float)
        valid = np.isfinite(weights) & (weights > 0) & np.isfinite(values)
        point = float(np.sum(values[valid] * weights[valid]) / np.sum(weights[valid]))
        replicates = []
        for flag in FLAGS:
            replicate_weights = weights[valid] * 2 * merged.loc[valid, flag].to_numpy(float)
            replicates.append(float(np.sum(values[valid] * replicate_weights) / np.sum(replicate_weights)))
        se = float(np.sqrt(np.mean((np.asarray(replicates) - point) ** 2)))
        output["estimates"][field] = {
            "valid_records": int(valid.sum()),
            "mean": point,
            "brr_standard_error": se,
            "ci95_low": point - 1.96 * se,
            "ci95_high": point + 1.96 * se,
        }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
