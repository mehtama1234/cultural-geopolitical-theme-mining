#!/usr/bin/env python3
"""Build a bounded claim/source traceability sample for one IBIS finding."""

from __future__ import annotations

import json
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "ibis-finding-claim-sample.json"
REPO = "/home/mehta/git-repo/ibis-industries"
REVISION = "b895acd021fbe3dc1d610255952b1373748e3bc3"
PATTERN_PATH = "cross_industry_pattern_inventory.json"
SAMPLE_SIZE = 100


def show(path: str) -> str:
    return subprocess.check_output(["git", "-C", REPO, "show", f"{REVISION}:{path}"], text=True)


def main() -> int:
    inventory = json.loads(show(PATTERN_PATH))
    pattern = next(item for item in inventory["ranked_patterns"] if item["slug"] == "compliance-as-economic-architecture")
    # Select a deterministic, sector-covered sample rather than taking the
    # first alphabetical records, which over-represents a few sectors.
    matched = []
    for slug in sorted(pattern["matched_industries"]):
        record = json.loads(show(f"business_knowledge_examples/{slug}.json"))
        matched.append((record["identity"].get("sector", "Unknown"), slug))
    by_sector = {}
    for sector, slug in matched:
        by_sector.setdefault(sector, []).append(slug)
    industries = []
    for sector in sorted(by_sector):
        industries.append(by_sector[sector][0])
    remaining = [slug for _, slug in matched if slug not in set(industries)]
    industries.extend(remaining[: max(0, SAMPLE_SIZE - len(industries))])
    industries = industries[:SAMPLE_SIZE]
    samples = []
    for slug in industries:
        record = json.loads(show(f"business_knowledge_examples/{slug}.json"))
        claims = []
        for claim in record.get("evidence", {}).get("claims", [])[:3]:
            source_ids = claim.get("source_ids", [])
            sources = [source for source in record.get("evidence", {}).get("sources", []) if source.get("id") in source_ids]
            claims.append(
                {
                    "claim_id": claim.get("id"),
                    "claim_text": claim.get("text"),
                    "claim_type": claim.get("claim_type"),
                    "source_ids": source_ids,
                    "sources": sources,
                }
            )
        samples.append(
            {
                "industry_slug": slug,
                "industry_title": record["identity"]["title"],
                "industry_sector": record["identity"].get("sector", "Unknown"),
                "geography": record["identity"]["geography"],
                "as_of": record["scope"]["as_of"],
                "claims": claims,
                "outcome_measure_candidates": sorted({
                    signal
                    for force in record.get("forces", [])
                    for signal in force.get("signals_to_watch", [])
                }),
                "record_falsifiers": record.get("judgment", {}).get("falsifiers", []),
            }
        )
    payload = {
        "schema": "external-trend-intelligence.ibis-finding-claim-sample.v1",
        "finding_slug": pattern["slug"],
        "finding_title": pattern["title"],
        "source_revision": REVISION,
        "sample_status": "bounded_traceability_sample",
        "sampling_method": "one_record_per_observed_sector_then_sorted_fill",
        "sample_industry_count": len(samples),
        "sample_sector_count": len({sample["industry_sector"] for sample in samples}),
        "sample_sector_counts": dict(sorted(Counter(sample["industry_sector"] for sample in samples).items())),
        "counter_signals": pattern["counterforces"],
        "outcome_measure_candidate_count": sum(len(sample["outcome_measure_candidates"]) for sample in samples),
        "sample_source_urls": sorted({
            source["url"]
            for sample in samples
            for claim in sample["claims"]
            for source in claim["sources"]
            if source.get("url")
        }),
        "samples": samples,
        "boundary": "This bounded sample traces 100 matched industries across the observed sectors to claim-level source IDs and URLs. It does not validate the full finding, establish causality, or represent all 1,161 matched industries.",
        "next_test": "Expand the same traceability method across a pre-specified industry sample, add counterexamples and outcomes, and review publisher independence before promotion.",
    }
    payload["sample_source_url_count"] = len(payload["sample_source_urls"])
    payload["sample_source_host_count"] = len({urlparse(url).netloc.lower() for url in payload["sample_source_urls"] if urlparse(url).netloc})
    url_counts = Counter(payload["sample_source_urls"])
    payload["duplicate_source_urls"] = {url: count for url, count in url_counts.items() if count > 1}
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(samples)} industries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
