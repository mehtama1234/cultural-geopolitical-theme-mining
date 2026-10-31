#!/usr/bin/env python3
"""Build the operational control register for every external source family."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "source-family-controls.json"


def main() -> int:
    registry = json.loads((ANALYSIS / "source-family-registry.json").read_text())
    schedule = json.loads((ANALYSIS / "refresh-schedule.json").read_text())
    schedule_by_id = {item["family_id"]: item for item in schedule["families"]}
    families = []
    for family in registry["source_families"]:
        item = schedule_by_id[family["id"]]
        families.append({
            "family_id": family["id"],
            "repository": family.get("repository"),
            "revision": family.get("revision", "working-tree-or-local-source"),
            "role": family["role"],
            "owner": "external evidence review queue",
            "cadence": item["cadence"],
            "trigger": item["trigger"],
            "access_basis": "pinned repository revision or local source artifact",
            "rights_status": "not_yet_verified",
            "publisher_dependence": "review_required",
            "lineage_status": "pinned_revision" if family.get("revision") else "local_source_requires_pin",
            "observation_requirements": ["unit", "denominator_or_scope", "geography", "observation_period", "uncertainty", "counter_signal", "source_locator"],
            "evidence_boundary": family["evidence_boundary"],
            "status": family["status"],
        })
    report = {
        "schema": "external-trend-intelligence.source-family-controls.v1",
        "registry": "source-family-registry.json",
        "schedule": "refresh-schedule.json",
        "family_count": len(families),
        "families": families,
        "boundary": "Control fields preserve what must be reviewed. 'not_yet_verified' and 'review_required' do not establish rights, independence, or current availability.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(families)} families)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
