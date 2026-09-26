#!/usr/bin/env python3
"""Regression checks for the scope of the governing broad-program documents."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    goal = (ROOT / "BROAD-GOAL-RESTATEMENT_V1.md").read_text(encoding="utf-8")
    focus = (ROOT / "BROAD-PROGRAM-FOCUS_V1.md").read_text(encoding="utf-8")
    continuity = (ROOT / "analysis/US-BROAD-PROGRAM-CONTINUITY-LEDGER_V1.md").read_text(
        encoding="utf-8"
    )
    coverage_audit = (ROOT / "analysis/US-BROAD-THEME-END-TO-END-COVERAGE-AUDIT_V1.json").read_text(
        encoding="utf-8"
    )

    assert "The 14-theme breadth requirement" in goal
    assert "condition, shock, decision, or capability" in goal
    assert "political judgment, collective action, switching, exit, or non-use" in goal
    assert "No deep lane" in goal and "one dataset" in goal
    assert "full US-centered" in focus and "one household lane" in focus
    assert "active long-term program control record" in continuity
    assert '"explicit_open_link"' in coverage_audit
    assert '"same_unit_end_to_end_link"' not in coverage_audit
    assert all(re.search(rf"^\s*{number}\.\s", goal, re.MULTILINE) for number in range(1, 15))

    print("PASS broad-goal integrity checks: scope, chain, and 14 themes preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
