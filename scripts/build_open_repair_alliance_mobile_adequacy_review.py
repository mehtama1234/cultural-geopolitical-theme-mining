#!/usr/bin/env python3
"""Assess whether the ORA mobile proxy can answer the phone-policy question."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "open-repair-alliance-mobile-snapshot.json"
OUTPUT = ANALYSIS / "open-repair-alliance-mobile-adequacy-review.json"


def main() -> int:
    snapshot = json.loads(INPUT.read_text())
    payload = {
        "schema": "external-trend-intelligence.open-repair-alliance-mobile-adequacy-review.v1",
        "status": "acquired_but_policy_backtest_inadequate",
        "source_artifact": INPUT.name,
        "question": "Can this external phone-specific outcome proxy test whether repair-policy exposure changes repair outcomes for a US company-relevant population?",
        "observed_scope": {
            "global_mobile_records": snapshot["coverage"]["mobile_record_count"],
            "us_mobile_records": snapshot["coverage"]["us_mobile_record_count"],
            "population": "items logged at participating community repair events",
            "geography": "country only in the published EEE extract",
        },
        "available_fields": [
            "country", "event_date", "repair_status", "product_age", "brand",
            "data_provider", "partner_product_category", "repair_barrier_if_end_of_life",
        ],
        "required_for_policy_backtest": [
            "state_or_subnational_geography",
            "policy_exposure_date_and_treatment_definition",
            "comparison_geography_or_control_group",
            "stable_outcome_denominator_and_sampling_frame",
            "repair_price_or_cost",
            "replacement_decision_or_device_life_outcome",
        ],
        "field_coverage_assessment": {
            "state_or_subnational_geography": False,
            "policy_exposure_date_and_treatment_definition": False,
            "comparison_geography_or_control_group": False,
            "stable_outcome_denominator_and_sampling_frame": False,
            "repair_price_or_cost": False,
            "replacement_decision_or_device_life_outcome": False,
        },
        "decision": "Use for descriptive global/US community-repair context and hypothesis generation only. Do not pool with Census proxies, state-policy records, e-waste, or company data; do not claim a policy effect or population repair rate.",
        "why_held": [
            "The file has country but no state or other subnational treatment geography.",
            "Community-event participation is a selected convenience sample, not a population denominator.",
            "Repair status is observed, but price, replacement, and device-life outcomes are absent.",
        ],
        "next_action": "Acquire a representative US transaction or consumer panel with state, policy timing, denominator, and replacement/device-life measures; use ORA only as a descriptive external comparator until then.",
        "falsifier": "A later state-resolved, representative outcome source shows a materially different direction or timing than the ORA descriptive signal.",
        "rights_and_lineage": "Carry forward the ORA CC BY-SA 4.0 attribution, archive checksum, and field-level transformation notes from the source snapshot.",
        "boundary": "Acquisition is complete; qualification for the policy or company-pilot question is not.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
