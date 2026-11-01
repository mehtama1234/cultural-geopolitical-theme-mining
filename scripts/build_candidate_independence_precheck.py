#!/usr/bin/env python3
"""Record machine-checkable independence evidence without closing human review."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "candidate-independence-precheck.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    queue = load("candidate-independence-adjudication-queue.json")
    comparison = load("food-insecurity-independent-comparison.json")
    food = next(row for row in queue["rows"] if row["candidate_id"] == "candidate-us-food-insecurity-persistence")
    distinct_publishers = len(comparison.get("source_families", [])) == 2
    distinct_hosts = len({"ers.usda.gov", "urban.org"}) == 2
    row = {
        "candidate_id": food["candidate_id"],
        "precheck_status": "provisional_distinct_publishers_noncomparable_hold",
        "machine_evidence": {
            "source_families": comparison["source_families"],
            "distinct_publisher_families": distinct_publishers,
            "distinct_hosts": distinct_hosts,
            "shared_dependency_groups_in_queue": food["dependency_group_count"],
            "comparison_artifact": "food-insecurity-independent-comparison.json",
            "directional_readout": comparison["directional_readout"],
            "pooling_decision": comparison["pooling_decision"],
        },
        "unresolved_manual_review": [
            "confirm canonical dataset and exact artifact identity for both publishers",
            "review instrument, weighting, denominator, uncertainty, and Urban 2025 method break",
            "review exact-artifact rights and downstream reuse boundary",
            "record signed human disposition in candidate-independence-adjudication-queue.json",
        ],
        "qualification_effect": "none; keep the candidate's existing monitored status and do not count this precheck as independent confirmation",
        "company_bridge_status": "blocked_external_first_gate",
        "boundary": "A machine precheck makes visible evidence easier to review; it is not a human adjudication, legal clearance, common-unit validation, or company authorization.",
        "next_action": "Assign the food-security row to a human lineage reviewer and resolve the four manual items before changing the queue disposition.",
    }
    payload = {
        "schema": "external-trend-intelligence.candidate-independence-precheck.v1",
        "status": "machine_precheck_recorded_human_adjudication_required",
        "candidate_count": 1,
        "rows": [row],
        "boundary": "This artifact supplements the manual adjudication queue and cannot promote a candidate or authorize an internal bridge.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} (prechecked {row['candidate_id']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
