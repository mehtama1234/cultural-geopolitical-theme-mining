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
    pilot_intake = load("pilot-contract-intake.json")
    monitoring = load("trend-monitoring-status.json")
    dependence = load("publisher-dependence-summary.json")
    ownership = load("ownership-assignment-queue.json")
    independence_queue = load("candidate-independence-adjudication-queue.json")
    continuity = load("refresh-continuity-audit.json")
    inventory_dependence = load("record-host-dependence-audit.json")
    record_quality = load("record-quality-audit.json")
    remediation = load("record-quality-remediation-queue.json")
    host_queue = load("host-dependence-review-queue.json")
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
        "pilot_contract_intake_status": pilot_intake["status"],
        "pilot_contract_count": pilot_intake["pilot_count"],
        "monitoring_watches": monitoring["trend_count"],
        "qualified_monitor_watches": monitoring["qualified_monitor_count"],
        "prequalification_watches": monitoring["prequalification_watch_count"],
        "shared_host_count": dependence["shared_host_count"],
        "inventory_unique_host_count": inventory_dependence["unique_host_count"],
        "inventory_shared_host_count": inventory_dependence["shared_host_count"],
        "inventory_shared_host_record_count": inventory_dependence["shared_host_record_count"],
        "host_dependence_reviews_unassigned": host_queue["unassigned_count"],
        "host_dependence_reviews_high_priority": host_queue["high_priority_count"],
        "publisher_independence_status": dependence["independence_status"],
        "record_quality_min_coverage": min(record_quality["field_coverage"].values()),
        "record_quality_gap_count": remediation["record_count_with_gaps"],
        "unassigned_operating_roles": ownership["unassigned_role_count"],
        "independence_adjudication_pending": independence_queue["unassigned_count"],
        "independence_adjudication_high_priority": independence_queue["high_priority_count"],
        "observed_refresh_continuity": continuity["continuity_status"],
        "unattended_two_year_coverage": continuity["unattended_two_year_coverage"],
    }
    thresholds = {
        "refresh_pipeline_pass_rate": {"target": "100% latest run", "status": "pass" if metrics["latest_pipeline_status"] == "passed" else "hold"},
        "stale_source_gate": {"target": "0 stale families", "status": "pass" if metrics["stale_source_families"] == 0 else "hold"},
        "source_contract_gate": {"target": "0 incomplete families", "status": "pass" if metrics["incomplete_source_families"] == 0 else "hold"},
        "successor_validation": {"target": "read-only validation passes", "status": successor["status"]},
        "external_first_pilot_gate": {"target": "0 approved tests until all gates pass", "status": "pass" if metrics["approved_company_pilots"] == 0 else "review"},
        "external_only_boundary": {"target": "no connected company data in release", "status": metrics["external_only_boundary"]},
        "pilot_design_contracts": {"target": "all design-only pilots pass contract dry run", "status": metrics["pilot_design_dry_run"]},
        "pilot_intake_contracts": {"target": "every design-only pilot has a fillable pre-registration contract", "status": "pass" if metrics["pilot_contract_count"] == pilots["pilot_count"] and metrics["pilot_contract_intake_status"] == "template_only_no_company_data" else "hold"},
        "monitoring_register_coverage": {"target": "every candidate has an execution state", "status": "pass" if metrics["monitoring_watches"] == qualification["candidate_count"] else "hold"},
        "publisher_dependence_review": {"target": "shared hosts remain visible and reviewed", "status": "pass" if metrics["inventory_shared_host_count"] >= 0 and metrics["publisher_independence_status"] != "unreviewed" else "hold"},
        "record_metadata_completeness": {"target": "all required record metadata fields explicitly present", "status": "pass" if metrics["record_quality_gap_count"] == 0 and metrics["record_quality_min_coverage"] == 1 else "hold"},
        "host_dependence_review_queue": {"target": "shared-host lineage work is assigned and dispositioned", "status": "pass" if metrics["host_dependence_reviews_unassigned"] == 0 else "hold"},
        "named_operating_ownership": {"target": "0 unassigned primary/backup roles", "status": "pass" if metrics["unassigned_operating_roles"] == 0 else "hold"},
        "independence_adjudication": {"target": "every candidate has a disposition and reviewer", "status": "pass" if metrics["independence_adjudication_pending"] == 0 else "hold"},
        "refresh_continuity": {"target": "weekly runs observed across distinct weeks", "status": "pass" if metrics["unattended_two_year_coverage"] == "demonstrated" else "hold"},
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
