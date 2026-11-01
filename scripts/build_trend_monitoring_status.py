#!/usr/bin/env python3
"""Materialize the current execution state of every trend-monitoring watch."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "trend-monitoring-status.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    register = load("trend-monitoring-register.json")
    rows = []
    for trend in register["trends"]:
        state = trend["state"]
        rows.append(
            {
                "candidate_id": trend["candidate_id"],
                "state": state,
                "execution_status": "awaiting_next_comparable_release" if state == "qualified_monitor" else "blocked_prequalification",
                "cadence": trend["cadence"],
                "next_review": trend["next_review"],
                "leading_indicator_count": len(trend["leading_indicators"]),
                "reversal_condition_count": len(trend["reversal_conditions"]),
                "owner": trend["owner"],
            }
        )
    payload = {
        "schema": "external-trend-intelligence.trend-monitoring-status.v1",
        "as_of": date.today().isoformat(),
        "trend_count": len(rows),
        "qualified_monitor_count": sum(row["state"] == "qualified_monitor" for row in rows),
        "prequalification_watch_count": sum(row["state"] == "pre_qualification_watch" for row in rows),
        "rows": rows,
        "boundary": "This status records monitoring execution state and next-review conditions. It does not promote held candidates, predict outcomes, or authorize company data access.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} watches)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
