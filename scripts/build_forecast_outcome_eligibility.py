#!/usr/bin/env python3
"""Determine whether each forecast row is eligible for a realized-outcome backtest."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "forecast-outcome-eligibility.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def target_year(measure: str) -> int:
    return int(measure.rsplit("_", 1)[-1])


def main() -> int:
    register = load("forecast-backtest-register.json")
    as_of = date.today()
    rows = []
    for forecast in register["rows"]:
        year = target_year(forecast["measure"])
        period_closed = as_of > date(year, 12, 31)
        if forecast["observed_outcome"] is not None:
            status = "outcome_present_pending_quality_review"
        elif period_closed:
            status = "eligible_outcome_missing"
        else:
            status = "not_yet_eligible_period_open"
        rows.append(
            {
                "backtest_id": forecast["backtest_id"],
                "measure": forecast["measure"],
                "target_year": year,
                "period_closed": period_closed,
                "eligibility_status": status,
                "forecast_value": forecast["forecast_value"],
                "observed_outcome_present": forecast["observed_outcome"] is not None,
                "required_outcome_fields": forecast["acceptance_criteria"],
                "next_action": "Append a comparable full-year official outcome and retained vintage before calculating error." if period_closed else "Do not score yet; retain the forecast and wait for a full-year official realized release.",
            }
        )
    payload = {
        "schema": "external-trend-intelligence.forecast-outcome-eligibility.v1",
        "as_of": as_of.isoformat(),
        "row_count": len(rows),
        "not_yet_eligible_count": sum(row["eligibility_status"] == "not_yet_eligible_period_open" for row in rows),
        "eligible_outcome_missing_count": sum(row["eligibility_status"] == "eligible_outcome_missing" for row in rows),
        "outcome_present_count": sum(row["observed_outcome_present"] for row in rows),
        "rows": rows,
        "boundary": "Eligibility is a timing control, not evidence of forecast accuracy. No forecast error is calculated until a comparable full-year realized outcome, vintage, definition, and uncertainty are accepted.",
        "next_action": "At each refresh, re-evaluate period closure; for eligible rows acquire the first comparable official outcome and preserve later revisions separately.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({payload['not_yet_eligible_count']} periods still open)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
