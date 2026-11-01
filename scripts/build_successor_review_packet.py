#!/usr/bin/env python3
"""Create a concrete, signable handoff packet for the next human analyst."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "successor-review-packet.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    manifest = load("release-manifest.json")
    matrix = load("candidate-qualification-matrix.json")
    queue = load("ownership-assignment-queue.json")
    held = [row for row in matrix["rows"] if row["gate_status"] == "held"]
    packet = {
        "schema": "external-trend-intelligence.successor-review-packet.v1",
        "packet_id": "successor-review-packet-current",
        "status": "ready_for_named_human_successor",
        "release": {
            "artifact_count": manifest["artifact_count"],
            "source_tree_commit": manifest["source_tree_commit"],
            "qualification_summary": {
                "candidate_count": matrix["candidate_count"],
                "monitored_external_trend_count": matrix["monitored_external_trend_count"],
                "held_count": matrix["held_count"],
            },
        },
        "required_assignee_fields": queue["assignment_protocol"]["required_fields"],
        "review_tasks": [
            {
                "task_id": "full_refresh_reproduction",
                "owner_role": "release_owner",
                "instruction": "Run scripts/refresh_external_observatory.py from a clean checkout and preserve the terminal 100-step output.",
                "evidence_required": ["refresh-history.json", "release-manifest.json", "validate_external_trend_intelligence.py", "smoke_test_external_board.py"],
                "stop_rule": "Stop and retain the prior release if any step fails, a rights gate changes unexpectedly, or the frontend smoke test is not HTTP 200.",
                "assignee": None,
                "completed_on": None,
                "signoff": None,
            },
            {
                "task_id": "held_candidate_challenge",
                "owner_role": "trend_challenger",
                "instruction": "Review one held candidate end-to-end, verify source identity, periods, units, counter-signal, falsifier, and next acquisition step; do not promote it.",
                "candidate_options": [row["candidate_id"] for row in held],
                "evidence_required": ["candidate-qualification-matrix.json", "falsification-review-queue.json", "candidate-lineage-dependency-review.json"],
                "stop_rule": "Leave the candidate held when any required field is missing or publisher dependence is unresolved.",
                "assignee": None,
                "completed_on": None,
                "signoff": None,
            },
            {
                "task_id": "rights_and_boundary_review",
                "owner_role": "lineage_reviewer",
                "instruction": "Review one source family’s rights, publisher dependence, redistribution boundary, and company-bridge prohibition, then record the unresolved question.",
                "evidence_required": ["rights-review-queue.json", "rights-evidence-register.json", "publisher-dependence-summary.json", "test_rights_release_gate.py"],
                "stop_rule": "Do not clear reuse or internal connection from metadata alone; escalate missing terms or ownership evidence.",
                "assignee": None,
                "completed_on": None,
                "signoff": None,
            },
        ],
        "acceptance_criteria": [
            "All three tasks have named assignees and dated sign-off.",
            "The successor records at least one held candidate and one unresolved rights question.",
            "No company data is accessed and no pilot status is upgraded by this packet.",
        ],
        "next_action": "Assign a primary and backup human for each task, then attach the signed packet to the next refresh handoff.",
        "boundary": "This packet makes succession work executable; it is not evidence that human ownership or company-pilot approval exists.",
    }
    OUTPUT.write_text(json.dumps(packet, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(packet['review_tasks'])} tasks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
