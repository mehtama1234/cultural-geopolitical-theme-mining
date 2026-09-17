#!/usr/bin/env python3
"""Regression checks for the storage-light Older Ages UAS follow-up."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/analyze_uas_older_ages_event_followup.py"
FIELDS = ["uasid", "wave", "final_weight", "le001", "le011_1_", "le_hrs_srh1", "le_hrs_s1", "le_hrs_p1", "le_hrs_ic_total", "le_earn_m_full"]


def main() -> int:
    rows = [
        {"uasid": "1", "wave": "1", "final_weight": "1", "le001": "1", "le011_1_": "2020-01-10", "le_hrs_srh1": "3", "le_hrs_s1": "6", "le_hrs_p1": "4", "le_hrs_ic_total": "20", "le_earn_m_full": "100"},
        {"uasid": "1", "wave": "2", "final_weight": "1", "le001": "2", "le011_1_": "", "le_hrs_srh1": "2", "le_hrs_s1": "5", "le_hrs_p1": "5", "le_hrs_ic_total": "18", "le_earn_m_full": "90"},
        {"uasid": "2", "wave": "1", "final_weight": "2", "le001": "2", "le011_1_": "", "le_hrs_srh1": "2", "le_hrs_s1": "4", "le_hrs_p1": "5", "le_hrs_ic_total": "30", "le_earn_m_full": "200"},
        {"uasid": "2", "wave": "2", "final_weight": "2", "le001": "2", "le011_1_": "", "le_hrs_srh1": "1", "le_hrs_s1": "3", "le_hrs_p1": "6", "le_hrs_ic_total": "28", "le_earn_m_full": "180"},
    ]
    with tempfile.TemporaryDirectory(prefix="uas-older-guards-") as directory:
        root = Path(directory)
        source = root / "panel.csv"
        with source.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        output = root / "result.json"
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(source), "--event-date", "le011_1_", "--output", str(output)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            raise SystemExit(result.stderr)
        record = json.loads(output.read_text(encoding="utf-8"))
        assert record["records"]["eligible_event_followup_rows"] == 2
        assert record["records"]["event_present_rows"] == 1
        assert record["records"]["event_absent_rows"] == 1
        assert record["outcomes"]["health"]["next_wave_event_present"]["weighted_mean"] == 2.0
        duplicate = root / "duplicate.csv"
        with duplicate.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows + [rows[0]])
        bad = subprocess.run(
            [sys.executable, str(SCRIPT), str(duplicate), "--output", str(root / "bad.json")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        assert bad.returncode != 0
        assert "duplicate uasid-wave rows" in bad.stderr
    print("UAS Older Ages event follow-up guards: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
