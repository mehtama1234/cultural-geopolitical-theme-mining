#!/usr/bin/env python3
"""Build a bounded sector context record combining mobility, representation, and pay."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/ai-work-control/data"
OUT = ROOT / "analysis/records/us-bls-jolts-union-earnings-industry-context-2025.json"


def main() -> int:
    ces = json.loads((DATA / "bls-ces-industry-earnings-2022-2025-derived.json").read_text())
    jolts = json.loads((DATA / "bls-jolts-selected-industries-2020-2025-derived.json").read_text())
    union = {"manufacturing": 7.7, "professional_and_business_services": 2.1, "education_and_health_services": 8.2, "leisure_and_hospitality": 3.0}
    out = []
    for name, membership in union.items():
        out.append({"period": f"2025; {name.replace('_', ' ')}; mobility, representation, and pay context", "denominator": {"value": 12, "unit": "monthly BLS observations per establishment/earnings series; CPS denominator retained separately", "value_type": "comparison_frame"}, "measures": {"jolts_quits_rate": {"value": jolts["annual_mean_of_monthly_rates_percent"][{"manufacturing": "300000", "professional_and_business_services": "540099", "education_and_health_services": "600000", "leisure_and_hospitality": "700000"}[name]]["2025"]["quits_rate"], "unit": "percent annual mean of seasonally adjusted monthly establishment rate", "value_type": "estimated_rate"}, "cps_union_membership_rate": {"value": membership, "unit": "percent of 2025 CPS industry denominator", "value_type": "share"}, "ces_average_hourly_earnings": {"value": ces["annual_mean_of_monthly_dollars_per_hour"][name]["2025"], "unit": "US dollars per hour, annual mean of seasonally adjusted monthly average for all employees", "value_type": "estimated_average"}}, "method": "Descriptive cross-source comparison of BLS JOLTS, CPS Union Members Table 3, and CES average hourly earnings; no records are joined at worker level.", "uncertainty": "Sources use different populations, frames, weighting, and denominators; CES is an establishment average, JOLTS an establishment rate, and CPS 2025 annual estimates exclude October.", "subgroup": name.replace('_', ' '), "counterinterpretation": "Sector differences in pay, representation, or quits do not establish worker control, job quality, or a causal representation effect.", "source_url": "https://api.bls.gov/publicAPI/v2/timeseries/data/", "retrieval_hash": f"sha256:{ces['raw_response_sha256']}", "status": "compared"})
    record = {"format": "us-trend-observation-record-v1", "trend_id": "us-bls-jolts-union-earnings-industry-context-2025", "title": "Sector mobility, formal representation, and average pay form different US workplace contexts", "theme_ids": ["work", "voice", "cost"], "program_theme_ids": ["work_control_bargaining", "unequal_exposure_status", "firm_sector_market_power", "household_room_consumption"], "source_unit": "BLS JOLTS, CPS Union Members, and CES industry aggregates", "geography": "United States; selected industries", "observations": out, "related_sources": [{"source_url": "https://www.bls.gov/news.release/union2.t03.htm", "claim": "CPS industry union-membership rates provide formal-representation context.", "status": "reported", "access_boundary": "CPS 2025 estimates exclude October and are not strictly comparable with earlier annual averages."}], "boundary": "This record places sector-level mobility, formal representation, and average hourly earnings beside one another. It does not estimate causal union effects, worker bargaining power, job quality, schedule control, household security, or political meaning."}
    OUT.write_text(json.dumps(record, indent=2) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(out)} observations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
