# External trend-intelligence operating contract

This directory defines the first-stage external analysis layer. It discovers
and qualifies trends before any internal company data is used.

`observation-manifest.json` is the current provenance-preserving index of the
source-backed records already in this repository. It contains record metadata,
themes, source hosts, and boundaries; it does not copy or merge the underlying
measurements. Rebuild it from a pinned tree with:

```text
python3 scripts/build_external_observation_manifest.py \
  --git-ref HEAD \
  --output analysis/external-trend-intelligence/observation-manifest.json
```

`source-registry-snapshot.json` preserves the complete 118-source inventory
from `manifests/source-registry.json`, even when that upstream manifest is not
present in the working tree. It is a source-universe map, not proof that a
source is currently reachable, licensed, fresh, or independent. Rebuild it
with:

```text
python3 scripts/build_external_source_registry_snapshot.py \
  --git-ref HEAD \
  --output analysis/external-trend-intelligence/source-registry-snapshot.json
```

The first cross-source comparison is in
[`CROSS-SOURCE-CANDIDATES.md`](CROSS-SOURCE-CANDIDATES.md). These are
qualified candidates, not yet company findings or forecasts.

The first URL and publisher-lineage review is in
[`SOURCE-LINEAGE-AUDIT.md`](SOURCE-LINEAGE-AUDIT.md). Host and URL counts are
coverage measures, not independent-confirmation scores.

The broader repository-level source universe is pinned in
[`source-family-registry.json`](source-family-registry.json). The annual-report
research family and Inc. 5000 family now have explicit sibling-repository
revisions and manifest paths; their records remain source-scoped until their
individual evidence and independence are reviewed.

The later internal-data step is documented in
[`INTERNAL-BRIDGE.md`](INTERNAL-BRIDGE.md). It is a separate contract and does
not change the meaning or status of external evidence.

Potential internal systems and their authority boundaries are listed in
[`INTERNAL-SOURCE-READINESS.md`](INTERNAL-SOURCE-READINESS.md) and
[`internal-source-catalog.json`](internal-source-catalog.json). The catalog is
inventory-only until an owner approves a specific source and snapshot.

For a visual readout of the external inventory and candidate comparisons, open
[`board.html`](board.html) through a local HTTP server.

## Stages

1. **Capture:** preserve the external URL/API, publisher, date, retrieval
   method, version, checksum, license/access boundary, unit, geography,
   denominator, and observation period.
2. **Normalize:** retain the original value and unit; record any transformation
   separately. Never silently merge incompatible definitions.
3. **Compare:** group observations by a declared theme, mechanism, place,
   period, or entity. Compare independent source families rather than counting
   copies of the same claim.
4. **Challenge:** add counter-signals, missing populations, competing
   explanations, source revisions, and what would change the interpretation.
5. **Qualify:** classify the result as signal, repeated pattern, qualified
   trend, structural shift, reversal, or contested finding.
6. **Bridge:** only after qualification, define the internal company data needed
   to test exposure or relevance. Keep external and internal evidence separate.
7. **Publish:** expose the qualified result and provenance to the frontend;
   do not make the frontend scrape raw external sites.

## Minimum external observation

Each observation should have:

- stable observation ID and source ID;
- source URL/API, publisher, retrieval date, revision, and checksum;
- publication date and observation period;
- unit, denominator, geography, population, sector, and measure definition;
- original value, unit, and transformation history;
- method, uncertainty, missingness, and access/rights boundary;
- theme/subtheme and proposed mechanism;
- supporting source, counter-source, and competing interpretation; and
- status: `observed`, `reported`, `estimated`, `compared`, `inferred`, or
  `open`.

## Internal bridge record

An internal bridge is valid only when it names:

- the external trend and exact source observations;
- the company, internal dataset, entity identifier, geography, and time window;
- the hypothesized exposure or mechanism;
- the outcome to test and its denominator;
- unmatched or incompatible records;
- privacy, access, and rights constraints; and
- the decision that the test can inform.

Industry labels, company names, rankings, similar categories, or coincident
timing are candidate connections—not proof of a valid join.

## Current next build

The machine-readable manifest and full source-universe snapshot are generated
from a pinned source tree. The next build is deeper lineage and cross-source
candidate comparison for the 14 themes, with counter-signals and a promotion
queue. The company trend board remains a downstream view, not the discovery
engine.
