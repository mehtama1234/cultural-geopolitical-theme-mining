#!/usr/bin/env python3
"""Select a small, evidence-rich first batch from the IBIS review queue."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "ibis-claim-independence-review-queue.json"
OUTPUT = ANALYSIS / "ibis-first-review-batch.json"
BATCH_SIZE = 10


def source_score(row: dict) -> tuple[int, int, int, str]:
    types = {source.get("source_type") for source in row.get("sources", [])}
    authoritative = len(types & {"government", "academic"})
    diversity = row["independence_candidate_basis"]["source_host_count"]
    return (-authoritative, -diversity, -len(row.get("sources", [])), row["review_id"])


def main() -> int:
    queue = json.loads(INPUT.read_text())
    candidates = sorted(queue["candidates"], key=source_score)
    selected = []
    for rank, row in enumerate(candidates[:BATCH_SIZE], start=1):
        selected.append(
            {
                "batch_rank": rank,
                "review_id": row["review_id"],
                "industry_slug": row["industry_slug"],
                "industry_sector": row.get("industry_sector"),
                "claim_id": row["claim_id"],
                "claim_text": row.get("claim_text"),
                "claim_type": row["claim_type"],
                "geography": row.get("geography"),
                "as_of": row.get("as_of"),
                "sources": row["sources"],
                "outcome_measure_candidates": row.get("outcome_measure_candidates", []),
                "review_status": "pending_manual_review",
                "selection_reason": "High-priority claim with at least two hosts and at least one government or academic source type; selected for source-ownership and outcome-method review before broader sampling.",
                "required_review": [
                    "verify publisher identity and exact artifact",
                    "classify each source as primary, secondary, or sponsored",
                    "check shared study/dataset/press-release lineage",
                    "record period, geography, unit, denominator, and uncertainty",
                    "acquire or document the absence of an independent dated outcome",
                    "record rights and reuse boundary",
                ],
                "disposition": "pending",
                "stop_rule": "Do not count as independent confirmation or connect to company data until all required review fields are evidenced.",
            }
        )

    payload = {
        "schema": "external-trend-intelligence.ibis-first-review-batch.v1",
        "finding_slug": queue["finding_slug"],
        "source_revision": queue["source_revision"],
        "status": "first_batch_ready_for_manual_review",
        "batch_size": len(selected),
        "selection_rule": "rank queue claims by authoritative source-type presence, host diversity, and source count; retain the queue's fail-closed boundary",
        "review_owner_role": "lineage reviewer with evidence analyst support",
        "assignment_sla": queue["review_protocol"]["assignment_sla"],
        "completion_evidence": queue["review_protocol"]["completion_evidence"],
        "next_action": "Assign this batch, complete source ownership and lineage fields, then acquire dated independent outcomes for claims that survive the first review.",
        "boundary": "This is a work packet, not a qualification result. Every row remains pending and blocked from independent-confirmation counting and company bridging.",
        "claims": selected,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(selected)} claims)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
