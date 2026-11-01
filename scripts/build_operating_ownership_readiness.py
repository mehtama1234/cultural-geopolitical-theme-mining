#!/usr/bin/env python3
"""Evaluate whether the observatory is ready for named human handoff."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "operating-ownership-readiness.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    ownership = load("ownership-assignment-queue.json")
    successor = load("successor-run-evidence.json")
    packet = load("successor-review-packet.json")
    pass_count = sum(check["status"] == "pass" for check in successor["checks"])
    blockers = []
    if successor["status"] != "pass":
        blockers.append("successor validation is not passing")
    if ownership["unassigned_role_count"]:
        blockers.append(f"{ownership['unassigned_role_count']} operating roles lack named primary and backup owners")
    if successor["human_successor_assignment"] is not True:
        blockers.append("human successor assignment is not recorded")
    if packet["status"] != "assigned_pending_signoff":
        blockers.append("successor packet assignees and dated sign-offs are incomplete")
    status = "ready_for_named_human_assignment" if successor["status"] == "pass" and ownership["unassigned_role_count"] == ownership["role_count"] else "handoff_incomplete"
    payload = {
        "schema": "external-trend-intelligence.operating-ownership-readiness.v1",
        "status": status,
        "role_count": ownership["role_count"],
        "assigned_role_count": ownership["assigned_role_count"],
        "successor_checks_passed": pass_count,
        "successor_check_count": len(successor["checks"]),
        "successor_run_status": successor["status"],
        "human_successor_assignment": successor["human_successor_assignment"],
        "successor_packet_status": packet["status"],
        "blockers": blockers,
        "next_action": ownership["next_action"],
        "boundary": "This readiness evaluation separates reproducible control validation from named human ownership. It does not assign people, approve a company pilot, or authorize internal data access.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({status}; {len(blockers)} blockers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
