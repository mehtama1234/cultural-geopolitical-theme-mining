#!/usr/bin/env python3
"""Build a descriptive first-event/payment/round-context MEPS ledger."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


EVENTS = {
    "office": ("EVNTIDX", "OBDATEYR", "OBDATEMM", "OBSF24X"),
    "emergency_room": ("EVNTIDX", "ERDATEYR", "ERDATEMM", "ERFSF24X"),
    "inpatient": ("EVNTIDX", "IPBEGYR", "IPBEGMM", "IPFSF24X"),
}


def read(path: Path, columns: list[str]) -> pd.DataFrame:
    frame, _ = pyreadstat.read_dta(path, usecols=columns)
    return frame


def key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def weighted_mean(values: pd.Series, weights: pd.Series) -> float | None:
    x = pd.to_numeric(values, errors="coerce").to_numpy(float)
    w = pd.to_numeric(weights, errors="coerce").to_numpy(float)
    valid = np.isfinite(x) & np.isfinite(w) & (w > 0)
    if not valid.any() or w[valid].sum() == 0:
        return None
    return float(np.average(x[valid], weights=w[valid]))


def weighted_share(values: pd.Series, weights: pd.Series) -> float | None:
    mean = weighted_mean(values, weights)
    return None if mean is None else 100.0 * mean


def summarize(frame: pd.DataFrame, mask: pd.Series) -> dict[str, object]:
    subset = frame.loc[mask].copy()
    weights = pd.to_numeric(subset["PERWT24F"], errors="coerce")
    valid = weights.gt(0)
    subset = subset.loc[valid]
    weights = weights.loc[valid]
    def share(field: str) -> float | None:
        return weighted_share(subset[field], weights)
    return {
        "records": int(len(subset)),
        "weighted_self_family_payment_mean": weighted_mean(subset["SELF_PAYMENT"], weights),
        "zero_self_family_payment_percent": share("ZERO_PAYMENT"),
        "fair_or_poor_health_baseline_percent": share("FAIR_POOR_BASELINE"),
        "fair_or_poor_health_followup_percent": share("FAIR_POOR_FOLLOWUP"),
        "not_employed_baseline_percent": share("NOT_EMPLOYED_BASELINE"),
        "not_employed_followup_percent": share("NOT_EMPLOYED_FOLLOWUP"),
        "medical_bill_problem_followup_percent": share("BILL_PROBLEM_FOLLOWUP"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person_fields = [
        "DUPERSID", "PANEL", "PERWT24F", "ENDRFY42", "ENDRFM42",
        "EMPST31", "EMPST42", "RTHLTH31", "RTHLTH42", "PROBPY42",
    ]
    person = read(args.hc256_file, person_fields)
    person["PERSON_KEY"] = key(person)
    person_lookup = person.set_index("PERSON_KEY")
    r4_month = pd.to_numeric(person["ENDRFY42"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM42"], errors="coerce")
    person["R4_MONTH"] = r4_month

    output: dict[str, object] = {
        "schema": "us-meps-2024-bounded-episode-ledger-v1",
        "method": "One first valid dated event per person/event family is joined exactly by DUPERSID+PANEL to HC-256. Event month is classified before, same month as, or after the R4/2 reference-period endpoint. Payment and round fields are weighted descriptive summaries; no standard errors or causal effect is claimed.",
        "person_records": int(len(person)),
        "person_positive_weight_records": int(pd.to_numeric(person["PERWT24F"], errors="coerce").gt(0).sum()),
        "events": {},
        "limitation": "The first observed event is not necessarily the triggering need, bill, or first care contact. Annual/round health, work, and bill-problem fields are contextual and may include the event month. No care decision, alternative, debt, unpaid care, remedy, trust, or action field is observed.",
    }

    for name, path in {"office": args.office_file, "emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}.items():
        event_id, year_field, month_field, payment_field = EVENTS[name]
        event = read(path, ["DUPERSID", "PANEL", event_id, year_field, month_field, payment_field])
        event["PERSON_KEY"] = key(event)
        event["EVENT_MONTH"] = pd.to_numeric(event[year_field], errors="coerce") * 12 + pd.to_numeric(event[month_field], errors="coerce")
        event["SELF_PAYMENT"] = pd.to_numeric(event[payment_field], errors="coerce")
        valid = event["EVENT_MONTH"].sub(1900 * 12).between(0, (2024 - 1900) * 12 + 11) & event["EVENT_MONTH"].notna() & event["SELF_PAYMENT"].notna()
        event = event.loc[valid].sort_values(["PERSON_KEY", "EVENT_MONTH", event_id])
        first = event.drop_duplicates("PERSON_KEY", keep="first")
        joined = first.merge(person.reset_index(drop=True), on="PERSON_KEY", how="inner", validate="many_to_one", suffixes=("", "_PERSON"))
        joined["ZERO_PAYMENT"] = joined["SELF_PAYMENT"].eq(0).astype(float)
        joined["FAIR_POOR_BASELINE"] = joined["RTHLTH31"].isin([4, 5]).astype(float)
        joined["FAIR_POOR_FOLLOWUP"] = joined["RTHLTH42"].isin([4, 5]).astype(float)
        joined["NOT_EMPLOYED_BASELINE"] = (~joined["EMPST31"].isin([1, 2, 3])).astype(float)
        joined["NOT_EMPLOYED_FOLLOWUP"] = (~joined["EMPST42"].isin([1, 2, 3])).astype(float)
        joined["BILL_PROBLEM_FOLLOWUP"] = joined["PROBPY42"].eq(1).astype(float)
        joined["R4_MONTH"] = pd.to_numeric(joined["ENDRFY42"], errors="coerce") * 12 + pd.to_numeric(joined["ENDRFM42"], errors="coerce")
        joined["timing"] = np.select(
            [joined["EVENT_MONTH"] < joined["R4_MONTH"], joined["EVENT_MONTH"] == joined["R4_MONTH"]],
            ["before_r4_endpoint_month", "same_r4_endpoint_month"],
            default="after_r4_endpoint_month",
        )
        output["events"][name] = {
            "source_file": str(path),
            "source_event_records": int(len(event)),
            "first_event_people": int(len(joined)),
            "timing_groups": {timing: summarize(joined, joined["timing"].eq(timing)) for timing in ["before_r4_endpoint_month", "same_r4_endpoint_month", "after_r4_endpoint_month"]},
            "payment_field": payment_field,
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
