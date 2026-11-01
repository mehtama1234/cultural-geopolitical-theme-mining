#!/usr/bin/env python3
"""Compare realized USAspending transactions with Navy budget context without pooling them."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "usaspending-bath-iron-works-execution-snapshot.json"
OUTPUT = ANALYSIS / "ibis-dock-defense-execution-comparison.json"


def fiscal_year(date: str) -> str:
    year, month, _ = (int(part) for part in date.split("-"))
    return f"FY{year + 1}" if month >= 10 else f"FY{year}"


def main() -> int:
    snapshot = json.loads(INPUT.read_text())
    by_year = defaultdict(lambda: {"transaction_count": 0, "positive_obligation_usd": 0.0, "negative_obligation_usd": 0.0, "zero_amount_count": 0, "award_ids": set(), "description_terms": defaultdict(int)})
    for row in snapshot["rows"]:
        year = fiscal_year(row["Action Date"])
        amount = float(row.get("Transaction Amount") or 0)
        bucket = by_year[year]
        bucket["transaction_count"] += 1
        bucket["award_ids"].add(row.get("Award ID"))
        if amount > 0:
            bucket["positive_obligation_usd"] += amount
        elif amount < 0:
            bucket["negative_obligation_usd"] += amount
        else:
            bucket["zero_amount_count"] += 1
        text = (row.get("Transaction Description") or "").lower()
        for term in ("maintenance", "alteration", "delivery", "construction", "engineering", "design", "deobligation"):
            if term in text:
                bucket["description_terms"][term] += 1
    rows = []
    for year in sorted(by_year):
        bucket = by_year[year]
        rows.append({"period": year, "measure": "transaction_obligations", "transaction_count": bucket["transaction_count"], "award_id_count": len(bucket["award_ids"]), "positive_obligation_usd": round(bucket["positive_obligation_usd"], 2), "negative_obligation_usd": round(bucket["negative_obligation_usd"], 2), "zero_amount_count": bucket["zero_amount_count"], "description_terms": dict(bucket["description_terms"])})
    payload = {
        "schema": "external-trend-intelligence.ibis-dock-defense-execution-comparison.v1",
        "status": "non_pooled_execution_context_comparison",
        "source_artifacts": ["usaspending-bath-iron-works-execution-snapshot.json", "ibis-dock-defense-outcome-review.json"],
        "rows": rows,
        "interpretation": "USAspending transaction obligations provide a realized-award context for one named recipient and fiscal-year window. They are shown beside, not pooled with, Navy budget-request measures.",
        "comparability_limits": ["Transaction amounts are obligations/actions, not completed maintenance or utilization.", "Bath Iron Works text matching is not all Navy shipyard activity.", "Budget request dollars and transaction obligations use different constructs and cannot be subtracted or treated as a conversion rate.", "Zero-dollar actions and deobligations remain visible rather than silently removed."],
        "counter_signal": "A high transaction total can reflect modifications, advance funding, or administrative actions without equivalent completed work; a low total can reflect timing or reporting lag.",
        "release_decision": "internal_review_only_no_pooling",
        "next_action": "Reconcile award-level identity and fiscal-year coverage with Navy execution milestones before any trend qualification or company decision use.",
        "boundary": "This comparison is descriptive evidence for lineage review. It does not validate the IBIS claim, establish causality, or authorize an internal company bridge.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} fiscal-year rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
