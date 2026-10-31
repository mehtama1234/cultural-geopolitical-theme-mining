# External trend-intelligence refresh runbook

This is the operating procedure for keeping the external-first goal current.
It keeps source capture, normalization, comparison, and company bridging as
separate stages.

[`refresh-schedule.json`](refresh-schedule.json) is the machine-readable
cadence and trigger register for the eight source families. Use it to decide
when to rerun a family-specific refresh; every refresh still follows the full
pin, normalize, lineage, challenge, promotion, and validation sequence below.

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
python3 scripts/build_ibis_finding_claim_sample.py
python3 scripts/build_external_release_manifest.py
```

The sibling intake is deliberately separate from the 2,131-record local
manifest until its source URLs, units, populations, periods, and independence
have been reviewed. The lineage review also checks URL and host overlap across
observations so shared publishers are not mistaken for independent evidence.
Rebuild the explicit gap queue after the lineage review:

```text
python3 scripts/build_external_evidence_gap_queue.py
```

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

Use [`promotion-queue.json`](promotion-queue.json) as the single gate register;
do not create an internal bridge from a candidate that is not marked
`internal_bridge_ready`.

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

Run the release-manifest build after all artifact changes so the frontend and
downstream consumers can identify one checksum-backed package and its
source-tree commit.

Serve `analysis/external-trend-intelligence/` over HTTP and smoke-test
`board.html` after changing a JSON artifact. The board is a reader; source
records and lineage files remain authoritative.

## Current held work

The care/longevity lane has a measurement matrix and contextual subset but is
held because its populations and denominators are heterogeneous. IBIS,
social-research, and trend-hunting inputs are synthesis or hypothesis layers
until claim-level and outcome evidence are attached. This is expected state,
not a validation failure.
