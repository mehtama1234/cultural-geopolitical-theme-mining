#!/usr/bin/env python3
"""Check acquisition paths against the atlas storage policy.

This is a local, read-only check. It never downloads, deletes, or moves files.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


MB = 1024 * 1024


def inspect_path(path: Path, warn_bytes: int, block_bytes: int) -> dict:
    files = [path] if path.is_file() else [p for p in path.rglob("*") if p.is_file()]
    rows = []
    for item in sorted(files):
        size = item.stat().st_size
        if size > block_bytes:
            status = "block"
        elif size > warn_bytes:
            status = "ask"
        else:
            status = "allow"
        rows.append({"path": str(item), "bytes": size, "status": status})
    return {"path": str(path), "files": rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="+", type=Path)
    parser.add_argument("--warn-mb", type=float, default=25)
    parser.add_argument("--block-mb", type=float, default=100)
    args = parser.parse_args()
    if args.warn_mb <= 0 or args.block_mb <= args.warn_mb:
        parser.error("require 0 < --warn-mb < --block-mb")

    missing = [str(path) for path in args.path if not path.exists()]
    if missing:
        parser.error("path does not exist: " + ", ".join(missing))

    report = {
        "format": "acquisition-resource-policy-check-v1",
        "read_only": True,
        "warn_bytes": int(args.warn_mb * MB),
        "block_bytes": int(args.block_mb * MB),
        "paths": [
            inspect_path(path, int(args.warn_mb * MB), int(args.block_mb * MB))
            for path in args.path
        ],
    }
    rows = [row for group in report["paths"] for row in group["files"]]
    report["counts"] = {
        "files": len(rows),
        "allow": sum(row["status"] == "allow" for row in rows),
        "ask": sum(row["status"] == "ask" for row in rows),
        "block": sum(row["status"] == "block" for row in rows),
    }
    print(json.dumps(report, indent=2))
    return 1 if report["counts"]["block"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
