#!/usr/bin/env python3
"""Build an explicit gate matrix for external trend candidates."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "candidate-qualification-matrix.json"


def main() -> int:
    candidates = json.loads((ANALYSIS / "candidate-comparisons.json").read_text())["candidates"]
    queue = {
        item["candidate_id"]: item
        for item in json.loads((ANALYSIS / "promotion-queue.json").read_text())["candidates"]
    }
    rows = []
    for candidate in candidates:
        review = candidate.get("lineage_review", {})
        coverage = candidate.get("coverage", {})
        gates = {
            "source_identity": bool(candidate.get("evidence_record_ids")) and review.get("primary_artifact_count", 0) > 0,
            "comparability": False,
            "independence": review.get("independence_status") == "independent",
            "persistence": False,
            "counter_signal": bool(candidate.get("counter_signal")),
            "falsifier": False,
            "backtest": False,
            "decision_relevance": False,
        }
        blocking = [name for name, passed in gates.items() if not passed]
        queue_item = queue.get(candidate["id"], {})
        rows.append({
            "candidate_id": candidate["id"],
            "title": candidate["title"],
            "source_status": candidate.get("status"),
            "gate_status": "qualified_external_trend" if not blocking else "held",
            "gates": gates,
            "passed_gate_count": sum(gates.values()),
            "gate_count": len(gates),
            "blocking_gates": blocking,
            "evidence_record_count": coverage.get("evidence_record_count", len(candidate.get("evidence_record_ids", []))),
            "source_host_count": coverage.get("source_host_count"),
            "next_action": queue_item.get("next_action") or candidate.get("next_comparison"),
            "internal_bridge_ready": queue_item.get("internal_bridge_ready", False),
        })
    report = {
        "schema": "external-trend-intelligence.candidate-qualification-matrix.v1",
        "rubric": "trend-qualification-rubric.json",
        "candidate_count": len(rows),
        "qualified_external_trend_count": sum(row["gate_status"] == "qualified_external_trend" for row in rows),
        "held_count": sum(row["gate_status"] == "held" for row in rows),
        "rows": rows,
        "boundary": "This matrix is conservative: absent evidence is a failed gate, not an inferred pass. A qualified candidate is not automatically a qualified trend or an internal company finding.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
