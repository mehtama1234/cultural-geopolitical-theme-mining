#!/usr/bin/env python3
"""Build a signable weekly continuity packet without fabricating future runs."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "continuity-review-packet.json"


def main() -> int:
    plan = json.loads((ANALYSIS / "continuity-coverage-plan.json").read_text())
    audit = json.loads((ANALYSIS / "refresh-continuity-audit.json").read_text())
    observed = {row["week"]: row for row in plan["observed_weeks"]}
    rows = []
    for week, evidence in sorted(observed.items()):
        rows.append({
            "week": week,
            "status": "observed",
            "scheduled_window_utc": None,
            "actual_run_timestamp_utc": evidence["latest_run"],
            "run_count": evidence["run_count"],
            "passed_run_count": evidence["passed_run_count"],
            "pipeline_status_and_step_count": "passed full refresh; see refresh-history.json",
            "source_family_freshness_decision": "see refresh-freshness-decision.json",
            "open_gate_delta": None,
            "missed_window_reason_or_null": None,
            "manual_dispatch_recovery_artifact_or_null": None,
            "release_owner_review_and_next_review_date": None,
        })
    for index in range(len(rows) + 1, plan["required_week_count"] + 1):
        rows.append({
            "week": None,
            "slot_index": index,
            "status": "unobserved",
            "scheduled_window_utc": None,
            "actual_run_timestamp_utc": None,
            "run_count": 0,
            "passed_run_count": 0,
            "pipeline_status_and_step_count": None,
            "source_family_freshness_decision": None,
            "open_gate_delta": None,
            "missed_window_reason_or_null": None,
            "manual_dispatch_recovery_artifact_or_null": None,
            "release_owner_review_and_next_review_date": None,
        })
    payload = {
        "schema": "external-trend-intelligence.continuity-review-packet.v1",
        "status": "ready_for_weekly_release_owner_review",
        "required_week_count": plan["required_week_count"],
        "observed_week_count": plan["observed_distinct_week_count"],
        "remaining_week_count": plan["remaining_week_count"],
        "passed_run_count": audit["passed_run_count"],
        "rows": rows,
        "required_signoff_fields": plan["weekly_window_record_schema"],
        "acceptance_criteria": [
            "Every distinct weekly window has one passed full refresh and the required evidence fields.",
            "A gap over 168 hours retains the prior release and manual-dispatch recovery evidence.",
            "A burst of runs in one week is not counted as multiple weekly windows.",
            "Unobserved future slots remain blank rather than being treated as passed.",
        ],
        "next_action": plan["next_action"],
        "boundary": "This packet structures continuity review; it does not predict future execution or convert configured scheduling into two-year evidence.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} weekly slots; {payload['observed_week_count']} observed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
