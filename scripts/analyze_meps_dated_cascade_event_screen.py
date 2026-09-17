#!/usr/bin/env python3
"""Build a dated MEPS event-to-household-response screen."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat

FLAGS = [f"BRR{i}" for i in range(1, 129)]
EVENTS = {
    "office": ("OBDATEYR", "OBDATEMM", "OBSF24X"),
    "emergency_room": ("ERDATEYR", "ERDATEMM", "ERFSF24X"),
    "inpatient": ("IPBEGYR", "IPBEGMM", "IPFSF24X"),
    "prescription": ("RXBEGYRX", "RXBEGMM", "RXSF24X"),
}
OUTCOMES = {
    "cost_related_care_delay": ("DLAYCA42", lambda s: s.eq(1), lambda s: s.isin([1, 2])),
    "medical_bill_problem": ("PROBPY42", lambda s: s.eq(1), lambda s: s.isin([1, 2])),
    "medical_debt": ("MEDDEBT42", lambda s: s.between(1, 7), lambda s: s.between(0, 7)),
    "debt_collector_contact": ("FWDEBT42", lambda s: s.eq(1), lambda s: s.isin([1, 2])),
    "not_employed_followup": ("EMPST42", lambda s: s.eq(4), lambda s: s.isin([1, 2, 3, 4])),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def estimate(frame: pd.DataFrame, mask: pd.Series, valid: pd.Series,
             values: pd.Series) -> dict[str, object]:
    weights = pd.to_numeric(frame["PERWT24F"], errors="coerce")
    selected = mask & valid & weights.gt(0)
    if not selected.any():
        return {"valid_records": 0, "share_percent": None,
                "brr_se_percentage_points": None, "approx_95_ci_percentage_points": None}
    y = values.astype(float)
    point = float(np.average(y[selected], weights=weights[selected]) * 100)
    replicate = []
    for flag in FLAGS:
        replicate_weights = weights[selected] * 2 * pd.to_numeric(frame.loc[selected, flag], errors="coerce")
        replicate.append(float(np.average(y[selected], weights=replicate_weights) * 100))
    se = float(np.sqrt(np.mean((np.asarray(replicate) - point) ** 2)))
    return {
        "valid_records": int(selected.sum()),
        "share_percent": point,
        "brr_se_percentage_points": se,
        "approx_95_ci_percentage_points": [point - 1.96 * se, point + 1.96 * se],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("brr_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--prescription-file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    person_fields = [
        "DUPERSID", "PANEL", "PERWT24F", "ENDRFY31", "ENDRFM31", "ENDRFY42", "ENDRFM42",
        *[field for field, _, _ in OUTCOMES.values()], "RTHLTH31", "RTHLTH42", "EMPST31", "EMPST42",
    ]
    person, _ = pyreadstat.read_dta(args.hc256_file, usecols=person_fields, apply_value_formats=False, encoding="latin1")
    brr, _ = pyreadstat.read_dta(args.brr_file, usecols=["DUPERSID", "PANEL", *FLAGS], apply_value_formats=False, encoding="latin1")
    person["KEY"] = key(person)
    brr["KEY"] = key(brr)
    person = person.merge(brr.drop(columns=["DUPERSID", "PANEL"]), on="KEY", how="left", validate="one_to_one")
    if int(person["BRR1"].isna().sum()):
        raise SystemExit("HC-256 to BRR file merge has missing replicate flags")
    r3 = pd.to_numeric(person["ENDRFY31"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM31"], errors="coerce")
    r4 = pd.to_numeric(person["ENDRFY42"], errors="coerce") * 12 + pd.to_numeric(person["ENDRFM42"], errors="coerce")
    round_valid = r3.between(1900 * 12, 2030 * 12) & r4.between(1900 * 12, 2030 * 12) & r4.gt(r3)

    output: dict[str, object] = {
        "schema": "us-meps-dated-cascade-event-screen-v1",
        "method": "Select each person's first valid event month strictly between R3/1 and R4/2 endpoints; compare the event-window group with the complementary round-valid group using PERWT24F and 128 HC-036BRR flags. The event window is dated at month level; outcomes are same-person R4/2 context, including a valid EMPST42 non-employment endpoint.",
        "person_records": int(len(person)),
        "round_order_valid_records": int(round_valid.sum()),
        "inputs": {
            "hc256": {"path": str(args.hc256_file), "sha256": sha256(args.hc256_file)},
            "brr": {"path": str(args.brr_file), "sha256": sha256(args.brr_file)},
        },
        "events": {},
        "limitation": "A dated event is not necessarily the triggering need or the bill that caused the household response. Care delay, debt, bill, and employment status are same-person outcomes or context without a claim identifier, event-specific obligation, exact day, remedy, or causal identification. The complementary group is not a no-need control; EMPST42 non-employment is not job loss, hours loss, or employment quality.",
    }

    event_files = {"office": args.office_file, "emergency_room": args.emergency_room_file, "inpatient": args.inpatient_file}
    if args.prescription_file is not None:
        event_files["prescription"] = args.prescription_file
    for name, path in event_files.items():
        year_field, month_field, payment_field = EVENTS[name]
        event, _ = pyreadstat.read_dta(path, usecols=["DUPERSID", "PANEL", year_field, month_field, payment_field], apply_value_formats=False, encoding="latin1")
        event["KEY"] = key(event)
        year = pd.to_numeric(event[year_field], errors="coerce")
        month = pd.to_numeric(event[month_field], errors="coerce")
        event["EVENT_MONTH"] = year * 12 + month
        event_valid = year.between(1900, 2024) & month.between(1, 12)
        first = event.loc[event_valid].sort_values(["KEY", "EVENT_MONTH"]).drop_duplicates("KEY", keep="first")
        first = first[["KEY", "EVENT_MONTH", payment_field]].rename(columns={payment_field: "EVENT_PAYMENT"})
        joined = person.merge(first, on="KEY", how="left", validate="one_to_one")
        in_window = round_valid & joined["EVENT_MONTH"].gt(r3) & joined["EVENT_MONTH"].lt(r4)
        comparison = round_valid & ~in_window
        groups: dict[str, object] = {}
        for group_name, group_mask in (("event_window", in_window), ("complementary_round_valid", comparison)):
            group: dict[str, object] = {"records": int(group_mask.sum()), "outcomes": {}}
            for outcome, (field, positive, valid_field) in OUTCOMES.items():
                numeric = pd.to_numeric(joined[field], errors="coerce")
                group["outcomes"][outcome] = estimate(joined, group_mask, valid_field(numeric), positive(numeric))
            groups[group_name] = group
        payment_mask = in_window & pd.to_numeric(joined["EVENT_PAYMENT"], errors="coerce").notna() & pd.to_numeric(joined["PERWT24F"], errors="coerce").gt(0)
        payment = pd.to_numeric(joined["EVENT_PAYMENT"], errors="coerce")
        output["events"][name] = {
            "source_file": str(path),
            "source_sha256": sha256(path),
            "valid_dated_event_people": int(len(first)),
            "event_window_people": int(in_window.sum()),
            "event_window_date_rule": "first event month > R3/1 endpoint month and < R4/2 endpoint month",
            "event_payment_field": payment_field,
            "event_window_weighted_self_family_payment_mean": float(np.average(payment[payment_mask], weights=joined.loc[payment_mask, "PERWT24F"])) if payment_mask.any() else None,
            "event_window_zero_self_family_payment_percent": float(100 * np.average((payment[payment_mask] == 0).astype(float), weights=joined.loc[payment_mask, "PERWT24F"])) if payment_mask.any() else None,
            "groups": groups,
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"person_records": len(person), "round_order_valid_records": int(round_valid.sum()), "events": {name: value["event_window_people"] for name, value in output["events"].items()}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
