# Frontend integration contract

The external observatory exposes JSON artifacts as the reader API. Frontend
pages may compose these artifacts, but must preserve their status and boundary
fields. Do not turn a held candidate into a positive signal by hiding its
blockers.

## Core page data

| UI section | Artifact | Required visible fields |
| --- | --- | --- |
| Inventory charts | `observation-manifest.json` | record count, theme, host, source unit, geography, boundary |
| Compatible-measure search | `compatible-measure-search.json` | scanned record count, candidate measure/unit groups, hosts, periods, review boundary |
| Global forecast comparison | `global-growth-forecast-comparison.json` | publisher, forecast period, value, spread, vintage/uncertainty boundary, backtest next action |
| Forecast lineage review | `forecast-lineage-review.json` | source host, publisher-distinct check, vintage/rights/uncertainty/outcome review status, boundary |
| Forecast backtest register | `forecast-backtest-register.json` | original forecast, realized-outcome slot, error field, refresh trigger, acceptance criteria, pending/completed status |
| 24-month roadmap | `two-year-roadmap.json` | phase window, current status, outcomes, acceptance criteria, evidence links, blocking requirement statuses |
| Source family cards | `source-family-registry.json`, `source-family-controls.json`, `refresh-status.json` | role, cadence, revision, rights status, publisher dependence, lineage status, file age |
| Candidate cards | `candidate-comparisons.json`, `candidate-qualification-matrix.json` | title, mechanism, counter-signal, evidence count, gate status, blocking gates, next action |
| Promotion queue | `promotion-queue.json` | current status, blocking gates, internal bridge readiness |
| Backtest view | `backtest-readiness.json`, `backtest-comparability-review.json` | record availability, periods, units, geographies, outcomes, harmonization blockers |
| Monitoring view | `trend-monitoring-register.json` | state, cadence, leading indicators, reversal conditions |
| Case panel | `case-stage-panel.json`, `bounded-subset-lineage-review.json` | stage status, not-observed distinction, hosts, shared-host overlap, independence status |
| IBIS bounded outcome panel | `ibis-adult-day-outcome-review.json` | dated measures, derived changes, uncertainty, cross-publisher status, counter-signal, next action, outcome acquisition plan and stop rule |
| NPALS public-table reconciliation | `npals-public-table-extract.json` | API query, retrieval/hash, 2020 state coverage, 2022/2025 national rows, definition mismatch and non-pooling boundary |
| IBIS claim review | `ibis-finding-claim-sample.json` | sampled claim count, source identity, URL/publisher/time metadata, outcome-linkage candidate, independence pending status |
| Independent comparison | `independent-stage-comparison.json`, `room-independent-comparison.json` | source families, mechanism status, blocking items, non-pooling boundary |
| Food-insecurity independent challenge | `food-insecurity-independent-comparison.json` | distinct publishers/hosts, overlapping periods, directional change, uncertainty, pooling decision, rights and comparability blockers |
| Temporal holdout and narrative | `temporal-holdout-design.json`, `temporal-holdout-result.json`, `temporal-decision-narrative.json` | construction/holdout periods, units, directional result, counter-signal, uncertainty, decision use |
| Rights evidence | `rights-review-queue.json`, `rights-assignment-queue.json`, `rights-evidence-register.json` | rights status, accountable review owner, local evidence files, hashes, publisher dependence, stop rule |
| Acquisition queue | `evidence-acquisition-plan.json` | target source, required fields, acceptance criteria, stop rule, owner |
| Program completion audit | `goal-completion-audit.json` | requirement status, evidence, gap, release status, next action |
| Pilot view | `pilot-register.json` | design status, external gate, company/data contract, privacy, falsifier |
| Release banner | `release-health.json`, `release-manifest.json` | release status, blockers, source commit, artifact count |

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
