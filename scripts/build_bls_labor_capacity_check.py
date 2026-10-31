#!/usr/bin/env python3
"""Build a comparable, same-publisher labor-capacity mechanism check."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis" / "projects" / "ai-work-control" / "data"
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "bls-labor-capacity-mechanism-check.json"
JOLTS = DATA / "bls-jolts-selected-industries-2020-2025-derived.json"
EARNINGS = DATA / "bls-ces-industry-earnings-2022-2025-derived.json"
YEARS = ["2022", "2023", "2024", "2025"]


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def series_row(name: str, earnings_name: str, jolts: dict, earnings: dict) -> dict:
    return {
        "industry": name,
        "geography": "United States",
        "periods": YEARS,
        "job_openings_rate_percent": [jolts[name][year]["job_openings_rate"] for year in YEARS],
        "hires_rate_percent": [jolts[name][year]["hires_rate"] for year in YEARS],
        "quits_rate_percent": [jolts[name][year]["quits_rate"] for year in YEARS],
        "average_hourly_earnings_dollars": [earnings[earnings_name][year] for year in YEARS],
        "opening_rate_change_2022_to_2025_percentage_points": round(jolts[name]["2025"]["job_openings_rate"] - jolts[name]["2022"]["job_openings_rate"], 4),
        "hires_rate_change_2022_to_2025_percentage_points": round(jolts[name]["2025"]["hires_rate"] - jolts[name]["2022"]["hires_rate"], 4),
        "earnings_change_2022_to_2025_dollars": round(earnings[earnings_name]["2025"] - earnings[earnings_name]["2022"], 4),
        "earnings_change_2022_to_2025_percent": round((earnings[earnings_name]["2025"] / earnings[earnings_name]["2022"] - 1) * 100, 2),
    }


def main() -> int:
    jolts_doc = load(JOLTS)
    earnings_doc = load(EARNINGS)
    jolts = jolts_doc["annual_mean_of_monthly_rates_percent"]
    earnings = earnings_doc["annual_mean_of_monthly_dollars_per_hour"]
    rows = [
        series_row("600000", "education_and_health_services", jolts, earnings),
        series_row("300000", "manufacturing", jolts, earnings),
    ]
    rows[0]["industry_label"] = "education_and_health_services"
    rows[1]["industry_label"] = "manufacturing"
    payload = {
        "schema": "external-trend-intelligence.bls-labor-capacity-mechanism-check.v1",
        "status": "held_mechanism_check_same_publisher",
        "question": "Do compatible labor-market indicators show persistent capacity pressure in education and health services, with manufacturing as a broad comparator?",
        "source_family": "Bureau of Labor Statistics",
        "source_publisher_dependence": "Both JOLTS and CES are BLS products; this is triangulation within one publisher, not independent-source confirmation.",
        "rows": rows,
        "observed_pattern": "Education and health services show falling annual-average job-openings and hires rates from 2022 to 2025 while average hourly earnings rise. Manufacturing shows the same direction, so the result may reflect broad labor-market cooling plus wage adjustment rather than a sector-specific scarcity mechanism.",
        "supporting_signal": "Hourly earnings rose in education and health services from $31.88 to $35.59 (11.64%) between 2022 and 2025.",
        "counter_signal": "Education and health job-openings rate fell from 8.1917% to 5.3750% and hires rate fell from 3.5083% to 2.9750%; this does not by itself show worsening unfilled capacity.",
        "alternative_explanation": "Hiring normalization, reduced labor churn, composition changes, inflation, or delayed wage adjustment could produce the observed combination without a persistent staffing bottleneck.",
        "falsifier": "A compatible sector-specific source showing stable or rising unmet labor demand, filled/requested hours, vacancy duration, or service rationing after 2025 would be needed to distinguish capacity pressure from broad labor-market cooling.",
        "methods": {
            "jolts": jolts_doc["method"],
            "ces": earnings_doc["method"],
            "period_alignment": "Annual means of monthly observations; common comparison window 2022-2025.",
            "units": "JOLTS rates are percentages; CES is dollars per hour. They are shown side-by-side, not pooled.",
        },
        "sources": [
            {"artifact": str(JOLTS.relative_to(ROOT)), "source_url": jolts_doc["source_url"], "retrieval_hash": jolts_doc["raw_response_sha256"], "unit": "annual mean of monthly rates, percent"},
            {"artifact": str(EARNINGS.relative_to(ROOT)), "source_url": earnings_doc["source_url"], "retrieval_hash": earnings_doc["raw_response_sha256"], "unit": "annual mean of monthly average hourly earnings, dollars per hour"},
        ],
        "boundary": "This is a descriptive same-publisher mechanism challenge. It does not estimate caregiver shortages, service quality, unmet care demand, causality, or company exposure, and it does not clear the independent-source qualification gate.",
        "next_test": "Acquire a separate source family with a compatible vacancy, filled-hours, or service-rationing measure and pre-specify a post-2025 holdout.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} comparator rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
