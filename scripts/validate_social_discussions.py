#!/usr/bin/env python3
"""Validate the bounded public-discussion evidence layer."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "analysis" / "social-discussions"
SCHEMA = json.loads((BASE / "schema.json").read_text(encoding="utf-8"))


def main() -> int:
    records_dir = BASE / "records"
    records = []
    errors: list[str] = []
    for path in sorted(records_dir.glob("*.json")):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        records.append(record)
        missing = [key for key in SCHEMA["required"] if key not in record]
        if missing:
            errors.append(f"{path}: missing {', '.join(missing)}")
            continue
        if record["platform"] not in SCHEMA["platforms"]:
            errors.append(f"{path}: unsupported platform {record['platform']!r}")
        parsed = urlparse(record["canonical_url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"{path}: canonical_url is not an absolute URL")
        if not isinstance(record["classification"], list) or not record["classification"]:
            errors.append(f"{path}: classification must be a non-empty list")
        if not isinstance(record["research_anchor_paths"], list) or not record["research_anchor_paths"]:
            errors.append(f"{path}: research_anchor_paths must be a non-empty list")
        if not isinstance(record["limits"], list) or not record["limits"]:
            errors.append(f"{path}: limits must be a non-empty list")

    ids = [record.get("record_id") for record in records]
    duplicate_ids = sorted({record_id for record_id in ids if ids.count(record_id) > 1})
    if duplicate_ids:
        errors.append(f"duplicate record_id values: {', '.join(duplicate_ids)}")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1

    by_platform: dict[str, int] = {}
    by_topic: dict[str, int] = {}
    for record in records:
        by_platform[record["platform"]] = by_platform.get(record["platform"], 0) + 1
        by_topic[record["topic"]] = by_topic.get(record["topic"], 0) + 1
    print(f"VALID social discussions: {len(records)} records; platforms={by_platform}; topics={by_topic}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
