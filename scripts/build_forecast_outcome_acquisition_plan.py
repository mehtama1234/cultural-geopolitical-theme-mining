#!/usr/bin/env python3
"""Define the official-release protocol for forecast outcome backtests."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "forecast-outcome-acquisition-plan.json"


def main() -> int:
    plan = {
        "schema": "external-trend-intelligence.forecast-outcome-acquisition-plan.v1",
        "comparison_artifact": "global-growth-forecast-comparison.json",
        "backtest_register": "forecast-backtest-register.json",
        "status": "protocol_ready_outcomes_pending",
        "outcome_definition": "First comparable full-year realized global-growth or global-inflation estimate published after the forecast period, with the release vintage retained. A later revision is a separate outcome vintage, not a replacement.",
        "tracks": [
            {
                "measure": "global_growth_2026",
                "target_period": 2026,
                "primary_release_family": "World Bank Global Economic Prospects",
                "official_source_url": "https://www.worldbank.org/en/publication/global-economic-prospects",
                "secondary_challenge_family": "IMF World Economic Outlook",
                "secondary_source_url": "https://www.imf.org/en/Publications/WEO",
                "earliest_acceptable_release": "first official 2026 full-year estimate after year end",
            },
            {
                "measure": "global_growth_2027",
                "target_period": 2027,
                "primary_release_family": "World Bank Global Economic Prospects",
                "official_source_url": "https://www.worldbank.org/en/publication/global-economic-prospects",
                "secondary_challenge_family": "IMF World Economic Outlook",
                "secondary_source_url": "https://www.imf.org/en/Publications/WEO",
                "earliest_acceptable_release": "first official 2027 full-year estimate after year end",
            },
            {
                "measure": "global_inflation_2026",
                "target_period": 2026,
                "primary_release_family": "IMF World Economic Outlook",
                "official_source_url": "https://www.imf.org/en/Publications/WEO",
                "secondary_challenge_family": "World Bank Global Economic Prospects",
                "secondary_source_url": "https://www.worldbank.org/en/publication/global-economic-prospects",
                "earliest_acceptable_release": "first official 2026 full-year inflation estimate after year end",
            },
        ],
        "required_fields": ["publisher", "release_date", "vintage_or_revision", "measure_definition", "geography", "period", "value", "unit", "uncertainty_or_interval", "source_url", "rights_basis"],
        "acceptance_criteria": ["original forecast remains unchanged", "outcome is full-year and definition-compatible", "forecast and outcome vintages are explicit", "uncertainty is retained or marked unavailable", "absolute and signed forecast errors are calculated only after acceptance", "independent challenge remains separate from the primary outcome"],
        "stop_rules": ["Do not backfill a partial-year release as a realized annual outcome.", "Do not use a later forecast as the realized outcome.", "Do not pool publisher estimates when model lineage or definitions differ.", "Do not publish a forecast score without recording revision and uncertainty status."],
        "owner": "external evidence review queue",
        "next_action": "At the first eligible official release after each target period, append a vintage-preserving outcome row and run the forecast error review.",
        "boundary": "This is an acquisition protocol, not evidence that any forecast is accurate or a company-relevant signal.",
    }
    OUTPUT.write_text(json.dumps(plan, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(plan['tracks'])} forecast tracks; outcomes pending)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
