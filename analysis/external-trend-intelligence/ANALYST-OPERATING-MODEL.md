# External trend-intelligence analyst operating model

This workflow keeps discovery, evidence review, trend qualification, and
company testing separate. Every handoff leaves a machine-readable artifact and
an explicit unresolved question.

## Roles

- **Source steward:** maintains the source-family registry, revisions, rights
  status, access route, cadence, and refresh evidence.
- **Evidence analyst:** extracts observations and claims with units,
  denominators, geography, period, uncertainty, counter-signal, and source
  locator.
- **Lineage reviewer:** checks publisher, URL, host, shared dataset, and
  restatement dependence; records whether apparent corroboration is actually
  independent.
- **Trend challenger:** tests mechanism, comparability, persistence,
  falsifier, and backtest design; can keep a candidate held or reverse it.
- **Decision translator:** writes bounded decision implications only after an
  external trend clears the qualification gates; owns the pilot contract but
  cannot approve its own internal data access.
- **Release owner:** runs validators, checks the manifest, publishes the board,
  and records the release commit and known limitations.

## The recurring cycle

### Intake (as triggered)

The source steward pins the revision or artifact, records the access and rights
boundary, and adds the trigger to `refresh-schedule.json`. The evidence analyst
does not infer freshness from a title or URL alone.

### Weekly review

The evidence analyst reviews new or changed records, fills the evidence
contract, and adds missing source locators or counter-signals to the gap queue.
The lineage reviewer checks shared URLs and publishers before a source count is
described as corroboration.

### Monthly challenge

The trend challenger reviews every candidate in the qualification matrix and
the falsification review queue, updates the next decisive test, and records
whether the candidate should remain held, move to qualified, enter monitoring,
or be marked reversed. A candidate with absent evidence fails the gate; it is
not scored by optimism.

### Quarterly decision review

The decision translator may propose a bounded company pilot only for a trend
marked `qualified_external_trend`. The proposal must specify company, unit,
identifier or aggregate basis, geography, period, outcome, denominator,
unmatched cases, privacy, rights, and a falsifier. The release owner verifies
that no internal join was made before approval.

### Release and handoff

The release owner runs the refresh-status report, evidence-contract audit,
qualification matrix, monitoring status, falsification queue, release-manifest
build, and external validator. The handoff records the commit, artifact
checksums, open gaps, held candidates, and the next review date. A frontend
chart is not authoritative unless its source artifact appears in the release
manifest.

The machine-readable `ownership-assignment-queue.json` reconciles the six
roles to `operating-handoff.json` and records the acceptance criteria for named
primary and backup owners. `refresh-continuity-audit.json` records observed
run spacing and explicitly distinguishes a short run burst from demonstrated
weekly operation. These controls must remain visible in the handoff; neither
one invents an owner or proves future two-year continuity.

The ownership queue also carries the assignment protocol: required identity
and acknowledgement fields, a ten-business-day assignment target, backup
activation triggers, an escalation path, and evidence required to accept a
role. Until a person or accountable team is recorded, the role remains
unassigned and release ownership is not inferred.

## Required review record

Every review note must answer:

1. What changed since the previous revision?
2. Which source, unit, population, geography, and period support the claim?
3. What publisher or dataset dependence could make this look independent?
4. What counter-signal or subgroup exception is present?
5. What observation would falsify or reverse the candidate?
6. What is the smallest next test, and who owns it?
7. Is a company connection permitted yet? If not, why not?

## Escalation rules

- Missing source identity, rights boundary, or observation period: stop and hold.
- Shared publisher or dataset discovered after comparison: downgrade the
  independence gate and re-review the comparison.
- Incompatible denominator, unit, geography, or period: do not pool; create a
  bounded comparison request instead.
- A later release contradicts the mechanism: mark the candidate for reversal
  review rather than silently editing the original claim.
- Any privacy, access, or redistribution uncertainty: keep the pilot in
  `design_only_external_gate` and do not connect internal data.

## Current handoff

The current release has eight source families, 2,135 indexed records, five
cross-source candidates (one monitored external trend and four held), three
design-only company pilots (all blocked by the external-first gate), and a
monitoring register. The next analyst actions
are the claim-level source maps and dated holdout evidence named in the
qualification and backtest registers.
