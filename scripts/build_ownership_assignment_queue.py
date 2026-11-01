#!/usr/bin/env python3
"""Build the named-ownership queue required before operational handoff."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "ownership-assignment-queue.json"

ROLE_HANDOFFS = {
    "source_steward": {"first_30_day_action": "Review the acquired-source register and close or escalate one rights/release question.", "required_evidence": ["acquired-source-register.json", "external-acquisition-rights-review.json", "release-watchlist.json"]},
    "evidence_analyst": {"first_30_day_action": "Reproduce one external source snapshot and reconcile its rows to the release manifest.", "required_evidence": ["release-manifest.json", "refresh-history.json", "EXTERNAL-DATA-SOURCES.md"]},
    "lineage_reviewer": {"first_30_day_action": "Adjudicate one publisher/upstream dependence question and record the unresolved boundary.", "required_evidence": ["rights-review-queue.json", "rights-evidence-register.json", "publisher-dependence-summary.json"]},
    "trend_challenger": {"first_30_day_action": "Challenge one held candidate using its counter-signal, falsifier, and next acquisition step.", "required_evidence": ["candidate-qualification-matrix.json", "falsification-review-queue.json", "candidate-lineage-dependency-review.json"]},
    "decision_translator": {"first_30_day_action": "Translate one monitored or qualified trend into a bounded decision question without requesting company data.", "required_evidence": ["PILOT-VALIDATION-PROTOCOL.md", "trend-qualification-matrix.json", "goal-completion-audit.json"]},
    "release_owner": {"first_30_day_action": "Run the release controls and preserve terminal evidence for a passing refresh and frontend smoke test.", "required_evidence": ["REFRESH-RUNBOOK.md", "refresh-history.json", "release-manifest.json", "operating-ownership-readiness.json"]},
}


def main() -> int:
    handoff = json.loads((ANALYSIS / "operating-handoff.json").read_text())
    roles = []
    for role in handoff["roles"]:
        roles.append(
            {
                "role": role["role"],
                "primary_owner": None if role["owner"] == "unassigned" else role["owner"],
                "backup_owner": None if role["backup"] == "unassigned" else role["backup"],
                "current_status": "unassigned" if role["owner"] == "unassigned" else "assigned",
                "evidence": role["evidence"],
                "acceptance_criteria": [
                    "named primary owner recorded",
                    "named backup owner recorded",
                    "scope and escalation boundary acknowledged",
                    "one independently reviewable run or decision note signed",
                ],
                "handoff_checkpoint": "month_21_successor_validation",
                "first_30_day_action": ROLE_HANDOFFS[role["role"]]["first_30_day_action"],
                "required_evidence": ROLE_HANDOFFS[role["role"]]["required_evidence"],
            }
        )
    assigned = sum(item["current_status"] == "assigned" for item in roles)
    payload = {
        "schema": "external-trend-intelligence.ownership-assignment-queue.v1",
        "role_count": len(roles),
        "assigned_role_count": assigned,
        "unassigned_role_count": len(roles) - assigned,
        "status": "assignment_required" if assigned < len(roles) else "assigned_pending_successor_signoff",
        "assignment_protocol": {
            "required_fields": ["person_or_team", "primary_acknowledgement", "backup_person_or_team", "scope_acknowledgement", "conflict_declaration", "effective_date"],
            "assignment_sla_business_days": 10,
            "backup_activation": "Activate the named backup after two missed review cycles, an unacknowledged release hold, or a primary conflict declaration.",
            "escalation_path": ["release_owner", "program_sponsor", "rights_and_privacy_owner"],
            "acceptance_evidence": ["signed role acknowledgement", "one independently reviewable run or decision note", "handoff update with open gates and next review date"],
        },
        "roles": roles,
        "next_action": "Use the assignment protocol to record named primary and backup owners for every role, then have a second analyst run the full refresh and sign the handoff independently.",
        "boundary": "This queue requests operational ownership; it does not infer identity, authorize internal data access, or prove that a successor run has occurred.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(roles)} roles; {assigned} assigned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
