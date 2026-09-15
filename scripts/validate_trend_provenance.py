"""Strictly validate source URL and retrieval-hash provenance in trend records."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
HASH_TOKEN = re.compile(r"(?:[A-Za-z0-9_.-]+:)?sha256:[0-9a-f]{64}\Z|[0-9a-f]{64}\Z")


def main() -> int:
    failures: list[str] = []
    records = sorted((ROOT / "analysis/records").glob("*.json"))
    for path in records:
        data = json.loads(path.read_text(encoding="utf-8"))
        for index, observation in enumerate(data.get("observations", [])):
            prefix = f"{path.relative_to(ROOT)} observation {index}"
            url = observation.get("source_url", "")
            parsed = urlsplit(url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                failures.append(f"{prefix}: source_url is not an HTTP(S) URL")
            raw_hash = str(observation.get("retrieval_hash", ""))
            tokens = [token.strip() for token in raw_hash.split(";") if token.strip()]
            if not tokens or any(not HASH_TOKEN.fullmatch(token) for token in tokens):
                failures.append(f"{prefix}: retrieval_hash has a malformed SHA-256 token")

    if failures:
        print("\n".join(failures))
        print(f"INVALID trend provenance: {len(failures)} failures")
        return 1
    print(f"VALID trend provenance: {len(records)} records checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
