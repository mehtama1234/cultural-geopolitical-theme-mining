#!/usr/bin/env python3
"""Keep the reader-facing theme pulse visibly broad across all 14 lenses."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PULSE = ROOT / "analysis/US-BROAD-CURRENT-THEME-PULSE_V1.md"

EXPECTED = {
    1: "Unequal optionality",
    2: "Time is a hidden currency",
    3: "interface",
    4: "Cultural meaning",
    5: "Formal and informal support",
    6: "AI and digital systems",
    7: "Capacity does not",
    8: "Population movement",
    9: "Market and institutional power",
    10: "Domestic conditions",
    11: "Different realization clocks",
    12: "Control can improve",
    13: "Material progress",
    14: "Status changes",
}


def main() -> int:
    text = PULSE.read_text(encoding="utf-8")
    sections = {
        int(number): title
        for number, title in re.findall(r"^## (\d+)\. (.+)$", text, re.MULTILINE)
    }
    if sorted(sections) != list(range(1, 15)):
        raise SystemExit(f"theme pulse must expose contiguous sections 1-14; found {sorted(sections)}")
    for number, fragment in EXPECTED.items():
        if fragment.lower() not in sections[number].lower():
            raise SystemExit(f"theme pulse section {number} does not preserve expected broad lens: {fragment}")
    print("VALID broad theme pulse: 14 contiguous macro sections preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
