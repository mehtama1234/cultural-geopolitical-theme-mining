#!/usr/bin/env python3
"""Normalize the pinned annual-report public citation table for lineage review."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "annual-report-citation-map.json"
REPO = "/home/mehta/git-repo/organization-intelligence-system"
REVISION = "5d4434b9ff46e8d28176624a7ec44dfddee8be4b"
PATH = "annual-report-research/analysis/company-first-principles/annual-report-public-citation-source-list-pass-1.md"


def main() -> int:
    text = subprocess.check_output(["git", "-C", REPO, "show", f"{REVISION}:{PATH}"], text=True)
    lines = [line for line in text.splitlines() if line.startswith("| ARPCSL-")]
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 10:
            raise ValueError(f"unexpected citation row with {len(cells)} cells: {line}")
        citation_id, packet, company, period, doc_type, url, local_path, use, status, boundary = cells
        rows.append(
            {
                "citation_source_id": citation_id,
                "source_packet": packet,
                "company": company,
                "period": period,
                "document_type": doc_type,
                "public_url": url,
                "publisher_host": urlparse(url).netloc.lower(),
                "local_path": local_path.strip("`") if local_path != "—" else None,
                "article_use": use,
                "citation_status": status,
                "boundary": boundary,
                "lineage_status": "source_row_pinned",
                "rights_status": "not_yet_verified",
                "independence_status": "not_reviewed",
            }
        )
    by_packet = {}
    for row in rows:
        by_packet.setdefault(row["source_packet"], 0)
        by_packet[row["source_packet"]] += 1
    payload = {
        "schema": "external-trend-intelligence.annual-report-citation-map.v1",
        "source_family": "annual-report-research",
        "source_revision": REVISION,
        "source_path": PATH,
        "row_count": len(rows),
        "packet_counts": dict(sorted(by_packet.items())),
        "publisher_host_count": len({row["publisher_host"] for row in rows}),
        "rows": rows,
        "status_counts": {
            status: sum(row["citation_status"] == status for row in rows)
            for status in sorted({row["citation_status"] for row in rows})
        },
        "boundary": "This map preserves the annual-report citation table and its boundaries. It does not prove that a company disclosure is an independently observed outcome, that the URL is currently reachable, or that redistribution rights are cleared.",
        "next_test": "Map each citation to a specific annual-report theme and claim, verify retrieval and rights, and compare company disclosures with an independent outcome source before trend promotion.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} citation rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
