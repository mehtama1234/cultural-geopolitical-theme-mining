#!/usr/bin/env python3
"""Regression checks for durable handoff count synchronization."""

from __future__ import annotations

from validate_program_control_sync import validate_handoff_counts, validate_local_markdown_count


def main() -> int:
    current = (
        "**Current registry state:** 255 machine-readable records, 979 observations,\n"
        "the current checkpoint: 255 trend records and 979 observations pass the\n"
    )
    queue = "The trend registry holds 255 records and\n979 observations."
    review = "**Registry checkpoint:** 255 canonical records, 979 observations,"

    validate_handoff_counts(current, queue, review, 255, 979)
    try:
        validate_handoff_counts(current, queue, review, 252, 961)
    except ValueError as error:
        assert str(error) == "current-status audit registry count is stale", error
    else:
        raise AssertionError("stale handoff counts were accepted")

    current_status = "families; 1,169 local Markdown links and 537 published HTML pages pass link"
    validate_local_markdown_count(current_status, 1169)
    try:
        validate_local_markdown_count(current_status, 1168)
    except ValueError as error:
        assert str(error) == "current-status audit Markdown-file count is stale", error
    else:
        raise AssertionError("stale Markdown-file count was accepted")

    print("PASS program control handoff-count regression checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
