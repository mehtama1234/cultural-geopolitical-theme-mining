#!/usr/bin/env python3
"""Publish a concise, evidence-bound summary of current trend findings."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "trend-finding-summary.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    matrix = load("candidate-qualification-matrix.json")
    rows = []
    for candidate in matrix["rows"]:
        rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "title": candidate["title"],
                "status": "qualified_monitored" if candidate["gate_status"] == "monitored_external_trend" else "held_hypothesis",
                "passed_gate_count": candidate["passed_gate_count"],
                "gate_count": candidate["gate_count"],
                "evidence_record_count": candidate["evidence_record_count"],
                "source_host_count": candidate["source_host_count"],
                "blocking_gates": candidate["blocking_gates"],
                "falsifier": candidate["falsifier"],
                "next_action": candidate["next_action"],
                "internal_bridge_ready": candidate["internal_bridge_ready"],
            }
        )
    rows.sort(key=lambda row: (row["status"] != "qualified_monitored", row["title"]))
    payload = {
        "schema": "external-trend-intelligence.trend-finding-summary.v1",
        "as_of": date.today().isoformat(),
        "finding_count": len(rows),
        "qualified_monitored_count": sum(row["status"] == "qualified_monitored" for row in rows),
        "held_hypothesis_count": sum(row["status"] == "held_hypothesis" for row in rows),
        "findings": rows,
        "boundary": "This is a decision-facing summary of the qualification matrix. Held hypotheses are not validated trends, and no row authorizes internal company data access.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} findings)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
