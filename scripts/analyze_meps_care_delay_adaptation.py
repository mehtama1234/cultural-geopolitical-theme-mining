#!/usr/bin/env python3
"""Profile MEPS cost-related care delay against ESAQ adaptation routes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


ADAPTATION_FIELDS = {
    "sacrificed_leisure": "EQSLEI53",
    "sacrificed_big_purchase": "EQSBIG53",
    "sacrificed_basic_spending": "EQSBAS53",
    "sacrificed_savings": "EQSSAV53",
    "sacrificed_living_situation": "EQSLIV53",
    "worked_when_health_needed_time_off": "EQWSIK53",
    "leave_denied": "EQLDEN53",
    "no_paid_or_unpaid_leave": "EQLUPD53",
    "not_enough_leave": "EQLENH53",
    "feared_job_consequence": "EQLJBSC53",
    "could_not_afford_income_loss": "EQLSIN53",
    "care_instead_of_work": "EQCRNW53",
}


def weighted_share(frame: pd.DataFrame, field: str) -> float | None:
    weight = pd.to_numeric(frame["ESAQWT24F"], errors="coerce")
    value = pd.to_numeric(frame[field], errors="coerce")
    valid = weight.gt(0) & value.notna()
    if not valid.any() or weight[valid].sum() == 0:
        return None
    return float(100 * np.average(value[valid], weights=weight[valid]))


def weighted_category_share(frame: pd.DataFrame, field: str, code: int) -> float | None:
    value = frame[field].eq(code).astype(float)
    frame = frame.assign(_CATEGORY=value)
    return weighted_share(frame, "_CATEGORY")


def profile(frame: pd.DataFrame) -> dict[str, object]:
    weight = pd.to_numeric(frame["ESAQWT24F"], errors="coerce")
    valid = weight.gt(0)
    frame = frame.loc[valid]
    return {
        "records": int(len(frame)),
        "sacrifice_or_work_adaptation": {
            key: weighted_share(frame, key) for key in ADAPTATION_FIELDS
        },
        "payment_strategy_500_bill": {
            str(code): int((frame["EQPAYB53"] == code).sum())
            for code in range(1, 9)
        },
        "payment_strategy_500_bill_weighted_percent": {
            str(code): weighted_category_share(frame, "EQPAYB53", code)
            for code in range(1, 9)
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    fields = ["ESAQWT24F", "DLAYCA42", "AFRDCA42", "DLAYPM42", "AFRDPM42", "EQPAYB53", *ADAPTATION_FIELDS.values()]
    frame, _ = pyreadstat.read_dta(args.hc256_file, usecols=fields)
    for key, field in ADAPTATION_FIELDS.items():
        frame[key] = frame[field].eq(1).astype(float)
    frame["DELAYED_MEDICAL_CARE"] = frame["DLAYCA42"].eq(1).astype(float)
    frame["COULD_NOT_AFFORD_MEDICAL_CARE"] = frame["AFRDCA42"].eq(1).astype(float)
    frame["DELAYED_PRESCRIPTION"] = frame["DLAYPM42"].eq(1).astype(float)
    frame["COULD_NOT_AFFORD_PRESCRIPTION"] = frame["AFRDPM42"].eq(1).astype(float)
    output: dict[str, object] = {
        "schema": "us-meps-2024-care-delay-adaptation-v1",
        "method": "Use ESAQWT24F and valid HC-256 round-level fields; compare cost-related care-delay groups with payment strategy, spending/saving sacrifices, work/leave constraints, and care-for-work substitution.",
        "groups": {},
        "limitation": "DLAY/AFRD fields are R4/2 and ESAQ fields are R5/3 or 2024 ESAQ measures; they are not a dated same-bill sequence. Associations do not establish whether delay caused adaptation or whether an institutional response repaired it.",
    }
    output["groups"]["medical_care_delayed_for_cost"] = profile(frame.loc[frame["DELAYED_MEDICAL_CARE"].eq(1)])
    output["groups"]["medical_care_not_delayed_for_cost"] = profile(frame.loc[frame["DELAYED_MEDICAL_CARE"].eq(0)])
    output["groups"]["could_not_afford_medical_care"] = profile(frame.loc[frame["COULD_NOT_AFFORD_MEDICAL_CARE"].eq(1)])
    output["groups"]["medical_care_affordability_not_reported"] = profile(frame.loc[frame["COULD_NOT_AFFORD_MEDICAL_CARE"].eq(0)])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
