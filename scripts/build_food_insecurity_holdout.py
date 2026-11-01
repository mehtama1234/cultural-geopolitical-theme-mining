#!/usr/bin/env python3
"""Build a bounded temporal holdout for the qualified food-insecurity pattern."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "food-insecurity-temporal-holdout.json"


def main() -> int:
    urban_release = json.loads((ANALYSIS / "urban-wbns-food-insecurity-2025.json").read_text())
    urban_working_age_2025 = next(
        row["food_insecurity_percent"]
        for row in urban_release["rows"]
        if row["category"] == "working_age_adults_18_64"
    )
    result = {
        "schema": "external-trend-intelligence.food-insecurity-temporal-holdout.v1",
        "candidate_id": "candidate-us-food-insecurity-persistence",
        "status": "descriptive_holdout_supported",
        "construction": {
            "source": "Urban Institute WBNS",
            "period": "December 2019 through December 2023",
            "values": [24.0, 20.4, 19.9, 24.7, 27.2],
            "mean_percent": 23.24,
        },
        "holdout": {
            "source": "Urban Institute WBNS",
            "period": "December 2024 through December 2025",
            "values": [27.0, urban_working_age_2025],
            "mean_percent": round((27.0 + urban_working_age_2025) / 2, 2),
        },
        "readout": {
            "change_percentage_points": 4.11,
            "direction": "increase",
            "interpretation": "The holdout remains above the 2019–2023 construction mean, supporting persistence of elevated food insecurity in the Urban working-age series.",
            "source_reported_significance": {
                "reference_estimate": "December 2025",
                "statistically_unchanged_from": [2023, 2024],
                "significantly_higher_than": [2019, 2020, 2021, 2022],
                "test_note": "Urban publication reports two-tailed significance annotations at the 0.10, 0.05, and 0.01 levels; machine-readable standard errors are not retained.",
            },
        },
        "independent_challenge": {
            "source": "USDA ERS CPS Food Security Supplement",
            "period": "2022 through 2024",
            "values": [12.8, 13.5, 13.7],
            "direction": "slight_increase",
            "boundary": "USDA household prevalence is not numerically pooled with the Urban adult-respondent series; USDA reports the 2024 change was not statistically significant versus 2023.",
        },
        "falsifier": "A later Urban release that falls below the 2019–2021 baseline without a documented questionnaire or frame change, or a later USDA release showing a sustained reversal, would weaken the persistence claim.",
        "does_not_support": ["causality", "policy effect", "pooled prevalence", "forecast validity", "company exposure"],
        "next_action": "Refresh both source families on their next releases, preserve questionnaire and denominator definitions, and review whether the 2025 Urban method change alters the holdout interpretation.",
        "source_records": [
            "us-urban-wbns-food-insecurity-persistence-2019-2025",
            "comparative-usda-food-security-2022-2024",
        ],
        "source_artifacts": ["urban-wbns-food-insecurity-2025.json", "usda-community-food-assistance-2024.json"],
        "boundary": "This is a descriptive temporal holdout with a non-pooled independent challenge. It qualifies external persistence for monitoring, not a causal or company result.",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
