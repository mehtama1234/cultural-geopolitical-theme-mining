#!/usr/bin/env python3
"""Publish a bounded comparison of independent global-growth forecasts."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "global-growth-forecast-comparison.json"


def main() -> int:
    search = json.loads((ANALYSIS / "compatible-measure-search.json").read_text())
    rows = [row for row in search["rows"] if row["measure"] in {"global_growth_2026", "global_growth_2027"}]
    assert len(rows) == 2
    forecasts = []
    for row in rows:
        values = []
        for observation in row["observations"]:
            values.append(
                {
                    "record_id": observation["record_id"],
                    "title": observation["title"],
                    "period": observation["period"],
                    "value": observation["value"],
                    "source_hosts": observation["hosts"],
                }
            )
        values.sort(key=lambda item: item["record_id"])
        forecasts.append({"measure": row["measure"], "unit": row["unit"], "values": values, "spread": round(max(item["value"] for item in values) - min(item["value"] for item in values), 2)})
    report = {
        "schema": "external-trend-intelligence.global-growth-forecast-comparison.v1",
        "status": "independent_forecast_comparison_pending_backtest",
        "source_families": ["OECD", "UN DESA", "World Bank"],
        "forecasts": forecasts,
        "supports": ["independent forecast-range visibility", "geopolitical and financial scenario framing", "future forecast-versus-outcome backtest design"],
        "does_not_support": ["observed global growth trend", "causal attribution to an energy shock", "pooled forecast", "company exposure"],
        "blocking_items": [
            "forecast vintages and publication dates differ",
            "global-economy coverage and model definitions are not identical",
            "forecast uncertainty intervals are not carried in the source records",
            "realized 2026 and 2027 outcomes are not yet available for backtesting",
            "rights and publisher-dependence review remains open",
        ],
        "next_action": "Record the forecast vintage, interval or scenario range, and realized outcome when each release becomes available; retain revisions rather than overwriting the forecast.",
        "boundary": "This is a bounded independent forecast comparison. It is not a qualified trend, forecast endorsement, causal estimate, or internal company finding.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(forecasts)} forecast measures)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
