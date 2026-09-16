#!/usr/bin/env python3
"""Validate the local AI/work-control endpoint audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = {"source", "unit", "exposure_or_implementation", "worker_voice_or_control", "worker_outcome", "boundary"}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=root / "analysis/projects/ai-work-control/data/ai-work-control-endpoint-audit-v1.json")
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    if data.get("status") != "coverage_audit_only":
        raise ValueError("manifest must remain coverage_audit_only")
    rows = data.get("sources", [])
    for row in rows:
        missing = REQUIRED - set(row)
        if missing:
            raise ValueError(f"{row.get('source')} missing {sorted(missing)}")
        if not (root / row["source"]).exists():
            raise FileNotFoundError(root / row["source"])
    print(f"VALID AI/work-control endpoint audit: {len(rows)} local source rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
