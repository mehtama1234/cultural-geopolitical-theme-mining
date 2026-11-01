#!/usr/bin/env python3
"""Exercise the bounded bridge logic on synthetic aggregate cells only."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "pilot-bridge-simulation.json"


def main() -> int:
    external = [
        {"geography": "synthetic-west", "period": "2026-Q1", "external_context_rate": 0.18},
        {"geography": "synthetic-east", "period": "2026-Q1", "external_context_rate": 0.11},
        {"geography": "synthetic-unmatched", "period": "2026-Q1", "external_context_rate": 0.15},
        {"geography": "synthetic-missing-outcome", "period": "2026-Q1", "external_context_rate": 0.14},
    ]
    internal = [
        {"geography": "synthetic-west", "period": "2026-Q1", "workflow_completion_rate": 0.74, "denominator": 100},
        {"geography": "synthetic-east", "period": "2026-Q1", "workflow_completion_rate": 0.81, "denominator": 120},
        {"geography": "synthetic-missing-outcome", "period": "2026-Q1", "workflow_completion_rate": None, "denominator": 90},
    ]
    internal_by_key = {(row["geography"], row["period"]): row for row in internal}
    matched, unmatched_external, missing_outcome = [], [], []
    for row in external:
        key = (row["geography"], row["period"])
        target = internal_by_key.get(key)
        if target is None:
            unmatched_external.append(row)
        elif target["workflow_completion_rate"] is None:
            missing_outcome.append({"external": row, "internal": target})
        else:
            matched.append({"key": {"geography": row["geography"], "period": row["period"]}, "external_context_rate": row["external_context_rate"], "workflow_completion_rate": target["workflow_completion_rate"], "denominator": target["denominator"]})
    payload = {
        "schema": "external-trend-intelligence.pilot-bridge-simulation.v1",
        "status": "synthetic_contract_exercised_fail_closed",
        "pilot_id": "pilot-food-security-service-room-001",
        "candidate_id": "candidate-us-food-insecurity-persistence",
        "join_basis": "aggregate_comparison",
        "synthetic_only": True,
        "company_data_accessed": False,
        "matched_cells": matched,
        "unmatched_external_cells": unmatched_external,
        "missing_outcome_cells": missing_outcome,
        "required_visibility_checks": {
            "unmatched_remain_visible": bool(unmatched_external),
            "missing_outcomes_remain_visible": bool(missing_outcome),
            "denominators_present_for_matched": all(row["denominator"] > 0 for row in matched),
            "no_individual_identity": True,
        },
        "falsifier": "A later compatible comparison with no stable difference, reversed direction, or stronger operational explanation stops the pilot claim.",
        "stop_rule": "Stop before real internal access if rights, privacy, denominator, external monitoring, or preregistration gates fail.",
        "approved_test_count": 0,
        "boundary": "Synthetic aggregate cells exercise schema and visibility behavior only. They are not company data, a pilot result, causal evidence, or authorization to connect an internal system.",
        "next_action": "Have a named decision owner complete the real contract only after external qualification, rights, privacy, and access gates pass.",
    }
    assert matched and unmatched_external and missing_outcome
    assert all(payload["required_visibility_checks"].values())
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(matched)} matched; fail-closed visibility exercised)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
