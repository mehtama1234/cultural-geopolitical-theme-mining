#!/usr/bin/env python3
"""Join Treasury 2022 ZIP metrics to 2022 ACS ZCTA socioeconomic context."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/us-housing-insurance-risk/data"
OUT = DATA / "treasury-fio-census-zcta-2022-join.json"


def read_pipe(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="") as handle:
        rows = csv.DictReader(handle, delimiter="|")
        result = {}
        for row in rows:
            geo = row.get("GEO_ID", "")
            if not geo.startswith("860Z200US"):
                continue
            result[geo.removeprefix("860Z200US")] = row
        return result


def main() -> int:
    income = read_pipe(DATA / "acs2022-b19013.dat")
    poverty = read_pipe(DATA / "acs2022-b17001.dat")
    tenure = read_pipe(DATA / "acs2022-b25003.dat")
    context = {}
    for zcta in sorted(set(income) & set(poverty) & set(tenure)):
        try:
            median_income = int(income[zcta]["B19013_E001"])
            poverty_total = int(poverty[zcta]["B17001_E001"])
            poverty_count = int(poverty[zcta]["B17001_E002"]) + int(poverty[zcta]["B17001_E017"])
            tenure_total = int(tenure[zcta]["B25003_E001"])
            owners = int(tenure[zcta]["B25003_E002"])
            renters = int(tenure[zcta]["B25003_E003"])
        except (KeyError, TypeError, ValueError):
            continue
        if median_income < 0 or poverty_total <= 0 or tenure_total <= 0:
            continue
        context[zcta] = {
            "median_income": median_income,
            "poverty_rate": poverty_count / poverty_total,
            "owner_share": owners / tenure_total,
            "renter_share": renters / tenure_total,
        }

    buckets = defaultdict(list)
    ws = load_workbook(DATA / "treasury-fio-homeowners-insurance-2018-2022.xlsx", read_only=True, data_only=True)["Supporting Underlying Metrics"]
    total_2022 = 0
    matched_2022 = 0
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[1] != 2022 or row[0] is None or row[6] is None or row[7] is None:
            continue
        total_2022 += 1
        zcta = str(int(row[0])).zfill(5)
        c = context.get(zcta)
        if c is None:
            continue
        matched_2022 += 1
        if c["median_income"] < 50000:
            income_bucket = "below_50000"
        elif c["median_income"] < 100000:
            income_bucket = "50000_to_99999"
        else:
            income_bucket = "at_least_100000"
        if c["poverty_rate"] >= 0.20:
            poverty_bucket = "poverty_at_least_20_percent"
        elif c["poverty_rate"] < 0.10:
            poverty_bucket = "poverty_below_10_percent"
        else:
            poverty_bucket = "poverty_10_to_199_percent"
        if c["owner_share"] < 0.50:
            tenure_bucket = "owner_share_below_50_percent"
        elif c["owner_share"] >= 0.75:
            tenure_bucket = "owner_share_at_least_75_percent"
        else:
            tenure_bucket = "owner_share_50_to_749_percent"
        values = {"premium_per_policy": float(row[6]), "nonrenewal_rate": float(row[7]), "claim_severity": float(row[4]) if row[4] is not None else None}
        for dimension, bucket in [("income", income_bucket), ("poverty", poverty_bucket), ("tenure", tenure_bucket)]:
            buckets[(dimension, bucket)].append(values)

    summaries = {}
    for (dimension, bucket), values in sorted(buckets.items()):
        def mean(key: str):
            x = [v[key] for v in values if v[key] is not None]
            return round(sum(x) / len(x), 6) if x else None
        summaries[f"{dimension}:{bucket}"] = {"matched_zip_year_rows": len(values), "mean_premium_per_policy": mean("premium_per_policy"), "mean_nonrenewal_rate": mean("nonrenewal_rate"), "mean_claim_severity": mean("claim_severity")}
    result = {
        "format": "treasury-fio-census-zcta-join-v1",
        "period": "2022",
        "treasury_input": "treasury-fio-homeowners-insurance-2018-2022.xlsx",
        "census_inputs": ["acs2022-b19013.dat", "acs2022-b17001.dat", "acs2022-b25003.dat"],
        "treasury_2022_rows_considered": total_2022,
        "matched_2022_rows": matched_2022,
        "match_rate": round(matched_2022 / total_2022, 6) if total_2022 else None,
        "classification": "Descriptive grouping by matched 2022 ACS ZCTA context; Treasury five-digit ZIP codes are matched to same-text ZCTA codes as an approximation.",
        "summaries": summaries,
        "limits": ["ZIP codes and ZCTAs are not identical geographies.", "The Treasury workbook is not a complete insurer or policy census and its metrics are not household-level.", "ACS context and insurance metrics are joined descriptively; no causal or individual affordability inference is identified.", "Results are unweighted means of matched ZIP-year rows, not policy-weighted estimates."],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"treasury_2022_rows_considered": total_2022, "matched_2022_rows": matched_2022, "match_rate": result["match_rate"], "output": str(OUT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
