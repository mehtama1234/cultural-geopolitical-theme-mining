#!/usr/bin/env python3
"""Align the existing MEPS R4/2 and R5/3 event-work outputs by event family."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--r4", type=Path, required=True)
    ap.add_argument("--r5", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    r4 = json.loads(args.r4.read_text(encoding="utf-8"))
    r5 = json.loads(args.r5.read_text(encoding="utf-8"))
    families = ("office", "emergency_room", "inpatient")
    rows = {}
    for family in families:
        early = r4["events"][family]
        later = r5["events"][family]
        early_level = early["groups"]["event_window"]["outcomes"]["not_employed_followup"]
        comparison_level = early["groups"]["complementary_round_valid"]["outcomes"]["not_employed_followup"]
        later_levels = later["outcomes"]
        rows[family] = {
            "r4_nonemployment": {
                "event_window": early_level,
                "complementary_round_valid": comparison_level,
            },
            "r5_nonemployment": later_levels["not_employed_r5"],
            "r4_to_r5_status_change": later_levels["employment_status_changed_r4_to_r5"],
            "r4_nonemployment_resolution": later_levels["nonemployment_resolved"],
            "r4_nonemployment_onset": later_levels["nonemployment_onset"],
            "event_window_people_r4": early["event_window_people"],
            "event_window_people_r5": later["group_counts"]["event_window"],
            "comparison_people_r4": early["groups"]["complementary_round_valid"]["records"],
            "comparison_people_r5": later["group_counts"]["no_event_in_window"],
        }
    result = {
        "format": "meps-event-work-two-clock-audit-v1",
        "period": "2024 MEPS; strict R3/1-to-R4/2 event window with R4/2 and R5/3 work endpoints",
        "alignment": "Event-family and month-rule alignment across two existing outputs; R5/3-valid records are not asserted to be the same row set as the R4/2 screen.",
        "event_families": rows,
        "source_outputs": {
            "r4_screen": {"path": str(args.r4), "sha256": digest(args.r4)},
            "r5_followup": {"path": str(args.r5), "sha256": digest(args.r5)},
        },
        "boundary": "The R4/2 endpoint is a level of valid EMPST42=4; the R5/3 outcomes add descriptive status-change, onset, and resolution screens. Neither identifies job loss cause, hours, earnings, schedule control, treatment continuity, remedy, household recovery, trust, political action, or exit.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "families": len(rows)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
