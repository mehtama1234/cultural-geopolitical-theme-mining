#!/usr/bin/env python3
"""Audit record and observation density across the 14-theme broad atlas."""
from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD_DIR = ROOT / "analysis/records"
OUT_JSON = ROOT / "analysis/US-BROAD-THEME-BALANCE-AUDIT_V1.json"
OUT_MD = ROOT / "analysis/US-BROAD-THEME-BALANCE-AUDIT_V1.md"

THEMES = [
    ("household_room_consumption", "Household room and consumption"),
    ("time_hidden_price", "Time, care, and social reproduction"),
    ("consumer_power_recourse", "Consumer power and recourse"),
    ("platforms_data_attention", "Platforms, data, and attention"),
    ("work_control_bargaining", "Work, control, and bargaining"),
    ("care_health_reproduction", "Care, health, and reproduction"),
    ("housing_place_mobility", "Housing, place, and mobility"),
    ("unequal_exposure_status", "Unequal exposure and status"),
    ("trust_identity_meaning", "Trust, identity, and meaning"),
    ("public_systems_feedback", "Public systems and policy feedback"),
    ("political_judgment_action", "Political judgment and collective action"),
    ("firm_sector_market_power", "Firm, sector, and market power"),
    ("infrastructure_technology_dependency", "Infrastructure, technology, and dependency"),
    ("geopolitical_state_consequences", "Geopolitical and state consequences"),
]

records = [json.loads(path.read_text()) for path in sorted(RECORD_DIR.glob("*.json"))]
record_counts = Counter(theme for record in records for theme in record.get("program_theme_ids", []))
observation_counts = Counter(
    theme
    for record in records
    for theme in record.get("program_theme_ids", [])
    for _ in record.get("observations", [])
)
rows = []
for rank, (theme_id, title) in enumerate(sorted(THEMES, key=lambda item: (record_counts[item[0]], item[1])), 1):
    rows.append({
        "rank_by_record_density": rank,
        "theme_id": theme_id,
        "theme": title,
        "records": record_counts[theme_id],
        "observations": observation_counts[theme_id],
    })

lowest_density_titles = [row["theme"] for row in rows[:3]]
lowest_density_text = ", ".join(f"**{title}**" for title in lowest_density_titles[:-1])
lowest_density_text += f", and **{lowest_density_titles[-1]}**"

payload = {
    "checked": date.today().isoformat(),
    "record_count": len(records),
    "theme_count": len(THEMES),
    "rows": rows,
    "interpretation": {
        "purpose": "coverage-balance control, not a quality or causal-strength score",
        "lowest_density_themes": [row["theme_id"] for row in rows[:3]],
        "next_rotation_rule": "prioritize a distinct unit or conversion stage in a low-density theme; do not add another aggregate endpoint merely to equalize counts",
    },
}
OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")

lines = [
    "# US broad theme balance audit v1",
    "",
    f"**Checked:** {payload['checked']}",
    "**Purpose:** identify under-covered parts of the 14-theme atlas before the next research rotation.",
    "",
    "This is a coverage-control artifact, not a quality ranking, sample-size measure, causal-strength score, or claim that a theme with fewer records matters less. Record counts reflect the current machine-readable registry and can be shaped by source availability and project history.",
    "",
    f"The registry currently contains **{len(records)} records** across **{len(THEMES)} themes**. The three lowest-density surfaces are {lowest_density_text}.",
    "",
    "## Density by theme",
    "",
    "| Rank (lowest first) | Theme | Records | Observations |",
    "|---:|---|---:|---:|",
]
for row in rows:
    lines.append(f"| {row['rank_by_record_density']} | {row['theme']} | {row['records']} | {row['observations']} |")
lines += [
    "",
    "## How to use this",
    "",
    "The next breadth rotation should give first consideration to a low-density theme only when it adds a genuinely different unit or stage: encounter-to-interpretation-to-action for digital life; allocation of paid and unpaid time, care continuity, or social participation for time/care; and acceptance, operation, public consent, alliance behavior, or external response for geopolitical/state capability.",
    "",
    "Do not manufacture balance by adding another announcement, aggregate attitude snapshot, procurement commitment, or platform-reach statistic. A thin theme with a strong missing middle is more valuable than a dense theme with another endpoint duplicate.",
    "",
    "The machine-readable source is [the balance audit JSON](US-BROAD-THEME-BALANCE-AUDIT_V1.json).",
]
OUT_MD.write_text("\n".join(lines) + "\n")
print(f"WROTE {OUT_JSON}")
print(f"WROTE {OUT_MD}")
