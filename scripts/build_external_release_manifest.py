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
    "TWO_YEAR_EXTERNAL_TREND_INTELLIGENCE_GOAL_V1.md",
    "EXTERNAL_TREND_INTELLIGENCE_GOAL_V1.md",
    "EXTERNAL_SOURCE_REGISTRY.md",
    "analysis/external-trend-intelligence/README.md",
    "analysis/external-trend-intelligence/REFRESH-RUNBOOK.md",
    "analysis/external-trend-intelligence/NEXT-ACTIONS.md",
    "analysis/external-trend-intelligence/refresh-schedule.json",
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
    "analysis/external-trend-intelligence/external-family-comparisons.json",
    "analysis/external-trend-intelligence/candidate-comparisons.json",
    "analysis/external-trend-intelligence/candidate-qualification-matrix.json",
    "analysis/external-trend-intelligence/pilot-register.json",
    "analysis/external-trend-intelligence/care-capacity-candidate.json",
    "analysis/external-trend-intelligence/care-capacity-measurement-matrix.json",
    "analysis/external-trend-intelligence/care-capacity-comparable-subset.json",
    "analysis/external-trend-intelligence/adaptation-control-candidate.json",
    "analysis/external-trend-intelligence/held-candidates.json",
    "analysis/external-trend-intelligence/board.html",
    "analysis/external-trend-intelligence/CROSS-SOURCE-CANDIDATES.md",
    "analysis/external-trend-intelligence/promotion-queue.json",
]


def main() -> int:
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
