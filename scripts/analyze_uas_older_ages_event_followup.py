#!/usr/bin/env python3
"""Run a bounded next-wave follow-up for the UAS Older Ages panel.

The Older Ages Monthly Events file records events occurring in the prior
calendar month and is organized by respondent and wave. This script compares
the next observed wave after a selected event with the next wave after no
selected event. It is descriptive only: it does not claim a bill-level,
clinical, causal, or recovery effect.
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


DEFAULT_OUTCOMES = {
    "health": "le_hrs_srh1",
    "life_satisfaction": "le_hrs_s1",
    "pain": "le_hrs_p1",
    "hours_worked": "le_hrs_ic_total",
    "earnings": "le_earn_m_full",
}


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def available_columns(path: Path) -> list[str]:
    if path.suffix.lower() in {".dta", ".tab"}:
        _, meta = pyreadstat.read_dta(path, metadataonly=True, encoding="latin1")
        return list(meta.column_names)
    return list(pd.read_csv(path, nrows=0).columns)


def read_columns(path: Path, columns: list[str]) -> pd.DataFrame:
    if path.suffix.lower() in {".dta", ".tab"}:
        frame, _ = pyreadstat.read_dta(path, usecols=columns, encoding="latin1")
        return frame
    return pd.read_csv(path, usecols=columns)


def weighted_mean(values: pd.Series, weights: pd.Series) -> float | None:
    valid = values.notna() & weights.gt(0)
    if not valid.any():
        return None
    return float(np.average(values[valid].astype(float), weights=weights[valid]))


def summarize(frame: pd.DataFrame, mask: pd.Series, field: str) -> dict[str, Any]:
    weights = pd.to_numeric(frame["_weight"], errors="coerce")
    values = pd.to_numeric(frame[field], errors="coerce")
    valid = mask & weights.gt(0) & values.notna()
    return {
        "valid_records": int(valid.sum()),
        "weighted_denominator": float(weights[valid].sum()) if valid.any() else 0.0,
        "weighted_mean": weighted_mean(values[valid], weights[valid]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("panel_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--event", default="le001", help="Event occurrence field; default is illness/injury (le001).")
    parser.add_argument("--event-date", default=None, help="Optional event-date field to report, e.g. le011_1_.")
    parser.add_argument("--event-positive", default="1", help="Code treated as event present; default 1.")
    parser.add_argument("--event-negative", default="2", help="Code treated as event absent; default 2.")
    args = parser.parse_args()

    required = ["uasid", "wave", "final_weight", args.event]
    available = set(available_columns(args.panel_file))
    missing = [field for field in required if field not in available]
    if missing:
        parser.error("missing required Older Ages fields: " + ", ".join(missing))
    outcomes = {label: field for label, field in DEFAULT_OUTCOMES.items() if field in available}
    optional = [field for field in [args.event_date] if field and field in available]
    columns = list(dict.fromkeys(required + list(outcomes.values()) + optional))
    frame = read_columns(args.panel_file, columns)

    if frame["uasid"].isna().any():
        parser.error("uasid contains missing values; respondent continuity is not auditable")
    frame["_wave_num"] = pd.to_numeric(frame["wave"], errors="coerce")
    if frame["_wave_num"].isna().any():
        parser.error("wave contains missing or nonnumeric values; cannot order follow-up")
    duplicate = frame.duplicated(subset=["uasid", "_wave_num"], keep=False)
    if duplicate.any():
        parser.error(
            "duplicate uasid-wave rows detected after numeric normalization; resolve "
            f"respondent-wave uniqueness ({int(duplicate.sum())} rows)"
        )
    frame["_weight"] = pd.to_numeric(frame["final_weight"], errors="coerce")
    frame = frame.sort_values(["uasid", "_wave_num"], kind="stable").reset_index(drop=True)
    frame["_next_wave"] = frame.groupby("uasid", sort=False)["_wave_num"].shift(-1)
    for field in outcomes.values():
        frame[f"_next_{field}"] = frame.groupby("uasid", sort=False)[field].shift(-1)

    event = pd.to_numeric(frame[args.event], errors="coerce")
    positive = event.eq(float(args.event_positive))
    negative = event.eq(float(args.event_negative))
    eligible = (positive | negative) & frame["_weight"].gt(0) & frame["_next_wave"].gt(frame["_wave_num"])
    positive_followup = eligible & positive
    negative_followup = eligible & negative

    outcome_results: dict[str, Any] = {}
    for label, field in outcomes.items():
        next_field = f"_next_{field}"
        outcome_frame = frame.assign(**{field: frame[next_field]})
        outcome_results[label] = {
            "field": field,
            "next_wave_event_present": summarize(outcome_frame, positive_followup, field),
            "next_wave_event_absent": summarize(outcome_frame, negative_followup, field),
        }

    timing = {
        field: {
            "present": field in frame,
            "valid_event_records": int(frame.loc[positive, field].notna().sum()) if field in frame else 0,
        }
        for field in optional
    }
    output = {
        "schema": "uas-older-ages-event-followup-v1",
        "method": "Event-present and event-absent rows are carried to the next observed respondent wave. Weighted means use final_weight. The Older Ages event refers to the preceding calendar month; no causal, clinical, bill-level, remedy, or recovery estimate is produced.",
        "input": {"path": str(args.panel_file), "bytes": args.panel_file.stat().st_size, "sha256": file_hash(args.panel_file)},
        "event": {"field": args.event, "positive_code": args.event_positive, "negative_code": args.event_negative},
        "records": {
            "rows": int(len(frame)),
            "unique_persons": int(frame["uasid"].nunique(dropna=True)),
            "unique_waves": int(frame["_wave_num"].nunique(dropna=True)),
            "eligible_event_followup_rows": int(eligible.sum()),
            "event_present_rows": int(positive_followup.sum()),
            "event_absent_rows": int(negative_followup.sum()),
            "event_codes_observed": sorted(str(value) for value in event.dropna().unique()),
        },
        "event_timing_fields": timing,
        "outcomes": outcome_results,
        "limitation": "This is a selected descriptive next-wave comparison. Event occurrence is reported for the prior calendar month, and the next wave is not a verified recovery interval. Confounding, attrition, missing codes, event-date precision, treatment continuity, alternatives, remedy, trust, political action, and exit remain open.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
