#!/usr/bin/env python3
"""Validate broad-program counterexample coverage and source traceability."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


THEME_IDS = set(range(1, 15))
ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--register",
        type=Path,
        default=root / "analysis/US-BROAD-COUNTEREXAMPLE-REGISTER_V1.md",
    )
    args = parser.parse_args()
    text = args.register.read_text(encoding="utf-8")
    marker = "## Additional measured or bounded counterexamples already in the atlas"
    if marker not in text:
        raise ValueError("promoted counterexample section is missing")
    section = text.split(marker, 1)[1].split("## How to use the register", 1)[0]
    rows = [
        match.groups()
        for line in section.splitlines()
        if (match := ROW_RE.match(line))
        and match.group(1).strip().lower() not in {"themes", "---"}
    ]
    if not rows:
        raise ValueError("promoted counterexample table is empty")

    covered: set[int] = set()
    for themes, counterexample, _rules_out, boundary in rows:
        ids = {int(value) for value in re.findall(r"\b\d+\b", themes)}
        if not ids or not ids <= THEME_IDS:
            raise ValueError(f"invalid theme IDs in row: {themes}")
        if not counterexample.strip() or not boundary.strip():
            raise ValueError("counterexample rows require an observation and boundary")
        if not re.search(r"\[[^]]+\]\([^)]+\)", boundary):
            raise ValueError("counterexample row lacks a source link")
        covered |= ids

    missing = THEME_IDS - covered
    if missing:
        raise ValueError(f"themes lack a promoted counterexample: {sorted(missing)}")
    print(f"VALID broad counterexample register: {len(rows)} rows cover themes 1-14")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
