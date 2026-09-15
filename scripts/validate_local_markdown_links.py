#!/usr/bin/env python3
"""Validate relative Markdown links in the research workspace."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_SCHEMES = {"http", "https", "mailto", "tel"}


def local_target(raw: str) -> str | None:
    target = raw.strip().strip("<>").split()[0]
    parsed = urlsplit(target)
    if parsed.scheme in SKIP_SCHEMES or target.startswith("#"):
        return None
    return unquote(parsed.path)


def main() -> int:
    failures: list[tuple[str, str, str]] = []
    files = sorted(ROOT.rglob("*.md"))
    for path in files:
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = local_target(raw)
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                failures.append((str(path.relative_to(ROOT)), raw, "outside workspace"))
                continue
            if not resolved.exists():
                failures.append((str(path.relative_to(ROOT)), raw, str(resolved.relative_to(ROOT))))
    if failures:
        for source, raw, reason in failures:
            print(f"BROKEN {source}: {raw} -> {reason}")
        print(f"Checked {len(files)} Markdown files; {len(failures)} broken local links", file=sys.stderr)
        return 1
    print(f"VALID local Markdown links: {len(files)} files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
