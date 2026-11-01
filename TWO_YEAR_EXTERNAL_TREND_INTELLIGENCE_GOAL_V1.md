# Two-year external trend-intelligence observatory goal

## The goal in plain language

Build a durable company-facing observatory that turns external evidence into
decision-ready trend intelligence. The system will continuously collect and
refresh cultural, social, geopolitical, financial, industry, workforce,
technology, infrastructure, and market evidence; compare genuinely different
source families; test whether an apparent pattern is a recurring trend; and
publish charts, narratives, uncertainty, counter-signals, and falsifiers.

Only after a trend clears the external evidence gates will the team run a
bounded connection to internal company data. Internal data is a test of company
exposure or decision relevance, not a substitute for external evidence.

## What success looks like after 24 months

The organization has an operating capability, not a collection of one-off
reports:

- A maintained registry and refresh schedule for at least the current eight
  external source families, with source identity, rights, publisher lineage,
  units, geography, period, and freshness recorded.
- A versioned observation and trend schema that preserves claims, evidence
  links, uncertainty, counter-signals, falsifiers, and unresolved gaps.
- A repeatable qualification process that compares independent source families,
  separates shared publisher restatements from corroboration, and backtests
  whether a signal persists or fails.
- A frontend observatory that exposes source lineage, trend status, evidence
  quality, time and geography, and the difference between a candidate,
  qualified trend, and company decision test.
- A small portfolio of externally qualified trends and three to five bounded
  company decision pilots with explicit identifiers, periods, outcomes,
  unmatched cases, and stop rules. These pilots test usefulness; they do not
  claim that a trend caused a company result.
- A documented analyst workflow and release process that another analyst can
  run, audit, refresh, challenge, or hand off.

## 24-month sequence

### Months 0–3: establish the control plane

Lock the external-first boundary; finish the source-family registry; define the
observation, claim, trend, source-lineage, and internal-bridge schemas; record
rights and refresh expectations; and make validation and release manifests
routine. Resolve the current high-value provenance gaps, beginning with the
claim-level IBIS sample and the source-to-claim maps for annual reports, Inc.,
social research, and trend-hunting inputs.

### Months 4–6: make the external intake dependable

Automate or schedule refreshes for the source families, preserve immutable
revisions and checksums, and make stale or unavailable sources visible. Add
claim-level samples where an artifact is too large for full extraction. Every
published chart must have a source path, period, unit, denominator or scope,
and a clear boundary on what it does not establish.

### Months 7–12: qualify recurring trends

Run cross-source comparisons using mechanism, geography, period, and unit
compatibility. Require counter-signals and a falsifier. Backtest candidate
signals against later releases or held-out periods. Promote only findings that
survive lineage review and record why similar-looking evidence was not merged.

### Months 13–18: test decision relevance

Select a small set of qualified trends and design bounded internal bridges.
Each bridge names the company, business unit, geography, period, identifier
crosswalk, outcome, unmatched cases, privacy boundary, and stopping rule. Use
the results to improve prioritization and decision options, not to retrofit a
company story onto an unqualified external pattern.

### Months 19–24: operationalize and hand off

Measure refresh reliability, stale-source recovery, review time, promotion and
reversal rates, and pilot usefulness. Publish case studies showing what the
observatory changed, what it could not show, and where it was wrong. Establish
an ownership model, quarterly review, release checklist, and succession path
so the capability survives beyond the initial build.

## Core workstreams

1. **Source and rights control:** registry, access route, license/rights,
   publisher dependence, cadence, and revision history.
2. **Evidence model:** normalized observations, claims, units, periods,
   denominators, uncertainty, counter-signals, and falsifiers.
3. **Lineage and independence:** URL/host overlap, shared publisher detection,
   source-family comparison, and transparent confidence boundaries.
4. **Trend qualification:** candidate → held → qualified → monitored →
   reversed, with backtests and explicit promotion/reversal reasons.
5. **Frontend observatory:** charts and narratives that expose provenance and
   status instead of hiding caveats behind a single score.
6. **Analyst operating model:** refresh runbook, review queue, challenge
   process, release manifest, and reproducible handoff.
7. **Bounded company pilots:** carefully scoped internal joins only after an
   external trend clears the gates.

## Non-negotiable gates

No trend is promoted without identifiable source evidence, compatible unit,
geography, and period, a stated denominator or scope, a counter-signal, a
falsifier, uncertainty, and a lineage/independence review. No internal bridge
is run without a written bridge contract and unmatched-case accounting. A
shared URL or publisher is a dependency warning, not independent confirmation.
An attractive chart with missing provenance remains a candidate.

## Baseline at the start of this goal

The current external layer already provides 2,135 indexed records across 14
themes, eight source families, a source registry, refresh schedule, lineage
review, evidence-gap queue, candidate comparisons, claim-level IBIS sampling,
and a validated frontend release. The current boundary is intentionally strict:
there are no internal company joins in the external release, and the remaining
work is to deepen claim-level provenance, qualify recurring patterns, and then
run a few bounded decision tests.

## First 30 days

- Treat this document as the program charter and link it from the repository
  start page and release manifest.
- Complete the first claim-to-source maps for the 200-industry IBIS sample
  (with a 48-industry non-matching comparator set),
  annual-report themes, Inc. opportunities, and social atlas claims.
- Add a repeatable refresh/checksum run and an explicit stale-source report.
- Adopt a one-page qualification rubric covering source identity, comparability,
  independence, persistence, counter-signal, falsifier, and outcome relevance.
- Select one candidate trend for a design-only internal bridge; do not join data
  until the external qualification gate is passed.

This is a two-year capability-building goal. The immediate deliverable is not
more charts; it is a trustworthy system that can say what is changing, how
strongly the evidence supports it, what would disprove it, and when it is safe
to ask whether a company is exposed.
