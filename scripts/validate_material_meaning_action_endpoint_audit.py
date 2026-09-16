#!/usr/bin/env python3
"""Validate the local material-to-meaning/action endpoint audit manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = {"source", "unit", "material_surface", "meaning_surface", "action_surface", "time_order", "event_actor", "boundary"}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=root / "analysis/projects/us-cost-trust-politics/data/material-meaning-action-endpoint-audit-v1.json")
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    if data.get("status") != "coverage_audit_only":
        raise ValueError("manifest must remain coverage_audit_only")
    rows = data.get("sources", [])
    if not rows:
        raise ValueError("manifest needs source rows")
    for row in rows:
        missing = REQUIRED - set(row)
        if missing:
            raise ValueError(f"{row.get('source')} missing {sorted(missing)}")
        source = root / row["source"]
        if not source.exists():
            raise FileNotFoundError(source)
    print(f"VALID material-to-meaning/action endpoint audit: {len(rows)} local source rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
