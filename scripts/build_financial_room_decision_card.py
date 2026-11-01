#!/usr/bin/env python3
"""Assemble the financial-room evidence into one bounded reader card."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "financial-room-decision-card.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    comparison = load("us-financial-room-independent-comparison.json")
    directional = load("room-independent-result.json")
    chart = load("jpmorgan-household-liquidity-chart.json")
    rights = load("financial-room-rights-review.json")
    narrative = load("temporal-decision-narrative.json")
    payload = {
        "schema": "external-trend-intelligence.financial-room-decision-card.v1",
        "status": "bounded_external_mechanism_context",
        "title": "Financial pressure is construct-dependent and should be treated as separate planning signals",
        "candidate_id": comparison["candidate_id"],
        "headline": narrative["headline"],
        "evidence": {
            "australia_directional_panel": directional["rows"],
            "us_cross_source_comparison": comparison["rows"],
            "jpmorgan_chart_endpoints": chart["chart_asset"]["visible_endpoint_labels"],
        },
        "interpretation": comparison["directional_readout"],
        "counter_signal": narrative["counter_signal"],
        "uncertainty": comparison["uncertainty_audit"],
        "rights": {
            "release_decision": rights["release_decision"],
            "open_source_reviews": sum(row["rights_status"].endswith("open") or "required" in row["rights_status"] for row in rights["rows"]),
            "source_count": rights["source_count"],
        },
        "decision_use": "Use this card to frame scenario questions about household and consumer pressure. Do not pool unlike denominators, infer causality, or label a company population from the external series.",
        "company_gate": "No internal bridge until a compatible independent outcome, source-specific rights approval, a named decision contract, and privacy/access review pass.",
        "next_action": "Attach year-specific uncertainty or a reproducible variance extract, complete artifact-level rights review, and keep the lane as mechanism context until the qualification gates pass.",
        "boundary": "This is a reader-facing external evidence card, not a qualified trend, causal result, forecast, market estimate, legal clearance, or company finding.",
        "source_artifacts": [
            "us-financial-room-independent-comparison.json",
            "room-independent-result.json",
            "jpmorgan-household-liquidity-chart.json",
            "financial-room-rights-review.json",
            "temporal-decision-narrative.json",
        ],
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({rights['source_count']} rights-reviewed sources)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
