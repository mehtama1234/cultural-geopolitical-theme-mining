#!/usr/bin/env python3
"""Build a release manifest for the external trend-intelligence reader surface."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "release-manifest.json"

ARTIFACTS = [
    ".github/workflows/external-observatory-refresh.yml",
    "TWO_YEAR_EXTERNAL_TREND_INTELLIGENCE_GOAL_V1.md",
    "EXTERNAL_TREND_INTELLIGENCE_GOAL_V1.md",
    "EXTERNAL_SOURCE_REGISTRY.md",
    "analysis/external-trend-intelligence/README.md",
    "analysis/external-trend-intelligence/ANALYST-OPERATING-MODEL.md",
    "analysis/external-trend-intelligence/operating-handoff.json",
    "analysis/external-trend-intelligence/successor-run-evidence.json",
    "analysis/external-trend-intelligence/operational-kpi-scorecard.json",
    "analysis/external-trend-intelligence/pilot-design-dry-run.json",
    "analysis/external-trend-intelligence/FRONTEND-INTEGRATION.md",
    "analysis/external-trend-intelligence/PILOT-VALIDATION-PROTOCOL.md",
    "analysis/external-trend-intelligence/independent-stage-comparison.json",
    "analysis/external-trend-intelligence/backtest-readiness.json",
    "analysis/external-trend-intelligence/backtest-source-snapshot.json",
    "analysis/external-trend-intelligence/backtest-comparability-review.json",
    "analysis/external-trend-intelligence/bounded-subset-register.json",
    "analysis/external-trend-intelligence/case-stage-panel.json",
    "analysis/external-trend-intelligence/cross-publisher-stage-panel.json",
    "analysis/external-trend-intelligence/cross-publisher-stage-comparison.json",
    "analysis/external-trend-intelligence/temporal-holdout-design.json",
    "analysis/external-trend-intelligence/temporal-holdout-result.json",
    "analysis/external-trend-intelligence/temporal-decision-narrative.json",
    "analysis/external-trend-intelligence/release-health.json",
    "analysis/external-trend-intelligence/bounded-subset-lineage-review.json",
    "analysis/external-trend-intelligence/program-progress.json",
    "analysis/external-trend-intelligence/program-scorecard.json",
    "analysis/external-trend-intelligence/rights-review-queue.json",
    "analysis/external-trend-intelligence/rights-evidence-register.json",
    "analysis/external-trend-intelligence/room-independent-comparison.json",
    "analysis/external-trend-intelligence/evidence-acquisition-plan.json",
    "analysis/external-trend-intelligence/goal-completion-audit.json",
    "analysis/external-trend-intelligence/room-independent-result.json",
    "analysis/external-trend-intelligence/denominator-reconciliation-review.json",
    "analysis/external-trend-intelligence/REFRESH-RUNBOOK.md",
    "analysis/external-trend-intelligence/NEXT-ACTIONS.md",
    "analysis/external-trend-intelligence/refresh-schedule.json",
    "analysis/external-trend-intelligence/refresh-schedule-health.json",
    "analysis/external-trend-intelligence/refresh-status.json",
    "analysis/external-trend-intelligence/trend-qualification-rubric.json",
    "analysis/external-trend-intelligence/source-family-registry.json",
    "analysis/external-trend-intelligence/observation-manifest.json",
    "analysis/external-trend-intelligence/source-registry-snapshot.json",
    "analysis/external-trend-intelligence/repository-family-snapshot.json",
    "analysis/external-trend-intelligence/external-family-observations.json",
    "analysis/external-trend-intelligence/evidence-contract-audit.json",
    "analysis/external-trend-intelligence/external-family-lineage-review.json",
    "analysis/external-trend-intelligence/external-evidence-gap-queue.json",
    "analysis/external-trend-intelligence/ibis-finding-claim-sample.json",
    "analysis/external-trend-intelligence/ibis-force-claim-map.json",
    "analysis/external-trend-intelligence/bls-labor-capacity-mechanism-check.json",
    "analysis/external-trend-intelligence/annual-report-citation-map.json",
    "analysis/external-trend-intelligence/social-publication-citation-map.json",
    "analysis/external-trend-intelligence/inc5000-opportunity-source-map.json",
    "analysis/external-trend-intelligence/publisher-dependence-summary.json",
    "analysis/external-trend-intelligence/trend-hunting-source-map.json",
    "analysis/external-trend-intelligence/ibis-claim-source-review.json",
    "analysis/external-trend-intelligence/ibis-claim-dependency-review.json",
    "analysis/external-trend-intelligence/ibis-adult-day-outcome-review.json",
    "analysis/external-trend-intelligence/refresh-history.json",
    "analysis/external-trend-intelligence/federal-reserve-shed-financial-room-2013-2025.json",
    "analysis/external-trend-intelligence/shed-temporal-holdout.json",
    "analysis/external-trend-intelligence/shed-emergency-expense-2013-2025.json",
    "analysis/external-trend-intelligence/shed-emergency-expense-uncertainty-audit.json",
    "analysis/external-trend-intelligence/shed-point-estimate-reproduction-audit.json",
    "analysis/external-trend-intelligence/jpmorgan-household-liquidity-chart.json",
    "analysis/external-trend-intelligence/usda-temporal-holdout.json",
    "analysis/external-trend-intelligence/food-insecurity-temporal-holdout.json",
    "analysis/external-trend-intelligence/food-insecurity-rights-review.json",
    "analysis/external-trend-intelligence/us-financial-room-independent-comparison.json",
    "analysis/external-trend-intelligence/external-acquisition-rights-review.json",
    "analysis/external-trend-intelligence/external-family-comparisons.json",
    "analysis/external-trend-intelligence/candidate-comparisons.json",
    "analysis/external-trend-intelligence/candidate-lineage-dependency-review.json",
    "analysis/external-trend-intelligence/candidate-qualification-matrix.json",
    "analysis/external-trend-intelligence/pilot-register.json",
    "analysis/external-trend-intelligence/pilot-readiness.json",
    "analysis/external-trend-intelligence/trend-monitoring-register.json",
    "analysis/external-trend-intelligence/trend-monitoring-status.json",
    "analysis/external-trend-intelligence/source-family-controls.json",
    "analysis/external-trend-intelligence/care-capacity-candidate.json",
    "analysis/external-trend-intelligence/care-capacity-measurement-matrix.json",
    "analysis/external-trend-intelligence/care-capacity-comparable-subset.json",
    "analysis/external-trend-intelligence/adaptation-control-candidate.json",
    "analysis/external-trend-intelligence/held-candidates.json",
    "analysis/external-trend-intelligence/board.html",
    "analysis/external-trend-intelligence/CROSS-SOURCE-CANDIDATES.md",
    "analysis/external-trend-intelligence/promotion-queue.json",
    "analysis/records/comparative-jpmorgan-household-liquidity-2023.json",
]


def main() -> int:
    # Keep the handoff baseline synchronized before hashing the packaged files.
    # The manifest itself is one of the packaged files, so this must happen
    # before entry hashes are computed.
    progress_path = ANALYSIS / "program-progress.json"
    if progress_path.exists():
        progress = json.loads(progress_path.read_text())
        progress["baseline"]["release_artifacts"] = len(ARTIFACTS)
        progress_path.write_text(json.dumps(progress, indent=2) + "\n")
    entries = []
    for relative in ARTIFACTS:
        path = ROOT / relative
        data = path.read_bytes()
        entries.append(
            {
                "path": relative,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    manifest = {
        "schema": "external-trend-intelligence.release-manifest.v1",
        "release_id": "external-trend-intelligence-current",
        "source_tree_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "artifact_count": len(entries),
        "artifacts": entries,
        "boundary": "This release manifest proves which local reader artifacts were packaged together. It does not prove that the underlying external sources are independent, current, licensed, or outcome-valid.",
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(entries)} artifacts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
