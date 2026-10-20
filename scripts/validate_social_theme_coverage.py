#!/usr/bin/env python3
"""Validate dated social coverage or documented access gaps for all 14 themes."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage.json"
THEMES = {
    "household-room-consumption",
    "time-care-social-reproduction",
    "consumer-power-recourse",
    "platform-exit",
    "ai-work-control",
    "care-health-social-reproduction",
    "housing-place-mobility",
    "unequal-exposure-status",
    "trust-identity-cultural-meaning",
    "public-systems-policy-feedback",
    "political-judgment-collective-action",
    "firm-sector-market-power",
    "infrastructure-technology-dependency",
    "geopolitical-state-consequences",
}
TERMINAL = {"augmented", "documented_access_gap", "not_socially_applicable"}
PLATFORMS = ("youtube", "reddit", "linkedin", "x")


def main() -> int:
    payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])
    by_theme: dict[str, list[dict]] = {theme: [] for theme in THEMES}
    errors: list[str] = []
    for row in rows:
        theme = row.get("canonical_theme")
        if theme not in THEMES:
            errors.append(f"unexpected or missing canonical theme: {theme!r}")
            continue
        by_theme[theme].append(row)
        if row.get("status") not in TERMINAL:
            errors.append(f"{row.get('atlas_record_id')}: non-terminal status")
        for platform in PLATFORMS:
            attempt = row.get("platforms", {}).get(platform, {})
            if not attempt.get("retrieved"):
                errors.append(f"{row.get('atlas_record_id')}/{platform}: missing retrieval date")
    for theme, theme_rows in sorted(by_theme.items()):
        if not theme_rows:
            errors.append(f"{theme}: no dated social wave or access-gap row")
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    counts = Counter(row["status"] for row in rows)
    print(
        f"VALID 14-theme social coverage: {len(THEMES)} themes, "
        f"{len(rows)} dated rows, statuses={dict(sorted(counts.items()))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
