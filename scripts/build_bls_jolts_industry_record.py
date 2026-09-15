#!/usr/bin/env python3
"""Build the validated selected-industry JOLTS trend record."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/ai-work-control/data"
OUT = ROOT / "analysis/records/us-bls-jolts-selected-industry-mobility-2022-2025.json"


def main() -> int:
    derived = json.loads((DATA / "bls-jolts-selected-industries-2020-2025-derived.json").read_text())
    observations = []
    labels = derived["industries"]
    for code, label in labels.items():
        for year in ("2022", "2025"):
            observations.append({
                "period": f"{year} calendar year; {label.replace('_', ' ')}",
                "denominator": {"value": 12, "unit": "monthly seasonally adjusted JOLTS rate observations for selected industry", "value_type": "time_series_mean"},
                "measures": {name: {"value": value, "unit": "percent annual arithmetic mean of monthly rate", "value_type": "estimated_rate"} for name, value in derived["annual_mean_of_monthly_rates_percent"][code][year].items()},
                "method": "Arithmetic mean of 12 BLS seasonally adjusted monthly rates; openings, hires, quits, layoffs/discharges, and total separations retain their BLS-specific denominators.",
                "uncertainty": "Establishment-survey estimates are subject to sampling error, revisions, seasonal-adjustment updates, and coverage limits; the annual mean does not represent unique workers.",
                "subgroup": f"National total-nonfarm JOLTS establishments in {label.replace('_', ' ')}; selected endpoint comparison against 2022.",
                "counterinterpretation": "Industry differences in openings or quits do not establish worker bargaining power, job quality, pay, schedule control, or the reason for a transition.",
                "source_url": "https://api.bls.gov/publicAPI/v2/timeseries/data/",
                "retrieval_hash": f"sha256:{derived['raw_response_sha256']}",
                "status": "compared",
            })
    record = {
        "format": "us-trend-observation-record-v1",
        "trend_id": "us-bls-jolts-selected-industry-mobility-2022-2025",
        "title": "Labor-market mobility cooled unevenly across selected US industries after 2022",
        "theme_ids": ["work", "voice", "cost"],
        "program_theme_ids": ["work_control_bargaining", "unequal_exposure_status", "firm_sector_market_power", "household_room_consumption"],
        "source_unit": "BLS Job Openings and Labor Turnover Survey national total-nonfarm establishment rates by selected industry",
        "geography": "United States, selected industries",
        "observations": observations,
        "related_sources": [{"source_url": "https://www.bls.gov/jlt/jltnaics.htm", "claim": "BLS publishes JOLTS industry estimates using the 2022 NAICS and makes seasonally adjusted data available for all listed series.", "status": "reported", "access_boundary": "Industry estimates remain establishment aggregates and do not identify worker-level outcomes."}],
        "boundary": "This record compares selected industry establishment-rate contexts at the 2022 peak and 2025 endpoint. It does not establish worker bargaining power, job quality, pay, schedule control, household security, or causation."
    }
    OUT.write_text(json.dumps(record, indent=2) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(observations)} observations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
