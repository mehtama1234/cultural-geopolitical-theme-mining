#!/usr/bin/env python3
"""Build an explicit ownership queue for source-rights and lineage review."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "rights-assignment-queue.json"


def main() -> int:
    review = json.loads((ANALYSIS / "rights-review-queue.json").read_text())
    rows = []
    for item in review["rows"]:
        rows.append(
            {
                "family_id": item["family_id"],
                "primary_owner": None,
                "backup_owner": None,
                "current_status": "unassigned",
                "rights_status": item["rights_status"],
                "publisher_dependence": item["publisher_dependence"],
                "evidence": "rights-review-queue.json",
                "acceptance_criteria": [
                    "named primary rights owner recorded",
                    "named backup rights owner recorded",
                    "exact terms or license evidence reviewed",
                    "publisher and upstream dataset dependence assessed",
                    "permitted storage, transformation, and redistribution scope signed",
                ],
                "checkpoint": "before_external_trend_promotion_or_company_bridge",
            }
        )
    assigned = sum(bool(row["primary_owner"] and row["backup_owner"]) for row in rows)
    report = {
        "schema": "external-trend-intelligence.rights-assignment-queue.v1",
        "family_count": len(rows),
        "assigned_family_count": assigned,
        "unassigned_family_count": len(rows) - assigned,
        "status": "assignment_required" if assigned < len(rows) else "assigned_pending_review_signoff",
        "rows": rows,
        "next_action": "Record named primary and backup rights owners, then attach exact terms evidence and a signed reuse decision for each family.",
        "boundary": "This queue requests accountable review ownership; it does not infer identity, grant a license, or clear redistribution.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} families; {assigned} assigned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
