#!/usr/bin/env python3
"""Normalize a small, reproducible first intake from pinned external artifacts."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "external-family-observations.json"
INC_REPO = "/home/mehta/git-repo/inc5000-analysis"
INC_REV = "92fad318ff05efcc5707f997bb1b5b18f3bceab2"
ANNUAL_REPO = "/home/mehta/git-repo/organization-intelligence-system"
ANNUAL_REV = "5d4434b9ff46e8d28176624a7ec44dfddee8be4b"
IBIS_REPO = "/home/mehta/git-repo/ibis-industries"
IBIS_REV = "b895acd021fbe3dc1d610255952b1373748e3bc3"
SOCIAL_REPO = "/home/mehta/git-repo/social-research"
SOCIAL_REV = "c2ff3e3a49129117802425514660ce4b2cf67744"
TREND_REPO = "/home/mehta/git-repo/trend-hunting"
TREND_REV = "19d8b2443f26f52da2331736320dcb265a9de34f"


def show(repo: str, revision: str, path: str) -> str:
    return subprocess.check_output(["git", "-C", repo, "show", f"{revision}:{path}"], text=True)


def record(
    observation_id: str,
    family_id: str,
    source_path: str,
    source_revision: str,
    title: str,
    value,
    unit: str,
    evidence_status: str,
    boundary: str,
    **extra,
) -> dict:
    return {
        "observation_id": observation_id,
        "family_id": family_id,
        "source_path": source_path,
        "source_revision": source_revision,
        "title": title,
        "value": value,
        "unit": unit,
        "observation_period": "artifact release dated 2026-10-30 or pinned revision",
        "geography": "not specified in the artifact",
        "source_url_status": "not_present_in_artifact",
        "evidence_status": evidence_status,
        "boundary": boundary,
        **extra,
    }


def main() -> int:
    strategic_path = "data/processed/strategic_source_ledger.json"
    strategic = json.loads(show(INC_REPO, INC_REV, strategic_path))
    opportunities_path = "data/processed/opportunity_intelligence_manifest.json"
    opportunities = json.loads(show(INC_REPO, INC_REV, opportunities_path))
    rebuild_path = "data/processed/inc5000_rebuild_manifest_v1.json"
    rebuild = json.loads(show(INC_REPO, INC_REV, rebuild_path))
    ibis_manifest_path = "research_manifest.json"
    ibis_manifest = json.loads(show(IBIS_REPO, IBIS_REV, ibis_manifest_path))
    ibis_source_inventory_path = "source_inventory.json"
    ibis_source_inventory = json.loads(show(IBIS_REPO, IBIS_REV, ibis_source_inventory_path))
    ibis_findings_path = "cross_industry_findings_register.json"
    ibis_findings = json.loads(show(IBIS_REPO, IBIS_REV, ibis_findings_path))
    ibis_forces_path = "cross_industry_trends_2025_2026.json"
    ibis_forces = json.loads(show(IBIS_REPO, IBIS_REV, ibis_forces_path))
    social_path = "analysis/social/integrated-trend-atlas-report.json"
    social_report = json.loads(show(SOCIAL_REPO, SOCIAL_REV, social_path))
    social_collection_path = "analysis/social/multi-platform-collection-manifest.json"
    social_collection = json.loads(show(SOCIAL_REPO, SOCIAL_REV, social_collection_path))
    trend_path = "data/processed/ai_v7_deep_trend_synthesis_v1.json"
    trend_report = json.loads(show(TREND_REPO, TREND_REV, trend_path))
    theme_path = "annual-report-research/analysis/company-first-principles/annual-report-final-integrated-theme-map-pass-1.md"
    theme_map = show(ANNUAL_REPO, ANNUAL_REV, theme_path)
    theme_rows = re.findall(r"\| (Core|Expansion) \| ([^|]+) \|", theme_map)
    folder_match = re.search(r"`(\d+)` company folder", theme_map)

    observations = []
    for trend in strategic["trends"]:
        source_urls = sorted(
            {
                url
                for example_group in ("high_growth_examples", "low_growth_counterexamples")
                for example in trend.get(example_group, [])
                for url in example.get("source_urls", [])
            }
        )
        observations.append(
            record(
                f"inc5000-{trend['trend_id']}-source-linked-share",
                "inc5000-analysis",
                strategic_path,
                INC_REV,
                trend["title"],
                trend["source_linked_share_pct"],
                "percent of candidate-flagged companies with source-linked records",
                "reported_candidate",
                "A source-linked share is a coverage measure inside the Inc. analysis; it is not market prevalence, demand, causality, or an outcome.",
                candidate_flagged_companies=trend["candidate_flagged_companies"],
                source_linked_companies=trend["source_linked_companies"],
                counter_signal_present=bool(trend.get("low_growth_counterexamples")),
                denominator="candidate_flagged_companies",
                source_urls=source_urls,
                source_url_status="present_in_artifact",
                source_url_count=len(source_urls),
                high_growth_example_count=len(trend.get("high_growth_examples", [])),
                low_growth_counterexample_count=len(trend.get("low_growth_counterexamples", [])),
                observation_period="Inc. 5000 2026 release; strategic ledger artifact generated 2026-10-30",
            )
        )
    observations.append(
        record(
            "inc5000-opportunity-intelligence-screen",
            "inc5000-analysis",
            opportunities_path,
            INC_REV,
            "Inc. 5000 opportunity screen",
            opportunities["counts"]["opportunities"],
            "screened opportunity hypotheses",
            "reported_queue",
            "The screen is a research queue. It does not prove market size, willingness to pay, or realized outcomes.",
            opportunity_titles=opportunities["opportunities"],
            field_evidence_submissions=opportunities["counts"]["field_evidence_submissions"],
            decisions=opportunities["decisions"],
            observation_period="Inc. 5000 opportunity-intelligence artifact; release generated 2026-10-30",
        )
    )
    observations.extend(
        [
            record(
                "ibis-industry-record-corpus",
                "ibis-industries",
                ibis_manifest_path,
                IBIS_REV,
                "IBIS industry evidence corpus",
                ibis_manifest["corpus"]["industry_record_count"],
                "industry records",
                "reported_provenance",
                "Corpus size describes the research inventory; it does not establish that every record is current, independent, or evidence for a trend.",
                data_window=ibis_manifest["corpus"]["current_data_window"],
                geography=ibis_manifest["geography"],
                source_url_status="inventory_present",
                source_inventory_path=ibis_source_inventory_path,
                source_inventory_count=ibis_source_inventory["metadata"]["source_count"],
                public_url_count=ibis_source_inventory["metadata"]["linked_source_count"],
                unlinked_source_count=ibis_source_inventory["metadata"]["unlinked_source_count"],
                unresolved_label_count=ibis_source_inventory["metadata"]["descriptive_label_resolution"]["unresolved"],
                observation_period=f"IBIS current data window {ibis_manifest['corpus']['current_data_window']}; research cutoff {ibis_manifest['research_cutoff']}",
            ),
            record(
                "ibis-cross-industry-discovery-findings",
                "ibis-industries",
                ibis_findings_path,
                IBIS_REV,
                "IBIS baseline cross-industry discovery findings",
                len(ibis_findings["findings"]),
                "discovery hypotheses",
                "reported_synthesis",
                "The findings are explicitly discovery hypotheses, not causal validation or proof of market outcomes.",
                finding_titles=[finding["title"] for finding in ibis_findings["findings"]],
                source_url_status="not_present_in_artifact",
                observation_period="IBIS baseline findings register at pinned revision; current data window 2025-2026",
            ),
            record(
                "ibis-cross-industry-business-forces",
                "ibis-industries",
                ibis_forces_path,
                IBIS_REV,
                "IBIS cross-industry business forces",
                len(ibis_forces["forces"]),
                "working hypotheses",
                "reported_synthesis",
                "Business-force chains connect external conditions to industry mechanisms but remain hypotheses until claim-level evidence and falsifiers are checked.",
                force_titles=[force["title"] for force in ibis_forces["forces"]],
                source_url_status="not_present_in_artifact",
                observation_period=ibis_forces.get("metadata", {}).get("as_of", "IBIS 2025-2026 working hypothesis register"),
            ),
        ]
    )
    observations.extend(
        [
            record(
                "social-integrated-trend-atlas",
                "social-research",
                social_path,
                SOCIAL_REV,
                social_report["title"],
                social_report["counts"]["themes"],
                "themes in integrated social atlas",
                "reported_synthesis",
                "The social atlas synthesizes public-signal and paid-research inputs; discussion and trend signals are not representative prevalence, causal effects, or market size.",
                cross_theme_findings=social_report["counts"]["cross_theme_findings"],
                subtheme_leads=social_report["counts"]["subtheme_leads"],
                proof_cards=social_report["counts"]["proof_cards"],
                paid_records=social_report["counts"]["paid_records"],
                headline=social_report["headline"],
                generated_at=social_report["generated_at"],
                method=social_report["method"],
                artifact_evidence_boundary=social_report["evidence_boundary"],
                collection_manifest_path=social_collection_path,
                collection_round_count=len(social_collection["rounds"]),
                collection_file_count=sum(round_data["files"] for round_data in social_collection["rounds"]),
                collection_failure_count=sum(round_data["failures"] for round_data in social_collection["rounds"]),
                collection_credits_charged=sum(round_data["credits_charged"] for round_data in social_collection["rounds"]),
                collection_platform_counts={
                    platform: sum(round_data.get("platforms", {}).get(platform, 0) for round_data in social_collection["rounds"])
                    for platform in sorted({platform for round_data in social_collection["rounds"] for platform in round_data.get("platforms", {})})
                },
                source_url_status="not_present_in_artifact",
                observation_period=f"Social atlas generated {social_report['generated_at']}",
            ),
            record(
                "trend-hunting-ai-deep-synthesis",
                "trend-hunting",
                trend_path,
                TREND_REV,
                "Trend-hunting AI deep-trend synthesis",
                len(trend_report["claims"]),
                "bounded synthesis claims",
                "reported_synthesis",
                "The synthesis traces a bounded AI control/recourse chain; it is not an adoption estimate or proof that formal control produced durable outcomes.",
                synthesis_status=trend_report["status"],
                falsifier_count=len(trend_report.get("falsifiers", [])),
                next_test=trend_report.get("next_test"),
                checked=trend_report["checked"],
                input_checksum_count=len(trend_report.get("input_checksums", {})),
                artifact_inputs=trend_report.get("inputs", []),
                source_url_status="not_present_in_artifact",
                observation_period=f"Trend-hunting synthesis checked {trend_report['checked']}",
            ),
        ]
    )
    observations.append(
        record(
            "inc5000-rebuild-public-input-inventory",
            "inc5000-analysis",
            rebuild_path,
            INC_REV,
            "Inc. 5000 reproducibility input inventory",
            len(rebuild["raw_inputs"]),
            "hashed raw input files",
            "reported_provenance",
            "Input hashes establish reproducibility lineage, not the truth of the underlying rankings or business claims.",
            release=rebuild["release"],
            generated_on=rebuild["generated_on"],
            observation_period=f"Inc. 5000 rebuild artifact generated {rebuild['generated_on']}",
        )
    )
    observations.append(
        record(
            "annual-report-integrated-theme-map",
            "annual-report-research",
            theme_path,
            ANNUAL_REV,
            "Annual-report integrated operating-pressure theme map",
            len(theme_rows),
            "named themes",
            "reported_synthesis",
            "This is an editorial synthesis over an annual-report archive; it does not prove every company, cash flow, causal mechanism, or investment result.",
            core_theme_count=sum(1 for layer, _ in theme_rows if layer == "Core"),
            expansion_theme_count=sum(1 for layer, _ in theme_rows if layer == "Expansion"),
            company_folder_reference=int(folder_match.group(1)) if folder_match else None,
            theme_names=[name.strip() for _, name in theme_rows],
            observation_period="Annual-report integrated theme map pass 1 at pinned revision",
        )
    )
    payload = {
        "schema": "external-trend-intelligence.external-family-observations.v1",
        "purpose": "First normalized observations from pinned external repository artifacts; these are not yet promoted cross-source trends.",
        "observation_count": len(observations),
        "observations": observations,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(observations)} observations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
