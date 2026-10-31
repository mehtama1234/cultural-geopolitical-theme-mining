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
    ibis_findings_path = "cross_industry_findings_register.json"
    ibis_findings = json.loads(show(IBIS_REPO, IBIS_REV, ibis_findings_path))
    ibis_forces_path = "cross_industry_trends_2025_2026.json"
    ibis_forces = json.loads(show(IBIS_REPO, IBIS_REV, ibis_forces_path))
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
                source_url_status="not_present_in_artifact",
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
