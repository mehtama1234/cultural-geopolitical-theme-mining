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
    usda = json.loads((ROOT / "analysis" / "records" / "comparative-usda-food-security-2022-2024.json").read_text())
    shed_values = {row["period"]: row["measures"]["doing_okay_or_living_comfortably"]["value"] for row in shed["observations"]}
    usda_values = {row["period"]: row["measures"]["food_insecure"]["value"] for row in usda["observations"]}
    rows = [
        {"source": "Federal Reserve SHED", "measure": "doing_okay_or_living_comfortably", "from_period": "2022", "to_period": "2024", "from_value": shed_values["2022"], "to_value": shed_values["2024"], "change": shed_values["2024"] - shed_values["2022"], "unit": "percent of adults"},
        {"source": "USDA ERS CPS-FSS", "measure": "food_insecure", "from_period": "2022", "to_period": "2024", "from_value": usda_values["2022"], "to_value": usda_values["2024"], "change": usda_values["2024"] - usda_values["2022"], "unit": "percent of households"}
    ]
    payload = {
        "schema": "external-trend-intelligence.us-financial-room-independent-comparison.v1",
        "candidate_id": "candidate-time-financial-pressure-practical-room",
        "status": "mechanism_comparison_only",
        "source_families": [shed["source_unit"], usda["source_unit"]],
        "rows": rows,
        "directional_readout": "Both independent U.S. series indicate continued resource pressure between 2022 and 2024, but they measure different constructs and use adult versus household denominators.",
        "supports": ["independent publisher challenge", "same-geography directional comparison", "counter-signal review"],
        "does_not_support": ["pooled prevalence", "common-unit effect estimate", "causality", "qualified trend", "company exposure"],
        "blocking_items": ["SHED is adult self-assessed financial wellbeing while USDA is household food insecurity", "different questionnaires and sampling frames", "USDA 2024 change is not statistically significant versus 2023", "no common outcome definition"],
        "next_action": "Retrieve full codebooks and uncertainty intervals, then pre-specify whether the comparison is a mechanism challenge or a separate U.S. trend lane.",
        "boundary": "Independent sources can converge directionally without measuring the same population outcome. No pooling or trend promotion is authorized."
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
