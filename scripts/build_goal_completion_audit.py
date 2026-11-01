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
    history = load("refresh-history.json")
    ibis_review = load("ibis-claim-source-review.json")
    financial_rights = load("financial-room-rights-review.json")
    pipeline_steps = history["latest"].get("pipeline_step_count", "recorded")
    audit = {
        "schema": "external-trend-intelligence.goal-completion-audit.v1",
        "objective": "two-year external-first enterprise trend-intelligence observatory",
        "as_of": progress["as_of"],
        "overall_status": "in_progress_with_open_gates",
        "requirements": [
            {"id": "external_capture_refresh", "status": "partial", "evidence": ["source-family-registry.json", "refresh_external_observatory.py", "refresh-schedule-health.json", "refresh-status.json", "refresh-history.json", "test_refresh_stale_gate.py", "test_external_refresh_workflow.py", "test_program_baseline_consistency.py", "program-scorecard.json"], "gap": f"The weekly schedule contract, stale gate, baseline consistency, and recovery path are exercised and refresh runs are recorded with {pipeline_steps}-step pass telemetry, but sustained unattended operation over the scheduled two-year cadence is not yet demonstrated."},
            {"id": "lineage_rights_units_periods_uncertainty", "status": "partial", "evidence": ["external-family-lineage-review.json", "rights-review-queue.json", "rights-assignment-queue.json", "rights-evidence-register.json", "food-insecurity-rights-review.json", "financial-room-rights-review.json", "mobility-access-rights-review.json", "uncertainty-coverage-audit.json", "external-acquisition-rights-review.json", "ibis-claim-dependency-review.json", "ibis-force-claim-review.json", "shed-emergency-expense-uncertainty-audit.json", "shed-point-estimate-reproduction-audit.json", "test_rights_release_gate.py", "observation-manifest.json"], "gap": f"Rights and publisher dependence remain unverified for all source families; the rights-assignment queue now makes the eight-family ownership work explicit, while candidate-specific reviews cover the monitored food-security lane, the mobility comparison, and {financial_rights['source_count']} financial-room sources. The uncertainty coverage audit makes source-level, incomplete, and pending uncertainty visible across six decision-facing artifacts. The {ibis_review['sample_industry_count']}-industry IBIS sample and six-force review expose repeated source IDs, URLs, missing claim periods, and metadata gaps for dependency review. Upstream redistribution and enterprise rights approval remain open. The SHED point estimate has only a non-release naive interval and design-based variance remains open."},
            {"id": "independent_source_comparison", "status": "partial", "evidence": ["independent-stage-comparison.json", "food-insecurity-independent-comparison.json", "mobility-access-independent-comparison.json", "room-independent-comparison.json", "room-independent-result.json", "us-financial-room-independent-comparison.json", "compatible-measure-search.json", "global-growth-forecast-comparison.json", "shed-emergency-expense-2013-2025.json", "bounded-subset-lineage-review.json"], "gap": "The compatibility scan now finds 209 cross-host measure groups and the release includes bounded food-insecurity, mobility-access, and OECD/UN DESA/World Bank comparisons. These comparisons have distinct publishers and directional signals but remain non-comparable holdouts because populations, reference periods, uncertainty, weighting, and rights differ; forecast vintages and other comparisons still require outcome backtests, and no common-unit observed holdout has passed."},
            {"id": "trend_qualification", "status": "open", "evidence": ["candidate-qualification-matrix.json", "trend-qualification-rubric.json"], "gap": f"{qualification['qualified_external_trend_count']} qualified trends; {qualification['held_count']} candidates held."},
            {"id": "backtest_and_falsification", "status": "partial", "evidence": ["backtest-readiness.json", "backtest-comparability-review.json", "food-insecurity-temporal-holdout.json", "ibis-adult-day-outcome-review.json", "temporal-holdout-design.json", "temporal-holdout-result.json", "shed-temporal-holdout.json", "usda-temporal-holdout.json"], "gap": "The food-insecurity candidate has a descriptive Urban 2019–2023 to 2024–2025 holdout and non-pooled USDA challenge, and the IBIS adult-day-care lane now has a dated CDC outcome series plus a CMS Medicaid rate comparison; causal validation, uncertainty harmonization, independent utilization outcomes, and holdouts for the other candidates remain open."},
            {"id": "decision_ready_frontend", "status": "partial", "evidence": ["board.html", "FRONTEND-INTEGRATION.md", "candidate-qualification-matrix.json", "temporal-decision-narrative.json"], "gap": "Reader surface exposes the qualified external food-insecurity pattern and held candidates, but no validated company outcome is published."},
            {"id": "analyst_operating_model", "status": "partial", "evidence": ["ANALYST-OPERATING-MODEL.md", "REFRESH-RUNBOOK.md", "operating-handoff.json", "ownership-assignment-queue.json", "refresh-continuity-audit.json", "successor-run-evidence.json", "evidence-acquisition-plan.json"], "gap": "The handoff records six roles, a reconciled ownership-assignment queue, and a reproducible read-only successor-validation artifact; named human ownership, an independently signed successor run, and sustained weekly continuity are still outstanding."},
            {"id": "validated_company_pilots", "status": "open", "evidence": ["pilot-register.json", "PILOT-VALIDATION-PROTOCOL.md", "test_internal_bridge_gate.py", "test_external_only_boundary.py"], "gap": "No pilot is approved because a company decision contract, named rights owner, internal exposure definition, and privacy review are still required after external monitoring; the fail-closed bridge and external-only release gates are exercised."},
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
