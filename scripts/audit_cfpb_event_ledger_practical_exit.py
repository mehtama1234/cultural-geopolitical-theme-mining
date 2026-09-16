#!/usr/bin/env python3
"""Audit the CFPB event ledger against the practical-exit contract."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def observed_or_unknown(value: str) -> str:
    return "unknown" if value.lower().startswith(("not observed", "unknown")) else "observed"


def convert(event: dict) -> dict:
    remedy = event["remedy_or_institutional_response"]
    later = event["later_outcome"]
    return {
        "episode_id": event["event_id"],
        "unit": event["unit"],
        "domain": "consumer_financial_recourse",
        "event_date": event["event_date"],
        "date_precision": event["date_precision"],
        "geography": event["geography"],
        "trigger": {"value": event["condition_or_decision"], "evidence_status": event["evidence_status"]},
        "threatened_resource": {"value": event["exposure"], "evidence_status": "observed"},
        "alternatives": {"value": event["alternatives_before_action"], "evidence_status": observed_or_unknown(event["alternatives_before_action"])},
        "attempted_route": {"value": event["choice_or_response"], "evidence_status": "observed"},
        "effort": {"value": event["cost_risk_transfer"], "evidence_status": observed_or_unknown(event["cost_risk_transfer"])},
        "decision": {"value": remedy, "evidence_status": "observed"},
        "remedy_verification": {"value": remedy, "evidence_status": "observed", "receipt_verified": "unknown"},
        "followup_window": {"value": later, "evidence_status": observed_or_unknown(later)},
        "post_event_status": "unknown",
        "protected_outcome": {"value": event["protected_outcome"], "evidence_status": observed_or_unknown(event["protected_outcome"])},
        "sacrificed_outcome": {"value": event["sacrificed_outcome"], "evidence_status": observed_or_unknown(event["sacrificed_outcome"])},
        "meaning_and_action": {"value": event["meaning_and_attribution"], "evidence_status": observed_or_unknown(event["meaning_and_attribution"])},
        "counterexample": {"value": event["counterexample"], "evidence_status": "observed"},
        "denominator": {"value": event["denominator"], "evidence_status": "observed"},
        "missingness": event["missingness"],
        "source_and_uncertainty": {"value": event["source_and_uncertainty"], "evidence_status": "observed"},
        "evidence_status": event["evidence_status"],
    }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=root / "analysis/projects/us-customer-automation-recourse/data/cfpb-student-loan-event-ledger-2024-25.json")
    parser.add_argument("--output", type=Path, default=root / "analysis/projects/us-customer-automation-recourse/cfpb-practical-exit-contract-dry-run-v1.json")
    args = parser.parse_args()
    data = json.loads(args.ledger.read_text(encoding="utf-8"))
    episodes = [convert(event) for event in data["events"]]
    result = {
        "format": "cfpb-practical-exit-contract-dry-run-v1",
        "status": "coverage_audit_only",
        "checked": "2026-09-16",
        "contract": "practical-exit-observation-contract-v1",
        "source_ledger": str(args.ledger.relative_to(root)),
        "source_record_count": len(episodes),
        "post_event_status_counts": dict(Counter(e["post_event_status"] for e in episodes)),
        "coverage": {
            "trigger_exposure_route_decision_counterexample_denominator": "observed",
            "alternatives": "unknown_for_all_records",
            "effort": "unknown_or_unmeasured_for_all_records",
            "remedy_receipt_and_durability": "unknown_for_all_records",
            "followup_switching_non_use_exit_trust_action": "unknown_for_all_records",
        },
        "promotion_rule_result": "No practical_exit labels are assigned: the ledger has no same-customer post-event status plus documented alternative, relevant cost or constraint, and protected or sacrificed outcome.",
        "episodes": episodes,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"WROTE {args.output.relative_to(root)}")
    print(f"records={len(episodes)} post_event_status_counts={result['post_event_status_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
