#!/usr/bin/env python3
"""Audit normalized observations against the evidence contract."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "external-family-observations.json"
OUTPUT = ANALYSIS / "evidence-contract-audit.json"

REQUIRED = {
    "source_path", "source_revision", "title", "unit", "observation_period",
    "geography", "uncertainty", "rights_status", "publisher_dependence",
    "lineage_status", "counter_signal_status", "boundary",
}


def main() -> int:
    payload = json.loads(INPUT.read_text())
    results = []
    for observation in payload["observations"]:
        missing = sorted(key for key in REQUIRED if not observation.get(key))
        results.append({
            "observation_id": observation["observation_id"],
            "family_id": observation["family_id"],
            "status": "contract_complete" if not missing else "contract_gap",
            "missing_fields": missing,
            "rights_status": observation.get("rights_status"),
            "publisher_dependence": observation.get("publisher_dependence"),
            "lineage_status": observation.get("lineage_status"),
        })
    report = {
        "schema": "external-trend-intelligence.evidence-contract-audit.v1",
        "input": "external-family-observations.json",
        "required_fields": sorted(REQUIRED),
        "observation_count": len(results),
        "contract_complete_count": sum(item["status"] == "contract_complete" for item in results),
        "contract_gap_count": sum(item["status"] == "contract_gap" for item in results),
        "observations": results,
        "boundary": "Field presence is a preservation check. 'not_yet_verified' and 'review_required' remain unresolved evidence states and do not establish rights or independence.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(results)} observations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
