#!/usr/bin/env python3
"""Pin the Federal Reserve SHED $400 emergency-expense series."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "shed-emergency-expense-2013-2025.json"


def main() -> int:
    observations = [
        {"period": str(year), "value": value}
        for year, value in zip(range(2013, 2026), [50, 53, 54, 56, 59, 61, 63, 64, 68, 63, 63, 63, 63])
    ]
    payload = {
        "schema": "external-trend-intelligence.external-acquisition.v1",
        "acquisition_id": "federal-reserve-shed-emergency-expense-2013-2025",
        "source_family": "Federal Reserve Survey of Household Economics and Decisionmaking",
        "status": "acquired_normalized_pending_design_based_uncertainty",
        "publisher": "Board of Governors of the Federal Reserve System",
        "geography": "United States",
        "population": "U.S. adults age 18 and above",
        "measure": "percent of all adults who would cover a $400 emergency expense completely using cash or its equivalent",
        "unit": "percent of adults",
        "denominator": "all adult respondents in the SHED survey year",
        "method": "Annual SHED repeated cross-sectional survey; values are published chart-data percentages, not a longitudinal panel estimate.",
        "observations": observations,
        "source_urls": [
            "https://www.federalreserve.gov/consumerscommunities/sheddataviz/unexpectedexpenses.html",
            "https://www.federalreserve.gov/consumerscommunities/sheddataviz/SHED_visualizations_unexpected_expenses.zip",
            "https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-description.htm",
        ],
        "retrieval": {
            "retrieved_at": "2026-10-31",
            "artifact": "SHED_visualizations_unexpected_expenses.zip",
            "artifact_sha256": "sha256:c54990ece065ea8b116dcda4e45b553d9a88ff4b580cd9c87205084c0b92aa40",
            "source_csv": "unexpected_expenses.csv",
            "publisher_last_update": "2026-05-13",
        },
        "latest_official_report_context": {
            "report_period": "2025",
            "report_url": "https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-description.htm",
            "field_period": "October 17-28, 2025",
            "final_report_sample_count": 12934,
            "reported_overall_design_effect": 1.14,
            "scope_boundary": "The published design effect is an overall survey-precision context, not a measure-specific variance estimate for the $400 emergency-expense series.",
        },
        "comparability_review": {
            "candidate_use": "closer U.S. adult financial-capacity measure for the practical-room holdout",
            "improvement_over_existing_measure": "This measures emergency liquidity directly, rather than self-assessed financial comfort.",
            "remaining_mismatch": "It remains an adult-level U.S. survey measure and is not interchangeable with Australian household cash-flow or USDA household food-security measures.",
            "independence_status": "independent_publisher_candidate",
            "counter_signal": "The measure improved through 2021 and then held at 63 percent in 2022-2025; financial capacity need not move monotonically with pressure narratives.",
            "next_test": "Attach year-specific uncertainty intervals and pre-specify a same-population comparison before any quantitative cross-source claim.",
        },
        "rights_boundary": "The Federal Reserve publishes the data and documentation; retain the source URL, retrieval date, version hash, and chart-data attribution. This artifact does not determine redistribution or derived-chart rights beyond the publisher's terms.",
        "boundary": "This is a pinned acquisition candidate, not a qualified trend, causal estimate, or company finding. It must be uncertainty-reviewed before cross-source comparison.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(observations)} observations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
