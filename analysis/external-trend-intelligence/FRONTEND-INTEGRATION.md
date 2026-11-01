# Frontend integration contract

The external observatory exposes JSON artifacts as the reader API. Frontend
pages may compose these artifacts, but must preserve their status and boundary
fields. Do not turn a held candidate into a positive signal by hiding its
blockers.

## Core page data

| UI section | Artifact | Required visible fields |
| --- | --- | --- |
| Inventory charts | `observation-manifest.json` | record count, theme, host, source unit, geography, boundary |
| Record quality audit | `record-quality-audit.json` | explicit coverage of lineage locator, period, unit, geography, uncertainty, counter-signal, boundary, and retrieval hash; missing metadata must remain visible |
| Record quality remediation | `record-quality-remediation-queue.json` | prioritized records missing counter-signals or retrieval hashes, acceptance criteria, and fail-closed boundary |
| Host dependence audit | `record-host-dependence-audit.json` | full-inventory shared-host counts, host/theme coverage, co-occurring host pairs, and independence boundary |
| Host dependence review queue | `host-dependence-review-queue.json` | prioritized shared-host lineage tasks, review questions, acceptance criteria, and unassigned status |
| Open-gate register | `open-gate-register.json` | consolidated rights, independence, qualification, backtest, pilot, ownership, and continuity work; the board renders each gate's open count, priority, owner, status, and acceptance criteria |
| Domain coverage audit | `domain-coverage-audit.json` | maps the required cultural, social, geopolitical, financial, industry, workforce, technology, infrastructure, and market domains to observed themes, records, hosts, and URLs; the board renders domain coverage without treating it as validity |
| Financial-room decision card | `financial-room-decision-card.json` | consolidates Australia/U.S. directional evidence, the JPMorgan chart endpoint, uncertainty, rights status, counter-signal, and the no-bridge company gate into one bounded mechanism-context card |
| Synthetic pilot bridge simulation | `pilot-bridge-simulation.json` | exercises aggregate matching, unmatched and missing-outcome visibility, falsifier, and stop-rule behavior without accessing company data or authorizing a test |
| Trend monitoring evaluation | `trend-monitoring-evaluation.json` | records current continue/hold decisions, reversal and retirement triggers, evidence basis, and next review for every watched candidate |
| Forecast outcome eligibility | `forecast-outcome-eligibility.json` | distinguishes forecast periods still open from eligible-but-missing realized outcomes so the board never scores a partial-year result as a backtest |
| Refresh freshness decisions | `refresh-freshness-decision.json` | converts artifact age, missing files, and incomplete states into explicit per-family ready/hold decisions and actions |
| Open-gate history | `open-gate-history.json` | preserves append-only gate workload snapshots so closure, reopening, and long-lived critical work can be monitored across refreshes |
| Compatible-measure search | `compatible-measure-search.json` | scanned record count, candidate measure/unit groups, hosts, periods, review boundary |
| Global forecast comparison | `global-growth-forecast-comparison.json` | publisher, forecast period, value, spread, vintage/uncertainty boundary, backtest next action |
| Forecast lineage review | `forecast-lineage-review.json` | source host, publisher-distinct check, vintage/rights/uncertainty/outcome review status, boundary |
| Forecast backtest register | `forecast-backtest-register.json` | original forecast, realized-outcome slot, error field, refresh trigger, acceptance criteria, pending/completed status |
| Forecast outcome acquisition | `forecast-outcome-acquisition-plan.json` | target period, official release family, vintage rule, uncertainty fields, acceptance criteria, and stop rules |
| 24-month roadmap | `two-year-roadmap.json` | phase window, current status, outcomes, acceptance criteria, evidence links, blocking requirement statuses |
| Source family cards | `source-family-registry.json`, `source-family-controls.json`, `refresh-status.json` | role, cadence, revision, rights status, publisher dependence, lineage status, file age |
| Acquired source register | `acquired-source-register.json` | acquired artifact, publisher, URL, revision, checksum, unit/population, geography/period, rights boundary, and next review |
| Candidate cards | `candidate-comparisons.json`, `candidate-qualification-matrix.json` | title, mechanism, counter-signal, evidence count, gate status, blocking gates, next action |
| Promotion queue | `promotion-queue.json` | current status, blocking gates, internal bridge readiness |
| Backtest view | `backtest-readiness.json`, `backtest-comparability-review.json` | record availability, periods, units, geographies, outcomes, harmonization blockers |
| Monitoring view | `trend-monitoring-register.json` | state, cadence, leading indicators, reversal conditions |
| Case panel | `case-stage-panel.json`, `bounded-subset-lineage-review.json` | stage status, not-observed distinction, hosts, shared-host overlap, independence status |
| IBIS bounded outcome panel | `ibis-adult-day-outcome-review.json` | dated measures, derived changes, uncertainty, cross-publisher status, counter-signal, next action, outcome acquisition plan and stop rule |
| NPALS public-table reconciliation | `npals-public-table-extract.json` | API query, retrieval/hash, 2020 state coverage, 2022/2025 national rows, definition mismatch and non-pooling boundary |
| IBIS claim review | `ibis-finding-claim-sample.json`, `ibis-claim-independence-audit.json`, `ibis-claim-independence-review-queue.json`, `ibis-first-review-batch.json`, `ibis-claim-review-dispositions.json` | sampled claim count, source identity, URL/publisher/time metadata, reused URL/host/publisher dependency flags, prioritized manual-review queue and first batch, conservative held dispositions, outcome-linkage candidate, independence pending status |
| Cell-phone repair outcome acquisition | `cell-phone-repair-outcome-acquisition-plan.json` | state-policy context, FTC mechanism context, ITU counter-signal, non-pooling reasons, target outcome measures, acceptance criteria, and stop rule |
| Census repair industry proxy | `census-repair-industry-snapshot.json` | 2019–2023 NAICS 811211/811213 national and state establishment/employment/payroll measures, download checksums, noise flags, proxy boundary, and non-pooling decision |
| Census nonemployer repair proxy | `census-nonemployer-repair-snapshot.json` | 2019–2024 NAICS 81121 national/state nonemployer establishments and receipts, download checksums, flags, broad-category caveat, and non-pooling decision |
| Census repair proxy comparison | `census-repair-proxy-comparison.json` | Aligned 2019–2023 CBP paid-employee and NES nonemployer repair measures, same-publisher warning, counter-signals, and explicit non-pooling decision |
| IBIS force review | `ibis-force-claim-map.json`, `ibis-force-claim-review.json` | force-level source and publisher counts, missing claim periods, outcome candidates, falsifiers, independence and promotion hold |
| Independent comparison | `independent-stage-comparison.json`, `room-independent-comparison.json` | source families, mechanism status, blocking items, non-pooling boundary |
| Food-insecurity independent challenge | `food-insecurity-independent-comparison.json` | distinct publishers/hosts, overlapping periods, directional change, uncertainty, pooling decision, rights and comparability blockers |
| Mobility independent challenge | `mobility-access-independent-comparison.json` | distinct datasets, income-gradient values, counter-signal, frame differences, pooling decision, and next holdout |
| Mobility rights review | `mobility-access-rights-review.json` | source URLs, terms routes, rights status, permitted scope, non-cleared reuse, and stop rule |
| Mobility temporal holdout | `mobility-access-temporal-holdout.json` | ACS construction/holdout periods, measures, uncertainty limitation, counter-signal, falsifier, and next test |
| Temporal holdout and narrative | `temporal-holdout-design.json`, `temporal-holdout-result.json`, `temporal-decision-narrative.json` | construction/holdout periods, units, directional result, counter-signal, uncertainty, decision use |
| Rights evidence | `rights-review-queue.json`, `rights-assignment-queue.json`, `rights-evidence-register.json` | rights status, accountable review owner, family-specific first artifact, rights/lineage questions, completion evidence, local files, hashes, publisher dependence, stop rule |
| Uncertainty coverage | `uncertainty-coverage-audit.json` | uncertainty state, evidence, release implication, and open acquisition action across decision-facing artifacts |
| Acquisition queue | `evidence-acquisition-plan.json` | target source, required fields, acceptance criteria, stop rule, owner |
| Program completion audit | `goal-completion-audit.json` | requirement status, evidence, gap, release status, next action |
| Pilot view | `pilot-register.json` | design status, external gate, company/data contract, privacy, falsifier |
| First pilot execution blueprint | `pilot-food-security-service-room-blueprint.json` | external qualification basis, permitted aggregate design, crosswalk boundary, blockers, falsifier, stop rule; never display it as an approved company test |
| Release banner | `release-health.json`, `release-manifest.json` | release status, blockers, source commit, artifact count |
| Publication registry | `frontend-publication-registry.json` | every reader-facing chart/narrative's period, unit, geography, denominator/scope, uncertainty, counter-signal, evidence boundary, and company gate |
| Ownership queue | `ownership-assignment-queue.json` | assigned/unassigned roles, assignment SLA, backup activation, escalation path, and acceptance evidence |

## Status semantics

- `candidate` or `qualified_candidate` means a hypothesis is being tested, not
  that it is a qualified trend.
- `held` means one or more required gates lack evidence.
- `not_observed_in_public_record` is not a zero and not evidence of absence.
- `review_required`, `not_yet_verified`, and `partial_independence_review`
  must remain visible wherever rights or lineage are shown.
- `design_only_external_gate` means no company data has been connected.
- `operational_with_open_gates` means the pipeline runs and validates while
  substantive evidence gates remain unresolved.

## Frontend boundary

The board is a reader, not the source of truth. Every displayed value must be
traceable to a release-manifest artifact, and every chart or narrative must
retain its period, unit, geography, denominator or scope, uncertainty,
counter-signal, and evidence boundary. Internal company exposure is not a
frontend join; it requires the separate bridge contract after qualification.

## Runtime check

Serve this directory over HTTP and run:

```text
python3 scripts/smoke_test_external_board.py
```
