#!/usr/bin/env python3
"""Audit the 14-theme broad evidence matrix without acquiring new data."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


STATUS_WORDS = ("Observed", "Reported", "Compared", "Inferred", "Open")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--output-json", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    themes: list[dict[str, object]] = []
    in_matrix = False
    for line_number, line in enumerate(args.matrix.read_text(encoding="utf-8").splitlines(), start=1):
        if line.startswith("| Theme | Current evidence anchor"):
            in_matrix = True
            continue
        if not in_matrix or not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 5:
            continue
        theme, anchors, level, current_status, next_test = cells
        status_tokens = [word for word in STATUS_WORDS if re.search(rf"\b{word}\b", current_status)]
        themes.append(
            {
                "theme": theme,
                "current_status": current_status,
                "status_tokens": status_tokens,
                "evidence_anchor_count": len(re.findall(r"\]\(", anchors)),
                "measurement_level": level,
                "next_required_test": next_test,
                "source_line": line_number,
                "same_unit_end_to_end_link": "Open" in status_tokens or "Open" in next_test,
            }
        )

    if len(themes) != 14:
        raise SystemExit(f"expected 14 theme rows, found {len(themes)}")

    status_counts = Counter(token for theme in themes for token in theme["status_tokens"])
    output = {
        "schema": "us-broad-theme-end-to-end-coverage-audit-v1",
        "status": "control_audit",
        "matrix": str(args.matrix),
        "matrix_sha256": hashlib.sha256(args.matrix.read_bytes()).hexdigest(),
        "theme_count": len(themes),
        "status_token_counts": dict(sorted(status_counts.items())),
        "themes_with_explicit_open_link": sum(
            bool(theme["same_unit_end_to_end_link"]) for theme in themes
        ),
        "themes": themes,
        "interpretation": (
            "This audit summarizes the matrix's declared evidence states. It does not infer "
            "causality, convert source layers into a common denominator, or treat a non-open "
            "status token as a completed end-to-end result."
        ),
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
