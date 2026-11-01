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
    ownership = load("ownership-assignment-queue.json")
    independence_queue = load("candidate-independence-adjudication-queue.json")
    continuity = load("refresh-continuity-audit.json")
    inventory_dependence = load("record-host-dependence-audit.json")
    record_quality = load("record-quality-audit.json")
    remediation = load("record-quality-remediation-queue.json")
    host_queue = load("host-dependence-review-queue.json")
    open_gates = load("open-gate-register.json")
    dry_run = load("pilot-design-dry-run.json")
    intake = load("pilot-contract-intake.json")
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
    assert m["pilot_contract_intake_status"] == intake["status"]
    assert m["pilot_contract_count"] == intake["pilot_count"]
    assert m["unassigned_operating_roles"] == ownership["unassigned_role_count"]
    assert m["independence_adjudication_pending"] == independence_queue["unassigned_count"]
    assert m["independence_adjudication_high_priority"] == independence_queue["high_priority_count"]
    assert m["observed_refresh_continuity"] == continuity["continuity_status"]
    assert m["unattended_two_year_coverage"] == continuity["unattended_two_year_coverage"]
    assert m["inventory_unique_host_count"] == inventory_dependence["unique_host_count"]
    assert m["inventory_shared_host_count"] == inventory_dependence["shared_host_count"]
    assert m["inventory_shared_host_record_count"] == inventory_dependence["shared_host_record_count"]
    assert m["record_quality_min_coverage"] == min(record_quality["field_coverage"].values())
    assert m["record_quality_gap_count"] == remediation["record_count_with_gaps"]
    assert m["host_dependence_reviews_unassigned"] == host_queue["unassigned_count"]
    assert m["host_dependence_reviews_high_priority"] == host_queue["high_priority_count"]
    assert m["open_gate_count"] == open_gates["gate_count"]
    assert m["critical_open_gate_count"] == open_gates["critical_gate_count"]
    assert m["open_gate_work_item_count"] == open_gates["total_open_work_items"]
    print("operational KPI scorecard: reconciled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
