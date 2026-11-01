#!/usr/bin/env python3
"""Serve the external board briefly and verify its reader artifacts are reachable."""

from __future__ import annotations

import http.server
import json
import pathlib
import subprocess
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOARD = ROOT / "analysis" / "external-trend-intelligence"
PORT = 8765
ARTIFACTS = [
    "board.html",
    "TWO-YEAR-GOAL.md",
    "EXTERNAL-DATA-SOURCES.md",
    "release-health.json",
    "refresh-status.json",
    "candidate-qualification-matrix.json",
    "backtest-readiness.json",
    "case-stage-panel.json",
    "pilot-register.json",
    "ibis-adult-day-outcome-review.json",
    "npals-public-table-extract.json",
    "source-registry-snapshot.json",
    "compatible-measure-search.json",
    "global-growth-forecast-comparison.json",
    "forecast-lineage-review.json",
    "forecast-backtest-register.json",
    "two-year-roadmap.json",
    "successor-run-evidence.json",
    "operational-kpi-scorecard.json",
    "review-calendar.json",
    "financial-room-rights-review.json",
    "rights-assignment-queue.json",
    "rights-review-readiness.json",
    "food-security-decision-brief.json",
    "food-security-release-tracker.json",
    "source-release-watchlist.json",
    "refresh-continuity-audit.json",
    "continuity-coverage-plan.json",
    "ownership-assignment-queue.json",
    "OWNERSHIP-ASSIGNMENT-REQUEST.md",
    "INDEPENDENCE-ADJUDICATION-REQUEST.md",
    "BACKTEST-DESIGN-REVIEW-REQUEST.md",
    "HOST-LINEAGE-REVIEW-REQUEST.md",
    "CONTINUITY-REVIEW-REQUEST.md",
    "census-cbp-release-check.json",
    "pilot-activation-queue.json",
    "PILOT-ACTIVATION-REQUEST.md",
    "RIGHTS-REVIEW-REQUEST.md",
    "observatory-chart-catalog.json",
    "trend-monitoring-status.json",
    "falsification-review-queue.json",
    "ibis-outcome-acquisition-queue.json",
    "ibis-community-food-outcome-linkage-review.json",
]


def main() -> int:
    proc = subprocess.Popen(
        ["python3", "-m", "http.server", str(PORT), "--bind", "127.0.0.1"],
        cwd=BOARD,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        deadline = time.time() + 5
        while True:
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/board.html", timeout=1) as response:
                    if response.status == 200:
                        board_text = response.read().decode("utf-8")
                        required_markers = [
                            "Release blockers",
                            "pipeline_status",
                            "U.S. USDA food-security temporal holdout",
                            "Falsifier:",
                            "Program scorecard",
                            "program-scorecard.json",
                            "TWO-YEAR-GOAL.md",
                            "EXTERNAL-DATA-SOURCES.md",
                            "Read the full two-year goal and operating contract",
                            "Operating handoff",
                            "operating-handoff.json",
                            "Successor validation control",
                            "successor-run-evidence.json",
                            "24-month operating KPI scorecard",
                            "operational-kpi-scorecard.json",
                            "24-month review calendar",
                            "review-calendar.json",
                            "financial-room-rights-review.json",
                            "rights-assignment-queue.json",
                            "rights-review-readiness.json",
                            "Rights review readiness",
                            "Qualified external trend brief",
                            "food-security-decision-brief.json",
                            "Publisher-reported significance",
                            "food-security-release-tracker.json",
                            "source-release-watchlist.json",
                            "refresh-continuity-audit.json",
                            "continuity-coverage-plan.json",
                            "ownership-assignment-queue.json",
                            "OWNERSHIP-ASSIGNMENT-REQUEST.md",
                            "INDEPENDENCE-ADJUDICATION-REQUEST.md",
                            "BACKTEST-DESIGN-REVIEW-REQUEST.md",
                            "HOST-LINEAGE-REVIEW-REQUEST.md",
                            "CONTINUITY-REVIEW-REQUEST.md",
                            "Pilot activation queue",
                            "pilot-activation-queue.json",
                            "PILOT-ACTIVATION-REQUEST.md",
                            "RIGHTS-REVIEW-REQUEST.md",
                            "Observatory chart catalog",
                            "observatory-chart-catalog.json",
                            "Monitoring execution status",
                            "trend-monitoring-status.json",
                            "Falsification review queue",
                            "falsification-review-queue.json",
                            "publisher-dependence-summary.json",
                            "SHED point-estimate reproduction",
                            "shed-point-estimate-reproduction-audit.json",
                            "JPMorgan household-liquidity chart",
                            "jpmorgan-household-liquidity-chart.json",
                            "candidate-lineage-dependency-review.json",
                            "Qualified food-insecurity temporal holdout",
                            "food-insecurity-temporal-holdout.json",
                            "food-insecurity-rights-review.json",
                            "IBIS bounded outcome review",
                            "ibis-adult-day-outcome-review.json",
                            "NPALS public table reconciliation",
                            "npals-public-table-extract.json",
                            "Next outcome acquisition",
                            "Registered external datasets and publishers",
                            "source-registry-snapshot.json",
                            "Concrete external data map",
                            "EXTERNAL-DATA-SOURCES.md",
                            "Compatible-measure search",
                            "compatible-measure-search.json",
                            "Global growth forecast comparison",
                            "global-growth-forecast-comparison.json",
                            "Forecast lineage review",
                            "forecast-lineage-review.json",
                            "Forecast backtest register",
                            "forecast-backtest-register.json",
                            "24-month observatory roadmap",
                            "two-year-roadmap.json",
                            "Backtest evidence readiness",
                            "pinned_git_record_path_count",
                            "IBIS sample coverage",
                            "claim_level_review",
                            "ibis-sector-chart",
                            "ibis-source-type-chart",
                            "IBIS independent-outcome acquisition queue",
                            "ibis-outcome-acquisition-queue.json",
                            "Official USDA outcome context",
                            "ibis-community-food-outcome-linkage-review.json",
                        ]
                        missing = [marker for marker in required_markers if marker not in board_text]
                        if missing:
                            raise RuntimeError(f"board.html missing required reader markers: {missing}")
                        break
            except (urllib.error.URLError, ConnectionError):
                if time.time() >= deadline:
                    raise RuntimeError("external board server did not become ready within 5 seconds")
                time.sleep(0.1)
        for artifact in ARTIFACTS:
            with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/{artifact}", timeout=5) as response:
                if response.status != 200:
                    raise RuntimeError(f"{artifact}: HTTP {response.status}")
                body = response.read()
                if artifact == "source-registry-snapshot.json":
                    snapshot = json.loads(body)
                    if snapshot.get("source_count") != 118 or len(snapshot.get("sources", [])) != 118:
                        raise RuntimeError("source-registry-snapshot.json does not expose the expected 118 sources")
                print(f"{artifact}: HTTP {response.status} ({len(body)} bytes)")
    finally:
        proc.terminate()
        proc.wait(timeout=5)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
