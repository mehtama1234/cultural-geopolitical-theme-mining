#!/usr/bin/env python3
"""Ensure falsification queue rows mirror the qualification matrix."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    matrix = load("candidate-qualification-matrix.json")
    queue = load("falsification-review-queue.json")
    by_id = {row["candidate_id"]: row for row in matrix["rows"]}
    assert queue["candidate_count"] == matrix["candidate_count"]
    assert set(row["candidate_id"] for row in queue["rows"]) == set(by_id)
    for row in queue["rows"]:
        source = by_id[row["candidate_id"]]
        assert row["gate_status"] == source["gate_status"]
        assert row["blocking_gates"] == source["blocking_gates"]
        assert row["falsifier"] == source["falsifier"]
        assert row["next_decisive_test"] == source["next_action"]
    print("falsification review queue: reconciled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
