#!/usr/bin/env python3
"""Acquire a reproducible Census CBP proxy for electronic repair activity."""

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
OUTPUT = ANALYSIS / "census-repair-industry-snapshot.json"
YEARS = range(2019, 2024)
NAICS = {
    "811211": "consumer electronics repair and maintenance",
    "811213": "communication equipment repair and maintenance",
}


def fetch(url: str) -> tuple[bytes, str]:
    data = urllib.request.urlopen(url, timeout=60).read()
    return data, "sha256:" + hashlib.sha256(data).hexdigest()


def parse_zip(data: bytes) -> list[dict[str, str]]:
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        name = archive.namelist()[0]
        text = archive.read(name).decode("utf-8-sig")
    return list(csv.DictReader(io.StringIO(text)))


def numeric(value: str) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def main() -> int:
    national = []
    states = []
    retrievals = []
    for year in YEARS:
        suffix = str(year)[2:]
        us_url = f"https://www2.census.gov/programs-surveys/cbp/datasets/{year}/cbp{suffix}us.zip"
        st_url = f"https://www2.census.gov/programs-surveys/cbp/datasets/{year}/cbp{suffix}st.zip"
        us_bytes, us_hash = fetch(us_url)
        st_bytes, st_hash = fetch(st_url)
        retrievals.extend([
            {"year": year, "geography": "us", "url": us_url, "artifact_sha256": us_hash},
            {"year": year, "geography": "state", "url": st_url, "artifact_sha256": st_hash},
        ])
        us_rows = parse_zip(us_bytes)
        st_rows = parse_zip(st_bytes)
        for row in us_rows:
            code = row.get("naics")
            if code not in NAICS or row.get("lfo") != "-":
                continue
            national.append({
                "year": year,
                "naics": code,
                "naics_label": NAICS[code],
                "establishments": numeric(row.get("est")),
                "employees": numeric(row.get("emp")),
                "annual_payroll_thousands_usd": numeric(row.get("ap")),
                "first_quarter_payroll_thousands_usd": numeric(row.get("qp1")),
                "noise_flags": {"establishments": row.get("est_nf"), "employees": row.get("emp_nf"), "annual_payroll": row.get("ap_nf"), "first_quarter_payroll": row.get("qp1_nf")},
                "suppression_or_noise_present": any(row.get(field, "") not in {"", "G", "H", "J", "N", "S"} for field in ("est_nf", "emp_nf", "ap_nf", "qp1_nf")),
            })
        for row in st_rows:
            code = row.get("naics")
            if code not in NAICS or row.get("lfo") != "-":
                continue
            states.append({
                "year": year,
                "state_fips": row.get("fipstate"),
                "naics": code,
                "naics_label": NAICS[code],
                "establishments": numeric(row.get("est")),
                "employees": numeric(row.get("emp")),
                "annual_payroll_thousands_usd": numeric(row.get("ap")),
                "first_quarter_payroll_thousands_usd": numeric(row.get("qp1")),
                "noise_flags": {"establishments": row.get("est_nf"), "employees": row.get("emp_nf"), "annual_payroll": row.get("ap_nf"), "first_quarter_payroll": row.get("qp1_nf")},
            })

    by_naics = {}
    for code in NAICS:
        rows = [row for row in national if row["naics"] == code]
        first, last = rows[0], rows[-1]
        by_naics[code] = {
            "label": NAICS[code],
            "first_year": first["year"],
            "last_year": last["year"],
            "establishment_change": (last["establishments"] - first["establishments"]) if first["establishments"] is not None and last["establishments"] is not None else None,
            "employee_change": (last["employees"] - first["employees"]) if first["employees"] is not None and last["employees"] is not None else None,
            "annual_payroll_change_thousands_usd": (last["annual_payroll_thousands_usd"] - first["annual_payroll_thousands_usd"]) if first["annual_payroll_thousands_usd"] is not None and last["annual_payroll_thousands_usd"] is not None else None,
        }
    payload = {
        "schema": "external-trend-intelligence.census-repair-industry-snapshot.v1",
        "acquisition_id": "census-cbp-electronic-repair-2019-2023",
        "status": "descriptive_industry_proxy_not_phone_outcome",
        "retrieved_at": "2026-10-31",
        "source": {
            "publisher": "U.S. Census Bureau",
            "dataset": "County Business Patterns",
            "documentation_url": "https://www.census.gov/data/developers/data-sets/cbp-zbp/cbp-api.html",
            "download_base": "https://www2.census.gov/programs-surveys/cbp/datasets/",
            "naics_definition_url": "https://www.census.gov/naics/federal_register_notices/agreements/naics_21.pdf",
            "retrievals": retrievals,
        },
        "coverage": {"years": list(YEARS), "national_row_count": len(national), "state_row_count": len(states), "naics": NAICS},
        "national": national,
        "state": states,
        "descriptive_readout": by_naics,
        "units": {
            "establishments": "count of establishments with paid employees",
            "employees": "employment during the week of March 12",
            "annual_payroll_thousands_usd": "annual payroll in thousands of US dollars",
            "first_quarter_payroll_thousands_usd": "first-quarter payroll in thousands of US dollars",
        },
        "uncertainty": "CBP suppresses or flags values using Census noise/suppression markers; this snapshot preserves flags but does not estimate sampling variance.",
        "interpretation_boundary": "NAICS 811211 covers consumer-electronics repair and NAICS 811213 covers communication-equipment repair, but neither isolates cell-phone repair transactions, policy exposure, prices, waiting time, device life, or repair versus replacement decisions.",
        "counter_signal": "Industry establishments, employment, and payroll can move because of broader electronics, telecommunications, and commercial repair activity even when household phone repair access does not change.",
        "falsifier": "A phone-specific outcome panel does not move with the industry proxy or shows different timing across policy-exposed and comparison geographies.",
        "pooling_decision": "do_not_pool_with_state_policy_or_global_ewaste",
        "next_action": "Use this only as a broad descriptive context series; acquire phone-specific transactions or consumer outcomes and verify policy effective dates before any causal or qualification claim.",
        "rights_basis": "Official Census public download; retain normalized values, source URLs, checksums, and suppression flags rather than redistributing raw ZIP files through the frontend.",
        "boundary": "This artifact is an official industry proxy and acquisition result, not evidence that right-to-repair policy changed phone repair demand or consumer outcomes.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(national)} national rows; {len(states)} state rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
