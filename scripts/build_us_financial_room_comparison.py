#!/usr/bin/env python3
"""Compare SHED wellbeing with USDA food-security outcomes without pooling."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "us-financial-room-independent-comparison.json"


def main() -> int:
    shed = json.loads((ROOT / "analysis" / "records" / "comparative-us-shed-financial-wellbeing-2013-2025.json").read_text())
    shed_emergency = json.loads((ANALYSIS / "shed-emergency-expense-2013-2025.json").read_text())
    usda = json.loads((ROOT / "analysis" / "records" / "comparative-usda-food-security-2022-2024.json").read_text())
    shed_values = {row["period"]: row["measures"]["doing_okay_or_living_comfortably"]["value"] for row in shed["observations"]}
    usda_values = {row["period"]: row["measures"]["food_insecure"]["value"] for row in usda["observations"]}
    emergency_values = {row["period"]: row["value"] for row in shed_emergency["observations"]}
    rows = [
        {"source": "Federal Reserve SHED", "measure": "doing_okay_or_living_comfortably", "from_period": "2022", "to_period": "2024", "from_value": shed_values["2022"], "to_value": shed_values["2024"], "change": shed_values["2024"] - shed_values["2022"], "unit": "percent of adults"},
        {"source": "Federal Reserve SHED", "measure": "would_cover_400_dollar_emergency", "from_period": "2022", "to_period": "2024", "from_value": emergency_values["2022"], "to_value": emergency_values["2024"], "change": emergency_values["2024"] - emergency_values["2022"], "unit": "percent of adults"},
        {"source": "USDA ERS CPS-FSS", "measure": "food_insecure", "from_period": "2022", "to_period": "2024", "from_value": usda_values["2022"], "to_value": usda_values["2024"], "change": usda_values["2024"] - usda_values["2022"], "unit": "percent of households"},
        {"source": "JPMorganChase Institute", "measure": "cash_savings_cover_400_shock", "from_period": "December 2023", "to_period": "December 2023", "from_value": 67, "to_value": 67, "change": 0, "unit": "percent of households"},
        {"source": "JPMorganChase Institute", "measure": "cash_disposable_income_or_short_term_credit_cover_400_shock", "from_period": "December 2023", "to_period": "December 2023", "from_value": 92, "to_value": 92, "change": 0, "unit": "percent of households"},
    ]
    payload = {
        "schema": "external-trend-intelligence.us-financial-room-independent-comparison.v1",
        "candidate_id": "candidate-time-financial-pressure-practical-room",
        "status": "mechanism_comparison_only",
        "source_families": [shed["source_unit"], usda["source_unit"], "JPMorganChase Institute household liquidity study"],
        "rows": rows,
        "directional_readout": "The independent U.S. series do not move identically: both SHED adult measures are flat from 2022 to 2024, USDA household food insecurity rises slightly, and JPMorganChase reports a higher household cash-liquidity endpoint when disposable income and short-term credit are included. Together they show construct-dependent, non-uniform resource pressure, not a common trend estimate.",
        "supports": ["independent publisher challenge", "same-geography directional comparison", "counter-signal review"],
        "does_not_support": ["pooled prevalence", "common-unit effect estimate", "causality", "qualified trend", "company exposure"],
        "blocking_items": ["SHED is adult-level while USDA and JPMorganChase are household-level", "different questionnaires, administrative methods, and sampling frames", "USDA 2024 change is not statistically significant versus 2023", "JPMorganChase combines cash, disposable income, and short-term credit in its broader endpoint", "no common outcome definition", "year-specific uncertainty intervals are not attached to the SHED chart series"],
        "uncertainty_audit": {
            "status": "intervals_not_comparable_in_current_artifacts",
            "shed": "The public chart artifact supplies point estimates only; the 2024 codebook identifies 12,295 respondents, but no interval was attached to either normalized SHED series.",
            "usda": "USDA publishes statistical-significance guidance and calculates standard errors with balanced repeated replication; the 2022-2024 national points are not statistically distinguishable on the published comparison.",
            "use": "Keep the comparison descriptive and unpooled until year-specific intervals or a reproducible variance extract is attached to both series."
        },
        "next_action": "Attach year-specific uncertainty intervals or a reproducible variance extract and preserve JPMorganChase licensing limits before any quantitative comparison; keep this lane as a mechanism challenge in the meantime.",
        "boundary": "Independent sources can converge directionally without measuring the same population outcome. No pooling or trend promotion is authorized."
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
