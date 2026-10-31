#!/usr/bin/env python3
"""Exercise stale detection and recovery without touching the release tree."""

from __future__ import annotations

import os
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from build_external_refresh_status import build_report


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="external-refresh-gate-") as directory:
        root = Path(directory)
        analysis = root / "analysis"
        analysis.mkdir()
        artifact = analysis / "artifact.json"
        artifact.write_text("{}\n")
        schedule = {"families": [{"family_id": "demo-family", "cadence": "daily", "trigger": "test", "refresh_artifacts": ["artifact.json"]}]}
        registry = {"source_families": [{"id": "demo-family"}]}
        now = datetime.now(timezone.utc)
        old = (now - timedelta(hours=24 * 200)).timestamp()
        os.utime(artifact, (old, old))
        stale = build_report(schedule, registry, now, root=root, analysis=analysis)
        assert stale["stale_count"] == 1
        assert stale["families"][0]["status"] == "stale"

        artifact.write_text("refreshed\n")
        recovered = build_report(schedule, registry, datetime.now(timezone.utc), root=root, analysis=analysis)
        assert recovered["stale_count"] == 0
        assert recovered["families"][0]["status"] == "ready_for_review"
    print("refresh stale gate: stale detection and recovery passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
