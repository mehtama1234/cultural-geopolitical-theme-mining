#!/usr/bin/env python3
"""Build a bounded 2024 MEPS hospital-inpatient event layer."""

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
    parser.add_argument("inpatient_file", type=Path)
    parser.add_argument("hc256_file", type=Path)
    args = parser.parse_args()
    ip, _ = pyreadstat.read_dta(
        args.inpatient_file,
        usecols=["DUPERSID", "PANEL", "PERWT24F", "VARSTR", "VARPSU", "IPXP24X", "IPFSF24X", "IPDSF24X", "NUMNIGHX", "EMERROOM"],
    )
    people, _ = pyreadstat.read_dta(args.hc256_file, usecols=["DUPERSID", "PANEL", "INSURC24"])
    ip["PANELKEY"] = ip["PANEL"].astype(str)
    people["PANELKEY"] = people["PANEL"].astype(str)
    ip["KEY"] = ip["DUPERSID"].astype(str) + "|" + ip["PANELKEY"]
    people["KEY"] = people["DUPERSID"].astype(str) + "|" + people["PANELKEY"]
    people = people.drop_duplicates("KEY")
    merged = ip.merge(people[["KEY", "INSURC24"]], on="KEY", how="left", validate="many_to_one")
    weights = merged["PERWT24F"].to_numpy(float)
    positive = np.isfinite(weights) & (weights > 0)
    total_payment = merged["IPXP24X"].to_numpy(float)
    family_payment = (merged["IPFSF24X"] + merged["IPDSF24X"]).to_numpy(float)
    output: dict[str, object] = {
        "inpatient_event_file_records": len(ip),
        "positive_weight_events": int(positive.sum()),
        "person_link_missing": int(merged["INSURC24"].isna().sum()),
        "variance_method": "HC-254D VARSTR/VARPSU Taylor linearization; event-level estimates use PERWT24F",
        "documentation_boundary": "HC-254D represents people with reported inpatient stays; person-level prevalence including non-users must use HC-256.",
        "national": {
            "inpatient_stays_millions": taylor_total_millions(merged, positive),
            "mean_total_payments_per_stay": taylor_mean(merged, total_payment, positive),
            "mean_self_family_payment_per_stay": taylor_mean(merged, family_payment, positive),
            "mean_nights_per_stay": taylor_mean(merged, merged["NUMNIGHX"].to_numpy(float), positive),
            "emergency_room_start_share": taylor_mean(merged, (merged["EMERROOM"].to_numpy(float) == 1).astype(float), positive),
        },
        "under65_insurance": {},
    }
    insurance = merged["INSURC24"].to_numpy(float)
    for code, label in INSURANCE_LABELS.items():
        group = positive & (insurance == code)
        output["under65_insurance"][label] = {
            "inpatient_stays_millions": taylor_total_millions(merged, group),
            "mean_total_payments_per_stay": taylor_mean(merged, total_payment, group),
            "mean_self_family_payment_per_stay": taylor_mean(merged, family_payment, group),
            "mean_nights_per_stay": taylor_mean(merged, merged["NUMNIGHX"].to_numpy(float), group),
        }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
