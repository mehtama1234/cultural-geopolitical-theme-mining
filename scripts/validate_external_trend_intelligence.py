#!/usr/bin/env python3
"""Validate the external-first trend manifest and candidate comparison."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"


def main() -> int:
    manifest = json.loads((ANALYSIS / "observation-manifest.json").read_text())
    assert manifest["schema"] == "external-trend-intelligence.observation-manifest.v1"
    assert manifest["record_count"] == len(manifest["records"])
    assert manifest["parse_error_count"] == 0
    assert len(manifest["program_theme_counts"]) == 14
    ids = {record["trend_id"] for record in manifest["records"]}
    assert len(ids) == manifest["record_count"]
    for record in manifest["records"]:
        assert record["record_path"].startswith("analysis/records/")
        assert record["title"] and record["boundary"]
        assert record["observation_count"] >= 1
        assert record["program_theme_ids"]
        assert isinstance(record["source_urls"], list)
        assert isinstance(record["source_hosts"], list)

    candidates = (ANALYSIS / "CROSS-SOURCE-CANDIDATES.md").read_text()
    references = set(re.findall(r"`([a-z0-9][a-z0-9-]+)`", candidates))
    record_refs = {
        ref
        for ref in references
        if ref.startswith(("au-", "bsa", "comparative-", "us-"))
    }
    missing = sorted(record_refs - ids)
    assert not missing, f"candidate references missing from manifest: {missing}"
    assert candidates.count("**Current status:**") >= 4
    assert candidates.count("**Counter-signal:**") >= 4
    assert candidates.count("**External evidence lanes:**") >= 4
    assert "Promotion gate" in candidates
    machine = json.loads((ANALYSIS / "candidate-comparisons.json").read_text())
    assert machine["schema"] == "external-trend-intelligence.candidate-comparisons.v1"
    assert len(machine["candidates"]) == 4
    for candidate in machine["candidates"]:
        assert candidate["status"] == "qualified_candidate"
        assert candidate["evidence_record_ids"]
        assert set(candidate["evidence_record_ids"]) <= ids
        assert candidate["mechanism"]
        assert candidate["counter_signal"]
        assert candidate["next_comparison"]
        coverage = candidate["coverage"]
        assert coverage["evidence_record_count"] == len(candidate["evidence_record_ids"])
        assert coverage["source_host_count"] == len(coverage["source_host_counts"])
        assert coverage["unique_source_url_count"] >= coverage["source_host_count"]
        assert all(count > 1 for count in coverage["duplicate_source_urls"].values())
        assert coverage["independence_status"] == "unverified"
        assert coverage["interpretation"]
        lineage_review = candidate["lineage_review"]
        assert lineage_review["status"] in {"not_started", "partial", "complete"}
        assert lineage_review["independence_status"] in {"unverified", "partially_reviewed", "independent", "dependent_restatement", "same_artifact"}
        if lineage_review["status"] == "partial":
            assert lineage_review["primary_artifact_count"] >= 1
            assert lineage_review["remaining"]
    bridge_schema = json.loads((ANALYSIS / "internal-bridge-schema.json").read_text())
    bridge_template = json.loads((ANALYSIS / "internal-bridge-template.json").read_text())
    assert bridge_schema["schema"] == "external-trend-intelligence.internal-bridge.v1"
    assert bridge_template["schema"] == bridge_schema["schema"]
    assert set(bridge_schema["required"]) <= set(bridge_template)
    assert bridge_template["join_basis"] in bridge_schema["join_basis_values"]
    assert bridge_template["status"] in bridge_schema["status_values"]
    bridge_request = json.loads((ANALYSIS / "bridge-request-001.json").read_text())
    assert bridge_request["schema"] == bridge_schema["schema"]
    assert bridge_request["candidate_id"] == "candidate-time-financial-pressure-practical-room"
    assert set(bridge_request["external_record_ids"]) <= ids
    assert bridge_request["join_basis"] == "no_valid_join"
    assert bridge_request["status"] == "review_required"
    internal_catalog = json.loads((ANALYSIS / "internal-source-catalog.json").read_text())
    assert internal_catalog["schema"] == "external-trend-intelligence.internal-source-catalog.v1"
    assert internal_catalog["status"] == "inventory_only"
    assert len(internal_catalog["sources"]) >= 8
    assert all("authority" in source and "readiness" in source for source in internal_catalog["sources"])
    source_snapshot = json.loads((ANALYSIS / "source-registry-snapshot.json").read_text())
    assert source_snapshot["schema"] == "external-trend-intelligence.source-registry-snapshot.v1"
    assert source_snapshot["upstream_registry_path"] == "manifests/source-registry.json"
    assert source_snapshot["upstream_format"] == "cultural-geopolitical-theme-mining-source-registry-v1"
    assert source_snapshot["source_count"] == len(source_snapshot["sources"]) == 118
    assert source_snapshot["boundary"]
    source_ids = [source["id"] for source in source_snapshot["sources"]]
    assert len(set(source_ids)) == len(source_ids)
    assert all(
        source["name"]
        and source["url"]
        and source["role"]
        and source["source_types"]
        and source["license_note"]
        and source["access_notes"]
        for source in source_snapshot["sources"]
    )
    family_registry = json.loads((ANALYSIS / "source-family-registry.json").read_text())
    assert family_registry["schema"] == "external-trend-intelligence.source-family-registry.v1"
    families = {family["id"]: family for family in family_registry["source_families"]}
    assert len(families) == 8
    for family_id in ("annual-report-research", "inc5000-analysis"):
        family = families[family_id]
        assert family["status"] == "pinned_external_snapshot"
        assert family["revision"]
        assert family["manifest_paths"]
        assert family["pin_note"]
    repository_snapshot = json.loads((ANALYSIS / "repository-family-snapshot.json").read_text())
    assert repository_snapshot["schema"] == "external-trend-intelligence.repository-family-snapshot.v1"
    snapshot_families = {family["id"]: family for family in repository_snapshot["families"]}
    for family_id in ("annual-report-research", "inc5000-analysis"):
        family = snapshot_families[family_id]
        assert family["revision"] == families[family_id]["revision"]
        assert family["manifest_paths"]
        assert all(entry["blob"] and entry["size"] >= 0 for entry in family["manifest_paths"])
        assert all(count >= 0 for count in family["directory_prefix_counts"].values())
        assert family["boundary"]
    intake_queue = json.loads((ANALYSIS / "external-family-intake-queue.json").read_text())
    assert intake_queue["schema"] == "external-trend-intelligence.external-family-intake-queue.v1"
    assert len(intake_queue["items"]) == 4
    assert intake_queue["promotion_rule"]
    for item in intake_queue["items"]:
        assert item["family_id"] in snapshot_families
        assert item["source_path"]
        assert item["target_observations"]
        assert item["status"] == "ready_for_extraction"
        assert item["boundary"]
    family_observations = json.loads((ANALYSIS / "external-family-observations.json").read_text())
    assert family_observations["schema"] == "external-trend-intelligence.external-family-observations.v1"
    assert family_observations["observation_count"] == len(family_observations["observations"]) == 5
    observation_ids = [observation["observation_id"] for observation in family_observations["observations"]]
    assert len(set(observation_ids)) == len(observation_ids)
    for observation in family_observations["observations"]:
        assert observation["family_id"] in snapshot_families
        assert observation["source_path"]
        assert observation["source_revision"] == snapshot_families[observation["family_id"]]["revision"]
        assert observation["title"] and observation["unit"]
        assert observation["evidence_status"] in {"reported_candidate", "reported_queue", "reported_provenance", "reported_synthesis"}
        assert observation["boundary"]
        if observation["observation_id"].endswith("source-linked-share"):
            assert observation["source_url_status"] == "present_in_artifact"
            assert observation["source_urls"]
            assert observation["source_url_count"] == len(observation["source_urls"])
            assert observation["denominator"] == "candidate_flagged_companies"
            assert observation["low_growth_counterexample_count"] >= 1
    family_comparisons = json.loads((ANALYSIS / "external-family-comparisons.json").read_text())
    assert family_comparisons["schema"] == "external-trend-intelligence.external-family-comparisons.v1"
    assert len(family_comparisons["comparisons"]) == 3
    family_observation_ids = set(observation_ids)
    for comparison in family_comparisons["comparisons"]:
        assert comparison["observation_ids"]
        assert set(comparison["observation_ids"]) <= family_observation_ids
        assert comparison["relationship"] in {"thematic_adjacency", "mechanism_hypothesis"}
        assert comparison["status"] == "held_no_join"
        assert comparison["rationale"] and comparison["counter_signal"]
        assert comparison["next_test"] and comparison["promotion_gate"]
    lineage_review = json.loads((ANALYSIS / "external-family-lineage-review.json").read_text())
    assert lineage_review["schema"] == "external-trend-intelligence.external-family-lineage-review.v1"
    assert len(lineage_review["reviews"]) == len(family_observations["observations"])
    assert lineage_review["promotion_rule"]
    for review in lineage_review["reviews"]:
        assert review["observation_id"] in family_observation_ids
        assert review["status"] in {"not_started", "partial", "complete"}
        assert review["independence_status"] == "unverified"
        assert review["promotion_decision"] == "hold"
        assert review["remaining"]
    lineage = (ANALYSIS / "SOURCE-LINEAGE-AUDIT.md").read_text()
    assert "source-independence result" in lineage
    assert "partially source-mapped" in lineage
    assert "dependent_restatement" in lineage
    print(
        "valid external trend intelligence:",
        manifest["record_count"],
        "records;",
        len(record_refs),
        "candidate evidence references;",
        len(manifest["program_theme_counts"]),
        "themes",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
