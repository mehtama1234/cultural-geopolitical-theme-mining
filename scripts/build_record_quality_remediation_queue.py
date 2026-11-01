#!/usr/bin/env python3
"""Create actionable remediation work from record metadata gaps."""

from __future__ import annotations

import json
from pathlib import Path

from build_external_observation_manifest import archived_records
from build_record_quality_audit import audit_row


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "record-quality-remediation-queue.json"


def main() -> int:
    rows = []
    for path, record in archived_records("HEAD"):
        audit = audit_row(path, record)
        checks = audit["checks"]
        missing = [field for field, present in checks.items() if not present]
        if not missing:
            continue
        priority = "high" if "counter_signal" in missing else "medium"
        rows.append(
            {
                "record_path": path,
                "trend_id": record.get("trend_id"),
                "priority": priority,
                "missing_fields": missing,
                "status": "unassigned",
                "acceptance": {
                    "counter_signal": "Record a source-backed counter-signal or explicitly document that none was found after review.",
                    "retrieval_hash": "Pin the retrieved artifact hash and state its scope, or document why a hash is unavailable.",
                    "other_metadata": "Complete the missing field without inferring values from another source.",
                },
            }
        )
    rows.sort(key=lambda row: (0 if row["priority"] == "high" else 1, row["record_path"]))
    counts = {}
    for row in rows:
        for field in row["missing_fields"]:
            counts[field] = counts.get(field, 0) + 1
    payload = {
        "schema": "external-trend-intelligence.record-quality-remediation-queue.v1",
        "status": "remediation_required",
        "record_count_with_gaps": len(rows),
        "missing_field_counts": dict(sorted(counts.items())),
        "high_priority_count": sum(row["priority"] == "high" for row in rows),
        "row_limit": 100,
        "rows": rows[:100],
        "boundary": "This queue assigns metadata repair work only. It does not invent counter-signals, create retrieval evidence, clear rights, prove independence, or qualify a trend.",
        "next_action": "Assign the high-priority counter-signal rows first; document an explicit null review when no counter-signal is found, then pin retrieval hashes where source custody permits.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} records with gaps; {payload['high_priority_count']} high priority)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
