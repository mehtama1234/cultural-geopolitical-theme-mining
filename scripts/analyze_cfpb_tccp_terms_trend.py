"""Reproduce the descriptive CFPB TCCP 2024/2025 offer-surface comparison."""

from __future__ import annotations

import hashlib
import io
import json
import urllib.request
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "2024H2": "https://files.consumerfinance.gov/f/documents/cfpb_tccp-data_2024-12-31_uYJ9Krf.xlsx",
    "2025H2": "https://files.consumerfinance.gov/f/documents/cfpb_tccp-data_2025-12-31.xlsx",
}


def fetch(url: str) -> tuple[bytes, str]:
    with urllib.request.urlopen(url, timeout=60) as response:
        payload = response.read()
    return payload, hashlib.sha256(payload).hexdigest()


def summarize(payload: bytes) -> dict:
    frame = pd.read_excel(io.BytesIO(payload), header=9)
    def numeric(name: str) -> pd.Series:
        return pd.to_numeric(frame[name], errors="coerce")

    return {
        "rows": int(len(frame)),
        "columns": int(len(frame.columns)),
        "unique_institutions": int(frame["Institution Name"].nunique()),
        "unique_products": int(frame["Product Name"].nunique()),
        "purchase_apr_offered": int((frame["Purchase APR Offered?"] == "Yes").sum()),
        "credit_tier_apr_variation": int((frame["Purchase APR Vary by Credit Tier"] == "Yes").sum()),
        "intro_apr_offered": int((frame["Introductory APR Offered?"] == "Yes").sum()),
        "balance_transfer_offered": int((frame["Balance Transfer Offered?"] == "Yes").sum()),
        "late_fees_offered": int((frame["Late Fees?"] == "Yes").sum()),
        "cashback_rewards": int(frame["Rewards"].fillna("").str.contains("Cashback rewards", case=False).sum()),
        "purchase_apr_median_percent": round(float(numeric("Purchase APR median").median() * 100), 2),
        "purchase_apr_min_median_percent": round(float(numeric("Purchase APR min").median() * 100), 2),
        "purchase_apr_max_median_percent": round(float(numeric("Purchase APR max").median() * 100), 2),
        "annual_fee_numeric_rows": int(numeric("Annual Fee").notna().sum()),
        "annual_fee_median_dollars": round(float(numeric("Annual Fee").median()), 2),
        "late_fee_numeric_rows": int(numeric("Late Fee ($)").notna().sum()),
        "late_fee_median_dollars": round(float(numeric("Late Fee ($)").median()), 2),
    }


def main() -> None:
    output = {}
    for period, url in FILES.items():
        payload, digest = fetch(url)
        output[period] = {"source_url": url, "sha256": f"sha256:{digest}", "summary": summarize(payload)}
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
