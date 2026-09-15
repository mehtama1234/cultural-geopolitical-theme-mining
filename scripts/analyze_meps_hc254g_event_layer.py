#!/usr/bin/env python3
"""Build a bounded 2024 MEPS office-visit event layer.

Uses the event file's VARSTR/VARPSU Taylor design for event-level uncertainty,
following the HC-254G documentation. Person-level coverage categories are
appended from HC-256 by DUPERSID and PANEL; event rows retain their own
PERWT24F and are not treated as person-level prevalence.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


INSURANCE_LABELS = {
    1: "under65_private",
    2: "under65_public_only",
    3: "under65_uninsured",
}


def taylor_mean(df: pd.DataFrame, value: np.ndarray, mask: np.ndarray) -> dict[str, float | int]:
    weights = df["PERWT24F"].to_numpy(float)
    base = np.asarray(mask) & np.isfinite(weights) & (weights > 0) & np.isfinite(value)
    if not int(base.sum()):
        return {"valid_events": 0, "estimate": None, "standard_error": None, "ci95_low": None, "ci95_high": None}
    den = float(weights[base].sum())
    estimate = float(np.sum(weights[base] * value[base]) / den)
    linearized = weights[base] * (value[base] - estimate)
    work = pd.DataFrame({
        "stratum": df.loc[base, "VARSTR"].to_numpy(),
        "psu": df.loc[base, "VARPSU"].to_numpy(),
        "linearized": linearized,
    })
    psu = work.groupby(["stratum", "psu"], as_index=False)["linearized"].sum()
    variance_numerator = 0.0
    for _, group in psu.groupby("stratum"):
        count = len(group)
        if count > 1:
            variance_numerator += count / (count - 1) * float(((group["linearized"] - group["linearized"].mean()) ** 2).sum())
    standard_error = float(np.sqrt(variance_numerator) / den)
    return {
        "valid_events": int(base.sum()),
        "estimate": estimate,
        "standard_error": standard_error,
        "ci95_low": estimate - 1.96 * standard_error,
        "ci95_high": estimate + 1.96 * standard_error,
    }


def taylor_total_millions(df: pd.DataFrame, mask: np.ndarray) -> dict[str, float | int]:
    weights = df["PERWT24F"].to_numpy(float)
    base = np.asarray(mask) & np.isfinite(weights) & (weights > 0)
    total = float(weights[base].sum())
    work = pd.DataFrame({
        "stratum": df.loc[base, "VARSTR"].to_numpy(),
        "psu": df.loc[base, "VARPSU"].to_numpy(),
        "linearized": weights[base],
    })
    psu = work.groupby(["stratum", "psu"], as_index=False)["linearized"].sum()
    variance = 0.0
    for _, group in psu.groupby("stratum"):
        count = len(group)
        if count > 1:
            variance += count / (count - 1) * float(((group["linearized"] - group["linearized"].mean()) ** 2).sum())
    scale = 1_000_000.0
    estimate = total / scale
    standard_error = float(np.sqrt(variance) / scale)
    return {
        "valid_events": int(base.sum()),
        "estimate_millions": estimate,
        "standard_error_millions": standard_error,
        "ci95_low_millions": estimate - 1.96 * standard_error,
        "ci95_high_millions": estimate + 1.96 * standard_error,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("event_file", type=Path)
    parser.add_argument("hc256_file", type=Path)
    args = parser.parse_args()
    event_fields = [
        "DUPERSID", "PANEL", "PERWT24F", "VARSTR", "VARPSU", "OBXP24X", "OBSF24X",
        "TELEHEALTHFLAG", "SEEDOC_M18",
    ]
    events, _ = pyreadstat.read_dta(args.event_file, usecols=event_fields)
    people, _ = pyreadstat.read_dta(args.hc256_file, usecols=["DUPERSID", "PANEL", "INSURC24"])
    events["PANELKEY"] = events["PANEL"].astype(str)
    people["PANELKEY"] = people["PANEL"].astype(str)
    events["KEY"] = events["DUPERSID"].astype(str) + "|" + events["PANELKEY"]
    people["KEY"] = people["DUPERSID"].astype(str) + "|" + people["PANELKEY"]
    people = people.drop_duplicates("KEY")
    merged = events.merge(people[["KEY", "INSURC24"]], on="KEY", how="left", validate="many_to_one")
    weights = merged["PERWT24F"].to_numpy(float)
    positive = np.isfinite(weights) & (weights > 0)
    total_payment = merged["OBXP24X"].to_numpy(float)
    family_payment = merged["OBSF24X"].to_numpy(float)
    output: dict[str, object] = {
        "event_file_records": len(events),
        "positive_weight_events": int(positive.sum()),
        "person_link_missing": int(merged["INSURC24"].isna().sum()),
        "variance_method": "HC-254G VARSTR/VARPSU Taylor linearization; event-level estimates use PERWT24F",
        "documentation_boundary": "HC-254G event files include people with office-based visits; person-level analyses including people with no office-based visit must use HC-256.",
        "national": {
            "office_visits_millions": taylor_total_millions(merged, positive),
            "mean_total_payments_per_visit": taylor_mean(merged, total_payment, positive),
            "mean_out_of_pocket_per_visit": taylor_mean(merged, family_payment, positive),
            "positive_payment_share": taylor_mean(merged, (total_payment > 0).astype(float), positive),
            "telehealth_share": taylor_mean(merged, (merged["TELEHEALTHFLAG"].to_numpy(float) == 1).astype(float), positive),
            "physician_visit_share": taylor_mean(merged, (merged["SEEDOC_M18"].to_numpy(float) == 1).astype(float), positive),
        },
        "under65_insurance": {},
    }
    insurance = merged["INSURC24"].to_numpy(float)
    for code, label in INSURANCE_LABELS.items():
        group = positive & (insurance == code)
        output["under65_insurance"][label] = {
            "office_visits_millions": taylor_total_millions(merged, group),
            "mean_total_payments_per_visit": taylor_mean(merged, total_payment, group),
            "mean_out_of_pocket_per_visit": taylor_mean(merged, family_payment, group),
            "positive_payment_share": taylor_mean(merged, (total_payment > 0).astype(float), group),
        }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
