#!/usr/bin/env python3
"""Audit the two-year observatory objective against current repository evidence."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "goal-completion-audit.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    progress = load("program-progress.json")
    health = load("release-health.json")
    qualification = load("candidate-qualification-matrix.json")
    audit = {
        "schema": "external-trend-intelligence.goal-completion-audit.v1",
        "objective": "two-year external-first enterprise trend-intelligence observatory",
        "as_of": progress["as_of"],
        "overall_status": "in_progress_with_open_gates",
        "requirements": [
            {"id": "external_capture_refresh", "status": "partial", "evidence": ["source-family-registry.json", "refresh_external_observatory.py", "refresh-status.json", "refresh-history.json", "test_refresh_stale_gate.py", "test_external_refresh_workflow.py", "test_program_baseline_consistency.py", "program-scorecard.json"], "gap": "The stale gate, scheduled workflow contract, baseline consistency, and recovery path are exercised and refresh runs are recorded with 56-step pass telemetry, but sustained unattended operation over the scheduled two-year cadence is not yet demonstrated."},
            {"id": "lineage_rights_units_periods_uncertainty", "status": "partial", "evidence": ["external-family-lineage-review.json", "rights-review-queue.json", "rights-evidence-register.json", "shed-emergency-expense-uncertainty-audit.json", "shed-point-estimate-reproduction-audit.json", "test_rights_release_gate.py", "observation-manifest.json"], "gap": "Rights and publisher dependence remain unverified for all families; the SHED point estimate now reproduces through the publisher-derived field, but only a non-release naive interval is available and design-based variance remains open. The release gate is tested to fail closed."},
            {"id": "independent_source_comparison", "status": "partial", "evidence": ["independent-stage-comparison.json", "room-independent-comparison.json", "room-independent-result.json", "us-financial-room-independent-comparison.json", "shed-emergency-expense-2013-2025.json", "bounded-subset-lineage-review.json"], "gap": "Comparisons now include a closer SHED emergency-liquidity measure and an independent U.S. SHED/USDA mechanism challenge, but remain mechanism-only; no common unit and holdout have passed."},
            {"id": "trend_qualification", "status": "open", "evidence": ["candidate-qualification-matrix.json", "trend-qualification-rubric.json"], "gap": f"{qualification['qualified_external_trend_count']} qualified trends; {qualification['held_count']} candidates held."},
            {"id": "backtest_and_falsification", "status": "partial", "evidence": ["backtest-readiness.json", "backtest-comparability-review.json", "food-insecurity-temporal-holdout.json", "temporal-holdout-design.json", "temporal-holdout-result.json", "shed-temporal-holdout.json", "usda-temporal-holdout.json"], "gap": "The food-insecurity candidate now has a descriptive Urban 2019–2023 to 2024–2025 holdout and non-pooled USDA challenge; causal validation, uncertainty harmonization, and holdouts for the other candidates remain open."},
            {"id": "decision_ready_frontend", "status": "partial", "evidence": ["board.html", "FRONTEND-INTEGRATION.md", "candidate-qualification-matrix.json", "temporal-decision-narrative.json"], "gap": "Reader surface exposes the qualified external food-insecurity pattern and held candidates, but no validated company outcome is published."},
            {"id": "analyst_operating_model", "status": "partial", "evidence": ["ANALYST-OPERATING-MODEL.md", "REFRESH-RUNBOOK.md", "operating-handoff.json", "evidence-acquisition-plan.json"], "gap": "The handoff records six roles and exercised controls, but named ownership and an independent successor run are still outstanding."},
            {"id": "validated_company_pilots", "status": "open", "evidence": ["pilot-register.json", "PILOT-VALIDATION-PROTOCOL.md", "test_internal_bridge_gate.py"], "gap": "No pilot is approved because a company decision contract, named rights owner, internal exposure definition, and privacy review are still required after external monitoring; the fail-closed bridge gate is exercised."},
        ],
        "release_status": health["release_status"],
        "boundary": "This audit is a conservative program status report. It does not redefine the goal as complete because the control plane and frontend are operational.",
        "next_action": "Use evidence-acquisition-plan.json to close the independent compatible holdout and rights gates, then re-run this audit before any internal bridge.",
    }
    OUTPUT.write_text(json.dumps(audit, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(audit['requirements'])} requirements)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
