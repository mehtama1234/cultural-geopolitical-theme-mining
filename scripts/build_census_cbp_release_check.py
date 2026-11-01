#!/usr/bin/env python3
"""Check whether the next official Census CBP release is available."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
SNAPSHOT = ANALYSIS / "census-repair-industry-snapshot.json"
OUTPUT = ANALYSIS / "census-cbp-release-check.json"


def probe(url: str) -> dict:
    request = Request(url, method="HEAD", headers={"User-Agent": "external-observatory-release-check/1.0"})
    try:
        with urlopen(request, timeout=30) as response:
            return {"url": url, "http_status": response.status, "availability": "available"}
    except HTTPError as exc:
        return {"url": url, "http_status": exc.code, "availability": "not_published" if exc.code == 404 else "unavailable"}
    except URLError as exc:
        return {"url": url, "http_status": None, "availability": "check_failed", "error": str(exc.reason)}


def main() -> int:
    snapshot = json.loads(SNAPSHOT.read_text())
    latest = max(int(row["year"]) for row in snapshot["source"]["retrievals"])
    target = latest + 1
    suffix = str(target)[2:]
    urls = {
        "us": f"https://www2.census.gov/programs-surveys/cbp/datasets/{target}/cbp{suffix}us.zip",
        "state": f"https://www2.census.gov/programs-surveys/cbp/datasets/{target}/cbp{suffix}st.zip",
    }
    checks = [{"geography": geography, **probe(url)} for geography, url in urls.items()]
    available = all(check["availability"] == "available" for check in checks)
    payload = {
        "schema": "external-trend-intelligence.census-cbp-release-check.v1",
        "publisher": "U.S. Census Bureau",
        "dataset": "County Business Patterns",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "latest_pinned_year": latest,
        "target_year": target,
        "checks": checks,
        "status": "target_release_available" if available else "target_not_published_or_unavailable",
        "next_action": "Acquire both official national and state files and record checksums before replacing the pinned snapshot." if available else "Retain the current pinned snapshot and recheck the exact official URLs at the next scheduled refresh; do not infer a zero or a missing observation from an unavailable release.",
        "boundary": "An HTTP availability check is not data acquisition, rights clearance, or evidence about the repair industry. A 404 means the target was not published at this URL when checked.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} (target {target}; {payload['status']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
