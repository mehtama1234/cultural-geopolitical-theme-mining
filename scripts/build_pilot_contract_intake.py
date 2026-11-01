#!/usr/bin/env python3
"""Build a fillable, fail-closed intake contract for bounded company pilots."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "pilot-contract-intake.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    register = load("pilot-register.json")
    readiness = load("pilot-readiness.json")
    rows = []
    readiness_by_id = {row["pilot_id"]: row for row in readiness["pilots"]}
    for pilot in register["pilots"]:
        rows.append({
            "pilot_id": pilot["pilot_id"],
            "candidate_id": pilot["candidate_id"],
            "current_external_gate": pilot["external_gate"]["current_status"],
            "readiness_status": readiness_by_id[pilot["pilot_id"]]["readiness_status"],
            "decision_question": pilot["decision_question"],
            "required_registration": {
                "company_id": None,
                "company_name": None,
                "business_unit": None,
                "decision_owner": None,
                "decision_deadline": None,
                "internal_dataset": None,
                "snapshot_or_query": None,
                "entity_or_aggregate_basis": None,
                "geography": None,
                "period": None,
                "primary_outcome": None,
                "secondary_outcomes": [],
                "unit": None,
                "denominator": None,
                "comparison_group": None,
                "external_to_internal_crosswalk": None,
                "expected_unmatched_case_policy": "Report unmatched, suppressed, missing, and incompatible records separately; never drop them silently.",
                "privacy_class": None,
                "lawful_access_basis": None,
                "retention_limit": None,
                "redistribution_rule": None,
                "analysis_owner": None,
                "falsifier": pilot["falsifier"],
                "stop_rule": None,
            },
            "required_before_approved_test": [
                "external candidate is qualified or monitored under the matrix",
                "source-specific rights owner approves proposed reuse",
                "company decision owner and business unit are named",
                "internal data contract and crosswalk are complete",
                "privacy, lawful access, retention, and redistribution review pass",
                "analysis is preregistered with primary outcome, comparison, falsifier, and stop rule",
            ],
            "prohibited_transitions": [
                "Do not populate internal dataset fields from this template alone.",
                "Do not change readiness_status to approved_for_test without all required checks passing.",
                "Do not infer company exposure from the external candidate.",
            ],
        })
    payload = {
        "schema": "external-trend-intelligence.pilot-contract-intake.v1",
        "status": "template_only_no_company_data",
        "pilot_count": len(rows),
        "required_fields": ["company_id", "business_unit", "decision_owner", "internal_dataset", "period", "primary_outcome", "unit", "denominator", "privacy_class", "lawful_access_basis", "analysis_owner", "stop_rule"],
        "pilots": rows,
        "boundary": "This is a fillable pre-registration contract, not an approval. It intentionally contains no company identity, internal dataset, or personal data.",
        "next_action": "A named decision owner should complete one row only after the linked external candidate and rights gates pass.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} pilot contracts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
