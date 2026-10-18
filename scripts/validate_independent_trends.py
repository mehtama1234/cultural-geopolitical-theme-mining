#!/usr/bin/env python3
"""Validate the research-independent social-trend candidate queue."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "analysis" / "independent-trend-discovery"
SCHEMA = json.loads((BASE / "schema.json").read_text(encoding="utf-8"))


def main() -> int:
    candidates = json.loads((BASE / "candidate-queue.json").read_text(encoding="utf-8"))
    social_dir = ROOT / "analysis" / "social-discussions" / "records"
    social_record_ids: set[str] = set()
    for path in social_dir.glob("*.json"):
        social_record_ids.add(json.loads(path.read_text(encoding="utf-8"))["record_id"])
    errors: list[str] = []
    ids: list[str] = []
    for index, candidate in enumerate(candidates):
        prefix = f"candidate[{index}]"
        missing = [key for key in SCHEMA["required"] if key not in candidate]
        if missing:
            errors.append(f"{prefix}: missing {', '.join(missing)}")
            continue
        ids.append(candidate["candidate_id"])
        if candidate["research_status"] not in SCHEMA["research_status_values"]:
            errors.append(f"{prefix}: invalid research_status")
        if not candidate["source_record_ids"]:
            errors.append(f"{prefix}: source_record_ids must not be empty")
        missing_sources = sorted(set(candidate["source_record_ids"]) - social_record_ids)
        if missing_sources:
            errors.append(f"{prefix}: unknown source records: {', '.join(missing_sources)}")
        if len(set(candidate["platforms_present"])) < 2:
            errors.append(f"{prefix}: needs at least two platforms")
        if not candidate["supporting_signal"] or not candidate["counter_signal"]:
            errors.append(f"{prefix}: supporting_signal and counter_signal are required")
        if candidate["research_status"] == "not_started" and "No atlas research anchor" not in candidate["research_check"]:
            errors.append(f"{prefix}: not_started candidate must say research was not used to form it")
        if not candidate["limits"]:
            errors.append(f"{prefix}: limits must not be empty")

    if len(ids) != len(set(ids)):
        errors.append("candidate_id values must be unique")
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print(f"VALID independent trend candidates: {len(candidates)} provisional candidates; research checks remain separate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
