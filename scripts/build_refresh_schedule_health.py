#!/usr/bin/env python3
"""Verify and publish the external observatory schedule contract."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
WORKFLOW = ROOT / ".github" / "workflows" / "external-observatory-refresh.yml"
OUTPUT = ANALYSIS / "refresh-schedule-health.json"


def main() -> int:
    schedule = json.loads((ANALYSIS / "refresh-schedule.json").read_text())
    workflow_text = WORKFLOW.read_text()
    families = schedule["families"]
    checks = {
        "weekly_cron_present": "cron: '17 6 * * 1'" in workflow_text,
        "manual_dispatch_present": "workflow_dispatch:" in workflow_text,
        "concurrency_guard_present": "group: external-observatory-refresh" in workflow_text and "cancel-in-progress: false" in workflow_text,
        "pinned_workspace_check_present": "Verify pinned sibling workspace" in workflow_text,
        "full_refresh_command_present": "python3 scripts/refresh_external_observatory.py" in workflow_text,
        "generated_artifact_push_present": "git push" in workflow_text,
        "all_registered_families_have_triggers": all(item.get("trigger") for item in families),
        "all_registered_families_have_artifacts": all(item.get("refresh_artifacts") for item in families),
    }
    report = {
        "schema": "external-trend-intelligence.refresh-schedule-health.v1",
        "workflow": ".github/workflows/external-observatory-refresh.yml",
        "configured_cadence": "weekly_monday_06_17_utc",
        "registered_family_count": len(families),
        "event_triggered_family_count": sum(bool(item.get("trigger")) for item in families),
        "checks": checks,
        "status": "configured" if all(checks.values()) else "hold",
        "boundary": "This proves the schedule and workflow contract are configured. It does not prove two years of unattended execution, source freshness, rights clearance, or trend validity.",
        "next_action": "Review refresh-history.json after each scheduled run and investigate any missed, stale, or incomplete run.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({report['status']})")
    return 0 if report["status"] == "configured" else 1


if __name__ == "__main__":
    raise SystemExit(main())
