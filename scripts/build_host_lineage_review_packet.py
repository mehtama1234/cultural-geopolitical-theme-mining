#!/usr/bin/env python3
"""Build a signable shared-host lineage and publisher-dependence packet."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "host-lineage-review-packet.json"


def main() -> int:
    queue = json.loads((ANALYSIS / "host-dependence-review-queue.json").read_text())
    rows = []
    for item in queue["rows"]:
        rows.append({
            "review_id": item["review_id"],
            "host": item["host"],
            "priority": item["priority"],
            "record_count": item["record_count"],
            "theme_count": item["theme_count"],
            "current_status": item["status"],
            "review_questions": item["review_questions"],
            "required_evidence": item["required_evidence"],
            "first_30_day_action": item["first_30_day_action"],
            "acceptance": item["acceptance"],
            "required_signoff": item["required_signoff"],
            "decision_options": ["independent_publisher_family", "shared_upstream_restatement", "same_artifact_cluster", "noncomparable_context_only", "hold_pending_rights_or_identity"],
            "required_decision_fields": [
                "canonical publisher identity",
                "upstream dataset, report, or synthesis identity",
                "URL and artifact cluster mapping",
                "distinct outcome versus restatement assessment",
                "rights route and restrictions",
                "independence disposition and rationale",
                "lineage reviewer and second-reviewer signoff",
                "effective date and next review date",
            ],
            "signoff": {"lineage_reviewer": None, "rights_reviewer": None, "second_reviewer": None, "disposition": None, "reviewed_on": None},
            "stop_rule": item["stop_rule"],
        })
    payload = {
        "schema": "external-trend-intelligence.host-lineage-review-packet.v1",
        "status": "ready_for_host_lineage_signoff",
        "row_limit": queue["row_limit"],
        "unique_host_count": queue["unique_host_count"],
        "shared_host_count": queue["shared_host_count"],
        "review_count": len(rows),
        "high_priority_count": sum(row["priority"] == "high" for row in rows),
        "rows": rows,
        "acceptance_criteria": [
            "Every prioritized shared host has canonical publisher and upstream identity.",
            "Shared URLs, datasets, and restatements are classified before repetition is counted as independent evidence.",
            "Rights route and downstream chart restrictions are recorded.",
            "Unresolved hosts remain blocked from independence claims and promotion.",
        ],
        "next_action": "Assign lineage and rights reviewers, complete the highest-priority host rows first, and write dispositions back to host-dependence-review-queue.json.",
        "boundary": "This packet makes shared-host review executable; it is not an independence finding, rights clearance, or trend promotion.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} hosts; {payload['high_priority_count']} high priority)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
