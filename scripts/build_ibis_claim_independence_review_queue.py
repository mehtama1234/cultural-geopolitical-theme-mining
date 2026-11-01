#!/usr/bin/env python3
"""Create a work queue for manual review of low-dependency IBIS claims."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
AUDIT = ANALYSIS / "ibis-claim-independence-audit.json"
SAMPLE = ANALYSIS / "ibis-finding-claim-sample.json"
OUTPUT = ANALYSIS / "ibis-claim-independence-review-queue.json"


def main() -> int:
    audit = json.loads(AUDIT.read_text())
    sample = json.loads(SAMPLE.read_text())
    source_by_claim = {}
    for industry in sample["samples"]:
        for claim in industry["claims"]:
            key = f"{industry['industry_slug']}::{claim.get('claim_id')}"
            source_by_claim[key] = claim.get("sources", [])

    candidates = []
    for row in audit["claims"]:
        if row["independence_status"] != "candidate_for_manual_review":
            continue
        key = f"{row['industry_slug']}::{row['claim_id']}"
        sources = source_by_claim.get(key, [])
        source_rows = [
            {
                "source_id": source.get("id"),
                "publisher": source.get("publisher"),
                "url": source.get("url"),
                "source_type": source.get("source_type"),
                "published_at": source.get("published_at"),
            }
            for source in sources
        ]
        priority = "high" if row["claim_type"] in {"fact", "estimate"} else "medium"
        candidates.append(
            {
                "review_id": f"ibis-independence::{key}",
                "industry_slug": row["industry_slug"],
                "claim_id": row["claim_id"],
                "claim_type": row["claim_type"],
                "priority": priority,
                "review_status": "unassigned",
                "independence_candidate_basis": {
                    "source_host_count": row["source_host_count"],
                    "publisher_count": row["publisher_count"],
                    "source_url_count": row["source_url_count"],
                    "dependency_flags": row["dependency_flags"],
                },
                "sources": source_rows,
                "required_evidence": [
                    "verify the named publisher and legal source owner",
                    "confirm whether each source is primary, secondary, or company-sponsored",
                    "record publication date, observation period, geography, unit, and denominator",
                    "check whether any sources share an underlying dataset, study, filing, or press release",
                    "attach one independent outcome measure or record why none is available",
                    "record rights/reuse status for the exact artifact",
                ],
                "decision_options": ["independent_candidate", "dependent_restate", "insufficient_evidence", "contradicted"],
                "stop_rule": "Keep the claim held and do not use it as independent confirmation if ownership, period, outcome linkage, or rights cannot be verified.",
                "company_bridge_status": "blocked_external_first_gate",
            }
        )

    candidates.sort(key=lambda row: (0 if row["priority"] == "high" else 1, row["industry_slug"], row["claim_id"]))
    payload = {
        "schema": "external-trend-intelligence.ibis-claim-independence-review-queue.v1",
        "finding_slug": audit["finding_slug"],
        "source_revision": audit["source_revision"],
        "status": "manual_review_queue_ready",
        "candidate_count": len(candidates),
        "high_priority_count": sum(row["priority"] == "high" for row in candidates),
        "unassigned_count": len(candidates),
        "review_protocol": {
            "assignment_sla": "10 business days",
            "required_reviewer_role": "lineage reviewer with evidence analyst support",
            "completion_evidence": "completed required_evidence fields, source ownership decision, outcome linkage decision, rights note, and signed disposition",
            "promotion_boundary": "No claim or finding is promoted from this queue without a recorded independent outcome or an explicit held disposition.",
        },
        "next_action": "Assign the first high-priority claims to a lineage reviewer, resolve ownership and underlying-dataset dependence, then acquire dated independent outcome measures before any IBIS finding promotion.",
        "boundary": "This queue identifies candidates for manual review; it does not establish independence, validate outcomes, clear rights, or authorize an internal company bridge.",
        "candidates": candidates,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(candidates)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
