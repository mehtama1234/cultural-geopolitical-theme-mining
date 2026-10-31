#!/usr/bin/env python3
"""Map social-publication citations to atlas themes without inferring prevalence."""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "social-publication-citation-map.json"
REPO = "/home/mehta/git-repo/social-research"
REVISION = "c2ff3e3a49129117802425514660ce4b2cf67744"
APPENDIX = "analysis/social/publication-evidence-appendix.md"
REPORT = "analysis/social/integrated-trend-atlas-report.json"


def main() -> int:
    appendix = subprocess.check_output(["git", "-C", REPO, "show", f"{REVISION}:{APPENDIX}"], text=True)
    report = json.loads(subprocess.check_output(["git", "-C", REPO, "show", f"{REVISION}:{REPORT}"], text=True))
    current_section = None
    linked_rows = []
    for line_number, line in enumerate(appendix.splitlines(), start=1):
        heading = re.match(r"^### (.+)$", line)
        if heading:
            current_section = heading.group(1)
        match = re.match(r"^- (.+?) · (.+?) · (https?://\S+)$", line)
        if match and current_section:
            label, category, url = match.groups()
            linked_rows.append(
                {
                    "theme": current_section,
                    "label": label,
                    "category": category,
                    "url": url.rstrip("`),."),
                    "publisher_host": urlparse(url).netloc.lower(),
                    "appendix_line": line_number,
                    "lineage_status": "theme_linked_citation",
                    "rights_status": "not_yet_verified",
                    "independence_status": "not_reviewed",
                }
            )
    raw_urls = sorted(set(re.findall(r"https?://[^ )>`]+", appendix)))
    # The appendix contains a few URLs split across Markdown line continuations
    # (for example a trailing ``\n-``). Preserve the raw count but normalize
    # those artifacts before lineage comparison.
    all_urls = sorted({url.replace("\n-", "").rstrip("`),.\"]") for url in raw_urls})
    linked_urls = {row["url"] for row in linked_rows}
    rows = linked_rows + [
        {
            "url": url,
            "publisher_host": urlparse(url).netloc.lower(),
            "theme": None,
            "lineage_status": "appendix_url_unmapped",
            "rights_status": "not_yet_verified",
            "independence_status": "not_reviewed",
        }
        for url in all_urls
        if url not in linked_urls
    ]
    payload = {
        "schema": "external-trend-intelligence.social-publication-citation-map.v1",
        "source_family": "social-research",
        "source_revision": REVISION,
        "source_path": APPENDIX,
        "atlas_report_path": REPORT,
        "atlas_theme_count": report["counts"]["themes"],
        "atlas_cross_theme_finding_count": report["counts"]["cross_theme_findings"],
        "appendix_raw_url_count": len(raw_urls),
        "appendix_url_count": len(all_urls),
        "theme_linked_citation_count": len(linked_rows),
        "theme_linked_unique_url_count": len(linked_urls),
        "unmapped_url_count": len(set(all_urls) - linked_urls),
        "raw_url_normalization_count": len(raw_urls) - len(all_urls),
        "publisher_host_count": len({row["publisher_host"] for row in rows}),
        "theme_counts": dict(sorted(Counter(row["theme"] for row in linked_rows).items())),
        "rows": rows,
        "boundary": "This map links selected publication citations to social-atlas themes and preserves the remaining appendix URLs as unmapped. Platform discussion and creator signals are bounded signals, not representative prevalence, causality, market size, or buying intent.",
        "next_test": "Map the remaining URLs to specific atlas claims, verify publisher and collection lineage, and compare each material claim with an independent population or outcome source before promotion.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(linked_rows)} theme-linked citations; {len(all_urls)} URLs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
