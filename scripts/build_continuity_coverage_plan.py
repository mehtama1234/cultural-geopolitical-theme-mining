#!/usr/bin/env python3
"""Translate refresh history into an explicit two-year weekly coverage plan."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "continuity-coverage-plan.json"


def parse_run_id(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def main() -> int:
    history = json.loads((ANALYSIS / "refresh-history.json").read_text())
    audit = json.loads((ANALYSIS / "refresh-continuity-audit.json").read_text())
    runs = history.get("runs", [])
    weeks = {}
    for row in runs:
        run_id = row.get("run_id")
        if not run_id:
            continue
        dt = parse_run_id(run_id)
        iso = dt.isocalendar()
        key = f"{iso.year}-W{iso.week:02d}"
        bucket = weeks.setdefault(key, {"week": key, "run_count": 0, "passed_run_count": 0, "first_run": run_id, "latest_run": run_id})
        bucket["run_count"] += 1
        bucket["passed_run_count"] += int(row.get("pipeline_status") == "passed")
        bucket["first_run"] = min(bucket["first_run"], run_id)
        bucket["latest_run"] = max(bucket["latest_run"], run_id)
    observed = sorted(weeks.values(), key=lambda row: row["week"])
    required = int(audit.get("required_two_year_weeks", 104))
    observed_count = len(observed)
    payload = {
        "schema": "external-trend-intelligence.continuity-coverage-plan.v1",
        "status": "two_year_weekly_coverage_not_demonstrated" if observed_count < required else "two_year_weekly_coverage_demonstrated",
        "expected_cadence": audit.get("expected_cadence", "weekly"),
        "required_week_count": required,
        "observed_distinct_week_count": observed_count,
        "remaining_week_count": max(required - observed_count, 0),
        "observed_week_coverage_ratio": round(min(observed_count / required, 1.0), 4) if required else 0.0,
        "observed_week_coverage_percent": round(min(observed_count / required * 100, 100), 2) if required else 0.0,
        "observed_weeks": observed,
        "run_count": len(runs),
        "passed_run_count": sum(int(row.get("pipeline_status") == "passed") for row in runs),
        "acceptance": "Each of 104 distinct weekly windows must contain a passed full refresh, with missed-window recovery evidence retained.",
        "weekly_window_record_schema": [
            "scheduled_window_utc",
            "actual_run_timestamp_utc",
            "pipeline_status_and_step_count",
            "source_family_freshness_decision",
            "open_gate_delta",
            "missed_window_reason_or_null",
            "manual_dispatch_recovery_artifact_or_null",
            "release_owner_review_and_next_review_date",
        ],
        "missed_window_policy": "Investigate any gap over 168 hours, preserve the prior release, run manual dispatch, and retain the recovery output alongside the affected weekly row.",
        "required_review_evidence": [
            "refresh-history.json",
            "refresh-continuity-audit.json",
            "refresh-schedule-health.json",
            "release-health.json",
        ],
        "next_action": "Allow the scheduled workflow to accumulate distinct weekly windows; investigate any missing or stale window and retain manual-dispatch recovery evidence.",
        "boundary": "This plan measures observed weekly coverage only. It does not predict future execution, clear rights, qualify trends, or authorize internal company access.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({observed_count}/{required} distinct weeks observed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
