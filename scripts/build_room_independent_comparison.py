#!/usr/bin/env python3
"""Compare independent household-room signals without pooling unlike measures."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "room-independent-comparison.json"


def main() -> int:
    records = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())["records"]
    abs_record = records["comparative-abs-general-social-survey-2025-cultural-participation-financial-stress-connection"]["record"]
    anz_record = records["comparative-anz-roy-morgan-australian-consumer-confidence-september-29-2026-financial-outlook"]["record"]
    abs_obs = abs_record["observations"][1]["measures"]
    anz_headline = anz_record["observations"][0]["measures"]
    anz_obs = anz_record["observations"][1]["measures"]
    report = {
        "schema": "external-trend-intelligence.room-independent-comparison.v1",
        "candidate_id": "candidate-time-financial-pressure-practical-room",
        "status": "mechanism_comparison_only",
        "source_families": ["Australian Bureau of Statistics General Social Survey", "HILDA via Australian Institute of Health and Welfare", "ANZ / Roy Morgan"],
        "records": [
            {
                "publisher": "Australian Bureau of Statistics",
                "record_id": abs_record["trend_id"],
                "geography": abs_record["geography"],
                "measures": {
                    "cash_flow_problem_2020": abs_obs["cash_flow_problem_2020"],
                    "cash_flow_problem_2025": abs_obs["cash_flow_problem_2025"],
                    "dissaving_2020": abs_obs["dissaving_2020"],
                    "dissaving_2025": abs_obs["dissaving_2025"],
                    "outside_household_weekly_contact_2020": abs_obs["outside_household_weekly_contact_2020"],
                    "outside_household_weekly_contact_2025": abs_obs["outside_household_weekly_contact_2025"],
                },
            },
            {
                "publisher": "Australian Institute of Health and Welfare / HILDA",
                "record_id": "aihw-hilda-financial-stress-2001-2023",
                "geography": "Australia; HILDA household-level custom analysis",
                "measures": {
                    "cash_flow_problem_2020": {"value": 26.9, "unit": "percent of households with at least one person reporting a cash-flow problem", "period": "2020"},
                    "cash_flow_problem_2023": {"value": 28.1, "unit": "percent of households with at least one person reporting a cash-flow problem", "period": "2023"},
                    "unable_to_raise_2000_2020": {"value": 26.6, "unit": "percent of households with at least one person unable to raise $2,000", "period": "2020"},
                    "unable_to_raise_2000_2023": {"value": 27.1, "unit": "percent of households with at least one person unable to raise $2,000", "period": "2023"}
                },
                "source_url": "https://www.abs.gov.au/statistics/measuring-what-matters/measuring-what-matters-themes-and-indicators/secure/making-ends-meet",
                "retrieval_hash": "sha256:ad78b94069aa43911be3a9a8de2f9ddb645785a545f4076971c7e8b5c5c60620",
                "checked": "2026-10-31",
                "lineage_note": "AIHW presents custom HILDA analysis; HILDA is a separate longitudinal source from the ABS General Social Survey."
            },
            {
                "publisher": "ANZ / Roy Morgan",
                "record_id": anz_record["trend_id"],
                "geography": anz_record["geography"],
                "measures": {
                    "confidence_index": anz_headline["confidence_index"],
                    "better_off_now": anz_obs["better_off_now"],
                    "worse_off_now": anz_obs["worse_off_now"],
                    "buying_intention": anz_obs["buying_intention"],
                },
            },
        ],
        "supports": ["independent mechanism challenge", "counter-signal design", "future compatible-source selection"],
        "does_not_support": ["pooled prevalence", "common-unit effect estimate", "temporal backtest across publishers", "causal effect", "company exposure"],
        "blocking_items": [
            "ABS measures are 2020-to-2025 repeated cross-sections while ANZ/Roy Morgan is a weekly 2026 release",
            "HILDA is 2020-to-2023 and does not extend to the ABS 2025 holdout",
            "household financial-stress, adult social-contact, and confidence-index denominators differ",
            "no common holdout period or outcome definition",
            "publisher methods and sampling frames differ",
        ],
        "next_action": "Acquire an independent repeated household-finance or purchase-behavior series with a compatible population and period before promoting the candidate.",
        "boundary": "Independent publishers can challenge the household-room mechanism without making unlike measures numerically comparable.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
