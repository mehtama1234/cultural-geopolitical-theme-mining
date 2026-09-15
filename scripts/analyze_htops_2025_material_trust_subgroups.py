#!/usr/bin/env python3
"""Estimate bounded subgroup cross-lags in the linked 2025 HTOPS panel.

The output is intentionally a descriptive retained-panel diagnostic: April
expense difficulty is the exposure, June Congress confidence is the outcome,
and April PWEIGHT plus the 80 April replicate weights are used.  No
attrition-adjusted population estimator is implied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def weighted_share(frame: pd.DataFrame, value: pd.Series, weight: pd.Series) -> tuple[float, int]:
    ok = value.notna() & weight.notna() & (weight > 0)
    if not ok.any():
        return float("nan"), 0
    w = weight[ok].to_numpy(dtype=float)
    y = value[ok].to_numpy(dtype=float)
    return float((w * y).sum() / w.sum() * 100), int(ok.sum())


def estimate(frame: pd.DataFrame, group: str, pressure: int) -> dict:
    sub = frame[(frame["group"] == group) & (frame["pressure"] == pressure)].copy()
    share, n = weighted_share(sub, sub["high_confidence"], sub["PWEIGHT0"])
    reps = []
    for c in [f"PWEIGHT{i}" for i in range(1, 81)]:
        if c not in sub:
            continue
        v, _ = weighted_share(sub, sub["high_confidence"], sub[c])
        reps.append(v)
    # Successive-difference replicate variance, reported as a conditional
    # precision diagnostic for the retained linked sample.
    se = float(np.sqrt(np.nansum((np.asarray(reps) - share) ** 2) / 80.0)) if reps else None
    return {
        "weighted_share": round(share, 4) if np.isfinite(share) else None,
        "standard_error": round(se, 4) if se is not None and np.isfinite(se) else None,
        "unweighted_n": n,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True, type=Path)
    ap.add_argument("--followup", required=True, type=Path)
    ap.add_argument("--replicates", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    cols = ["SCRAMID", "EXPNS_DIF", "TRUST2_CONGRESS", "RFAM_INCOME", "RRACETH1"]
    base = pd.read_csv(args.baseline, usecols=cols)
    follow = pd.read_csv(args.followup, usecols=["SCRAMID", "TRUST2_CONGRESS"])
    reps = pd.read_csv(args.replicates)
    weight_cols = [c for c in reps.columns if c.startswith("PWEIGHT")]
    if "PWEIGHT0" not in weight_cols or len(weight_cols) < 81:
        raise SystemExit(f"expected PWEIGHT0 plus 80 replicates, found {len(weight_cols)}")
    reps = reps[["SCRAMID", *weight_cols]]

    d = base.merge(follow, on="SCRAMID", how="inner", suffixes=("_apr", "_jun"))
    d = d.merge(reps, on="SCRAMID", how="inner")
    d["pressure"] = d["EXPNS_DIF"].where(d["EXPNS_DIF"].isin([1, 2, 3, 4]))
    d["pressure"] = d["pressure"].map({1: 0, 2: 1, 3: 1, 4: 1})
    d["high_confidence"] = d["TRUST2_CONGRESS_jun"].map({1: 1, 2: 1, 3: 0, 4: 0})

    income = {
        1: "under_25k", 2: "25k_34k", 3: "35k_49k", 4: "50k_74k",
        5: "75k_99k", 6: "100k_149k", 7: "150k_plus",
    }
    race = {1: "white_alone", 2: "hispanic", 3: "black_alone", 4: "asian_alone", 5: "other"}
    outputs = []
    for var, mapping in [("RFAM_INCOME", income), ("RRACETH1", race)]:
        for code, label in mapping.items():
            d["group"] = d[var].map({code: label})
            for pressure, pressure_label in [(0, "not_difficult"), (1, "any_difficulty")]:
                est = estimate(d, label, pressure)
                if est["unweighted_n"]:
                    outputs.append({"dimension": var, "group": label, "baseline_expense": pressure_label, **est})

    result = {
        "format": "htops-2025-material-trust-subgroup-audit-v1",
        "period": "April 15–29 to June 16–25, 2025",
        "linked_ids": int(len(d)),
        "weight": "April PWEIGHT0 and 80 April successive-difference replicate weights among linked respondents",
        "outcome": "June TRUST2_CONGRESS: high confidence = a great deal or quite a lot",
        "exposure": "April EXPNS_DIF: any difficulty = a little, somewhat, or very difficult",
        "estimates": outputs,
        "input_sha256": {
            "baseline_topical": f"sha256:{sha256(args.baseline)}",
            "followup_topical": f"sha256:{sha256(args.followup)}",
            "baseline_replicates": f"sha256:{sha256(args.replicates)}",
        },
        "boundary": "Subgroup cross-lags are descriptive among the selected linked panel. April weights are not documented as attrition-adjusted longitudinal weights; results do not establish that expense difficulty caused confidence, identify attribution, or measure civic/political action.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"linked_ids": len(d), "estimates": len(outputs), "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
