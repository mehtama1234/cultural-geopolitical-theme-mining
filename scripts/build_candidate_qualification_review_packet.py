#!/usr/bin/env python3
"""Build a signable qualification and backtest packet for every trend candidate."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "candidate-qualification-review-packet.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    matrix = {row["candidate_id"]: row for row in load("candidate-qualification-matrix.json")["rows"]}
    independence = {row["candidate_id"]: row for row in load("candidate-independence-adjudication-queue.json")["rows"]}
    backtest = {row["candidate_id"]: row for row in load("backtest-readiness.json")["rows"]}
    comparability = {row["candidate_id"]: row for row in load("backtest-comparability-review.json")["rows"]}
    falsification = {row["candidate_id"]: row for row in load("falsification-review-queue.json")["rows"]}
    rows = []
    for candidate_id, candidate in matrix.items():
        ind = independence[candidate_id]
        bt = backtest[candidate_id]
        comp = comparability[candidate_id]
        fals = falsification[candidate_id]
        rows.append({
            "candidate_id": candidate_id,
            "title": candidate["title"],
            "current_state": candidate["gate_status"],
            "priority": ind["priority"],
            "gate_statuses": candidate["gates"],
            "blocking_gates": candidate["blocking_gates"],
            "independence_review": {
                "status": ind["review_status"],
                "unassigned": ind["assignee"] is None,
                "unresolved_record_ids": ind["unresolved_record_ids"],
                "dependency_groups": ind["dependency_groups"],
                "required_evidence": ind["required_evidence"],
                "stop_rule": ind["stop_rule"],
            },
            "backtest_review": {
                "status": bt["status"],
                "record_count": bt["evidence_record_count"],
                "pinned_git_record_path_count": bt["pinned_git_record_path_count"],
                "comparability_status": comp["status"],
                "comparable_subset": comp.get("comparable_subset", []),
                "harmonization_required": comp.get("harmonization_required", []),
                "next_action": comp.get("next_action", candidate["next_action"]),
            },
            "falsification": {
                "falsifier": fals["falsifier"],
                "next_decisive_test": fals["next_decisive_test"],
                "backtest_plan": fals["backtest_plan"],
            },
            "required_decision_fields": [
                "target state: held, qualified, monitored, or reversed",
                "evidence for every required rubric gate",
                "independence disposition for every comparator",
                "compatible unit, denominator, population, geography, and period",
                "holdout outcome and uncertainty treatment",
                "counter-signal and falsifier result",
                "reviewer and second-reviewer acknowledgement",
                "effective date and next review date",
            ],
            "decision_options": ["retain_held", "promote_to_qualified", "promote_to_monitored", "reverse_or_retire"],
            "signoff": {"trend_challenger": None, "lineage_reviewer": None, "second_reviewer": None, "reviewed_on": None},
        })
    payload = {
        "schema": "external-trend-intelligence.candidate-qualification-review-packet.v1",
        "status": "ready_for_human_qualification_signoff",
        "candidate_count": len(rows),
        "unassigned_candidate_count": sum(row["independence_review"]["unassigned"] for row in rows),
        "rows": rows,
        "acceptance_criteria": [
            "Every candidate has a recorded disposition for each required qualification gate.",
            "Independence, comparability, backtest, and falsification evidence are reviewed before promotion.",
            "Held candidates remain held when evidence is missing, incompatible, or rights-limited.",
            "No candidate is promoted to monitored or bridged to company data from this packet alone.",
        ],
        "next_action": "Assign a trend challenger and lineage reviewer, complete one row per candidate, and write the signed disposition back to candidate-qualification-matrix.json and the adjudication queue.",
        "boundary": "This packet makes qualification review executable; it is not a trend promotion, causal finding, forecast, or company authorization.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates; {payload['unassigned_candidate_count']} unassigned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
