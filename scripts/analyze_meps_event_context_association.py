#!/usr/bin/env python3
"""Estimate bounded same-person MEPS event/context associations with BRR."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


FLAGS = [f"BRR{i}" for i in range(1, 129)]
EVENTS = {"office": "OBTOTV24", "emergency_room": "ERTOT24", "inpatient": "IPDIS24"}
OUTCOMES = {
    "medical_bill_problem": lambda d: (d["PROBPY42"].isin([1, 2]), d["PROBPY42"] == 1),
    "sacrificed_big_purchase": lambda d: (d["CFNPUR42"].isin([1, 2]), d["CFNPUR42"] == 1),
    "paid_leave_for_doctor_visit": lambda d: (d["PAYDR53"].isin([1, 2]), d["PAYDR53"] == 1),
    "fair_or_poor_perceived_health": lambda d: (d["RTHLTH53"].isin([1, 2, 3, 4, 5]), d["RTHLTH53"] >= 4),
    "not_employed_round_5_3": lambda d: (d["EMPST53"].isin([1, 2, 3, 4]), d["EMPST53"] == 4),
}


def estimate(frame: pd.DataFrame, exposure: pd.Series, valid: pd.Series, outcome: pd.Series) -> dict[str, float | int | None]:
    weights = frame["PERWT24F"].to_numpy(float)
    group = exposure.to_numpy(bool)
    valid_array = valid.to_numpy(bool) & np.isfinite(weights) & (weights > 0)
    if not valid_array.any():
        return {"valid_records": 0, "weighted_share_percent": None, "brr_se_percentage_points": None, "ci95_low": None, "ci95_high": None}
    selected = valid_array & group
    if not selected.any():
        return {"valid_records": 0, "weighted_share_percent": None, "brr_se_percentage_points": None, "ci95_low": None, "ci95_high": None}
    values = outcome.to_numpy(bool)
    point = float(np.average(values[selected].astype(float), weights=weights[selected]) * 100)
    reps = []
    for flag in FLAGS:
        rw = weights[selected] * 2 * frame.loc[selected, flag].to_numpy(float)
        reps.append(float(np.average(values[selected].astype(float), weights=rw) * 100))
    se = float(np.sqrt(np.mean((np.asarray(reps) - point) ** 2)))
    return {
        "valid_records": int(selected.sum()),
        "weighted_share_percent": point,
        "brr_se_percentage_points": se,
        "ci95_low": point - 1.96 * se,
        "ci95_high": point + 1.96 * se,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    fields = ["DUPERSID", "PANEL", "PERWT24F", *EVENTS.values(), *OUTCOMES.keys()]
    # Replace outcome names with their source fields.
    fields = ["DUPERSID", "PANEL", "PERWT24F", *EVENTS.values(), "PROBPY42", "CFNPUR42", "PAYDR53", "RTHLTH53", "EMPST53"]
    hc, _ = pyreadstat.read_dta(args.hc256_file, usecols=fields)
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS])
    hc["KEY"] = hc["DUPERSID"].astype(str) + "|" + hc["PANEL"].astype(str)
    brr["KEY"] = brr["DUPERSID"].astype(str) + "|" + brr["PANEL"].round().astype(int).astype(str)
    merged = hc.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    if int(merged["BRR1"].isna().sum()):
        raise SystemExit("HC-256 to HC-036BRR merge has missing replicate flags")

    output: dict[str, object] = {
        "schema": "us-meps-2024-event-context-association-v1",
        "method": "Person-level descriptive shares use PERWT24F; standard BRR uses BRR1-BRR128 * 2 * PERWT24F. Event presence is annual event count > 0.",
        "records": len(merged),
        "positive_weight_records": int((merged["PERWT24F"] > 0).sum()),
        "events": {},
        "limitation": "Same-year event presence and reported context are associated observations, not event-triggered outcomes or causal estimates. Event indicators do not identify delayed or forgone care, and annual fields do not provide a post-event window.",
    }
    for event_name, event_field in EVENTS.items():
        counts = pd.to_numeric(merged[event_field], errors="coerce")
        positive_weight = pd.to_numeric(merged["PERWT24F"], errors="coerce") > 0
        exposure = counts > 0
        event_output: dict[str, object] = {
            "event_field": event_field,
            "positive_event_records": int((positive_weight & exposure).sum()),
            "no_event_records": int((positive_weight & (counts == 0)).sum()),
            "event_presence_weighted_percent": float(np.average(exposure[positive_weight].astype(float), weights=merged.loc[positive_weight, "PERWT24F"])) * 100,
            "outcomes": {},
        }
        for outcome_name, builder in OUTCOMES.items():
            valid, outcome = builder(merged)
            event_output["outcomes"][outcome_name] = {
                "event_present": estimate(merged, exposure, valid, outcome),
                "event_absent": estimate(merged, ~exposure, valid, outcome),
            }
        output["events"][event_name] = event_output

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
