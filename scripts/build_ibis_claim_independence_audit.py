#!/usr/bin/env python3
"""Build a conservative dependency audit for the bounded IBIS claim sample.

The audit exposes repeated URLs, hosts, and publishers before they can be
mistaken for independent corroboration.  It deliberately does not infer
ownership or clear a claim as independent; those remain manual review gates.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "ibis-finding-claim-sample.json"
OUTPUT = ANALYSIS / "ibis-claim-independence-audit.json"


def host(url: str) -> str:
    return urlparse(url).netloc.lower()


def main() -> int:
    sample = json.loads(INPUT.read_text())
    claims = []
    for industry in sample["samples"]:
        for claim in industry["claims"]:
            sources = claim.get("sources", [])
            urls = sorted({source.get("url") for source in sources if source.get("url")})
            hosts = sorted({host(url) for url in urls if host(url)})
            publishers = sorted({source.get("publisher") for source in sources if source.get("publisher")})
            source_types = sorted({source.get("source_type", "unknown") for source in sources})
            claims.append(
                {
                    "industry_slug": industry["industry_slug"],
                    "claim_id": claim.get("claim_id"),
                    "claim_type": claim.get("claim_type"),
                    "source_ids": sorted({source.get("id") for source in sources if source.get("id")}),
                    "source_url_count": len(urls),
                    "source_host_count": len(hosts),
                    "publisher_count": len(publishers),
                    "source_type_count": len(source_types),
                    "source_hosts": hosts,
                    "publishers": publishers,
                    "source_types": source_types,
                    "dependency_flags": [],
                    "independence_status": "pending_manual_review",
                }
            )

    url_claims: dict[str, list[str]] = defaultdict(list)
    host_claims: dict[str, list[str]] = defaultdict(list)
    publisher_claims: dict[str, list[str]] = defaultdict(list)
    for row in claims:
        key = f"{row['industry_slug']}::{row['claim_id']}"
        for source_host in row["source_hosts"]:
            host_claims[source_host].append(key)
        for publisher in row["publishers"]:
            publisher_claims[publisher].append(key)

    # Reconstruct URL counts directly from the source rows so repeated source
    # material is visible across claims as well as within a claim.
    url_to_claims: dict[str, list[str]] = defaultdict(list)
    for industry in sample["samples"]:
        for claim in industry["claims"]:
            key = f"{industry['industry_slug']}::{claim.get('claim_id')}"
            for source in claim.get("sources", []):
                if source.get("url"):
                    url_to_claims[source["url"]].append(key)
    for url, keys in url_to_claims.items():
        url_claims[url].extend(keys)

    repeated_urls = {url: sorted(set(keys)) for url, keys in url_claims.items() if len(set(keys)) > 1}
    repeated_hosts = {name: sorted(set(keys)) for name, keys in host_claims.items() if len(set(keys)) > 1}
    repeated_publishers = {name: sorted(set(keys)) for name, keys in publisher_claims.items() if len(set(keys)) > 1}

    for row in claims:
        key = f"{row['industry_slug']}::{row['claim_id']}"
        if row["source_url_count"] == 0:
            row["dependency_flags"].append("no_public_url")
        if row["source_host_count"] <= 1:
            row["dependency_flags"].append("single_host_within_claim")
        if row["publisher_count"] <= 1:
            row["dependency_flags"].append("single_publisher_within_claim")
        if any(key in keys for keys in repeated_urls.values()):
            row["dependency_flags"].append("url_reused_across_claims")
        if any(key in keys for keys in repeated_hosts.values()):
            row["dependency_flags"].append("host_reused_across_claims")
        if any(key in keys for keys in repeated_publishers.values()):
            row["dependency_flags"].append("publisher_reused_across_claims")
        if row["source_host_count"] >= 2 and row["publisher_count"] >= 2 and not row["dependency_flags"]:
            row["independence_status"] = "candidate_for_manual_review"
        elif row["dependency_flags"]:
            row["independence_status"] = "dependency_warning_pending_review"

    status_counts = Counter(row["independence_status"] for row in claims)
    flag_counts = Counter(flag for row in claims for flag in row["dependency_flags"])
    payload = {
        "schema": "external-trend-intelligence.ibis-claim-independence-audit.v1",
        "finding_slug": sample["finding_slug"],
        "source_revision": sample["source_revision"],
        "sample_industry_count": sample["sample_industry_count"],
        "sample_claim_count": len(claims),
        "sample_counterexample_industry_count": sample["counterexample_industry_count"],
        "status": "dependency_audit_complete_independence_unverified",
        "independence_status_counts": dict(sorted(status_counts.items())),
        "dependency_flag_counts": dict(sorted(flag_counts.items())),
        "unique_url_count": len(url_to_claims),
        "reused_url_count": len(repeated_urls),
        "unique_host_count": len(host_claims),
        "reused_host_count": len(repeated_hosts),
        "unique_publisher_count": len(publisher_claims),
        "reused_publisher_count": len(repeated_publishers),
        "reused_urls": {url: keys for url, keys in sorted(repeated_urls.items())},
        "reused_hosts": {name: keys for name, keys in sorted(repeated_hosts.items())},
        "reused_publishers": {name: keys for name, keys in sorted(repeated_publishers.items())},
        "claims": claims,
        "next_action": "Manually verify publisher ownership, study provenance, publication dates, and outcome linkage for candidate claims; retain dependency warnings and do not count repeated hosts or publishers as independent confirmation.",
        "boundary": "This is a mechanical dependency audit of the bounded matched-industry sample. It does not establish that sources are independent, does not clear rights, does not validate outcomes, and does not qualify the IBIS finding.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(claims)} claims; {len(repeated_urls)} reused URLs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
