#!/usr/bin/env python3
"""Validate the broad same-case episode availability audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = {
    "source",
    "unit",
    "records",
    "stage_status",
    "boundary",
}

REQUIRED_TOP_LEVEL = {
    "format",
    "status",
    "checked",
    "purpose",
    "required_stages",
    "stage_summary_rule",
    "stage_summary",
    "sources",
    "result",
    "next_test",
    "promotion_gate",
    "storage_boundary",
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--audit",
        type=Path,
        default=root / "analysis/data/broad-same-case-episode-availability-audit-v1.json",
    )
    args = parser.parse_args()
    data = json.loads(args.audit.read_text(encoding="utf-8"))
    missing_top_level = REQUIRED_TOP_LEVEL - set(data)
    if missing_top_level:
        raise ValueError(f"audit missing top-level fields: {sorted(missing_top_level)}")
    if data.get("status") != "stage_availability_audit":
        raise ValueError("audit must remain a stage availability audit")
    required_stages = set(data.get("required_stages", []))
    if len(required_stages) != 9:
        raise ValueError("audit must define nine required stages")
    rows = data.get("sources", [])
    if len(rows) < 3:
        raise ValueError("audit requires at least three source surfaces")
    for row in rows:
        missing = REQUIRED - set(row)
        if missing:
            raise ValueError(f"{row.get('source')} missing {sorted(missing)}")
        source = Path(row["source"])
        if source.is_absolute() or ".." in source.parts:
            raise ValueError(f"source must be a repository-relative path: {row['source']}")
        if not isinstance(row["records"], int) or row["records"] < 0:
            raise ValueError(f"{row['source']} records must be a nonnegative integer")
        if set(row["stage_status"]) != required_stages:
            raise ValueError(f"{row['source']} has incomplete stage status")
        if not (root / source).is_file():
            raise FileNotFoundError(root / source)
    if set(data["stage_summary"]) != required_stages:
        raise ValueError("stage summary must cover every required stage")
    for stage in required_stages:
        summary = data["stage_summary"][stage]
        if set(summary) != {"observed", "partial", "open_or_unknown"}:
            raise ValueError(f"{stage} has incomplete stage summary")
        computed = {
            "observed": sum(row["stage_status"][stage].startswith("observed") for row in rows),
            "partial": sum(row["stage_status"][stage].startswith("partial") for row in rows),
            "open_or_unknown": sum(
                not row["stage_status"][stage].startswith(("observed", "partial"))
                for row in rows
            ),
        }
        if summary != computed:
            raise ValueError(f"{stage} stage summary does not match source rows")
    gate = data["promotion_gate"]
    if gate.get("qualifies") is not False:
        raise ValueError("current audit must not qualify a new end-to-end finding")
    if gate.get("alternative_or_nonuse_observed_surfaces") != data["stage_summary"]["alternative_or_nonuse"]["observed"]:
        raise ValueError("promotion gate alternative count does not match stage summary")
    if gate.get("verified_remedy_or_outcome_followup_observed_surfaces") != 0:
        raise ValueError("promotion gate currently requires zero observed verified-remedy/outcome-follow-up surfaces")
    if not gate.get("rule") or not gate.get("failure_reason"):
        raise ValueError("promotion gate must state its rule and current failure reason")
    print(f"VALID broad same-case episode availability audit: {len(rows)} local source surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
