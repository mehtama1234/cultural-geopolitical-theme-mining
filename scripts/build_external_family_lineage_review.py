#!/usr/bin/env python3
"""Audit source URL coverage and independence risks for normalized family observations."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "external-family-lineage-review.json"


def main() -> int:
    observations = json.loads((ANALYSIS / "external-family-observations.json").read_text())["observations"]
    url_to_observations = {}
    host_to_observations = {}
    for observation in observations:
        observation_id = observation["observation_id"]
        for url in set(observation.get("source_urls", [])):
            url_to_observations.setdefault(url, set()).add(observation_id)
            host = urlparse(url).netloc.lower()
            if host:
                host_to_observations.setdefault(host, set()).add(observation_id)
    cross_observation_urls = {
        url: sorted(observation_ids)
        for url, observation_ids in sorted(url_to_observations.items())
        if len(observation_ids) > 1
    }
    cross_observation_hosts = {
        host: sorted(observation_ids)
        for host, observation_ids in sorted(host_to_observations.items())
        if len(observation_ids) > 1
    }
    reviews = []
    for observation in observations:
        urls = observation.get("source_urls", [])
        url_counts = Counter(urls)
        hosts = sorted({urlparse(url).netloc.lower() for url in urls if urlparse(url).netloc})
        duplicate_urls = {url: count for url, count in url_counts.items() if count > 1}
        if observation["observation_id"].endswith("source-linked-share"):
            remaining = [
                "publisher and artifact identity review for each URL",
                "check whether URLs repeat the same company claim or underlying source",
                "independent population-level or outcome measure",
            ]
            status = "partial"
        elif observation.get("source_url_status") == "inventory_present":
            remaining = [
                "map inventory sources to the specific observation or finding",
                "unit, geography, period, and denominator audit",
                "independence review against the synthesis source",
            ]
            status = "partial"
        else:
            remaining = [
                "source URLs or filing identities for the underlying records",
                "unit, geography, period, and denominator audit",
                "independence review against the synthesis source",
            ]
            status = "not_started"
        reviews.append(
            {
                "observation_id": observation["observation_id"],
                "status": status,
                "source_url_count": len(urls),
                "source_host_count": len(hosts),
                "source_hosts": hosts,
                "duplicate_source_urls": duplicate_urls,
                "cross_observation_shared_urls": sorted(
                    url for url, observation_ids in cross_observation_urls.items() if observation["observation_id"] in observation_ids
                ),
                "cross_observation_shared_hosts": sorted(
                    host for host, observation_ids in cross_observation_hosts.items() if observation["observation_id"] in observation_ids
                ),
                "denominator": observation.get("denominator"),
                "source_url_status": observation["source_url_status"],
                "independence_status": "unverified",
                "remaining": remaining,
                "promotion_decision": "hold",
            }
        )
    payload = {
        "schema": "external-trend-intelligence.external-family-lineage-review.v1",
        "purpose": "Lineage and independence review for the first normalized external-family intake.",
        "promotion_rule": "URL count and host diversity are coverage measures, not independent confirmation.",
        "cross_observation_url_overlap": cross_observation_urls,
        "cross_observation_host_overlap": cross_observation_hosts,
        "reviews": reviews,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(reviews)} reviews)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
