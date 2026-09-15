#!/usr/bin/env python3
"""Build a bounded JOLTS-by-union-representation context comparison."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/ai-work-control/data"
OUT = ROOT / "analysis/records/us-bls-jolts-union-industry-context-2025.json"
UNION = {
    "manufacturing": {"employed_thousand": 14371, "membership_rate": 7.7},
    "professional_and_business_services": {"employed_thousand": 17700, "membership_rate": 2.1},
    "education_and_health_services": {"employed_thousand": 25522, "membership_rate": 8.2},
    "leisure_and_hospitality": {"employed_thousand": 12211, "membership_rate": 3.0},
}
INDUSTRY_CODES = {"manufacturing": "300000", "professional_and_business_services": "540099", "education_and_health_services": "600000", "leisure_and_hospitality": "700000"}


def main() -> int:
    derived = json.loads((DATA / "bls-jolts-selected-industries-2020-2025-derived.json").read_text())
    observations = []
    for name, union in UNION.items():
        code = INDUSTRY_CODES[name]
        jolts = derived["annual_mean_of_monthly_rates_percent"][code]["2025"]
        label = name.replace("_", " ")
        observations.append({
            "period": f"2025; {label}; JOLTS establishment mobility",
            "denominator": {"value": 12, "unit": "monthly seasonally adjusted JOLTS observations", "value_type": "time_series_mean"},
            "measures": {"quits_rate": {"value": jolts["quits_rate"], "unit": "percent annual arithmetic mean of monthly rate", "value_type": "estimated_rate"}, "job_openings_rate": {"value": jolts["job_openings_rate"], "unit": "percent annual arithmetic mean of monthly rate", "value_type": "estimated_rate"}},
            "method": "BLS JOLTS 2025 annual arithmetic mean of monthly seasonally adjusted establishment rates.",
            "uncertainty": "JOLTS measures establishments and not unique workers; rates are revised and do not identify transition reasons or job quality.",
            "subgroup": label,
            "counterinterpretation": "Mobility rates cannot be read as worker power or as outcomes caused by representation.",
            "source_url": "https://api.bls.gov/publicAPI/v2/timeseries/data/",
            "retrieval_hash": f"sha256:{derived['raw_response_sha256']}",
            "status": "compared",
        })
        observations.append({
            "period": f"2025; {label}; CPS union representation context",
            "denominator": {"value": union["employed_thousand"], "unit": "thousand employed wage and salary workers in industry", "value_type": "survey_population"},
            "measures": {"union_membership_rate": {"value": union["membership_rate"], "unit": "percent of CPS industry denominator", "value_type": "share"}},
            "method": "BLS CPS Union Members 2025 Table 3 annual average; membership is a descriptive institutional-representation measure.",
            "uncertainty": "CPS survey and classification uncertainty apply; BLS states 2025 annual estimates exclude October and are not strictly comparable with prior annual averages.",
            "subgroup": label,
            "counterinterpretation": "Membership does not measure practical schedule control, grievance success, autonomy, or the causal effect of a union on JOLTS mobility.",
            "source_url": "https://www.bls.gov/news.release/union2.t03.htm",
            "retrieval_hash": "sha256:8b8e3eacf651d192f79014a60e56308b7548e46d92be3094693fc4b216d9a094",
            "status": "observed",
        })
    record = {
        "format": "us-trend-observation-record-v1",
        "trend_id": "us-bls-jolts-union-industry-context-2025",
        "title": "Sector mobility and formal union membership differ across US industries",
        "theme_ids": ["work", "voice", "cost"],
        "program_theme_ids": ["work_control_bargaining", "unequal_exposure_status", "firm_sector_market_power", "household_room_consumption"],
        "source_unit": "BLS JOLTS establishment rates and CPS union-affiliation industry estimates",
        "geography": "United States; selected industries",
        "observations": observations,
        "related_sources": [{"source_url": "https://www.bls.gov/news.release/union2.t03.htm", "claim": "CPS industry union-membership estimates provide institutional context for selected JOLTS sectors.", "status": "reported", "access_boundary": "The two BLS programs use different populations, sampling frames, measures, and denominators; this is a conditioning comparison, not a joined worker dataset."}],
        "boundary": "This record places 2025 sector-level establishment mobility beside CPS formal union membership. It does not estimate a causal representation effect, worker bargaining power, job quality, pay, schedule control, household security, or political meaning."
    }
    OUT.write_text(json.dumps(record, indent=2) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(observations)} observations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
