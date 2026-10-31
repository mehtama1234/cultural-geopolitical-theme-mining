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
            assert observation["source_url_status"] == "bounded_sample_present"
            assert observation["traceability_sample_industry_count"] == 100
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
    assert ibis_sample["sample_industry_count"] == len(ibis_sample["samples"]) == 100
    assert ibis_sample["sample_sector_count"] >= 20
    ibis_review = json.loads((ANALYSIS / "ibis-claim-source-review.json").read_text())
    assert ibis_review["schema"] == "external-trend-intelligence.ibis-claim-source-review.v1"
    assert ibis_review["sample_industry_count"] == 100
    assert ibis_review["independence_status"] == "not_qualified"
    assert ibis_review["outcome_validation_status"] == "not_observed_in_traceability_sample"
    ibis_force_map = json.loads((ANALYSIS / "ibis-force-claim-map.json").read_text())
    assert ibis_force_map["schema"] == "external-trend-intelligence.ibis-force-claim-map.v1"
    assert ibis_force_map["force_count"] == len(ibis_force_map["forces"]) == 6
    assert ibis_force_map["aggregate"]["declared_source_id_count"] == 21
    assert ibis_force_map["aggregate"]["resolved_source_id_count"] == 21
    assert ibis_force_map["aggregate"]["unresolved_source_id_count"] == 0
    assert ibis_force_map["aggregate"]["claim_reference_count"] > 0
    assert all(force["falsifiers"] and force["outcome_measure_candidates"] for force in ibis_force_map["forces"])
    assert all(force["review_status"] == "held_claim_level_lineage_and_independence" for force in ibis_force_map["forces"])
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
    assert shed_emergency["boundary"] and shed_emergency["comparability_review"]["next_test"]
    uncertainty = json.loads((ANALYSIS / "shed-emergency-expense-uncertainty-audit.json").read_text())
    assert uncertainty["schema"] == "external-trend-intelligence.uncertainty-audit.v1"
    assert uncertainty["public_sample_size"] == 12295
    assert uncertainty["naive_srs_interval"]["status"] == "diagnostic_only_not_release_valid"
    assert uncertainty["design_based_status"] == "not_estimable_from_current_pinned_artifacts"
    assert uncertainty["release_decision"] == "hold"
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
    assert refresh_history["latest"]["record_count"] == 2134
    assert refresh_history["latest"]["parse_error_count"] == 0
    assert refresh_history["latest"]["pipeline_step_count"] == 52
    assert refresh_history["latest"]["pipeline_status"] == "passed"
    assert all(sample["claims"] for sample in ibis_sample["samples"])
    assert any(claim["sources"] for sample in ibis_sample["samples"] for claim in sample["claims"])
    assert ibis_sample["counter_signals"]
    assert ibis_sample["outcome_measure_candidate_count"] > 0
    assert all(sample["record_falsifiers"] for sample in ibis_sample["samples"])
    assert ibis_sample["sample_source_url_count"] == len(ibis_sample["sample_source_urls"]) >= 1
    assert ibis_sample["sample_source_host_count"] >= 1
    assert all(count > 1 for count in ibis_sample["duplicate_source_urls"].values())
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
    assert release_manifest["artifact_count"] == len(release_manifest["artifacts"]) == 75
    assert re.fullmatch(r"[0-9a-f]{40}", release_manifest["source_tree_commit"])
    assert release_manifest["boundary"]
    assert any(item["path"] == ".github/workflows/external-observatory-refresh.yml" for item in release_manifest["artifacts"])
    for artifact in release_manifest["artifacts"]:
        path = ROOT / artifact["path"]
        assert path.exists(), artifact["path"]
        assert artifact["bytes"] == path.stat().st_size
    refresh_status = json.loads((ANALYSIS / "refresh-status.json").read_text())
    assert refresh_status["schema"] == "external-trend-intelligence.refresh-status.v1"
    assert refresh_status["stale_count"] == 0
    assert refresh_status["family_count"] == 8
    assert refresh_status["ready_for_review_count"] == 8
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
    assert qualification_matrix["candidate_count"] == 4
    assert qualification_matrix["held_count"] == 4
    assert qualification_matrix["qualified_external_trend_count"] == 0
    pilot_register = json.loads((ANALYSIS / "pilot-register.json").read_text())
    assert pilot_register["schema"] == "external-trend-intelligence.pilot-register.v1"
    assert len(pilot_register["pilots"]) == 1
    pilot = pilot_register["pilots"][0]
    assert pilot["status"] == "design_only_external_gate"
    assert pilot["external_gate"]["current_status"] == "held"
    assert pilot["company_ref"]["company_id"] is None
    monitoring = json.loads((ANALYSIS / "trend-monitoring-register.json").read_text())
    assert monitoring["schema"] == "external-trend-intelligence.trend-monitoring-register.v1"
    assert len(monitoring["trends"]) == 4
    assert all(item["state"] == "pre_qualification_watch" for item in monitoring["trends"])
    controls = json.loads((ANALYSIS / "source-family-controls.json").read_text())
    assert controls["schema"] == "external-trend-intelligence.source-family-controls.v1"
    assert controls["family_count"] == 8
    assert all(item["rights_status"] and item["publisher_dependence"] for item in controls["families"])
    backtest_readiness = json.loads((ANALYSIS / "backtest-readiness.json").read_text())
    assert backtest_readiness["schema"] == "external-trend-intelligence.backtest-readiness.v1"
    assert backtest_readiness["candidate_count"] == 4
    assert backtest_readiness["ready_for_design_review_count"] == 4
    assert backtest_readiness["blocked_missing_local_record_count"] == 0
    snapshot = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())
    assert snapshot["schema"] == "external-trend-intelligence.backtest-source-snapshot.v1"
    assert snapshot["record_count"] == 28
    comparability = json.loads((ANALYSIS / "backtest-comparability-review.json").read_text())
    assert comparability["schema"] == "external-trend-intelligence.backtest-comparability-review.v1"
    assert comparability["candidate_count"] == 4
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
    assert release_health["sections"]["rights_and_publisher_dependence"]["rights_unverified"] == 8
    assert release_health["sections"]["rights_and_publisher_dependence"]["local_evidence_families"] >= 1
    assert release_health["sections"]["temporal_holdout"]["status"] == "design_readout_only"
    assert release_health["sections"]["independent_source_comparison"]["directional_agreement_status"] == "directional_agreement_mechanism_only"
    assert release_health["sections"]["denominator_reconciliation"]["pooling_decision"] == "do_not_pool"
    assert release_health["sections"]["denominator_reconciliation"]["status"] == "hold"
    assert release_health["sections"]["independent_source_comparison"]["comparison_status"] == "mechanism_comparison_only"
    bounded_lineage = json.loads((ANALYSIS / "bounded-subset-lineage-review.json").read_text())
    assert bounded_lineage["schema"] == "external-trend-intelligence.bounded-subset-lineage-review.v1"
    assert bounded_lineage["record_count"] == 5
    assert bounded_lineage["source_host_count"] == 2
    assert bounded_lineage["independence_status"] == "partial_independence_review"
    progress = json.loads((ANALYSIS / "program-progress.json").read_text())
    assert progress["schema"] == "external-trend-intelligence.program-progress.v1"
    assert progress["baseline"]["records"] == 2134
    assert progress["baseline"]["qualified_external_trends"] == 0
    assert progress["baseline"]["release_artifacts"] == 75
    assert progress["baseline"]["rights_reviews_required"] == 8
    assert progress["baseline"]["independent_comparison_status"] == "directional_agreement_mechanism_only"
    assert len(progress["phases"]) == 5
    handoff = json.loads((ANALYSIS / "operating-handoff.json").read_text())
    assert handoff["schema"] == "external-trend-intelligence.operating-handoff.v1"
    assert len(handoff["roles"]) == 6
    assert handoff["exercised_controls"]["full_refresh"] is True
    assert handoff["exercised_controls"]["independent_successor_run"] is False
    scorecard = json.loads((ANALYSIS / "program-scorecard.json").read_text())
    assert scorecard["schema"] == "external-trend-intelligence.program-scorecard.v1"
    assert scorecard["metrics"]["records"] == 2134
    assert scorecard["metrics"]["source_families"] == 8
    assert scorecard["metrics"]["latest_pipeline_steps"] == 52
    assert scorecard["metrics"]["latest_pipeline_status"] == "passed"
    assert scorecard["metrics"]["scheduled_workflow_contract"] == "passed"
    assert scorecard["metrics"]["refresh_runs"] == refresh_history["run_count"]
    assert scorecard["metrics"]["latest_pipeline_steps"] == refresh_history["latest"]["pipeline_step_count"]
    assert scorecard["metrics"]["qualified_external_trends"] == 0
    assert scorecard["metrics"]["approved_company_pilots"] == 0
    assert len(scorecard["phases"]) == 5
    independent = json.loads((ANALYSIS / "independent-stage-comparison.json").read_text())
    assert independent["schema"] == "external-trend-intelligence.independent-stage-comparison.v1"
    assert independent["status"] == "mechanism_comparison_only"
    assert independent["record_count"] == 2
    rights_queue = json.loads((ANALYSIS / "rights-review-queue.json").read_text())
    assert rights_queue["schema"] == "external-trend-intelligence.rights-review-queue.v1"
    assert rights_queue["family_count"] == 8
    assert rights_queue["review_required_count"] == 8
    rights_evidence = json.loads((ANALYSIS / "rights-evidence-register.json").read_text())
    assert rights_evidence["schema"] == "external-trend-intelligence.rights-evidence-register.v1"
    assert rights_evidence["family_count"] == 8
    assert all(row["rights_status"] == "not_verified" for row in rights_evidence["rows"])
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
    assert len(us_comparison["rows"]) == 3
    assert any(row["measure"] == "would_cover_400_dollar_emergency" for row in us_comparison["rows"])
    acquisition_rights = json.loads((ANALYSIS / "external-acquisition-rights-review.json").read_text())
    assert acquisition_rights["schema"] == "external-trend-intelligence.external-acquisition-rights-review.v1"
    assert len(acquisition_rights["rows"]) == 2
    assert all(row["rights_evidence_status"] == "official_policy_identified_exact_artifact_review_open" for row in acquisition_rights["rows"])
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
