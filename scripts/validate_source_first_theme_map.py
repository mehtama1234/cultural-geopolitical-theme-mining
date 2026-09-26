#!/usr/bin/env python3
"""Keep the broad theme map anchored to the available source corpus."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "analysis/US-BROAD-THEME-SUBTHEME-MAP_V1.md"

REQUIRED_FRAGMENTS = (
    "## Start from the source corpus",
    "The starting point is the available evidence, not a preferred story",
    "machine-readable record",
    "source unit,",
    "denominator, measures, method, uncertainty,",
    "counterinterpretation, and source URL",
    "Do not pool their percentages",
    "[the source registry](us-trend-observations.md)",
    "[machine-generated theme coverage view](us-trend-theme-coverage.md)",
    "[evidence matrix](US-BROAD-EVIDENCE-MATRIX_V1.md)",
    "[coverage matrix](US-BROAD-THEME-COVERAGE-MATRIX_V1.md)",
    "[current theme pulse](US-BROAD-CURRENT-THEME-PULSE_V1.md)",
)


def main() -> int:
    text = MAP.read_text(encoding="utf-8")
    missing = [fragment for fragment in REQUIRED_FRAGMENTS if fragment not in text]
    if missing:
        raise SystemExit(f"source-first theme-map contract missing: {missing}")

    sections = {
        int(number): title
        for number, title in re.findall(r"^## (\d+)\. (.+)$", text, re.MULTILINE)
    }
    if sorted(sections) != list(range(1, 15)):
        raise SystemExit(
            "source-first theme map must retain contiguous sections 1-14; "
            f"found {sorted(sections)}"
        )

    print("VALID source-first theme map: corpus workflow and 14-theme navigation preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
