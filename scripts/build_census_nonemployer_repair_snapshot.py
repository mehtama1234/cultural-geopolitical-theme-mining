#!/usr/bin/env python3
"""Acquire the Census NES repair-industry proxy with checksummed downloads."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "census-nonemployer-repair-snapshot.json"
YEARS = range(2019, 2025)
# NES publishes repair at 5-digit 81121; it does not split CBP's 811211/811213.
NAICS = {"81121": "electronic and precision equipment repair and maintenance"}


def fetch(url: str) -> tuple[bytes, str]:
    data = urllib.request.urlopen(url, timeout=60).read()
    return data, "sha256:" + hashlib.sha256(data).hexdigest()


def parse_zip(data: bytes) -> list[dict[str, str]]:
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        text = archive.read(archive.namelist()[0]).decode("utf-8-sig")
    return list(csv.DictReader(io.StringIO(text)))


def numeric(value: str) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def main() -> int:
    national: list[dict] = []
    states: list[dict] = []
    retrievals: list[dict] = []
    for year in YEARS:
        suffix = str(year)[2:]
        base = f"https://www2.census.gov/programs-surveys/nonemployer-statistics/datasets/{year}/historical-datasets"
        us_url = f"{base}/nonemp{suffix}us.zip"
        st_url = f"{base}/nonemp{suffix}st.zip"
        us_bytes, us_hash = fetch(us_url)
        st_bytes, st_hash = fetch(st_url)
        retrievals.extend([
            {"year": year, "geography": "us", "url": us_url, "artifact_sha256": us_hash},
            {"year": year, "geography": "state", "url": st_url, "artifact_sha256": st_hash},
        ])
        for row in parse_zip(us_bytes):
            if row.get("NAICS") not in NAICS or row.get("LFO") != "-" or row.get("RCPTOT_SIZE") != "001":
                continue
            national.append({
                "year": year, "naics": row["NAICS"], "naics_label": NAICS[row["NAICS"]],
                "establishments": numeric(row.get("ESTAB")),
                "receipts_thousands_usd": numeric(row.get("RCPTOT")),
                "establishments_flag": row.get("ESTAB_F"), "receipts_flag": row.get("RCPTOT_F"),
            })
        for row in parse_zip(st_bytes):
            if row.get("NAICS") not in NAICS or row.get("LFO") != "-":
                continue
            states.append({
                "year": year, "state_fips": row.get("ST"), "naics": row["NAICS"],
                "naics_label": NAICS[row["NAICS"]], "establishments": numeric(row.get("ESTAB")),
                "receipts_thousands_usd": numeric(row.get("RCPTOT")),
                "establishments_flag": row.get("ESTAB_F"), "receipts_flag": row.get("RCPTOT_F"),
            })
    first, last = national[0], national[-1]
    payload = {
        "schema": "external-trend-intelligence.census-nonemployer-repair-snapshot.v1",
        "acquisition_id": "census-nes-electronic-repair-2019-2024",
        "status": "descriptive_nonemployer_industry_proxy_not_phone_outcome",
        "retrieved_at": "2026-10-31",
        "source": {
            "publisher": "U.S. Census Bureau", "dataset": "Nonemployer Statistics",
            "program_url": "https://www.census.gov/programs-surveys/nonemployer-statistics.html",
            "dataset_url": "https://www.census.gov/data/datasets/2024/econ/nonemployer-statistics/2024-ns.html",
            "download_base": "https://www2.census.gov/programs-surveys/nonemployer-statistics/datasets/",
            "retrievals": retrievals,
        },
        "coverage": {"years": list(YEARS), "national_row_count": len(national), "state_row_count": len(states), "naics": NAICS},
        "national": national, "state": states,
        "descriptive_readout": {
            "first_year": first["year"], "last_year": last["year"],
            "establishment_change": last["establishments"] - first["establishments"],
            "receipts_change_thousands_usd": last["receipts_thousands_usd"] - first["receipts_thousands_usd"],
        },
        "units": {"establishments": "nonemployer businesses reported by Census", "receipts_thousands_usd": "gross receipts in thousands of US dollars"},
        "uncertainty": "NES is based on administrative tax records and preserves Census suppression/noise flags; it does not provide sampling variance here.",
        "interpretation_boundary": "NAICS 81121 is a broad five-digit repair category. It does not isolate cell-phone repair transactions, policy exposure, prices, waiting time, device life, or repair versus replacement decisions, and nonemployer establishments are not workers or jobs.",
        "counter_signal": "Nonemployer repair counts or receipts can move because of tax classification, business entry/exit, broader equipment repair, inflation, or reporting changes without household phone-repair access changing.",
        "pooling_decision": "do_not_pool_with_state_policy_global_ewaste_or_cbp_paid_employee_series",
        "falsifier": "A phone-specific outcome panel does not move with this broad nonemployer proxy or shows different timing across policy-exposed and comparison geographies.",
        "next_action": "Use as small-business context only; acquire phone-specific transactions or consumer outcomes before any policy, market, or causal claim.",
        "rights_basis": "Official Census public downloads; retain normalized values, source URLs, checksums, and flags rather than raw ZIP files in the frontend.",
        "boundary": "This is a reproducible external industry proxy, not evidence that right-to-repair policy changed phone repair demand or consumer outcomes.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(national)} national rows; {len(states)} state rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
