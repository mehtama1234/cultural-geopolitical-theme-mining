#!/usr/bin/env python3
"""Validate the human-readable external data source guide."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "analysis" / "external-trend-intelligence" / "EXTERNAL-DATA-SOURCES.md"


def main() -> int:
    text = GUIDE.read_text()
    required = [
        "# External data sources in the observatory",
        "## The eight source families",
        "## Named external datasets currently used for tests",
        "USDA Economic Research Service",
        "Urban Institute Well-Being and Basic Needs Survey",
        "Federal Reserve SHED",
        "ACS and NHTS",
        "Census County Business Patterns and Nonemployer Statistics",
        "NPALS public tables",
        "Open Repair Alliance",
        "IBIS industries",
        "## How a source reaches the frontend",
        "source artifact",
        "lineage and rights review",
        "qualification/backtest gate",
        "No company identifier or internal dataset is connected",
    ]
    missing = [phrase for phrase in required if phrase not in text]
    if missing:
        raise AssertionError(f"external source guide missing required content: {missing}")
    families = [
        "Cultural-geopolitical theme mining",
        "Social research",
        "Trend hunting",
        "Annual-report research",
        "Inc. 5000 analysis",
        "IBIS industries",
        "Research signals",
        "Organization intelligence system",
    ]
    assert all(family in text for family in families)
    print("external data source guide contract: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
