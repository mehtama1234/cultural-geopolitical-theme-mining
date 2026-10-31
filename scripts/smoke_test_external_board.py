#!/usr/bin/env python3
"""Serve the external board briefly and verify its reader artifacts are reachable."""

from __future__ import annotations

import http.server
import pathlib
import subprocess
import time
import urllib.error
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
        deadline = time.time() + 5
        while True:
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/board.html", timeout=1) as response:
                    if response.status == 200:
                        board_text = response.read().decode("utf-8")
                        required_markers = [
                            "Release blockers",
                            "pipeline_status",
                            "U.S. USDA food-security temporal holdout",
                            "Falsifier:",
                            "Program scorecard",
                            "program-scorecard.json",
                            "Operating handoff",
                            "operating-handoff.json",
                            "publisher-dependence-summary.json",
                            "SHED point-estimate reproduction",
                            "shed-point-estimate-reproduction-audit.json",
                            "JPMorgan household-liquidity chart",
                            "jpmorgan-household-liquidity-chart.json",
                            "candidate-lineage-dependency-review.json",
                            "Qualified food-insecurity temporal holdout",
                            "food-insecurity-temporal-holdout.json",
                            "food-insecurity-rights-review.json",
                        ]
                        missing = [marker for marker in required_markers if marker not in board_text]
                        if missing:
                            raise RuntimeError(f"board.html missing required reader markers: {missing}")
                        break
            except (urllib.error.URLError, ConnectionError):
                if time.time() >= deadline:
                    raise RuntimeError("external board server did not become ready within 5 seconds")
                time.sleep(0.1)
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
