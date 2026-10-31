# External trend-intelligence goal v1

**Program:** External signal, trend, and cross-source intelligence
**Audience:** Research, strategy, market, product, risk, and company-intelligence teams
**Status:** Governing, living, external-first goal

## The goal

Build and maintain a living system that uses external data and research to
identify meaningful cultural, social, financial, technological, workforce,
institutional, infrastructure, industry, and geopolitical trends before they
become obvious.

The system must begin with external evidence. It should discover signals,
compare independent sources, identify repetition and reversal, preserve
counter-signals, explain mechanisms and affected groups, and distinguish
observed change from interpretation. Only after a trend is externally
qualified should the system connect it to internal company data to test
exposure, relevance, and action.

## Plain-language promise

See what is changing outside the company, understand whether it is real and
important, and then test whether it matters inside the company.

## The end-to-end chain

```text
external source
  -> source snapshot and provenance
  -> normalized observation
  -> cross-source comparison
  -> trend candidate and counter-signal
  -> mechanism, distribution, and uncertainty
  -> qualified external trend
  -> internal company-data bridge
  -> company exposure, opportunity, risk, and decision test
  -> monitoring and refresh
```

## External source perimeter

The first source perimeter includes:

- `cultural-geopolitical-theme-mining` for cultural, social, institutional,
  place, consumer, and geopolitical research;
- `social-research` for bounded public discussion and creator signals;
- `trend-hunting` for public-signal and consumer-trend synthesis;
- `annual-report-research` / `trends-observatory` for public-company filings,
  strategy, operating constraints, and financial claims;
- `inc5000-analysis` for private-company growth and bottom-up market signals;
- `ibis-industries` for industry structure, forces, bottlenecks, and operating
  context; and
- official statistics, administrative records, research papers, market data,
  infrastructure records, cultural/community sources, and geopolitical
  records listed in the [external source registry](EXTERNAL_SOURCE_REGISTRY.md).

`research-signals` and `organization-intelligence-system` provide provenance,
identity, comparability, review, and release infrastructure. They are not
substitutes for the underlying evidence.

## Required questions for every external trend

1. What changed, in which source units, places, and periods?
2. Which sources independently support it, and which contradict it?
3. Is it a signal, repeated pattern, structural shift, reversal, or contested
   interpretation?
4. What mechanism could explain it, and which arrows remain inferred?
5. Who is more exposed, who has alternatives, and who absorbs residual cost?
6. What cultural, financial, institutional, and geopolitical meaning follows?
7. What would change the conclusion?
8. What internal company data could test relevance, without pretending the
   external source followed the same company, person, or event?

## External-to-internal bridge rule

Internal company data is a second-stage validation layer. A bridge must state
the company, unit, geography, period, identifier, and hypothesized mechanism.
It must preserve unmatched cases, incompatible periods, missing denominators,
and alternative explanations. A thematic match, industry label, ranking, or
similar name is not a valid company join by itself.

## What success means

Success is not a fixed number of trend records. Success is a repeatable,
refreshable pipeline that can move from external evidence to qualified trends,
then to clearly bounded internal tests, while retaining source lineage,
uncertainty, counterevidence, and the ability to revise or reject a finding.

## Current operating state

The first implementation is live in
[`analysis/external-trend-intelligence`](analysis/external-trend-intelligence):

- `2,131` source-backed observations are indexed in the current repository;
- `118` candidate external sources are preserved in the source-registry
  snapshot;
- `14` program themes and `4` qualified-but-unconfirmed cross-source
  candidates are visible on the board;
- `10` observations from pinned Inc. 5000, annual-report, IBIS,
  social-research, and trend-hunting artifacts have been normalized with
  source paths, revisions, units, and boundaries;
- `8` external-family comparisons and `2` held candidates (care/longevity and
  adaptation/control/proof/resilience) have been added without treating
  thematic adjacency as a valid join; and
- `0` internal company datasets have been joined or used to claim company
  impact.

The care/longevity candidate has a measurement matrix and a contextual subset,
but remains held because its source populations, periods, denominators, and
units are heterogeneous. This is the intended operating posture: preserve a
useful signal, make uncertainty visible, and keep testing before promotion.

## Operating materials

- [External source registry](EXTERNAL_SOURCE_REGISTRY.md)
- [External trend-analysis contract](analysis/external-trend-intelligence/README.md)
- [External refresh runbook](analysis/external-trend-intelligence/REFRESH-RUNBOOK.md)
- [Company-facing translation layer](COMPANY_TREND_INTELLIGENCE_GOAL_V1.md)
