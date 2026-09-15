#!/usr/bin/env python3
"""Cross-tab MEPS 2024 financial room and cost-related care delay."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


def weighted_share(frame: pd.DataFrame, field: str) -> float | None:
    weight = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    value = pd.to_numeric(frame[field], errors="coerce")
    valid = weight.gt(0) & value.notna()
    if not valid.any() or weight[valid].sum() == 0:
        return None
    return float(100 * np.average(value[valid], weights=weight[valid]))


def summarize(frame: pd.DataFrame) -> dict[str, object]:
    weight = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = weight.gt(0)
    frame = frame.loc[valid]
    return {
        "records": int(len(frame)),
        "delayed_medical_care_for_cost_percent": weighted_share(frame, "DELAYED_MEDICAL_CARE"),
        "could_not_afford_medical_care_percent": weighted_share(frame, "COULD_NOT_AFFORD_MEDICAL_CARE"),
        "delayed_prescription_for_cost_percent": weighted_share(frame, "DELAYED_PRESCRIPTION"),
        "could_not_afford_prescription_percent": weighted_share(frame, "COULD_NOT_AFFORD_PRESCRIPTION"),
        "unexpected_expense_not_confident_percent": weighted_share(frame, "UNEXPECTED_NOT_CONFIDENT"),
        "missed_loan_or_credit_payment_percent": weighted_share(frame, "MISSED_PAYMENT"),
        "debt_collector_contact_percent": weighted_share(frame, "DEBT_COLLECTOR"),
        "medical_debt_any_percent": weighted_share(frame, "MEDICAL_DEBT_ANY"),
        "late_or_unable_rent_percent": weighted_share(frame, "LATE_RENT"),
        "unable_utility_percent": weighted_share(frame, "UNABLE_UTILITY"),
        "fair_poor_health_percent": weighted_share(frame, "FAIR_POOR_HEALTH"),
        "not_employed_percent": weighted_share(frame, "NOT_EMPLOYED"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    fields = ["PERWT24F", "FWUNEXP42", "FWCRED42", "FWDEBT42", "FWRENT42", "FWUTIL42", "MEDDEBT42", "INSCOV24", "POVCAT24", "EMPST42", "RTHLTH42", "DLAYCA42", "AFRDCA42", "DLAYPM42", "AFRDPM42"]
    frame, _ = pyreadstat.read_dta(args.hc256_file, usecols=fields)
    frame["DELAYED_MEDICAL_CARE"] = frame["DLAYCA42"].eq(1).astype(float)
    frame["COULD_NOT_AFFORD_MEDICAL_CARE"] = frame["AFRDCA42"].eq(1).astype(float)
    frame["DELAYED_PRESCRIPTION"] = frame["DLAYPM42"].eq(1).astype(float)
    frame["COULD_NOT_AFFORD_PRESCRIPTION"] = frame["AFRDPM42"].eq(1).astype(float)
    frame["UNEXPECTED_NOT_CONFIDENT"] = frame["FWUNEXP42"].isin([1, 2]).astype(float)
    frame["MISSED_PAYMENT"] = frame["FWCRED42"].eq(1).astype(float) if "FWCRED42" in frame else 0.0
    frame["DEBT_COLLECTOR"] = frame["FWDEBT42"].eq(1).astype(float) if "FWDEBT42" in frame else 0.0
    frame["MEDICAL_DEBT_ANY"] = frame["MEDDEBT42"].between(1, 7).astype(float)
    frame["LATE_RENT"] = frame["FWRENT42"].eq(1).astype(float) if "FWRENT42" in frame else 0.0
    frame["UNABLE_UTILITY"] = frame["FWUTIL42"].eq(1).astype(float) if "FWUTIL42" in frame else 0.0
    frame["FAIR_POOR_HEALTH"] = frame["RTHLTH42"].isin([4, 5]).astype(float)
    frame["NOT_EMPLOYED"] = (~frame["EMPST42"].isin([1, 2, 3])).astype(float)
    output: dict[str, object] = {
        "schema": "us-meps-2024-financial-room-care-delay-v1",
        "method": "Use positive PERWT24F and valid round 4/2 financial-room, medical-debt, and cost-related care-access fields from HC-256; report weighted cross-sectional shares.",
        "financial_room_measure": "FWUNEXP42: confidence paying an unexpected expense",
        "financial_room_labels": {"1": "not_at_all_confident", "2": "not_too_confident", "3": "somewhat_confident", "4": "very_confident"},
        "confidence_groups": {},
        "medical_debt_groups": {},
        "coverage_groups": {},
        "limitation": "Same-round associations do not identify event timing, causation, a specific bill, alternatives, care completion, or later recovery, trust, or action. Financial-room and care-access fields may refer to different needs.",
    }
    confidence = {1: "not_at_all_confident", 2: "not_too_confident", 3: "somewhat_confident", 4: "very_confident"}
    for code, label in confidence.items():
        output["confidence_groups"][label] = summarize(frame.loc[frame["FWUNEXP42"].eq(code)])
    output["confidence_groups"]["not_confident_combined"] = summarize(frame.loc[frame["FWUNEXP42"].isin([1, 2])])
    output["confidence_groups"]["confident_combined"] = summarize(frame.loc[frame["FWUNEXP42"].isin([3, 4])])
    output["medical_debt_groups"]["no_medical_debt"] = summarize(frame.loc[frame["MEDDEBT42"].eq(0)])
    output["medical_debt_groups"]["any_medical_debt"] = summarize(frame.loc[frame["MEDDEBT42"].between(1, 7)])
    debt_amounts = {
        "no_medical_debt": [0],
        "$0-$500": [1],
        "$501-$1,000": [2],
        "$1,001-$2,000": [3],
        "$2,001-$5,000": [4],
        "$5,001-$10,000": [5],
        "$10,001-$20,000": [6],
        "$20,001+": [7],
    }
    output["medical_debt_amount_groups"] = {
        label: summarize(frame.loc[frame["MEDDEBT42"].isin(codes)])
        for label, codes in debt_amounts.items()
    }
    coverage = {1: "any_private", 2: "public_only", 3: "uninsured"}
    for code, label in coverage.items():
        output["coverage_groups"][label] = summarize(frame.loc[frame["INSCOV24"].eq(code)])
    output["coverage_by_confidence"] = {}
    for coverage_code, coverage_label in coverage.items():
        covered = frame["INSCOV24"].eq(coverage_code)
        output["coverage_by_confidence"][coverage_label] = {
            "not_confident": summarize(frame.loc[covered & frame["FWUNEXP42"].isin([1, 2])]),
            "confident": summarize(frame.loc[covered & frame["FWUNEXP42"].isin([3, 4])]),
        }
    resources = {1: "poor_or_negative", 2: "near_poor", 3: "low_income", 4: "middle_income", 5: "high_income"}
    output["resource_groups"] = {}
    output["resource_by_confidence"] = {}
    for code, label in resources.items():
        resource_mask = frame["POVCAT24"].eq(code)
        output["resource_groups"][label] = summarize(frame.loc[resource_mask])
        output["resource_by_confidence"][label] = {
            "not_confident": summarize(frame.loc[resource_mask & frame["FWUNEXP42"].isin([1, 2])]),
            "confident": summarize(frame.loc[resource_mask & frame["FWUNEXP42"].isin([3, 4])]),
        }
    output["employment_groups"] = {
        "employed": summarize(frame.loc[frame["EMPST42"].isin([1, 2, 3])]),
        "not_employed": summarize(frame.loc[~frame["EMPST42"].isin([1, 2, 3]) & frame["EMPST42"].notna()]),
    }
    output["employment_by_confidence"] = {
        "employed": {
            "not_confident": summarize(frame.loc[frame["EMPST42"].isin([1, 2, 3]) & frame["FWUNEXP42"].isin([1, 2])]),
            "confident": summarize(frame.loc[frame["EMPST42"].isin([1, 2, 3]) & frame["FWUNEXP42"].isin([3, 4])]),
        },
        "not_employed": {
            "not_confident": summarize(frame.loc[~frame["EMPST42"].isin([1, 2, 3]) & frame["EMPST42"].notna() & frame["FWUNEXP42"].isin([1, 2])]),
            "confident": summarize(frame.loc[~frame["EMPST42"].isin([1, 2, 3]) & frame["EMPST42"].notna() & frame["FWUNEXP42"].isin([3, 4])]),
        },
    }
    output["care_delay_groups"] = {
        "medical_care_delayed_for_cost": summarize(frame.loc[frame["DELAYED_MEDICAL_CARE"].eq(1)]),
        "medical_care_not_delayed_for_cost": summarize(frame.loc[frame["DELAYED_MEDICAL_CARE"].eq(0)]),
        "prescription_delayed_for_cost": summarize(frame.loc[frame["DELAYED_PRESCRIPTION"].eq(1)]),
        "prescription_not_delayed_for_cost": summarize(frame.loc[frame["DELAYED_PRESCRIPTION"].eq(0)]),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
