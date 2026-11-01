#!/usr/bin/env python3
"""Acquire a bounded USAspending transaction snapshot for Bath Iron Works."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "usaspending-bath-iron-works-execution-snapshot.json"
API_URL = "https://api.usaspending.gov/api/v2/search/spending_by_transaction/"
FIELDS = ["Award ID", "Recipient Name", "Action Date", "Transaction Amount", "Awarding Agency", "Awarding Sub Agency", "Transaction Description", "NAICS", "PSC", "Recipient Location"]
FILTERS = {"award_type_codes": ["A", "B", "C", "D"], "time_period": [{"start_date": "2024-10-01", "end_date": "2026-09-30"}], "recipient_search_text": ["BATH IRON WORKS"]}


def main() -> int:
    rows: list[dict] = []
    page = 1
    metadata = []
    while True:
        payload = {"filters": FILTERS, "fields": FIELDS, "page": page, "limit": 100, "subawards": False, "sort": "Action Date", "order": "desc"}
        request = urllib.request.Request(API_URL, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
        result = json.loads(body)
        rows.extend(result.get("results", []))
        metadata.append(result.get("page_metadata", {}))
        if not result.get("page_metadata", {}).get("hasNext"):
            break
        page += 1
        if page > 100:
            raise RuntimeError("USAspending pagination exceeded 100 pages; stop rather than silently truncate")
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    amounts = [float(row.get("Transaction Amount") or 0) for row in rows]
    dates = [row.get("Action Date") for row in rows if row.get("Action Date")]
    payload = {
        "schema": "external-trend-intelligence.usaspending-bath-iron-works-execution-snapshot.v1",
        "status": "official_execution_snapshot_lineage_review_pending",
        "publisher": "USAspending.gov / U.S. Department of the Treasury",
        "source_url": "https://www.usaspending.gov/",
        "api_url": API_URL,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "query": {"filters": FILTERS, "fields": FIELDS, "page_size": 100, "sort": "Action Date", "order": "desc", "spending_level": "transactions"},
        "pagination": {"page_count": len(metadata), "rows": len(rows), "metadata": metadata},
        "rows": rows,
        "summary": {"transaction_count": len(rows), "transaction_amount_sum_usd": sum(amounts), "min_action_date": min(dates) if dates else None, "max_action_date": max(dates) if dates else None, "award_id_count": len({row.get("Award ID") for row in rows})},
        "normalized_rows_sha256": "sha256:" + hashlib.sha256(canonical).hexdigest(),
        "unit_and_denominator": "federal transaction amount in USD per returned USAspending transaction; recipient search is Bath Iron Works text match, not all shipyard activity",
        "uncertainty_and_missingness": "USAspending results reflect reported federal transactions and can include modifications, zero-dollar actions, and deobligations; this snapshot does not estimate total facility utilization or unobserved work.",
        "independence_status": "publisher_distinct_execution_source_lineage_review_pending",
        "rights_boundary": "Retain normalized API observations, query parameters, retrieval timestamp, and hash with USAspending attribution. Do not redistribute bulk downloads or imply that API access is legal clearance for commercial derived products without exact terms review.",
        "counter_signal": "Transaction activity may reflect modifications or administrative actions rather than new workload; contract obligations are not the same as completed maintenance or capacity utilization.",
        "release_decision": "retain_normalized_execution_snapshot_internal_review_only",
        "next_action": "Reconcile transaction descriptions, award identity, fiscal-year aggregation, and facility scope against the Navy budget context before any trend qualification or company bridge.",
        "boundary": "This is a bounded realized-award acquisition, not independent confirmation of the IBIS claim, a causal result, or permission to connect company data.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} transactions across {len(metadata)} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
