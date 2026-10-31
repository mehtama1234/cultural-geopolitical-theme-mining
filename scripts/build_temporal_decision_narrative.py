#!/usr/bin/env python3
"""Publish a bounded, decision-ready narrative from the temporal holdout."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "temporal-decision-narrative.json"


def main() -> int:
    result = json.loads((ANALYSIS / "temporal-holdout-result.json").read_text())
    report = {
        "schema": "external-trend-intelligence.temporal-decision-narrative.v1",
        "candidate_id": result["candidate_id"],
        "status": "bounded_external_narrative",
        "headline": "Financial pressure increased while social reconnection also increased in Australia between 2020 and 2025.",
        "what_the_evidence_shows": [
            "ABS reported higher household cash-flow problems in 2025 than 2020.",
            "ABS reported higher household dissaving in 2025 than 2020.",
            "ABS also reported higher weekly face-to-face contact outside the household in 2025 than 2020.",
        ],
        "decision_use": "Treat material pressure and social reconnection as separate planning signals: a rising participation or connection headline should not be read as proof that household financial room has improved.",
        "counter_signal": "Social contact increased alongside the financial-pressure measures; the evidence does not support a simple collapse-of-participation story.",
        "uncertainty": [
            "The comparison uses repeated cross-sections, not the same people over time.",
            "Financial stress is measured at household level and social contact at adult level.",
            "ABS flags questionnaire and methodology changes across cycles.",
            "This is one source family and is not independent confirmation.",
        ],
        "recommended_next_action": "Use the narrative to frame questions and monitor the next ABS cycle; do not initiate an internal company exposure test until an independent compatible source clears the qualification gates.",
        "boundary": "This is a bounded external narrative, not a causal explanation, forecast, market-size estimate, or company finding.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
