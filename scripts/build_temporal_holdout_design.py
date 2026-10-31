#!/usr/bin/env python3
"""Register a same-instrument temporal holdout without overstating comparability."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "temporal-holdout-design.json"


def main() -> int:
    record_id = "comparative-abs-general-social-survey-2025-cultural-participation-financial-stress-connection"
    record = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())["records"][record_id]["record"]
    observation = record["observations"][1]
    measures = observation["measures"]
    rows = []
    for name in ("cash_flow_problem", "dissaving", "outside_household_weekly_contact"):
        rows.append({
            "measure": name,
            "construction_period": "2020",
            "holdout_period": "2025",
            "construction_value": measures[f"{name}_2020"]["value"],
            "holdout_value": measures[f"{name}_2025"]["value"],
            "unit": measures[f"{name}_2025"]["unit"],
            "change": measures.get(f"{name}_change", {}).get("value"),
            "status": "same_instrument_repeated_cross_section",
        })
    report = {
        "schema": "external-trend-intelligence.temporal-holdout-design.v1",
        "candidate_id": "candidate-time-financial-pressure-practical-room",
        "record_id": record_id,
        "status": "design_ready_single_family_holdout",
        "construction_period": "2020",
        "holdout_period": "2025",
        "geography": "Australia",
        "source_family": "Australian Bureau of Statistics General Social Survey",
        "measures": rows,
        "supports": ["pre-specified temporal holdout", "same-instrument direction check", "counter-signal separation between financial stress and social contact"],
        "does_not_support": ["independent-source confirmation", "individual longitudinal change", "causal effect", "company exposure", "pooled denominator across measures"],
        "method_cautions": [
            "2020 and 2025 are repeated cross-sections, not a panel",
            "financial-stress measures use households while social-contact measures use adults",
            "ABS warns that questionnaire wording and methodology changes require care in cycle comparisons",
            "the holdout is one source family and cannot satisfy the independence gate",
        ],
        "next_action": "Compare the 2020-to-2025 direction against an independent source with a compatible population and period; retain the ABS result as a temporal check, not a qualified trend.",
        "boundary": "This artifact registers a reproducible holdout design. It is not a statistical backtest result or evidence that financial pressure caused participation change.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} measures)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
