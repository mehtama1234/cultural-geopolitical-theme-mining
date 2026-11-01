#!/usr/bin/env python3
"""Verify reader publications and chart contracts resolve to release artifacts."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"


def main() -> int:
    registry = json.loads((ANALYSIS / "frontend-publication-registry.json").read_text())
    catalog = json.loads((ANALYSIS / "observatory-chart-catalog.json").read_text())
    manifest = json.loads((ANALYSIS / "release-manifest.json").read_text())
    required = set(registry["required_visible_fields"])
    manifest_paths = {row["path"] for row in manifest["artifacts"]}

    assert registry["publication_count"] == len(registry["publications"])
    for publication in registry["publications"]:
        assert required <= set(publication), publication["publication_id"]
        narrative = ANALYSIS / publication["narrative_artifact"]
        assert narrative.exists(), publication["narrative_artifact"]
        assert f"analysis/external-trend-intelligence/{publication['narrative_artifact']}" in manifest_paths
        for artifact in publication["chart_artifacts"]:
            assert (ANALYSIS / artifact).exists(), artifact
            assert f"analysis/external-trend-intelligence/{artifact}" in manifest_paths

    chart_required = {"theme", "subtheme", "concept", "chart_type", "source_artifacts", "visual_encoding", "required_visible_fields", "boundary"}
    assert catalog["chart_count"] == len(catalog["charts"])
    for chart in catalog["charts"]:
        assert chart_required <= set(chart) | {"company_gate"}, chart["chart_id"]
        assert chart["visual_encoding"] and chart["required_visible_fields"]
        for artifact in chart["source_artifacts"]:
            assert (ANALYSIS / artifact).exists(), artifact
            assert f"analysis/external-trend-intelligence/{artifact}" in manifest_paths

    board = (ANALYSIS / "board.html").read_text()
    for marker in ["chart-catalog", "qualified-trend-brief", "source-release-watchlist"]:
        assert marker in board, marker
    print("frontend publication contract: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
