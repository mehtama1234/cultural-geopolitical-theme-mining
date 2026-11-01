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
    history = load("refresh-history.json")
    refresh_status = load("refresh-status.json")
    assert progress["baseline"]["records"] == manifest["record_count"] == scorecard["metrics"]["records"]
    assert progress["baseline"]["themes"] == len(manifest["program_theme_counts"]) == scorecard["metrics"]["themes"]
    assert progress["baseline"]["source_families"] == scorecard["metrics"]["source_families"] == refresh_status["family_count"]
    assert progress["baseline"]["release_artifacts"] == release["artifact_count"]
    assert progress["baseline"]["refresh_runs_recorded"] == history["run_count"]
    release_paths = {item["path"] for item in release["artifacts"]}
    assert {
        ".github/workflows/external-observatory-refresh.yml",
        "analysis/external-trend-intelligence/program-scorecard.json",
        "analysis/external-trend-intelligence/review-calendar.json",
        "analysis/external-trend-intelligence/financial-room-rights-review.json",
        "analysis/external-trend-intelligence/operating-handoff.json",
        "analysis/external-trend-intelligence/successor-run-evidence.json",
        "analysis/external-trend-intelligence/operational-kpi-scorecard.json",
        "analysis/external-trend-intelligence/trend-monitoring-status.json",
        "analysis/external-trend-intelligence/falsification-review-queue.json",
        "analysis/external-trend-intelligence/pilot-design-dry-run.json",
    }.issubset(release_paths)
    print("program baseline consistency: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
