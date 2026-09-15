#!/usr/bin/env python3
"""Regression checks for the UAS acquisition and continuity gates."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "scripts/audit_uas_health_cost_legitimacy_files.py"
FOLLOWUP = ROOT / "scripts/analyze_uas_monthly_medical_expense_followup.py"
FIELDS = ["uasid", "wave", "final_weight", "fin3s4"]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    valid = [
        {"uasid": "a", "wave": "1", "final_weight": "1", "fin3s4": "1"},
        {"uasid": "a", "wave": "2", "final_weight": "1", "fin3s4": "2"},
        {"uasid": "b", "wave": "1", "final_weight": "1", "fin3s4": "2"},
    ]
    with tempfile.TemporaryDirectory(prefix="uas-guards-") as directory:
        root = Path(directory)
        valid_path = root / "valid.csv"
        write_csv(valid_path, valid)

        audit_output = root / "audit.json"
        audit = run(str(AUDIT), "--file", f"monthly={valid_path}", "--output", str(audit_output))
        assert audit.returncode == 0, audit.stderr
        record = json.loads(audit_output.read_text(encoding="utf-8"))["files"][0]
        assert record["unique_person_wave_keys"] == 3
        assert record["duplicate_person_wave_rows"] == 0

        followup = run(str(FOLLOWUP), str(valid_path), "--output", str(root / "followup.json"))
        assert followup.returncode == 0, followup.stderr

        duplicate_path = root / "duplicate.csv"
        write_csv(duplicate_path, valid + [valid[0]])
        duplicate = run(str(FOLLOWUP), str(duplicate_path), "--output", str(root / "duplicate.json"))
        assert duplicate.returncode != 0
        assert "duplicate uasid-wave rows" in duplicate.stderr

        invalid_wave_path = root / "invalid-wave.csv"
        write_csv(invalid_wave_path, [{**valid[0], "wave": "unknown"}])
        invalid_wave = run(
            str(FOLLOWUP), str(invalid_wave_path), "--output", str(root / "invalid-wave.json")
        )
        assert invalid_wave.returncode != 0
        assert "missing or nonnumeric" in invalid_wave.stderr

    print("UAS acquisition and continuity guards: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
