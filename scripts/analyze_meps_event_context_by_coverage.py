#!/usr/bin/env python3
"""Estimate MEPS event/context associations within under-65 coverage groups."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


FLAGS = [f"BRR{i}" for i in range(1, 129)]
EVENTS = {"office": "OBTOTV24", "emergency_room": "ERTOT24", "inpatient": "IPDIS24"}
COVERAGE = {1: "under65_private", 2: "under65_public_only", 3: "under65_uninsured"}
OUTCOMES = {
    "medical_bill_problem": ("PROBPY42", lambda s: s == 1, [1, 2]),
    "fair_or_poor_perceived_health": ("RTHLTH53", lambda s: s >= 4, [1, 2, 3, 4, 5]),
    "not_employed_round_5_3": ("EMPST53", lambda s: s == 4, [1, 2, 3, 4]),
}


def estimate(frame: pd.DataFrame, mask: pd.Series, outcome_field: str, outcome_fn, valid_codes: list[int]) -> dict[str, float | int | None]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = mask & weights.gt(0) & frame[outcome_field].isin(valid_codes)
    if not valid.any():
        return {"valid_records": 0, "share_percent": None, "brr_se_percentage_points": None, "ci95_low": None, "ci95_high": None}
    values = outcome_fn(frame[outcome_field]).astype(float)
    point = float(np.average(values[valid], weights=weights[valid]) * 100)
    reps = []
    for flag in FLAGS:
        rw = weights[valid] * 2 * frame.loc[valid, flag]
        reps.append(float(np.average(values[valid], weights=rw) * 100))
    se = float(np.sqrt(np.mean((np.asarray(reps) - point) ** 2)))
    return {"valid_records": int(valid.sum()), "share_percent": point, "brr_se_percentage_points": se, "ci95_low": point - 1.96 * se, "ci95_high": point + 1.96 * se}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    fields = ["DUPERSID", "PANEL", "PERWT24F", "INSURC24", *EVENTS.values(), "PROBPY42", "RTHLTH53", "EMPST53"]
    hc, _ = pyreadstat.read_dta(args.hc256_file, usecols=fields)
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS])
    hc["KEY"] = hc["DUPERSID"].astype(str) + "|" + hc["PANEL"].astype(str)
    brr["KEY"] = brr["DUPERSID"].astype(str) + "|" + brr["PANEL"].round().astype(int).astype(str)
    frame = hc.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    if int(frame["BRR1"].isna().sum()):
        raise SystemExit("missing BRR flags after merge")
    weight_valid = pd.to_numeric(frame["PERWT24F"], errors="coerce").gt(0)
    output: dict[str, object] = {
        "schema": "us-meps-2024-event-context-by-coverage-v1",
        "method": "Under-65 INSURC24 coverage groups; event presence is annual count > 0; shares use PERWT24F and standard BRR with 128 replicate flags.",
        "coverage": {},
        "limitation": "Coverage-conditioned same-year associations are descriptive. They do not identify insurance effects, care delay, event-triggered financial burden, or post-event outcomes.",
    }
    for code, label in COVERAGE.items():
        coverage_mask = weight_valid & frame["INSURC24"].eq(code)
        entry: dict[str, object] = {"coverage_code": code, "positive_weight_records": int(coverage_mask.sum()), "events": {}}
        for event_name, field in EVENTS.items():
            event_present = pd.to_numeric(frame[field], errors="coerce").gt(0)
            event_entry: dict[str, object] = {"event_present_records": int((coverage_mask & event_present).sum()), "event_absent_records": int((coverage_mask & ~event_present).sum()), "outcomes": {}}
            for outcome_name, (outcome_field, outcome_fn, valid_codes) in OUTCOMES.items():
                event_entry["outcomes"][outcome_name] = {
                    "present": estimate(frame, coverage_mask & event_present, outcome_field, outcome_fn, valid_codes),
                    "absent": estimate(frame, coverage_mask & ~event_present, outcome_field, outcome_fn, valid_codes),
                }
            entry["events"][event_name] = event_entry
        output["coverage"][label] = entry
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
