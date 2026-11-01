#!/usr/bin/env python3
"""Record whether current evidence triggers a trend reversal or retirement decision."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "trend-monitoring-evaluation.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    matrix = load("candidate-qualification-matrix.json")
    status = load("trend-monitoring-status.json")
    status_by_id = {row["candidate_id"]: row for row in status["rows"]}
    rows = []
    for candidate in matrix["rows"]:
        watch = status_by_id[candidate["candidate_id"]]
        qualified = candidate["gate_status"] == "monitored_external_trend"
        rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "current_state": watch["state"],
                "evaluation_status": "continue_watch_pending_next_comparable_release" if qualified else "not_eligible_for_reversal_decision",
                "reversal_triggered": False,
                "retirement_triggered": False,
                "evidence_basis": ["candidate-qualification-matrix.json", "trend-monitoring-register.json", "trend-monitoring-status.json"],
                "gate_snapshot": {
                    "passed_gate_count": candidate["passed_gate_count"],
                    "gate_count": candidate["gate_count"],
                    "blocking_gates": candidate["blocking_gates"],
                },
                "next_review": watch["next_review"],
                "decision_boundary": "No reversal or retirement decision is made without a new comparable release, preserved definitions, and review of counter-signals and uncertainty.",
            }
        )
    payload = {
        "schema": "external-trend-intelligence.trend-monitoring-evaluation.v1",
        "status": "monitoring_evaluated_no_reversal_triggered",
        "evaluation_count": len(rows),
        "reversal_trigger_count": sum(row["reversal_triggered"] for row in rows),
        "retirement_trigger_count": sum(row["retirement_triggered"] for row in rows),
        "rows": rows,
        "boundary": "This is a conservative control-plane evaluation. A zero trigger count means no current release has been adjudicated as a reversal; it does not prove that any trend will persist.",
        "next_action": "At each scheduled or event-triggered review, attach the new release, compare it with the pre-specified reversal conditions, and record continue, reverse, retire, or hold explicitly.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} watches evaluated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
