#!/usr/bin/env python3
"""Audit uncertainty preservation across decision-facing observatory artifacts."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "uncertainty-coverage-audit.json"


def main() -> int:
    ibis = json.loads((ANALYSIS / "ibis-adult-day-outcome-review.json").read_text())
    ibis_observations = ibis["observations"]
    recorded_count = sum(bool(item.get("uncertainty")) for item in ibis_observations)
    standard_error_count = sum(item.get("standard_error") is not None for item in ibis_observations)
    rows = [
        {
            "artifact": "ibis-adult-day-outcome-review.json",
            "uncertainty_state": "source_level_uncertainty_recorded",
            "evidence": f"{recorded_count}/{len(ibis_observations)} observations carry uncertainty notes; {standard_error_count} carry standard errors.",
            "release_implication": "retain source-specific uncertainty and do not pool unlike CDC and CMS measures",
        },
        {
            "artifact": "food-insecurity-temporal-holdout.json",
            "uncertainty_state": "explicitly_incomplete",
            "evidence": "USDA significance caveat is retained, but comparable Urban interval estimates are not present in the retained artifact.",
            "release_implication": "monitoring only; no pooled estimate or causal claim",
        },
        {
            "artifact": "food-insecurity-independent-comparison.json",
            "uncertainty_state": "explicitly_incomplete",
            "evidence": "USDA non-significance is recorded; Urban uncertainty and a harmonized interval are unavailable.",
            "release_implication": "directional challenge only; do not pool",
        },
        {
            "artifact": "mobility-access-independent-comparison.json",
            "uncertainty_state": "not_reported_by_source_in_retained_summary",
            "evidence": "ACS and NHTS income-gradient values are retained with frame and weighting boundaries, but margins of error are not in the comparison artifact.",
            "release_implication": "directional challenge only; acquire source-specific uncertainty before a holdout",
        },
        {
            "artifact": "global-growth-forecast-comparison.json",
            "uncertainty_state": "not_carried",
            "evidence": "Forecast values and spreads are retained, but publisher intervals or scenario ranges are not carried.",
            "release_implication": "scenario context only; forecast backtest remains pending",
        },
        {
            "artifact": "forecast-backtest-register.json",
            "uncertainty_state": "reserved_pending_outcome",
            "evidence": "Forecast and outcome uncertainty fields are reserved in acceptance criteria; no realized outcome is available yet.",
            "release_implication": "no forecast accuracy claim",
        },
    ]
    report = {
        "schema": "external-trend-intelligence.uncertainty-coverage-audit.v1",
        "artifact_count": len(rows),
        "rows": rows,
        "recorded_or_explicit_count": sum(row["uncertainty_state"] != "missing" for row in rows),
        "complete_source_level_count": sum(row["uncertainty_state"] == "source_level_uncertainty_recorded" for row in rows),
        "incomplete_or_pending_count": sum(row["uncertainty_state"] != "source_level_uncertainty_recorded" for row in rows),
        "status": "uncertainty_visible_with_open_gates",
        "next_action": "Acquire source-level intervals or standard errors for the food and mobility comparisons and publisher forecast ranges before promotion or company use.",
        "boundary": "Presence of an uncertainty note is not proof of statistical validity. Missing, unavailable, and pending uncertainty remain visible and keep the affected artifact bounded.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} artifacts; {report['complete_source_level_count']} complete source-level rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
