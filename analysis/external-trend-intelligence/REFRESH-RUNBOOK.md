# External trend-intelligence refresh runbook

This is the operating procedure for keeping the external-first goal current.
It keeps source capture, normalization, comparison, and company bridging as
separate stages.

## 1. Pin the external inputs

Update the revisions and manifest paths in
[`source-family-registry.json`](source-family-registry.json) and
`scripts/build_external_repository_family_snapshot.py` only after reviewing the
new sibling-repository state. Never use an unpinned working tree as evidence.

Run:

```text
python3 scripts/build_external_source_registry_snapshot.py
python3 scripts/build_external_repository_family_snapshot.py
```

Review the resulting blob IDs, file sizes, missing paths, and directory counts.

## 2. Rebuild the local observation index

For the cultural-geopolitical repository, rebuild the source-backed index from
a pinned tree:

```text
python3 scripts/build_external_observation_manifest.py \
  --git-ref HEAD \
  --output analysis/external-trend-intelligence/observation-manifest.json
```

For the pinned sibling families, rebuild the bounded intake:

```text
python3 scripts/build_external_family_observations.py
python3 scripts/build_external_family_lineage_review.py
```

The sibling intake is deliberately separate from the 2,131-record local
manifest until its source URLs, units, populations, periods, and independence
have been reviewed.

## 3. Compare and challenge

Update `external-family-comparisons.json` only when a relationship has:

- exact observation IDs;
- a named mechanism;
- a counter-signal;
- a next test; and
- a promotion gate.

Thematic adjacency, shared words, industry labels, ranking, or timing is not a
valid join. Host count and URL count are coverage measures, not independent
confirmation.

## 4. Promote cautiously

Before moving a candidate from held to qualified, reconcile:

- source publisher and artifact identity;
- unit, denominator, geography, population, and period;
- transformation and uncertainty;
- replication versus restatement of the same underlying source;
- affected groups, alternatives, and counterexamples; and
- the smallest decisive next test.

Only a qualified external trend can enter the internal bridge contract. The
bridge must name the company, internal dataset, identifier, geography, period,
outcome, and unmatched cases. No internal company join is implied by this
repository’s source or theme labels.

## 5. Validate and publish

Run:

```text
python3 scripts/validate_external_trend_intelligence.py
```

Serve `analysis/external-trend-intelligence/` over HTTP and smoke-test
`board.html` after changing a JSON artifact. The board is a reader; source
records and lineage files remain authoritative.

## Current held work

The care/longevity lane has a measurement matrix and contextual subset but is
held because its populations and denominators are heterogeneous. IBIS,
social-research, and trend-hunting inputs are synthesis or hypothesis layers
until claim-level and outcome evidence are attached. This is expected state,
not a validation failure.
