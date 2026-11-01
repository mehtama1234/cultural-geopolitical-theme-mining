#!/usr/bin/env python3
"""Build the candidate falsification and challenge queue."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "falsification-review-queue.json"


def main() -> int:
    matrix = json.loads((ANALYSIS / "candidate-qualification-matrix.json").read_text())
    rows = []
    for candidate in matrix["rows"]:
        rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "gate_status": candidate["gate_status"],
                "review_state": "ready_for_monitoring_challenge" if candidate["gate_status"] in {"qualified_external_trend", "monitored_external_trend"} else "held_pending_decisive_evidence",
                "blocking_gates": candidate["blocking_gates"],
                "falsifier": candidate["falsifier"],
                "next_decisive_test": candidate["next_action"],
                "backtest_plan": candidate["backtest_plan"],
            }
        )
    payload = {
        "schema": "external-trend-intelligence.falsification-review-queue.v1",
        "candidate_count": len(rows),
        "ready_for_monitoring_challenge_count": sum(row["review_state"] == "ready_for_monitoring_challenge" for row in rows),
        "held_pending_decisive_evidence_count": sum(row["review_state"] == "held_pending_decisive_evidence" for row in rows),
        "rows": rows,
        "boundary": "A falsification queue records how a claim could be weakened or reversed. It does not promote a candidate or authorize an internal test.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
