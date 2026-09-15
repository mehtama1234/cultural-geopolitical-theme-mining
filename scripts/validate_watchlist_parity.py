#!/usr/bin/env python3
"""Ensure the published vintage-watchlist page exposes its maintained lanes."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = ROOT / "analysis/US-RECURRENT-SOURCE-VINTAGE-WATCHLIST_V1.md"
HTML = ROOT / "site/US-RECURRENT-SOURCE-VINTAGE-WATCHLIST_V1.html"

REQUIRED_LABELS = [
    "CMS National Health Expenditure Accounts",
    "MEPS / Panel 27 and HC-256",
    "GSS / NORC",
    "Federal Reserve SHED",
    "Census HTOPS/HPS",
    "CFPB Consumer Complaint Database",
    "PSID",
    "World Bank Enterprise Surveys",
]


def main() -> int:
    markdown = MARKDOWN.read_text(encoding="utf-8")
    html = HTML.read_text(encoding="utf-8")
    missing_markdown = [label for label in REQUIRED_LABELS if label not in markdown]
    # HTML uses compact display labels for a few combined rows.
    html_aliases = {
        "CMS National Health Expenditure Accounts": "CMS NHEA",
        "CFPB Consumer Complaint Database": "CFPB complaint database",
        "World Bank Enterprise Surveys": "World Bank Enterprise Surveys",
    }
    missing_html = [
        label for label in REQUIRED_LABELS
        if html_aliases.get(label, label) not in html
    ]
    if missing_markdown or missing_html:
        if missing_markdown:
            print("Markdown watchlist missing: " + ", ".join(missing_markdown))
        if missing_html:
            print("HTML watchlist missing: " + ", ".join(missing_html))
        return 1
    print(f"VALID watchlist parity: {len(REQUIRED_LABELS)} maintained lanes visible in Markdown and HTML")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
