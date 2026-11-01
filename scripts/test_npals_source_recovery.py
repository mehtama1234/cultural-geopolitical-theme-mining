#!/usr/bin/env python3
"""Verify the NPALS extractor preserves the last good extract during an outage."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "build_npals_public_table_extract.py"


def load_module():
    spec = importlib.util.spec_from_file_location("build_npals_public_table_extract", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load NPALS extractor")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    with tempfile.TemporaryDirectory(prefix="npals-recovery-") as directory:
        output = Path(directory) / "npals-public-table-extract.json"
        module.OUTPUT = output

        rows = [
            {
                "survey_year": "2020",
                "geography": "Alabama",
                "select_measure": "Number of providers",
                "levels_of_measure": "Number of providers",
                "value": "12",
                "se": "1",
                "low_95_ci": "10",
                "high_95_ci": "14",
            }
        ]
        module.fetch_rows = lambda: ("https://example.test/npals", rows)
        assert module.main() == 0
        fresh = json.loads(output.read_text())
        assert fresh["retrieval_status"] == "fresh_api_extract"
        assert fresh["source_available"] is True
        original_hash = fresh["normalized_rows_sha256"]

        def outage():
            raise OSError("simulated upstream outage")

        module.fetch_rows = outage
        assert module.main() == 0
        stale = json.loads(output.read_text())
        assert stale["retrieval_status"] == "stale_previous_extract_source_unavailable"
        assert stale["source_available"] is False
        assert stale["normalized_rows_sha256"] == original_hash
        assert "simulated upstream outage" in stale["retrieval_error"]

        module.fetch_rows = lambda: ("https://example.test/npals", rows)
        assert module.main() == 0
        recovered = json.loads(output.read_text())
        assert recovered["retrieval_status"] == "fresh_api_extract"
        assert recovered["source_available"] is True
        assert recovered["normalized_rows_sha256"] == original_hash

    print("NPALS source recovery: fresh, outage preservation, and recovery passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
