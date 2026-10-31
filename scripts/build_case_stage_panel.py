#!/usr/bin/env python3
"""Code common remedy and recovery stages for the bounded Australian case panel."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "case-stage-panel.json"

PANEL_ID = "australia-platform-remedy-case-panel-001"
RECORD_IDS = [
    "au-al-hussein-reactivation-deemed-work-2025",
    "au-fwc-khan-platform-repeat-deactivation-2026",
    "au-mansoor-platform-alternative-earnings-remedy-2025",
]

STAGES = {
    "formal_response": ("reactivation_order", "reactivation", "procedural_finding", "remedy", "lost_pay_confer_direction"),
    "implementation": ("deemed_work_during_interruption", "payment_deadline_days", "lost_pay_confer_direction"),
    "receipt": ("payment_receipt_observed", "quantified_payment_order_observed"),
    "durable_access": ("actual_access_after_order_observed", "continued_work_or_switching_observed", "later_continued_use_or_exit_observed", "payment_and_durability"),
    "substitution_or_exit": ("baysec_substitute_earnings", "didi_post_deactivation_earnings", "continued_work_or_switching_observed", "later_continued_use_or_exit_observed"),
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
            if refs:
                stage_values[stage] = {"status": "observed", "measure_refs": refs}
            else:
                stage_values[stage] = {"status": "not_observed_in_public_record", "measure_refs": {}}
        cases.append({"record_id": record_id, "geography": record.get("geography"), "stages": stage_values})
    report = {
        "schema": "external-trend-intelligence.case-stage-panel.v1",
        "subset_id": PANEL_ID,
        "case_count": len(cases),
        "stage_definitions": {stage: list(keys) for stage, keys in STAGES.items()},
        "cases": cases,
        "status": "stage_coded_bounded_panel",
        "boundary": "A stage marked not_observed_in_public_record is not a negative outcome. This panel is shared-publisher case evidence, not population prevalence, independent confirmation, a backtest, or a company finding.",
        "next_action": "Add an independent source family with the same stage definitions and comparable periods before trend promotion or internal bridging.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
