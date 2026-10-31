#!/usr/bin/env python3
"""Snapshot the upstream external source inventory without restoring deleted files."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "source-registry-snapshot.json"
REGISTRY_PATH = "manifests/source-registry.json"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--git-ref", default="HEAD")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    raw = subprocess.check_output(
        ["git", "show", f"{args.git_ref}:{REGISTRY_PATH}"], cwd=ROOT, text=True
    )
    registry = json.loads(raw)
    sources = registry["sources"]
    required = {"id", "name", "url", "role", "source_types", "license_note", "access_notes"}
    if registry.get("format") != "cultural-geopolitical-theme-mining-source-registry-v1":
        raise ValueError("unexpected upstream source registry format")
    if not sources or any(set(source) != required for source in sources):
        raise ValueError("source registry entries do not match the expected schema")
    if len({source["id"] for source in sources}) != len(sources):
        raise ValueError("source IDs are not unique")

    snapshot = {
        "schema": "external-trend-intelligence.source-registry-snapshot.v1",
        "source_git_ref": args.git_ref,
        "upstream_registry_path": REGISTRY_PATH,
        "upstream_format": registry["format"],
        "source_count": len(sources),
        "boundary": (
            "This is an inventory of candidate external source families. It does not prove "
            "current availability, access rights, licensing, freshness, or independent evidence. "
            "Those checks occur when observations are captured and lineage is audited."
        ),
        "sources": [
            {
                "id": source["id"],
                "name": source["name"],
                "url": source["url"],
                "role": source["role"],
                "source_types": source["source_types"],
                "license_note": source["license_note"],
                "access_notes": source["access_notes"],
            }
            for source in sources
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {args.output} ({len(sources)} sources)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
