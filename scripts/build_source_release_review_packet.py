#!/usr/bin/env python3
"""Build a signable next-release review packet for acquired external sources."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "source-release-review-packet.json"


def main() -> int:
    watchlist = json.loads((ANALYSIS / "source-release-watchlist.json").read_text())
    register = {row["source_id"]: row for row in json.loads((ANALYSIS / "acquired-source-register.json").read_text())["sources"]}
    rows = []
    for item in watchlist["rows"]:
        source = register[item["source_id"]]
        rows.append({
            "source_id": item["source_id"],
            "publisher": item["publisher"],
            "artifact": item["artifact"],
            "current_status": item["status"],
            "latest_observation_period": item["latest_observation_period"],
            "next_target_period": item["next_target_period"],
            "cadence_or_trigger": item["cadence_or_trigger"],
            "acquisition_action": item["acquisition_action"],
            "current_checksum": source["checksum"],
            "current_rights_boundary": source["rights_boundary"],
            "current_lineage": {"publisher_dependence": source["publisher_dependence"], "population_and_unit": source["population_and_unit"], "geography_and_period": source["geography_and_period"]},
            "decision_options": ["acquire_and_replace", "retain_current_artifact", "hold_pending_rights_or_method_review", "retire_watch_target"],
            "required_decision_fields": [
                "official release URL or locator",
                "release period and revision",
                "retrieval timestamp and checksum",
                "population, unit, geography, and period comparison",
                "method and definition break assessment",
                "rights and terms evidence",
                "publisher/upstream dependence disposition",
                "owner, decision, and next review date",
            ],
            "signoff": {"source_steward": None, "lineage_reviewer": None, "rights_reviewer": None, "decision": None, "reviewed_on": None},
        })
    payload = {
        "schema": "external-trend-intelligence.source-release-review-packet.v1",
        "status": "ready_for_source_steward_review",
        "source_count": len(rows),
        "rows": rows,
        "acceptance_criteria": [
            "Every acquired source has a next-release decision and retained current checksum.",
            "New releases are not substituted when a method, definition, rights, or lineage break is unresolved.",
            "Unavailable releases remain unavailable rather than being converted to zero or silently dropped.",
            "A release decision updates the watchlist and acquired-source register together.",
        ],
        "next_action": "Assign a source steward and lineage reviewer, complete one row per source at each scheduled release check, and update the watchlist only after evidence is retained.",
        "boundary": "This packet makes release monitoring executable; it is not proof of freshness, rights clearance, comparability, or trend qualification.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} sources)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
