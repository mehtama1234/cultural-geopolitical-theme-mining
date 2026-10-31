# External source registry and trend-analysis loop

This is the operating map for the living trend-intelligence program. The
company-trend records are outputs of this process; they are not the complete
source universe.

## The external repositories you mean

These are the named upstream sources already used by the wider program:

1. **`cultural-geopolitical-theme-mining`** — societal, institutional,
   cultural, consumer, place, and geopolitical research; the current repo and
   14-theme evidence atlas.
2. **`social-research`** — bounded public discussion and creator signals from
   YouTube, Reddit, LinkedIn, X, TikTok, and related platform work. It is a
   signal observatory, not a representative population or buying-intent panel.
3. **`trend-hunting`** — broad public-signal, consumer, and trend synthesis,
   including theme/subtheme conclusions, counterexamples, and cross-repository
   trend chains.
4. **`annual-report-research` / `trends-observatory`** — public-company annual
   and quarterly filings, strategy, operating constraints, financial claims,
   monetization, and burden transfer.
5. **`inc5000-analysis`** — private-company and bottom-up market signals,
   growth patterns, business models, and emerging commercial responses.
6. **`ibis-industries`** — industry definitions, structures, forces, capacity,
   dependencies, and operating pressures. Its pinned corpus contains 1,491
   industry records and a separate 17,998-source provenance inventory; the
   analytic synthesis still does not establish customer demand, prevalence,
   willingness to pay, or a live customer outcome.

`research-signals` provides source capture and provenance infrastructure, while
`organization-intelligence-system` provides shared identity, evidence,
comparability, review, and release contracts. Those two are integration and
governance layers, not interchangeable evidence of a trend.

The external source set is therefore not just government statistics. It is the
combination of public discussion, trend synthesis, cultural/geopolitical
research, company filings, Inc. 5000 company signals, and IBIS industry
context. A trend becomes stronger when independent source families converge;
the sources must not be flattened into one score.

## Purpose

Continuously bring in external evidence, detect repeated or changing patterns,
compare supporting and counter-signals, and promote only decision-grade
findings into the company-facing portfolio.

```text
external source
  -> dated source snapshot
  -> normalized observation
  -> cross-source comparison
  -> trend candidate and counter-signal
  -> mechanism, distribution, and uncertainty
  -> company exposure and decision test
  -> monitored record and next refresh
```

## Source families

| Family | Examples of external sources | What it can observe | Typical refresh |
|---|---|---|---|
| Households, work, and prices | BLS, Census, BEA, Federal Reserve, FRED, OECD | income, prices, employment, time, confidence, entry/exit, household room | monthly, quarterly, annual |
| Health, care, and access | CDC, NCHS, AHRQ/MEPS, CMS, WHO | disability, unmet need, care use, transport, health burden, access | quarterly, annual |
| Housing, place, and mobility | HUD, FHFA, Census ACS, FEMA, NOAA, DOT, local open data | rent, housing cost, insurance, displacement, hazards, commuting, mobility | monthly, quarterly, annual, event-driven |
| Markets, firms, and competition | SEC EDGAR, company filings, FTC, DOJ, Census BDS, procurement records | ownership, concentration, transactions, suppliers, capital, firm entry/exit | event-driven, quarterly, annual |
| Infrastructure, energy, and technology | EIA, FERC, FCC, DOE, EPA, grid operators, public utility data | capacity, outages, energy, connectivity, dependency, reliability | hourly to annual |
| Culture, language, and public meaning | UNESCO, national statistics, language/community bodies, cultural institutions, public discussion | language use, identity, trust, norms, representation, legitimacy, emerging concerns | event-driven, periodic |
| Geopolitics and state power | UN, World Bank, IMF, WTO, State Department, sanctions/procurement records, SIPRI, ACLED/UCDP where licensed | conflict, trade, sanctions, alliances, state capability, burden, permission, dependence | daily to annual |
| Research and evaluation | peer-reviewed papers, working papers, policy evaluations, methods documentation | mechanisms, causal estimates, limits, replication, counterevidence | publication-driven |

The examples are source families, not a claim that every source is always
available, comparable, or licensed for reuse. Access terms and revision status
must be recorded for each source snapshot.

## Minimum source-snapshot fields

Every external observation entering the system should preserve:

- source name, publisher, URL or API endpoint, and access date;
- publication date, observation period, revision/version, and retrieval method;
- unit, denominator, geography, population, sector, and measure definition;
- original value and transformed value, if any, with transformation code;
- method, sample, missingness, suppression, and known bias;
- licensing or access restriction;
- source tier: official statistic, administrative record, firm/market record,
  research, community/cultural source, or public discussion;
- related observations and identifiers, without implying a join that is not
  supported; and
- supporting signal, counter-signal, and the next refresh date.

## Analysis rules

1. Keep source units separate until a documented transformation makes them
   comparable.
2. Do not join different sources as if they followed the same person,
   household, firm, place, or event without identifiers and aligned timing.
3. Compare at least two independent source families for a material trend.
4. Preserve a counter-signal and a plausible alternative explanation.
5. Separate observed change, inferred mechanism, company exposure, and scenario.
6. Record revisions and rerun affected findings when the source changes.
7. Promote a candidate only when the evidence supports a named mechanism,
   affected-group distribution, business exposure, uncertainty, and next test.

## External-to-frontend contract

The external source layer should feed normalized observations and trend records;
the frontend should not scrape or reinterpret raw external pages. The live
external reader is `analysis/external-trend-intelligence/board.html`; the
company-facing portfolio remains a downstream translation surface at
`analysis/company-trend-intelligence/portfolio.json`. Machine-readable source
observations preserve stable IDs, provenance, timestamps, and links back to the
source packet and trend record.

## First implementation sequence

1. Inventory source endpoints and access terms by theme.
2. Build one normalized observation schema and source-snapshot manifest.
3. Start with official, stable sources for each theme and add research and
   community sources for mechanism and meaning.
4. Run scheduled refreshes and revision checks.
5. Generate candidate comparisons, counter-signals, and promotion queues.

The initial implementation now has the source snapshot, normalized family
intake, lineage review, held comparisons, and external board. Remaining work is
to resolve artifact-level independence and outcome gates before any candidate
is bridged to internal company data.
6. Publish only promoted findings to the company-facing board.
