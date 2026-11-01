#!/usr/bin/env python3
"""Build a fail-closed queue for acquiring independent outcomes for IBIS claims."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "ibis-claim-independence-review-queue.json"
OUTPUT = ANALYSIS / "ibis-outcome-acquisition-queue.json"


def priority(row: dict) -> tuple[int, int, int, str]:
    """Prefer claims with an explicit outcome candidate and diverse source hosts."""
    outcomes = len(row.get("outcome_measure_candidates", []))
    hosts = row.get("independence_candidate_basis", {}).get("source_host_count", 0)
    high = row.get("priority") == "high"
    return (0 if outcomes else 1, 0 if high else 1, -hosts, row["review_id"])


def main() -> int:
    queue = json.loads(INPUT.read_text())
    rows = []
    for rank, row in enumerate(sorted(queue["candidates"], key=priority), start=1):
        outcome_candidates = row.get("outcome_measure_candidates", [])
        rows.append(
            {
                "acquisition_rank": rank,
                "review_id": row["review_id"],
                "industry_slug": row["industry_slug"],
                "industry_sector": row.get("industry_sector"),
                "claim_id": row["claim_id"],
                "claim_text": row.get("claim_text"),
                "claim_type": row["claim_type"],
                "geography": row.get("geography"),
                "claim_as_of": row.get("as_of"),
                "source_review_status": row["review_status"],
                "outcome_measure_candidates": outcome_candidates,
                "outcome_candidate_count": len(outcome_candidates),
                "acquisition_status": "candidate_outcome_not_acquired",
                "required_fields": [
                    "canonical publisher and exact artifact",
                    "outcome definition, unit, denominator, population, geography, and period",
                    "release or observation date and retrieval checksum",
                    "uncertainty, suppression, missingness, and methodology notes",
                    "rights and permitted storage/transformation/redistribution",
                    "independence and upstream-lineage disposition against the IBIS claim",
                ],
                "stop_rule": "Do not use the outcome as independent confirmation or promote the claim until the source review and outcome fields are complete.",
                "next_action": "Select one candidate outcome, acquire the official artifact, preserve its metadata and checksum, and reconcile its unit and period with the claim.",
            }
        )

    payload = {
        "schema": "external-trend-intelligence.ibis-outcome-acquisition-queue.v1",
        "finding_slug": queue["finding_slug"],
        "source_revision": queue["source_revision"],
        "status": "outcome_acquisition_queue_ready",
        "candidate_count": len(rows),
        "with_outcome_candidate_count": sum(bool(row["outcome_candidate_count"]) for row in rows),
        "unacquired_count": len(rows),
        "selection_rule": "rank claims with named outcome candidates first, then high-priority claims and source-host diversity; retain all rows as unacquired until an official artifact is reviewed",
        "review_owner_role": "evidence analyst with lineage reviewer support",
        "promotion_boundary": "An outcome candidate is a discovery lead, not an observation. No claim is promoted or bridged to company data from this queue alone.",
        "next_action": "Assign the top-ranked candidates, acquire official outcome artifacts, and complete the required fields before any IBIS finding promotion.",
        "boundary": "This queue converts claim-level review into a concrete acquisition workflow. It does not establish independence, validate outcomes, clear rights, or authorize a company bridge.",
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates; {payload['with_outcome_candidate_count']} with outcome leads)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
