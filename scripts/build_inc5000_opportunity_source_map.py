#!/usr/bin/env python3
"""Normalize Inc. 5000 opportunity evidence and buyer-proxy source links."""

from __future__ import annotations

import json
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "inc5000-opportunity-source-map.json"
REPO = "/home/mehta/git-repo/inc5000-analysis"
REVISION = "92fad318ff05efcc5707f997bb1b5b18f3bceab2"
PATH = "data/processed/opportunity_validation_release.json"


def main() -> int:
    release = json.loads(subprocess.check_output(["git", "-C", REPO, "show", f"{REVISION}:{PATH}"], text=True))
    rows = []
    buyer_rows = []
    for record in release["records"]:
        opportunity = record["opportunity"]
        for evidence in record.get("evidence", []):
            for url in evidence.get("source_urls", []):
                rows.append(
                    {
                        "opportunity": opportunity,
                        "company": evidence.get("company"),
                        "role": evidence.get("role"),
                        "growth_pct_2026": evidence.get("growth_pct_2026"),
                        "source_url": url,
                        "publisher_host": urlparse(url).netloc.lower(),
                        "source_class": evidence.get("source_class"),
                        "observed_facts": evidence.get("observed_facts"),
                        "measurable_outcome_claim": evidence.get("measurable_outcome_claim"),
                        "evidence_limits": evidence.get("evidence_limits"),
                        "assessment": evidence.get("assessment"),
                        "outcome_verification_status": evidence.get("outcome_verification_status"),
                        "durability_status": evidence.get("durability_status"),
                        "lineage_status": "source_row_pinned",
                        "rights_status": "not_yet_verified",
                        "independence_status": "not_reviewed",
                    }
                )
        for proxy in record.get("buyer_proxies", []):
            for url in proxy.get("source_urls", []):
                buyer_rows.append(
                    {
                        "opportunity": opportunity,
                        "organization": proxy.get("organization"),
                        "role": proxy.get("role"),
                        "research_mode": proxy.get("research_mode"),
                        "source_url": url,
                        "publisher_host": urlparse(url).netloc.lower(),
                        "buyer_signal": proxy.get("buyer_signal"),
                        "pain_signal": proxy.get("pain_signal"),
                        "outcome_signal": proxy.get("outcome_signal"),
                        "procurement_signal": proxy.get("procurement_signal"),
                        "limitation": proxy.get("limitation"),
                        "lineage_status": "buyer_proxy_source_pinned",
                        "rights_status": "not_yet_verified",
                        "independence_status": "not_reviewed",
                    }
                )
    all_urls = {row["source_url"] for row in rows + buyer_rows}
    payload = {
        "schema": "external-trend-intelligence.inc5000-opportunity-source-map.v1",
        "source_family": "inc5000-analysis",
        "source_revision": REVISION,
        "source_path": PATH,
        "opportunity_count": len(release["records"]),
        "opportunities": [record["opportunity"] for record in release["records"]],
        "evidence_row_count": len(rows),
        "buyer_proxy_row_count": len(buyer_rows),
        "unique_source_url_count": len(all_urls),
        "publisher_host_count": len({urlparse(url).netloc.lower() for url in all_urls}),
        "decision_counts": release["operating_state"]["decision_distribution"],
        "field_evidence_status": release["operating_state"]["field_evidence_status"],
        "opportunity_counts": dict(sorted(Counter(row["opportunity"] for row in rows).items())),
        "rows": rows,
        "buyer_proxy_rows": buyer_rows,
        "boundary": release["boundary"],
        "next_test": "For each opportunity, obtain the specified buyer/operator interviews and de-identified outcome cohort before treating public company evidence as validated demand or a company decision pilot.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} evidence rows; {len(buyer_rows)} buyer-proxy rows; {len(all_urls)} URLs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
