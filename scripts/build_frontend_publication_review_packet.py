#!/usr/bin/env python3
"""Build an executable review packet for frontend chart publication contracts."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "frontend-publication-review-packet.json"


def main() -> int:
    catalog = json.loads((ANALYSIS / "observatory-chart-catalog.json").read_text())
    registry = json.loads((ANALYSIS / "frontend-publication-registry.json").read_text())
    required = set(catalog["required_chart_metadata"])
    reviews = []
    for chart in catalog["charts"]:
        declared = set(chart.get("required_visible_fields", []))
        # Chart definitions use source artifacts for the remaining fields; the
        # packet makes that handoff explicit instead of implying they are rendered.
        missing_declaration = sorted(required - declared - {"evidence_boundary", "company_gate"})
        reviews.append(
            {
                "chart_id": chart["chart_id"],
                "title": chart["title"],
                "theme": chart["theme"],
                "subtheme": chart["subtheme"],
                "concept": chart["concept"],
                "source_artifacts": chart["source_artifacts"],
                "required_visible_fields": chart["required_visible_fields"],
                "boundary": chart["boundary"],
                "contract_status": "source_contract_review_required" if missing_declaration else "declared",
                "missing_chart_level_declarations": missing_declaration,
                "reviewer": "",
                "reviewed_at": "",
                "disposition": "",
            }
        )
    packet = {
        "schema": "external-trend-intelligence.frontend-publication-review-packet.v1",
        "status": "review_required_before_frontend_claims",
        "catalog_chart_count": catalog["chart_count"],
        "registered_publication_count": registry["publication_count"],
        "review_count": len(reviews),
        "open_review_count": sum(row["contract_status"] != "declared" for row in reviews),
        "required_chart_metadata": sorted(required),
        "reviews": reviews,
        "boundary": "This packet checks publication-contract completeness only. It does not render charts, grant rights, qualify a trend, or authorize a company bridge.",
        "next_action": "For every chart, map period, unit, geography, denominator, uncertainty, counter-signal, evidence boundary, and company gate to visible frontend fields; record reviewer disposition before calling the chart decision-ready.",
    }
    OUTPUT.write_text(json.dumps(packet, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(reviews)} charts; {packet['open_review_count']} require review)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
