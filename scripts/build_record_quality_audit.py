#!/usr/bin/env python3
"""Audit required evidence fields across the external observation inventory.

This is a completeness audit only. It does not infer a unit, uncertainty,
counter-signal, rights status, or lineage when a record omits one.
"""

from __future__ import annotations

import json
from pathlib import Path

from build_external_observation_manifest import archived_records


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "record-quality-audit.json"


def text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def has_measure_unit(record: dict) -> bool:
    for observation in record.get("observations", []):
        measures = observation.get("measures", {})
        if any(isinstance(value, dict) and text(value.get("unit")) for value in measures.values()):
            return True
        if text(observation.get("unit")):
            return True
    return text(record.get("unit"))


def has_period(record: dict) -> bool:
    if text(record.get("period")) or text(record.get("observation_period")):
        return True
    return any(text(observation.get("period")) for observation in record.get("observations", []))


def has_uncertainty(record: dict) -> bool:
    if any(text(record.get(key)) for key in ("uncertainty", "uncertainty_notes", "standard_error", "margin_of_error")):
        return True
    for observation in record.get("observations", []):
        if any(text(observation.get(key)) for key in ("uncertainty", "uncertainty_notes", "standard_error", "margin_of_error")):
            return True
        if any(
            isinstance(value, dict)
            and any(text(value.get(key)) for key in ("uncertainty", "standard_error", "margin_of_error"))
            for value in observation.get("measures", {}).values()
        ):
            return True
    return False


def has_counter_signal(record: dict) -> bool:
    keys = ("counterinterpretation", "counter_signal", "counter_signals", "counterevidence", "counter_signal_status")
    return any(text(record.get(key)) or (isinstance(record.get(key), list) and bool(record[key])) for key in keys)


def audit_row(path: str, record: dict) -> dict:
    checks = {
        "source_identity": text(record.get("source_unit")),
        "lineage_locator": bool(record.get("related_sources")) or bool(record.get("observations")) and any(
            text(item.get("source_url")) for item in record.get("observations", [])
        ),
        "period": has_period(record),
        "unit": has_measure_unit(record),
        "geography": text(record.get("geography")),
        "uncertainty": has_uncertainty(record),
        "counter_signal": has_counter_signal(record),
        "boundary": text(record.get("boundary")),
        "retrieval_hash": text(record.get("retrieval_hash")),
    }
    return {"record_path": path, "trend_id": record.get("trend_id"), "checks": checks}


def main() -> int:
    rows = [audit_row(path, record) for path, record in archived_records("HEAD")]
    fields = sorted(rows[0]["checks"]) if rows else []
    field_counts = {field: sum(row["checks"][field] for row in rows) for field in fields}
    missing_examples = {
        field: [row["record_path"] for row in rows if not row["checks"][field]][:25]
        for field in fields
    }
    payload = {
        "schema": "external-trend-intelligence.record-quality-audit.v1",
        "status": "record_completeness_visible_quality_unresolved",
        "record_count": len(rows),
        "field_counts": field_counts,
        "field_coverage": {
            field: round(count / len(rows), 4) if rows else 0
            for field, count in field_counts.items()
        },
        "missing_example_limit": 25,
        "missing_examples": missing_examples,
        "boundary": "This audit reports explicit field presence in each retained record. It does not infer missing metadata, validate source truth, clear rights, prove independence, or qualify a trend.",
        "next_action": "Prioritize records missing period, unit, uncertainty, counter-signal, or lineage metadata before using them in cross-source comparisons or company decision work.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
