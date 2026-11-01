#!/usr/bin/env python3
"""Build a signable operating-ownership handoff packet for all observatory roles."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "operating-ownership-review-packet.json"


def main() -> int:
    queue = json.loads((ANALYSIS / "ownership-assignment-queue.json").read_text())
    roles = []
    for item in queue["roles"]:
        roles.append({
            "role": item["role"],
            "current_status": item["current_status"],
            "primary_owner": item["primary_owner"],
            "backup_owner": item["backup_owner"],
            "scope_evidence": item["evidence"],
            "first_30_day_action": item["first_30_day_action"],
            "required_evidence": item["required_evidence"],
            "handoff_checkpoint": item["handoff_checkpoint"],
            "acceptance_criteria": item["acceptance_criteria"],
            "required_decision_fields": [
                "named primary person or team",
                "named backup person or team",
                "primary and backup acknowledgement",
                "scope and escalation boundary acknowledgement",
                "conflict declaration",
                "effective date and next review date",
                "independently reviewable run or decision note",
            ],
            "decision_options": ["accept_assignment", "accept_with_scope", "decline_and_reassign", "hold_pending_sponsor_decision"],
            "signoff": {"primary_acknowledgement": None, "backup_acknowledgement": None, "conflict_declaration": None, "sponsor_signoff": None, "effective_date": None},
        })
    payload = {
        "schema": "external-trend-intelligence.operating-ownership-review-packet.v1",
        "status": "ready_for_named_human_assignment",
        "role_count": len(roles),
        "assigned_role_count": queue["assigned_role_count"],
        "unassigned_role_count": queue["unassigned_role_count"],
        "roles": roles,
        "acceptance_criteria": [
            "Every role has a named primary and backup owner.",
            "Each owner acknowledges scope, escalation, conflicts, and effective date.",
            "A second analyst independently signs one reviewable run or decision note.",
            "Open gates and the next review date are carried into the handoff record.",
        ],
        "next_action": "Assign primary and backup owners, collect acknowledgements, and attach one independently reviewable run or decision note per role.",
        "boundary": "This packet makes ownership handoff executable; it does not infer identity, authorize internal data access, or prove a successor run.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(roles)} roles; {queue['assigned_role_count']} assigned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
