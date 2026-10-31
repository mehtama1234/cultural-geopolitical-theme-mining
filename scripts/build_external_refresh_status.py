#!/usr/bin/env python3
"""Build a visible, evidence-backed refresh status report for source families."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "refresh-status.json"


def main() -> int:
    schedule = json.loads((ANALYSIS / "refresh-schedule.json").read_text())
    registry = json.loads((ANALYSIS / "source-family-registry.json").read_text())
    registered = {family["id"] for family in registry["source_families"]}
    now = datetime.now(timezone.utc)
    families = []
    for item in schedule["families"]:
        family_id = item["family_id"]
        artifacts = []
        for relative in item["refresh_artifacts"]:
            path = ANALYSIS / relative if "/" not in relative else ROOT / relative
            exists = path.exists()
            age_hours = None
            if exists:
                age_hours = round((now.timestamp() - path.stat().st_mtime) / 3600, 2)
            artifacts.append({"path": relative, "exists": exists, "age_hours": age_hours})
        missing = [a["path"] for a in artifacts if not a["exists"]]
        families.append({
            "family_id": family_id,
            "registered": family_id in registered,
            "cadence": item["cadence"],
            "trigger": item["trigger"],
            "artifacts": artifacts,
            "status": "ready_for_review" if not missing and family_id in registered else "incomplete",
            "missing_artifacts": missing,
        })
    report = {
        "schema": "external-trend-intelligence.refresh-status.v1",
        "generated_at": now.isoformat(),
        "source_schedule": "refresh-schedule.json",
        "source_registry": "source-family-registry.json",
        "family_count": len(families),
        "ready_for_review_count": sum(f["status"] == "ready_for_review" for f in families),
        "incomplete_count": sum(f["status"] == "incomplete" for f in families),
        "families": families,
        "boundary": "Artifact presence and file age are operational checks, not proof that an external source is current, reachable, licensed, independent, or outcome-valid.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(families)} families)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
