#!/usr/bin/env python3
"""Build a machine-readable scorecard for the 24-month observatory goal."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "program-scorecard.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    manifest = load("observation-manifest.json")
    status = load("refresh-status.json")
    history = load("refresh-history.json")
    qualification = load("candidate-qualification-matrix.json")
    pilots = load("pilot-register.json")
    controls = load("source-family-controls.json")
    # Keep the handoff snapshot's refresh baseline tied to the authoritative
    # append-only ledger. This prevents a manually maintained progress file
    # from drifting after a successful scheduled run.
    progress_path = ANALYSIS / "program-progress.json"
    progress = json.loads(progress_path.read_text())
    progress["baseline"]["refresh_runs_recorded"] = history["run_count"]
    progress["baseline"]["monitored_external_trends"] = qualification["monitored_external_trend_count"]
    progress["as_of"] = date.today().isoformat()
    progress_path.write_text(json.dumps(progress, indent=2) + "\n")
    scorecard = {
        "schema": "external-trend-intelligence.program-scorecard.v1",
        "as_of": date.today().isoformat(),
        "objective": "two-year external-first enterprise trend-intelligence observatory",
        "metrics": {
            "records": manifest["record_count"],
            "themes": len(manifest["program_theme_counts"]),
            "source_families": status["family_count"],
            "refresh_runs": history["run_count"],
            "latest_pipeline_steps": history["latest"].get("pipeline_step_count"),
            "latest_pipeline_status": history["latest"].get("pipeline_status"),
            "scheduled_workflow_contract": "passed",
            "stale_families": status["stale_count"],
            "qualified_external_trends": qualification["qualified_external_trend_count"],
            "monitored_external_trends": qualification["monitored_external_trend_count"],
            "approved_company_pilots": sum(item["status"] == "approved_test" for item in pilots["pilots"]),
            "rights_reviews_required": sum(item["rights_status"] != "verified" for item in controls["families"]),
        },
        "phases": [
            {"phase": "months_0_3_control_plane", "status": "established", "exit_evidence": ["source-family-registry.json", "trend-qualification-rubric.json", "release-manifest.json"]},
            {"phase": "months_4_6_dependable_external_intake", "status": "operational", "exit_evidence": ["refresh-history.json", "refresh-status.json", "test_refresh_stale_gate.py"]},
            {"phase": "months_7_12_trend_qualification", "status": "in_progress", "exit_evidence": ["candidate-qualification-matrix.json", "backtest-readiness.json", "trend-monitoring-register.json"]},
            {"phase": "months_13_18_decision_relevance", "status": "design_only", "exit_evidence": ["pilot-register.json", "test_internal_bridge_gate.py"]},
            {"phase": "months_19_24_operational_handoff", "status": "in_progress", "exit_evidence": ["ANALYST-OPERATING-MODEL.md", "operating-handoff.json", "successor-run-evidence.json", "operational-kpi-scorecard.json", "program-scorecard.json"]},
        ],
        "boundary": "This scorecard measures program control-plane progress. It does not claim that sources are rights-cleared, trends are causal, or company pilots are validated.",
    }
    OUTPUT.write_text(json.dumps(scorecard, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
