#!/usr/bin/env python3
"""Summarize claim-level source quality and independence limits for the IBIS sample."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "ibis-finding-claim-sample.json"
OUTPUT = ANALYSIS / "ibis-claim-source-review.json"


def main() -> int:
    sample = json.loads(INPUT.read_text())
    sources = {}
    claim_count = 0
    linked_source_ids = set()
    claim_types = Counter()
    for industry in sample["samples"]:
        for claim in industry["claims"]:
            claim_count += 1
            claim_types[claim.get("claim_type", "unknown")] += 1
            for source in claim.get("sources", []):
                sources[source["id"]] = source
                linked_source_ids.add(source["id"])

    hosts = Counter()
    publishers = Counter()
    source_types = Counter()
    missing_published_at = 0
    local_sources = 0
    for source in sources.values():
        url = source.get("url", "")
        parsed = urlparse(url)
        if parsed.netloc:
            hosts[parsed.netloc.lower()] += 1
        if source.get("publisher"):
            publishers[source["publisher"]] += 1
        source_types[source.get("source_type", "unknown")] += 1
        missing_published_at += source.get("published_at") is None
        local_sources += url.startswith("file:")

    payload = {
        "schema": "external-trend-intelligence.ibis-claim-source-review.v1",
        "finding_slug": sample["finding_slug"],
        "source_revision": sample["source_revision"],
        "sample_industry_count": sample["sample_industry_count"],
        "sample_sector_count": sample["sample_sector_count"],
        "claim_count": claim_count,
        "unique_source_count": len(sources),
        "linked_source_id_count": len(linked_source_ids),
        "source_url_count": sum(1 for source in sources.values() if source.get("url")),
        "source_host_count": len(hosts),
        "source_type_counts": dict(sorted(source_types.items())),
        "claim_type_counts": dict(sorted(claim_types.items())),
        "publisher_counts": dict(sorted(publishers.items())),
        "top_source_hosts": hosts.most_common(20),
        "missing_published_at_count": missing_published_at,
        "local_source_count": local_sources,
        "source_inventory_label_count": publishers.get("source inventory", 0),
        "independence_status": "not_qualified",
        "outcome_validation_status": "not_observed_in_traceability_sample",
        "review_findings": [
            "Claim-to-source links are present for the bounded sample.",
            "Source inventory labels do not establish publisher independence or source ownership.",
            "Missing publication dates prevent a complete temporal comparison for the sample.",
            "Industry claim traceability is not the same as an observed outcome series.",
        ],
        "next_actions": [
            "Resolve publisher identity and publication date for each high-leverage source.",
            "Map selected claims to dated cost, access, output, trust, or competitive outcomes.",
            "Deduplicate shared studies and company-sponsored material before counting corroboration.",
            "Retain counterexamples and null outcomes in the next review sample.",
        ],
        "boundary": "This review audits the source links inside a 100-industry IBIS traceability sample. It does not clear rights, establish independent corroboration, validate outcomes, or qualify the finding.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(sources)} unique sources)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
