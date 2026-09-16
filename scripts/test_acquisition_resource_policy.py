#!/usr/bin/env python3
"""Regression checks for the read-only acquisition resource guard."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts/check_acquisition_resource_policy.py"


def run(*args: str) -> tuple[int, dict]:
    completed = subprocess.run(
        [sys.executable, str(CHECKER), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return completed.returncode, json.loads(completed.stdout)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="acquisition-policy-test-") as temp:
        path = Path(temp)
        (path / "small.bin").write_bytes(b"x" * 1024)
        code, report = run("--max-total-mb", "1", str(path))
        assert code == 0, report
        assert report["total_status"] == "allow", report
        assert report["total_bytes"] == 1024, report
        assert report["largest_files"][0]["path"].endswith("small.bin"), report

        code, report = run("--max-total-mb", "0.0005", str(path))
        assert code == 1, report
        assert report["total_status"] == "block", report

    print("PASS acquisition resource policy regression checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
