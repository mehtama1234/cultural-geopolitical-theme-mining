#!/usr/bin/env python3
"""Build the 24-month operating review calendar from current phase evidence."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "review-calendar.json"


def main() -> int:
    scorecard = json.loads((ANALYSIS / "program-scorecard.json").read_text())
    phases = scorecard["phases"]
    checkpoints = [
        {"month": 1, "cadence": "monthly", "phase": "months_0_3_control_plane", "review": "source registry, evidence contract, and rights queue", "owner": "source steward"},
        {"month": 3, "cadence": "quarterly", "phase": "months_0_3_control_plane", "review": "control-plane exit review and release-manifest audit", "owner": "release owner"},
        {"month": 6, "cadence": "quarterly", "phase": "months_4_6_dependable_external_intake", "review": "refresh SLA, stale recovery, record metadata, lineage, and rights evidence", "owner": "release owner"},
        {"month": 9, "cadence": "monthly", "phase": "months_7_12_trend_qualification", "review": "candidate challenge, falsification, and shared-host dependence queue", "owner": "trend challenger"},
        {"month": 12, "cadence": "quarterly", "phase": "months_7_12_trend_qualification", "review": "qualification, holdout, reversal, and monitoring review", "owner": "trend challenger"},
        {"month": 15, "cadence": "monthly", "phase": "months_13_18_decision_relevance", "review": "design-only pilot contract and external gate review", "owner": "decision translator"},
        {"month": 18, "cadence": "quarterly", "phase": "months_13_18_decision_relevance", "review": "pilot authorization review; no internal join before approval", "owner": "release owner"},
        {"month": 21, "cadence": "monthly", "phase": "months_19_24_operational_handoff", "review": "successor validation and ownership assignment", "owner": "release owner"},
        {"month": 24, "cadence": "quarterly", "phase": "months_19_24_operational_handoff", "review": "two-year outcome, reversal rate, pilot usefulness, and handoff", "owner": "program owner"},
    ]
    phase_by_id = {phase["phase"]: phase for phase in phases}
    for checkpoint in checkpoints:
        checkpoint["phase_status"] = phase_by_id[checkpoint["phase"]]["status"]
        checkpoint["evidence"] = phase_by_id[checkpoint["phase"]]["exit_evidence"]
    next(e for e in checkpoints if e["month"] == 6)["evidence"] += ["record-quality-audit.json", "record-quality-remediation-queue.json"]
    next(e for e in checkpoints if e["month"] == 9)["evidence"] += ["record-host-dependence-audit.json", "host-dependence-review-queue.json"]
    payload = {
        "schema": "external-trend-intelligence.review-calendar.v1",
        "as_of": date.today().isoformat(),
        "horizon_months": 24,
        "checkpoint_count": len(checkpoints),
        "checkpoints": checkpoints,
        "boundary": "This calendar schedules review and ownership work. It does not imply that a phase has passed its gates or that company pilots are authorized.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(checkpoints)} checkpoints)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
