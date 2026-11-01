#!/usr/bin/env python3
"""Build a signable uncertainty review packet for decision-facing artifacts."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "uncertainty-review-packet.json"


def main() -> int:
    audit = json.loads((ANALYSIS / "uncertainty-coverage-audit.json").read_text())
    rows = []
    for item in audit["rows"]:
        rows.append({
            "artifact": item["artifact"],
            "current_state": item["uncertainty_state"],
            "evidence": item["evidence"],
            "release_implication": item["release_implication"],
            "required_review_fields": [
                "estimate and unit",
                "sample or denominator",
                "weights and design effect",
                "standard error, margin of error, interval, or explicit unavailable status",
                "suppression and missingness rules",
                "method and population boundary",
                "uncertainty treatment in chart or narrative",
                "reviewer and review date",
            ],
            "decision_options": ["source_level_uncertainty_complete", "retain_explicitly_incomplete", "hold_pending_source_interval", "not_applicable_with_reason"],
            "signoff": {"evidence_analyst": None, "lineage_reviewer": None, "release_owner": None, "reviewed_on": None, "decision": None},
        })
    payload = {
        "schema": "external-trend-intelligence.uncertainty-review-packet.v1",
        "status": "ready_for_uncertainty_review",
        "artifact_count": len(rows),
        "complete_source_level_count": audit["complete_source_level_count"],
        "incomplete_or_pending_count": audit["incomplete_or_pending_count"],
        "rows": rows,
        "acceptance_criteria": [
            "Every decision-facing artifact records source-level uncertainty or an explicit, bounded unavailable status.",
            "Design-based uncertainty is not replaced with a naive interval without a visible diagnostic label.",
            "Missing intervals, weights, denominators, and suppression rules remain release blockers for pooling or company use.",
            "Charts and narratives carry the same uncertainty boundary as the underlying artifact.",
        ],
        "next_action": audit["next_action"],
        "boundary": "This packet makes uncertainty review executable; it does not create statistical validity or permit pooling of unlike measures.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} artifacts; {audit['complete_source_level_count']} complete)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
