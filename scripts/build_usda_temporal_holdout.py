#!/usr/bin/env python3
"""Build a descriptive temporal holdout for the USDA food-security series."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
RECORD = ROOT / "analysis" / "records" / "comparative-usda-food-security-2022-2024.json"
OUTPUT = ANALYSIS / "usda-temporal-holdout.json"


def main() -> int:
    record = json.loads(RECORD.read_text())
    values = [{"period": int(row["period"]), "value": row["measures"]["food_insecure"]["value"]} for row in record["observations"]]
    construction = [row for row in values if row["period"] <= 2023]
    holdout = [row for row in values if row["period"] >= 2024]
    payload = {
        "schema": "external-trend-intelligence.usda-temporal-holdout.v1",
        "record_id": record["trend_id"],
        "source_family": record["source_unit"],
        "status": "descriptive_single_family_holdout",
        "construction_period": "2022-2023",
        "holdout_period": "2024",
        "measure": record["observations"][0]["measures"]["food_insecure"]["unit"],
        "construction": construction,
        "holdout": holdout,
        "construction_start": construction[0],
        "construction_end": construction[-1],
        "holdout_start": holdout[0],
        "holdout_end": holdout[-1],
        "change_to_holdout": holdout[-1]["value"] - construction[-1]["value"],
        "readout": "Food insecurity rose numerically from 2022 through the 2024 holdout, but USDA reports the 2024 prevalence was not statistically significantly different from 2023 or 2022.",
        "falsifier": "A later compatible release showing a statistically reliable reversal or a method break would weaken this descriptive persistence readout.",
        "does_not_support": ["independent-source confirmation", "causality", "pooled adult-household estimate", "company exposure", "qualified trend"],
        "next_action": "Attach year-specific standard errors or confidence intervals and compare with a pre-specified independent household-finance measure.",
        "boundary": "This is a descriptive repeated-cross-section holdout from one USDA survey family. It is not a causal or independent validation result."
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
