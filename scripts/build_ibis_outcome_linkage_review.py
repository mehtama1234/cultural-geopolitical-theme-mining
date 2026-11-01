#!/usr/bin/env python3
"""Record a bounded official outcome linkage for the first IBIS acquisition target."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
QUEUE = ANALYSIS / "ibis-outcome-acquisition-queue.json"
INDEPENDENCE_QUEUE = ANALYSIS / "ibis-claim-independence-review-queue.json"
USDA = Path(__file__).resolve().parents[1] / "analysis" / "records" / "comparative-usda-food-security-2022-2024.json"
OUTPUT = ANALYSIS / "ibis-community-food-outcome-linkage-review.json"


def main() -> int:
    queue = json.loads(QUEUE.read_text())
    independence_queue = json.loads(INDEPENDENCE_QUEUE.read_text())
    record = json.loads(USDA.read_text())
    target = next(row for row in queue["rows"] if row["review_id"] == "ibis-independence::community-food-services-in-the-us::community-demand")
    source_review = next(row for row in independence_queue["candidates"] if row["review_id"] == target["review_id"])
    payload = {
        "schema": "external-trend-intelligence.ibis-community-food-outcome-linkage-review.v1",
        "status": "official_outcome_acquired_lineage_review_pending",
        "review_id": target["review_id"],
        "industry_slug": target["industry_slug"],
        "claim_id": target["claim_id"],
        "claim": {
            "text": target["claim_text"],
            "publisher_candidates": [source["publisher"] for source in source_review["sources"]],
            "source_urls": [source["url"] for source in source_review["sources"]],
            "geography": target["geography"],
            "as_of": target["claim_as_of"],
        },
        "outcome_artifact": {
            "record_id": record["trend_id"],
            "publisher": "USDA Economic Research Service",
            "source_unit": record["source_unit"],
            "source_urls": [item["source_url"] for item in record["related_sources"]],
            "retrieval_hash": record["retrieval_hash"],
            "population": record["geography"],
            "periods": [observation["period"] for observation in record["observations"]],
            "measure": "percent of U.S. households food insecure at some time during the year",
            "observations": [
                {
                    "period": observation["period"],
                    "value": observation["measures"]["food_insecure"]["value"],
                    "unit": observation["measures"]["food_insecure"]["unit"],
                    "denominator": observation["denominator"]["unit"],
                }
                for observation in record["observations"]
            ],
            "uncertainty": record["uncertainty"],
            "counterinterpretation": record["counterinterpretation"],
            "rights_boundary": "Retain normalized values, source locator, retrieval hash, and derived internal-review calculations with ERS attribution; raw publication reproduction and redistribution remain uncleared.",
        },
        "lineage_adjudication": {
            "publisher_status": "canonical_official_publisher_resolved",
            "independence_status": "dependent_restatement_possible",
            "reason": "FRAC may summarize the same USDA series; the direct USDA record is a canonical outcome artifact but is not counted as a second independent publisher until source-level lineage is signed off.",
            "population_compatibility": "not_comparable_to_the_IBIS_industry_population_without_a_service-use denominator",
            "outcome_linkage": "food-insecurity outcome is relevant context for community food-service demand but does not measure visits, meals, pantry capacity, enrollment, or provider revenue",
            "rights_status": "conditional_attribution_use_documented",
            "review_status": "pending_human_lineage_and_outcome_scope_signoff",
        },
        "decision": "retain_as_acquired_external_context; do_not_promote_ibis_claim_or_bridge_to_company_data",
        "required_next_steps": [
            "Confirm whether the FRAC record is a restatement of the USDA artifact and record the source lineage.",
            "Acquire a direct community-food-service utilization or capacity outcome with a defined denominator.",
            "Reconcile the outcome period, population, unit, uncertainty, and rights before any IBIS qualification.",
        ],
        "boundary": "This artifact documents one acquired official outcome context and its limits. It does not validate the IBIS claim, establish demand causality, prove independent confirmation, or authorize an internal company bridge.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({payload['status']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
