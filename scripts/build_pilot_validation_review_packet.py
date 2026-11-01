#!/usr/bin/env python3
"""Build a signable, fail-closed validation packet for the design-only pilots."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "pilot-validation-review-packet.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    activation = load("pilot-activation-queue.json")
    intake = {row["pilot_id"]: row for row in load("pilot-contract-intake.json")["pilots"]}
    readiness = {row["pilot_id"]: row for row in load("pilot-readiness.json")["pilots"]}
    rows = []
    for item in activation["rows"]:
        contract = intake[item["pilot_id"]]
        ready = readiness[item["pilot_id"]]
        rows.append({
            "pilot_id": item["pilot_id"],
            "candidate_id": item["candidate_id"],
            "external_gate": item["external_gate"],
            "readiness_status": item["readiness_status"],
            "design_contract_complete": item["design_contract_complete"],
            "decision_question": contract["decision_question"],
            "falsifier": contract["required_registration"]["falsifier"],
            "required_before_approved_test": item["required_evidence_before_data_access"],
            "missing_approval_inputs": item["missing_approval_inputs"],
            "blocking_check_ids": item["blocking_check_ids"],
            "synthetic_bridge_status": "not_company_data; see pilot-bridge-simulation.json" if item["pilot_id"] == "pilot-food-security-service-room-001" else "not_run",
            "readiness_evidence": ready.get("evidence", []),
            "decision_options": ["hold_external_first", "approve_bounded_test", "reject_or_retire", "return_for_contract_revision"],
            "required_decision_fields": [
                "external qualification and rights status",
                "company, business unit, and decision owner",
                "internal dataset, period, unit, denominator, and crosswalk",
                "privacy, lawful access, retention, and redistribution decision",
                "preregistered primary outcome, comparison, falsifier, and stop rule",
                "unmatched, missing, suppressed, and incompatible case policy",
                "validation result, reviewer, and effective date",
            ],
            "signoff": {"decision_owner": None, "privacy_reviewer": None, "analysis_owner": None, "release_owner": None, "approved_on": None, "validation_result": None},
            "stop_rule": item["stop_rule"],
        })
    payload = {
        "schema": "external-trend-intelligence.pilot-validation-review-packet.v1",
        "status": "design_only_ready_for_human_activation_review",
        "pilot_count": len(rows),
        "approved_test_count": activation["approved_test_count"],
        "company_data_accessed": activation["company_data_accessed"],
        "rows": rows,
        "acceptance_criteria": [
            "Every pilot has an explicit external gate and rights decision before internal access.",
            "Every pilot has a named decision owner, privacy review, lawful-access basis, and preregistered analysis.",
            "Synthetic bridge evidence is kept separate from company results.",
            "No pilot is approved while any prerequisite, stop rule, or unmatched-case policy is incomplete.",
        ],
        "next_action": "Complete the external and rights gates first; then assign a decision owner and fill one pilot contract without providing internal data until every check passes.",
        "boundary": "This packet makes pilot activation review executable; it is not a company finding, approval, causal estimate, or authorization to access internal data.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} pilots; {activation['approved_test_count']} approved)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
