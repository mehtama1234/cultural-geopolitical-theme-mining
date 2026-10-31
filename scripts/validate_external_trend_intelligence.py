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
    assert "external-family-observations.json" in candidates
    assert "external-family-comparisons.json" in candidates
    assert "CARE-CAPACITY-CANDIDATE.md" in candidates
    assert "adaptation-control-candidate.json" in candidates
    runbook = (ANALYSIS / "REFRESH-RUNBOOK.md").read_text()
    next_actions = (ANALYSIS / "NEXT-ACTIONS.md").read_text()
    assert "build_external_repository_family_snapshot.py" in runbook
    assert "build_external_family_observations.py" in runbook
    assert "validate_external_trend_intelligence.py" in runbook
    assert "No internal company join" in runbook
    assert "IBIS discovery findings" in next_actions
    assert "build_external_evidence_gap_queue.py" in next_actions
    assert "build_ibis_finding_claim_sample.py" in runbook
    refresh_schedule = json.loads((ANALYSIS / "refresh-schedule.json").read_text())
    assert refresh_schedule["schema"] == "external-trend-intelligence.refresh-schedule.v1"
    assert len(refresh_schedule["families"]) == 8
    assert {family["family_id"] for family in refresh_schedule["families"]} == {
        "cultural-geopolitical-theme-mining",
        "social-research",
        "trend-hunting",
        "annual-report-research",
        "inc5000-analysis",
        "ibis-industries",
        "research-signals",
        "organization-intelligence-system",
    }
    assert all(
        family["cadence"] and family["trigger"] and family["refresh_artifacts"]
        for family in refresh_schedule["families"]
    )
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
    for family_id in ("annual-report-research", "inc5000-analysis", "ibis-industries", "social-research", "trend-hunting"):
        family = families[family_id]
        assert family["status"] == "pinned_external_snapshot"
        assert family["revision"]
        assert family["manifest_paths"]
        assert family["pin_note"]
    assert "trends-observatory" in families["annual-report-research"]["aliases"]
    assert families["annual-report-research"]["alias_status"] == "no_separate_local_checkout_found"
    assert "source-level lineage" in family_registry["next_action"]
    repository_snapshot = json.loads((ANALYSIS / "repository-family-snapshot.json").read_text())
    assert repository_snapshot["schema"] == "external-trend-intelligence.repository-family-snapshot.v1"
    snapshot_families = {family["id"]: family for family in repository_snapshot["families"]}
    for family_id in ("annual-report-research", "inc5000-analysis", "ibis-industries", "social-research", "trend-hunting"):
        family = snapshot_families[family_id]
        assert family["revision"] == families[family_id]["revision"]
        assert family["manifest_paths"]
        assert {entry["path"] for entry in family["manifest_paths"]} == set(families[family_id]["manifest_paths"])
        assert all(entry["blob"] and entry["size"] >= 0 for entry in family["manifest_paths"])
        assert all(count >= 0 for count in family["directory_prefix_counts"].values())
        assert family["boundary"]
    intake_queue = json.loads((ANALYSIS / "external-family-intake-queue.json").read_text())
    assert intake_queue["schema"] == "external-trend-intelligence.external-family-intake-queue.v1"
    assert len(intake_queue["items"]) == 9
    assert intake_queue["promotion_rule"]
    for item in intake_queue["items"]:
        assert item["family_id"] in snapshot_families
        assert item["source_path"]
        assert item["target_observations"]
        assert item["status"] == "ready_for_extraction"
        assert item["boundary"]
    family_observations = json.loads((ANALYSIS / "external-family-observations.json").read_text())
    assert family_observations["schema"] == "external-trend-intelligence.external-family-observations.v1"
    assert family_observations["observation_count"] == len(family_observations["observations"]) == 10
    observation_ids = [observation["observation_id"] for observation in family_observations["observations"]]
    assert len(set(observation_ids)) == len(observation_ids)
    for observation in family_observations["observations"]:
        assert observation["family_id"] in snapshot_families
        assert observation["source_path"]
        assert observation["source_revision"] == snapshot_families[observation["family_id"]]["revision"]
        assert observation["title"] and observation["unit"]
        assert observation["observation_period"] and observation["observation_period"] != "artifact release dated 2026-10-30 or pinned revision"
        assert observation["evidence_status"] in {"reported_candidate", "reported_queue", "reported_provenance", "reported_synthesis"}
        assert observation["boundary"]
        if observation["observation_id"].endswith("source-linked-share"):
            assert observation["source_url_status"] == "present_in_artifact"
            assert observation["source_urls"]
            assert observation["source_url_count"] == len(observation["source_urls"])
            assert observation["denominator"] == "candidate_flagged_companies"
            assert observation["low_growth_counterexample_count"] >= 1
        if observation["observation_id"] == "ibis-industry-record-corpus":
            assert observation["source_url_status"] == "inventory_present"
            assert observation["source_inventory_count"] == 17998
            assert observation["public_url_count"] == 17087
            assert observation["unlinked_source_count"] == 911
        if observation["observation_id"] == "social-integrated-trend-atlas":
            assert observation["collection_round_count"] >= 1
            assert observation["collection_file_count"] >= 1
            assert observation["collection_failure_count"] == 0
            assert observation["collection_platform_counts"]
        if observation["observation_id"] == "annual-report-integrated-theme-map":
            assert observation["source_url_status"] == "present_in_artifact"
            assert observation["source_url_count"] == len(observation["source_urls"]) >= 1
            assert observation["citation_row_count"] == len(observation["citation_source_ids"]) >= observation["source_url_count"]
            assert sum(observation["citation_category_counts"].values()) == observation["citation_row_count"]
        if observation["observation_id"] == "inc5000-rebuild-public-input-inventory":
            assert observation["source_url_status"] == "present_in_artifact"
            assert observation["independent_source_record_count"] == 104
            assert observation["independent_source_unique_company_count"] == 95
            assert observation["source_url_count"] == len(observation["source_urls"]) >= 1
        if observation["observation_id"] == "inc5000-opportunity-intelligence-screen":
            assert observation["source_url_status"] == "present_in_artifact"
            assert observation["opportunity_evidence_opportunity_count"] == 5
            assert observation["opportunity_evidence_record_count"] >= 1
            assert observation["source_url_count"] == len(observation["source_urls"]) >= 1
        if observation["observation_id"] == "ibis-cross-industry-business-forces":
            assert observation["source_url_status"] == "present_in_artifact"
            assert observation["source_ids"] and observation["source_url_count"] == len(observation["source_urls"]) >= 1
        if observation["observation_id"] == "ibis-cross-industry-discovery-findings":
            assert observation["pattern_artifacts_pinned"] is True
            assert len(observation["pattern_artifact_paths"]) == 3
            assert len(observation["pattern_aggregate_counts"]) == 12
            assert observation["pattern_claim_count_total"] > 0
            assert observation["pattern_source_count_total"] > 0
        if observation["observation_id"] == "trend-hunting-ai-deep-synthesis":
            assert observation["source_url_status"] == "present_in_artifact"
            assert len(observation["source_input_paths"]) == 16
            assert observation["source_url_count"] == len(observation["source_urls"]) >= 1
        if observation["observation_id"] == "social-integrated-trend-atlas":
            assert observation["publication_evidence_url_count"] == 89
            assert observation["source_url_status"] == "present_in_artifact"
            assert observation["source_url_count"] == len(observation["source_urls"]) >= 1
    family_comparisons = json.loads((ANALYSIS / "external-family-comparisons.json").read_text())
    assert family_comparisons["schema"] == "external-trend-intelligence.external-family-comparisons.v1"
    assert len(family_comparisons["comparisons"]) == 8
    family_observation_ids = set(observation_ids)
    candidate_ids = {candidate["id"] for candidate in machine["candidates"]}
    for comparison in family_comparisons["comparisons"]:
        assert comparison["observation_ids"]
        assert set(comparison["observation_ids"]) <= family_observation_ids
        if "existing_candidate_ids" in comparison:
            assert set(comparison["existing_candidate_ids"]) <= candidate_ids
        assert comparison["relationship"] in {"thematic_adjacency", "mechanism_hypothesis"}
        assert comparison["status"] == "held_no_join"
        assert comparison["rationale"] and comparison["counter_signal"]
        assert comparison["next_test"] and comparison["promotion_gate"]
    lineage_review = json.loads((ANALYSIS / "external-family-lineage-review.json").read_text())
    assert lineage_review["schema"] == "external-trend-intelligence.external-family-lineage-review.v1"
    assert len(lineage_review["reviews"]) == len(family_observations["observations"])
    assert lineage_review["promotion_rule"]
    assert "cross_observation_url_overlap" in lineage_review
    assert "cross_observation_host_overlap" in lineage_review
    assert all(len(ids) > 1 for ids in lineage_review["cross_observation_url_overlap"].values())
    for review in lineage_review["reviews"]:
        assert review["observation_id"] in family_observation_ids
        assert isinstance(review["cross_observation_shared_urls"], list)
        assert isinstance(review["cross_observation_shared_hosts"], list)
        assert review["status"] in {"not_started", "partial", "complete"}
        assert review["independence_status"] == "unverified"
        assert review["promotion_decision"] == "hold"
        assert review["remaining"]
    gap_queue = json.loads((ANALYSIS / "external-evidence-gap-queue.json").read_text())
    assert gap_queue["schema"] == "external-trend-intelligence.external-evidence-gap-queue.v1"
    assert gap_queue["gap_count"] == len(gap_queue["gaps"]) == len(lineage_review["reviews"])
    assert gap_queue["high_priority_count"] == 1
    assert {gap["observation_id"] for gap in gap_queue["gaps"]} == family_observation_ids
    assert all(gap["decision"] == "hold" and gap["missing_evidence"] for gap in gap_queue["gaps"])
    ibis_sample = json.loads((ANALYSIS / "ibis-finding-claim-sample.json").read_text())
    assert ibis_sample["schema"] == "external-trend-intelligence.ibis-finding-claim-sample.v1"
    assert ibis_sample["finding_slug"] == "compliance-as-economic-architecture"
    assert ibis_sample["sample_status"] == "bounded_traceability_sample"
    assert ibis_sample["sample_industry_count"] == len(ibis_sample["samples"]) == 3
    assert all(sample["claims"] for sample in ibis_sample["samples"])
    assert any(claim["sources"] for sample in ibis_sample["samples"] for claim in sample["claims"])
    care_candidate = json.loads((ANALYSIS / "care-capacity-candidate.json").read_text())
    assert care_candidate["schema"] == "external-trend-intelligence.external-care-capacity-candidate.v1"
    assert care_candidate["status"] == "held_candidate"
    assert len(care_candidate["main_manifest_evidence_ids"]) == 7
    assert set(care_candidate["main_manifest_evidence_ids"]) <= ids
    assert set(care_candidate["external_family_observation_ids"]) <= family_observation_ids
    assert care_candidate["mechanism"] and care_candidate["counter_signal"]
    assert care_candidate["next_test"] and care_candidate["promotion_gate"]
    care_markdown = (ANALYSIS / "CARE-CAPACITY-CANDIDATE.md").read_text()
    assert "held_candidate" in care_markdown
    assert "Promotion test" in care_markdown
    measurement_matrix = json.loads((ANALYSIS / "care-capacity-measurement-matrix.json").read_text())
    assert measurement_matrix["schema"] == "external-trend-intelligence.care-capacity-measurement-matrix.v1"
    assert measurement_matrix["candidate_id"] == care_candidate["candidate_id"]
    assert measurement_matrix["status"] == "measurement_reconciliation_required"
    assert len(measurement_matrix["rows"]) == len(care_candidate["main_manifest_evidence_ids"]) == 7
    assert set(row["record_id"] for row in measurement_matrix["rows"]) == set(care_candidate["main_manifest_evidence_ids"])
    assert all(row["observations"] for row in measurement_matrix["rows"])
    assert measurement_matrix["decision"] == "hold"
    assert measurement_matrix["decision_reason"]
    release_manifest = json.loads((ANALYSIS / "release-manifest.json").read_text())
    assert release_manifest["schema"] == "external-trend-intelligence.release-manifest.v1"
    assert release_manifest["artifact_count"] == len(release_manifest["artifacts"]) == 24
    assert re.fullmatch(r"[0-9a-f]{40}", release_manifest["source_tree_commit"])
    assert release_manifest["boundary"]
    for artifact in release_manifest["artifacts"]:
        path = ROOT / artifact["path"]
        assert path.exists(), artifact["path"]
        assert artifact["bytes"] == path.stat().st_size
    care_subset = json.loads((ANALYSIS / "care-capacity-comparable-subset.json").read_text())
    assert care_subset["schema"] == "external-trend-intelligence.care-capacity-comparable-subset.v1"
    assert care_subset["candidate_id"] == care_candidate["candidate_id"]
    assert care_subset["status"] == "contextual_comparison_only"
    assert len(care_subset["measures"]) == 6
    assert set(measure["record_id"] for measure in care_subset["measures"]) <= set(care_candidate["main_manifest_evidence_ids"])
    assert care_subset["decision"] == "hold"
    assert care_subset["next_test"] and care_subset["boundary"]
    adaptation_candidate = json.loads((ANALYSIS / "adaptation-control-candidate.json").read_text())
    assert adaptation_candidate["schema"] == "external-trend-intelligence.external-adaptation-control-candidate.v1"
    assert adaptation_candidate["status"] == "held_candidate"
    assert set(adaptation_candidate["external_family_observation_ids"]) <= family_observation_ids
    assert adaptation_candidate["mechanism"] and adaptation_candidate["counter_signal"]
    assert adaptation_candidate["next_test"] and adaptation_candidate["promotion_gate"]
    held_candidates = json.loads((ANALYSIS / "held-candidates.json").read_text())
    assert held_candidates["schema"] == "external-trend-intelligence.held-candidates.v1"
    assert len(held_candidates["candidates"]) == 2
    assert all(candidate["status"] == "held_candidate" for candidate in held_candidates["candidates"])
    assert all(candidate["mechanism"] and candidate["counter_signal"] and candidate["next_test"] for candidate in held_candidates["candidates"])
    promotion_queue = json.loads((ANALYSIS / "promotion-queue.json").read_text())
    assert promotion_queue["schema"] == "external-trend-intelligence.promotion-queue.v1"
    assert promotion_queue["internal_bridge_rule"]
    promotion_ids = {candidate["candidate_id"] for candidate in promotion_queue["candidates"]}
    assert promotion_ids == {
        "candidate-formal-response-before-recovery",
        "candidate-time-financial-pressure-practical-room",
        "candidate-digital-capability-control-trust",
        "candidate-infrastructure-dependency-power",
        "candidate-care-longevity-access-capacity",
        "candidate-adaptation-control-proof-resilience",
    }
    assert all(candidate["blocking_gates"] and candidate["next_action"] for candidate in promotion_queue["candidates"])
    assert all(candidate["internal_bridge_ready"] is False for candidate in promotion_queue["candidates"])
    social_observation = next(observation for observation in family_observations["observations"] if observation["family_id"] == "social-research")
    trend_observation = next(observation for observation in family_observations["observations"] if observation["family_id"] == "trend-hunting")
    assert social_observation["generated_at"] and social_observation["method"] and social_observation["artifact_evidence_boundary"]
    assert trend_observation["checked"] and trend_observation["input_checksum_count"] >= 1 and trend_observation["artifact_inputs"]
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
