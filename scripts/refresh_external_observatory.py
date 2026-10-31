#!/usr/bin/env python3
"""Run the external observatory refresh and validation pipeline in order."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STEPS = [
    ["scripts/build_external_source_registry_snapshot.py"],
    ["scripts/build_external_repository_family_snapshot.py"],
    ["scripts/build_external_observation_manifest.py", "--git-ref", "HEAD", "--output", "analysis/external-trend-intelligence/observation-manifest.json"],
    ["scripts/build_external_family_observations.py"],
    ["scripts/build_external_family_lineage_review.py"],
    ["scripts/build_ibis_finding_claim_sample.py"],
    ["scripts/build_external_evidence_gap_queue.py"],
    ["scripts/build_external_refresh_status.py"],
    ["scripts/build_source_family_controls.py"],
    ["scripts/build_rights_review_queue.py"],
    ["scripts/build_rights_evidence_register.py"],
    ["scripts/build_room_independent_comparison.py"],
    ["scripts/build_candidate_qualification_matrix.py"],
    ["scripts/build_backtest_source_snapshot.py"],
    ["scripts/build_backtest_readiness.py"],
    ["scripts/build_backtest_comparability_review.py"],
    ["scripts/build_bounded_subset_register.py"],
    ["scripts/build_case_stage_panel.py"],
    ["scripts/build_cross_publisher_stage_panel.py"],
    ["scripts/build_cross_publisher_stage_comparison.py"],
    ["scripts/build_temporal_holdout_design.py"],
    ["scripts/build_temporal_holdout_result.py"],
    ["scripts/build_temporal_decision_narrative.py"],
    ["scripts/build_bounded_subset_lineage.py"],
    ["scripts/build_independent_stage_comparison.py"],
    ["scripts/build_release_health.py"],
    ["scripts/build_room_independent_result.py"],
    ["scripts/build_denominator_reconciliation_review.py"],
    ["scripts/build_goal_completion_audit.py"],
    ["scripts/build_external_release_manifest.py"],
    ["scripts/validate_external_trend_intelligence.py"],
    ["scripts/smoke_test_external_board.py"],
]


def main() -> int:
    for index, command in enumerate(STEPS, start=1):
        print(f"[{index}/{len(STEPS)}] {' '.join(command)}", flush=True)
        result = subprocess.run([sys.executable, *command], cwd=ROOT)
        if result.returncode:
            print(f"refresh stopped at step {index}: {command[0]}", file=sys.stderr)
            return result.returncode
    print("external observatory refresh complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
