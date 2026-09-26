#!/usr/bin/env python3
"""Audit direct source-record promotion into the broad reader syntheses.

This is a routing control, not a quality score. A record absent from the broad
reader documents can still be represented indirectly by a project finding.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "analysis" / "records"
CATALOG = ROOT / "manifests" / "us-trend-observation-schema-v1.json"
READER_FILES = (
    ROOT / "analysis" / "US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md",
    ROOT / "analysis" / "US-BROAD-SOCIETAL-SUBTHEME-CONCEPT-REGISTER_V1.md",
    ROOT / "analysis" / "US-BROAD-THEME-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-CONSUMER-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-PLATFORM-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-CARE-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-CULTURAL-POLITICAL-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-GEOPOLITICAL-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-WORK-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-HOUSING-PLACE-MOBILITY-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-UNEQUAL-EXPOSURE-STATUS-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-HOUSEHOLD-ROOM-CONSUMPTION-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-FIRM-SECTOR-MARKET-POWER-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-INFRASTRUCTURE-TECHNOLOGY-DEPENDENCY-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-SOCIAL-INFRASTRUCTURE-CIVIC-CAPACITY-SOURCE-LED-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-TIME-HIDDEN-PRICE-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-CROSS-LANE-TREND-PORTFOLIO_V1.md",
    ROOT / "analysis" / "US-BROAD-PUBLIC-SYSTEMS-SOURCE-LED-SUBTHEME-MAP_V1.md",
    ROOT / "analysis" / "US-BROAD-EXTERNAL-DATA-FIRST-PASS_2026-09-25.md",
)
OUTPUT_MD = ROOT / "analysis" / "US-BROAD-SOURCE-PROMOTION-AUDIT_V1.md"
OUTPUT_JSON = ROOT / "analysis" / "US-BROAD-SOURCE-PROMOTION-AUDIT_V1.json"


def main() -> int:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["program_theme_catalog"]
    names = {item["id"]: item["title"] for item in catalog}
    reader_text = "\n".join(path.read_text(encoding="utf-8") for path in READER_FILES)
    records = []
    for path in sorted(RECORDS.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        # Trend identifiers are stable analytical names, but they do not have
        # to mirror a renamed record filename. Keep the source path so generated
        # Markdown links always resolve to the actual corpus file.
        record["_record_path"] = path
        records.append(record)

    total = Counter()
    direct = Counter()
    candidates: dict[str, list[dict]] = defaultdict(list)
    directly_promoted = []
    for record in records:
        is_direct = record["trend_id"] in reader_text
        if is_direct:
            directly_promoted.append(record["trend_id"])
        for theme in record.get("program_theme_ids", []):
            total[theme] += 1
            if is_direct:
                direct[theme] += 1
            else:
                candidates[theme].append(record)

    rows = []
    for theme in names:
        unpromoted = total[theme] - direct[theme]
        rows.append(
            {
                "theme_id": theme,
                "theme": names[theme],
                "records": total[theme],
                "directly_promoted_records": direct[theme],
                "not_directly_named": unpromoted,
            }
        )
    rows.sort(key=lambda row: (-row["not_directly_named"], row["theme"]))
    low_density = sorted(rows, key=lambda row: (row["records"], row["theme"]))[:4]
    payload = {
        "format": "us-broad-source-promotion-audit-v1",
        "scope": "Exact trend_id mentions, including explicit record links, in the central synthesis, societal subtheme register, broad theme map, or source-led subtheme maps.",
        "reader_files": [str(path.relative_to(ROOT)) for path in READER_FILES],
        "total_records": len(records),
        "directly_promoted_record_count": len(directly_promoted),
        "themes": rows,
        "low_density_theme_candidates": {
            row["theme_id"]: [
                {"trend_id": record["trend_id"], "title": record["title"]}
                for record in sorted(candidates[row["theme_id"]], key=lambda item: item["title"])[:12]
            ]
            for row in low_density
        },
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# US broad source-promotion audit v1",
        "",
        "**Purpose:** distinguish records available in the source corpus from records directly named in the broad reader syntheses.",
        "",
        "This is a routing control, not an evidence-quality, importance, or omission score. A record not directly named here can still be represented indirectly by a project finding or cross-source bridge. Direct promotion means its exact trend ID appears in the [central synthesis](US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md), [societal subtheme register](US-BROAD-SOCIETAL-SUBTHEME-CONCEPT-REGISTER_V1.md), [broad theme map](US-BROAD-THEME-SUBTHEME-MAP_V1.md), or one of the [source-led subtheme maps](US-BROAD-CONSUMER-SOURCE-LED-SUBTHEME-MAP_V1.md).",
        "",
        f"The current corpus has **{len(records)} records**; **{len(directly_promoted)}** are directly named in at least one of those reader documents.",
        "",
        "## Direct-ID promotion by theme",
        "",
        "| Theme | Corpus records | Directly named | Not directly named |",
        "|---|---:|---:|---:|",
    ]
    lines.extend(
        f"| {row['theme']} | {row['records']} | {row['directly_promoted_records']} | {row['not_directly_named']} |"
        for row in rows
    )
    lines.extend([
        "",
        "## Candidate pool for the four lowest-density theme surfaces",
        "",
        "These are alphabetized direct-ID candidates, not ranked recommendations. The next pass should choose one only if it advances a genuinely different unit or stage and preserves the source boundary.",
    ])
    for row in low_density:
        lines.extend(["", f"### {row['theme']}", ""])
        for record in sorted(candidates[row["theme_id"]], key=lambda item: item["title"])[:12]:
            path = f"records/{record['_record_path'].name}"
            lines.append(f"- [{record['title']}]({path})")
    lines.extend([
        "",
        "The machine-readable counterpart is [the promotion audit JSON](US-BROAD-SOURCE-PROMOTION-AUDIT_V1.json).",
        "",
        "Generated by `scripts/audit_source_promotion.py` from `analysis/records/*.json` and the named reader documents.",
    ])
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {OUTPUT_MD}")
    print(f"WROTE {OUTPUT_JSON}")
    print(f"AUDITED {len(records)} records; {len(directly_promoted)} directly named in broad readers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
