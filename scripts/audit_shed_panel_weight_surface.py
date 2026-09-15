#!/usr/bin/env python3
"""Audit SHED panel archives for weights and replicate-weight fields."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path

OUT = Path("analysis/projects/us-household-financial-pressure/shed-panel-weight-audit-2026-09-13.json")
ARCHIVES = {
    "2024": (Path("/tmp/cgm-shed/shed2024.zip"), "public2024.csv", "https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2024_(CSV).zip"),
    "2025": (Path("/tmp/cgm-shed/shed2025.zip"), "public2025.csv", "https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2025_(CSV).zip"),
}


def main() -> int:
    result = {"format": "shed-panel-weight-surface-audit-v1", "checked": {}, "conclusion": ""}
    for year, (archive_path, member, url) in ARCHIVES.items():
        blob = archive_path.read_bytes()
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            with archive.open(member) as handle:
                reader = csv.reader(io.TextIOWrapper(handle, encoding="utf-8-sig"))
                header = next(reader)
                rows = sum(1 for _ in reader)
        weights = [h for h in header if "weight" in h.lower()]
        replicate = [h for h in header if any(token in h.lower() for token in ("replicate", "repweight", "variance", "jackknife", "bootstrap", "brr"))]
        result["checked"][year] = {"url": url, "archive_sha256": hashlib.sha256(blob).hexdigest(), "csv_member": member, "csv_rows": rows, "column_count": len(header), "weight_columns": weights, "replicate_or_variance_columns": replicate}
    result["conclusion"] = "The 2024 and 2025 public-use files expose main and panel weights but no replicate or variance-estimation columns. The existing panel persistence estimates can be weighted descriptively, but design-based standard errors cannot be claimed from these files alone."
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
