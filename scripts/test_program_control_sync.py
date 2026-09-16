#!/usr/bin/env python3
"""Regression checks for durable handoff count synchronization."""

from __future__ import annotations

from validate_program_control_sync import validate_handoff_counts


def main() -> int:
    current = (
        "**Current registry state:** 253 machine-readable records, 963 observations,\n"
        "the current checkpoint: 253 trend records and 963 observations pass the\n"
    )
    queue = "The trend registry holds 253 records and\n963 observations."
    review = "**Registry checkpoint:** 253 canonical records, 963 observations,"

    validate_handoff_counts(current, queue, review, 253, 963)
    try:
        validate_handoff_counts(current, queue, review, 252, 961)
    except ValueError as error:
        assert str(error) == "current-status audit registry count is stale", error
    else:
        raise AssertionError("stale handoff counts were accepted")

    print("PASS program control handoff-count regression checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
