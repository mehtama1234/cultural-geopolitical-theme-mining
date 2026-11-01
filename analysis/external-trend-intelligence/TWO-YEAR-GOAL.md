# Two-year external-first enterprise trend-intelligence observatory

## The goal in plain language

Build a trusted observatory that helps companies see meaningful external change
before making an internal decision about it. The observatory continuously
captures cultural, social, geopolitical, financial, industry, workforce,
technology, infrastructure, and market evidence; tests whether apparent trends
are real and recurring; publishes charts and narratives with their limits; and
only then asks whether a bounded company decision test is appropriate.

The system must be useful without company data. Internal data is a second-stage
test, never the source of the external trend and never an automatic join.

## What the observatory must preserve

Every observation and publication keeps:

- source identity, exact locator, retrieval hash, and revision;
- publisher and upstream-dataset dependence;
- unit, denominator, population, geography, and reference period;
- uncertainty, missingness, counter-signals, and methodology breaks;
- rights, retention, attribution, and redistribution boundaries; and
- the evidence boundary: descriptive, comparative, qualified, held, or
  company-test design only.

## External source families

The first intake spans eight pinned families:

1. cultural-geopolitical-theme-mining — cultural, social, institutional,
   consumer, place, and geopolitical records;
2. social-research — bounded public discussion and creator signals;
3. trend-hunting — public-signal and counter-signal synthesis;
4. annual-report-research — public-company filings and operating claims;
5. inc5000-analysis — private-company growth and bottom-up market signals;
6. ibis-industries — industry structure, forces, capacity, and dependencies;
7. research-signals — provenance, normalization, deduplication, and custody;
8. organization-intelligence-system — shared identity, comparability, rights,
   review, and release contracts.

These families are discovery and evidence layers, not automatic corroboration.
Shared publishers, hosts, datasets, or summaries are counted once until a
lineage reviewer records a different disposition.

## Concrete external datasets already in use

The current release is not built from one giant pooled dataset. It combines
named, source-specific products such as:

- USDA ERS food-security household series and Urban Institute WBNS food-security
  releases, including the December 2025 monitoring vintage;
- Federal Reserve SHED emergency-expense measures and JPMorganChase household
  liquidity chart evidence;
- ABS, HILDA/AIHW, ANUPoll, and Roy Morgan financial-pressure, time-use, and
  care measures;
- CDC capacity observations, CMS Medicaid-rate evidence, and BLS labor-capacity
  comparisons in the adult-day-care and workforce lanes;
- ACS and NHTS mobility-access measures;
- Census CBP and Nonemployer Statistics repair-industry proxies;
- NPALS public tables and Open Repair Alliance mobile-repair event records;
- OECD, UN DESA, World Bank, IRENA, PJM, undersea-cable, and regional
  infrastructure/geopolitical records; and
- IBIS industry reports, annual-report citations, Inc. 5000 company signals,
  social-publication evidence, and trend-hunting synthesis inputs.

The detailed source map is [EXTERNAL-DATA-SOURCES.md](EXTERNAL-DATA-SOURCES.md).
Each item remains source-specific for population, geography, period, unit,
uncertainty, rights, and publisher dependence.

## Reader-facing chart themes

Frontend pages use the chart catalog to keep the visual language consistent:

- observatory health: domain coverage, source freshness, and continuity;
- trend qualification: qualified, monitored, and held candidates;
- social and economic pressure: food insecurity and financial room;
- infrastructure and access: mobility constraints and repair outcomes;
- financial and market: forecast vintages and publisher spread;
- governance and rights: rights-review readiness and dependence; and
- operating model: open-gate workload and pilot activation.

Each chart must show its period, unit, geography, denominator or scope,
uncertainty, counter-signal, evidence boundary, and company-data boundary.

## 24-month delivery phases

### Months 0–3: control plane

Establish the source registry, observation and trend schemas, rights queue,
lineage controls, release manifest, external-only boundary, and fail-closed
bridge. Acceptance means the system can explain where every value came from and
why unresolved evidence remains unresolved.

### Months 4–6: dependable intake

Run the weekly refresh workflow, preserve revisions and hashes, detect stale or
missing families, retain recovery evidence, and measure distinct weekly
coverage. The two-year continuity requirement is 104 passed weekly windows;
short bursts do not count as continuity.

### Months 7–12: trend qualification

Compare independent source families without double-counting. Require
comparability, independence, persistence, uncertainty, counter-signal,
falsifier, backtest, and decision relevance before promotion. Keep held,
monitored, reversed, and retired states visible.

### Months 13–18: decision relevance

For a qualified or monitored external trend, define a bounded company decision
question. Specify aggregate or approved identifier basis, period, geography,
outcome, denominator, unmatched cases, privacy, rights, falsifier, and stop
rule. No company data is connected until every approval gate passes.

### Months 19–24: operationalize and hand off

Measure refresh reliability, review time, promotion and reversal rates, chart
usefulness, and pilot usefulness. Assign named primary and backup owners,
complete an independently signed successor run, and preserve the audit trail.

## Current evidence and open gates

The current release has 2,135 indexed records, 14 themes, eight source
families, nine required domains, one monitored external trend, four held
candidates, nine open gates, and zero approved company pilots. The pipeline,
board, chart catalog, continuity plan, and synthetic bridge simulation pass
their automated checks.

The following are intentionally still open: exact upstream rights and
publisher-dependence decisions, named human owners, independent candidate
adjudication, 104-week continuity, additional comparable holdouts, and real
company decision contracts with privacy and lawful-access approval.

## Authoritative artifacts

- `two-year-roadmap.json` — phase windows and acceptance criteria;
- `goal-completion-audit.json` — requirement-level completion status;
- `source-family-registry.json` and `source-registry-snapshot.json` — intake;
- `EXTERNAL-DATA-SOURCES.md` — concrete named external datasets and boundaries;
- `observation-manifest.json` and `evidence-contract-audit.json` — evidence;
- `candidate-qualification-matrix.json` and `falsification-review-queue.json`;
- `observatory-chart-catalog.json` and `frontend-publication-registry.json`;
- `continuity-coverage-plan.json` and `refresh-continuity-audit.json`;
- `pilot-activation-queue.json` and `pilot-bridge-simulation.json`; and
- `ANALYST-OPERATING-MODEL.md` and `REFRESH-RUNBOOK.md` — operating workflow.

This document describes the goal and operating contract. The JSON artifacts,
source records, validators, and release manifest remain the source of truth for
current values and gate status.
