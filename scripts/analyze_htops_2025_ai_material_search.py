#!/usr/bin/env python3
"""Screen household expense difficulty against AI use, trust, and material searches.

This is a weighted, same-round HTOPS 2506 description.  It preserves the
respondent unit, the household-reported expense condition, and the 80 public
replicate weights.  It is not a causal or longitudinal estimate.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import pandas as pd


GROUPS = (1, 2, 3, 4)
OUTCOMES = {
    "any_ai_use": None,
    "factual_information": ["AI1_1"],
    "work_projects": ["AI1_3"],
    "housing_search": ["AI4_1"],
    "job_search": ["AI4_2"],
    "food_search": ["AI4_4"],
    "medical_search": ["AI4_5"],
    "public_benefit_search": ["AI4_6"],
    "credit_search": ["AI4_8"],
    "trust_ai_information": ["AI2_5"],
    "actively_opted_out": ["AI3"],
}


AI_SELECTIONS = ["AI1_1", "AI1_2", "AI1_3", "AI1_4", "AI1_5", "AI1_6", "AI1_7", "AI1_9"]


def positive(frame: pd.DataFrame, name: str, fields: list[str] | None) -> pd.Series:
    if name == "any_ai_use":
        return frame[AI_SELECTIONS].apply(pd.to_numeric, errors="coerce").eq(1).any(axis=1)
    values = frame[fields].apply(pd.to_numeric, errors="coerce")
    return values.iloc[:, 0].eq(1) if len(fields) == 1 else values.eq(1).any(axis=1)


def valid(frame: pd.DataFrame, name: str, fields: list[str] | None) -> pd.Series:
    numeric = frame.apply(pd.to_numeric, errors="coerce")
    if name == "any_ai_use":
        # AI1_8=1 is the explicit no-use route.  -99 means a seen but
        # unselected checkbox; -88 is missing and cannot establish a zero.
        active_seen = numeric[AI_SELECTIONS].isin([1, -99]).any(axis=1)
        no_use_seen = numeric["AI1_8"].isin([1, -99])
        return active_seen | no_use_seen
    if name == "trust_ai_information":
        ai_user = positive(frame, "any_ai_use", None)
        return ai_user & numeric["AI2_5"].isin([1, -99])
    if name == "actively_opted_out":
        return numeric["AI3"].isin([1, 2, 3])
    return numeric[fields[0]].isin([1, -99])


def estimate(frame: pd.DataFrame, group: int, name: str, fields: list[str] | None, rep_cols: list[str]) -> dict[str, float | int | None]:
    group_mask = frame["EXPNS_DIF"].eq(group)
    valid_mask = group_mask & valid(frame, name, fields)
    if not valid_mask.any():
        return {"unweighted_n": 0, "weighted_valid": 0, "estimate_pct": None, "se_pct_points": None}
    weights = pd.to_numeric(frame.loc[valid_mask, "PWEIGHT"], errors="coerce")
    values = positive(frame.loc[valid_mask], name, fields).astype(float)
    usable = weights.gt(0) & weights.notna()
    weights = weights[usable]
    values = values[usable]
    if weights.empty:
        return {"unweighted_n": 0, "weighted_valid": 0, "estimate_pct": None, "se_pct_points": None}
    point = float((weights * values).sum() / weights.sum() * 100)
    reps: list[float] = []
    for col in rep_cols:
        rw = pd.to_numeric(frame.loc[weights.index, col], errors="coerce")
        keep = rw.gt(0) & rw.notna()
        reps.append(float((rw[keep] * values[keep]).sum() / rw[keep].sum() * 100) if keep.any() else math.nan)
    finite = [x for x in reps if math.isfinite(x)]
    se = math.sqrt(sum((x - point) ** 2 for x in finite) / len(rep_cols)) if finite else math.nan
    return {
        "unweighted_n": int(len(values)),
        "weighted_valid": round(float(weights.sum())),
        "estimate_pct": round(point, 3),
        "se_pct_points": round(se, 3) if math.isfinite(se) else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--puf", type=Path, required=True)
    parser.add_argument("--replicate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    puf = pd.read_csv(args.puf)
    rep = pd.read_csv(args.replicate)
    required = {"SCRAMID", "EXPNS_DIF", "PWEIGHT", "AI1_8"} | {field for fields in OUTCOMES.values() if fields for field in fields}
    missing = sorted(required - set(puf.columns))
    if missing:
        raise SystemExit(f"PUF missing fields: {missing}")
    rep_cols = [f"PWEIGHT{i}" for i in range(1, 81)]
    missing_rep = sorted(set(["SCRAMID", "PWEIGHT0", *rep_cols]) - set(rep.columns))
    if missing_rep:
        raise SystemExit(f"replicate file missing fields: {missing_rep}")
    if puf["SCRAMID"].duplicated().any() or rep["SCRAMID"].duplicated().any():
        raise SystemExit("duplicate SCRAMID in PUF or replicate file")
    if set(puf["SCRAMID"]) != set(rep["SCRAMID"]):
        raise SystemExit("PUF and replicate SCRAMID sets differ")
    merged = puf.merge(rep[["SCRAMID", "PWEIGHT0", *rep_cols]], on="SCRAMID", how="inner", validate="one_to_one")
    max_weight_difference = float((pd.to_numeric(merged["PWEIGHT"], errors="coerce") - pd.to_numeric(merged["PWEIGHT0"], errors="coerce")).abs().max())
    valid_groups = merged["EXPNS_DIF"].isin(GROUPS) & pd.to_numeric(merged["PWEIGHT"], errors="coerce").gt(0)
    estimates = {
        str(group): {name: estimate(merged.loc[valid_groups], group, name, fields, rep_cols) for name, fields in OUTCOMES.items()}
        for group in GROUPS
    }
    result = {
        "format": "htops-2025-ai-material-search-screen-v1",
        "field_window": "June 2025 HTOPS/HPS 2506 topical file",
        "unit": "responding person, conditioned on household-reported expense difficulty",
        "puf_rows": int(len(puf)),
        "replicate_rows": int(len(rep)),
        "valid_weighted_rows": int(valid_groups.sum()),
        "alignment": {"puf_replicate_id_match": True, "max_abs_pweight_difference": max_weight_difference},
        "weight": "PWEIGHT with PWEIGHT1-PWEIGHT80 successive-difference replicate weights",
        "estimates": estimates,
        "interpretation": "Same-round weighted conditional shares. AI and search fields describe respondent/household reports; expense difficulty is household-reported. No causal, longitudinal, or event-level interpretation is permitted.",
        "boundary": "The file does not identify a specific bill, actor, search result, alternative, remedy, outcome, or later trust/action change. AI use, trust, opt-out, and material search should remain separate constructs.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "valid_weighted_rows": result["valid_weighted_rows"]}, indent=2))


if __name__ == "__main__":
    main()
