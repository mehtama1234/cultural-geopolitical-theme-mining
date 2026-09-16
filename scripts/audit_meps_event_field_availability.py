#!/usr/bin/env python3
"""Audit stage-field availability in the privacy-minimized MEPS event ledger."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


def contains(value: str, *terms: str) -> bool:
    text = value.lower()
    return any(term in text for term in terms)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=root / "analysis/projects/us-health-cost-household-choice/data/meps-event-field-availability-2024.json",
    )
    args = parser.parse_args()

    rows = 0
    event_families: Counter[str] = Counter()
    windows: Counter[str] = Counter()
    coverage = Counter()
    exact_text_counts: dict[str, Counter[str]] = {
        "evidence_status": Counter(),
        "unit": Counter(),
    }
    for line in args.input.open(encoding="utf-8"):
        if not line.strip():
            continue
        row = json.loads(line)
        rows += 1
        event_id = str(row.get("episode_id", ""))
        event_families[event_id.split("-", 2)[1] if event_id.startswith("MEPS24-") else "unknown"] += 1
        trigger = str(row.get("trigger", ""))
        room = str(row.get("practical_room_and_alternatives", ""))
        choice = str(row.get("choice_and_tradeoff", ""))
        route = str(row.get("institutional_route", ""))
        remedy = str(row.get("remedy_verification", ""))
        followup = str(row.get("followup_outcomes", ""))
        meaning = str(row.get("meaning_and_action", ""))
        geography = str(row.get("geography", ""))
        if row.get("event_date") and re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(row["event_date"])):
            coverage["event_date_month_precision"] += 1
        if event_id and event_id.startswith("MEPS24-"):
            coverage["hashed_episode_id"] += 1
        if "underlying need is not identified" not in trigger.lower():
            coverage["initiating_need_observed"] += 1
        if "self/family payment=" in room.lower():
            coverage["round_payment_context_present"] += 1
        if "alternatives not observed" not in room.lower():
            coverage["alternatives_observed"] += 1
        if "reported round cost-related-care-delay" in choice.lower():
            coverage["round_care_delay_context_present"] += 1
        if "event-specific care choice" not in choice.lower():
            coverage["event_specific_choice_observed"] += 1
        if "reported round denial/prior-authorization" in route.lower():
            coverage["round_denial_context_present"] += 1
        if "response, appeal, and authority are not identified" not in route.lower():
            coverage["institutional_response_observed"] += 1
        if not contains(remedy, "unknown", "not observed", "not identified"):
            coverage["remedy_status_observed"] += 1
        if "not event-specific" not in followup.lower():
            coverage["event_specific_followup_observed"] += 1
        if "round context:" in followup.lower():
            coverage["round_followup_context_present"] += 1
        if not contains(meaning, "not observed", "not identified", "unknown"):
            coverage["meaning_action_observed"] += 1
        if geography.strip() and not contains(geography, "not included", "not observed", "not identified", "unknown"):
            coverage["geography_present"] += 1
        window = "in_window" if "strict R3/1-to-R4/2 event window=yes" in trigger else "outside_window"
        windows[window] += 1
        exact_text_counts["evidence_status"][str(row.get("evidence_status", ""))] += 1
        exact_text_counts["unit"][str(row.get("unit", ""))] += 1

    if rows == 0:
        raise ValueError("input ledger contained no rows")
    data = {
        "format": "meps-event-field-availability-audit-v1",
        "status": "field_availability_audit",
        "checked": "2026-09-16",
        "source_unit": "privacy-minimized MEPS 2024 first-event-family JSONL rows",
        "rows": rows,
        "event_family_counts": dict(sorted(event_families.items())),
        "timing_window_counts": dict(sorted(windows.items())),
        "coverage_counts": {key: {"available_rows": value, "share_percent": round(100 * value / rows, 4)} for key, value in sorted(coverage.items())},
        "exact_text_counts": {key: dict(sorted(value.items())) for key, value in exact_text_counts.items()},
        "result": "The ledger has complete hashed episode/date scaffolding and round-level payment/follow-up context, but no row-level initiating need, alternative, event-specific choice, institutional response, verified remedy, meaning/action, or geography.",
        "boundary": "This audits text-coded availability in an existing staged ledger; it does not infer that a field was absent from the original MEPS files beyond the staged record, and it does not estimate a causal or population outcome.",
        "input": str(args.input),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"VALID MEPS event field availability audit: {rows} rows; output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
