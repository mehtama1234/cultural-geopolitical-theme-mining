#!/usr/bin/env python3
"""Acquire the official O*NET 31.0 and NBER W35677 crosswalk inputs.

The acquisition is deliberately separate from interpretation: it records the
source URLs, byte counts, hashes, and selected extracted file names before the
existing provisional label crosswalk is run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import urllib.request
import zipfile
from pathlib import Path


ONET_URL = "https://www.onetcenter.org/dl_files/database/db_31_0_csv.zip"
NBER_URLS = {
    "DWA.csv": "https://docs.google.com/spreadsheets/d/17OI5xRALkN4lDZ1fHw2R9xPJUdDgWyFU/gviz/tq?tqx=out:csv&gid=416182935",
    "IWA.csv": "https://docs.google.com/spreadsheets/d/17OI5xRALkN4lDZ1fHw2R9xPJUdDgWyFU/gviz/tq?tqx=out:csv&gid=1821519318",
    "BWA.csv": "https://docs.google.com/spreadsheets/d/17OI5xRALkN4lDZ1fHw2R9xPJUdDgWyFU/gviz/tq?tqx=out:csv&gid=646067329",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, destination: Path) -> dict[str, object]:
    request = urllib.request.Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response, destination.open("wb") as handle:
        shutil.copyfileobj(response, handle)
    return {"url": url, "bytes": destination.stat().st_size, "sha256": sha256(destination)}


def existing_or_download(url: str, destination: Path) -> dict[str, object]:
    if destination.exists() and destination.stat().st_size > 0:
        try:
            if destination.suffix == ".zip":
                with zipfile.ZipFile(destination) as archive:
                    archive.testzip()
            return {"url": url, "bytes": destination.stat().st_size, "sha256": sha256(destination), "reused": True}
        except (OSError, zipfile.BadZipFile):
            destination.unlink()
    return download(url, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    onet_dir = args.output_dir / "onet-31-0-csv"
    nber_dir = args.output_dir / "nber-w35677"
    onet_dir.mkdir(parents=True, exist_ok=True)
    nber_dir.mkdir(parents=True, exist_ok=True)

    onet_zip = args.output_dir / "db_31_0_csv.zip"
    manifest: dict[str, object] = {
        "format": "onet-nber-crosswalk-acquisition-v1",
        "onet_release": "31.0",
        "onet_release_month": "August 2026",
        "onet_archive": existing_or_download(ONET_URL, onet_zip),
        "nber_indexes": {},
    }
    with zipfile.ZipFile(onet_zip) as archive:
        member = next((name for name in archive.namelist() if name.endswith("gwas_to_iwas_to_dwas.csv")), None)
        if member is None:
            raise RuntimeError("O*NET archive did not contain gwas_to_iwas_to_dwas.csv")
        extracted = onet_dir / "gwas_to_iwas_to_dwas.csv"
        with archive.open(member) as source, extracted.open("wb") as target:
            shutil.copyfileobj(source, target)
        manifest["onet_mapping"] = {
            "archive_member": member,
            "path": str(extracted.relative_to(args.output_dir)),
            "bytes": extracted.stat().st_size,
            "sha256": sha256(extracted),
        }

    for filename, url in NBER_URLS.items():
        manifest["nber_indexes"][filename] = download(url, nber_dir / filename)

    manifest["inputs"] = {
        "onet_dir": str(onet_dir.relative_to(args.output_dir)),
        "nber_dir": str(nber_dir.relative_to(args.output_dir)),
    }
    manifest_path = args.output_dir / "acquisition-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
