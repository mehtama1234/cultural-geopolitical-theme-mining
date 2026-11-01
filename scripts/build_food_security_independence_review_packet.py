#!/usr/bin/env python3
"""Prepare a signable independence-review packet for the monitored food trend."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "food-security-independence-review-packet.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    urban = load("urban-wbns-food-insecurity-2025.json")
    comparison = load("food-insecurity-independent-comparison.json")
    usda = load("usda-temporal-holdout.json")
    rights = load("external-acquisition-rights-review.json")
    urban_rights = next(row for row in rights["rows"] if row["acquisition_id"] == "urban-wbns-food-insecurity-2025")
    packet = {
        "schema": "external-trend-intelligence.food-security-independence-review-packet.v1",
        "candidate_id": "candidate-us-food-insecurity-persistence",
        "status": "ready_for_human_independence_signoff",
        "machine_recommendation": "publisher_distinct_directional_challenge_noncomparable_hold",
        "evidence": {
            "urban": {
                "publisher": urban["publisher"],
                "artifact": "urban-wbns-food-insecurity-2025.json",
                "source_url": urban["source_url"],
                "checksum": urban["source_checksum"],
                "population_and_unit": urban["population_and_unit"],
                "geography_and_period": f"{urban['geography']}; {urban['observation_period']}",
                "instrument_and_method": urban["method"],
                "uncertainty_and_limits": urban["comparability_and_uncertainty"],
            },
            "usda": {
                "publisher": "USDA Economic Research Service",
                "artifact": "usda-temporal-holdout.json",
                "source_url": "https://www.ers.usda.gov/publications/113622",
                "record_id": usda["record_id"],
                "population_and_unit": usda["measure"],
                "geography_and_period": f"{usda['source_family']}; {usda['construction_period']} construction and {usda['holdout_period']} holdout",
                "instrument_and_method": "Annual CPS Food Security Supplement household survey",
                "uncertainty_and_limits": [usda["readout"], usda["boundary"]],
            },
            "comparison_artifact": "food-insecurity-independent-comparison.json",
            "comparison_rows": comparison["overlap_rows"],
            "pooling_decision": comparison["pooling_decision"],
        },
        "independence_assessment": {
            "publisher_families_distinct": True,
            "hosts_distinct": True,
            "shared_dependency_groups": [],
            "same_population_or_denominator": False,
            "same_instrument": False,
            "assessment": "Distinct publisher families provide a directional challenge, but different populations, denominators, uncertainty treatment, and method details prevent a common estimate or independent confirmation claim.",
        },
        "rights_assessment": {
            "urban_status": urban_rights["rights_evidence_status"],
            "urban_next_action": urban_rights["next_action"],
            "release_boundary": "Do not redistribute upstream tables, figures, or company-linked outputs until exact-artifact rights review is signed.",
        },
        "human_review": {
            "reviewer": None,
            "review_date": None,
            "final_disposition": None,
            "evidence_link_or_signoff": None,
        },
        "required_signoff_fields": [
            "canonical artifact identity confirmed for both publishers",
            "population, denominator, geography, period, unit, and outcome checked",
            "method and uncertainty differences acknowledged",
            "rights and downstream reuse boundary approved or held",
            "final disposition recorded as independent, dependent_restatement, same_artifact, or noncomparable_directional_challenge",
        ],
        "stop_rule": "Keep the candidate at monitored or held status and do not use it for a company bridge until a human reviewer signs the explicit disposition.",
        "boundary": "This packet makes the human review actionable; it is not a human adjudication, legal clearance, pooled estimate, causal result, or company authorization.",
        "next_action": "Assign a lineage reviewer, complete the five signoff fields, and write the final disposition back to candidate-independence-adjudication-queue.json.",
    }
    OUTPUT.write_text(json.dumps(packet, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({packet['status']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
