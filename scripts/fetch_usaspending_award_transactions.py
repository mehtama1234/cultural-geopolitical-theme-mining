#!/usr/bin/env python3
"""Fetch and persist the transaction history for one USAspending award."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

BASE_URL = "https://api.usaspending.gov/api/v2/search/spending_by_transaction/"
FIELDS = ["Award ID", "Transaction Amount", "Action Date", "Transaction Description", "Mod", "Award Type"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--award-id", required=True, help="PIID/Award ID, e.g. FA868224CB001")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "filters": {"award_ids": [args.award_id], "award_type_codes": ["A", "B", "C", "D"]},
        "fields": FIELDS, "page": 1, "limit": 100, "subawards": False,
        "sort": "Action Date", "order": "asc",
    }
    request = Request(BASE_URL, data=json.dumps(payload).encode("utf-8"),
                      headers={"Content-Type": "application/json", "User-Agent": "cultural-geopolitical-theme-mining/1.0"}, method="POST")
    with urlopen(request, timeout=60) as response:
        raw = response.read()
    parsed = json.loads(raw.decode("utf-8"))
    output = {
        "format": "usaspending-award-transaction-history-v1",
        "retrieved_at": datetime.now(timezone.utc).isoformat(), "endpoint": BASE_URL,
        "request": payload, "response_sha256": hashlib.sha256(raw).hexdigest(),
        "response": parsed,
        "boundary": "One award transaction history from USAspending; not delivered capability, production, readiness, supplier market share, local benefit, or geopolitical leverage.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "records": len(parsed.get("results", [])), "response_sha256": output["response_sha256"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
