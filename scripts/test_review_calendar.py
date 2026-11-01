#!/usr/bin/env python3
"""Validate the 24-month review calendar against the current program phases."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def main() -> int:
    calendar = json.loads((ANALYSIS / "review-calendar.json").read_text())
    scorecard = json.loads((ANALYSIS / "program-scorecard.json").read_text())
    assert calendar["schema"] == "external-trend-intelligence.review-calendar.v1"
    assert calendar["horizon_months"] == 24
    checkpoints = calendar["checkpoints"]
    assert calendar["checkpoint_count"] == len(checkpoints) == 9
    assert [item["month"] for item in checkpoints] == [1, 3, 6, 9, 12, 15, 18, 21, 24]
    phase_ids = {phase["phase"] for phase in scorecard["phases"]}
    assert all(item["phase"] in phase_ids for item in checkpoints)
    assert all(item["cadence"] in {"monthly", "quarterly"} for item in checkpoints)
    assert all(item["owner"] and item["review"] and item["evidence"] for item in checkpoints)
    assert "does not imply" in calendar["boundary"]
    print("review calendar contract: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
