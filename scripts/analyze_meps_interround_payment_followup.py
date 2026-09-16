#!/usr/bin/env python3
"""Condition strict inter-round MEPS event transitions on family-paid amount."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat

FLAGS = [f"BRR{i}" for i in range(1, 129)]
EVENTS = {
    "emergency_room": ("ERDATEYR", "ERDATEMM", ("ERFSF24X", "ERDSF24X")),
    "inpatient": ("IPBEGYR", "IPBEGMM", ("IPFSF24X", "IPDSF24X")),
}
BANDS = ("zero", "positive_under_100", "100_or_more")


def read(path: Path, columns: list[str]) -> pd.DataFrame:
    frame, _ = pyreadstat.read_dta(path, usecols=columns)
    return frame


def person_key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def band(value: float) -> str:
    if value == 0:
        return "zero"
    if value < 100:
        return "positive_under_100"
    return "100_or_more"


def estimate(frame: pd.DataFrame, mask: pd.Series, outcome: pd.Series) -> dict[str, float | int | None]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    valid = mask & weights.gt(0) & outcome.notna()
    if not valid.any():
        return {"valid_records": 0, "share_percent": None, "brr_se_percentage_points": None, "ci95_low": None, "ci95_high": None}
    point = float(np.average(outcome[valid], weights=weights[valid]) * 100)
    replicate = []
    for flag in FLAGS:
        replicate_weights = weights[valid] * 2 * frame.loc[valid, flag]
        replicate.append(float(np.average(outcome[valid], weights=replicate_weights) * 100))
    se = float(np.sqrt(np.mean((np.asarray(replicate) - point) ** 2)))
    return {
        "valid_records": int(valid.sum()),
        "share_percent": point,
        "brr_se_percentage_points": se,
        "ci95_low": point - 1.96 * se,
        "ci95_high": point + 1.96 * se,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person = read(args.hc256_file, [
        "DUPERSID", "PANEL", "PERWT24F", "ENDRFY31", "ENDRFM31",
        "ENDRFY42", "ENDRFM42", "EMPST31", "EMPST42",
        "RTHLTH31", "RTHLTH42", "PROBPY42",
    ])
    person["KEY"] = person_key(person)
    brr = read(args.brr_file, ["DUPERSID", "PANEL", *FLAGS])
    brr["KEY"] = person_key(brr)
    person = person.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    person["R3_MONTH"] = pd.to_numeric(person["ENDRFY31"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM31"], errors="coerce")
    person["R4_MONTH"] = pd.to_numeric(person["ENDRFY42"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM42"], errors="coerce")
    round_valid = person["R3_MONTH"].notna() & person["R4_MONTH"].notna() & person["R4_MONTH"].gt(person["R3_MONTH"])
    output: dict[str, object] = {
        "schema": "us-meps-2024-interround-payment-followup-v1",
        "method": "For each event family, retain the first event strictly after R3/1 and strictly before R4/2 endpoint month. Condition weighted R3/1 and R4/2 outcomes on the event-level family-paid amount band. Standard BRR uses 128 replicate flags.",
        "person_records": int(len(person)),
        "round_order_valid_records": int(round_valid.sum()),
        "events": {},
        "limitation": "Family-paid amount is event-level payment, not a complete bill or household burden. The event window is selected and baseline differences remain; month ordering excludes exact-day ambiguity. Results are descriptive, not causal.",
    }
    for name, path in {"emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}.items():
        year_field, month_field, payment_fields = EVENTS[name]
        event = read(path, ["DUPERSID", "PANEL", "EVNTIDX", year_field, month_field, *payment_fields])
        event["KEY"] = person_key(event)
        event["EVENT_MONTH"] = pd.to_numeric(event[year_field], errors="coerce") * 12 + pd.to_numeric(event[month_field], errors="coerce")
        payment = event[list(payment_fields)].apply(pd.to_numeric, errors="coerce")
        event["FAMILY_PAYMENT"] = payment.sum(axis=1, min_count=1)
        valid = event["EVENT_MONTH"].notna() & event["FAMILY_PAYMENT"].notna() & event["FAMILY_PAYMENT"].ge(0)
        event = event.loc[valid].sort_values(["KEY", "EVENT_MONTH", "EVNTIDX"])
        first = event.drop_duplicates("KEY", keep="first")[["KEY", "EVENT_MONTH", "FAMILY_PAYMENT"]]
        joined = person.merge(first, on="KEY", how="inner", validate="one_to_one")
        outcome_series = {
            "fair_or_poor_health_baseline": joined["RTHLTH31"].isin([4, 5]).astype(float),
            "fair_or_poor_health_followup": joined["RTHLTH42"].isin([4, 5]).astype(float),
            "health_worsened": (joined["RTHLTH42"] > joined["RTHLTH31"]).where(
                joined["RTHLTH31"].isin([1, 2, 3, 4, 5]) & joined["RTHLTH42"].isin([1, 2, 3, 4, 5])
            ),
            "not_employed_followup": (~joined["EMPST42"].isin([1, 2, 3])).astype(float),
            "medical_bill_problem_followup": joined["PROBPY42"].eq(1).where(joined["PROBPY42"].isin([1, 2])),
        }
        window = (
            round_valid.loc[joined.index].to_numpy()
            & joined["EVENT_MONTH"].gt(joined["R3_MONTH"]).to_numpy()
            & joined["EVENT_MONTH"].lt(joined["R4_MONTH"]).to_numpy()
        )
        joined["PAYMENT_BAND"] = joined["FAMILY_PAYMENT"].map(band)
        groups = {}
        for group in BANDS:
            mask = pd.Series(window, index=joined.index) & joined["PAYMENT_BAND"].eq(group)
            weights = pd.to_numeric(joined.loc[mask, "PERWT24F"], errors="coerce")
            groups[group] = {
                "event_window_people": int(mask.sum()),
                "family_payment_mean": float(np.average(joined.loc[mask, "FAMILY_PAYMENT"], weights=weights)) if mask.any() else None,
                "outcomes": {outcome_name: estimate(joined, mask, series) for outcome_name, series in outcome_series.items()},
            }
        output["events"][name] = {
            "source_file": str(path),
            "valid_event_payment_records": int(len(event)),
            "event_window_people": int(window.sum()),
            "payment_field": "+".join(payment_fields),
            "payment_bands": groups,
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
