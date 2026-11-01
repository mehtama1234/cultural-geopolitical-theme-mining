#!/usr/bin/env python3
"""Build an ordered, fail-closed queue for activating company decision pilots."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "pilot-activation-queue.json"


def main() -> int:
    intake = json.loads((ANALYSIS / "pilot-contract-intake.json").read_text())
    readiness = json.loads((ANALYSIS / "pilot-readiness.json").read_text())
    simulation = json.loads((ANALYSIS / "pilot-bridge-simulation.json").read_text())
    readiness_by_id = {row["pilot_id"]: row for row in readiness["pilots"]}
    rows = []
    for pilot in intake["pilots"]:
        pilot_id = pilot["pilot_id"]
        registration = pilot["required_registration"]
        readiness_row = readiness_by_id[pilot_id]
        missing = [field for field in intake["required_fields"] if registration.get(field) in (None, "")]
        design_fields = {
            "decision_question": bool(pilot.get("decision_question")),
            "falsifier": bool(registration.get("falsifier")),
            "unmatched_case_policy": bool(registration.get("expected_unmatched_case_policy")),
            "required_before_approved_test": bool(pilot.get("required_before_approved_test")),
        }
        rows.append({
            "pilot_id": pilot_id,
            "candidate_id": pilot["candidate_id"],
            "external_gate": pilot["current_external_gate"],
            "readiness_status": pilot["readiness_status"],
            "design_contract_complete": all(design_fields.values()),
            "design_fields": design_fields,
            "missing_approval_inputs": missing,
            "blocking_check_ids": readiness_row["blocking_check_ids"],
            "ordered_prerequisites": [
                "external candidate is qualified or monitored",
                "source-specific rights reuse is approved",
                "company decision owner and business unit are named",
                "internal dataset, denominator, period, and crosswalk are registered",
                "privacy, lawful access, retention, and redistribution review pass",
                "analysis is preregistered with falsifier and stop rule",
            ],
            "company_data_accessed": bool(simulation.get("company_data_accessed")) if pilot_id == simulation.get("pilot_id") else False,
            "next_action": "Complete the next unmet prerequisite in order; do not connect internal data while any earlier gate is blocked.",
        })
    payload = {
        "schema": "external-trend-intelligence.pilot-activation-queue.v1",
        "status": "design_contracts_ready_activation_blocked",
        "pilot_count": len(rows),
        "design_complete_count": sum(row["design_contract_complete"] for row in rows),
        "approved_test_count": 0,
        "company_data_accessed": False,
        "rows": rows,
        "boundary": "This queue sequences approvals; it does not name a company, authorize access, create a join, or turn synthetic bridge cells into a pilot result.",
        "next_action": "A named decision owner must complete one pilot's registration fields only after its external and rights gates pass.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} pilots; {payload['design_complete_count']} design contracts complete)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
