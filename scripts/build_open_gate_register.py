#!/usr/bin/env python3
"""Build one conservative register of unresolved observatory gates."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "open-gate-register.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    rights = load("rights-assignment-queue.json")
    independence = load("candidate-independence-adjudication-queue.json")
    host_queue = load("host-dependence-review-queue.json")
    qualification = load("candidate-qualification-matrix.json")
    backtest = load("backtest-readiness.json")
    forecast = load("forecast-backtest-register.json")
    pilots = load("pilot-readiness.json")
    ownership = load("ownership-assignment-queue.json")
    continuity = load("refresh-continuity-audit.json")
    gates = [
        {
            "gate_id": "source_family_rights",
            "priority": "critical",
            "open_count": rights["unassigned_family_count"],
            "owner": "source governance",
            "status": rights["status"],
            "evidence": "rights-assignment-queue.json",
            "acceptance": "Named primary and backup owners, exact terms evidence, and signed storage/transformation/redistribution decision for every family.",
        },
        {
            "gate_id": "candidate_independence_adjudication",
            "priority": "high",
            "open_count": independence["unassigned_count"],
            "owner": "lineage reviewer",
            "status": independence["status"],
            "evidence": "candidate-independence-adjudication-queue.json",
            "acceptance": "Artifact-level publisher, upstream, unit, period, and independence disposition for every candidate.",
        },
        {
            "gate_id": "shared_host_lineage",
            "priority": "high",
            "open_count": host_queue["unassigned_count"],
            "owner": "lineage reviewer",
            "status": host_queue["status"],
            "evidence": "host-dependence-review-queue.json",
            "acceptance": "Publisher and upstream identity, rights route, and restatement/independence disposition for each prioritized host.",
        },
        {
            "gate_id": "trend_qualification",
            "priority": "high",
            "open_count": qualification["held_count"],
            "owner": "trend challenger",
            "status": "held_candidates_present",
            "evidence": "candidate-qualification-matrix.json",
            "acceptance": "All eight qualification gates passed or the candidate is explicitly retired; no inferred passes.",
        },
        {
            "gate_id": "candidate_backtest_design",
            "priority": "high",
            "open_count": backtest["candidate_count"],
            "owner": "trend challenger",
            "status": "design_review_required",
            "evidence": "backtest-readiness.json",
            "acceptance": "Compatible construction and holdout periods, units, outcomes, uncertainty, and falsifier reviewed per candidate.",
        },
        {
            "gate_id": "forecast_realized_outcomes",
            "priority": "normal",
            "open_count": forecast["pending_count"],
            "owner": "evidence analyst",
            "status": "awaiting_realized_outcome",
            "evidence": "forecast-backtest-register.json",
            "acceptance": "First comparable official realized outcome with vintage, definition, uncertainty, and retained forecast error.",
        },
        {
            "gate_id": "company_pilot_readiness",
            "priority": "critical",
            "open_count": pilots["blocked_external_first_count"],
            "owner": "decision translator",
            "status": "blocked_external_first",
            "evidence": "pilot-readiness.json",
            "acceptance": "Rights, named company decision contract, privacy/lawful access, internal crosswalk, and preregistration pass before any bridge.",
        },
        {
            "gate_id": "operating_ownership",
            "priority": "critical",
            "open_count": ownership["unassigned_role_count"],
            "owner": "program sponsor",
            "status": ownership["status"],
            "evidence": "ownership-assignment-queue.json",
            "acceptance": "Named primary/backup, acknowledgement, conflict declaration, and independently reviewable handoff for every role.",
        },
        {
            "gate_id": "two_year_continuity",
            "priority": "normal",
            "open_count": max(continuity["required_two_year_weeks"] - continuity["observed_distinct_week_count"], 0),
            "owner": "release owner",
            "status": continuity["unattended_two_year_coverage"],
            "evidence": "refresh-continuity-audit.json",
            "acceptance": "104 distinct weekly windows with passed runs and recovery evidence.",
        },
    ]
    payload = {
        "schema": "external-trend-intelligence.open-gate-register.v1",
        "status": "open_gates_consolidated",
        "gate_count": len(gates),
        "critical_gate_count": sum(gate["priority"] == "critical" for gate in gates),
        "total_open_work_items": sum(gate["open_count"] for gate in gates),
        "gates": gates,
        "boundary": "This register consolidates work queues; it does not close a gate, infer ownership, grant rights, qualify a trend, or authorize a company bridge.",
        "next_action": "Work critical gates first, then high-priority independence and backtest gates; re-run the register after every evidence or ownership decision.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(gates)} gates; {payload['total_open_work_items']} open work items)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
