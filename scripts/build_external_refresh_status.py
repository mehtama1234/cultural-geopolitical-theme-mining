#!/usr/bin/env python3
"""Build a visible, evidence-backed refresh status report for source families."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "refresh-status.json"

STALE_THRESHOLDS_HOURS = {
    "cultural-geopolitical-theme-mining": 24 * 45,
    "social-research": 24 * 45,
    "trend-hunting": 24 * 45,
    "annual-report-research": 24 * 120,
    "inc5000-analysis": 24 * 400,
    "ibis-industries": 24 * 120,
    "research-signals": 24 * 400,
    "organization-intelligence-system": 24 * 400,
}


def build_report(schedule: dict, registry: dict, now: datetime, *, root: Path = ROOT, analysis: Path = ANALYSIS) -> dict:
    registered = {family["id"] for family in registry["source_families"]}
    families = []
    for item in schedule["families"]:
        family_id = item["family_id"]
        artifacts = []
        for relative in item["refresh_artifacts"]:
            path = analysis / relative if "/" not in relative else root / relative
            exists = path.exists()
            age_hours = None
            if exists:
                age_hours = round((now.timestamp() - path.stat().st_mtime) / 3600, 2)
            artifacts.append({"path": relative, "exists": exists, "age_hours": age_hours})
        missing = [a["path"] for a in artifacts if not a["exists"]]
        threshold = STALE_THRESHOLDS_HOURS.get(family_id, 24 * 90)
        observed_ages = [a["age_hours"] for a in artifacts if a["age_hours"] is not None]
        stale = bool(observed_ages) and max(observed_ages) > threshold
        families.append({
            "family_id": family_id,
            "registered": family_id in registered,
            "cadence": item["cadence"],
            "trigger": item["trigger"],
            "stale_threshold_hours": threshold,
            "artifacts": artifacts,
            "status": "incomplete" if missing or family_id not in registered else ("stale" if stale else "ready_for_review"),
            "missing_artifacts": missing,
            "stale": stale,
        })
    return {
        "schema": "external-trend-intelligence.refresh-status.v1",
        "generated_at": now.isoformat(),
        "source_schedule": "refresh-schedule.json",
        "source_registry": "source-family-registry.json",
        "family_count": len(families),
        "ready_for_review_count": sum(f["status"] == "ready_for_review" for f in families),
        "incomplete_count": sum(f["status"] == "incomplete" for f in families),
        "stale_count": sum(f["status"] == "stale" for f in families),
        "families": families,
        "boundary": "Artifact presence and file age are operational checks, not proof that an external source is current, reachable, licensed, independent, or outcome-valid.",
    }
def main() -> int:
    schedule = json.loads((ANALYSIS / "refresh-schedule.json").read_text())
    registry = json.loads((ANALYSIS / "source-family-registry.json").read_text())
    report = build_report(schedule, registry, datetime.now(timezone.utc))
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(report['families'])} families)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
