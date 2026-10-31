#!/usr/bin/env python3
"""Audit publisher and host lineage for the cross-publisher bounded panel."""

from __future__ import annotations

import json
from urllib.parse import urlparse
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "bounded-subset-lineage-review.json"


def main() -> int:
    snapshot = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())["records"]
    subset = json.loads((ANALYSIS / "bounded-subset-register.json").read_text())["subsets"][1]
    rows = []
    all_hosts = {}
    for record_id in subset["record_ids"]:
        record = snapshot[record_id]["record"]
        urls = sorted({obs.get("source_url") for obs in record.get("observations", []) if obs.get("source_url", "").startswith("http")})
        hosts = sorted({urlparse(url).netloc for url in urls})
        for host in hosts:
            all_hosts.setdefault(host, []).append(record_id)
        rows.append({"record_id": record_id, "source_urls": urls, "source_hosts": hosts})
    shared_hosts = {host: ids for host, ids in all_hosts.items() if len(ids) > 1}
    report = {
        "schema": "external-trend-intelligence.bounded-subset-lineage-review.v1",
        "subset_id": subset["subset_id"],
        "record_count": len(rows),
        "publisher_families": subset["publisher_families"],
        "source_host_count": len(all_hosts),
        "source_hosts": sorted(all_hosts),
        "shared_hosts": shared_hosts,
        "records": rows,
        "independence_status": "partial_independence_review",
        "boundary": "Different publisher families and hosts provide lineage diversity, not proof of independent populations, methods, or outcomes.",
        "next_action": "Review underlying study/data lineage and harmonize case type, denominator, period, and outcome before counting this panel as corroboration.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} records; {len(all_hosts)} hosts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
