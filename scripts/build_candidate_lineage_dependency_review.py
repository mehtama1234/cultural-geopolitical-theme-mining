#!/usr/bin/env python3
"""Record explicit same-publisher, same-study, and same-event dependencies."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "candidate-lineage-dependency-review.json"

DEPENDENCY_GROUPS = {
    "candidate-formal-response-before-recovery": [
        {
            "group_id": "fair-work-commission-case-family",
            "record_ids": [
                "au-al-hussein-reactivation-deemed-work-2025",
                "au-fwc-khan-platform-repeat-deactivation-2026",
                "au-mansoor-platform-alternative-earnings-remedy-2025",
                "comparative-australia-fwc-no-alternative-employment-remedy-2024",
            ],
            "classification": "same_publisher_family",
            "reason": "Four records are Fair Work Commission cases; separate case IDs do not establish independent publisher or population evidence.",
        },
    ],
    "candidate-time-financial-pressure-practical-room": [
        {
            "group_id": "abs-general-social-survey",
            "record_ids": ["comparative-abs-general-social-survey-2025-cultural-participation-financial-stress-connection"],
            "classification": "same_survey_family",
            "reason": "Multiple measures in this record come from one ABS General Social Survey family and are not independent observations.",
        },
        {
            "group_id": "jpmorgan-single-endpoint",
            "record_ids": ["comparative-jpmorgan-household-liquidity-2023"],
            "classification": "single_publisher_endpoint",
            "reason": "JPMorgan is one administrative-data endpoint with a restrictive republication notice; the chart does not expose a numeric table.",
        },
    ],
    "candidate-digital-capability-control-trust": [
        {
            "group_id": "informs-hbs-study-lineage",
            "record_ids": ["us-hbs-ai-customer-service-contextual-recourse-2020-2021"],
            "classification": "secondary_summary_underlying_study",
            "reason": "The HBS record summarizes an INFORMS field experiment; a summary and its underlying study must not be counted twice.",
        },
        {
            "group_id": "dima-musicwatch-lineage",
            "record_ids": ["comparative-dima-music-streaming-2026-discovery-spend-local-culture-ai"],
            "classification": "secondary_publisher_dependency",
            "reason": "The DIMA record depends on MusicWatch research and requires claim-level source review.",
        },
    ],
    "candidate-infrastructure-dependency-power": [
        {
            "group_id": "pjm-large-load-event",
            "record_ids": ["us-pjm-large-load-disconnection-response-2026"],
            "classification": "single_event_record",
            "reason": "The PJM material describes one operating event; multiple documents about that event would not be independent replications.",
        },
    ],
}


def main() -> int:
    candidates = json.loads((ANALYSIS / "candidate-comparisons.json").read_text())["candidates"]
    rows = []
    for candidate in candidates:
        record_ids = candidate.get("evidence_record_ids", [])
        groups = []
        grouped = set()
        for group in DEPENDENCY_GROUPS.get(candidate["id"], []):
            present = [record_id for record_id in group["record_ids"] if record_id in record_ids]
            if present:
                item = dict(group)
                item["record_ids"] = present
                groups.append(item)
                grouped.update(present)
        rows.append({
            "candidate_id": candidate["id"],
            "evidence_record_count": len(record_ids),
            "dependency_group_count": len(groups),
            "dependency_groups": groups,
            "unclassified_record_ids": [record_id for record_id in record_ids if record_id not in grouped],
            "independence_status": "unverified",
            "promotion_decision": "hold",
            "boundary": "Dependency groups identify reasons not to count records as independent. Records outside a group are not automatically independent; publisher, dataset, population, method, and outcome review remains required.",
            "next_test": "Resolve each record to a canonical publisher, artifact, underlying dataset, population, period, and outcome before assigning an independence status.",
        })
    payload = {
        "schema": "external-trend-intelligence.candidate-lineage-dependency-review.v1",
        "purpose": "Explicit dependency review for candidate evidence before independence or trend qualification.",
        "candidate_count": len(rows),
        "rows": rows,
        "boundary": "This is a conservative dependency register, not a legal rights determination, independence score, or qualified trend result.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
