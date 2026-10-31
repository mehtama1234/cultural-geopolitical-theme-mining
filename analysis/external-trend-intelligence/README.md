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
The registry records `trends-observatory` as an alias for the annual-report
family; no separate local checkout was found, so it is not treated as a second
independent source family.

[`repository-family-snapshot.json`](repository-family-snapshot.json) records
the exact Git blob IDs and file sizes for those pinned manifests. This makes
the lineage auditable without copying or silently importing the sibling
repositories into this one.

The first bounded intake queue is in
[`external-family-intake-queue.json`](external-family-intake-queue.json). It
names the exact Inc. 5000, annual-report, and IBIS artifacts to extract next and
states what each artifact can—and cannot—support.

The first normalized intake is in
[`external-family-observations.json`](external-family-observations.json). It
contains ten reported observations from the pinned Inc. 5000,
annual-report, IBIS, social-research, and trend-hunting artifacts. They are
deliberately not merged into the 2,131-record observation manifest yet: their
source coverage is uneven, and units, geographies, and independence still
require artifact-level review. The two Inc. 5000 trend records now preserve
their example URLs and denominator explicitly; the other records remain
artifact-level synthesis or provenance signals.

The held comparison layer is
[`external-family-comparisons.json`](external-family-comparisons.json). It
records three thematic/mechanism relationships without treating adjacency as
a data join or promoting any new trend prematurely. It now includes three
additional held comparisons for IBIS compliance, labor-capacity, and
infrastructure forces, plus social adaptation and AI-control comparisons.

The corresponding URL, host, denominator, and independence audit is in
[`external-family-lineage-review.json`](external-family-lineage-review.json).
The two Inc. 5000 trend records have partial URL coverage review; every new
observation remains on hold until independence and outcome evidence are checked.

The first broader candidate built from these lanes is documented in
[`CARE-CAPACITY-CANDIDATE.md`](CARE-CAPACITY-CANDIDATE.md) and
[`care-capacity-candidate.json`](care-capacity-candidate.json). It is a held
candidate linking care/longevity company signals to access time, unpaid care,
work, demographic, and service-capacity evidence; it is not yet a promoted
structural trend.

Its measurement audit is in
[`care-capacity-measurement-matrix.json`](care-capacity-measurement-matrix.json).
The matrix preserves each record’s period, geography, denominator, and measure
definitions and confirms that the current evidence is heterogeneous rather than
poolable.

[`care-capacity-comparable-subset.json`](care-capacity-comparable-subset.json)
then isolates six contextual measures—work participation, work exit, care
intensity, diary-day time, and support satisfaction. These illuminate the
mechanism but remain explicitly non-pooled and held.

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

The machine-readable manifest, full source-universe snapshot, sibling-family
intake, and first comparison queue are generated from pinned source trees. The
next build is source-level lineage, independence, and promotion testing for
the held candidates across the 14 themes. The company trend board remains a
downstream view, not the discovery engine.

The repeatable refresh procedure is in
[`REFRESH-RUNBOOK.md`](REFRESH-RUNBOOK.md). It covers pinning sibling
repositories, rebuilding observations, auditing lineage, challenging
comparisons, and publishing the board.
