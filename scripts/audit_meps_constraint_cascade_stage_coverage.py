#!/usr/bin/env python3
"""Audit stage coverage in the privacy-minimized local MEPS event ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


STAGES = (
    "trigger",
    "practical_room_and_alternatives",
    "choice_and_tradeoff",
    "institutional_route",
    "remedy_verification",
    "followup_outcomes",
    "meaning_and_action",
)
WINDOW_RE = re.compile(r"strict R3/1-to-R4/2 event window=(yes|no|unknown)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_jsonl", type=Path)
    parser.add_argument("--output-json", type=Path, required=True)
    return parser.parse_args()


def pct(count: int, total: int) -> float:
    return round((100.0 * count / total), 4) if total else 0.0


def main() -> int:
    args = parse_args()
    rows = 0
    evidence_status = Counter()
    family_counts = Counter()
    window_counts = Counter()
    stage_counts = {stage: Counter() for stage in STAGES}
    family_stage_counts = defaultdict(lambda: {stage: Counter() for stage in STAGES})

    with args.input_jsonl.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            rows += 1
            evidence_status[row.get("evidence_status", "missing")] += 1
            episode_id = str(row.get("episode_id", ""))
            family = episode_id.split("-", 2)[1] if episode_id.count("-") >= 2 else "unknown"
            family_counts[family] += 1
            match = WINDOW_RE.search(str(row.get("trigger", "")))
            window_counts[match.group(1) if match else "unknown"] += 1
            stages = row.get("stages", {})
            for stage in STAGES:
                status = stages.get(stage, {}).get("status", "missing")
                stage_counts[stage][status] += 1
                family_stage_counts[family][stage][status] += 1

    if rows == 0:
        raise SystemExit("input ledger contains no rows")

    def counts_with_rates(counter: Counter) -> dict[str, dict[str, float | int]]:
        return {
            key: {"count": count, "percent_of_rows": pct(count, rows)}
            for key, count in sorted(counter.items())
        }

    output = {
        "schema": "us-household-constraint-cascade-stage-coverage-audit-v1",
        "status": "local_staging_only",
        "input_jsonl": str(args.input_jsonl),
        "input_sha256": hashlib.sha256(args.input_jsonl.read_bytes()).hexdigest(),
        "rows": rows,
        "family_counts": dict(sorted(family_counts.items())),
        "strict_interround_window": counts_with_rates(window_counts),
        "evidence_status": counts_with_rates(evidence_status),
        "stage_coverage": {
            stage: counts_with_rates(stage_counts[stage]) for stage in STAGES
        },
        "stage_coverage_by_family": {
            family: {
                stage: dict(sorted(statuses.items()))
                for stage, statuses in sorted(stage_map.items())
            }
            for family, stage_map in sorted(family_stage_counts.items())
        },
        "interpretation": (
            "This is an evidence-boundary audit, not a population estimate or causal finding. "
            "Observed event/payment context and reported round proxies do not establish an "
            "event-specific household cascade."
        ),
        "limitations": [
            "The underlying need, alternatives, event-specific choice, and household trade-off are not observed.",
            "Institutional route fields are round-level denial/prior-authorization proxies, not responses or appeals.",
            "Verified remedy, event-specific recovery, trust, action, switching, and exit are not observed.",
            "The strict inter-round flag is temporal context, not proof of causation.",
        ],
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
