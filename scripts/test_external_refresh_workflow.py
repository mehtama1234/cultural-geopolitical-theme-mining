#!/usr/bin/env python3
"""Verify the scheduled refresh workflow retains its safety contract."""

from __future__ import annotations

from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "external-observatory-refresh.yml"


def main() -> int:
    text = WORKFLOW.read_text()
    required = [
        "schedule:",
        "cron: '17 6 1 * *'",
        "workflow_dispatch:",
        "runs-on: [self-hosted, external-observatory]",
        "concurrency:",
        "group: external-observatory-refresh",
        "cancel-in-progress: false",
        "timeout-minutes: 45",
        "Verify pinned sibling workspace",
        "python3 scripts/refresh_external_observatory.py",
        "git push",
    ]
    missing = [marker for marker in required if marker not in text]
    assert not missing, missing
    for sibling in ["organization-intelligence-system", "inc5000-analysis", "ibis-industries", "social-research", "trend-hunting"]:
        assert sibling in text
    print("external refresh workflow contract: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
