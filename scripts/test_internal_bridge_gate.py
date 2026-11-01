#!/usr/bin/env python3
"""Verify that internal company pilots remain blocked before qualification."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    qualification = load("candidate-qualification-matrix.json")
    pilots = load("pilot-register.json")
    health = load("release-health.json")
    assert qualification["qualified_external_trend_count"] >= 1
    assert pilots["pilots"]
    assert all(item["status"] == "design_only_external_gate" for item in pilots["pilots"])
    assert {item["external_gate"]["current_status"] for item in pilots["pilots"]} == {"held", "monitored_external_trend"}
    assert all(item["company_ref"]["company_id"] is None for item in pilots["pilots"])
    assert health["sections"]["company_pilots"]["approved_tests"] == 0
    assert "no company pilot is approved; company decision contract, rights owner, and internal exposure definition remain open" in health["blockers"]
    print("internal bridge gate: no company connection is allowed before an approved decision contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
