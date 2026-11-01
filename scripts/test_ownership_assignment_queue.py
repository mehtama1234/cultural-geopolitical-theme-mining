#!/usr/bin/env python3
"""Ensure the ownership queue reconciles exactly to the operating handoff."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def main() -> int:
    handoff = json.loads((ANALYSIS / "operating-handoff.json").read_text())
    queue = json.loads((ANALYSIS / "ownership-assignment-queue.json").read_text())
    handoff_by_role = {role["role"]: role for role in handoff["roles"]}
    assert queue["schema"] == "external-trend-intelligence.ownership-assignment-queue.v1"
    assert queue["role_count"] == len(handoff["roles"]) == len(queue["roles"])
    assert {item["role"] for item in queue["roles"]} == set(handoff_by_role)
    for item in queue["roles"]:
        role = handoff_by_role[item["role"]]
        expected_status = "unassigned" if role["owner"] == "unassigned" else "assigned"
        assert item["current_status"] == expected_status
        assert item["evidence"] == role["evidence"]
        assert item["acceptance_criteria"] and item["handoff_checkpoint"]
    assert queue["assigned_role_count"] == sum(role["owner"] != "unassigned" for role in handoff["roles"])
    assert queue["unassigned_role_count"] + queue["assigned_role_count"] == queue["role_count"]
    protocol = queue["assignment_protocol"]
    assert protocol["assignment_sla_business_days"] > 0
    assert protocol["required_fields"] and protocol["backup_activation"] and protocol["escalation_path"]
    assert protocol["acceptance_evidence"]
    request = (ANALYSIS / "OWNERSHIP-ASSIGNMENT-REQUEST.md").read_text()
    assert "Required fields for every role" in request
    for role in queue["roles"]:
        assert f"`{role['role']}`" in request
    for field in protocol["required_fields"]:
        assert field.replace("_", " ") in request.lower()
    print("ownership assignment queue: reconciled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
