#!/usr/bin/env python3
"""Regression guard for the dated MEPS friction-cascade analyzer."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pandas as pd
import pyreadstat


ROOT = Path(__file__).resolve().parents[1]
ANALYZER = ROOT / "scripts/analyze_meps_dated_friction_cascade.py"
FLAGS = [f"BRR{i}" for i in range(1, 129)]


def write(path: Path, frame: pd.DataFrame) -> None:
    pyreadstat.write_dta(frame, str(path), version=15)


def main() -> int:
    people = pd.DataFrame(
        {
            "DUPERSID": ["1", "2", "3", "4"],
            "PANEL": [28, 28, 28, 28],
            "PERWT24F": [1.0, 0.0, 1.0, 1.0],
            "ENDRFY31": [2023, 2023, 2023, 2023],
            "ENDRFM31": [1, 1, 1, 1],
            "ENDRFY42": [2024, 2024, 2024, 2024],
            "ENDRFM42": [1, 1, 1, 1],
            "EQDENY53": [1, 2, 1, 2],
            "INSCOV24": [1, 1, 3, 1],
            "FWUNEXP42": [1, 4, 3, 4],
            "DLAYCA42": [1, 2, 1, 2],
            "PROBPY42": [1, 2, 1, 2],
            "MEDDEBT42": [1, 0, 1, 0],
            "FWDEBT42": [1, 2, 1, 2],
        }
    )
    brr = pd.DataFrame(
        {
            "DUPERSID": people["DUPERSID"],
            "PANEL": people["PANEL"],
            **{flag: [1.0] * len(people) for flag in FLAGS},
        }
    )

    with tempfile.TemporaryDirectory(prefix="meps-friction-guards-") as directory:
        root = Path(directory)
        hc256 = root / "h256.dta"
        brr_path = root / "brr.dta"
        write(hc256, people)
        write(brr_path, brr)
        event_specs = {
            "office": ("OBDATEYR", "OBDATEMM", "OBSF24X"),
            "emergency_room": ("ERDATEYR", "ERDATEMM", "ERFSF24X"),
            "inpatient": ("IPBEGYR", "IPBEGMM", "IPFSF24X"),
        }
        event_paths: dict[str, Path] = {}
        for family, (year, month, payment) in event_specs.items():
            event = pd.DataFrame(
                {
                    "DUPERSID": people["DUPERSID"],
                    "PANEL": people["PANEL"],
                    year: [2023, 2023, 2022, 2024],
                    month: [6, 7, 12, 2],
                    payment: [20.0, 30.0, 40.0, 50.0],
                }
            )
            path = root / f"{family}.dta"
            write(path, event)
            event_paths[family] = path
        output = root / "output.json"
        command = [
            sys.executable, str(ANALYZER), str(hc256), str(brr_path),
            "--office-file", str(event_paths["office"]),
            "--emergency-room-file", str(event_paths["emergency_room"]),
            "--inpatient-file", str(event_paths["inpatient"]),
            "--output", str(output),
        ]
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        if result.returncode != 0:
            raise AssertionError(result.stderr)
        data = json.loads(output.read_text(encoding="utf-8"))
        assert data["person_records_positive_weight"] == 3
        assert data["round_order_valid_records"] == 3
        for family, record in data["events"].items():
            assert record["event_window_people"] == 1, (family, record)
            assert record["friction_groups"]["denial_or_delay"]["records"] == 1
            assert record["friction_groups"]["no_denial_or_delay"]["records"] == 0
            assert record["conditioned_strata"]["any_private_coverage"]["denial_or_delay"]["records"] == 1

    print("MEPS dated friction cascade guards: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
