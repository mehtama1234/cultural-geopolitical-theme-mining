#!/usr/bin/env python3
"""Reconcile the rights ownership queue with the rights review queue."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"


def main() -> int:
    review = json.loads((ANALYSIS / "rights-review-queue.json").read_text())
    queue = json.loads((ANALYSIS / "rights-assignment-queue.json").read_text())
    expected = {row["family_id"] for row in review["rows"]}
    observed = {row["family_id"] for row in queue["rows"]}
    assert queue["schema"] == "external-trend-intelligence.rights-assignment-queue.v1"
    assert queue["family_count"] == len(queue["rows"])
    assert observed == expected
    assert queue["unassigned_family_count"] + queue["assigned_family_count"] == queue["family_count"]
    assert all(row["acceptance_criteria"] and row["checkpoint"] for row in queue["rows"])
    assert all(row.get("review_plan") and row["review_plan"]["first_artifact"] for row in review["rows"])
    request = (ANALYSIS / "RIGHTS-REVIEW-REQUEST.md").read_text()
    for family_id in sorted(expected):
        assert f"| {family_id} |" in request, family_id
    for phrase in ["Terms evidence", "Storage / transform / redistribution decision", "Rights reviewer", "Lineage reviewer"]:
        assert phrase in request, phrase
    print("rights assignment queue: reconciled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
