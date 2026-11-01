#!/usr/bin/env python3
"""Build a signable independence and lineage packet for every candidate."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "candidate-independence-review-packet.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    queue = load("candidate-independence-adjudication-queue.json")
    rows = []
    for item in queue["rows"]:
        rows.append({
            "candidate_id": item["candidate_id"],
            "title": item["title"],
            "priority": item["priority"],
            "review_status": item["review_status"],
            "assignee": item["assignee"],
            "unresolved_record_ids": item["unresolved_record_ids"],
            "publisher_or_dataset_candidates": item["publisher_or_dataset_candidates"],
            "dependency_groups": item["dependency_groups"],
            "required_evidence": item["required_evidence"],
            "first_review_action": item["first_review_action"],
            "evidence_artifacts": item["review_evidence_artifacts"],
            "decision_options": ["independent", "dependent_restatement", "same_artifact", "noncomparable_directional_challenge", "hold_pending_evidence"],
            "required_decision_fields": [
                "canonical publisher and exact artifact",
                "underlying dataset or event",
                "population, geography, period, unit, and denominator",
                "shared publisher, URL, host, dataset, and restatement dependence",
                "rights and downstream redistribution boundary",
                "candidate-level disposition and rationale",
                "reviewer, second reviewer, and effective date",
            ],
            "stop_rule": item["stop_rule"],
            "signoff": {"lineage_reviewer": None, "second_reviewer": None, "reviewed_on": None, "disposition": None},
        })
    payload = {
        "schema": "external-trend-intelligence.candidate-independence-review-packet.v1",
        "status": "ready_for_human_independence_signoff",
        "candidate_count": len(rows),
        "unassigned_candidate_count": sum(row["assignee"] is None for row in rows),
        "rows": rows,
        "acceptance_criteria": [
            "Every comparator is assigned an explicit independence, dependence, or non-comparability disposition.",
            "Canonical publisher, artifact, underlying dataset, unit, period, and rights evidence are attached.",
            "Shared hosts and restatements are not counted as independent confirmation.",
            "Unresolved candidates remain blocked from qualification and company use.",
        ],
        "next_action": "Assign a lineage reviewer and second reviewer, complete one row per candidate, and write the signed disposition back to candidate-independence-adjudication-queue.json.",
        "boundary": "This packet makes independence review executable; it is not an adjudication, rights clearance, trend promotion, or company authorization.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates; {payload['unassigned_candidate_count']} unassigned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
