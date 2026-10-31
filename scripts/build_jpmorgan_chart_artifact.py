#!/usr/bin/env python3
"""Expose the pinned JPMorgan chart metadata through the board reader API."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "analysis" / "records" / "comparative-jpmorgan-household-liquidity-2023.json"
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "jpmorgan-household-liquidity-chart.json"


def main() -> int:
    record = json.loads(SOURCE.read_text())
    payload = {
        "schema": "external-trend-intelligence.frontend-chart-artifact.v1",
        "record_id": record["trend_id"],
        "title": record["title"],
        "source_unit": record["source_unit"],
        "chart_asset": record["chart_asset"],
        "rights_boundary": record["boundary"],
        "source_record": "../records/comparative-jpmorgan-household-liquidity-2023.json",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
