#!/usr/bin/env python3
"""Ensure the human source guide covers every registered source family."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"


def main() -> int:
    registry = json.loads((ANALYSIS / "source-family-registry.json").read_text())
    guide = (ANALYSIS / "EXTERNAL-DATA-SOURCES.md").read_text()
    families = registry["source_families"]
    assert len(families) == 8
    labels = {
        "cultural-geopolitical-theme-mining": "Cultural-geopolitical theme mining",
        "social-research": "Social research",
        "trend-hunting": "Trend hunting",
        "annual-report-research": "Annual-report research",
        "inc5000-analysis": "Inc. 5000 analysis",
        "ibis-industries": "IBIS industries",
        "research-signals": "Research signals",
        "organization-intelligence-system": "Organization intelligence system",
    }
    missing = [labels[row["id"]] for row in families if labels.get(row["id"]) not in guide]
    if missing:
        raise AssertionError(f"source guide missing registered families: {missing}")
    for family in families:
        assert family["role"] and family["evidence_boundary"]
    assert "Current boundary" in guide and "lineage" in guide and "rights" in guide
    print("source family guide alignment: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
