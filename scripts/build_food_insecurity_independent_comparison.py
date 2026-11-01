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
            {"publisher": "Urban Institute", "host": "www.urban.org", "population": "U.S. working-age adults", "instrument": "Well-Being and Basic Needs Survey", "measure": "food insecurity in the prior 30 days", "periods": "2019-2025", "rights_status": "permission_required_for_republication"},
            {"publisher": "USDA Economic Research Service", "host": "www.ers.usda.gov", "population": "U.S. households", "instrument": "Current Population Survey Food Security Supplement", "measure": "food insecure at some time during the year", "periods": "2022-2024", "rights_status": "conditional_attribution_use_documented"},
        ],
        "overlap_rows": rows,
        "directional_readout": {
            "urban_change_2022_to_2024_percentage_points": round(urban[2024] - urban[2022], 1),
            "usda_change_2022_to_2024_percentage_points": round(usda[2024] - usda[2022], 1),
            "direction": "both_series_increase",
            "uncertainty": "USDA reports the 2024 change was not statistically significant; comparable Urban uncertainty was not available in the retained artifact.",
        },
        "independence_review": {
            "publisher_distinct": True,
            "host_distinct": True,
            "same_underlying_instrument": False,
            "status": "distinct_publishers_but_population_measure_and_uncertainty_differ",
        },
        "pooling_decision": "do_not_pool",
        "blocking_items": ["different population denominator", "30-day versus annual reference period", "instrument and threshold differ", "Urban uncertainty not retained", "Urban republication permission remains open"],
        "next_action": "Acquire comparable uncertainty and questionnaire documentation for the next Urban and USDA releases before revising the monitored trend or using it in a company decision contract.",
        "boundary": "This is a directional independent challenge. It supports monitoring, not a common prevalence estimate, causal effect, forecast, or company exposure.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} overlap rows; pooling={report['pooling_decision']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
