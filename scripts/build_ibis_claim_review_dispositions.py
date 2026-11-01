#!/usr/bin/env python3
"""Record conservative, evidence-backed triage dispositions for IBIS claims."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "ibis-first-review-batch.json"
OUTPUT = ANALYSIS / "ibis-claim-review-dispositions.json"


def main() -> int:
    batch = json.loads(INPUT.read_text())
    target = next(row for row in batch["claims"] if row["review_id"].endswith("drug-and-alcohol-test-kit-manufacturing::test-demand"))
    publisher_counts = {}
    source_type_counts = {}
    for source in target["sources"]:
        publisher_counts[source.get("publisher", "unknown")] = publisher_counts.get(source.get("publisher", "unknown"), 0) + 1
        source_type_counts[source.get("source_type", "unknown")] = source_type_counts.get(source.get("source_type", "unknown"), 0) + 1
    disposition = {
        "review_id": target["review_id"],
        "industry_slug": target["industry_slug"],
        "claim_id": target["claim_id"],
        "claim_text": target["claim_text"],
        "review_scope": "repository_metadata_triage",
        "review_status": "triage_complete_full_review_required",
        "disposition": "held_insufficient_evidence",
        "evidence_checked": {
            "source_count": len(target["sources"]),
            "publisher_counts": publisher_counts,
            "source_type_counts": source_type_counts,
            "missing_published_at_count": sum(source.get("published_at") is None for source in target["sources"]),
            "source_urls": [source.get("url") for source in target["sources"]],
        },
        "independence_finding": "Not established: three of four source rows are Quest Diagnostics material, and the local records do not establish whether those publications share an underlying study, sample, or methodology.",
        "outcome_finding": "Not observed: the artifact lists candidate measures such as test volume, positivity, turnaround, and lab capacity but contains no dated independent outcome series.",
        "rights_finding": "Not verified for the exact artifacts; retain links as evidence locators only.",
        "counter_signal": "The government source describes population substance-use context, while the company sources describe a vendor's testing observations; the populations and denominators are not interchangeable.",
        "next_test": "Recover the exact Quest methodology and sample frame, then acquire an independent dated testing-volume or positivity series with a compatible population and denominator.",
        "company_bridge_status": "blocked_external_first_gate",
        "stop_rule": "Do not count this claim as independent confirmation, use it to qualify the IBIS finding, or connect it to internal company data until the missing lineage, rights, and outcome fields are completed.",
    }
    pending = [row["review_id"] for row in batch["claims"] if row["review_id"] != target["review_id"]]
    payload = {
        "schema": "external-trend-intelligence.ibis-claim-review-dispositions.v1",
        "finding_slug": batch["finding_slug"],
        "source_revision": batch["source_revision"],
        "status": "one_conservative_triage_disposition_recorded",
        "review_method": "metadata-only triage from pinned repository artifacts; not legal rights clearance or independent outcome validation",
        "completed_disposition_count": 1,
        "pending_first_batch_count": len(pending),
        "pending_review_ids": pending,
        "dispositions": [disposition],
        "next_action": disposition["next_test"],
        "boundary": "This artifact records one held triage disposition. It does not qualify the claim, establish source independence, clear rights, validate an outcome, or authorize a company bridge.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} (1 disposition; {len(pending)} first-batch claims pending)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
