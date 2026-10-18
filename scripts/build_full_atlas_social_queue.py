#!/usr/bin/env python3
"""Build the deterministic record-level social augmentation queue."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "analysis" / "records"
OUT = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage.json"

THEME_MAP = {
    "household": "household-room-consumption",
    "cost": "household-room-consumption",
    "time": "time-care-social-reproduction",
    "consumer": "consumer-power-recourse",
    "platform": "platform-exit",
    "attention": "platform-exit",
    "work": "ai-work-control",
    "control": "ai-work-control",
    "care": "time-care-social-reproduction",
    "health": "time-care-social-reproduction",
    "housing": "housing-place-mobility",
    "place": "housing-place-mobility",
    "mobility": "housing-place-mobility",
    "unequal": "unequal-exposure-status",
    "status": "unequal-exposure-status",
    "trust": "trust-identity-cultural-meaning",
    "identity": "trust-identity-cultural-meaning",
    "meaning": "trust-identity-cultural-meaning",
    "public": "public-systems-policy-feedback",
    "policy": "public-systems-policy-feedback",
    "political": "political-judgment-collective-action",
    "action": "political-judgment-collective-action",
    "firm": "firm-sector-market-power",
    "sector": "firm-sector-market-power",
    "market": "firm-sector-market-power",
    "infrastructure": "infrastructure-technology-dependency",
    "technology": "infrastructure-technology-dependency",
    "dependency": "infrastructure-technology-dependency",
    "geopolitical": "geopolitical-state-consequences",
    "state": "geopolitical-state-consequences",
    "ai": "ai-work-control",
}

PROGRAM_THEME_MAP = {
    "household_room_consumption": "household-room-consumption",
    "time_hidden_price": "time-care-social-reproduction",
    "consumer_power_recourse": "consumer-power-recourse",
    "platforms_data_attention": "platform-exit",
    "work_control_bargaining": "ai-work-control",
    "care_health_reproduction": "care-health-social-reproduction",
    "housing_place_mobility": "housing-place-mobility",
    "unequal_exposure_status": "unequal-exposure-status",
    "trust_identity_meaning": "trust-identity-cultural-meaning",
    "public_systems_feedback": "public-systems-policy-feedback",
    "political_judgment_action": "political-judgment-collective-action",
    "firm_sector_market_power": "firm-sector-market-power",
    "infrastructure_technology_dependency": "infrastructure-technology-dependency",
    "geopolitical_state_consequences": "geopolitical-state-consequences",
}


def clean_terms(value: str, limit: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9'-]{2,}", value.lower())
    stop = {"the", "and", "for", "with", "from", "that", "this", "record", "source", "united", "states"}
    result: list[str] = []
    for word in words:
        if word in stop or word in result:
            continue
        result.append(word)
        if len(result) >= limit:
            break
    return result


def map_theme(record: dict) -> str:
    for program_theme in record.get("program_theme_ids", []):
        if program_theme in PROGRAM_THEME_MAP:
            return PROGRAM_THEME_MAP[program_theme]
    text = " ".join(
        [
            record.get("title", ""),
            " ".join(record.get("program_theme_ids", [])),
            " ".join(record.get("theme_ids", [])),
        ]
    ).lower()
    for token, theme in THEME_MAP.items():
        if token in text:
            return theme
    return "trust-identity-cultural-meaning"


def main() -> None:
    rows = []
    for path in sorted(ATLAS.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        trend_id = record.get("trend_id")
        if not trend_id:
            continue
        title = record.get("title", trend_id)
        source_unit = record.get("source_unit", "")
        geography = record.get("geography", "")
        theme = map_theme(record)
        terms = clean_terms(f"{title} {source_unit} {geography}")
        base_query = " ".join(terms)
        rows.append(
            {
                "atlas_record_id": trend_id,
                "atlas_record_path": str(path.relative_to(ROOT)),
                "canonical_theme": theme,
                "title": title,
                "geography": geography,
                "status": "queued",
                "batch_id": None,
                "platforms": {
                    platform: {
                        "status": "not_started",
                        "query": f"{base_query} {theme} 2025-10-17..2026-10-17",
                        "retrieved": None,
                        "result_or_gap": None,
                        "social_record_ids": [],
                    }
                    for platform in ("youtube", "reddit", "linkedin", "x")
                },
                "terminal_reason": None,
                "next_action": "run_public_or_authorized_platform_search",
            }
        )
    payload = {
        "schema": "full-atlas-social-coverage-v1",
        "generated": "2026-10-18",
        "atlas_record_count": len(rows),
        "terminal_states": ["augmented", "documented_access_gap", "not_socially_applicable"],
        "batch_size": 25,
        "rows": rows,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"BUILT full-atlas queue: {len(rows)} records -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
