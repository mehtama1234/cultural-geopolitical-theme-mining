#!/usr/bin/env python3
"""Acquire identifier and location fields for one award's subawards."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


ENDPOINT = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
OUT = Path("analysis/projects/ai-work-control/data/usaspending-jassm-lrasm-rich-subaward-search-2026-09-14.json")
PAYLOAD = {
    "filters": {"award_type_codes": ["A", "B", "C", "D"], "keywords": ["FA868224CB001"]},
    "fields": [
        "Prime Award ID",
        "Prime Award Recipient UEI",
        "Prime Recipient Name",
        "Sub-Award Amount",
        "Sub-Award Date",
        "Sub-Award Description",
        "Sub-Award ID",
        "Sub-Award Primary Place of Performance",
        "sub_award_recipient_id",
        "Sub-Award Type",
        "Sub-Awardee Name",
        "Sub-Recipient Location",
        "Sub-Recipient UEI",
    ],
    "page": 1,
    "limit": 100,
    "subawards": True,
    "sort": "Sub-Award Date",
    "order": "asc",
}


def main() -> int:
    request = Request(
        ENDPOINT,
        data=json.dumps(PAYLOAD).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "cultural-geopolitical-theme-mining/1.0"},
        method="POST",
    )
    with urlopen(request, timeout=60) as response:
        raw = response.read()
    parsed = json.loads(raw.decode("utf-8"))
    output = {
        "format": "usaspending-rich-subaward-search-v1",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "endpoint": ENDPOINT,
        "request": PAYLOAD,
        "response_sha256": hashlib.sha256(raw).hexdigest(),
        "response": parsed,
        "boundary": (
            "Official USAspending award-search subaward response with subaward UEI and location fields; "
            "recipient location is not necessarily the manufacturing facility, and the response does not "
            "establish production, acceptance, delivery, workforce, replaceability, or geopolitical leverage."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUT), "records": len(parsed.get("results", [])), "response_sha256": output["response_sha256"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
