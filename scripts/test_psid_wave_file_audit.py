#!/usr/bin/env python3
"""Regression-test the PSID structural acquisition gate with synthetic headers."""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "scripts/audit_psid_wave_files.py"


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="cgtm-psid-audit-") as temp:
        temp_path = Path(temp)
        files: list[tuple[int, Path]] = []
        for year in (2019, 2021, 2023):
            path = temp_path / f"FAM{year}.csv"
            path.write_text("ER30001,ER30002\n1,2\n", encoding="utf-8")
            files.append((year, path))

        # The audit needs the manifest's mapped columns. Build synthetic headers
        # from the same manifest without creating or retaining respondent data.
        manifest = __import__("json").loads(
            (ROOT / "manifests/us-psid-material-time-care-field-map-v1.json").read_text(encoding="utf-8")
        )
        from audit_psid_wave_files import manifest_variables  # type: ignore

        for year, path in files:
            columns = sorted(manifest_variables(manifest, year) | {"ER30001", "ER30002"})
            with path.open("w", encoding="utf-8", newline="") as handle:
                csv.writer(handle).writerow(columns)

        command = [sys.executable, str(AUDIT)]
        for year, path in files:
            command.extend(["--file", f"{year}={path}"])
        command.extend(["--identifier", "ER30001", "--identifier", "ER30002"])
        passed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if passed.returncode != 0:
            raise SystemExit("synthetic complete PSID headers should pass the audit")

        # Remove one mapped column and require the gate to reject the file.
        broken = files[0][1]
        rows = list(csv.reader(broken.open(encoding="utf-8")))
        rows[0].pop()
        with broken.open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerows(rows)
        failed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if failed.returncode == 0:
            raise SystemExit("PSID audit must reject a wave missing a mapped variable")

    print("PASS PSID wave-file audit regression: complete and incomplete synthetic headers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
