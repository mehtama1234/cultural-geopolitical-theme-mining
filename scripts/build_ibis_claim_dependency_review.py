#!/usr/bin/env python3
"""Audit shared source dependence inside the bounded IBIS claim sample."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "ibis-claim-dependency-review.json"


def main() -> int:
    sample = json.loads((ANALYSIS / "ibis-finding-claim-sample.json").read_text())
    source_use: dict[str, dict] = {}
    source_industries: defaultdict[str, set[str]] = defaultdict(set)
    url_industries: defaultdict[str, set[str]] = defaultdict(set)
    publisher_counts = Counter()
    host_counts = Counter()
    claim_count = 0
    for industry in sample["samples"]:
        slug = industry["industry_slug"]
        for claim in industry["claims"]:
            claim_count += 1
            for source in claim.get("sources", []):
                source_id = source.get("id") or f"url:{source.get('url', '')}"
                source_use.setdefault(source_id, source)
                source_industries[source_id].add(slug)
                url = source.get("url")
                if url:
                    url_industries[url].add(slug)
                    parsed = urlparse(url)
                    if parsed.netloc:
                        host_counts[parsed.netloc.lower()] += 1
                publisher = source.get("publisher") or "unknown"
                publisher_counts[publisher] += 1

    shared_sources = [
        {"source_id": sid, "industry_count": len(industries), "industry_slugs": sorted(industries),
         "publisher": source_use[sid].get("publisher"), "url": source_use[sid].get("url")}
        for sid, industries in source_industries.items() if len(industries) > 1
    ]
    shared_urls = [
        {"url": url, "industry_count": len(industries), "industry_slugs": sorted(industries)}
        for url, industries in url_industries.items() if len(industries) > 1
    ]
    missing_metadata = {
        "missing_url": sum(not source.get("url") for source in source_use.values()),
        "missing_publisher": sum(not source.get("publisher") for source in source_use.values()),
        "missing_published_at": sum(source.get("published_at") is None for source in source_use.values()),
        "missing_source_type": sum(not source.get("source_type") for source in source_use.values()),
    }
    report = {
        "schema": "external-trend-intelligence.ibis-claim-dependency-review.v1",
        "finding_slug": sample["finding_slug"],
        "source_revision": sample["source_revision"],
        "sample_industry_count": sample["sample_industry_count"],
        "claim_count": claim_count,
        "unique_source_count": len(source_use),
        "shared_source_id_count": len(shared_sources),
        "shared_url_count": len(shared_urls),
        "shared_source_ids": sorted(shared_sources, key=lambda row: (-row["industry_count"], row["source_id"])),
        "shared_urls": sorted(shared_urls, key=lambda row: (-row["industry_count"], row["url"])),
        "top_publishers_by_claim_link": publisher_counts.most_common(20),
        "top_source_hosts_by_claim_link": host_counts.most_common(20),
        "missing_metadata": missing_metadata,
        "independence_status": "partial_dependency_review",
        "review_findings": [
            "Repeated source IDs or URLs across industries are dependence signals, not independent confirmation.",
            "Publisher concentration is a review priority and is not an independence score.",
            "Missing publication dates prevent complete temporal ordering of claim evidence.",
        ],
        "next_actions": [
            "Resolve shared source IDs to the underlying study, filing, dataset, or company release.",
            "Separate primary observations from secondary summaries before counting corroboration.",
            "Add dated independent outcome measures for selected matched and non-matching industries.",
        ],
        "boundary": f"This artifact audits source reuse inside the {sample['sample_industry_count']}-industry matched sample. It does not establish independent corroboration, causal validity, rights clearance, or trend qualification.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(shared_sources)} shared source IDs; {len(shared_urls)} shared URLs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
