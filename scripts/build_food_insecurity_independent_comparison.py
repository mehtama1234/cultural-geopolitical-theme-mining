#!/usr/bin/env python3
"""Compare the Urban and USDA food-insecurity series without pooling unlike frames."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "food-insecurity-independent-comparison.json"


def main() -> int:
    urban = {2019: 24.0, 2020: 20.4, 2021: 19.9, 2022: 24.7, 2023: 27.2, 2024: 27.0, 2025: 27.7}
    usda = {2022: 12.8, 2023: 13.5, 2024: 13.7}
    overlap = sorted(set(urban) & set(usda))
    rows = []
    for year in overlap:
        rows.append({"period": year, "urban_working_age_percent": urban[year], "usda_household_percent": usda[year], "difference_percentage_points": round(urban[year] - usda[year], 1)})
    report = {
        "schema": "external-trend-intelligence.food-insecurity-independent-comparison.v1",
        "candidate_id": "candidate-us-food-insecurity-persistence",
        "status": "independent_directional_challenge_not_comparable",
        "source_families": [
            {"publisher": "Urban Institute", "host": "www.urban.org", "population": "U.S. working-age adults", "instrument": "Well-Being and Basic Needs Survey", "measure": "household food insecurity in the prior 12 months using the six-item USDA short form", "periods": "2019-2025", "rights_status": "permission_required_for_republication"},
            {"publisher": "USDA Economic Research Service", "host": "www.ers.usda.gov", "population": "U.S. households", "instrument": "Current Population Survey Food Security Supplement", "measure": "food insecure at some time during the year", "periods": "2022-2024", "rights_status": "conditional_attribution_use_documented"},
        ],
        "overlap_rows": rows,
        "directional_readout": {
            "urban_change_2022_to_2024_percentage_points": round(urban[2024] - urban[2022], 1),
            "usda_change_2022_to_2024_percentage_points": round(usda[2024] - usda[2022], 1),
            "direction": "both_series_increase",
            "uncertainty": "USDA reports the 2024 change was not statistically significant; comparable Urban uncertainty was not available in the retained artifact.",
            "urban_source_reported_significance": {
                "reference_estimate": "December 2025",
                "statistically_unchanged_from": [2023, 2024],
                "significantly_higher_than": [2019, 2020, 2021, 2022],
                "test_note": "Urban reports two-tailed significance annotations at the 0.10, 0.05, and 0.01 levels; the retained publication does not provide machine-readable standard errors or confidence intervals.",
            },
        },
        "independence_review": {
            "publisher_distinct": True,
            "host_distinct": True,
            "same_underlying_instrument": False,
            "status": "distinct_publishers_but_population_and_uncertainty_differ",
        },
        "pooling_decision": "do_not_pool",
        "urban_methodology_review": {
            "source_url": "https://www.urban.org/sites/default/files/2026-03/Food%20Insecurity%20Remained%20High%20in%202025%2C%20As%20Safety%20Net%20Cuts%20Loom%20.pdf",
            "reference_period_confirmed": "12 months",
            "instrument": "six-item short form of the USDA Household Food Security Survey Module",
            "sample_change": "More than 7,500 adults ages 18–64 in each 2017–2024 round; approximately 2,500 adults ages 65+ added in 2025.",
            "weighting": "KnowledgePanel probability-based sample with weights poststratified to CPS and ACS benchmarks.",
            "uncertainty_status": "Published significance annotations are captured below, but a full machine-readable standard-error table is not retained in this artifact.",
            "source_reported_significance": {
                "reference_estimate": "December 2025 working-age-adult estimate (27.7 percent)",
                "unchanged_comparisons": "December 2023 and December 2024",
                "higher_comparisons": "December 2022 and earlier years",
                "annotation_basis": "two-tailed tests with 0.10, 0.05, and 0.01 significance markers",
                "interpretation_boundary": "These are publisher-reported hypothesis-test annotations, not reconstructed intervals; they do not harmonize the Urban and USDA series.",
            },
            "reviewed_on": "2026-10-31"
        },
        "blocking_items": ["different population denominator", "instrument and threshold implementation differ despite shared six-item short-form lineage", "Urban uncertainty not retained", "Urban republication permission remains open"],
        "next_action": "Acquire comparable uncertainty and questionnaire documentation for the next Urban and USDA releases before revising the monitored trend or using it in a company decision contract.",
        "boundary": "This is a directional independent challenge. It supports monitoring, not a common prevalence estimate, causal effect, forecast, or company exposure.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} overlap rows; pooling={report['pooling_decision']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
