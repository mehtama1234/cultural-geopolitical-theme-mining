#!/usr/bin/env python3
"""Validate the machine-readable six-tension synthesis against the 14 themes."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "analysis/data/us-broad-macro-tensions-v1.json"
SCHEMA = ROOT / "manifests/us-trend-observation-schema-v1.json"


def main() -> int:
    register = json.loads(REGISTER.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    catalog = {item["id"] for item in schema["program_theme_catalog"]}
    tensions = register.get("tensions", [])
    if len(tensions) != 6:
        raise SystemExit(f"expected 6 macro tensions, found {len(tensions)}")

    ids = [item.get("id") for item in tensions]
    if any(not item for item in ids) or len(set(ids)) != len(ids):
        raise SystemExit("macro tension IDs must be present and unique")

    used = {theme for item in tensions for theme in item.get("themes", [])}
    unknown = used - catalog
    missing = catalog - used
    if unknown:
        raise SystemExit(f"macro register uses unknown themes: {sorted(unknown)}")
    if missing:
        raise SystemExit(f"macro register omits canonical themes: {sorted(missing)}")

    required = {"name", "themes", "test", "evidence_boundary"}
    for item in tensions:
        absent = required - item.keys()
        if absent:
            raise SystemExit(f"macro tension {item.get('id')} missing: {sorted(absent)}")

    sequence = register.get("end_to_end_sequence", [])
    if len(sequence) < 6:
        raise SystemExit("macro register end-to-end sequence is too short")

    print(f"VALID macro tension register: {len(tensions)} tensions cover {len(used)} canonical themes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
