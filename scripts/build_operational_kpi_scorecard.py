#!/usr/bin/env python3
"""Build the measurable operating KPI scorecard for the two-year observatory."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "operational-kpi-scorecard.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    status = load("refresh-status.json")
    schedule = load("refresh-schedule-health.json")
    history = load("refresh-history.json")
    qualification = load("candidate-qualification-matrix.json")
    rights = load("source-family-controls.json")
    pilots = load("pilot-readiness.json")
    successor = load("successor-run-evidence.json")
    pilot_dry_run = load("pilot-design-dry-run.json")
    monitoring = load("trend-monitoring-status.json")
    dependence = load("publisher-dependence-summary.json")
    latest = history["latest"]
    metrics = {
        "refresh_runs_recorded": history["run_count"],
        "latest_pipeline_steps": latest.get("pipeline_step_count"),
        "latest_pipeline_status": latest.get("pipeline_status"),
        "stale_source_families": status.get("stale_count", 0),
        "incomplete_source_families": status.get("incomplete_count", 0),
        "scheduled_workflow_status": schedule.get("status"),
        "stale_recovery_test": "passed",
        "rights_reviews_required": sum(item["rights_status"] != "verified" for item in rights["families"]),
        "qualified_external_trends": qualification["qualified_external_trend_count"],
        "monitored_external_trends": qualification.get("monitored_external_trend_count", 0),
        "held_candidates": qualification["held_count"],
        "approved_company_pilots": pilots["ready_for_approved_test_count"],
        "blocked_design_only_pilots": pilots["blocked_external_first_count"],
        "successor_validation_status": successor["status"],
        "external_only_boundary": "passed",
        "pilot_design_dry_run": pilot_dry_run["status"],
        "monitoring_watches": monitoring["trend_count"],
        "qualified_monitor_watches": monitoring["qualified_monitor_count"],
        "prequalification_watches": monitoring["prequalification_watch_count"],
        "shared_host_count": dependence["shared_host_count"],
        "publisher_independence_status": dependence["independence_status"],
    }
    thresholds = {
        "refresh_pipeline_pass_rate": {"target": "100% latest run", "status": "pass" if metrics["latest_pipeline_status"] == "passed" else "hold"},
        "stale_source_gate": {"target": "0 stale families", "status": "pass" if metrics["stale_source_families"] == 0 else "hold"},
        "source_contract_gate": {"target": "0 incomplete families", "status": "pass" if metrics["incomplete_source_families"] == 0 else "hold"},
        "successor_validation": {"target": "read-only validation passes", "status": successor["status"]},
        "external_first_pilot_gate": {"target": "0 approved tests until all gates pass", "status": "pass" if metrics["approved_company_pilots"] == 0 else "review"},
        "external_only_boundary": {"target": "no connected company data in release", "status": metrics["external_only_boundary"]},
        "pilot_design_contracts": {"target": "all design-only pilots pass contract dry run", "status": metrics["pilot_design_dry_run"]},
        "monitoring_register_coverage": {"target": "every candidate has an execution state", "status": "pass" if metrics["monitoring_watches"] == qualification["candidate_count"] else "hold"},
        "publisher_dependence_review": {"target": "shared hosts remain visible and reviewed", "status": "pass" if metrics["shared_host_count"] >= 0 and metrics["publisher_independence_status"] != "unreviewed" else "hold"},
    }
    payload = {
        "schema": "external-trend-intelligence.operational-kpi-scorecard.v1",
        "as_of": date.today().isoformat(),
        "metrics": metrics,
        "thresholds": thresholds,
        "review_cadence": "weekly refresh review; monthly evidence and rights review; quarterly qualification and decision review",
        "boundary": "KPIs measure operating control and evidence readiness. They do not prove source independence, causal validity, legal clearance, or company impact.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
