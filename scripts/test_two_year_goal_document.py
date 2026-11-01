#!/usr/bin/env python3
"""Validate the human-readable two-year goal contract."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
DOCUMENT = ANALYSIS / "TWO-YEAR-GOAL.md"


def main() -> int:
    text = DOCUMENT.read_text()
    required_phrases = [
        "# Two-year external-first enterprise trend-intelligence observatory",
        "## The goal in plain language",
        "## What the observatory must preserve",
        "## External source families",
        "## Concrete external datasets already in use",
        "## Reader-facing chart themes",
        "## 24-month delivery phases",
        "### Months 0–3: control plane",
        "### Months 4–6: dependable intake",
        "### Months 7–12: trend qualification",
        "### Months 13–18: decision relevance",
        "### Months 19–24: operationalize and hand off",
        "The system must be useful without company data. Internal data is a second-stage",
        "No company data is connected until every approval gate passes",
        "`goal-completion-audit.json`",
        "`observatory-chart-catalog.json`",
        "`pilot-activation-queue.json`",
    ]
    missing = [phrase for phrase in required_phrases if phrase not in text]
    if missing:
        raise AssertionError(f"goal document missing required contract sections: {missing}")
    expected_families = [
        "cultural-geopolitical-theme-mining",
        "social-research",
        "trend-hunting",
        "annual-report-research",
        "inc5000-analysis",
        "ibis-industries",
        "research-signals",
        "organization-intelligence-system",
    ]
    missing_families = [family for family in expected_families if family not in text]
    if missing_families:
        raise AssertionError(f"goal document missing source families: {missing_families}")
    print("two-year goal document contract: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
