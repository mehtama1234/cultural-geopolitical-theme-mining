#!/usr/bin/env python3
"""Verify that durable program control counts match source-of-truth outputs."""

from __future__ import annotations

import json
import re
from pathlib import Path

from validate_us_broad_event_ledger import validate as validate_event_ledger

ROOT = Path(__file__).resolve().parents[1]


def number_words(value: int) -> str:
    """Render the small counts used in the prose handoff."""
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if value < 10:
        return ones[value]
    if value < 20:
        return teens[value - 10]
    if value < 100:
        return tens[value // 10] + (f"-{ones[value % 10]}" if value % 10 else "")
    if value < 1000:
        remainder = value % 100
        return f"{ones[value // 100]} hundred" + (f" and {number_words(remainder)}" if remainder else "")
    raise ValueError("prose count helper only supports counts below 1,000")


def validate_handoff_counts(
    current_status: str,
    next_queue: str,
    review_packet: str,
    records: int,
    observations: int,
) -> None:
    """Require the three human handoff documents to show current counts."""
    expected_status = f"**Current registry state:** {records} machine-readable records, {observations} observations,"
    if expected_status not in current_status:
        raise ValueError("current-status audit registry count is stale")
    expected_status_checkpoint = f"the current checkpoint: {records} trend records and {observations} observations pass the"
    if expected_status_checkpoint not in current_status:
        raise ValueError("current-status audit checkpoint count is stale")
    expected_queue = f"The trend registry holds {records} records and\n{observations} observations."
    if expected_queue not in next_queue:
        raise ValueError("next-pass queue registry count is stale")
    expected_review = f"**Registry checkpoint:** {records} canonical records, {observations} observations,"
    if expected_review not in review_packet:
        raise ValueError("current themes review packet registry count is stale")


def validate_local_markdown_count(current_status: str, markdown_files: int) -> None:
    """Require the current-status audit to show the live Markdown-file count."""
    expected = f"{markdown_files:,} local Markdown links and"
    if expected not in current_status:
        raise ValueError("current-status audit Markdown-file count is stale")


def main() -> int:
    records = [json.loads(path.read_text(encoding="utf-8")) for path in sorted((ROOT / "analysis/records").glob("*.json"))]
    observations = sum(len(record.get("observations", [])) for record in records)
    schema = json.loads((ROOT / "manifests/us-trend-observation-schema-v1.json").read_text(encoding="utf-8"))
    catalog = {item["id"] for item in schema["program_theme_catalog"]}
    used_themes = {theme for record in records for theme in record.get("program_theme_ids", [])}
    missing_catalog = used_themes - catalog
    if missing_catalog:
        raise SystemExit(f"trend records use unknown program themes: {sorted(missing_catalog)}")

    trend_md = (ROOT / "analysis/us-trend-observations.md").read_text(encoding="utf-8")
    theme_md = (ROOT / "analysis/us-trend-theme-coverage.md").read_text(encoding="utf-8")
    source_md = (ROOT / "analysis/us-source-coverage.md").read_text(encoding="utf-8")
    ledger = (ROOT / "analysis/US-BROAD-PROGRAM-CONTINUITY-LEDGER_V1.md").read_text(encoding="utf-8")
    synthesis = (ROOT / "analysis/US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md").read_text(encoding="utf-8")
    synthesis_site = (ROOT / "site/US-CROSS-SOURCE-TREND-SYNTHESIS_V1.html").read_text(encoding="utf-8")
    handoff = (ROOT / "analysis/US-CENTERED-RESEARCH-HANDOFF_V1.md").read_text(encoding="utf-8")
    dashboard = (ROOT / "analysis/US-PROGRAM-DASHBOARD_V1.md").read_text(encoding="utf-8")
    current_status = (ROOT / "analysis/US-BROAD-CURRENT-STATUS-AUDIT_V1.md").read_text(encoding="utf-8")
    next_queue = (ROOT / "analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md").read_text(encoding="utf-8")
    review_packet = (ROOT / "REVIEW-PACKET_CURRENT-THEMES_V1.md").read_text(encoding="utf-8")
    big_picture = (ROOT / "analysis/us-big-picture-synthesis.md").read_text(encoding="utf-8")
    big_picture_site = (ROOT / "site/us-big-picture-synthesis.html").read_text(encoding="utf-8")
    connections = json.loads((ROOT / "manifests/us-theme-connections.json").read_text(encoding="utf-8"))
    edge_count = len(connections.get("edges", []))
    path_count = len(connections.get("reading_paths", []))
    event_ledger_path = ROOT / "analysis/projects/us-customer-automation-recourse/data/cfpb-student-loan-event-ledger-2024-25.json"
    event_count, arrow_count, event_class = validate_event_ledger(event_ledger_path)
    if event_class == "simulated_test_data":
        raise SystemExit("public CFPB event ledger was incorrectly marked simulated")
    expected_trend = f"{len(records)} machine-readable trend records"
    expected_theme = f"The current registry contains {len(records)} machine-readable records and {observations} observations."
    expected_source = re.search(r"^(\d+) project packets are recorded below\.", source_md, re.M)
    ledger_match = re.search(r"\| Trend registry \| (\d+) machine-readable records; (\d+) observations \|", ledger)
    if expected_trend not in trend_md:
        raise SystemExit(f"trend Markdown is stale: expected {expected_trend}")
    if expected_theme not in theme_md:
        raise SystemExit(f"theme coverage Markdown is stale: expected {expected_theme}")
    if not expected_source:
        raise SystemExit("source coverage packet count missing")
    source_count = len(list((ROOT / "analysis/projects").glob("*/source-search-*.md")))
    if int(expected_source.group(1)) != source_count:
        raise SystemExit(f"source coverage is stale: generated {expected_source.group(1)}, source files {source_count}")
    if not ledger_match or (int(ledger_match.group(1)), int(ledger_match.group(2))) != (len(records), observations):
        actual = ledger_match.groups() if ledger_match else None
        raise SystemExit(f"continuity ledger is stale: generated {actual}, source of truth {(len(records), observations)}")
    expected_registry_sentence = f"The current registry contains {len(records)} machine-readable records, {observations} observations,"
    if expected_registry_sentence not in synthesis:
        raise SystemExit("cross-source synthesis registry count is stale")
    if expected_registry_sentence not in synthesis_site:
        raise SystemExit("published cross-source synthesis registry count is stale")
    expected_edge_words = number_words(edge_count)
    expected_path_words = number_words(path_count)
    expected_handoff_start = f"with {expected_edge_words} explained cross-topic connections"
    expected_handoff_state = f"{expected_edge_words} connections, and {expected_path_words} reading paths"
    if expected_handoff_start not in handoff:
        raise SystemExit("research handoff opening connection count is stale")
    if expected_handoff_state not in handoff:
        raise SystemExit("research handoff state connection count is stale")
    if f"**{len(records)}** validated machine-readable trend records" not in dashboard or f"**{observations}** period-specific observations" not in dashboard:
        raise SystemExit("program dashboard registry count is stale")
    try:
        validate_handoff_counts(current_status, next_queue, review_packet, len(records), observations)
        markdown_files = sum(
            1
            for path in ROOT.rglob("*.md")
            if ".git" not in path.parts
        )
        validate_local_markdown_count(current_status, markdown_files)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    expected_big_picture = f"{edge_count} recorded cross-topic links"
    if expected_big_picture not in big_picture:
        raise SystemExit("big-picture synthesis connection count is stale")
    if f"{edge_count} recorded links" not in big_picture_site:
        raise SystemExit("published big-picture synthesis connection count is stale")
    site = (ROOT / "site/us-trend-observations.html").read_text(encoding="utf-8")
    if f">{len(records)} of {len(records)} trend records shown<" not in site:
        raise SystemExit("trend HTML count is stale")
    print(f"VALID program control sync: {len(records)} records, {observations} observations, {source_count} source packets, {len(catalog)} themes, {edge_count} connections, {path_count} paths, {event_count} public episode events, {arrow_count} episode arrows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
