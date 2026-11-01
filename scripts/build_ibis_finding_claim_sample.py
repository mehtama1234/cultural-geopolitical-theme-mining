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
SAMPLE_SIZE = 500
COUNTEREXAMPLE_SIZE = 100


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
    matched_slugs = {slug for _, slug in matched}
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
        outcome_measure_candidates = sorted({
            signal
            for force in record.get("forces", [])
            for signal in force.get("signals_to_watch", [])
        })
        claims = []
        for claim in record.get("evidence", {}).get("claims", [])[:3]:
            source_ids = claim.get("source_ids", [])
            sources = [source for source in record.get("evidence", {}).get("sources", []) if source.get("id") in source_ids]
            has_url = bool(sources) and all(source.get("url") for source in sources)
            has_publisher = bool(sources) and all(source.get("publisher") and source.get("publisher") != "source inventory" for source in sources)
            has_time = bool(claim.get("period")) or any(source.get("published_at") for source in sources)
            claims.append(
                {
                    "claim_id": claim.get("id"),
                    "claim_text": claim.get("text"),
                    "claim_type": claim.get("claim_type"),
                    "source_ids": source_ids,
                    "sources": sources,
                    "review": {
                        "source_identity": "pass" if source_ids and sources else "fail",
                        "url_locator": "pass" if has_url else "fail",
                        "publisher_identity": "pass" if has_publisher else "fail",
                        "temporal_metadata": "pass" if has_time else "fail",
                        "source_type": "pass" if sources and all(source.get("source_type") for source in sources) else "fail",
                        "outcome_linkage": "candidate_available" if outcome_measure_candidates else "missing",
                        "independence": "pending_claim_level_review",
                    },
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
                "outcome_measure_candidates": outcome_measure_candidates,
                "record_falsifiers": record.get("judgment", {}).get("falsifiers", []),
            }
        )

    # Keep a deterministic set of industries that were not matched to the
    # finding.  These are comparator/counterexample candidates, not proof that
    # compliance has no effect: the pattern engine's matching rule may simply
    # have failed to clear its threshold for that industry.  One record per
    # observed sector is retained before filling the remaining slots so the
    # comparison does not over-represent one part of the corpus.
    all_paths = subprocess.check_output(
        ["git", "-C", REPO, "ls-tree", "-r", "--name-only", REVISION, "business_knowledge_examples"],
        text=True,
    ).splitlines()
    unmatched = []
    for path in all_paths:
        slug = Path(path).stem
        if slug in matched_slugs:
            continue
        record = json.loads(show(path))
        unmatched.append((record["identity"].get("sector", "Unknown"), slug, record))
    by_sector_unmatched = {}
    for sector, slug, record in unmatched:
        by_sector_unmatched.setdefault(sector, []).append((slug, record))
    counterexample_records = []
    for sector in sorted(by_sector_unmatched):
        slug, record = by_sector_unmatched[sector][0]
        counterexample_records.append((sector, slug, record))
    selected = {(sector, slug) for sector, slug, _ in counterexample_records}
    for sector, slug, record in unmatched:
        if len(counterexample_records) >= COUNTEREXAMPLE_SIZE:
            break
        if (sector, slug) not in selected:
            counterexample_records.append((sector, slug, record))
            selected.add((sector, slug))
    counterexamples = []
    for sector, slug, record in counterexample_records[:COUNTEREXAMPLE_SIZE]:
        claims = []
        outcome_measure_candidates = sorted({
            signal
            for force in record.get("forces", [])
            for signal in force.get("signals_to_watch", [])
        })
        for claim in record.get("evidence", {}).get("claims", [])[:2]:
            source_ids = claim.get("source_ids", [])
            sources = [source for source in record.get("evidence", {}).get("sources", []) if source.get("id") in source_ids]
            has_url = bool(sources) and all(source.get("url") for source in sources)
            has_publisher = bool(sources) and all(source.get("publisher") and source.get("publisher") != "source inventory" for source in sources)
            has_time = bool(claim.get("period")) or any(source.get("published_at") for source in sources)
            claims.append({
                "claim_id": claim.get("id"),
                "claim_text": claim.get("text"),
                "claim_type": claim.get("claim_type"),
                "source_ids": source_ids,
                "sources": sources,
                "review": {
                    "source_identity": "pass" if source_ids and sources else "fail",
                    "url_locator": "pass" if has_url else "fail",
                    "publisher_identity": "pass" if has_publisher else "fail",
                    "temporal_metadata": "pass" if has_time else "fail",
                    "source_type": "pass" if sources and all(source.get("source_type") for source in sources) else "fail",
                    "outcome_linkage": "candidate_available" if outcome_measure_candidates else "missing",
                    "independence": "pending_claim_level_review",
                },
            })
        counterexamples.append({
            "industry_slug": slug,
            "industry_title": record["identity"]["title"],
            "industry_sector": sector,
            "geography": record["identity"].get("geography"),
            "as_of": record.get("scope", {}).get("as_of"),
            "pattern_match": False,
            "comparison_role": "non_matching_comparator",
            "claims": claims,
            "record_falsifiers": record.get("judgment", {}).get("falsifiers", []),
        })

    source_rows = [
        source
        for sample in samples + counterexamples
        for claim in sample["claims"]
        for source in claim["sources"]
    ]
    publisher_counts = Counter(source.get("publisher", "unknown") for source in source_rows)
    source_type_counts = Counter(source.get("source_type", "unknown") for source in source_rows)
    claim_rows = [
        {"industry_slug": sample["industry_slug"], "claim_id": claim["claim_id"], "review": claim["review"]}
        for sample in samples
        for claim in sample["claims"]
    ]
    review_summary = {
        "claim_count": len(claim_rows),
        "source_identity_pass_count": sum(row["review"]["source_identity"] == "pass" for row in claim_rows),
        "url_locator_pass_count": sum(row["review"]["url_locator"] == "pass" for row in claim_rows),
        "publisher_identity_pass_count": sum(row["review"]["publisher_identity"] == "pass" for row in claim_rows),
        "temporal_metadata_pass_count": sum(row["review"]["temporal_metadata"] == "pass" for row in claim_rows),
        "source_type_pass_count": sum(row["review"]["source_type"] == "pass" for row in claim_rows),
        "outcome_linkage_candidate_count": sum(row["review"]["outcome_linkage"] == "candidate_available" for row in claim_rows),
        "independence_pending_count": sum(row["review"]["independence"] == "pending_claim_level_review" for row in claim_rows),
        "review_rows": claim_rows,
    }
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
        "counterexample_industry_count": len(counterexamples),
        "counterexample_sector_count": len({sample["industry_sector"] for sample in counterexamples}),
        "counterexample_sector_counts": dict(sorted(Counter(sample["industry_sector"] for sample in counterexamples).items())),
        "counterexample_selection": "one non-matching industry per observed sector, then sorted fill",
        "source_publisher_counts_in_sample": dict(sorted(publisher_counts.items())),
        "source_type_counts_in_sample": dict(sorted(source_type_counts.items())),
        "claim_review_summary": review_summary,
        "sample_source_urls": sorted({
            source["url"]
            for sample in samples
            for claim in sample["claims"]
            for source in claim["sources"]
            if source.get("url")
        }),
        "samples": samples,
        "counterexamples": counterexamples,
        "boundary": f"This bounded sample traces {len(samples)} matched industries and {len(counterexamples)} non-matching comparator industries to claim-level source IDs and URLs. Non-matching records are counterexample candidates, not proof that compliance has no effect. The artifact does not validate the full finding, establish causality, or represent all 1,161 matched industries and 330 non-matching industries.",
        "next_test": "Review the comparator industries against an independent outcome measure, verify claim-level publisher independence, and expand coverage before promotion.",
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
