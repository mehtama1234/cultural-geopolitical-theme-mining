#!/usr/bin/env python3
"""Review source completeness and independence warnings for each IBIS force."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "ibis-force-claim-review.json"


def main() -> int:
    force_map = json.loads((ANALYSIS / "ibis-force-claim-map.json").read_text())
    rows = []
    for force in force_map["forces"]:
        sources = force.get("sources", [])
        claims = force.get("claim_references", [])
        publishers = sorted({source.get("publisher") for source in sources if source.get("publisher")})
        hosts = sorted({urlparse(source.get("url", "")).netloc.lower() for source in sources if source.get("url")})
        missing_period = sum(not claim.get("period") for claim in claims)
        rows.append({
            "force_id": force["force_id"],
            "title": force["title"],
            "source_count": len(sources),
            "publisher_count": len(publishers),
            "publishers": publishers,
            "host_count": len(hosts),
            "hosts": hosts,
            "claim_reference_count": len(claims),
            "claim_period_missing_count": missing_period,
            "unresolved_source_id_count": len(force.get("unresolved_source_ids", [])),
            "outcome_measure_candidates": force.get("outcome_measure_candidates", []),
            "falsifiers": force.get("falsifiers", []),
            "independence_status": "publisher_diversity_signal_pending_dataset_and_claim_review" if len(publishers) > 1 else "single_publisher_or_unresolved",
            "review_status": "held_claim_level_lineage_independence_and_outcome_review",
            "next_action": "Resolve claim periods, distinguish primary observations from secondary summaries, and attach an independent outcome measure before promotion.",
        })
    report = {
        "schema": "external-trend-intelligence.ibis-force-claim-review.v1",
        "source_revision": force_map["source_revision"],
        "force_count": len(rows),
        "rows": rows,
        "aggregate": {
            "publisher_diversity_signal_count": sum(row["publisher_count"] > 1 for row in rows),
            "claims_missing_period_count": sum(row["claim_period_missing_count"] for row in rows),
            "unresolved_source_id_count": sum(row["unresolved_source_id_count"] for row in rows),
        },
        "status": "held_pending_claim_level_lineage_independence_and_outcome_review",
        "boundary": "Distinct publishers or hosts are signals for review, not proof of independent evidence. This force review does not qualify an IBIS finding or authorize a company bridge.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} forces; {report['aggregate']['claims_missing_period_count']} claims missing periods)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
