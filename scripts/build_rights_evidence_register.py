#!/usr/bin/env python3
"""Record local terms/license evidence without making a legal clearance claim."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS = ROOT / "cultural-geopolitical-theme-mining" / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "rights-evidence-register.json"

FAMILIES = {
    "cultural-geopolitical-theme-mining": ROOT / "cultural-geopolitical-theme-mining",
    "social-research": ROOT / "social-research",
    "trend-hunting": ROOT / "trend-hunting",
    "annual-report-research": ROOT / "organization-intelligence-system" / "annual-report-research",
    "inc5000-analysis": ROOT / "inc5000-analysis",
    "ibis-industries": ROOT / "ibis-industries",
    "research-signals": ROOT / "research-signals",
    "organization-intelligence-system": ROOT / "organization-intelligence-system",
}


def main() -> int:
    rows = []
    for family_id, repo in FAMILIES.items():
        files = []
        if repo.exists():
            for path in sorted(repo.rglob("*")):
                if not path.is_file() or "node_modules" in path.parts or ".git" in path.parts:
                    continue
                upper = path.name.upper()
                if upper.startswith(("LICENSE", "COPYING", "NOTICE", "TERMS")) or "TERMS_AND_DISCLOSURES" in upper:
                    data = path.read_bytes()
                    files.append({"path": str(path.relative_to(repo)), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        rows.append({
            "family_id": family_id,
            "repository_path": str(repo),
            "evidence_status": "partial_file_evidence" if files else "no_local_terms_file_found",
            "observed_files": files[:50],
            "rights_status": "not_verified",
            "publisher_dependence": "review_required",
            "legal_boundary": "A local license, terms, or notice file is evidence to review, not legal clearance for third-party source material, redistribution, or derived charts.",
            "next_action": "Review the observed file or confirm the absence of repository-level terms, then separately document upstream publisher terms and retention/redistribution limits.",
        })
    report = {
        "schema": "external-trend-intelligence.rights-evidence-register.v1",
        "family_count": len(rows),
        "partial_file_evidence_count": sum(row["evidence_status"] == "partial_file_evidence" for row in rows),
        "no_local_terms_file_count": sum(row["evidence_status"] == "no_local_terms_file_found" for row in rows),
        "rows": rows,
        "boundary": "This register records local evidence discovery only. It does not determine license scope, publisher permission, fair use, retention rights, or independence.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} families)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
