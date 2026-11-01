#!/usr/bin/env python3
"""Turn refresh-status telemetry into explicit freshness actions by source family."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "refresh-freshness-decision.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    status = load("refresh-status.json")
    rows = []
    for family in status["families"]:
        if family["missing_artifacts"]:
            decision = "unavailable_missing_artifact"
            action = "Restore or reacquire the missing artifact before using this family in comparison or publication."
        elif family["stale"]:
            decision = "stale_hold"
            action = "Run the family-specific refresh or document an approved exception before promotion."
        elif family["status"] == "incomplete":
            decision = "incomplete_hold"
            action = "Resolve the incomplete refresh state and retain diagnostics before downstream use."
        else:
            decision = "fresh_ready_for_review"
            action = "Proceed to lineage, rights, independence, and qualification review; freshness alone is not validity."
        rows.append(
            {
                "family_id": family["family_id"],
                "decision": decision,
                "status": family["status"],
                "stale": family["stale"],
                "missing_artifacts": family["missing_artifacts"],
                "stale_threshold_hours": family["stale_threshold_hours"],
                "artifacts": family["artifacts"],
                "action": action,
            }
        )
    payload = {
        "schema": "external-trend-intelligence.refresh-freshness-decision.v1",
        "generated_at": status["generated_at"],
        "family_count": len(rows),
        "fresh_ready_count": sum(row["decision"] == "fresh_ready_for_review" for row in rows),
        "hold_count": sum(row["decision"] != "fresh_ready_for_review" for row in rows),
        "rows": rows,
        "boundary": "Freshness decisions are file-age and artifact-availability controls. They do not prove source reachability, rights, publisher independence, comparability, or trend validity.",
        "next_action": "Route every stale, unavailable, or incomplete family to its acquisition and lineage owner before using it in a published comparison or company decision contract.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({payload['fresh_ready_count']} ready; {payload['hold_count']} held)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
