#!/usr/bin/env python3
"""Validate that the successor packet is actionable but cannot self-authorize."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"


def main() -> int:
    packet = json.loads((ANALYSIS / "successor-review-packet.json").read_text())
    assert packet["status"] == "ready_for_named_human_successor"
    assert len(packet["review_tasks"]) == 3
    required = {"assignee", "completed_on", "signoff", "evidence_required", "stop_rule"}
    for task in packet["review_tasks"]:
        assert required <= task.keys()
        assert task["assignee"] is None
        assert task["completed_on"] is None
        assert task["signoff"] is None
        assert task["evidence_required"] and task["stop_rule"]
    assert any("company data" in criterion.lower() for criterion in packet["acceptance_criteria"])
    assert "not evidence" in packet["boundary"]
    print("successor review packet: actionable and fail-closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
