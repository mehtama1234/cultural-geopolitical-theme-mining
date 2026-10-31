#!/usr/bin/env python3
"""Build the source rights and publisher-dependence review queue."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "rights-review-queue.json"


def main() -> int:
    controls = json.loads((ANALYSIS / "source-family-controls.json").read_text())
    rows = []
    for family in controls["families"]:
        rows.append({
            "family_id": family["family_id"],
            "status": "review_required",
            "rights_status": family["rights_status"],
            "publisher_dependence": family["publisher_dependence"],
            "evidence_required": [
                "access route and terms or license basis",
                "permitted storage, transformation, and redistribution scope",
                "publisher and upstream dataset identity",
                "shared-publisher/shared-dataset dependence assessment",
                "retention and refresh obligation",
            ],
            "stop_rule": "Do not promote a trend or connect internal data while rights basis or publisher dependence remains unresolved.",
            "owner": family["owner"],
        })
    report = {
        "schema": "external-trend-intelligence.rights-review-queue.v1",
        "family_count": len(rows),
        "review_required_count": sum(row["status"] == "review_required" for row in rows),
        "rows": rows,
        "boundary": "This queue identifies evidence needed for clearance; it is not a legal determination or a claim that any source is licensed.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} families)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
