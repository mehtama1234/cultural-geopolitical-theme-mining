#!/usr/bin/env python3
"""Turn candidate dependency findings into an explicit independence-review queue."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "candidate-independence-adjudication-queue.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    dependency = load("candidate-lineage-dependency-review.json")
    comparisons = {row["id"]: row for row in load("candidate-comparisons.json")["candidates"]}
    rows = []
    for item in dependency["rows"]:
        candidate = comparisons[item["candidate_id"]]
        unresolved = item["unclassified_record_ids"]
        row = {
            "candidate_id": item["candidate_id"],
            "title": candidate["title"],
            "priority": "high" if item["dependency_group_count"] or len(unresolved) >= 5 else "standard",
            "review_status": "pending_manual_adjudication",
            "publisher_or_dataset_candidates": candidate["coverage"].get("source_host_counts", {}),
            "dependency_group_count": item["dependency_group_count"],
            "dependency_groups": item["dependency_groups"],
            "unresolved_record_ids": unresolved,
            "required_evidence": [
                "canonical publisher and source-family identity",
                "underlying dataset or event, not only a summary or citation",
                "population, geography, period, unit, denominator, and outcome",
                "method overlap or non-overlap with every comparator",
                "rights and redistribution boundary for the exact artifact",
                "explicit reason the comparison is independent, dependent, or non-comparable",
            ],
            "stop_rule": "Do not count the candidate as independently confirmed when any comparator lacks canonical publisher, underlying dataset, compatible unit, or rights evidence.",
            "assignee": None,
            "due_date": None,
            "disposition": "pending",
            "next_action": item["next_test"],
            "first_review_action": (
                "Resolve every unresolved record to a canonical publisher, exact artifact, "
                "underlying dataset/event, population, period, unit, denominator, outcome, and rights boundary; "
                "then classify each dependency before deciding the candidate disposition."
            ),
            "review_evidence_artifacts": [
                "candidate-lineage-dependency-review.json",
                "observation-manifest.json",
                "rights-review-queue.json",
                "publisher-dependence-summary.json",
            ],
            "required_signoff": [
                "reviewer acknowledgement",
                "second-reviewer check",
                "explicit disposition for every unresolved record",
                "candidate-level disposition recorded without promotion",
            ],
        }
        if item["candidate_id"] == "candidate-us-food-insecurity-persistence":
            row["review_packet"] = "food-security-independence-review-packet.json"
            row["next_action"] = "Complete food-security-independence-review-packet.json, then write the signed disposition back to this row."
        rows.append(row)
    payload = {
        "schema": "external-trend-intelligence.candidate-independence-adjudication-queue.v1",
        "status": "manual_adjudication_queue_ready",
        "candidate_count": len(rows),
        "high_priority_count": sum(row["priority"] == "high" for row in rows),
        "unassigned_count": sum(row["assignee"] is None for row in rows),
        "rows": rows,
        "boundary": "This queue operationalizes independence review; distinct hosts or URLs are not treated as independent confirmation without adjudication.",
        "next_action": "Assign a reviewer to each candidate, resolve the required evidence, and record an explicit disposition before any qualification or company bridge.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates; {payload['high_priority_count']} high priority)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
