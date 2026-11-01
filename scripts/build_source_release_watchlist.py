#!/usr/bin/env python3
"""Build an external release watchlist from acquired source artifacts.

The watchlist records the latest pinned period and the next acquisition target;
it does not infer that a source is current, licensed, or comparable.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "source-release-watchlist.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    ora = load("open-repair-alliance-mobile-snapshot.json")
    cbp = load("census-repair-industry-snapshot.json")
    nes = load("census-nonemployer-repair-snapshot.json")
    npals = load("npals-public-table-extract.json")
    shed = load("federal-reserve-shed-financial-room-2013-2025.json")

    cbp_latest = max(row["year"] for row in cbp["source"]["retrievals"])
    nes_latest = max(row["year"] for row in nes["source"]["retrievals"])
    npals_latest = max(int(row["survey_year"]) for row in npals["rows"])
    shed_latest = max(int(row["period"]) for row in shed["observations"])
    rows = [
        {
            "source_id": ora["acquisition_id"],
            "publisher": ora["source"]["publisher"],
            "artifact": "open-repair-alliance-mobile-snapshot.json",
            "latest_observation_period": "through July 2026",
            "next_target_period": "next ORA aggregate release",
            "cadence_or_trigger": "new aggregate archive or schema revision",
            "status": "latest_pinned_period_recorded",
            "acquisition_action": ora["next_action"],
        },
        {
            "source_id": cbp["acquisition_id"],
            "publisher": cbp["source"]["publisher"],
            "artifact": "census-repair-industry-snapshot.json",
            "latest_observation_period": str(cbp_latest),
            "next_target_period": str(cbp_latest + 1),
            "cadence_or_trigger": "annual CBP release",
            "status": "next_annual_release_targeted",
            "acquisition_action": cbp["next_action"],
        },
        {
            "source_id": nes["acquisition_id"],
            "publisher": nes["source"]["publisher"],
            "artifact": "census-nonemployer-repair-snapshot.json",
            "latest_observation_period": str(nes_latest),
            "next_target_period": str(nes_latest + 1),
            "cadence_or_trigger": "annual NES release",
            "status": "next_annual_release_targeted",
            "acquisition_action": nes["next_action"],
        },
        {
            "source_id": npals["source_id"],
            "publisher": "CDC/NCHS",
            "artifact": "npals-public-table-extract.json",
            "latest_observation_period": str(npals_latest),
            "next_target_period": "next biennial or table revision",
            "cadence_or_trigger": "new NPALS public table or API revision",
            "status": npals["retrieval_status"],
            "acquisition_action": npals["next_action"],
        },
        {
            "source_id": shed["acquisition_id"],
            "publisher": shed["publisher"],
            "artifact": "federal-reserve-shed-financial-room-2013-2025.json",
            "latest_observation_period": str(shed_latest),
            "next_target_period": str(shed_latest + 1),
            "cadence_or_trigger": "annual SHED release and codebook update",
            "status": "latest_report_context_recorded_uncertainty_open",
            "acquisition_action": "Acquire the next SHED chart-data and codebook release; preserve question wording, weights, design-effect context, and exact-artifact rights review.",
        },
    ]
    payload = {
        "schema": "external-trend-intelligence.source-release-watchlist.v1",
        "status": "acquired_source_release_targets_recorded",
        "source_count": len(rows),
        "rows": rows,
        "boundary": "The watchlist records release targets from pinned artifacts. It does not prove upstream freshness, rights clearance, independence, comparability, or a trend result.",
        "next_action": "At each scheduled refresh, compare the pinned period with the target period, acquire only the official revision, preserve its checksum and terms, and route method or rights breaks to review.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} source release targets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
