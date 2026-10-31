#!/usr/bin/env python3
"""Map Trend-hunting synthesis claims to pinned input artifacts and URLs."""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "trend-hunting-source-map.json"
REPO = "/home/mehta/git-repo/trend-hunting"
REVISION = "19d8b2443f26f52da2331736320dcb265a9de34f"
PATH = "data/processed/ai_v7_deep_trend_synthesis_v1.json"


def show(path: str) -> str:
    return subprocess.check_output(["git", "-C", REPO, "show", f"{REVISION}:{path}"], text=True)


def urls(value) -> set[str]:
    return set(re.findall(r"https?://[^\s)>'\"]+", json.dumps(value, ensure_ascii=False)))


def main() -> int:
    synthesis = json.loads(show(PATH))
    rows = []
    input_summary = []
    for input_path in synthesis["inputs"]:
        raw = show(input_path)
        try:
            document = json.loads(raw)
            input_urls = urls(document)
        except json.JSONDecodeError:
            input_urls = set(re.findall(r"https?://[^\s)>'\"]+", raw))
        input_summary.append({"path": input_path, "url_count": len(input_urls), "sha256": next((item["sha256"] for item in synthesis["input_checksums"] if item["path"] == input_path), None)})
        matching_claims = [claim for claim in synthesis["claims"] if input_path in claim.get("support_inputs", [])]
        if not matching_claims:
            for url in sorted(input_urls):
                rows.append({"input_path": input_path, "claim_ids": [], "url": url, "publisher_host": urlparse(url).netloc.lower(), "lineage_status": "input_link_unmapped", "independence_status": "not_reviewed"})
        for claim in matching_claims:
            for url in sorted(input_urls):
                rows.append({"input_path": input_path, "claim_ids": [claim["id"]], "claim_state": claim.get("state"), "claim": claim.get("claim"), "claim_limit": claim.get("limit"), "url": url, "publisher_host": urlparse(url).netloc.lower(), "lineage_status": "claim_input_linked", "independence_status": "not_reviewed"})
    unique_urls = {row["url"] for row in rows}
    payload = {
        "schema": "external-trend-intelligence.trend-hunting-source-map.v1",
        "source_family": "trend-hunting",
        "source_revision": REVISION,
        "source_path": PATH,
        "synthesis_status": synthesis["status"],
        "input_artifact_count": len(synthesis["inputs"]),
        "input_summary": input_summary,
        "claim_count": len(synthesis["claims"]),
        "mapped_row_count": len(rows),
        "unique_url_count": len(unique_urls),
        "publisher_host_count": len({row["publisher_host"] for row in rows}),
        "claim_state_counts": dict(sorted(Counter(claim.get("state") for claim in synthesis["claims"]).items())),
        "rows": rows,
        "falsifiers": synthesis["falsifiers"],
        "next_test": synthesis["next_test"],
        "boundary": "This map connects a bounded Trend-hunting synthesis to its pinned input artifacts and any URLs found inside them. Synthesis remains interpretation and signal inventory; it does not establish prevalence, causality, adoption, or outcomes, and shared publishers require independence review.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(synthesis['inputs'])} inputs; {len(unique_urls)} URLs; {len(rows)} mapped rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
