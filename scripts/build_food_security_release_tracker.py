#!/usr/bin/env python3
"""Track the next comparable releases for the monitored food-security trend."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "food-security-release-tracker.json"


def main() -> int:
    holdout = json.loads((ANALYSIS / "food-insecurity-temporal-holdout.json").read_text())
    payload = {
        "schema": "external-trend-intelligence.food-security-release-tracker.v1",
        "candidate_id": holdout["candidate_id"],
        "status": "monitoring_release_state_recorded",
        "source_records": [
            {
                "source_record_id": "comparative-usda-food-security-2022-2024",
                "publisher": "USDA Economic Research Service",
                "latest_observation_period": "2024",
                "latest_release_date": "2025-12-30",
                "latest_release_url": "https://ers.usda.gov/publications/113622",
                "official_key_statistics_url": "https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-us/key-statistics-graphics",
                "next_target_period": "2025",
                "next_target_status": "not_observed_in_pinned_artifact",
                "measure": "percent of U.S. households food insecure at some time during the year",
                "release_action": "Acquire the next annual ERS report or official table, then retain the definition, standard errors, method notes, and exact-artifact rights boundary.",
            },
            {
                "source_record_id": "us-urban-wbns-food-insecurity-persistence-2019-2025",
                "publisher": "Urban Institute",
                "latest_observation_period": "December 2025",
                "latest_release_date": "2026-03",
                "latest_release_url": "https://www.urban.org/sites/default/files/2026-03/Food%20Insecurity%20Remained%20High%20in%202025%2C%20As%20Safety%20Net%20Cuts%20Loom%20.pdf",
                "official_catalog_url": "https://datacatalog.urban.org/dataset/well-being-and-basic-needs-survey",
                "next_target_period": "next WBNS release",
                "next_target_status": "awaiting_next_comparable_wave",
                "measure": "percent of Urban WBNS adult-respondent households reporting food insecurity",
                "release_action": "Preserve the 2025 instrument/method break and obtain the next compatible table or public-use file before revising the holdout.",
            },
        ],
        "monitoring_decision": "continue_monitored_external_trend",
        "comparability_boundary": "USDA household prevalence and Urban adult-respondent prevalence remain separate series; do not pool values or treat the USDA 2024 nonsignificant change as independent confirmation of the Urban level.",
        "rights_boundary": "Retain attributed metadata and normalized internal-review values only until each exact publication, table, or public-use file has a recorded reuse decision.",
        "next_review": "At the next USDA ERS annual release or next comparable Urban WBNS wave, whichever arrives first.",
        "source_of_truth": "food-insecurity-temporal-holdout.json and source-specific rights reviews remain authoritative for current values and permissions.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(payload['source_records'])} tracked release families)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
