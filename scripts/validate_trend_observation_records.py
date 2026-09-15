#!/usr/bin/env python3
"""Validate machine-readable recurring-trend observation records."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "manifests/us-trend-observation-schema-v1.json").read_text())


def main() -> int:
    failures: list[str] = []
    records = sorted((ROOT / "analysis/records").glob("*.json"))
    for path in records:
        data = json.loads(path.read_text(encoding="utf-8"))
        for field in SCHEMA["required_record_fields"]:
            if field not in data:
                failures.append(f"{path.relative_to(ROOT)}: missing {field}")
        theme_ids = data.get("theme_ids", [])
        if not isinstance(theme_ids, list) or not theme_ids:
            failures.append(f"{path.relative_to(ROOT)}: theme_ids must be a non-empty list")
        else:
            invalid_themes = sorted(set(theme_ids) - set(SCHEMA["theme_id_values"]))
            if invalid_themes:
                failures.append(f"{path.relative_to(ROOT)}: invalid theme_ids: {', '.join(invalid_themes)}")
        program_theme_ids = data.get("program_theme_ids", [])
        valid_program_themes = {item["id"] for item in SCHEMA["program_theme_catalog"]}
        if not isinstance(program_theme_ids, list) or not program_theme_ids:
            failures.append(f"{path.relative_to(ROOT)}: program_theme_ids must be a non-empty list")
        else:
            invalid_program_themes = sorted(set(program_theme_ids) - valid_program_themes)
            if invalid_program_themes:
                failures.append(f"{path.relative_to(ROOT)}: invalid program_theme_ids: {', '.join(invalid_program_themes)}")
        observations = data.get("observations", [])
        if not observations:
            failures.append(f"{path.relative_to(ROOT)}: no observations")
        for index, observation in enumerate(observations):
            prefix = f"{path.relative_to(ROOT)} observation {index}"
            for field in SCHEMA["required_observation_fields"]:
                if field not in observation:
                    failures.append(f"{prefix}: missing {field}")
            denominator = observation.get("denominator", {})
            denominator_value = denominator.get("value")
            denominator_type = denominator.get("value_type")
            if isinstance(denominator_value, (int, float)) and denominator_value > 0:
                pass
            elif denominator_value is None and denominator_type == "not_disclosed" and denominator.get("unit"):
                # Preserve a genuinely unavailable study denominator explicitly;
                # do not force a fabricated count into the evidence object.
                pass
            else:
                failures.append(f"{prefix}: denominator must be positive or explicitly not_disclosed")
            if observation.get("status") not in SCHEMA["status_values"]:
                failures.append(f"{prefix}: invalid status")
            for name, measure in observation.get("measures", {}).items():
                if not isinstance(measure, dict) or "value" not in measure or "unit" not in measure or "value_type" not in measure:
                    failures.append(f"{prefix} measure {name}: missing value/unit/value_type")
    if failures:
        print("\n".join(failures))
        print(f"Checked {len(records)} trend records; {len(failures)} failures", file=sys.stderr)
        return 1
    print(f"VALID trend observation records: {len(records)} records checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
