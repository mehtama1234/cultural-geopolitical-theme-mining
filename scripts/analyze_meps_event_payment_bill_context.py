#!/usr/bin/env python3
"""Estimate MEPS event-payment means by the person's annual bill-problem report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat

EVENTS = {
    "office": ("OBXP24X", "OBSF24X"),
    "emergency_room": ("ERXP24X", "ERFSF24X"),
    "inpatient": ("IPXP24X", "IPFSF24X"),
    "prescription": ("RXXP24X", "RXSF24X"),
}
FLAGS = [f"BRR{i}" for i in range(1, 129)]
COVERAGE = {1: "under65_private", 2: "under65_public_only", 3: "under65_uninsured"}
POVERTY = {1: "poor_negative", 2: "near_poor", 3: "low_income", 4: "middle_income", 5: "high_income"}


def estimate(frame: pd.DataFrame, payment: pd.Series, mask: pd.Series) -> dict[str, float | int | None]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce").to_numpy(float)
    values = pd.to_numeric(payment, errors="coerce").to_numpy(float)
    valid = mask.to_numpy(bool) & np.isfinite(weights) & (weights > 0) & np.isfinite(values)
    if not valid.any():
        return {"valid_events": 0, "weighted_mean_dollars": None, "brr_se_dollars": None, "ci95_low": None, "ci95_high": None}
    point = float(np.average(values[valid], weights=weights[valid]))
    replicate = []
    for flag in FLAGS:
        replicate_weights = weights[valid] * 2 * pd.to_numeric(frame.loc[valid, flag], errors="coerce").to_numpy(float)
        replicate.append(float(np.average(values[valid], weights=replicate_weights)) if replicate_weights.sum() > 0 else np.nan)
    usable_replicates = np.asarray(replicate)[np.isfinite(replicate)]
    se = float(np.sqrt(np.mean((usable_replicates - point) ** 2))) if usable_replicates.size else None
    return {
        "valid_events": int(valid.sum()),
        "weighted_mean_dollars": round(point, 4),
        "brr_valid_replicates": int(usable_replicates.size),
        "brr_se_dollars": round(se, 4) if se is not None else None,
        "ci95_low": round(point - 1.96 * se, 4) if se is not None else None,
        "ci95_high": round(point + 1.96 * se, 4) if se is not None else None,
    }


def read_event(path: Path, total_field: str, family_field: str) -> pd.DataFrame:
    fields = ["DUPERSID", "PANEL", "PERWT24F", "VARSTR", "VARPSU", total_field, family_field]
    frame, _ = pyreadstat.read_dta(path, usecols=fields)
    return frame


def add_key(frame: pd.DataFrame) -> None:
    panel = pd.to_numeric(frame["PANEL"], errors="coerce")
    frame["KEY"] = frame["DUPERSID"].astype(str) + "|" + panel.round().astype("Int64").astype(str)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hc256", type=Path, required=True)
    parser.add_argument("--brr", type=Path, required=True)
    parser.add_argument("--office", type=Path, required=True)
    parser.add_argument("--emergency-room", type=Path, required=True)
    parser.add_argument("--inpatient", type=Path, required=True)
    parser.add_argument("--prescription", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person, _ = pyreadstat.read_dta(args.hc256, usecols=["DUPERSID", "PANEL", "PROBPY42", "INSURC24", "POVCAT24"])
    brr, _ = pyreadstat.read_dta(args.brr, usecols=["DUPERSID", "PANEL", *FLAGS])
    for frame in [person, brr]:
        add_key(frame)
    person = person.drop_duplicates("KEY")
    brr = brr.drop_duplicates("KEY")
    person = person.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    if person["BRR1"].isna().any():
        raise SystemExit("HC-256 to HC-036BRR merge has missing replicate flags")

    output: dict[str, object] = {
        "format": "us-meps-2024-event-payment-bill-context-v1",
        "source_unit": "2024 MEPS event records linked to HC-256 annual person context",
        "weight": "event PERWT24F with event-file BRR1-BRR128",
        "variance_estimation": True,
        "causal_estimation": False,
        "person_bill_problem_definition": "PROBPY42=1 reports a medical bill problem; PROBPY42=2 reports no problem; other codes excluded.",
        "events": {},
    }
    paths = {"office": args.office, "emergency_room": args.emergency_room, "inpatient": args.inpatient, "prescription": args.prescription}
    for event_name, path in paths.items():
        total_field, family_field = EVENTS[event_name]
        events = read_event(path, total_field, family_field)
        for frame in [events]:
            add_key(frame)
        merged = events.merge(person[["KEY", "PROBPY42", "INSURC24", "POVCAT24", *FLAGS]], on="KEY", how="left", validate="many_to_one")
        total = pd.to_numeric(merged[total_field], errors="coerce")
        family = pd.to_numeric(merged[family_field], errors="coerce")
        bill = pd.to_numeric(merged["PROBPY42"], errors="coerce")
        positive = pd.to_numeric(merged["PERWT24F"], errors="coerce") > 0
        by_coverage: dict[str, object] = {}
        for code, label in COVERAGE.items():
            coverage = merged["INSURC24"].eq(code)
            by_coverage[label] = {
                "problem_reported": {
                    "self_family_payment": estimate(merged, family, positive & coverage & (bill == 1)),
                },
                "no_problem_reported": {
                    "self_family_payment": estimate(merged, family, positive & coverage & (bill == 2)),
                },
            }
        by_poverty: dict[str, object] = {}
        for code, label in POVERTY.items():
            poverty = merged["POVCAT24"].eq(code)
            by_poverty[label] = {
                "problem_reported": {"self_family_payment": estimate(merged, family, positive & poverty & (bill == 1))},
                "no_problem_reported": {"self_family_payment": estimate(merged, family, positive & poverty & (bill == 2))},
            }
        output["events"][event_name] = {
            "event_file_records": len(events),
            "positive_weight_events": int(positive.sum()),
            "person_context_link_missing": int(merged["PROBPY42"].isna().sum()),
            "payment_fields": {"total": total_field, "self_family": family_field},
            "under65_by_coverage_and_bill_problem": by_coverage,
            "by_poverty_and_bill_problem": by_poverty,
            "by_bill_problem": {
                "problem_reported": {
                    "total_payment": estimate(merged, total, positive & (bill == 1)),
                    "self_family_payment": estimate(merged, family, positive & (bill == 1)),
                },
                "no_problem_reported": {
                    "total_payment": estimate(merged, total, positive & (bill == 2)),
                    "self_family_payment": estimate(merged, family, positive & (bill == 2)),
                },
            },
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
