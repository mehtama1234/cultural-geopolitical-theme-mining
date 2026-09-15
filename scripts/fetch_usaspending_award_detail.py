#!/usr/bin/env python3
"""Persist one USAspending award-detail response for case-level audit."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

BASE_URL = "https://api.usaspending.gov/api/v2/awards/"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--award-id", required=True, help="USAspending generated_unique_award_id")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    endpoint = BASE_URL + args.award_id + "/"
    request = Request(endpoint, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    with urlopen(request, timeout=60) as response:
        raw = response.read()
    parsed = json.loads(raw.decode("utf-8"))
    output = {
        "format": "usaspending-award-detail-acquisition-v1",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "endpoint": endpoint,
        "award_id": args.award_id,
        "response_sha256": hashlib.sha256(raw).hexdigest(),
        "response": parsed,
        "boundary": "One USAspending award-detail response; not delivered capability, production, readiness, supplier market share, local benefit, or geopolitical leverage.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "response_sha256": output["response_sha256"], "award_id": parsed.get("piid")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
