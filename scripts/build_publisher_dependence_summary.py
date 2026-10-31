#!/usr/bin/env python3
"""Summarize publisher/host overlap across normalized external source maps."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "publisher-dependence-summary.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    source_rows = []
    maps = {
        "ibis": ("ibis-force-claim-map.json", lambda d: [row for force in d["forces"] for row in force["sources"]]),
        "annual_report": ("annual-report-citation-map.json", lambda d: d["rows"]),
        "social": ("social-publication-citation-map.json", lambda d: d["rows"]),
        "inc5000": ("inc5000-opportunity-source-map.json", lambda d: d["rows"] + d["buyer_proxy_rows"]),
    }
    for family, (filename, extractor) in maps.items():
        for row in extractor(load(filename)):
            host = row.get("publisher_host") or row.get("publisher") or "unknown"
            url = row.get("url") or row.get("public_url") or row.get("source_url")
            source_rows.append({"family": family, "host": host, "url": url})
    host_families = defaultdict(set)
    host_urls = defaultdict(set)
    family_counts = Counter()
    for row in source_rows:
        host_families[row["host"]].add(row["family"])
        if row["url"]:
            host_urls[row["host"]].add(row["url"])
        family_counts[row["family"]] += 1
    shared_hosts = {
        host: {
            "families": sorted(families),
            "family_count": len(families),
            "url_count": len(host_urls[host]),
            "dependence_warning": "shared host is not independent confirmation",
        }
        for host, families in sorted(host_families.items())
        if len(families) > 1
    }
    payload = {
        "schema": "external-trend-intelligence.publisher-dependence-summary.v1",
        "purpose": "Cross-family host overlap summary for lineage review; it is not an independence score.",
        "source_maps": {family: filename for family, (filename, _) in maps.items()},
        "source_row_count": len(source_rows),
        "family_row_counts": dict(sorted(family_counts.items())),
        "unique_host_count": len(host_families),
        "shared_host_count": len(shared_hosts),
        "shared_hosts": shared_hosts,
        "family_host_counts": {
            family: len({row["host"] for row in source_rows if row["family"] == family})
            for family in sorted(maps)
        },
        "independence_status": "unverified",
        "boundary": "Host diversity is a lineage diagnostic only. Different URLs on different hosts may restate the same publisher, dataset, company claim, or synthesis; no source is counted as independent confirmation until artifact-level review is complete.",
        "next_test": "Review shared hosts and publisher ownership at claim level, then compare genuinely independent outcome measures with aligned units, periods, populations, and geographies.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(shared_hosts)} shared hosts across {len(maps)} maps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
