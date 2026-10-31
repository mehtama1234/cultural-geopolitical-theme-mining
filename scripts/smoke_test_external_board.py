#!/usr/bin/env python3
"""Serve the external board briefly and verify its reader artifacts are reachable."""

from __future__ import annotations

import http.server
import pathlib
import subprocess
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOARD = ROOT / "analysis" / "external-trend-intelligence"
PORT = 8765
ARTIFACTS = [
    "board.html",
    "release-health.json",
    "refresh-status.json",
    "candidate-qualification-matrix.json",
    "backtest-readiness.json",
    "case-stage-panel.json",
    "pilot-register.json",
]


def main() -> int:
    proc = subprocess.Popen(
        ["python3", "-m", "http.server", str(PORT), "--bind", "127.0.0.1"],
        cwd=BOARD,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        time.sleep(0.4)
        for artifact in ARTIFACTS:
            with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/{artifact}", timeout=5) as response:
                if response.status != 200:
                    raise RuntimeError(f"{artifact}: HTTP {response.status}")
                print(f"{artifact}: HTTP {response.status} ({len(response.read())} bytes)")
    finally:
        proc.terminate()
        proc.wait(timeout=5)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
