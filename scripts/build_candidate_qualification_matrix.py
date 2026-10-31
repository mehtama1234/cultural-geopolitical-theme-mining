#!/usr/bin/env python3
"""Build an explicit gate matrix for external trend candidates."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "candidate-qualification-matrix.json"

BACKTEST_DESIGNS = {
    "candidate-formal-response-before-recovery": {
        "status": "not_started",
        "holdout": "later case or release after the source observation period",
        "outcome": "receipt, usable recovery, durable access, and exit after formal response",
        "required_evidence": "dated comparable cases with the same response, implementation, receipt, recovery, and exit stages",
    },
    "candidate-time-financial-pressure-practical-room": {
        "status": "not_started",
        "holdout": "later survey wave or geography held out from candidate construction",
        "outcome": "time pressure, participation, substitution, or delayed completion using compatible denominators",
        "required_evidence": "at least two comparable waves or places with common unit, population, and participation measure",
    },
    "candidate-digital-capability-control-trust": {
        "status": "not_started",
        "holdout": "later attitude, adoption, or control-measure release",
        "outcome": "capability adoption alongside verification, contestability, remedy, or trust",
        "required_evidence": "repeated independent measures separating capability from control and trust",
    },
    "candidate-infrastructure-dependency-power": {
        "status": "not_started",
        "holdout": "later operating or disruption window after the candidate period",
        "outcome": "operation followed by reliability, tariff, bill, compensation, or acceptance outcome",
        "required_evidence": "dated event and outcome records linked by compatible geography and system unit",
    },
    "candidate-us-food-insecurity-persistence": {
        "status": "passed_descriptive_holdout",
        "holdout": "next USDA annual release and next Urban WBNS release, with 2025 Urban methodology break preserved",
        "outcome": "food-insecurity prevalence and subgroup persistence under clearly defined survey frames",
        "required_evidence": "same questionnaire threshold, denominator, geography, and uncertainty treatment across at least one new release",
    },
}

FALSIFIERS = {
    "candidate-formal-response-before-recovery": "If comparable cases repeatedly show usable recovery before formal response, or formal response without durable access improvement, the sequence claim is weakened.",
    "candidate-time-financial-pressure-practical-room": "If compatible repeated measures show pressure rising without reduced participation, substitution, or delayed completion, the practical-room mechanism is weakened.",
    "candidate-digital-capability-control-trust": "If capability adoption repeatedly coincides with stronger control, remedy, and trust outcomes across independent measures, the contested-control claim is weakened.",
    "candidate-infrastructure-dependency-power": "If comparable infrastructure events show no durable reliability, cost, compensation, or acceptance consequence, the dependency-to-power mechanism is weakened.",
}


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
        qualification_evidence = candidate.get("qualification_evidence", {})
        gates = {
            "source_identity": bool(candidate.get("evidence_record_ids")) and review.get("primary_artifact_count", 0) > 0,
            "comparability": qualification_evidence.get("comparability", {}).get("status") in {"compatible", "bounded"},
            "independence": qualification_evidence.get("independence", {}).get("status") == "independent",
            "persistence": qualification_evidence.get("persistence", {}).get("status") == "pass",
            "counter_signal": bool(candidate.get("counter_signal")),
            "falsifier": qualification_evidence.get("falsifier", {}).get("status") == "pass",
            "backtest": qualification_evidence.get("backtest", {}).get("status") == "pass",
            "decision_relevance": qualification_evidence.get("decision_relevance", {}).get("status") == "pass",
        }
        qualification_gate_names = ["source_identity", "comparability", "independence", "persistence", "counter_signal", "falsifier"]
        blocking = [name for name, passed in gates.items() if not passed]
        qualification_ready = all(gates[name] for name in qualification_gate_names)
        monitoring_ready = qualification_ready and gates["backtest"] and gates["decision_relevance"]
        queue_item = queue.get(candidate["id"], {})
        backtest_plan = BACKTEST_DESIGNS.get(candidate["id"], {
            "status": "not_started",
            "holdout": "later comparable release",
            "outcome": "candidate-specific outcome",
            "required_evidence": "dated repeated measure",
        })
        rows.append({
            "candidate_id": candidate["id"],
            "title": candidate["title"],
            "source_status": candidate.get("status"),
            "gate_status": "monitored_external_trend" if monitoring_ready else ("qualified_external_trend" if qualification_ready else "held"),
            "gates": gates,
            "passed_gate_count": sum(gates.values()),
            "gate_count": len(gates),
            "blocking_gates": blocking,
            "backtest_plan": backtest_plan,
            "falsifier": FALSIFIERS.get(candidate["id"], "A later comparable release that reverses the stated mechanism would falsify the candidate."),
            "evidence_record_count": coverage.get("evidence_record_count", len(candidate.get("evidence_record_ids", []))),
            "source_host_count": coverage.get("source_host_count"),
            "next_action": queue_item.get("next_action") or candidate.get("next_comparison"),
            "internal_bridge_ready": queue_item.get("internal_bridge_ready", False),
        })
    report = {
        "schema": "external-trend-intelligence.candidate-qualification-matrix.v1",
        "rubric": "trend-qualification-rubric.json",
        "candidate_count": len(rows),
        "qualified_external_trend_count": sum(row["gate_status"] in {"qualified_external_trend", "monitored_external_trend"} for row in rows),
        "monitored_external_trend_count": sum(row["gate_status"] == "monitored_external_trend" for row in rows),
        "held_count": sum(row["gate_status"] == "held" for row in rows),
        "rows": rows,
        "backtest_status_counts": {"not_started": sum(row["backtest_plan"]["status"] == "not_started" for row in rows)},
        "boundary": "This matrix is conservative: absent evidence is a failed gate, not an inferred pass. A qualified candidate is not automatically a qualified trend or an internal company finding. A backtest plan is not a backtest result.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
