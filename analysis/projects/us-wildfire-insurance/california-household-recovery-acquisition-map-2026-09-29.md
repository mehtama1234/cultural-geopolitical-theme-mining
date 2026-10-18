# California wildfire household-recovery acquisition map

**Checked:** 2026-09-29  
**Status:** executable public-data route; no household-level claim file or
same-property insurance-to-repair join is currently asserted

## Purpose

The California wildfire-insurance episode already observes market pressure,
claims, aggregate payment, complaint, regulatory intervention, and public
backstop response. The missing end-to-end stage is whether a damaged property
and household moved from claim activity to repair, safe occupancy, stable
housing, and later insurance choice.

This map identifies the next public evidence route while preserving the unit
boundary. It is an acquisition plan, not a claim that the sources below can be
joined into a person-level panel today.

## Public route

```text
fire footprint / damage
  -> property or neighborhood displacement
  -> permit and debris-removal progress
  -> insurance claim and payment aggregate
  -> [open] property-level repair, occupancy, mortgage, move/stay,
           renewed coverage, and later trust or political attribution
```

The new [California wildfire recovery stage audit](california-wildfire-recovery-stage-audit-v1.md)
turns the currently available dashboard, claims, enforcement, and advocacy
surfaces into a coverage-and-timing comparison. It does not infer a
same-household claim-to-repair trajectory.

### Available public surfaces

| Surface | Unit and contribution | What remains unobserved |
|---|---|---|
| [California DOI wildfire claims tracker](https://www.insurance.ca.gov/01-consumers/180-climate-change/Wildfire-Claims-Tracker.cfm) | Fire-level and claim-category counts, partial-payment status, and aggregate dollars paid for the Eaton/Palisades fires | Which property received what, payment timing, adequacy, final repair, safe occupancy, or move/stay |
| [LA County Wildfire and Windstorm Impact Dashboard](https://recovery.lacounty.gov/data-recovery-tools/) | Public integrated view of affected communities, housing/displacement, workers/businesses, and environmental conditions | Insurance status, household claim path, payment adequacy, and durable recovery |
| [LA County permitting-progress dashboard](https://recovery.lacounty.gov/rebuilding/permitting-progress-dashboard/) | Property/rebuild permitting progress and rebuilding-stage geography where the public dashboard exposes it | Whether a permit corresponds to an insurance payment, completed construction, occupancy, or the original household |
| [LA County debris-removal and recovery maps](https://recovery.lacounty.gov/returning-after-fire-faq/) | Damage, cleanup, and return-to-property context | Claim adjudication, temporary housing, mortgage continuity, and insurance renewal |
| [California DOI wildfire-risk reporting](https://www.insurance.ca.gov/01-consumers/200-wrr/WildfireRiskInfoRpt.cfm) | Insurer-submitted residential-property experience and risk-reporting framework | Public claim-level records, household affordability, and individual market transitions |

## Newly located routes and access gates

The county's permitting page currently links to a [Fire Survivor Insurance
Survey](https://www.efsurvivors.net/firesurvey) inviting Eaton and Palisades
survivors to report their experience with insurers. This could supply the
missing claimant-experience layer, but it is currently an invitation/survey
route rather than an authorized respondent file. Before use, record its sample
frame, recruitment, consent, weighting, question wording, missingness, and
data-use terms. Do not combine responses with public property or permit data
unless the terms explicitly permit that linkage and the identifiers are
handled lawfully.

### Survey data-governance audit completed — 2026-09-29

The survey's [August 2, 2026 data-handling policy](data/efsn-insurance-survey-data-handling-policy-2026-08-02.txt)
materially clarifies the route. It separates raw, analytic, public-use,
contact/advocacy, and qualitative files; permits insurer-, fire-, housing-,
owner/renter-, claim-, delay/payment-, service-rating-, and recoded-recovery
comparisons in a future public-use file; and requires address recoding,
small-cell suppression, and disclosure review. It also states that contact and
advocacy participation is voluntary and permission-based.

This is a governance/access result, not respondent evidence. The invitation
still does not publish the sample frame, response count, weighting plan, or
public-use dataset, and the policy does not authorize the atlas to obtain raw
identifiable files. The route is therefore promoted to “public-use dataset
watch,” with a lawful future acquisition gate rather than a current household
estimate.

### Live instrument audit completed — 2026-09-29

The accessible first page of the English SurveyMonkey instrument asks for the
affected-home address, Eaton-versus-Palisades fire, and renter-versus-owner
status, all required. This confirms that the instrument begins with a
household/property eligibility and stratification layer, while the exact
address is protected by the separate recoding policy before public release.
The live page still exposes no recruitment denominator, response count,
weighting plan, or results. No response was submitted; the [instrument audit
artifact](data/efsn-survey-instrument-page1-audit-2026-09-29.txt) preserves the
retrieval boundary.

The EFSN homepage now supplies a distinct advocacy-source layer: it reports
1,600 State Farm accounts used in Los Angeles County litigation, says seven in
ten survivors are still not home, roughly half have taken on new debt while
waiting for recovery funds, and claims more than $100 million in previously
stalled payments moved to families. These are source-defined advocacy claims,
not representative survey estimates or verified household outcomes; they are
retained separately in the [EFSN evidence-to-power record](../../records/us-efsn-survivor-insurance-advocacy-recovery-2026.json).

The County has now made the institutional conversion explicit: its State Farm
lawsuit says community-organization evidence, hundreds of complaints, and
policyholder documents informed the investigation, while a September Farmers
investigation addresses contamination, remediation, delays, underpayments,
denials, and living expenses. The [County enforcement record](../../records/us-la-county-wildfire-insurance-legal-response-2026.json)
advances the complaint-to-enforcement arrow without claiming adjudicated
liability, restitution, safe occupancy, or household recovery.

The same page links a [2025 Fire Rebuilding Power BI
dashboard](https://app.powerbigov.us/view?r=eyJrIjoiNzQ1YWIxN2UtNTFjZC00Yjg5LWE5YzctMzUwYWY3YjhjYTQ5IiwidCI6IjA3NTk3MjQ4LWVhMzgtNDUxYi04YWJlLWE2MzhlZGRiYWM4MSJ9)
and [metric definitions](https://file.lacounty.gov/SDSInter/dpw/recovery/1203584_2025FireRebuildingMetricDefinitions.pdf).
The dashboard is a promising public operational surface, but extraction must
first preserve its field definitions, refresh date, geography, suppression
rules, and export provenance. A dashboard count is not automatically a
property-level longitudinal record.

The California claims tracker was rechecked on 2026-09-29. Its displayed
figures remain 41,727 claims filed, 40,482 partially paid, and $25.2 billion
paid to date, with the page still marked updated July 6, 2026. This is a
freshness result, not a new recovery estimate: the claims surface remains
aggregate and stale relative to the current recheck date.

The first aggregate extraction has now been preserved in the [LA County
rebuilding dashboard record](../../records/us-la-county-fire-rebuilding-dashboard-2026.json)
and [stage-conversion memo](la-county-fire-rebuild-dashboard-stage-conversion-2026-09-29.md).
It reports damaged-unit/parcel estimates, construction-stage counts, county
occupancy-approval progress, displacement-assistance pressure, mobility, and
local spending indicators while leaving insurance payment adequacy, original-
household occupancy, and household mobility open.

## Join discipline

The next extraction may support geography- and time-bounded comparison among
fire, ZIP/census geography, permit status, debris-removal status, and claims
aggregates. It must not infer a household claim trajectory from a matching
address, parcel, or neighborhood unless the source explicitly establishes the
link and the use is lawful.

Required checks before any derived output:

1. preserve each source's date, geography, category definitions, and revision
   status;
2. distinguish destroyed, damaged, smoke-affected, and non-fire properties;
3. keep claims, policyholders, properties, permits, and households as separate
   denominators;
4. test whether permit records expose parcel identifiers, status dates, and
   completion/occupancy fields without protected personal information;
5. report missingness and unmatched records before calculating any rate; and
6. never label aggregate dollars paid or permits issued as household recovery.

## Highest-value next extraction

Start with one bounded geography—Altadena/Eaton or the Palisades—and build a
property-area ledger containing only public, non-sensitive fields:

```text
area/property reference -> damage or displacement status
  -> debris/removal status -> permit status/date
  -> public claims category and date context
  -> occupancy/rebuild indicator, if explicitly published
```

The first deliverable should be a coverage-and-timing table with unmatched
counts, not a recovery estimate. A stronger household result requires a lawful
claim or property panel that adds payment timing, repair completion, temporary
housing, mortgage continuity, and subsequent insurance status.

## Boundary

This route can tighten the operation-to-recovery middle without creating a
false same-household chain. It does not authorize scraping restricted systems,
obtaining insurer claimant data, re-identifying households, or combining
public records to infer protected personal information. Until a lawful linked
file exists, the atlas should describe this as a public property/place recovery
route with household recovery still open.
