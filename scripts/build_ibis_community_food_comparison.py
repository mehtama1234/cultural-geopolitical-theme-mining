#!/usr/bin/env python3
"""Compare USDA and Feeding America community-food context without pooling."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
LINKAGE = ANALYSIS / "ibis-community-food-outcome-linkage-review.json"
OUTPUT = ANALYSIS / "ibis-community-food-comparison.json"


def main() -> int:
    linkage = json.loads(LINKAGE.read_text())
    usda = linkage["outcome_artifact"]
    feeding = linkage["independent_publisher_challenge"]
    food_insecure = next(row for row in usda["observations"] if row["category"] == "food_insecure_households")
    payload = {
        "schema": "external-trend-intelligence.ibis-community-food-comparison.v1",
        "status": "non_pooled_directional_context_only",
        "claim_id": linkage["claim_id"],
        "comparison_period": "2024",
        "rows": [
            {
                "publisher": "USDA Economic Research Service",
                "measure": "receipt of free groceries among food-insecure households",
                "value": food_insecure["free_groceries_percent"],
                "unit": "percent of food-insecure households",
                "population": "CPS-FSS U.S. households",
                "source_artifact": "usda-community-food-assistance-2024.json",
            },
            {
                "publisher": "Feeding America",
                "measure": "overall food insecurity rate",
                "value": feeding["observations"]["food_insecurity_rate"] * 100,
                "unit": "percent of individuals living in food-insecure households",
                "population": "modeled U.S. overall population",
                "source_artifact": "feeding-america-map-meal-gap-2026-national.json",
            },
        ],
        "interpretation": "The two values describe different constructs and denominators: household-reported free-grocery receipt among food-insecure households versus a modeled individual food-insecurity rate. The numerical difference is not a gap estimate and must not be read as a change in demand or provider performance.",
        "lineage_and_dependence": {
            "publisher_diversity": "distinct_publishers",
            "shared_input_risk": "Feeding America models local estimates using CPS-FSS and other public inputs; shared survey lineage means distinct publishers do not automatically establish independent models.",
            "rights_status": "USDA normalized context retained under conditional attribution; Feeding America underlying data are request-gated.",
        },
        "decision": "hold",
        "next_action": "Acquire the request-gated Feeding America data or technical appendix, reconcile household versus individual denominators, and obtain a provider-side utilization or capacity measure before qualifying the IBIS claim.",
        "boundary": "This is a source-comparison control. It is not a pooled estimate, causal analysis, market-size estimate, or company decision result.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({payload['status']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
