#!/usr/bin/env python3
"""Summarize implementation depth in the committed platform remedy ledger."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=root / "analysis/projects/ai-work-control/data/platform-remedy-case-ledger-v1.json")
    parser.add_argument("--output", type=Path, default=root / "analysis/projects/ai-work-control/data/platform-remedy-implementation-depth-audit-v1.json")
    args = parser.parse_args()
    ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    records = ledger["records"]

    def cases(predicate):
        return [{"id": r["id"], "population": r["population"]} for r in records if predicate(r)]

    correction = Counter(r["stages"]["correction_restoration"] for r in records)
    payment = Counter(r["stages"]["payment_compensation"] for r in records)
    result = {
        "format": "platform-remedy-implementation-depth-audit-v1",
        "checked": "2026-09-16",
        "source": "analysis/projects/ai-work-control/data/platform-remedy-case-ledger-v1.json",
        "source_unit": "27 coded platform-remedy case records; not a representative sample",
        "record_count": len(records),
        "stage_counts": {
            "formal_reactivation_or_restoration_order": len(cases(lambda r: "reactivation_ordered" in r["stages"]["correction_restoration"])),
            "access_resumed_without_merits_remedy": len(cases(lambda r: r["stages"]["correction_restoration"] == "observed_access_resumed_not_merits_remedy")),
            "continued_work_after_restoration": len(cases(lambda r: r["stages"]["correction_restoration"] == "observed_adjudicated_reactivation_and_continued_work")),
            "payment_or_lost_earnings_stage_observed": len(cases(lambda r: "observed" in r["stages"]["payment_compensation"])),
            "payment_receipt_verified": 0,
            "durable_access_or_non_retaliation_verified": 0
        },
        "correction_restoration_values": dict(sorted(correction.items())),
        "payment_compensation_values": dict(sorted(payment.items())),
        "named_stage_cases": {
            "formal_reactivation_or_restoration_order": cases(lambda r: "reactivation_ordered" in r["stages"]["correction_restoration"]),
            "access_resumed_without_merits_remedy": cases(lambda r: r["stages"]["correction_restoration"] == "observed_access_resumed_not_merits_remedy"),
            "continued_work_after_restoration": cases(lambda r: r["stages"]["correction_restoration"] == "observed_adjudicated_reactivation_and_continued_work")
        },
        "result": "The ledger observes formal remedy stages more often than lived implementation. It contains orders and one continued-work record, but no verified payment receipt, durable access, or non-retaliation outcome.",
        "boundary": "Stage strings are source-coded evidence labels, not case weights, remedy rates, worker-welfare estimates, or prevalence estimates. An order is not receipt and continued work in one case is not durable recovery.",
        "storage_boundary": "Reads one committed JSON ledger and writes a compact JSON summary; no download or raw-data acquisition."
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"records": len(records), "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
