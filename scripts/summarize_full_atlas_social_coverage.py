#!/usr/bin/env python3
"""Write a compact audit of record-level social augmentation progress."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage.json"
OUT = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage-readout.md"


def main() -> None:
    payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    rows = payload["rows"]
    statuses = Counter(row["status"] for row in rows)
    platform_status = Counter()
    evidence_rows = 0
    evidence_items = 0
    for row in rows:
        row_items = 0
        for platform, item in row["platforms"].items():
            platform_status[f"{platform}:{item['status']}"] += 1
            row_items += len(item.get("social_record_ids", []))
        if row_items:
            evidence_rows += 1
            evidence_items += row_items
    lines = [
        "# Full-atlas social coverage readout",
        "",
        "This is a live control readout, not a completion claim.",
        "",
        f"- Atlas records: **{len(rows):,}**",
        f"- Atlas records with at least one exact linked social item: **{evidence_rows:,}**",
        f"- Exact linked social items: **{evidence_items:,}**",
        f"- Record statuses: `{dict(statuses)}`",
        "",
        "## Platform attempt states",
        "",
        "| Platform/status | Rows |",
        "|---|---:|",
    ]
    for key, count in sorted(platform_status.items()):
        lines.append(f"| `{key}` | {count:,} |")
    lines.extend(
        [
            "",
            "The queue is not complete until every row reaches a terminal state:",
            "`augmented`, `documented_access_gap`, or `not_socially_applicable`.",
        ]
    )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {OUT.relative_to(ROOT)}: {evidence_rows} rows, {evidence_items} items")


if __name__ == "__main__":
    main()
