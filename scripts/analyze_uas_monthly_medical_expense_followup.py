#!/usr/bin/env python3
"""Analyze a bounded UAS monthly medical-expense shock follow-up.

This is a descriptive transition screen.  It uses the next observed UAS wave
after a row reporting ``fin3s4`` and never presents the result as causal.  The
script requires the documented monthly-panel fields and records the actual
input hash and valid universes in its output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pyreadstat


REQUIRED = ["uasid", "wave", "final_weight", "fin3s4"]
OUTCOMES = {
    "health": "le_hrs_srh1",
    "life_satisfaction": "le_hrs_s1",
    "pain": "le_hrs_p1",
    "meaning": "meaningthetas_tscore_3_",
}
OPTIONAL_TIMING = [
    "fin1_when_month",
    "fin1_when_day",
    "fin1_when_year",
    "fin1_when_befores1",
]


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_file(path: Path, columns: list[str]) -> tuple[pd.DataFrame, dict[str, Any]]:
    if path.suffix.lower() in {".dta", ".tab"}:
        frame, meta = pyreadstat.read_dta(path, usecols=columns, encoding="latin1")
        labels = meta.variable_value_labels.get("fin3s4", {})
    else:
        frame = pd.read_csv(path, usecols=columns)
        labels = {}
    return frame, {"fin3s4_value_labels": labels}


def weighted_mean(values: pd.Series, weights: pd.Series) -> float | None:
    valid = values.notna() & weights.gt(0)
    if not valid.any():
        return None
    return float(np.average(values[valid].astype(float), weights=weights[valid]))


def summarize(frame: pd.DataFrame, mask: pd.Series, outcome: str) -> dict[str, Any]:
    weights = pd.to_numeric(frame["final_weight"], errors="coerce")
    values = pd.to_numeric(frame[outcome], errors="coerce")
    valid = mask & weights.gt(0) & values.notna()
    return {
        "valid_records": int(valid.sum()),
        "weighted_denominator": float(weights[valid].sum()) if valid.any() else 0.0,
        "weighted_mean": weighted_mean(values[valid], weights[valid]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("monthly_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    requested = REQUIRED + OPTIONAL_TIMING + list(OUTCOMES.values())
    # Keep only fields that exist so an older release can still report a
    # transparent partial outcome inventory; the four structural fields remain
    # mandatory below.
    if args.monthly_file.suffix.lower() in {".dta", ".tab"}:
        _, metadata = pyreadstat.read_dta(args.monthly_file, metadataonly=True, encoding="latin1")
        available = set(metadata.column_names)
    else:
        available = set(pd.read_csv(args.monthly_file, nrows=0).columns)
    missing = [field for field in REQUIRED if field not in available]
    if missing:
        parser.error("missing required UAS fields: " + ", ".join(missing))
    columns = [field for field in requested if field in available]
    frame, metadata_info = read_file(args.monthly_file, columns)
    if frame["uasid"].isna().any():
        parser.error("uasid contains missing values; cannot establish respondent continuity")
    frame["_wave_num"] = pd.to_numeric(frame["wave"], errors="coerce")
    if frame["_wave_num"].isna().any():
        parser.error("wave contains missing or nonnumeric values; cannot order follow-up")
    duplicate_key = frame.duplicated(subset=["uasid", "_wave_num"], keep=False)
    if duplicate_key.any():
        parser.error(
            "duplicate uasid-wave rows detected after numeric normalization; resolve "
            "respondent-wave uniqueness "
            f"before running a longitudinal follow-up ({int(duplicate_key.sum())} rows)"
        )
    frame["_weight"] = pd.to_numeric(frame["final_weight"], errors="coerce")
    frame = frame.sort_values(["uasid", "_wave_num"], kind="stable").reset_index(drop=True)
    frame["_next_wave"] = frame.groupby("uasid", sort=False)["_wave_num"].shift(-1)
    for outcome in OUTCOMES.values():
        if outcome in frame:
            frame[f"_next_{outcome}"] = frame.groupby("uasid", sort=False)[outcome].shift(-1)

    # UAS yes/no fields conventionally use 1/2.  Do not silently recode other
    # values: retain the observed labels and expose the codes in the output.
    exposure = pd.to_numeric(frame["fin3s4"], errors="coerce")
    eligible = exposure.isin([1, 2]) & frame["_weight"].gt(0) & frame["_next_wave"].gt(frame["_wave_num"])
    shock = eligible & exposure.eq(1)
    comparison = eligible & exposure.eq(2)
    outcomes: dict[str, Any] = {}
    for label, field in OUTCOMES.items():
        if field not in frame:
            outcomes[label] = {"field": field, "status": "not_present"}
            continue
        follow = f"_next_{field}"
        outcomes[label] = {
            "field": field,
            "followup_field": follow,
            "shock": summarize(frame.assign(**{field: frame[follow]}), shock, field),
            "no_medical_expense_shock": summarize(frame.assign(**{field: frame[follow]}), comparison, field),
            "baseline": {
                "shock": summarize(frame, shock, field),
                "no_medical_expense_shock": summarize(frame, comparison, field),
            },
        }
    timing = {
        field: {
            "present": field in frame,
            "valid_records": int(frame.loc[eligible, field].notna().sum()) if field in frame else 0,
        }
        for field in OPTIONAL_TIMING
    }
    output = {
        "schema": "uas-monthly-medical-expense-followup-v1",
        "method": "Rows reporting fin3s4=1 are compared with fin3s4=2 rows whose next observed wave is later; outcomes are measured on that next wave. Weighted means use final_weight. No design-based uncertainty or causal estimate is produced.",
        "input": {"path": str(args.monthly_file), "bytes": args.monthly_file.stat().st_size, "sha256": file_hash(args.monthly_file)},
        "metadata": metadata_info,
        "records": {
            "rows": int(len(frame)),
            "unique_persons": int(frame["uasid"].nunique(dropna=True)),
            "unique_waves": int(frame["_wave_num"].nunique(dropna=True)),
            "eligible_exposure_followup_rows": int(eligible.sum()),
            "medical_expense_shock_rows": int(shock.sum()),
            "comparison_rows": int(comparison.sum()),
            "exposure_codes_observed": sorted(str(value) for value in exposure.dropna().unique()),
        },
        "timing_fields": timing,
        "outcomes": outcomes,
        "limitation": "fin3s4 is a reported medical/dental expense component of a financial shock, not a linked bill or treatment event. Next-wave follow-up is temporally ordered at wave level, but exposure timing, care choice, remedy, selection, attrition, and unmeasured confounding remain unresolved. final_weight is used for descriptive means; no Taylor/replicate design variance is claimed.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
