# External trend-intelligence operating contract

This directory defines the first-stage external analysis layer. It discovers
and qualifies trends before any internal company data is used.

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

Create a machine-readable external-observation manifest from the existing
source registry and upstream repository snapshots. Then generate cross-source
candidate comparisons for the 14 themes, with counter-signals and a promotion
queue. The company trend board remains a downstream view, not the discovery
engine.
