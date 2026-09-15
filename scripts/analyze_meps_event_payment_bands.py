#!/usr/bin/env python3
"""Stratify first MEPS 2024 event payment by bounded round outcomes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


EVENTS = {
    "office": ("OBDATEYR", "OBDATEMM", "OBSF24X"),
    "emergency_room": ("ERDATEYR", "ERDATEMM", "ERFSF24X"),
    "inpatient": ("IPBEGYR", "IPBEGMM", "IPFSF24X"),
}


def read(path: Path, columns: list[str]) -> pd.DataFrame:
    frame, _ = pyreadstat.read_dta(path, usecols=columns)
    return frame


def person_key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def share(values: pd.Series, weights: pd.Series) -> float | None:
    x = pd.to_numeric(values, errors="coerce").to_numpy(float)
    w = pd.to_numeric(weights, errors="coerce").to_numpy(float)
    valid = np.isfinite(x) & np.isfinite(w) & (w > 0)
    if not valid.any() or w[valid].sum() == 0:
        return None
    return float(100 * np.average(x[valid], weights=w[valid]))


def summarize(frame: pd.DataFrame) -> dict[str, object]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = weights.gt(0)
    frame = frame.loc[valid]
    weights = weights.loc[valid]
    return {
        "records": int(len(frame)),
        "weighted_payment_mean": float(np.average(frame["PAYMENT"], weights=weights)) if len(frame) else None,
        "zero_payment_percent": share(frame["PAYMENT"].eq(0), weights),
        "bill_problem_followup_percent": share(frame["BILL_PROBLEM"], weights),
        "fair_poor_health_followup_percent": share(frame["FAIR_POOR_HEALTH"], weights),
        "not_employed_followup_percent": share(frame["NOT_EMPLOYED"], weights),
        "unexpected_expense_not_confident_percent": share(frame["UNEXPECTED_NOT_CONFIDENT"], weights),
        "missed_loan_or_credit_payment_percent": share(frame["MISSED_PAYMENT"], weights),
        "debt_collector_contact_percent": share(frame["DEBT_COLLECTOR"], weights),
        "medical_debt_any_percent": share(frame["MEDICAL_DEBT_ANY"], weights),
        "late_or_unable_rent_percent": share(frame["LATE_RENT"], weights),
        "unable_utility_percent": share(frame["UNABLE_UTILITY"], weights),
        "delayed_medical_care_for_cost_percent": share(frame["DELAYED_MEDICAL_CARE"], weights),
        "could_not_afford_medical_care_percent": share(frame["COULD_NOT_AFFORD_MEDICAL_CARE"], weights),
        "delayed_prescription_for_cost_percent": share(frame["DELAYED_PRESCRIPTION"], weights),
        "could_not_afford_prescription_percent": share(frame["COULD_NOT_AFFORD_PRESCRIPTION"], weights),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person = read(args.hc256_file, ["DUPERSID", "PANEL", "PERWT24F", "RTHLTH42", "EMPST42", "PROBPY42", "FWUNEXP42", "FWCRED42", "FWDEBT42", "MEDDEBT42", "FWRENT42", "FWUTIL42", "DLAYCA42", "AFRDCA42", "DLAYPM42", "AFRDPM42"])
    person["PERSON_KEY"] = person_key(person)
    person["BILL_PROBLEM"] = person["PROBPY42"].eq(1).astype(float)
    person["FAIR_POOR_HEALTH"] = person["RTHLTH42"].isin([4, 5]).astype(float)
    person["NOT_EMPLOYED"] = (~person["EMPST42"].isin([1, 2, 3])).astype(float)
    person["UNEXPECTED_NOT_CONFIDENT"] = person["FWUNEXP42"].isin([1, 2]).astype(float)
    person["MISSED_PAYMENT"] = person["FWCRED42"].eq(1).astype(float)
    person["DEBT_COLLECTOR"] = person["FWDEBT42"].eq(1).astype(float)
    person["MEDICAL_DEBT_ANY"] = person["MEDDEBT42"].between(1, 7).astype(float)
    person["LATE_RENT"] = person["FWRENT42"].eq(1).astype(float)
    person["UNABLE_UTILITY"] = person["FWUTIL42"].eq(1).astype(float)
    person["DELAYED_MEDICAL_CARE"] = person["DLAYCA42"].eq(1).astype(float)
    person["COULD_NOT_AFFORD_MEDICAL_CARE"] = person["AFRDCA42"].eq(1).astype(float)
    person["DELAYED_PRESCRIPTION"] = person["DLAYPM42"].eq(1).astype(float)
    person["COULD_NOT_AFFORD_PRESCRIPTION"] = person["AFRDPM42"].eq(1).astype(float)

    output: dict[str, object] = {
        "schema": "us-meps-2024-first-event-payment-bands-v1",
        "method": "Within each event family, retain the first valid dated event per DUPERSID+PANEL, join HC-256 round 4/2 health, work, bill-problem, financial-well-being, and cost-related care-access fields, and report weighted context shares by self/family payment band.",
        "payment_bands": ["$0", "$1-$99", "$100-$499", "$500-$1,999", "$2,000+"],
        "events": {},
        "limitation": "Payment is event-family self/family payment, not a complete bill or household burden. Financial-well-being and cost-related care-access fields are round 4/2 context and are not event-specific; the first event may follow an earlier need. No causation, care foregoing, alternatives, remedy, trust, or action is identified.",
    }
    for name, path in {"office": args.office_file, "emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}.items():
        year_field, month_field, payment_field = EVENTS[name]
        event = read(path, ["DUPERSID", "PANEL", "EVNTIDX", year_field, month_field, payment_field])
        event["PERSON_KEY"] = person_key(event)
        event["EVENT_MONTH"] = pd.to_numeric(event[year_field], errors="coerce") * 12 + pd.to_numeric(event[month_field], errors="coerce")
        event["PAYMENT"] = pd.to_numeric(event[payment_field], errors="coerce")
        valid = event["EVENT_MONTH"].between(2024 * 12, 2024 * 12 + 11) & event["PAYMENT"].notna()
        first = event.loc[valid].sort_values(["PERSON_KEY", "EVENT_MONTH", "EVNTIDX"]).drop_duplicates("PERSON_KEY")
        joined = first.merge(person, on="PERSON_KEY", how="inner", validate="many_to_one")
        bins = [(-0.01, 0, "$0"), (0.01, 99.99, "$1-$99"), (100, 499.99, "$100-$499"), (500, 1999.99, "$500-$1,999"), (2000, np.inf, "$2,000+")]
        output["events"][name] = {
            "payment_field": payment_field,
            "first_event_people": int(len(joined)),
            "payment_bands": {
                label: summarize(joined.loc[joined["PAYMENT"].between(low, high)])
                for low, high, label in bins
            },
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
