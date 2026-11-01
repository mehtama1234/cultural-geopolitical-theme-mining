#!/usr/bin/env python3
"""Measure observed refresh continuity without claiming future schedule coverage."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "refresh-continuity-audit.json"


def parse(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def main() -> int:
    history = json.loads((ANALYSIS / "refresh-history.json").read_text())
    runs = [run for run in history["runs"] if run.get("run_id")]
    times = sorted(parse(run["run_id"]) for run in runs)
    intervals_hours = [(later - earlier).total_seconds() / 3600 for earlier, later in zip(times, times[1:])]
    pass_count = sum(run.get("pipeline_status") == "passed" for run in runs)
    observed_days = sorted({time.date().isoformat() for time in times})
    observed_weeks = sorted({time.strftime("%G-W%V") for time in times})
    # Count only missing weekly windows between the first and latest observed
    # weeks; future windows remain unobserved rather than being called missed.
    week_starts = sorted({(time - timedelta(days=time.weekday())).date() for time in times})
    missing_intervening_week_count = sum(
        max((later - earlier).days // 7 - 1, 0)
        for earlier, later in zip(week_starts, week_starts[1:])
    )
    latest = times[-1] if times else None
    next_scheduled = None
    if latest:
        next_monday = (latest + timedelta(days=(7 - latest.weekday()) % 7)).date()
        if next_monday <= latest.date():
            next_monday += timedelta(days=7)
        next_scheduled = datetime.combine(next_monday, datetime.min.time(), tzinfo=timezone.utc).replace(hour=6, minute=17).isoformat()
    required_two_year_weeks = 104
    coverage_ratio = min(len(observed_weeks) / required_two_year_weeks, 1.0)
    payload = {
        "schema": "external-trend-intelligence.refresh-continuity-audit.v1",
        "run_count": len(runs),
        "passed_run_count": pass_count,
        "observed_day_count": len(observed_days),
        "observed_days": observed_days,
        "first_observed_run": runs[0]["run_id"] if runs else None,
        "latest_observed_run": runs[-1]["run_id"] if runs else None,
        "max_interval_hours": round(max(intervals_hours), 3) if intervals_hours else None,
        "median_interval_hours": round(sorted(intervals_hours)[len(intervals_hours) // 2], 3) if intervals_hours else None,
        "expected_cadence": "weekly",
        "required_two_year_weeks": required_two_year_weeks,
        "observed_distinct_week_count": len(observed_weeks),
        "observed_week_keys": observed_weeks,
        "missing_intervening_week_count": missing_intervening_week_count,
        "next_scheduled_window_utc": next_scheduled,
        "recovery_path": "workflow_dispatch -> full refresh -> retain diagnostics -> append refresh history",
        "observed_week_coverage_ratio": round(coverage_ratio, 4),
        "observed_week_coverage_percent": round(coverage_ratio * 100, 1),
        "continuity_status": "observed_burst_only" if intervals_hours and max(intervals_hours) < 168 else "gaps_require_review",
        "unattended_two_year_coverage": "not_demonstrated",
        "next_action": "Allow the scheduled workflow to accumulate weekly runs across distinct weeks; investigate any gap over 168 hours and retain the workflow dispatch path for recovery.",
        "boundary": "This audit describes observed run history only. It does not prove that a future weekly schedule will execute for two years or that open evidence gates have passed.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(runs)} observed runs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
