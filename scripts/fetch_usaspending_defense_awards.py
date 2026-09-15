#!/usr/bin/env python3
"""Fetch a bounded USAspending DoD award- or transaction-level sample.

This is an acquisition and visibility layer, not a procurement estimator. It
preserves the exact request and API response so a later pass can add award
type, recipient, place, product/service, and obligation checks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

AWARD_URL = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
TRANSACTION_URL = "https://api.usaspending.gov/api/v2/search/spending_by_transaction/"
AWARD_TYPE_CODES = ["A", "B", "C", "D"]
AWARD_FIELDS = ["Award ID", "Award Amount", "Awarding Agency", "Recipient Name", "Award Type"]
TRANSACTION_FIELDS = ["Award ID", "Transaction Amount", "Awarding Agency", "Recipient Name", "Award Type", "Action Date", "Transaction Description", "naics_code", "product_or_service_code", "pop_state_code"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--end-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--limit", type=int, default=100, choices=range(1, 101))
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--level", choices=("award", "transaction"), default="transaction")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "filters": {
            "time_period": [{"start_date": args.start_date, "end_date": args.end_date}],
            "agencies": [{"type": "awarding", "tier": "toptier", "name": "Department of Defense"}],
            "award_type_codes": AWARD_TYPE_CODES,
        },
        "fields": TRANSACTION_FIELDS if args.level == "transaction" else AWARD_FIELDS,
        "page": args.page,
        "limit": args.limit,
        "subawards": False,
        "order": "desc",
    }
    if args.level == "award":
        payload["order_by"] = "Award Amount"
        endpoint = AWARD_URL
    else:
        payload["sort"] = "Transaction Amount"
        endpoint = TRANSACTION_URL
    request = Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "cultural-geopolitical-theme-mining/1.0"},
        method="POST",
    )
    with urlopen(request, timeout=60) as response:
        raw = response.read()
    parsed = json.loads(raw.decode("utf-8"))
    output = {
        "format": "usaspending-defense-acquisition-v1",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "endpoint": endpoint,
        "level": args.level,
        "request": payload,
        "response_sha256": hashlib.sha256(raw).hexdigest(),
        "response": parsed,
        "boundary": "Bounded API retrieval sample of DoD award or transaction records; not total procurement, delivered capability, production, readiness, supplier concentration, or geopolitical leverage.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "records": len(parsed.get("results", [])), "response_sha256": output["response_sha256"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
