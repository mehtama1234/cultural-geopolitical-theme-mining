#!/usr/bin/env python3
"""Turn shared-host diagnostics into bounded lineage-review work items."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "host-dependence-review-queue.json"


def main() -> int:
    audit = json.loads((ANALYSIS / "record-host-dependence-audit.json").read_text())
    rows = []
    for host in audit["host_rows"]:
        if host["record_count"] < 2:
            continue
        rows.append(
            {
                "review_id": f"host:{host['host']}",
                "host": host["host"],
                "priority": "high" if host["record_count"] >= 25 else "normal",
                "record_count": host["record_count"],
                "theme_count": host["theme_count"],
                "status": "unassigned",
                "owner": "lineage review queue",
                "review_questions": [
                    "Which publisher or publishers control the cited artifacts?",
                    "Do multiple URLs resolve to the same upstream dataset, report, or synthesis?",
                    "Does the source provide a distinct outcome measure or only restate another source?",
                    "What exact storage, transformation, and derived-chart rights apply?",
                ],
                "acceptance": [
                    "publisher and upstream identity recorded",
                    "shared-dataset or restatement dependence assessed",
                    "rights route and restrictions recorded",
                    "independence disposition recorded before promotion",
                ],
            }
        )
    rows.sort(key=lambda row: (0 if row["priority"] == "high" else 1, -row["record_count"], row["host"]))
    payload = {
        "schema": "external-trend-intelligence.host-dependence-review-queue.v1",
        "status": "review_required",
        "unique_host_count": audit["unique_host_count"],
        "shared_host_count": audit["shared_host_count"],
        "row_limit": 100,
        "rows": rows[:100],
        "high_priority_count": sum(row["priority"] == "high" for row in rows),
        "unassigned_count": len(rows),
        "boundary": "This queue assigns lineage questions for shared hosts. It does not infer publisher identity, grant rights, or count any host as independent confirmation.",
        "next_action": "Assign the highest-volume shared hosts to a lineage reviewer and record a publisher, upstream-dependence, rights, and independence disposition before using repetition as confirmation.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} shared-host reviews; {payload['high_priority_count']} high priority)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
