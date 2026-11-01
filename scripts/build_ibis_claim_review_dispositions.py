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
    def summarize(target: dict, *, disposition: str, independence_finding: str, outcome_finding: str, counter_signal: str, next_test: str) -> dict:
        publisher_counts = {}
        source_type_counts = {}
        for source in target["sources"]:
            publisher_counts[source.get("publisher", "unknown")] = publisher_counts.get(source.get("publisher", "unknown"), 0) + 1
            source_type_counts[source.get("source_type", "unknown")] = source_type_counts.get(source.get("source_type", "unknown"), 0) + 1
        return {
        "review_id": target["review_id"],
        "industry_slug": target["industry_slug"],
        "claim_id": target["claim_id"],
        "claim_text": target["claim_text"],
        "review_scope": "repository_metadata_triage",
        "review_status": "triage_complete_full_review_required",
        "disposition": disposition,
        "evidence_checked": {
            "source_count": len(target["sources"]),
            "publisher_counts": publisher_counts,
            "source_type_counts": source_type_counts,
            "missing_published_at_count": sum(source.get("published_at") is None for source in target["sources"]),
            "source_urls": [source.get("url") for source in target["sources"]],
        },
        "independence_finding": independence_finding,
        "outcome_finding": outcome_finding,
        "rights_finding": "Not verified for the exact artifacts; retain links as evidence locators only.",
        "counter_signal": counter_signal,
        "next_test": next_test,
        "company_bridge_status": "blocked_external_first_gate",
        "stop_rule": "Do not count this claim as independent confirmation, use it to qualify the IBIS finding, or connect it to internal company data until the missing lineage, rights, and outcome fields are completed.",
        }
    target = next(row for row in batch["claims"] if row["review_id"].endswith("drug-and-alcohol-test-kit-manufacturing::test-demand"))
    repair = next(row for row in batch["claims"] if row["review_id"].endswith("cell-phone-repair::repair-policy"))
    dispositions = [
        summarize(
            target,
            disposition="held_insufficient_evidence",
            independence_finding="Not established: three of four source rows are Quest Diagnostics material, and the local records do not establish whether those publications share an underlying study, sample, or methodology.",
            outcome_finding="Not observed: the artifact lists candidate measures such as test volume, positivity, turnaround, and lab capacity but contains no dated independent outcome series.",
            counter_signal="The government source describes population substance-use context, while the company sources describe a vendor's testing observations; the populations and denominators are not interchangeable.",
            next_test="Recover the exact Quest methodology and sample frame, then acquire an independent dated testing-volume or positivity series with a compatible population and denominator.",
        ),
        summarize(
            repair,
            disposition="held_outcome_missing",
            independence_finding="Provisional source diversity only: New York Attorney General and Colorado General Assembly are distinct government publishers and URLs, with no shared host in the pinned metadata. This is not yet a verified independent comparison because publication dates and underlying policy-document lineage remain unresolved.",
            outcome_finding="Not observed: state policy materials establish legal or program context but do not provide a comparable repair-volume, repair-versus-replace, e-waste, or device-life outcome series.",
            counter_signal="Two state policy examples may not represent national policy adoption or consumer behavior; states differ in implementation, coverage, and effective dates.",
            next_test="Verify the enacted-law versions and effective dates, then acquire a dated independent outcome series with a defined device population and denominator (repair volume, repair rate, device age, or e-waste).",
        ),
    ]
    disposition_ids = {row["review_id"] for row in dispositions}
    pending = [row["review_id"] for row in batch["claims"] if row["review_id"] not in disposition_ids]
    payload = {
        "schema": "external-trend-intelligence.ibis-claim-review-dispositions.v1",
        "finding_slug": batch["finding_slug"],
        "source_revision": batch["source_revision"],
        "status": "two_conservative_triage_dispositions_recorded",
        "review_method": "metadata-only triage from pinned repository artifacts; not legal rights clearance or independent outcome validation",
        "completed_disposition_count": len(dispositions),
        "pending_first_batch_count": len(pending),
        "pending_review_ids": pending,
        "dispositions": dispositions,
        "next_action": "Complete the remaining first-batch reviews, then acquire dated independent outcomes for claims that survive metadata triage.",
        "boundary": "This artifact records two held triage dispositions. It does not qualify either claim, establish source independence, clear rights, validate an outcome, or authorize a company bridge.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(dispositions)} dispositions; {len(pending)} first-batch claims pending)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
