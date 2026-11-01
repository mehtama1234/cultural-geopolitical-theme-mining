#!/usr/bin/env python3
"""Evaluate whether source-family rights review is ready for accountable sign-off."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "rights-review-readiness.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    evidence = load("rights-evidence-register.json")
    assignment = load("rights-assignment-queue.json")
    rows = []
    for row in evidence["rows"]:
        owner = next(item for item in assignment["rows"] if item["family_id"] == row["family_id"])
        rows.append(
            {
                "family_id": row["family_id"],
                "local_evidence_status": row["evidence_status"],
                "observed_file_count": len(row["observed_files"]),
                "rights_status": row["rights_status"],
                "publisher_dependence": row["publisher_dependence"],
                "owner_status": owner["current_status"],
                "review_ready": bool(row["observed_files"] and owner["primary_owner"] and owner["backup_owner"]),
                "next_action": row["next_action"],
            }
        )
    payload = {
        "schema": "external-trend-intelligence.rights-review-readiness.v1",
        "status": "rights_review_not_ready_for_signoff" if any(not row["review_ready"] for row in rows) else "rights_review_ready_for_signoff",
        "family_count": len(rows),
        "review_ready_family_count": sum(row["review_ready"] for row in rows),
        "partial_local_evidence_count": evidence["partial_file_evidence_count"],
        "no_local_terms_file_count": evidence["no_local_terms_file_count"],
        "unassigned_owner_count": assignment["unassigned_family_count"],
        "rows": rows,
        "boundary": "This is a readiness evaluation, not a license determination. Local terms files and named owners are prerequisites for review, not proof of permission or redistribution rights.",
        "next_action": "Assign primary and backup rights owners, review exact upstream terms for each family, and record a signed storage/transformation/redistribution decision before release or company use.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({payload['review_ready_family_count']}/{payload['family_count']} families ready)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
