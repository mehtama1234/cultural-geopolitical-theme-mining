#!/usr/bin/env python3
"""Build a descriptive temporal holdout for the normalized SHED series."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
RECORD = ROOT / "analysis" / "records" / "comparative-us-shed-financial-wellbeing-2013-2025.json"
OUTPUT = ANALYSIS / "shed-temporal-holdout.json"


def main() -> int:
    record = json.loads(RECORD.read_text())
    values = [{"period": int(row["period"]), "value": row["measures"]["doing_okay_or_living_comfortably"]["value"]} for row in record["observations"]]
    construction = [row for row in values if row["period"] <= 2021]
    holdout = [row for row in values if row["period"] >= 2022]
    peak = max(values, key=lambda row: row["value"])
    payload = {
        "schema": "external-trend-intelligence.shed-temporal-holdout.v1",
        "record_id": record["trend_id"],
        "source_family": record["source_unit"],
        "status": "descriptive_single_family_holdout",
        "construction_period": "2013-2021",
        "holdout_period": "2022-2025",
        "measure": record["observations"][0]["measures"]["doing_okay_or_living_comfortably"]["unit"],
        "construction": construction,
        "holdout": holdout,
        "construction_start": construction[0],
        "construction_end": construction[-1],
        "holdout_start": holdout[0],
        "holdout_end": holdout[-1],
        "peak_observation": peak,
        "peak_to_holdout_end_change": holdout[-1]["value"] - peak["value"],
        "readout": "The measure rose through a 2021 peak, then remained below peak through the 2022-2025 holdout window.",
        "falsifier": "A later compatible wave returning to or exceeding the 2021 peak without a documented method break would weaken the persistence interpretation.",
        "does_not_support": ["independent-source confirmation", "causality", "pooled international estimate", "company exposure", "qualified trend"],
        "next_action": "Compare the SHED holdout with an independent U.S. household-finance or hardship measure using a pre-specified denominator and period.",
        "boundary": "This is a descriptive repeated-cross-section holdout from one survey family. It is a backtest design/readout, not a causal or independent validation result."
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
