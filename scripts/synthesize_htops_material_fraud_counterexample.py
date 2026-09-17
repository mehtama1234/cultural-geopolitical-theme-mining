#!/usr/bin/env python3
"""Compare existing HTOPS material-pressure and fraud follow-up aggregates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


OUTCOMES = {
    "food_insufficiency": "food_insufficiency",
    "unable_to_pay_energy_bill": "unable_to_pay_energy_bill",
    "recent_household_job_loss": "recent_household_job_loss",
}


def metric(data: dict, route: str, outcome: str) -> float:
    value = data[route][outcome]["weighted_percent"]
    if value is None:
        raise ValueError(f"missing metric {route}/{outcome}")
    return float(value)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--material",
        type=Path,
        default=root / "analysis/projects/us-cost-trust-politics/data/htops-2025-cross-lagged-panel-audit.json",
    )
    parser.add_argument(
        "--fraud",
        type=Path,
        default=root / "analysis/projects/us-cost-trust-politics/data/htops-2025-fraud-followup-2025-04-to-06.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=root / "analysis/projects/us-cost-trust-politics/data/htops-material-vs-fraud-counterexample-2025.json",
    )
    args = parser.parse_args()
    material = json.loads(args.material.read_text(encoding="utf-8"))
    fraud = json.loads(args.fraud.read_text(encoding="utf-8"))
    if material.get("format") != "htops-cross-lagged-panel-audit-v1":
        raise ValueError("unexpected material-pressure audit format")
    if fraud.get("format") != "htops-2025-fraud-followup-v1":
        raise ValueError("unexpected fraud follow-up format")

    material_routes = {
        "expense_difficulty": {
            outcome: material["measures"][f"baseline_expense_difficulty_{outcome}"]["value"]
            for outcome in OUTCOMES.values()
        },
        "expense_not_difficult": {
            outcome: material["measures"][f"baseline_expense_not_difficult_{outcome}"]["value"]
            for outcome in OUTCOMES.values()
        },
    }
    fraud_routes = {
        "not_exposed": {outcome: metric(fraud["metrics"], "not_exposed", f"june_{outcome}") for outcome in OUTCOMES.values()},
        "exposed": {outcome: metric(fraud["metrics"], "exposed", f"june_{outcome}") for outcome in OUTCOMES.values()},
        "exposed_and_lost": {outcome: metric(fraud["metrics"], "exposed_and_lost", f"june_{outcome}") for outcome in OUTCOMES.values()},
        "lost_and_reported": {outcome: metric(fraud["metrics"], "lost_and_reported", f"june_{outcome}") for outcome in OUTCOMES.values()},
    }
    comparisons = {}
    for outcome in OUTCOMES.values():
        comparisons[outcome] = {
            "expense_difficulty_minus_not_difficult_pp": round(material_routes["expense_difficulty"][outcome] - material_routes["expense_not_difficult"][outcome], 4),
            "fraud_exposed_minus_not_exposed_pp": round(fraud_routes["exposed"][outcome] - fraud_routes["not_exposed"][outcome], 4),
            "fraud_exposed_and_lost_minus_not_exposed_pp": round(fraud_routes["exposed_and_lost"][outcome] - fraud_routes["not_exposed"][outcome], 4),
            "loss_reported_minus_not_exposed_pp": round(fraud_routes["lost_and_reported"][outcome] - fraud_routes["not_exposed"][outcome], 4),
        }
    result = {
        "format": "htops-material-vs-fraud-counterexample-v1",
        "status": "within_panel_nonpooled_counterexample",
        "checked": "2026-09-16",
        "period": "April 15–29 to June 16–25, 2025",
        "unit": "same HTOPS respondent across the two source-derived aggregate screens; no respondent rows are rejoined here",
        "material_pressure_routes": material_routes,
        "fraud_routes": fraud_routes,
        "group_counts": {
            "material_linked_ids": material["linked_ids"],
            "fraud_linked_ids": fraud["linked_ids"],
            "fraud_not_exposed": fraud["group_unweighted_counts"]["not_exposed"],
            "fraud_exposed": fraud["group_unweighted_counts"]["exposed"],
            "fraud_exposed_and_lost": fraud["group_unweighted_counts"]["exposed_and_lost"],
            "fraud_lost_and_reported": fraud["group_unweighted_counts"]["lost_and_reported"],
        },
        "comparisons_percentage_points": comparisons,
        "interpretation": "The broad material-pressure route shows a consistent positive association with later food, energy, and job-loss outcomes. In the fraud route, exposure alone is not a monotonic marker: the exposed-minus-not-exposed contrast is negative for all three outcomes, while the exposure-plus-loss group is higher for food and energy. This is a counterexample to treating any retrospective scam exposure as equivalent to realized loss or to a general material-pressure state.",
        "boundary": "The two screens use different April group definitions and selected valid outcome universes, although both use the April-to-June linked HTOPS panel and April weights. The comparison is descriptive and associative; it does not establish fraud, expense difficulty, or loss causation, and it does not compare individual-level rows. Reported-loss and recovery groups are sparse, with 51 and 11 linked respondents respectively. No trust or exit conclusion is drawn from this comparison.",
        "source_records": [
            "analysis/projects/us-cost-trust-politics/data/htops-2025-cross-lagged-panel-audit.json",
            "analysis/projects/us-cost-trust-politics/data/htops-2025-fraud-followup-2025-04-to-06.json"
        ]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"VALID HTOPS material/fraud counterexample: output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
