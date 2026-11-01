#!/usr/bin/env python3
"""Build a future forecast-versus-outcome backtest register."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "forecast-backtest-register.json"


def main() -> int:
    comparison = json.loads((ANALYSIS / "global-growth-forecast-comparison.json").read_text())
    rows = []
    for forecast in comparison["forecasts"]:
        for value in forecast["values"]:
            rows.append(
                {
                    "backtest_id": f"{value['record_id']}::{forecast['measure']}",
                    "source_record_id": value["record_id"],
                    "source_host": value["source_hosts"][0] if value["source_hosts"] else None,
                    "measure": forecast["measure"],
                    "unit": forecast["unit"],
                    "forecast_period": value["period"],
                    "forecast_value": value["value"],
                    "observed_outcome": None,
                    "observed_outcome_period": None,
                    "forecast_error": None,
                    "status": "awaiting_realized_outcome",
                    "refresh_trigger": "first comparable official realized release after the forecast period",
                    "acceptance_criteria": [
                        "same measure definition and geography recorded",
                        "realized outcome period and revision/vintage recorded",
                        "uncertainty or interval treatment recorded for forecast and outcome",
                        "forecast error retained without overwriting the original forecast",
                    ],
                }
            )
    report = {
        "schema": "external-trend-intelligence.forecast-backtest-register.v1",
        "comparison_artifact": "global-growth-forecast-comparison.json",
        "row_count": len(rows),
        "pending_count": sum(row["status"] == "awaiting_realized_outcome" for row in rows),
        "completed_count": sum(row["status"] == "completed" for row in rows),
        "rows": rows,
        "next_action": "At each comparable official release, append the realized outcome and uncertainty, calculate error, and retain forecast revisions as separate vintages.",
        "boundary": "This register defines a future backtest; it is not evidence that any forecast was accurate and does not authorize company exposure.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} rows; {report['pending_count']} pending)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
