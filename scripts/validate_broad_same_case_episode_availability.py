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
        if set(row["stage_status"]) != required_stages:
            raise ValueError(f"{row['source']} has incomplete stage status")
        if not (root / row["source"]).exists():
            raise FileNotFoundError(root / row["source"])
    print(f"VALID broad same-case episode availability audit: {len(rows)} local source surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
