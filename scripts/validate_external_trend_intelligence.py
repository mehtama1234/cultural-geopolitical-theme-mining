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
    theme_audit = json.loads((ANALYSIS / "theme-coverage-audit.json").read_text())
    assert theme_audit["schema"] == "external-trend-intelligence.theme-coverage-audit.v1"
    assert theme_audit["status"] == "theme_coverage_visible_quality_unresolved"
    assert theme_audit["theme_count"] == theme_audit["observed_theme_count"] == 14
    assert theme_audit["sparse_theme_count"] == len(theme_audit["sparse_themes"])
    assert all(row["coverage_status"] == "observed" and row["quality_boundary"] for row in theme_audit["themes"].values())
    assert all(
        row["source_url_count"] >= row["unique_source_url_count"] >= 0
        and row["reused_source_url_count"] == row["source_url_count"] - row["unique_source_url_count"]
        and 0 <= row["source_url_reuse_ratio"] <= 1
        for row in theme_audit["themes"].values()
    )
    domain_audit = json.loads((ANALYSIS / "domain-coverage-audit.json").read_text())
    assert domain_audit["schema"] == "external-trend-intelligence.domain-coverage-audit.v1"
    assert domain_audit["required_domain_count"] == 9
    assert domain_audit["observed_domain_count"] + len(domain_audit["missing_domains"]) == domain_audit["required_domain_count"]
    assert all(row["coverage_status"] in {"observed", "missing"} and row["quality_boundary"] for row in domain_audit["domains"].values())
    assert domain_audit["boundary"] and domain_audit["next_action"]
    record_quality = json.loads((ANALYSIS / "record-quality-audit.json").read_text())
    assert record_quality["schema"] == "external-trend-intelligence.record-quality-audit.v1"
    assert record_quality["record_count"] == manifest["record_count"]
    assert set(record_quality["field_counts"]) == set(record_quality["field_coverage"])
    assert all(0 <= value <= 1 for value in record_quality["field_coverage"].values())
    assert record_quality["boundary"] and record_quality["next_action"]
    remediation = json.loads((ANALYSIS / "record-quality-remediation-queue.json").read_text())
    assert remediation["schema"] == "external-trend-intelligence.record-quality-remediation-queue.v1"
    assert remediation["status"] in {"remediation_required", "no_open_record_metadata_gaps"}
    assert remediation["record_count_with_gaps"] >= remediation["high_priority_count"] >= 0
    assert len(remediation["rows"]) <= remediation["row_limit"]
    assert remediation["boundary"] and remediation["next_action"]
    host_dependence = json.loads((ANALYSIS / "record-host-dependence-audit.json").read_text())
    assert host_dependence["schema"] == "external-trend-intelligence.record-host-dependence-audit.v1"
    assert host_dependence["record_count"] == manifest["record_count"]
    assert host_dependence["unique_host_count"] >= host_dependence["shared_host_count"] >= 0
    assert len(host_dependence["host_rows"]) <= host_dependence["host_row_limit"]
    assert len(host_dependence["shared_host_pairs"]) <= host_dependence["shared_host_pair_limit"]
    assert host_dependence["boundary"] and host_dependence["next_action"]
    host_queue = json.loads((ANALYSIS / "host-dependence-review-queue.json").read_text())
    assert host_queue["schema"] == "external-trend-intelligence.host-dependence-review-queue.v1"
    assert host_queue["shared_host_count"] == host_dependence["shared_host_count"]
    assert host_queue["unassigned_count"] >= host_queue["high_priority_count"] >= 0
    assert len(host_queue["rows"]) <= host_queue["row_limit"]
    assert host_queue["boundary"] and host_queue["next_action"]
    open_gates = json.loads((ANALYSIS / "open-gate-register.json").read_text())
    assert open_gates["schema"] == "external-trend-intelligence.open-gate-register.v1"
    assert open_gates["gate_count"] == len(open_gates["gates"])
    assert open_gates["critical_gate_count"] >= 0
    assert open_gates["total_open_work_items"] == sum(gate["open_count"] for gate in open_gates["gates"])
    assert open_gates["boundary"] and open_gates["next_action"]
    gate_history = json.loads((ANALYSIS / "open-gate-history.json").read_text())
    assert gate_history["schema"] == "external-trend-intelligence.open-gate-history.v1"
    assert gate_history["snapshot_count"] == len(gate_history["snapshots"]) >= 1
    assert gate_history["latest_total_open_work_items"] == open_gates["total_open_work_items"]
    assert gate_history["latest_critical_gate_count"] == open_gates["critical_gate_count"]
    assert gate_history["append_only"] is True and gate_history["boundary"] and gate_history["next_action"]
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
    source_registry_doc = (ROOT / "EXTERNAL_SOURCE_REGISTRY.md").read_text()
    assert "## Source status vocabulary" in source_registry_doc
    assert "Registered:" in source_registry_doc
    assert "Evidence-ready:" in source_registry_doc
    assert "Independently confirmed:" in source_registry_doc
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
    assert len(machine["candidates"]) >= 1
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
            assert observation["source_url_status"] == "bounded_sample_present"
            assert observation["traceability_sample_industry_count"] > 0
            assert observation["source_url_count"] == len(observation["source_urls"]) >= 1
        if observation["observation_id"] == "trend-hunting-ai-deep-synthesis":
            assert observation["source_url_status"] == "present_in_artifact"
            assert len(observation["source_input_paths"]) == 16
            assert observation["source_url_count"] == len(observation["source_urls"]) >= 1
            assert observation["source_map_input_count"] == 16
            assert observation["source_map_mapped_row_count"] > 0
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
    assert gap_queue["high_priority_count"] == 0
    assert {gap["observation_id"] for gap in gap_queue["gaps"]} == family_observation_ids
    assert all(gap["decision"] == "hold" and gap["missing_evidence"] for gap in gap_queue["gaps"])
    ibis_sample = json.loads((ANALYSIS / "ibis-finding-claim-sample.json").read_text())
    assert ibis_sample["schema"] == "external-trend-intelligence.ibis-finding-claim-sample.v1"
    assert ibis_sample["finding_slug"] == "compliance-as-economic-architecture"
    assert ibis_sample["sample_status"] == "bounded_traceability_sample"
    assert ibis_sample["sample_industry_count"] == len(ibis_sample["samples"])
    assert ibis_sample["sample_sector_count"] >= 20
    ibis_review = json.loads((ANALYSIS / "ibis-claim-source-review.json").read_text())
    assert ibis_review["schema"] == "external-trend-intelligence.ibis-claim-source-review.v1"
    assert ibis_review["sample_industry_count"] == ibis_sample["sample_industry_count"]
    assert ibis_review["independence_status"] == "not_qualified"
    assert ibis_review["outcome_validation_status"] == "not_observed_in_traceability_sample"
    ibis_independence = json.loads((ANALYSIS / "ibis-claim-independence-audit.json").read_text())
    assert ibis_independence["schema"] == "external-trend-intelligence.ibis-claim-independence-audit.v1"
    assert ibis_independence["status"] == "dependency_audit_complete_independence_unverified"
    assert ibis_independence["sample_claim_count"] == ibis_sample["claim_review_summary"]["claim_count"]
    assert ibis_independence["unique_url_count"] >= ibis_independence["reused_url_count"]
    assert ibis_independence["unique_host_count"] >= ibis_independence["reused_host_count"]
    assert ibis_independence["dependency_flag_counts"]
    assert ibis_independence["next_action"] and ibis_independence["boundary"]
    ibis_queue = json.loads((ANALYSIS / "ibis-claim-independence-review-queue.json").read_text())
    assert ibis_queue["schema"] == "external-trend-intelligence.ibis-claim-independence-review-queue.v1"
    assert ibis_queue["status"] == "manual_review_queue_ready"
    assert ibis_queue["candidate_count"] == ibis_independence["independence_status_counts"]["candidate_for_manual_review"]
    assert ibis_queue["unassigned_count"] == ibis_queue["candidate_count"]
    assert all(row["required_evidence"] and row["stop_rule"] for row in ibis_queue["candidates"])
    assert all(row["company_bridge_status"] == "blocked_external_first_gate" for row in ibis_queue["candidates"])
    ibis_batch = json.loads((ANALYSIS / "ibis-first-review-batch.json").read_text())
    assert ibis_batch["schema"] == "external-trend-intelligence.ibis-first-review-batch.v1"
    assert ibis_batch["status"] == "first_batch_ready_for_manual_review"
    assert ibis_batch["batch_size"] == len(ibis_batch["claims"]) == min(10, ibis_queue["candidate_count"])
    assert all(row["review_status"] == "pending_manual_review" and row["disposition"] == "pending" for row in ibis_batch["claims"])
    assert all(row["required_review"] and row["stop_rule"] for row in ibis_batch["claims"])
    ibis_dispositions = json.loads((ANALYSIS / "ibis-claim-review-dispositions.json").read_text())
    assert ibis_dispositions["schema"] == "external-trend-intelligence.ibis-claim-review-dispositions.v1"
    assert ibis_dispositions["status"] == "ten_conservative_triage_dispositions_recorded"
    assert ibis_dispositions["completed_disposition_count"] == 10
    assert ibis_dispositions["pending_first_batch_count"] == ibis_batch["batch_size"] - 10
    assert {row["disposition"] for row in ibis_dispositions["dispositions"]} == {"held_insufficient_evidence", "held_outcome_missing"}
    assert all(row["company_bridge_status"] == "blocked_external_first_gate" for row in ibis_dispositions["dispositions"])
    assert ibis_dispositions["next_action"] and ibis_dispositions["boundary"]
    repair_plan = json.loads((ANALYSIS / "cell-phone-repair-outcome-acquisition-plan.json").read_text())
    assert repair_plan["schema"] == "external-trend-intelligence.cell-phone-repair-outcome-acquisition-plan.v1"
    assert repair_plan["status"] == "held_outcome_acquisition_ready"
    assert repair_plan["current_disposition"] == "held_outcome_missing"
    assert repair_plan["observed_proxy_artifact"] == "census-repair-industry-snapshot.json"
    assert repair_plan["observed_proxy_status"] == "descriptive_industry_proxy_not_phone_outcome"
    assert len(repair_plan["why_not_pooled"]) >= 3
    assert repair_plan["target_outcome"]["required_measures"]
    assert repair_plan["acceptance_criteria"] and repair_plan["stop_rule"]
    assert len(repair_plan["source_screen_2026_10_31"]) == 6
    assert {row["screen_status"] for row in repair_plan["source_screen_2026_10_31"]} >= {"best_public_candidate", "counter_signal_only"}
    assert any(row["publisher"] == "Open Repair Alliance" and row["screen_status"] == "phone_specific_global_outcome_candidate_gated_download" for row in repair_plan["source_screen_2026_10_31"])
    assert repair_plan["observed_outcome_proxy_artifact"] == "open-repair-alliance-mobile-snapshot.json"
    assert repair_plan["observed_outcome_proxy_status"] == "acquired_phone_specific_global_community_repair_proxy_not_policy_outcome"
    ora_mobile = json.loads((ANALYSIS / "open-repair-alliance-mobile-snapshot.json").read_text())
    assert ora_mobile["schema"] == "external-trend-intelligence.open-repair-alliance-mobile-snapshot.v1"
    assert ora_mobile["status"] == "acquired_phone_specific_global_community_repair_proxy_not_policy_outcome"
    assert ora_mobile["coverage"]["mobile_record_count"] > 6000
    assert ora_mobile["coverage"]["us_mobile_record_count"] > 200
    assert ora_mobile["source"]["license"] == "CC BY-SA 4.0"
    assert ora_mobile["pooling_decision"] == "do_not_pool_with_census_industry_proxies_state_policy_or_global_ewaste"
    assert ora_mobile["interpretation_boundary"] and ora_mobile["uncertainty"] and ora_mobile["falsifier"]
    ora_adequacy = json.loads((ANALYSIS / "open-repair-alliance-mobile-adequacy-review.json").read_text())
    assert ora_adequacy["schema"] == "external-trend-intelligence.open-repair-alliance-mobile-adequacy-review.v1"
    assert ora_adequacy["status"] == "acquired_but_policy_backtest_inadequate"
    assert ora_adequacy["observed_scope"]["global_mobile_records"] == ora_mobile["coverage"]["mobile_record_count"]
    assert ora_adequacy["observed_scope"]["us_mobile_records"] == ora_mobile["coverage"]["us_mobile_record_count"]
    assert not any(ora_adequacy["field_coverage_assessment"].values())
    assert len(ora_adequacy["why_held"]) >= 3 and ora_adequacy["next_action"] and ora_adequacy["falsifier"]
    census_repair = json.loads((ANALYSIS / "census-repair-industry-snapshot.json").read_text())
    assert census_repair["schema"] == "external-trend-intelligence.census-repair-industry-snapshot.v1"
    assert census_repair["status"] == "descriptive_industry_proxy_not_phone_outcome"
    assert census_repair["coverage"]["years"] == [2019, 2020, 2021, 2022, 2023]
    assert census_repair["coverage"]["national_row_count"] == 10
    assert census_repair["coverage"]["state_row_count"] > 400
    assert len(census_repair["source"]["retrievals"]) == 10
    assert census_repair["pooling_decision"] == "do_not_pool_with_state_policy_or_global_ewaste"
    assert census_repair["interpretation_boundary"] and census_repair["uncertainty"]
    census_nonemployer = json.loads((ANALYSIS / "census-nonemployer-repair-snapshot.json").read_text())
    assert census_nonemployer["schema"] == "external-trend-intelligence.census-nonemployer-repair-snapshot.v1"
    assert census_nonemployer["status"] == "descriptive_nonemployer_industry_proxy_not_phone_outcome"
    assert census_nonemployer["coverage"]["years"] == [2019, 2020, 2021, 2022, 2023, 2024]
    assert census_nonemployer["coverage"]["national_row_count"] == 6
    assert census_nonemployer["coverage"]["state_row_count"] > 250
    assert len(census_nonemployer["source"]["retrievals"]) == 12
    assert census_nonemployer["pooling_decision"] == "do_not_pool_with_state_policy_global_ewaste_or_cbp_paid_employee_series"
    assert census_nonemployer["interpretation_boundary"] and census_nonemployer["uncertainty"]
    repair_comparison = json.loads((ANALYSIS / "census-repair-proxy-comparison.json").read_text())
    assert repair_comparison["schema"] == "external-trend-intelligence.census-repair-proxy-comparison.v1"
    assert repair_comparison["status"] == "bounded_same_publisher_comparison_not_independent_confirmation"
    assert repair_comparison["coverage"]["years"] == [2019, 2020, 2021, 2022, 2023]
    assert repair_comparison["coverage"]["row_count"] == 5
    assert repair_comparison["measurement_map"]["same_publisher"] is True
    assert repair_comparison["pooling_decision"] == "do_not_pool_or_count_as_independent_confirmation"
    assert repair_comparison["counter_signals"] and repair_comparison["falsifier"]
    ibis_force_map = json.loads((ANALYSIS / "ibis-force-claim-map.json").read_text())
    assert ibis_force_map["schema"] == "external-trend-intelligence.ibis-force-claim-map.v1"
    assert ibis_force_map["force_count"] == len(ibis_force_map["forces"]) == 6
    assert ibis_force_map["aggregate"]["declared_source_id_count"] == 21
    assert ibis_force_map["aggregate"]["resolved_source_id_count"] == 21
    assert ibis_force_map["aggregate"]["unresolved_source_id_count"] == 0
    assert ibis_force_map["aggregate"]["claim_reference_count"] > 0
    assert all(force["falsifiers"] and force["outcome_measure_candidates"] for force in ibis_force_map["forces"])
    assert all(force["review_status"] == "held_claim_level_lineage_and_independence" for force in ibis_force_map["forces"])
    ibis_force_review = json.loads((ANALYSIS / "ibis-force-claim-review.json").read_text())
    assert ibis_force_review["schema"] == "external-trend-intelligence.ibis-force-claim-review.v1"
    assert ibis_force_review["force_count"] == 6
    assert ibis_force_review["status"] == "held_pending_claim_level_lineage_independence_and_outcome_review"
    assert all(row["falsifiers"] and row["outcome_measure_candidates"] for row in ibis_force_review["rows"])
    labor_check = json.loads((ANALYSIS / "bls-labor-capacity-mechanism-check.json").read_text())
    assert labor_check["schema"] == "external-trend-intelligence.bls-labor-capacity-mechanism-check.v1"
    assert labor_check["status"] == "held_mechanism_check_same_publisher"
    assert len(labor_check["rows"]) == 2
    assert labor_check["counter_signal"] and labor_check["falsifier"]
    assert labor_check["source_publisher_dependence"]
    annual_map = json.loads((ANALYSIS / "annual-report-citation-map.json").read_text())
    assert annual_map["schema"] == "external-trend-intelligence.annual-report-citation-map.v1"
    assert annual_map["row_count"] == len(annual_map["rows"]) == 25
    assert annual_map["publisher_host_count"] >= 5
    assert all(row["public_url"].startswith("http") and row["boundary"] for row in annual_map["rows"])
    social_map = json.loads((ANALYSIS / "social-publication-citation-map.json").read_text())
    assert social_map["schema"] == "external-trend-intelligence.social-publication-citation-map.v1"
    assert social_map["appendix_raw_url_count"] == 89
    assert social_map["theme_linked_citation_count"] == 31
    assert social_map["theme_linked_unique_url_count"] >= 20
    assert social_map["boundary"] and social_map["next_test"]
    inc_map = json.loads((ANALYSIS / "inc5000-opportunity-source-map.json").read_text())
    assert inc_map["schema"] == "external-trend-intelligence.inc5000-opportunity-source-map.v1"
    assert inc_map["opportunity_count"] == len(inc_map["opportunities"]) == 5
    assert inc_map["evidence_row_count"] == 39
    assert inc_map["buyer_proxy_row_count"] > 0
    assert inc_map["unique_source_url_count"] >= 39
    assert inc_map["field_evidence_status"] == "collection plans ready; direct field evidence pending"
    assert inc_map["boundary"] and inc_map["next_test"]
    dependence = json.loads((ANALYSIS / "publisher-dependence-summary.json").read_text())
    assert dependence["schema"] == "external-trend-intelligence.publisher-dependence-summary.v1"
    assert dependence["source_row_count"] > 0
    assert dependence["shared_host_count"] >= 1
    assert dependence["independence_status"] == "unverified"
    assert dependence["boundary"] and dependence["next_test"]
    shed_emergency = json.loads((ANALYSIS / "shed-emergency-expense-2013-2025.json").read_text())
    assert shed_emergency["schema"] == "external-trend-intelligence.external-acquisition.v1"
    assert shed_emergency["acquisition_id"] == "federal-reserve-shed-emergency-expense-2013-2025"
    assert len(shed_emergency["observations"]) == 13
    assert shed_emergency["observations"][0]["value"] == 50
    assert shed_emergency["observations"][-1]["value"] == 63
    assert shed_emergency["retrieval"]["artifact_sha256"].startswith("sha256:")
    assert shed_emergency["latest_official_report_context"]["report_period"] == "2025"
    assert shed_emergency["latest_official_report_context"]["reported_overall_design_effect"] == 1.14
    assert shed_emergency["latest_official_report_context"]["scope_boundary"]
    assert shed_emergency["boundary"] and shed_emergency["comparability_review"]["next_test"]
    uncertainty = json.loads((ANALYSIS / "shed-emergency-expense-uncertainty-audit.json").read_text())
    assert uncertainty["schema"] == "external-trend-intelligence.uncertainty-audit.v1"
    assert uncertainty["public_sample_size"] == {"2023": 11400, "2024": 12295}
    assert uncertainty["naive_srs_interval"]["status"] == "diagnostic_only_not_release_valid"
    assert uncertainty["design_based_status"] == "not_estimable_from_current_pinned_artifacts"
    assert uncertainty["official_uncertainty_search"]["latest_report_context"]["reported_overall_design_effect"] == 1.14
    assert uncertainty["official_uncertainty_search"]["latest_report_context"]["scope_boundary"]
    assert uncertainty["release_decision"] == "hold"
    assert len(uncertainty["naive_srs_interval"]["diagnostics"]) == 2
    reproduction = json.loads((ANALYSIS / "shed-point-estimate-reproduction-audit.json").read_text())
    assert reproduction["schema"] == "external-trend-intelligence.reproduction-audit.v1"
    assert reproduction["status"] == "point_estimate_reproduced_variance_open"
    assert len(reproduction["microdata"]) == 2
    assert {row["period"] for row in reproduction["microdata"]} == {"2023", "2024"}
    assert {row["row_count"] for row in reproduction["microdata"]} == {11400, 12295}
    assert len(reproduction["reconstructions"]) == 4
    assert all(row["rule"] == "publisher-derived pay_casheqv == Yes" for row in reproduction["reconstructions"][:2])
    assert all(row["published_rounding"] == "63%" for row in reproduction["reconstructions"][:2])
    assert reproduction["next_test"] and reproduction["boundary"]
    trend_map = json.loads((ANALYSIS / "trend-hunting-source-map.json").read_text())
    assert trend_map["schema"] == "external-trend-intelligence.trend-hunting-source-map.v1"
    assert trend_map["source_family"] == "trend-hunting"
    assert trend_map["input_artifact_count"] == 16
    assert trend_map["mapped_row_count"] > 0
    assert trend_map["unique_url_count"] > 0
    assert trend_map["boundary"] and trend_map["next_test"]
    refresh_history = json.loads((ANALYSIS / "refresh-history.json").read_text())
    assert refresh_history["schema"] == "external-trend-intelligence.refresh-history.v1"
    assert refresh_history["run_count"] >= 1
    assert refresh_history["latest"]["record_count"] == manifest["record_count"]
    assert refresh_history["latest"]["parse_error_count"] == 0
    assert refresh_history["latest"]["pipeline_step_count"] > 0
    assert refresh_history["latest"]["pipeline_status"] == "passed"
    continuity = json.loads((ANALYSIS / "refresh-continuity-audit.json").read_text())
    assert continuity["schema"] == "external-trend-intelligence.refresh-continuity-audit.v1"
    assert continuity["run_count"] == refresh_history["run_count"]
    assert continuity["expected_cadence"] == "weekly"
    assert continuity["required_two_year_weeks"] == 104
    assert continuity["observed_distinct_week_count"] >= 0
    assert 0 <= continuity["observed_week_coverage_ratio"] <= 1
    assert continuity["observed_week_coverage_percent"] == round(continuity["observed_week_coverage_ratio"] * 100, 1)
    assert continuity["unattended_two_year_coverage"] == "not_demonstrated"
    assert continuity["next_action"] and continuity["boundary"]
    pilot_blueprint = json.loads((ANALYSIS / "pilot-food-security-service-room-blueprint.json").read_text())
    assert pilot_blueprint["schema"] == "external-trend-intelligence.pilot-blueprint.v1"
    assert pilot_blueprint["status"] == "external_gate_passed_internal_contract_pending"
    assert pilot_blueprint["pilot_id"] == "pilot-food-security-service-room-001"
    assert pilot_blueprint["current_blockers"] and pilot_blueprint["falsifier"] and pilot_blueprint["stop_rule"]
    assert pilot_blueprint["boundary"] and pilot_blueprint["decision_contract_to_complete"]["company_id"] is None
    ownership = json.loads((ANALYSIS / "ownership-assignment-queue.json").read_text())
    assert ownership["schema"] == "external-trend-intelligence.ownership-assignment-queue.v1"
    successor_packet = json.loads((ANALYSIS / "successor-review-packet.json").read_text())
    assert successor_packet["schema"] == "external-trend-intelligence.successor-review-packet.v1"
    assert successor_packet["status"] == "ready_for_named_human_successor"
    assert len(successor_packet["review_tasks"]) == 3
    assert all(task["assignee"] is None and task["signoff"] is None for task in successor_packet["review_tasks"])
    assert successor_packet["acceptance_criteria"] and successor_packet["boundary"]
    independence_queue = json.loads((ANALYSIS / "candidate-independence-adjudication-queue.json").read_text())
    assert independence_queue["schema"] == "external-trend-intelligence.candidate-independence-adjudication-queue.v1"
    assert independence_queue["status"] == "manual_adjudication_queue_ready"
    assert independence_queue["candidate_count"] == 5
    assert independence_queue["unassigned_count"] == independence_queue["candidate_count"]
    assert all(row["required_evidence"] and row["stop_rule"] and row["disposition"] == "pending" for row in independence_queue["rows"])
    independence_request = (ANALYSIS / "INDEPENDENCE-ADJUDICATION-REQUEST.md").read_text()
    assert "Required evidence checklist" in independence_request
    for row in independence_queue["rows"]:
        assert f"`{row['candidate_id']}`" in independence_request
    for field in ("canonical publisher", "underlying dataset", "population", "rights and redistribution boundary"):
        assert field in independence_request
    host_queue = json.loads((ANALYSIS / "host-dependence-review-queue.json").read_text())
    host_request = (ANALYSIS / "HOST-LINEAGE-REVIEW-REQUEST.md").read_text()
    assert host_queue["high_priority_count"] == 23
    assert "Required review fields" in host_request
    for row in host_queue["rows"]:
        if row["priority"] == "high":
            assert f"`{row['host']}`" in host_request
    for field in ("publisher or publishers", "upstream dataset", "rights route", "independence disposition"):
        assert field in host_request.lower()
    continuity_request = (ANALYSIS / "CONTINUITY-REVIEW-REQUEST.md").read_text()
    continuity = json.loads((ANALYSIS / "refresh-continuity-audit.json").read_text())
    assert "Required weekly review fields" in continuity_request
    assert f"{continuity['observed_distinct_week_count']}" in continuity_request
    assert "104 distinct weekly windows" in continuity_request
    for field in ("scheduled window", "freshness", "recovery evidence", "release-owner review"):
        assert field in continuity_request.lower()
    precheck = json.loads((ANALYSIS / "candidate-independence-precheck.json").read_text())
    assert precheck["schema"] == "external-trend-intelligence.candidate-independence-precheck.v1"
    assert precheck["status"] == "machine_precheck_recorded_human_adjudication_required"
    assert precheck["candidate_count"] == len(precheck["rows"]) == 2
    precheck_row = next(row for row in precheck["rows"] if row["candidate_id"] == "candidate-us-food-insecurity-persistence")
    assert precheck_row["candidate_id"] == "candidate-us-food-insecurity-persistence"
    assert precheck_row["precheck_status"] == "provisional_distinct_publishers_noncomparable_hold"
    assert precheck_row["machine_evidence"]["distinct_publisher_families"] is True
    assert precheck_row["machine_evidence"]["distinct_hosts"] is True
    assert precheck_row["unresolved_manual_review"] and precheck_row["qualification_effect"].startswith("none")
    phone_precheck = next(row for row in precheck["rows"] if row["candidate_id"] == "candidate-cell-phone-repair-policy-outcome")
    assert phone_precheck["precheck_status"] == "distinct_publishers_outcome_scope_mismatch_hold"
    assert phone_precheck["machine_evidence"]["distinct_publisher_families"] is True
    assert phone_precheck["machine_evidence"]["distinct_hosts"] is True
    assert phone_precheck["unresolved_manual_review"] and phone_precheck["qualification_effect"].startswith("none")
    pilot_intake = json.loads((ANALYSIS / "pilot-contract-intake.json").read_text())
    assert pilot_intake["schema"] == "external-trend-intelligence.pilot-contract-intake.v1"
    assert pilot_intake["status"] == "template_only_no_company_data"
    assert pilot_intake["pilot_count"] == 3
    assert all(row["required_registration"]["internal_dataset"] is None for row in pilot_intake["pilots"])
    assert all(row["prohibited_transitions"] and row["required_before_approved_test"] for row in pilot_intake["pilots"])
    assert ownership["role_count"] == len(ownership["roles"]) == 6
    assert ownership["unassigned_role_count"] + ownership["assigned_role_count"] == ownership["role_count"]
    assert ownership["status"] in {"assignment_required", "assigned_pending_successor_signoff"}
    assert all(item["acceptance_criteria"] and item["handoff_checkpoint"] for item in ownership["roles"])
    ownership_readiness = json.loads((ANALYSIS / "operating-ownership-readiness.json").read_text())
    assert ownership_readiness["schema"] == "external-trend-intelligence.operating-ownership-readiness.v1"
    assert ownership_readiness["role_count"] == ownership["role_count"]
    assert ownership_readiness["assigned_role_count"] == ownership["assigned_role_count"]
    assert ownership_readiness["successor_run_status"] == "pass"
    assert ownership_readiness["status"] in {"ready_for_named_human_assignment", "handoff_incomplete"}
    assert ownership_readiness["boundary"] and ownership_readiness["next_action"]
    assert all(sample["claims"] for sample in ibis_sample["samples"])
    assert any(claim["sources"] for sample in ibis_sample["samples"] for claim in sample["claims"])
    assert ibis_sample["counter_signals"]
    assert ibis_sample["outcome_measure_candidate_count"] > 0
    assert all(sample["record_falsifiers"] for sample in ibis_sample["samples"])
    assert ibis_sample["sample_source_url_count"] == len(ibis_sample["sample_source_urls"]) >= 1
    assert ibis_sample["sample_source_host_count"] >= 1
    assert all(count > 1 for count in ibis_sample["duplicate_source_urls"].values())
    claim_review = ibis_sample["claim_review_summary"]
    assert claim_review["claim_count"] == sum(len(sample["claims"]) for sample in ibis_sample["samples"])
    assert claim_review["claim_count"] == len(claim_review["review_rows"])
    assert claim_review["source_identity_pass_count"] == claim_review["claim_count"]
    assert claim_review["independence_pending_count"] == claim_review["claim_count"]
    assert all("review" in claim for sample in ibis_sample["samples"] for claim in sample["claims"])
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
    assert release_manifest["artifact_count"] == len(release_manifest["artifacts"])
    assert re.fullmatch(r"[0-9a-f]{40}", release_manifest["source_tree_commit"])
    assert release_manifest["boundary"]
    assert any(item["path"] == ".github/workflows/external-observatory-refresh.yml" for item in release_manifest["artifacts"])
    manifest_paths = {item["path"] for item in release_manifest["artifacts"]}
    assert "analysis/external-trend-intelligence/TWO-YEAR-GOAL.md" in manifest_paths
    assert "analysis/external-trend-intelligence/EXTERNAL-DATA-SOURCES.md" in manifest_paths
    assert "analysis/external-trend-intelligence/observatory-chart-catalog.json" in manifest_paths
    acquired_sources = json.loads((ANALYSIS / "acquired-source-register.json").read_text())
    assert acquired_sources["schema"] == "external-trend-intelligence.acquired-source-register.v1"
    assert acquired_sources["status"] == "acquired_sources_registered_with_lineage_and_boundaries"
    assert acquired_sources["source_count"] == len(acquired_sources["sources"]) == 5
    required_acquired_fields = set(acquired_sources["required_fields"])
    for source in acquired_sources["sources"]:
        assert required_acquired_fields <= set(source)
        assert source["artifact"] and source["source_url"] and source["checksum"]
        assert source["rights_boundary"] and source["next_review"]
    release_watchlist = json.loads((ANALYSIS / "source-release-watchlist.json").read_text())
    assert release_watchlist["schema"] == "external-trend-intelligence.source-release-watchlist.v1"
    assert release_watchlist["source_count"] == len(release_watchlist["rows"]) == 5
    assert {row["source_id"] for row in release_watchlist["rows"]} == {source["source_id"] for source in acquired_sources["sources"]}
    for row in release_watchlist["rows"]:
        assert row["latest_observation_period"] and row["next_target_period"]
        assert row["cadence_or_trigger"] and row["acquisition_action"]
    assert release_watchlist["boundary"] and release_watchlist["next_action"]
    publication_registry = json.loads((ANALYSIS / "frontend-publication-registry.json").read_text())
    assert publication_registry["schema"] == "external-trend-intelligence.frontend-publication-registry.v1"
    assert publication_registry["status"] == "reader_publications_registered_with_boundaries"
    assert publication_registry["publication_count"] == len(publication_registry["publications"]) >= 5
    required_publication_fields = set(publication_registry["required_visible_fields"])
    assert required_publication_fields >= {"period", "unit", "geography", "scope_or_denominator", "uncertainty", "counter_signal", "evidence_boundary", "company_gate"}
    for publication in publication_registry["publications"]:
        assert required_publication_fields <= set(publication)
        assert publication["narrative_artifact"]
        assert publication["chart_artifacts"]
    for artifact in release_manifest["artifacts"]:
        path = ROOT / artifact["path"]
        assert path.exists(), artifact["path"]
        assert artifact["bytes"] == path.stat().st_size
    refresh_status = json.loads((ANALYSIS / "refresh-status.json").read_text())
    assert refresh_status["schema"] == "external-trend-intelligence.refresh-status.v1"
    assert refresh_status["stale_count"] == 0
    assert refresh_status["family_count"] == 8
    assert refresh_status["ready_for_review_count"] == 8
    freshness = json.loads((ANALYSIS / "refresh-freshness-decision.json").read_text())
    assert freshness["schema"] == "external-trend-intelligence.refresh-freshness-decision.v1"
    assert freshness["family_count"] == refresh_status["family_count"]
    assert freshness["fresh_ready_count"] + freshness["hold_count"] == freshness["family_count"]
    assert freshness["boundary"] and freshness["next_action"]
    rubric = json.loads((ANALYSIS / "trend-qualification-rubric.json").read_text())
    assert rubric["schema"] == "external-trend-intelligence.trend-qualification-rubric.v1"
    assert len(rubric["rules"]) == 8
    assert "qualified" in rubric["states"] and "reversed" in rubric["states"]
    contract_audit = json.loads((ANALYSIS / "evidence-contract-audit.json").read_text())
    assert contract_audit["schema"] == "external-trend-intelligence.evidence-contract-audit.v1"
    assert contract_audit["observation_count"] == 10
    assert contract_audit["contract_gap_count"] == 0
    qualification_matrix = json.loads((ANALYSIS / "candidate-qualification-matrix.json").read_text())
    assert qualification_matrix["schema"] == "external-trend-intelligence.candidate-qualification-matrix.v1"
    assert qualification_matrix["candidate_count"] == len(qualification_matrix["rows"]) == len(machine["candidates"])
    assert qualification_matrix["held_count"] == sum(row["gate_status"] == "held" for row in qualification_matrix["rows"])
    assert qualification_matrix["qualified_external_trend_count"] == sum(row["gate_status"] in {"qualified_external_trend", "monitored_external_trend"} for row in qualification_matrix["rows"])
    pilot_register = json.loads((ANALYSIS / "pilot-register.json").read_text())
    assert pilot_register["schema"] == "external-trend-intelligence.pilot-register.v1"
    assert len(pilot_register["pilots"]) >= 1
    assert all(pilot["status"] == "design_only_external_gate" for pilot in pilot_register["pilots"])
    assert all(pilot["company_ref"]["company_id"] is None for pilot in pilot_register["pilots"])
    assert any(pilot["candidate_id"] == "candidate-us-food-insecurity-persistence" for pilot in pilot_register["pilots"])
    pilot_readiness = json.loads((ANALYSIS / "pilot-readiness.json").read_text())
    assert pilot_readiness["schema"] == "external-trend-intelligence.pilot-readiness.v1"
    assert pilot_readiness["pilot_count"] == len(pilot_register["pilots"])
    assert pilot_readiness["ready_for_approved_test_count"] == 0
    assert all(item["readiness_status"] == "blocked_external_first" for item in pilot_readiness["pilots"])
    activation_queue = json.loads((ANALYSIS / "pilot-activation-queue.json").read_text())
    assert activation_queue["schema"] == "external-trend-intelligence.pilot-activation-queue.v1"
    assert activation_queue["pilot_count"] == len(activation_queue["rows"]) == pilot_readiness["pilot_count"]
    assert activation_queue["approved_test_count"] == 0
    assert activation_queue["company_data_accessed"] is False
    assert all(row["ordered_prerequisites"] and row["blocking_check_ids"] for row in activation_queue["rows"])
    assert activation_queue["boundary"] and activation_queue["next_action"]
    pilot_simulation = json.loads((ANALYSIS / "pilot-bridge-simulation.json").read_text())
    assert pilot_simulation["schema"] == "external-trend-intelligence.pilot-bridge-simulation.v1"
    assert pilot_simulation["status"] == "synthetic_contract_exercised_fail_closed"
    assert pilot_simulation["synthetic_only"] is True and pilot_simulation["company_data_accessed"] is False
    assert pilot_simulation["approved_test_count"] == 0
    assert all(pilot_simulation["required_visibility_checks"].values())
    monitoring = json.loads((ANALYSIS / "trend-monitoring-register.json").read_text())
    assert monitoring["schema"] == "external-trend-intelligence.trend-monitoring-register.v1"
    assert len(monitoring["trends"]) == qualification_matrix["candidate_count"]
    assert {item["candidate_id"] for item in monitoring["trends"]} == {row["candidate_id"] for row in qualification_matrix["rows"]}
    assert all(item["state"] in {"pre_qualification_watch", "qualified_monitor"} for item in monitoring["trends"])
    monitoring_evaluation = json.loads((ANALYSIS / "trend-monitoring-evaluation.json").read_text())
    assert monitoring_evaluation["schema"] == "external-trend-intelligence.trend-monitoring-evaluation.v1"
    assert monitoring_evaluation["evaluation_count"] == qualification_matrix["candidate_count"]
    assert monitoring_evaluation["reversal_trigger_count"] == monitoring_evaluation["retirement_trigger_count"] == 0
    assert all(row["evidence_basis"] and row["next_review"] and row["decision_boundary"] for row in monitoring_evaluation["rows"])
    controls = json.loads((ANALYSIS / "source-family-controls.json").read_text())
    assert controls["schema"] == "external-trend-intelligence.source-family-controls.v1"
    assert controls["family_count"] == 8
    assert all(item["rights_status"] and item["publisher_dependence"] for item in controls["families"])
    backtest_readiness = json.loads((ANALYSIS / "backtest-readiness.json").read_text())
    assert backtest_readiness["schema"] == "external-trend-intelligence.backtest-readiness.v1"
    assert backtest_readiness["candidate_count"] == len(backtest_readiness["rows"]) == qualification_matrix["candidate_count"]
    assert backtest_readiness["ready_for_design_review_count"] == sum(row["status"] == "records_available_comparability_review" for row in backtest_readiness["rows"])
    assert backtest_readiness["blocked_missing_local_record_count"] == 0
    backtest_request = (ANALYSIS / "BACKTEST-DESIGN-REVIEW-REQUEST.md").read_text()
    assert "Required review fields" in backtest_request
    for row in backtest_readiness["rows"]:
        assert f"`{row['candidate_id']}`" in backtest_request
    for field in ("construction period", "holdout period", "uncertainty", "falsifier", "second reviewer"):
        assert field in backtest_request.lower()
    snapshot = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())
    assert snapshot["schema"] == "external-trend-intelligence.backtest-source-snapshot.v1"
    assert snapshot["record_count"] == 31
    compatible = json.loads((ANALYSIS / "compatible-measure-search.json").read_text())
    assert compatible["schema"] == "external-trend-intelligence.compatible-measure-search.v1"
    assert compatible["record_count_in_manifest"] == manifest["record_count"]
    assert compatible["candidate_compatibility_group_count"] == len(compatible["rows"])
    assert compatible["status"] in {"no_cross_host_measure_pairs_found", "candidates_found_pending_review"}
    forecast = json.loads((ANALYSIS / "global-growth-forecast-comparison.json").read_text())
    assert forecast["schema"] == "external-trend-intelligence.global-growth-forecast-comparison.v1"
    assert forecast["status"] == "independent_forecast_comparison_pending_backtest"
    assert forecast["source_families"] == ["OECD", "UN DESA", "World Bank"]
    assert len(forecast["forecasts"]) == 3
    assert all(item["values"] and item["spread"] >= 0 for item in forecast["forecasts"])
    forecast_lineage = json.loads((ANALYSIS / "forecast-lineage-review.json").read_text())
    assert forecast_lineage["schema"] == "external-trend-intelligence.forecast-lineage-review.v1"
    assert forecast_lineage["record_count"] == len(forecast_lineage["rows"]) == 4
    assert forecast_lineage["source_host_count"] == 3
    assert forecast_lineage["shared_host_count"] == 1
    assert forecast_lineage["independence_checks"]["distinct_publisher_hosts"] is True
    assert forecast_lineage["status"] == "publisher_distinct_pending_vintage_rights_and_outcome_review"
    backtest_register = json.loads((ANALYSIS / "forecast-backtest-register.json").read_text())
    assert backtest_register["schema"] == "external-trend-intelligence.forecast-backtest-register.v1"
    assert backtest_register["row_count"] == len(backtest_register["rows"])
    assert backtest_register["pending_count"] == backtest_register["row_count"]
    assert all(row["status"] == "awaiting_realized_outcome" and row["observed_outcome"] is None for row in backtest_register["rows"])
    assert all(row["acceptance_criteria"] and row["refresh_trigger"] for row in backtest_register["rows"])
    roadmap = json.loads((ANALYSIS / "two-year-roadmap.json").read_text())
    assert roadmap["schema"] == "external-trend-intelligence.two-year-roadmap.v1"
    assert roadmap["horizon_months"] == 24
    assert roadmap["phase_count"] == len(roadmap["phases"]) == 5
    assert all(phase["acceptance_criteria"] and phase["evidence"] for phase in roadmap["phases"])
    assert roadmap["completion_rule"]
    ibis_dependency = json.loads((ANALYSIS / "ibis-claim-dependency-review.json").read_text())
    assert ibis_dependency["schema"] == "external-trend-intelligence.ibis-claim-dependency-review.v1"
    assert ibis_dependency["sample_industry_count"] == ibis_sample["sample_industry_count"]
    assert ibis_dependency["independence_status"] == "partial_dependency_review"
    assert ibis_dependency["shared_source_id_count"] >= 0
    ibis_outcome = json.loads((ANALYSIS / "ibis-adult-day-outcome-review.json").read_text())
    assert ibis_outcome["schema"] == "external-trend-intelligence.ibis-adult-day-outcome-review.v1"
    assert ibis_outcome["industry_slug"] == "adult-day-care"
    assert ibis_outcome["outcome_status"] == "dated_outcomes_and_independent_policy_measure_present"
    assert ibis_outcome["independence_status"] == "partial_cross_publisher_temporal_mechanism_comparison"
    outcome_plan = ibis_outcome["outcome_acquisition_plan"]
    assert outcome_plan["status"] == "targeted_public_source_identified_pending_extraction"
    assert len(outcome_plan["source_targets"]) == 3
    assert outcome_plan["required_fields"] and outcome_plan["acceptance_criteria"] and outcome_plan["stop_rule"]
    public_assessment = outcome_plan["public_evidence_assessment"]
    assert public_assessment["cdc_2025_weighted_estimates_pdf"]["public_national_estimates"] is True
    assert public_assessment["cdc_2025_weighted_estimates_pdf"]["standard_errors_published"] is True
    assert public_assessment["cdc_2025_weighted_estimates_pdf"]["state_level_fields_in_this_artifact"] is False
    npals = json.loads((ANALYSIS / "npals-public-table-extract.json").read_text())
    assert npals["schema"] == "external-trend-intelligence.npals-public-table-extract.v1"
    assert npals["numeric_row_count"] == len(npals["rows"]) > 0
    assert npals["retrieval_status"] in {"fresh_api_extract", "stale_previous_extract_source_unavailable"}
    assert isinstance(npals["source_available"], bool)
    assert npals["state_2020_frame_geography_count"] >= 50
    assert npals["reconciliation"]["status"] == "definition_reconciliation_required"
    assert npals["reconciliation"]["comparisons"][1]["comparison_status"] == "not_comparable_without_definition_review"
    assert ibis_outcome["rights_review"]["release_decision"] == "normalized_values_and_citations_only"
    schedule_health = json.loads((ANALYSIS / "refresh-schedule-health.json").read_text())
    assert schedule_health["schema"] == "external-trend-intelligence.refresh-schedule-health.v1"
    assert schedule_health["status"] == "configured"
    assert schedule_health["registered_family_count"] == 8
    comparability = json.loads((ANALYSIS / "backtest-comparability-review.json").read_text())
    assert comparability["schema"] == "external-trend-intelligence.backtest-comparability-review.v1"
    assert comparability["candidate_count"] == len(comparability["rows"]) == qualification_matrix["candidate_count"]
    assert comparability["comparable_subset_candidate_count"] == 0
    bounded = json.loads((ANALYSIS / "bounded-subset-register.json").read_text())
    assert bounded["schema"] == "external-trend-intelligence.bounded-subset-register.v1"
    assert bounded["subsets"][0]["status"] == "bounded_panel_not_backtest"
    assert len(bounded["subsets"][0]["record_ids"]) == 3
    assert bounded["subsets"][1]["status"] == "independence_review_candidate"
    assert bounded["subsets"][1]["publisher_families"] == ["Fair Work Commission", "Fair Work Ombudsman"]
    assert len(bounded["subsets"][1]["record_ids"]) == 5
    stage_panel = json.loads((ANALYSIS / "case-stage-panel.json").read_text())
    assert stage_panel["schema"] == "external-trend-intelligence.case-stage-panel.v1"
    assert stage_panel["case_count"] == 3
    assert stage_panel["status"] == "stage_coded_bounded_panel"
    cross_stage = json.loads((ANALYSIS / "cross-publisher-stage-panel.json").read_text())
    assert cross_stage["schema"] == "external-trend-intelligence.cross-publisher-stage-panel.v1"
    assert cross_stage["case_count"] == 5
    assert cross_stage["status"] == "stage_coded_cross_publisher_panel"
    assert cross_stage["publisher_families"] == ["Fair Work Commission", "Fair Work Ombudsman"]
    cross_comparison = json.loads((ANALYSIS / "cross-publisher-stage-comparison.json").read_text())
    assert cross_comparison["schema"] == "external-trend-intelligence.cross-publisher-stage-comparison.v1"
    assert cross_comparison["case_count"] == 5
    assert cross_comparison["status"] == "descriptive_stage_coverage_only"
    holdout = json.loads((ANALYSIS / "temporal-holdout-design.json").read_text())
    assert holdout["schema"] == "external-trend-intelligence.temporal-holdout-design.v1"
    assert holdout["status"] == "design_ready_single_family_holdout"
    assert holdout["construction_period"] == "2020"
    assert holdout["holdout_period"] == "2025"
    assert len(holdout["measures"]) == 3
    holdout_result = json.loads((ANALYSIS / "temporal-holdout-result.json").read_text())
    assert holdout_result["schema"] == "external-trend-intelligence.temporal-holdout-result.v1"
    assert holdout_result["status"] == "descriptive_holdout_readout_single_family"
    assert len(holdout_result["result"]) == 3
    assert "counter-signal" in holdout_result["result"][2]["interpretation"]
    narrative = json.loads((ANALYSIS / "temporal-decision-narrative.json").read_text())
    assert narrative["schema"] == "external-trend-intelligence.temporal-decision-narrative.v1"
    assert narrative["status"] == "bounded_external_narrative"
    assert len(narrative["what_the_evidence_shows"]) == 3
    release_health = json.loads((ANALYSIS / "release-health.json").read_text())
    assert release_health["schema"] == "external-trend-intelligence.release-health.v1"
    assert release_health["release_status"] == "operational_with_open_gates"
    assert len(release_health["blockers"]) == 6
    assert release_health["sections"]["monitoring"]["registered"] == len(monitoring["trends"])
    assert release_health["sections"]["monitoring"]["status"] == "pass"
    qualification_health = release_health["sections"]["trend_qualification"]
    assert qualification_health["candidates"] == qualification_matrix["candidate_count"]
    assert qualification_health["qualified"] == qualification_matrix["qualified_external_trend_count"]
    assert qualification_health["monitored"] == sum(row["gate_status"] == "monitored_external_trend" for row in qualification_matrix["rows"])
    assert qualification_health["held"] == qualification_matrix["held_count"]
    pilot_health = release_health["sections"]["company_pilots"]
    assert pilot_health["registered"] == len(pilot_register["pilots"])
    assert pilot_health["approved_tests"] == pilot_readiness["ready_for_approved_test_count"]
    assert release_health["sections"]["rights_and_publisher_dependence"]["rights_unverified"] == 8
    assert release_health["sections"]["rights_and_publisher_dependence"]["local_evidence_families"] >= 1
    assert release_health["sections"]["temporal_holdout"]["status"] == "design_readout_only"
    assert release_health["sections"]["ibis_adult_day_outcome"]["status"] == "bounded_cross_publisher_mechanism_comparison"
    assert release_health["sections"]["ibis_adult_day_outcome"]["rights_decision"] == "normalized_values_and_citations_only"
    assert release_health["sections"]["independent_source_comparison"]["directional_agreement_status"] == "directional_agreement_mechanism_only"
    assert release_health["sections"]["denominator_reconciliation"]["pooling_decision"] == "do_not_pool"
    assert release_health["sections"]["denominator_reconciliation"]["status"] == "hold"
    assert release_health["sections"]["independent_source_comparison"]["comparison_status"] == "mechanism_comparison_only"
    assert release_health["sections"]["independent_source_comparison"]["mechanism_comparison_source_family_count"] == 3
    assert "JPMorganChase Institute household liquidity study" in release_health["sections"]["independent_source_comparison"]["mechanism_comparison_source_families"]
    bounded_lineage = json.loads((ANALYSIS / "bounded-subset-lineage-review.json").read_text())
    assert bounded_lineage["schema"] == "external-trend-intelligence.bounded-subset-lineage-review.v1"
    assert bounded_lineage["record_count"] == 5
    assert bounded_lineage["source_host_count"] == 2
    assert bounded_lineage["independence_status"] == "partial_independence_review"
    progress = json.loads((ANALYSIS / "program-progress.json").read_text())
    assert progress["schema"] == "external-trend-intelligence.program-progress.v1"
    assert progress["baseline"]["records"] == manifest["record_count"]
    assert progress["baseline"]["qualified_external_trends"] == qualification_matrix["qualified_external_trend_count"]
    assert progress["baseline"]["monitored_external_trends"] == qualification_matrix["monitored_external_trend_count"]
    assert progress["baseline"]["release_artifacts"] == release_manifest["artifact_count"]
    assert progress["baseline"]["refresh_runs_recorded"] == refresh_history["run_count"]
    assert progress["baseline"]["rights_reviews_required"] == controls["family_count"]
    assert progress["baseline"]["independent_comparison_status"] == "directional_agreement_mechanism_only"
    assert len(progress["phases"]) == 5
    goal_doc = (ROOT / "EXTERNAL_TREND_INTELLIGENCE_GOAL_V1.md").read_text()
    handoff_doc = (ANALYSIS / "ANALYST-OPERATING-MODEL.md").read_text()
    readme_doc = (ANALYSIS / "README.md").read_text()
    candidate_doc = (ANALYSIS / "CROSS-SOURCE-CANDIDATES.md").read_text()
    next_actions_doc = (ANALYSIS / "NEXT-ACTIONS.md").read_text()
    runbook_doc = (ANALYSIS / "REFRESH-RUNBOOK.md").read_text()
    expected_records = f"{manifest['record_count']:,}"
    expected_candidates = str(len(machine["candidates"]))
    assert f"`{expected_records}` source-backed observations" in goal_doc
    assert f"`{source_snapshot['source_count']}` candidate external sources" in goal_doc
    assert f"`{expected_candidates}` cross-source candidates" in goal_doc
    assert f"{expected_records} indexed records" in handoff_doc
    assert "cross-source candidates (" in handoff_doc
    assert f"{expected_records}-record observation manifest" in readme_doc
    assert "the five qualified candidates and two held candidates" in readme_doc
    assert f"**Source inventory:** {expected_records} records" in candidate_doc
    assert "all five candidate comparisons" in next_actions_doc
    assert f"{expected_records}-record local" in runbook_doc
    handoff = json.loads((ANALYSIS / "operating-handoff.json").read_text())
    assert handoff["schema"] == "external-trend-intelligence.operating-handoff.v1"
    assert len(handoff["roles"]) == 6
    assert handoff["exercised_controls"]["full_refresh"] is True
    assert handoff["exercised_controls"]["independent_successor_run"] is False
    scorecard = json.loads((ANALYSIS / "program-scorecard.json").read_text())
    assert scorecard["schema"] == "external-trend-intelligence.program-scorecard.v1"
    assert scorecard["metrics"]["records"] == manifest["record_count"]
    assert scorecard["metrics"]["source_families"] == refresh_status["family_count"]
    assert scorecard["metrics"]["latest_pipeline_steps"] == refresh_history["latest"]["pipeline_step_count"]
    assert scorecard["metrics"]["latest_pipeline_status"] == "passed"
    assert scorecard["metrics"]["scheduled_workflow_contract"] == "passed"
    assert scorecard["metrics"]["refresh_runs"] == refresh_history["run_count"]
    assert scorecard["metrics"]["latest_pipeline_steps"] == refresh_history["latest"]["pipeline_step_count"]
    assert scorecard["metrics"]["qualified_external_trends"] == qualification_matrix["qualified_external_trend_count"]
    assert scorecard["metrics"]["monitored_external_trends"] == qualification_matrix["monitored_external_trend_count"]
    assert scorecard["metrics"]["approved_company_pilots"] == 0
    assert len(scorecard["phases"]) == 5
    independent = json.loads((ANALYSIS / "independent-stage-comparison.json").read_text())
    assert independent["schema"] == "external-trend-intelligence.independent-stage-comparison.v1"
    assert independent["status"] == "mechanism_comparison_only"
    assert independent["record_count"] == 2
    rights_queue = json.loads((ANALYSIS / "rights-review-queue.json").read_text())
    assert rights_queue["schema"] == "external-trend-intelligence.rights-review-queue.v1"
    assert all(row["review_plan"]["first_artifact"] and row["review_plan"]["completion_evidence"] for row in rights_queue["rows"])
    rights_assignment = json.loads((ANALYSIS / "rights-assignment-queue.json").read_text())
    assert rights_assignment["schema"] == "external-trend-intelligence.rights-assignment-queue.v1"
    assert rights_assignment["family_count"] == len(rights_assignment["rows"]) == rights_queue["family_count"]
    assert rights_assignment["unassigned_family_count"] + rights_assignment["assigned_family_count"] == rights_assignment["family_count"]
    assert all(row["acceptance_criteria"] and row["checkpoint"] for row in rights_assignment["rows"])
    assert rights_queue["family_count"] == 8
    assert rights_queue["review_required_count"] == 8
    rights_evidence = json.loads((ANALYSIS / "rights-evidence-register.json").read_text())
    assert rights_evidence["schema"] == "external-trend-intelligence.rights-evidence-register.v1"
    assert rights_evidence["family_count"] == 8
    assert all(row["rights_status"] == "not_verified" for row in rights_evidence["rows"])
    rights_readiness = json.loads((ANALYSIS / "rights-review-readiness.json").read_text())
    assert rights_readiness["schema"] == "external-trend-intelligence.rights-review-readiness.v1"
    assert rights_readiness["family_count"] == rights_evidence["family_count"]
    assert rights_readiness["review_ready_family_count"] == 0
    assert rights_readiness["unassigned_owner_count"] == rights_assignment["unassigned_family_count"]
    assert rights_readiness["boundary"] and rights_readiness["next_action"]
    chart_catalog = json.loads((ANALYSIS / "observatory-chart-catalog.json").read_text())
    assert chart_catalog["schema"] == "external-trend-intelligence.observatory-chart-catalog.v1"
    assert chart_catalog["chart_count"] == len(chart_catalog["charts"]) >= 8
    assert all(row["theme"] and row["subtheme"] and row["concept"] for row in chart_catalog["charts"])
    assert all(row["source_artifacts"] and row["required_visible_fields"] for row in chart_catalog["charts"])
    assert chart_catalog["boundary"] and chart_catalog["next_action"]
    continuity_plan = json.loads((ANALYSIS / "continuity-coverage-plan.json").read_text())
    assert continuity_plan["schema"] == "external-trend-intelligence.continuity-coverage-plan.v1"
    assert continuity_plan["required_week_count"] == 104
    assert continuity_plan["observed_distinct_week_count"] == len(continuity_plan["observed_weeks"])
    assert continuity_plan["remaining_week_count"] == max(continuity_plan["required_week_count"] - continuity_plan["observed_distinct_week_count"], 0)
    assert continuity_plan["acceptance"] and continuity_plan["boundary"] and continuity_plan["next_action"]
    room_comparison = json.loads((ANALYSIS / "room-independent-comparison.json").read_text())
    assert room_comparison["schema"] == "external-trend-intelligence.room-independent-comparison.v1"
    assert room_comparison["status"] == "mechanism_comparison_only"
    assert room_comparison["source_families"] == ["Australian Bureau of Statistics General Social Survey", "HILDA via Australian Institute of Health and Welfare", "ANU COVID-19 Monitoring Survey / ANUPoll", "ANZ / Roy Morgan"]
    acquisition = json.loads((ANALYSIS / "evidence-acquisition-plan.json").read_text())
    assert acquisition["schema"] == "external-trend-intelligence.evidence-acquisition-plan.v1"
    shed = json.loads((ANALYSIS / "federal-reserve-shed-financial-room-2013-2025.json").read_text())
    assert shed["schema"] == "external-trend-intelligence.external-acquisition.v1"
    assert shed["status"] == "acquired_pending_normalization"
    assert len(shed["observations"]) == 13
    assert "method_change_notes" in shed
    shed_holdout = json.loads((ANALYSIS / "shed-temporal-holdout.json").read_text())
    assert shed_holdout["schema"] == "external-trend-intelligence.shed-temporal-holdout.v1"
    assert shed_holdout["status"] == "descriptive_single_family_holdout"
    assert shed_holdout["construction_period"] == "2013-2021"
    assert shed_holdout["holdout_period"] == "2022-2025"
    usda_holdout = json.loads((ANALYSIS / "usda-temporal-holdout.json").read_text())
    assert usda_holdout["schema"] == "external-trend-intelligence.usda-temporal-holdout.v1"
    assert usda_holdout["status"] == "descriptive_single_family_holdout"
    assert usda_holdout["construction_period"] == "2022-2023"
    assert usda_holdout["holdout_period"] == "2024"
    usda = json.loads((ANALYSIS / "../records/comparative-usda-food-security-2022-2024.json").resolve().read_text())
    assert usda["trend_id"] == "comparative-usda-food-security-2022-2024"
    us_comparison = json.loads((ANALYSIS / "us-financial-room-independent-comparison.json").read_text())
    assert us_comparison["schema"] == "external-trend-intelligence.us-financial-room-independent-comparison.v1"
    assert us_comparison["status"] == "mechanism_comparison_only"
    assert len(us_comparison["rows"]) == 5
    assert any(row["measure"] == "would_cover_400_dollar_emergency" for row in us_comparison["rows"])
    assert any(row["source"] == "JPMorganChase Institute" for row in us_comparison["rows"])
    financial_card = json.loads((ANALYSIS / "financial-room-decision-card.json").read_text())
    assert financial_card["schema"] == "external-trend-intelligence.financial-room-decision-card.v1"
    assert financial_card["status"] == "bounded_external_mechanism_context"
    assert financial_card["candidate_id"] == us_comparison["candidate_id"]
    assert financial_card["evidence"]["australia_directional_panel"] and financial_card["evidence"]["us_cross_source_comparison"]
    assert financial_card["rights"]["source_count"] >= 7
    assert financial_card["company_gate"] and financial_card["boundary"]
    acquisition_rights = json.loads((ANALYSIS / "external-acquisition-rights-review.json").read_text())
    assert acquisition_rights["schema"] == "external-trend-intelligence.external-acquisition-rights-review.v1"
    assert len(acquisition_rights["rows"]) == 7
    assert all(row["rights_evidence_status"] in {"official_policy_identified_exact_artifact_review_open", "restrictive_republication_notice_review_open", "license_identified_exact_archive_review_open", "official_terms_identified_exact_artifact_review_open"} for row in acquisition_rights["rows"])
    ora_rights = next(row for row in acquisition_rights["rows"] if row["acquisition_id"] == "ora-ords-v03-mobile-aggregate-202607")
    assert ora_rights["publisher"] == "Open Repair Alliance"
    assert "CC BY-SA" in ora_rights["official_policy_observation"]
    assert ora_rights["source_url"].endswith("OpenRepairData_v0.3_aggregate_202607.zip")
    census_rights = {
        row["acquisition_id"]: row
        for row in acquisition_rights["rows"]
        if row["acquisition_id"] in {"census-cbp-electronic-repair-2019-2023", "census-nes-electronic-repair-2019-2024"}
    }
    assert set(census_rights) == {"census-cbp-electronic-repair-2019-2023", "census-nes-electronic-repair-2019-2024"}
    assert all(
        "https://www.census.gov/data/developers/about/terms-of-service.html" in row["terms_evidence_urls"]
        and "https://www.census.gov/about/policies/citation.html" in row["terms_evidence_urls"]
        and row["rights_evidence_status"] == "official_terms_identified_exact_artifact_review_open"
        and "exact" in row["next_action"]
        for row in census_rights.values()
    )
    financial_rights = json.loads((ANALYSIS / "financial-room-rights-review.json").read_text())
    assert financial_rights["schema"] == "external-trend-intelligence.financial-room-rights-review.v1"
    assert financial_rights["candidate_id"] == "candidate-time-financial-pressure-practical-room"
    assert financial_rights["source_count"] == len(financial_rights["rows"]) >= 7
    assert all(row["publisher"] and row["terms_urls"] and row["rights_status"] and row["next_action"] for row in financial_rights["rows"])
    assert "do_not_redistribute" in financial_rights["release_decision"]
    brief = json.loads((ANALYSIS / "food-security-decision-brief.json").read_text())
    assert brief["schema"] == "external-trend-intelligence.food-security-decision-brief.v1"
    assert brief["candidate_id"] == "candidate-us-food-insecurity-persistence"
    assert brief["qualification_state"] == "monitored_external_trend"
    assert brief["evidence"]["primary_holdout"] == "food-insecurity-temporal-holdout.json"
    assert brief["uncertainty"] and brief["falsifier"] and brief["company_gate"]
    assert brief["source_reported_significance"]["reference_estimate"].startswith("December 2025")
    assert "reconstructed intervals" in brief["source_reported_significance"]["interpretation_boundary"]
    assert "not" in brief["boundary"]
    food_tracker = json.loads((ANALYSIS / "food-security-release-tracker.json").read_text())
    assert food_tracker["schema"] == "external-trend-intelligence.food-security-release-tracker.v1"
    assert food_tracker["candidate_id"] == brief["candidate_id"]
    assert len(food_tracker["source_records"]) == 2
    assert {row["publisher"] for row in food_tracker["source_records"]} == {"USDA Economic Research Service", "Urban Institute"}
    assert all(row["latest_observation_period"] and row["next_target_status"] and row["release_action"] for row in food_tracker["source_records"])
    assert food_tracker["monitoring_decision"] == "continue_monitored_external_trend"
    assert food_tracker["comparability_boundary"] and food_tracker["rights_boundary"] and food_tracker["next_review"]
    food_comparison = json.loads((ANALYSIS / "food-insecurity-independent-comparison.json").read_text())
    assert food_comparison["schema"] == "external-trend-intelligence.food-insecurity-independent-comparison.v1"
    assert food_comparison["status"] == "independent_directional_challenge_not_comparable"
    assert food_comparison["independence_review"]["publisher_distinct"] is True
    assert food_comparison["pooling_decision"] == "do_not_pool"
    assert len(food_comparison["overlap_rows"]) == 3
    assert food_comparison["source_families"][0]["measure"].endswith("prior 12 months using the six-item USDA short form")
    assert food_comparison["urban_methodology_review"]["reference_period_confirmed"] == "12 months"
    assert food_comparison["urban_methodology_review"]["sample_change"]
    assert food_comparison["urban_methodology_review"]["uncertainty_status"]
    urban_sig = food_comparison["urban_methodology_review"]["source_reported_significance"]
    assert urban_sig["reference_estimate"] == "December 2025 working-age-adult estimate (27.7 percent)"
    assert "reconstructed intervals" in urban_sig["interpretation_boundary"]
    directional_sig = food_comparison["directional_readout"]["urban_source_reported_significance"]
    assert directional_sig["statistically_unchanged_from"] == [2023, 2024]
    assert directional_sig["significantly_higher_than"] == [2019, 2020, 2021, 2022]
    food_holdout = json.loads((ANALYSIS / "food-insecurity-temporal-holdout.json").read_text())
    assert food_holdout["readout"]["source_reported_significance"]["statistically_unchanged_from"] == [2023, 2024]
    food_rights = json.loads((ANALYSIS / "food-insecurity-rights-review.json").read_text())
    assert food_rights["alternate_data_access_path"]["catalog_license_label"] == "odc-by"
    assert food_rights["alternate_data_access_path"]["catalog_url"]
    assert food_rights["alternate_data_access_path"]["rights_interpretation"]
    mobility_comparison = json.loads((ANALYSIS / "mobility-access-independent-comparison.json").read_text())
    assert mobility_comparison["schema"] == "external-trend-intelligence.mobility-access-independent-comparison.v1"
    assert mobility_comparison["status"] == "directional_gradient_agreement_not_common_holdout"
    assert mobility_comparison["independence_review"]["publisher_distinct"] is True
    assert mobility_comparison["pooling_decision"] == "do_not_pool"
    assert len(mobility_comparison["source_families"]) == 2
    mobility_rights = json.loads((ANALYSIS / "mobility-access-rights-review.json").read_text())
    assert mobility_rights["schema"] == "external-trend-intelligence.mobility-access-rights-review.v1"
    assert mobility_rights["source_count"] == 2
    assert all(row["rights_status"] and row["terms_urls"] and row["next_action"] for row in mobility_rights["rows"])
    assert "do_not_redistribute" in mobility_rights["release_decision"]
    mobility_holdout = json.loads((ANALYSIS / "mobility-access-temporal-holdout.json").read_text())
    assert mobility_holdout["schema"] == "external-trend-intelligence.mobility-access-temporal-holdout.v1"
    assert mobility_holdout["status"] == "descriptive_single_family_holdout"
    assert len(mobility_holdout["measures"]) == 2
    assert mobility_holdout["uncertainty"] and mobility_holdout["falsifier"]
    forecast_plan = json.loads((ANALYSIS / "forecast-outcome-acquisition-plan.json").read_text())
    assert forecast_plan["schema"] == "external-trend-intelligence.forecast-outcome-acquisition-plan.v1"
    assert forecast_plan["status"] == "protocol_ready_outcomes_pending"
    assert len(forecast_plan["tracks"]) == 3
    assert all(track["official_source_url"] and track["earliest_acceptable_release"] for track in forecast_plan["tracks"])
    assert forecast_plan["stop_rules"]
    forecast_eligibility = json.loads((ANALYSIS / "forecast-outcome-eligibility.json").read_text())
    assert forecast_eligibility["schema"] == "external-trend-intelligence.forecast-outcome-eligibility.v1"
    assert forecast_eligibility["row_count"] == backtest_register["row_count"]
    assert forecast_eligibility["not_yet_eligible_count"] + forecast_eligibility["eligible_outcome_missing_count"] + forecast_eligibility["outcome_present_count"] == forecast_eligibility["row_count"]
    assert forecast_eligibility["boundary"] and forecast_eligibility["next_action"]
    assert len(acquisition["tracks"]) == 4
    assert all(track["stop_rule"] for track in acquisition["tracks"])
    track_by_id = {track["track_id"]: track for track in acquisition["tracks"]}
    assert track_by_id["time-pressure-independent-holdout"]["status"] == "partial_bridge_found"
    assert track_by_id["us-shed-financial-room-acquisition"]["status"] == "acquired_pending_normalization"
    completion_audit = json.loads((ANALYSIS / "goal-completion-audit.json").read_text())
    assert completion_audit["schema"] == "external-trend-intelligence.goal-completion-audit.v1"
    assert completion_audit["overall_status"] == "in_progress_with_open_gates"
    assert len(completion_audit["requirements"]) == 8
    assert any(item["status"] == "open" for item in completion_audit["requirements"])
    room_result = json.loads((ANALYSIS / "room-independent-result.json").read_text())
    assert room_result["schema"] == "external-trend-intelligence.room-independent-result.v1"
    assert room_result["status"] == "directional_cross_source_agreement_with_2025_adult_endpoint"
    assert len(room_result["rows"]) == 5
    denominator = json.loads((ANALYSIS / "denominator-reconciliation-review.json").read_text())
    assert denominator["schema"] == "external-trend-intelligence.denominator-reconciliation-review.v1"
    assert denominator["status"] == "reconciliation_required"
    assert denominator["common_pooling_decision"] == "do_not_pool"
    assert len(denominator["rows"]) == 4
    uncertainty_audit = json.loads((ANALYSIS / "uncertainty-coverage-audit.json").read_text())
    assert uncertainty_audit["schema"] == "external-trend-intelligence.uncertainty-coverage-audit.v1"
    assert uncertainty_audit["status"] == "uncertainty_visible_with_open_gates"
    assert uncertainty_audit["artifact_count"] == 6
    assert uncertainty_audit["incomplete_or_pending_count"] > 0
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
        "candidate-us-food-insecurity-persistence",
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
