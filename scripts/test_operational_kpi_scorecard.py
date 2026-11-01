#!/usr/bin/env python3
"""Ensure the operating KPI scorecard reconciles to authoritative artifacts."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    kpi = load("operational-kpi-scorecard.json")
    history = load("refresh-history.json")
    status = load("refresh-status.json")
    qualification = load("candidate-qualification-matrix.json")
    rights = load("source-family-controls.json")
    pilots = load("pilot-readiness.json")
    successor = load("successor-run-evidence.json")
    dry_run = load("pilot-design-dry-run.json")
    m = kpi["metrics"]
    assert m["refresh_runs_recorded"] == history["run_count"]
    assert m["latest_pipeline_steps"] == history["latest"]["pipeline_step_count"]
    assert m["latest_pipeline_status"] == history["latest"]["pipeline_status"]
    assert m["stale_source_families"] == status["stale_count"]
    assert m["incomplete_source_families"] == status["incomplete_count"]
    assert m["qualified_external_trends"] == qualification["qualified_external_trend_count"]
    assert m["held_candidates"] == qualification["held_count"]
    assert m["rights_reviews_required"] == sum(item["rights_status"] != "verified" for item in rights["families"])
    assert m["approved_company_pilots"] == pilots["ready_for_approved_test_count"]
    assert m["successor_validation_status"] == successor["status"]
    assert m["pilot_design_dry_run"] == dry_run["status"]
    print("operational KPI scorecard: reconciled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
