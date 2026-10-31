#!/usr/bin/env python3
"""Code the same remedy/recovery stages across the five-case cross-publisher panel."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "cross-publisher-stage-panel.json"

RECORD_IDS = [
    "au-al-hussein-reactivation-deemed-work-2025",
    "au-fwc-khan-platform-repeat-deactivation-2026",
    "au-mansoor-platform-alternative-earnings-remedy-2025",
    "comparative-australia-fwo-atkins-truck-driver-backpay-receipt-2018",
    "comparative-australia-fwc-no-alternative-employment-remedy-2024",
]

STAGES = {
    "formal_response": ("reactivation_order", "reactivation", "procedural_finding", "remedy", "compensation_order"),
    "implementation": ("deemed_work_during_interruption", "payment_deadline_days", "lost_pay_confer_direction"),
    "receipt": ("payment_receipt_observed", "workers_reported_receiving", "payment_receipt_and_later_work"),
    "durable_access": ("actual_access_after_order_observed", "continued_work_or_switching_observed", "later_continued_use_or_exit_observed", "payment_and_durability"),
    "substitution_or_exit": ("alternative_employment_search", "baysec_substitute_earnings", "didi_post_deactivation_earnings", "continued_work_or_switching_observed", "later_continued_use_or_exit_observed"),
}


def main() -> int:
    snapshot = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())["records"]
    cases = []
    for record_id in RECORD_IDS:
        record = snapshot[record_id]["record"]
        measures = {}
        for observation in record.get("observations", []):
            for name, value in observation.get("measures", {}).items():
                measures[name] = {"value": value.get("value"), "unit": value.get("unit"), "period": observation.get("period"), "status": observation.get("status")}
        stage_values = {}
        for stage, keys in STAGES.items():
            refs = {key: measures[key] for key in keys if key in measures}
            stage_values[stage] = {"status": "observed" if refs else "not_observed_in_public_record", "measure_refs": refs}
        cases.append({"record_id": record_id, "publisher_family": record.get("publisher"), "geography": record.get("geography"), "stages": stage_values})
    report = {
        "schema": "external-trend-intelligence.cross-publisher-stage-panel.v1",
        "subset_id": "australia-remedy-cross-publisher-panel-001",
        "case_count": len(cases),
        "publisher_families": ["Fair Work Commission", "Fair Work Ombudsman"],
        "stage_definitions": {stage: list(keys) for stage, keys in STAGES.items()},
        "cases": cases,
        "status": "stage_coded_cross_publisher_panel",
        "boundary": "Common stage labels expose comparable structure; they do not make case types, denominators, periods, publishers, or outcomes identical. This is not a backtest, prevalence estimate, causal finding, or company finding.",
        "next_action": "Review underlying legal and administrative lineage, preserve publisher differences, and pre-specify an independent holdout before any promotion.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
