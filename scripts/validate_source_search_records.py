#!/usr/bin/env python3
"""Validate the minimum metadata contract for project source-search records."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = re.compile(r"\[[^\]]+\]\(https?://[^)\s]+\)")


def metadata(text: str, label: str) -> str | None:
    match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+)$", text, re.M)
    return match.group(1).strip() if match else None


def source_rows(text: str) -> list[str]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| ID"):
            continue
        if URL.search(line):
            rows.append(line)
    return rows


def main() -> int:
    failures: list[tuple[str, str]] = []
    records = sorted((ROOT / "analysis/projects").glob("*/source-search-*.md"))
    for path in records:
        text = path.read_text(encoding="utf-8")
        required = {
            "title": bool(re.search(r"^# Source search:\s*.+$", text, re.M)),
            "search date": bool(metadata(text, "Search date")),
            "geography": bool(metadata(text, "Geography")),
            "status": bool(metadata(text, "Status")),
            "working question": bool(re.search(r"^## Working question\s*$", text, re.M)),
            "source table": bool(source_rows(text)),
        }
        for field, present in required.items():
            if not present:
                failures.append((str(path.relative_to(ROOT)), field))
    if failures:
        for path, field in failures:
            print(f"INVALID {path}: missing {field}")
        print(f"Checked {len(records)} source-search records; {len(failures)} failures", file=sys.stderr)
        return 1
    print(f"VALID source-search records: {len(records)} records checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
