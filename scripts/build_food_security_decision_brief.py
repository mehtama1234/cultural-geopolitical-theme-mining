#!/usr/bin/env python3
"""Build a reader-ready brief for the one monitored external trend."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "food-security-decision-brief.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    holdout = load("food-insecurity-temporal-holdout.json")
    usda = load("usda-temporal-holdout.json")
    comparison = load("food-insecurity-independent-comparison.json")
    rights = load("food-insecurity-rights-review.json")
    matrix = load("candidate-qualification-matrix.json")
    candidate = next(row for row in matrix["rows"] if row["candidate_id"] == "candidate-us-food-insecurity-persistence")
    payload = {
        "schema": "external-trend-intelligence.food-security-decision-brief.v1",
        "candidate_id": candidate["candidate_id"],
        "qualification_state": candidate["gate_status"],
        "headline": "U.S. food insecurity remains elevated after pandemic support changes, with persistence visible in a later Urban holdout and a non-pooled USDA challenge.",
        "signal_summary": holdout["readout"]["interpretation"],
        "decision_use": "Use this as an external planning signal for service-capacity, affordability, and support-scenario review. Do not infer company exposure, causality, or a pooled adult-household prevalence estimate.",
        "evidence": {
            "primary_holdout": "food-insecurity-temporal-holdout.json",
            "independent_challenge": "usda-temporal-holdout.json",
            "qualification_matrix": "candidate-qualification-matrix.json",
            "rights_review": "food-insecurity-rights-review.json",
        },
        "chart_artifacts": ["food-insecurity-temporal-holdout.json", "usda-temporal-holdout.json"],
        "counter_signals": [
            holdout["independent_challenge"]["boundary"],
            "USDA reports that the 2024 prevalence was not statistically significantly different from 2023 or 2022.",
        ],
        "uncertainty": [
            "Urban and USDA use different populations, instruments, and denominators.",
            "The 2025 Urban methodology break must remain visible in future refreshes.",
            "The current result is descriptive persistence, not causal validation or a forecast.",
        ],
        "source_reported_significance": comparison["urban_methodology_review"]["source_reported_significance"],
        "falsifier": holdout["falsifier"],
        "next_action": holdout["next_action"],
        "rights_boundary": rights["release_decision"],
        "company_gate": "No company data connection or downstream redistribution is authorized until the rights owner approves reuse and a separate company decision contract, privacy review, and preregistered analysis pass.",
        "boundary": "This brief is a decision-ready external narrative for monitoring and scenario framing. It is not a company finding, causal claim, forecast, or legal clearance.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
