#!/usr/bin/env python3
"""Build a bounded 2024 MEPS emergency-room event layer."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat

from analyze_meps_hc254g_event_layer import INSURANCE_LABELS, taylor_mean, taylor_total_millions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("er_file", type=Path)
    parser.add_argument("hc256_file", type=Path)
    args = parser.parse_args()
    er, _ = pyreadstat.read_dta(
        args.er_file,
        usecols=["DUPERSID", "PANEL", "PERWT24F", "VARSTR", "VARPSU", "ERXP24X", "ERFSF24X", "ERDSF24X"],
    )
    people, _ = pyreadstat.read_dta(args.hc256_file, usecols=["DUPERSID", "PANEL", "INSURC24"])
    er["PANELKEY"] = er["PANEL"].astype(str)
    people["PANELKEY"] = people["PANEL"].astype(str)
    er["KEY"] = er["DUPERSID"].astype(str) + "|" + er["PANELKEY"]
    people["KEY"] = people["DUPERSID"].astype(str) + "|" + people["PANELKEY"]
    people = people.drop_duplicates("KEY")
    merged = er.merge(people[["KEY", "INSURC24"]], on="KEY", how="left", validate="many_to_one")
    weights = merged["PERWT24F"].to_numpy(float)
    positive = np.isfinite(weights) & (weights > 0)
    total_payment = merged["ERXP24X"].to_numpy(float)
    family_payment = (merged["ERFSF24X"] + merged["ERDSF24X"]).to_numpy(float)
    output: dict[str, object] = {
        "er_event_file_records": len(er),
        "positive_weight_events": int(positive.sum()),
        "person_link_missing": int(merged["INSURC24"].isna().sum()),
        "variance_method": "HC-254E VARSTR/VARPSU Taylor linearization; event-level estimates use PERWT24F",
        "documentation_boundary": "HC-254E represents people with reported emergency-room events; person-level prevalence including non-users must use HC-256.",
        "national": {
            "emergency_room_visits_millions": taylor_total_millions(merged, positive),
            "mean_total_payments_per_visit": taylor_mean(merged, total_payment, positive),
            "mean_self_family_payment_per_visit": taylor_mean(merged, family_payment, positive),
        },
        "under65_insurance": {},
    }
    insurance = merged["INSURC24"].to_numpy(float)
    for code, label in INSURANCE_LABELS.items():
        group = positive & (insurance == code)
        output["under65_insurance"][label] = {
            "emergency_room_visits_millions": taylor_total_millions(merged, group),
            "mean_total_payments_per_visit": taylor_mean(merged, total_payment, group),
            "mean_self_family_payment_per_visit": taylor_mean(merged, family_payment, group),
        }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
