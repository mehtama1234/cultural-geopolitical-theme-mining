# External trend-intelligence next actions

This is the current handoff for the living external-first goal. All actions
below preserve the rule that external evidence is qualified before any company
data is joined.

## Current backtest gate

The historical records for all five candidate comparisons are now pinned in
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
The family is no longer an untraced URL gap: a bounded 200-industry sample
across observed sectors is present. The full finding remains held until the
expanded sample's outcomes and source independence are independently checked.

A first [bounded traceability sample](ibis-finding-claim-sample.json) now
traces 200 matched industries across observed sectors and 48 non-matching
comparator industries across observed sectors, with claim-level source IDs, URLs,
publisher identities, and source types. The non-matching records are explicit
counterexample candidates; they are not proof that the finding is false or
that the pattern engine's threshold is unbiased. This is progress toward the
gate, not full-finding validation.

The sample now also carries a claim-level review table for 1,500 sampled claims.
It explicitly counts URL-locator, publisher-identity, temporal-metadata,
source-type, outcome-linkage, and independence-review status. In the current
refresh, 1,452 claims have URL locators, 1,227 have publisher identity, and
1,230 have temporal metadata; all 1,500 remain pending independence review.
These counts are evidence of the remaining work, not a promotion decision.

The new [IBIS claim-independence audit](ibis-claim-independence-audit.json)
now makes dependency visible at claim level: the sample contains 3,110 unique
URLs, 895 reused URLs, 1,324 hosts, and 517 reused hosts. It flags 1,453
claims with a dependency warning and leaves only 47 as candidates for manual
independence review. Reused URLs, hosts, or publishers are not counted as
independent confirmation; publisher ownership and study lineage still require
human verification.

The [IBIS independence review queue](ibis-claim-independence-review-queue.json)
turns those 47 candidates into assigned work. It records source URLs,
publisher/type/date fields, required evidence, four possible dispositions, a
10-business-day assignment target, and a fail-closed stop rule. All 47 start
unassigned and remain blocked from any company bridge until review is complete.

The [first review batch](ibis-first-review-batch.json) selects ten claims from
that queue using an explicit rule favoring government/academic source types,
host diversity, and source count. It is a work packet only: all ten remain
`pending_manual_review`, with no qualification or internal-data permission.

The first two metadata triages are recorded in
[`ibis-claim-review-dispositions.json`](ibis-claim-review-dispositions.json).
The drug-testing demand claim is held because three of four source rows are
Quest Diagnostics material, two lack publication dates, and no dated
independent outcome is present in the pinned artifact. This is a conservative
hold—not a finding that the claim is false. The cell-phone repair policy claim
has distinct New York and Colorado government publishers, but it is still held
because dates and a comparable repair or device-life outcome series are absent.
The other eight first-batch claims remain pending.

The [cell-phone repair outcome plan](cell-phone-repair-outcome-acquisition-plan.json)
now links the state policy records to the existing FTC repair-barrier evidence
and the ITU e-waste counter-signal. It explicitly refuses to pool them because
their populations, geographies, units, and outcomes differ, and specifies the
US repair/replacement panel needed for a real backtest.
An official-source screen now ranks Census NES (NAICS 811211/811213) as the
best public industry-scale candidate, while Census AIES, EPA electronics
tables/ADEPT, and BLS repair employment are retained with narrower context or
modeling boundaries. None is yet a phone-level repair outcome.
The resulting [Census CBP snapshot](census-repair-industry-snapshot.json)
contains 2019–2023 national and state rows for NAICS 811211 and 811213 with
download checksums and Census noise flags. It shows descriptive industry
movement, not a policy effect: 811211 establishments fell by 112 while
employees rose by 296; 811213 establishments fell by 218 and employees fell
by 8,869. These broad categories cannot be interpreted as phone-repair demand.

The [Census NES snapshot](census-nonemployer-repair-snapshot.json) adds the
small-business side for 2019–2024: one national row per year and 306 state
rows for five-digit NAICS 81121, with checksummed downloads, receipts, and
suppression flags. NES is more relevant to independent repair shops than CBP,
but it still measures broad electronic/precision repair businesses rather than
phone transactions, workers, policy exposure, or device-life outcomes. It is
kept as context and is explicitly not pooled with CBP, policy, or global
e-waste signals.

The [repair proxy comparison](census-repair-proxy-comparison.json) now aligns
the CBP paid-employee series and NES nonemployer series for 2019–2023. It is a
measurement-boundary check, not independent confirmation: both series come
from Census, cover different populations, and use different repair-category
granularity.

The food-insecurity independent challenge was also corrected against Urban's
published methods: the WBNS measure uses a 12-month reference period and the
six-item USDA short form, not a 30-day period. The comparison still remains
non-pooled because the populations, implementation details, uncertainty
release, and rights conditions differ; the 2025 WBNS sample also expanded to
include older adults.

Next test:

1. Select one finding, beginning with “Compliance Is Becoming Economic
   Architecture.”
2. Recover the underlying industry/claim records from the pinned pattern
   artifacts and source inventory.
3. Attach source IDs, URLs, publisher identity, period, geography, unit, and
   claim type to a bounded sample.
4. Review the 24 comparator candidates against at least one independent
   outcome measure and document why each comparator is informative.
5. Check publisher dependence and shared URLs at claim level, then expand the
   outcome sample before promotion.
6. Keep the finding held until the sample is traceable and independently
   reviewed.

The adult-day-care outcome review now identifies a bounded public acquisition
path through CDC/NCHS NPALS 2025 web tables, the 2022 public-use frame, and
Medicaid state context. It specifies the required denominator, period,
uncertainty, survey-frame, and rights fields. This is an acquisition gate, not
a utilization result; do not label policy rates as service utilization.
The 2025 weighted-estimates PDF is now recorded as national-only public evidence
with published standard errors; state-level fields still require verified web-
table/API extraction or separately approved restricted-data access.
The CDC public table API has now been queried and pinned: it exposes a 2020
state frame (52 geographies in the raw table, 44 with numeric rows in the
selected measures) and national 2022/2025 rows. Its 2025 provider value is
3,300 versus 4,448 in the weighted PDF, so the extract is retained as a
definition-reconciliation counter-signal and no cross-vintage growth rate is
calculated.

The forecast comparison now has a separate [forecast lineage review](forecast-lineage-review.json):
four rows resolve to three publisher hosts, with the repeated UN DESA host
visible. Distinct hosts are treated as a lineage signal only; model dependence,
forecast vintage, uncertainty, rights, and realized-outcome checks remain open.

## Remaining medium-priority work

- Review the new [IBIS force claim map](ibis-force-claim-map.json): all 21
  declared source IDs now resolve to the pinned source inventory, and claim
  references are attached where the reviewed claim inventory supports them.
  Claim-level review remains partial for some forces. The new
  [BLS labor-capacity mechanism check](bls-labor-capacity-mechanism-check.json)
  shows rising earnings alongside falling openings and hires in education and
  health services, with the same direction in manufacturing. Treat that as a
  counter-signal, not proof of a care-labor shortage; add an independent
  vacancy, filled-hours, or service-rationing measure and retain the finding on
  hold.
- Map the 25 annual-report citation URLs to specific themes and companies.
- The annual-report citation map now preserves all 25 rows, five source
  packets, ten publisher hosts, periods, document types, status, and claim
  boundaries. It remains source-scoped until each citation is tied to a theme
  claim and checked against an independent outcome source.
- Map the 39 Inc. opportunity URLs to the five opportunity hypotheses and
  independently test buyer demand and outcomes.
- The Inc. opportunity source map now preserves 39 evidence rows, 22 buyer
  proxy rows, five hypotheses, and 45 distinct URLs. All five remain
  `monitor`: direct interviews and field outcome cohorts are still pending, so
  public company pages are not treated as validated demand.
- Map the 89 social publication URLs to atlas claims while keeping platform
  discussion separate from prevalence.
- The social citation map now preserves 89 raw appendix URL occurrences, 70
  normalized URLs, and 31 theme-linked citations across ten themes. The
  remaining URLs are explicitly unmapped; platform evidence remains bounded
  signal until publisher lineage and independent population or outcome evidence
  are checked.
- Review shared URLs and hosts across observations before counting repeated
  publisher material as independent confirmation.
- The new [publisher-dependence summary](publisher-dependence-summary.json)
  compares 184 normalized source rows across four maps, finding 67 hosts and
  four shared hosts. These are dependency warnings, not an independence score;
  claim-level publisher ownership and dataset lineage remain to be reviewed.

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
