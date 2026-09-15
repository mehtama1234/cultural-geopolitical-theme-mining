#!/usr/bin/env python3
"""Acquire official USAspending recipient-identifier matches for named subaward recipients."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


OUT = Path("analysis/projects/ai-work-control/data/usaspending-recipient-reconciliation-2026-09-14.json")
ENDPOINT = "https://api.usaspending.gov/api/v2/recipient/"
QUERIES = [
    "BAE SYSTEMS INFORMATION AND ELECTRONIC SYSTEMS INTEGRATION INC.",
    "GENERAL DYNAMICS-OTS, INC.",
]


def main() -> int:
    results = []
    for keyword in QUERIES:
        body = {
            "keyword": keyword,
            "page": 1,
            "limit": 100,
            "award_type": "contracts",
            "sort": "name",
            "order": "asc",
        }
        request = Request(
            ENDPOINT,
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": "cultural-geopolitical-theme-mining/1.0",
            },
        )
        with urlopen(request, timeout=60) as response:
            raw = response.read()
        parsed = json.loads(raw.decode("utf-8"))
        results.append(
            {
                "keyword": keyword,
                "request": body,
                "response_sha256": hashlib.sha256(raw).hexdigest(),
                "response": parsed,
            }
        )
    output = {
        "format": "usaspending-recipient-reconciliation-v1",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "endpoint": ENDPOINT,
        "queries": results,
        "boundary": (
            "Official USAspending recipient search responses for two reported subaward names; "
            "the results expose possible recipient identifiers and aggregate endpoint values, "
            "but do not join a named subaward row to a specific UEI/CAGE, facility, work package, "
            "production event, or delivery."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUT), "queries": len(results)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
