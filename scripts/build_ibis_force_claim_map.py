#!/usr/bin/env python3
"""Map the pinned IBIS force register to claim-level source records.

The force register is a hypothesis layer.  This artifact makes its source
custody inspectable without treating a force's citations as independent proof.
"""

from __future__ import annotations

import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "ibis-force-claim-map.json"
REPO = "/home/mehta/git-repo/ibis-industries"
REVISION = "b895acd021fbe3dc1d610255952b1373748e3bc3"
FORCE_PATH = "cross_industry_trends_2025_2026.json"
SOURCE_INVENTORY_PATH = "source_inventory.json"
CLAIM_INVENTORY_PATH = "claim_inventory_reviewed.json"


def show(path: str) -> str:
    return subprocess.check_output(["git", "-C", REPO, "show", f"{REVISION}:{path}"], text=True)


def main() -> int:
    register = json.loads(show(FORCE_PATH))
    inventory = json.loads(show(SOURCE_INVENTORY_PATH))
    inventory_by_id = {source["source_id"]: source for source in inventory["sources"]}
    claim_inventory = json.loads(show(CLAIM_INVENTORY_PATH))
    paths = subprocess.check_output(
        ["git", "-C", REPO, "ls-tree", "-r", "--name-only", REVISION, "business_knowledge_examples"],
        text=True,
    ).splitlines()
    claim_link_paths = [path for path in subprocess.check_output(
        ["git", "-C", REPO, "ls-tree", "-r", "--name-only", REVISION], text=True
    ).splitlines() if path.startswith("claim_link_review_") and path.endswith(".json")]
    records = []
    for path in paths:
        records.append((path, json.loads(show(path))))

    force_rows = []
    all_source_rows = []
    for force in register["forces"]:
        source_ids = set(force.get("source_ids", []))
        claim_refs = []
        affected = set(force.get("affected_industries", []))
        for path, record in records:
            slug = Path(path).stem
            if slug not in affected:
                continue

        # The force register's source IDs are authoritative against the pinned
        # source inventory, even when the industry record itself stores the
        # citation in a separate claim-link review file.
        source_list = []
        for sid in sorted(source_ids):
            source = inventory_by_id.get(sid)
            if source:
                source_list.append(
                    {
                        "id": sid,
                        "title": source.get("raw"),
                        "publisher": source.get("publisher_domain"),
                        "url": source.get("url"),
                        "source_type": source.get("provenance_class"),
                        "record_slugs": source.get("record_slugs", []),
                    }
                )
        unresolved_source_ids = sorted(source_ids - {source["id"] for source in source_list})
        for claim in claim_inventory["claims"]:
            claim_source_ids = set(claim.get("source_ids", [])) | set(claim.get("review_source_ids", []))
            matched = sorted(source_ids.intersection(claim_source_ids))
            if not matched:
                continue
            claim_refs.append(
                {
                    "industry_slug": claim.get("record_slug"),
                    "claim_id": claim.get("claim_id"),
                    "claim_field": claim.get("field"),
                    "claim_text": claim.get("text"),
                    "claim_type": claim.get("claim_type"),
                    "period": claim.get("period"),
                    "citation_status": claim.get("citation_status"),
                    "review_status": claim.get("review_status"),
                    "source_ids": matched,
                }
            )
        # Some reviewed claim links live outside the general claim inventory.
        # Include them as a distinct review source so a zero in the inventory
        # does not look like an absent citation.
        seen_claims = {(ref.get("claim_id"), tuple(ref.get("source_ids", []))) for ref in claim_refs}
        for path in claim_link_paths:
            review = json.loads(show(path))
            record_slug = review.get("record_slug")
            if record_slug not in affected:
                continue
            for claim in review.get("reviewed_claims", []):
                matched = sorted(source_ids.intersection(claim.get("source_ids", [])))
                key = (claim.get("claim_id"), tuple(matched))
                if not matched or key in seen_claims:
                    continue
                seen_claims.add(key)
                claim_refs.append(
                    {
                        "industry_slug": record_slug,
                        "claim_id": claim.get("claim_id"),
                        "claim_text": None,
                        "claim_type": "reviewed_claim_link",
                        "citation_status": claim.get("status"),
                        "supported_scope": claim.get("supported_scope"),
                        "review_note": claim.get("review_note"),
                        "source_ids": matched,
                    }
                )
        all_source_rows.extend(source_list)
        hosts = sorted({urlparse(source.get("url", "")).netloc.lower() for source in source_list if source.get("url")})
        force_rows.append(
            {
                "force_id": force["id"],
                "title": force["title"],
                "categories": force.get("categories", []),
                "thesis": force.get("thesis"),
                "causal_chain": force.get("causal_chain", []),
                "affected_industries": force.get("affected_industries", []),
                "leading_indicators": force.get("leading_indicators", []),
                "outcome_measure_candidates": force.get("leading_indicators", []),
                "decision_questions": force.get("decision_questions", []),
                "falsifiers": force.get("falsifiers", []),
                "confidence": force.get("confidence"),
                "source_ids_declared": sorted(source_ids),
                "sources": source_list,
                "unresolved_source_ids": unresolved_source_ids,
                "claim_reference_count": len(claim_refs),
                "claim_type_counts": dict(sorted(Counter(c.get("claim_type", "unknown") for c in claim_refs).items())),
                "claim_references": claim_refs,
                "publisher_count": len({s.get("publisher", "unknown") for s in source_list}),
                "publisher_names": sorted({s.get("publisher", "unknown") for s in source_list}),
                "source_type_counts": dict(sorted(Counter(s.get("source_type", "unknown") for s in source_list).items())),
                "source_url_count": len({s.get("url") for s in source_list if s.get("url")}),
                "source_host_count": len(hosts),
                "source_hosts": hosts,
                "review_status": "held_claim_level_lineage_and_independence",
            }
        )

    payload = {
        "schema": "external-trend-intelligence.ibis-force-claim-map.v1",
        "purpose": "Claim-level lineage map for the pinned IBIS cross-industry force register.",
        "source_revision": REVISION,
        "source_path": FORCE_PATH,
        "force_count": len(force_rows),
        "record_count_scanned": len(records),
        "forces": force_rows,
        "aggregate": {
            "declared_source_id_count": len({sid for force in force_rows for sid in force["source_ids_declared"]}),
            "resolved_source_id_count": len({source["id"] for force in force_rows for source in force["sources"]}),
            "unresolved_source_id_count": len({sid for force in force_rows for sid in force["unresolved_source_ids"]}),
            "claim_reference_count": sum(force["claim_reference_count"] for force in force_rows),
            "publisher_count": len({source.get("publisher", "unknown") for source in all_source_rows}),
            "source_url_count": len({source.get("url") for source in all_source_rows if source.get("url")}),
        },
        "boundary": "This map attaches force citations to claims in affected industry records. It does not establish that the forces are independent, causal, current, representative, or outcome-valid; shared publishers and synthesis dependence require separate review.",
        "next_test": "Select one force, pre-specify an independent outcome measure and counterexample set, and review source rights, periods, units, and publisher dependence before promotion.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(force_rows)} forces; {payload['aggregate']['claim_reference_count']} claim references)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
