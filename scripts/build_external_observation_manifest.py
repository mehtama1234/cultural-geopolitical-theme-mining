#!/usr/bin/env python3
"""Build a provenance-preserving index of external observation records.

The script indexes records; it does not flatten measures, infer joins, or
replace source-owned evidence. It can read a pinned Git tree so a deleted or
partial working-tree checkout does not silently change the inventory.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import tarfile
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


def archived_records(ref: str):
    """Yield (path, parsed JSON) from one git archive process."""
    process = subprocess.Popen(
        ["git", "archive", "--format=tar", ref, "analysis/records"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.stdout is not None
    with tarfile.open(fileobj=process.stdout, mode="r|") as archive:
        for member in archive:
            if not member.isfile() or not member.name.endswith(".json"):
                continue
            stream = archive.extractfile(member)
            if stream is None:
                continue
            yield member.name, json.loads(stream.read().decode("utf-8"))
    stderr = process.stderr.read().decode("utf-8") if process.stderr else ""
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, process.args, stderr=stderr)


def source_hosts(record: dict) -> list[str]:
    urls: set[str] = set()
    for observation in record.get("observations", []):
        if observation.get("source_url"):
            urls.add(observation["source_url"])
    for related in record.get("related_sources", []):
        if isinstance(related, str):
            urls.add(related)
        elif related.get("source_url"):
            urls.add(related["source_url"])
    hosts = set()
    for url in urls:
        host = urlparse(url).netloc.lower()
        if host.startswith("www."):
            host = host[4:]
        if host:
            hosts.add(host)
    return sorted(hosts)


def compact_record(path: str, record: dict) -> dict:
    observations = record.get("observations", [])
    statuses = sorted({item.get("status", "unknown") for item in observations})
    return {
        "record_path": path,
        "trend_id": record.get("trend_id"),
        "title": record.get("title"),
        "source_unit": record.get("source_unit"),
        "geography": record.get("geography"),
        "program_theme_ids": record.get("program_theme_ids", []),
        "observation_count": len(observations),
        "observation_statuses": statuses,
        "source_hosts": source_hosts(record),
        "boundary": record.get("boundary"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--git-ref", default="HEAD")
    parser.add_argument(
        "--output",
        default="analysis/external-trend-intelligence/observation-manifest.json",
    )
    args = parser.parse_args()

    records: list[dict] = []
    parse_errors: list[dict] = []
    for path, record in archived_records(args.git_ref):
        try:
            records.append(compact_record(path, record))
        except (json.JSONDecodeError, TypeError, AttributeError) as exc:
            parse_errors.append({"record_path": path, "error": str(exc)})

    records.sort(key=lambda item: item.get("trend_id") or item["record_path"])
    themes = Counter(
        theme
        for record in records
        for theme in record.get("program_theme_ids", [])
    )
    hosts = Counter(
        host for record in records for host in record.get("source_hosts", [])
    )
    manifest = {
        "schema": "external-trend-intelligence.observation-manifest.v1",
        "generated_on": date.today().isoformat(),
        "source_git_ref": args.git_ref,
        "record_root": "analysis/records",
        "record_count": len(records),
        "parse_error_count": len(parse_errors),
        "program_theme_counts": dict(sorted(themes.items())),
        "source_host_counts": dict(hosts.most_common()),
        "records": records,
        "parse_errors": parse_errors,
        "boundary": "This is an index of source-backed observation records. It does not establish cross-record joins, prevalence, causality, customer demand, or company impact.",
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(
        f"indexed {len(records)} records from {args.git_ref}; "
        f"{len(parse_errors)} parse errors; wrote {output}"
    )
    return 1 if parse_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
