#!/usr/bin/env python3
"""Acquire and verify the public CES personal-crisis replication extracts."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import urllib.request
from pathlib import Path


FILES = {
    "CCES18_crisis_vv.tab": {
        "id": 8961297,
        "sha256": "c61ccc59c7f9232cbb7abd420654b907cb0997433c80ce0efe391d4f257d3d58",
    },
    "CCES20_crisis_vv.tab": {
        "id": 8961293,
        "sha256": "10fe9927942f345b9b39f58b4c07daa130baa997537f4cecfe76e6d7c024cd1e",
    },
    "crisis_rep_2018common.do": {
        "id": 8961294,
        "sha256": "7c68771b9caff0e12c2d534b2d1459f9b95445828cc2f7aae0131c0682e4e292",
    },
    "crisis_rep_2018module.do": {
        "id": 8961298,
        "sha256": "cc1a12be087bbe974453d0f5977b848008899c09d205f768c871cc154d5031b1",
    },
    "crisis_rep_2020common.do": {
        "id": 8961295,
        "sha256": "932c52db9f85c769353c91b90d5adc66f93b7235b72794f3b862dd8b20353e7e",
    },
    "crisis_rep_2020module.do": {
        "id": 8961291,
        "sha256": "5649de61127dd12f2fb135ce9d8f7b685f434ebcfc6c3938883baa300a24850c",
    },
}
BASE_URL = "https://dataverse.harvard.edu/api/access/datafile/{file_id}?format=original"


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def acquire(name: str, spec: dict[str, object], output_dir: Path) -> dict[str, object]:
    destination = output_dir / name
    url = BASE_URL.format(file_id=spec["id"])
    request = urllib.request.Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as handle:
        shutil.copyfileobj(response, handle)
    actual = digest(destination)
    expected = str(spec["sha256"])
    if actual != expected:
        raise RuntimeError(f"{name}: SHA-256 mismatch: expected {expected}, got {actual}")
    return {"file_id": spec["id"], "url": url, "bytes": destination.stat().st_size, "sha256": actual}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "format": "ces-personal-crisis-replication-acquisition-v1",
        "dataset_doi": "10.7910/DVN/PJQ57U",
        "source_url": "https://doi.org/10.7910/DVN/PJQ57U",
        "files": {name: acquire(name, spec, args.output_dir) for name, spec in FILES.items()},
    }
    (args.output_dir / "acquisition-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
