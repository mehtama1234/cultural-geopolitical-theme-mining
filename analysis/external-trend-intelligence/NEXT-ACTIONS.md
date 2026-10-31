# External trend-intelligence next actions

This is the current handoff for the living external-first goal. All actions
below preserve the rule that external evidence is qualified before any company
data is joined.

## Current backtest gate

The historical records for all four candidates are now pinned in
[`backtest-source-snapshot.json`](backtest-source-snapshot.json), and the
bounded Australian platform-remedy panel is stage-coded in
[`case-stage-panel.json`](case-stage-panel.json). Structural review still finds
zero comparable backtest subsets: units, denominators, geographies, and outcome
definitions remain heterogeneous. The next test is to acquire an independent
source family using the same stage or outcome definitions, not to pool the
current records.
The bounded-subset register now includes a five-case cross-publisher review
candidate spanning Fair Work Commission and Fair Work Ombudsman records; it is
an independence-review panel, not a pooled estimate.

## One substantive open gate

**IBIS discovery findings — claim-level source mapping.** The pinned register
has five discovery findings, three pinned pattern artifacts, 12 aggregate
pattern entries, 52,593 aggregate claims, and 77,606 aggregate source
references. It does not identify which source record supports each finding.
The family is no longer an untraced URL gap: a bounded 100-industry sample
across 48 observed sectors is present. The full finding remains held until the
expanded sample's outcomes and source independence are independently checked.

A first [bounded traceability sample](ibis-finding-claim-sample.json) now
traces 100 matched industries across observed sectors and their claim-level
source IDs and URLs.
This is progress toward the gate, not full-finding validation.

Next test:

1. Select one finding, beginning with “Compliance Is Becoming Economic
   Architecture.”
2. Recover the underlying industry/claim records from the pinned pattern
   artifacts and source inventory.
3. Attach source IDs, URLs, publisher identity, period, geography, unit, and
   claim type to a bounded sample.
4. Add at least one counterexample and one outcome measure.
5. Keep the finding held until the sample is traceable and independently
   reviewed.

## Remaining medium-priority work

- Map the 21 IBIS force URLs to individual force claims and outcomes.
- Map the 25 annual-report citation URLs to specific themes and companies.
- Map the 39 Inc. opportunity URLs to the five opportunity hypotheses and
  independently test buyer demand and outcomes.
- Map the 89 social publication URLs to atlas claims while keeping platform
  discussion separate from prevalence.
- Review shared URLs and hosts across observations before counting repeated
  publisher material as independent confirmation.

## Rebuild and validate

```text
python3 scripts/build_external_repository_family_snapshot.py
python3 scripts/build_external_family_observations.py
python3 scripts/build_external_family_lineage_review.py
python3 scripts/build_ibis_finding_claim_sample.py
python3 scripts/build_external_evidence_gap_queue.py
python3 scripts/build_external_release_manifest.py
python3 scripts/validate_external_trend_intelligence.py
```

Or run the full ordered pipeline, including the frontend smoke test:

```text
python3 scripts/refresh_external_observatory.py
```

No action in this queue authorizes an internal company join. A candidate must
pass source lineage, denominator, comparability, counter-signal, and outcome
gates before entering the internal bridge.

The cross-publisher panel's computed host review is in
[`bounded-subset-lineage-review.json`](bounded-subset-lineage-review.json). It
finds two hosts (`fwc.gov.au` and `fairwork.gov.au`), with four records sharing
the FWC host; this is partial lineage diversity, not independent confirmation.
The independent GSMA/British Social Attitudes mechanism comparison is in
[`independent-stage-comparison.json`](independent-stage-comparison.json); it
remains mechanism-only until common units, populations, periods, and outcomes
are acquired.

The household-room comparison now includes a normalized ANUPoll record and a
2020-to-2025 adult-level endpoint alongside ABS GSS and HILDA evidence. Source
custody is complete for ANUPoll; the remaining gate is denominator and measure
reconciliation between adult-level expense difficulty and household-level
cash-flow or dissaving measures.
