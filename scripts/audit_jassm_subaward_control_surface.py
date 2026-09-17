#!/usr/bin/env python3
"""Summarize the local rich JASSM/LRASM subaward control surface."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=root / "analysis/projects/ai-work-control/data/usaspending-jassm-lrasm-rich-subaward-search-2026-09-14.json")
    parser.add_argument("--output", type=Path, default=root / "analysis/projects/ai-work-control/data/jassm-subaward-control-surface-audit-v1.json")
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    rows = data["response"]["results"]
    by_recipient = defaultdict(lambda: {"amount": 0.0, "rows": 0, "ueis": set(), "locations": set()})
    countries = Counter()
    states = Counter()
    descriptions = 0
    for row in rows:
        name = row.get("Sub-Awardee Name") or "unknown recipient"
        bucket = by_recipient[name]
        bucket["amount"] += float(row.get("Sub-Award Amount") or 0)
        bucket["rows"] += 1
        if row.get("Sub-Recipient UEI"):
            bucket["ueis"].add(row["Sub-Recipient UEI"])
        loc = row.get("Sub-Recipient Location") or {}
        if loc.get("state_code"):
            states[loc["state_code"]] += 1
        if loc.get("country_name"):
            countries[loc["country_name"]] += 1
        if loc.get("city_name") and loc.get("state_code"):
            bucket["locations"].add(f"{loc['city_name']}, {loc['state_code']}")
        if row.get("Sub-Award Description"):
            descriptions += 1
    total = sum(v["amount"] for v in by_recipient.values())
    recipients = []
    for name, value in sorted(by_recipient.items(), key=lambda item: item[1]["amount"], reverse=True):
        recipients.append({
            "recipient": name,
            "amount": round(value["amount"], 2),
            "share_of_rich_extract_percent": round(100 * value["amount"] / total, 4) if total else None,
            "row_count": value["rows"],
            "uei_count": len(value["ueis"]),
            "locations": sorted(value["locations"]),
        })
    result = {
        "format": "jassm-subaward-control-surface-audit-v1",
        "status": "supplier_visibility_audit_only",
        "checked": "2026-09-16",
        "source": str(args.input.relative_to(root)),
        "parent_award": "FA868224CB001",
        "rich_row_count": len(rows),
        "unique_recipient_name_count": len(recipients),
        "recipient_rows_with_descriptions": descriptions,
        "recipient_rows_with_uei": sum(1 for r in rows if r.get("Sub-Recipient UEI")),
        "recipient_rows_with_location": sum(1 for r in rows if (r.get("Sub-Recipient Location") or {}).get("city_name")),
        "total_rich_extract_amount": round(total, 2),
        "top_5_share_percent": round(sum(r["share_of_rich_extract_percent"] for r in recipients[:5]), 4) if recipients else 0,
        "state_row_counts": dict(states.most_common()),
        "country_row_counts": dict(countries.most_common()),
        "top_recipients": recipients[:20],
        "boundary": "The rich subaward extract makes recipient identity, descriptions, UEIs, and performance locations more visible for returned rows. It does not establish supplier ownership beyond separately resolved records, facility output, production quantity, delivered/accepted missiles, replaceability, workforce incidence, or geopolitical leverage.",
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    try:
        output_label = args.output.relative_to(root)
    except ValueError:
        output_label = args.output
    print(f"WROTE {output_label}")
    print(f"rows={len(rows)} recipients={len(recipients)} total={total:.2f} top5_share={result['top_5_share_percent']}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
