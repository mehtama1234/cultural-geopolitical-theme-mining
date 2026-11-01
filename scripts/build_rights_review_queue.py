#!/usr/bin/env python3
"""Build the source rights and publisher-dependence review queue."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "rights-review-queue.json"


def main() -> int:
    controls = json.loads((ANALYSIS / "source-family-controls.json").read_text())
    family_plans = {
        "cultural-geopolitical-theme-mining": {"first_artifact": "source-registry-snapshot.json and observation-manifest.json", "rights_questions": ["identify upstream publisher terms", "separate local analysis from reproduced content", "record chart and narrative reuse boundary"], "lineage_questions": ["pin source revision", "deduplicate shared URLs and datasets", "record publisher dependence by theme"]},
        "social-research": {"first_artifact": "social-publication-citation-map.json", "rights_questions": ["check platform and publisher terms", "separate discussion excerpts from derived themes", "record storage and redistribution limits"], "lineage_questions": ["identify original publisher and collection method", "flag repeated platform or study sources", "preserve non-representative discussion boundary"]},
        "trend-hunting": {"first_artifact": "trend-hunting-source-map.json", "rights_questions": ["review synthesis input terms", "document permission for derived charts", "retain upstream attribution"], "lineage_questions": ["trace synthesis claims to primary observations", "deduplicate restated sources", "record analyst interpretation"]},
        "annual-report-research": {"first_artifact": "annual-report-citation-map.json", "rights_questions": ["review filing and report reuse notices", "separate reported claims from derived analysis", "document republication boundary"], "lineage_questions": ["pin filing identity and period", "identify repeated issuer or analyst material", "retain reported-versus-observed distinction"]},
        "inc5000-analysis": {"first_artifact": "inc5000-opportunity-source-map.json", "rights_questions": ["review ranking and company-page terms", "document permitted storage and derived-use scope", "hold buyer-facing reuse until cleared"], "lineage_questions": ["separate ranking source from company evidence", "identify sponsored material", "retain demand-proxy boundary"]},
        "ibis-industries": {"first_artifact": "ibis-force-claim-review.json and ibis-claim-dependency-review.json", "rights_questions": ["review IBIS and cited-source terms", "separate licensed content from normalized metadata", "hold public derived charts pending clearance"], "lineage_questions": ["resolve source IDs to primary artifacts", "deduplicate shared URLs and studies", "record secondary-summary dependence"]},
        "research-signals": {"first_artifact": "source-family-registry.json and evidence-contract-audit.json", "rights_questions": ["inventory third-party libraries and upstream inputs", "record repository license and retention obligations", "separate code rights from data rights"], "lineage_questions": ["pin custody and transformation steps", "record generated versus upstream artifacts", "document checksum and deletion obligations"]},
        "organization-intelligence-system": {"first_artifact": "source-family-registry.json and internal-bridge-schema.json", "rights_questions": ["review shared contract and dependency licenses", "separate governance templates from source content", "hold internal bridge until approval"], "lineage_questions": ["preserve source-owner decisions", "record cross-repository dependency", "prevent schema joins implying independence"]},
    }
    rows = []
    for family in controls["families"]:
        plan = family_plans.get(family["family_id"], {})
        rows.append({
            "family_id": family["family_id"],
            "status": "review_required",
            "rights_status": family["rights_status"],
            "publisher_dependence": family["publisher_dependence"],
            "evidence_required": [
                "access route and terms or license basis",
                "permitted storage, transformation, and redistribution scope",
                "publisher and upstream dataset identity",
                "shared-publisher/shared-dataset dependence assessment",
                "retention and refresh obligation",
            ],
            "stop_rule": "Do not promote a trend or connect internal data while rights basis or publisher dependence remains unresolved.",
            "owner": family["owner"],
            "review_plan": {
                "first_artifact": plan.get("first_artifact", "source-family-registry.json"),
                "rights_questions": plan.get("rights_questions", []),
                "lineage_questions": plan.get("lineage_questions", []),
                "completion_evidence": ["authoritative terms or license record", "publisher/dataset dependence review", "approved storage and reuse boundary", "reviewer and date"],
            },
        })
    report = {
        "schema": "external-trend-intelligence.rights-review-queue.v1",
        "family_count": len(rows),
        "review_required_count": sum(row["status"] == "review_required" for row in rows),
        "rows": rows,
        "boundary": "This queue identifies evidence needed for clearance; it is not a legal determination or a claim that any source is licensed.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} families)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
