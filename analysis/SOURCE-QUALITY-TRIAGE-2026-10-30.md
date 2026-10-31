# Source-quality triage — 2026-10-30

## Purpose

The source-link audit established structural provenance: every current rotation
packet has at least one URL. This triage adds the next layer. It classifies the
most frequently observed source domains by default authority and likely
evidentiary role, while preserving the distinction between an official source
and a source that actually closes a claim.

The companion CSV covers the 35 most frequently observed domains in the 327
rotation packets. It is a domain-level screening ledger, not a claim-level
verdict. Domain authority is a routing signal for review; it is never a
substitute for reading the source, checking the population and date, or testing
whether the source supports the packet’s exact proposition.

## Current inventory

- Rotation packets scanned: **327**
- URL occurrences: **2,518**
- Unique URL values: **2,277**
- Domains covered in this first triage batch: **35**
- Occurrences covered by the 35-domain batch: **1,492**
- Remaining occurrences outside this batch: **1,026**

## What the triage changes

The atlas should now treat source quality as a two-stage conversion:

```text
domain / document authority
  -> source design, population, date and method
  -> exact claim support and uncertainty
  -> named actor, place, exposure and outcome
  -> conversion packet and synthesis proposition
```

An OECD, WHO, UNESCO, GAO, World Bank or government link is usually a strong
starting point. It can still support only a global signal, legal standard,
scenario, recommendation, administrative count, selected case or risk
diagnosis. Conversely, a secondary source can be useful for discovery but should
not silently carry a high-stakes proposition when a primary source is available.

## Immediate review priorities

1. **High-frequency primary domains:** review the highest-weight claims from
   WHO, OECD, UNESCO, World Bank, UNICEF, GAO, ILO, IEA, NIST, EPA and UN
   sources for population, denominator, date, method and outcome boundary.
2. **Aggregators and document mirrors:** distinguish `documents1.worldbank.org`,
   `files.gao.gov` and `digitallibrary.un.org` from the parent institution and
   record the underlying report title, author, mandate and publication date.
3. **Bibliographic discovery:** treat PubMed as an index until the article,
   methods and limitations are inspected.
4. **Institutional secondary commentary:** treat World Bank blogs as leads and
   trace them to the underlying dataset, evaluation or report before promotion.
5. **Legal and policy text:** treat EUR-Lex and other official legal sources as
   evidence of a rule or obligation, not evidence of implementation,
   compliance, remedy or lived experience.

## Next evidence action

The first 20-claim batch is recorded in
`CLAIM-SOURCE-REVIEW-2026-10-30.csv`. The next batch should select the 20
highest-weight packet propositions whose
source domain is in the high-priority group. For each, record:

- exact source title, authoring institution and publication date;
- source type: law, administrative data, survey, evaluation, audit, scenario,
  normative framework or commentary;
- population, geography, denominator and observation period;
- direct observation versus interpretation;
- what stage of the six-stage conversion it closes;
- the strongest counterexample or alternative explanation; and
- the missing named actor, place, exposure, remedy or later outcome.

Only after that review should a proposition be upgraded, cross-linked or used
as a causal bridge in the atlas synthesis.
