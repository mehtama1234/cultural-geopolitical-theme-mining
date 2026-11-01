#!/usr/bin/env python3
"""Build a signable packet for the eight source-family rights reviews."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "source-family-rights-review-packet.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    queue = load("rights-assignment-queue.json")
    review = {row["family_id"]: row for row in load("rights-review-queue.json")["rows"]}
    evidence = {row["family_id"]: row for row in load("rights-evidence-register.json")["rows"]}
    rows = []
    for item in queue["rows"]:
        plan = review[item["family_id"]]["review_plan"]
        evidence_row = evidence[item["family_id"]]
        rows.append({
            "family_id": item["family_id"],
            "current_status": item["current_status"],
            "rights_status": item["rights_status"],
            "publisher_dependence": item["publisher_dependence"],
            "primary_owner": item["primary_owner"],
            "backup_owner": item["backup_owner"],
            "first_30_day_action": item["first_30_day_action"],
            "first_artifact": plan["first_artifact"],
            "observed_local_terms": evidence_row["observed_files"],
            "rights_questions": plan["rights_questions"],
            "lineage_questions": plan["lineage_questions"],
            "required_decision_fields": [
                "exact terms or license locator",
                "publisher and upstream identity",
                "storage scope",
                "transformation scope",
                "redistribution or derived-chart scope",
                "retention/deletion obligation",
                "publisher-dependence disposition",
                "reviewer and effective date",
            ],
            "decision_options": ["clear_with_scope", "retain_internal_review_only", "hold_pending_evidence", "retire_source"],
            "stop_rule": item["stop_rule"],
            "signoff": {"rights_reviewer": None, "lineage_reviewer": None, "release_owner": None, "reviewed_on": None},
        })
    payload = {
        "schema": "external-trend-intelligence.source-family-rights-review-packet.v1",
        "status": "ready_for_human_rights_signoff",
        "family_count": len(rows),
        "assigned_family_count": queue["assigned_family_count"],
        "rows": rows,
        "acceptance_criteria": [
            "Every family has a named primary and backup owner.",
            "Exact terms evidence and upstream identity are attached.",
            "Storage, transformation, redistribution, retention, and dependence decisions are signed.",
            "Unresolved families remain blocked from public redistribution, trend promotion, and company use.",
        ],
        "next_action": "Assign owners, complete one row per family, and write the signed disposition back to rights-assignment-queue.json and rights-review-readiness.json.",
        "boundary": "This packet makes rights review executable; it is not a license grant or legal clearance.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} families; {queue['assigned_family_count']} assigned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
