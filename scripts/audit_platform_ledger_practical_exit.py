#!/usr/bin/env python3
"""Audit an existing platform-remedy ledger against the practical-exit contract.

This is a field-coverage audit. It deliberately does not turn case-level
remedy records into practical-exit observations when alternatives, costs,
follow-up, or same-unit outcomes are absent.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def status_for(record: dict) -> str:
    correction = record["stages"].get("correction_restoration", "")
    if "reactivation_ordered" in correction or "access_resumed" in correction:
        return "access_restored"
    return "unknown"


def audit_record(record: dict) -> dict:
    stages = record["stages"]
    return {
        "source_id": record["id"],
        "unit": "case",
        "domain": "platform_work",
        "geography": record["place"],
        "trigger": {"value": ", ".join(record["decision_surface"]), "evidence_status": "observed"},
        "threatened_resource": {"value": "platform access, work opportunity, or remuneration", "evidence_status": "inferred"},
        "alternatives": {"value": "unknown", "evidence_status": "unknown"},
        "attempted_route": {"value": record["worker_route"], "evidence_status": "observed"},
        "effort": {"value": "unknown", "evidence_status": "unknown"},
        "decision": {"value": record.get("implementation_stage", "not separately coded; see boundary"), "evidence_status": "observed"},
        "remedy_verification": {
            "value": {
                "correction_or_restoration": stages.get("correction_restoration", "unknown"),
                "payment_compensation": stages.get("payment_compensation", "unknown"),
                "receipt_verified": "unknown",
                "durability": "unknown",
            },
            "evidence_status": "observed" if stages.get("correction_restoration") != "not_observed" else "unknown",
        },
        "followup_window": {"value": "not specified in source ledger", "evidence_status": "unknown"},
        "post_event_status": status_for(record),
        "protected_outcome": {"value": "unknown", "evidence_status": "unknown"},
        "sacrificed_outcome": {"value": "unknown", "evidence_status": "unknown"},
        "meaning_and_action": {"value": "unknown", "evidence_status": "unknown"},
        "counterexample": {"value": "not defined within this ledger", "evidence_status": "open"},
        "denominator": {"value": "27 source-ledger records; not a representative sample", "evidence_status": "observed"},
        "missingness": ["alternatives", "costs_and_constraints", "effort", "receipt", "durability", "followup", "same_unit_post_event_outcome"],
        "source_and_uncertainty": {"value": record["source_type"], "boundary": record["boundary"]},
        "evidence_status": "observed",
        "source_implementation_stage": record.get("implementation_stage", "not recorded"),
    }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=root / "analysis/projects/ai-work-control/data/platform-remedy-case-ledger-v1.json")
    parser.add_argument("--output", type=Path, default=root / "analysis/projects/us-customer-automation-recourse/practical-exit-platform-ledger-dry-run-v1.json")
    args = parser.parse_args()
    data = json.loads(args.ledger.read_text(encoding="utf-8"))
    audits = [audit_record(record) for record in data["records"]]
    counts = Counter(row["post_event_status"] for row in audits)
    result = {
        "format": "practical-exit-platform-ledger-dry-run-v1",
        "status": "coverage_audit_only",
        "checked": "2026-09-16",
        "source_ledger": str(args.ledger.relative_to(root)),
        "contract": "practical-exit-observation-contract-v1",
        "source_record_count": len(audits),
        "post_event_status_counts": dict(sorted(counts.items())),
        "promotion_rule_result": "No practical_exit labels are assigned: the source ledger does not document a same-unit post-event exit plus a documented alternative, relevant cost or constraint, and protected or sacrificed outcome.",
        "episodes": audits,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"WROTE {args.output.relative_to(root)}")
    print(f"records={len(audits)} status_counts={dict(sorted(counts.items()))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
