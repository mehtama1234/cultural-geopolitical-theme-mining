#!/usr/bin/env python3
"""Build a bounded 2024 MEPS prescribed-medicine event layer."""

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
    parser.add_argument("rx_file", type=Path)
    parser.add_argument("hc256_file", type=Path)
    args = parser.parse_args()
    rx, _ = pyreadstat.read_dta(
        args.rx_file,
        usecols=["DUPERSID", "PANEL", "PERWT24F", "VARSTR", "VARPSU", "RXXP24X", "RXSF24X"],
    )
    people, _ = pyreadstat.read_dta(args.hc256_file, usecols=["DUPERSID", "PANEL", "INSURC24"])
    rx["PANELKEY"] = rx["PANEL"].astype(str)
    people["PANELKEY"] = people["PANEL"].astype(str)
    rx["KEY"] = rx["DUPERSID"].astype(str) + "|" + rx["PANELKEY"]
    people["KEY"] = people["DUPERSID"].astype(str) + "|" + people["PANELKEY"]
    people = people.drop_duplicates("KEY")
    merged = rx.merge(people[["KEY", "INSURC24"]], on="KEY", how="left", validate="many_to_one")
    weights = merged["PERWT24F"].to_numpy(float)
    positive = np.isfinite(weights) & (weights > 0)
    total_payment = merged["RXXP24X"].to_numpy(float)
    family_payment = merged["RXSF24X"].to_numpy(float)
    output: dict[str, object] = {
        "rx_event_file_records": len(rx),
        "positive_weight_events": int(positive.sum()),
        "person_link_missing": int(merged["INSURC24"].isna().sum()),
        "variance_method": "HC-254A VARSTR/VARPSU Taylor linearization; event-level estimates use PERWT24F",
        "documentation_boundary": "HC-254A represents people with prescribed-medicine purchases; person-level prevalence including non-purchasers must use HC-256.",
        "national": {
            "prescribed_purchases_millions": taylor_total_millions(merged, positive),
            "mean_total_payments_per_purchase": taylor_mean(merged, total_payment, positive),
            "mean_out_of_pocket_per_purchase": taylor_mean(merged, family_payment, positive),
        },
        "under65_insurance": {},
    }
    insurance = merged["INSURC24"].to_numpy(float)
    for code, label in INSURANCE_LABELS.items():
        group = positive & (insurance == code)
        output["under65_insurance"][label] = {
            "prescribed_purchases_millions": taylor_total_millions(merged, group),
            "mean_total_payments_per_purchase": taylor_mean(merged, total_payment, group),
            "mean_out_of_pocket_per_purchase": taylor_mean(merged, family_payment, group),
        }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
