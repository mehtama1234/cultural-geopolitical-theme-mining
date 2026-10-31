#!/usr/bin/env python3
"""Ensure published program metrics agree across authoritative artifacts."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    manifest = load("observation-manifest.json")
    progress = load("program-progress.json")
    scorecard = load("program-scorecard.json")
    release = load("release-manifest.json")
    assert progress["baseline"]["records"] == manifest["record_count"] == scorecard["metrics"]["records"]
    assert progress["baseline"]["themes"] == len(manifest["program_theme_counts"]) == scorecard["metrics"]["themes"]
    assert progress["baseline"]["source_families"] == scorecard["metrics"]["source_families"] == 8
    assert progress["baseline"]["release_artifacts"] == release["artifact_count"]
    print("program baseline consistency: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
