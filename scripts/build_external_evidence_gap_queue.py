#!/usr/bin/env python3
"""Build a small, explicit review queue from the external lineage audit."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "external-evidence-gap-queue.json"


def main() -> int:
    observations = json.loads((ANALYSIS / "external-family-observations.json").read_text())["observations"]
    lineage = json.loads((ANALYSIS / "external-family-lineage-review.json").read_text())["reviews"]
    by_id = {observation["observation_id"]: observation for observation in observations}
    gaps = []
    for review in lineage:
        observation = by_id[review["observation_id"]]
        priority = "high" if review["source_url_status"] == "not_present_in_artifact" else "medium"
        gaps.append(
            {
                "observation_id": review["observation_id"],
                "family_id": observation["family_id"],
                "title": observation["title"],
                "priority": priority,
                "missing_evidence": review["remaining"],
                "shared_url_count": len(review["cross_observation_shared_urls"]),
                "shared_host_count": len(review["cross_observation_shared_hosts"]),
                "decision": review["promotion_decision"],
            }
        )
    gaps.sort(key=lambda item: (0 if item["priority"] == "high" else 1, item["family_id"], item["observation_id"]))
    payload = {
        "schema": "external-trend-intelligence.external-evidence-gap-queue.v1",
        "purpose": "Explicit next-review queue for external observations that cannot yet support independent trend promotion.",
        "gap_count": len(gaps),
        "high_priority_count": sum(gap["priority"] == "high" for gap in gaps),
        "gaps": gaps,
        "boundary": "A gap queue identifies missing review work; it does not establish that an observation is false or that a candidate is ready for internal company testing.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(gaps)} gaps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
