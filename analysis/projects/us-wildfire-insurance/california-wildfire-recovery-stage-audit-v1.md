# California wildfire recovery stage audit

Status: fifty-seventh active depth artifact; checked 2026-10-18.

## Purpose

The wildfire-insurance route asks whether a damaged household moves from
insurance availability and claim activity through payment, repair, safe
occupancy, stable housing, and later coverage choice. The public record now
contains aggregate claims, regulatory enforcement, county rebuilding
operations, displacement pressure, and survivor advocacy. This audit separates
those stages and records the current coverage gap.

## What we found

| Stage | Public evidence | Signal | Boundary |
|---|---|---|---|
| Market protection | California snapshot, December 2025/Q1 2026 | 8,300,730 private homeowner policies and 668,609 FAIR Plan homeowner/commercial policies; average California premium $1,571 versus $1,512 nationally | Policy counts and average premium do not show a named household's coverage, deductible, affordability, or renewal |
| Fire claim activity | California claims tracker rechecked September 29, 2026 | 41,727 claims filed, 40,482 partially paid, and $25.2 billion paid to date; displayed page remained at its July 6 update | Partial payment is not final adequacy, repair funding, safe occupancy, or household recovery |
| Claim correction | State Farm investigation and smoke-damage law | 398 violations across 114 reviewed claims; underpayment, delayed investigation, adjuster changes, smoke disputes, and communication problems were identified; statewide smoke-damage standards were enacted | Reviewed claims are not all claims; legal response is not payment receipt or repair completion |
| Public rebuilding pipeline | LA County dashboard refreshed September 29, 2026 | 7,417 estimated damaged/destroyed unincorporated units and 6,571 parcels; 1,752 construction-stage records, including 203 finaled/ready for certificate | Stage records, units, parcels, permits, and households have different denominators; finaled/ready is not occupied or affordable |
| Administrative throughput | Same dashboard | 4,052 applications, 3,811 building permits issued, 2,396 new residential projects in construction, and 217 completed; average 159.5 business days to permit issuance | These counts are not a common-denominator funnel and do not identify insurance payment or original household |
| Occupancy/recovery pressure | County DEO/LAEDC June 8, 2026 update | 26.7% of destroyed structures had rebuild permits, but 0.47% had completed reconstruction and occupancy approval; 38% of survivors had exhausted or were nearing exhaustion of displacement assistance | Aggregate county indicators do not identify why a property or household remains displaced |
| Place/economic consequence | Same county update | Metro routes most affected remained 17.7% below adjusted pre-fire baseline; estimated annual localized spending losses were $79M in Palisades and $73.6M in Eaton | Economic estimates are not household income, debt, housing, or insurance outcomes |
| Survivor voice and institutional response | EFSN public account rechecked September 2026 | 1,600 State Farm accounts reportedly helped power county litigation; EFSN claims 70% of survivors are still not home, roughly half took on new debt, and $100M-plus in stalled payments moved to families | Advocacy claims have no public sampling/weighting or respondent-level repair, payment, debt, or occupancy file |
| Future market choice | Department/insurer filings, September 2026 | State Farm and Allstate filed plans or rules to begin writing new policies, but both remained under review and were not yet open for new business | Filing is not an available, affordable, durable policy or household choice |

The strongest current result is a conversion gap. Insurance payment and public
rebuilding activity are visible before safe occupancy, stable housing,
displacement resolution, and renewed coverage are visible for the same unit.
The county's 0.47% occupancy-approval measure is not a household recovery rate;
it is a bounded aggregate indicator showing how far the operational pipeline
remains from the endpoint.

## Evidence ledger

| Arrow | Current evidence | Missing decisive field |
|---|---|---|
| Fire/damage → claim | Fire-area claims and damaged-unit/parcel estimates | Property-level damage type, policy status, claim ID, and household unit |
| Claim → payment | Filed, partially paid, and aggregate dollars-paid counts | Payment date, amount, deductible, advance/final status, adequacy, and recipient |
| Payment → repair | Permit applications, stages, finaling, and occupancy approval | Lawful claim-to-parcel link, construction financing, completion, safe occupancy, and household return |
| Displacement → stability | Displacement-assistance exhaustion and not-home advocacy claims | Temporary housing, mortgage continuity, rent/debt, move/stay decision, and duration |
| Complaint → correction | Regulatory investigation, violations, enforcement, law, and reported recovered dollars | Claimant-level correction, payment receipt, residual loss, repeat effort, and trust |
| Market reform → choice | Filings, mitigation standards, FAIR Plan and private-market reform | Actual policy offer, premium/deductible, acceptance, renewal, and alternative availability |
| Recovery → public meaning | Survivor litigation and bounded public discussion | Representative local participation, attributed burden, later acceptance/conflict, or political action |

## What this connects to

- **Household room:** insurance payment timing, displacement, debt, mortgage,
  and repair costs can move on different clocks.
- **Housing/place mobility:** safe return is not the same as permit progress;
  remaining away can reflect constraint rather than preference.
- **Institutional legitimacy:** complaints can generate enforcement while the
  affected household still lacks a usable or adequate remedy.
- **Infrastructure and local economy:** transit, spending, debris, and
  reconstruction shape the place-level recovery environment.
- **Climate/geopolitical risk:** insurance availability is a market and public
  backstop response to climate exposure, not proof that risk has been absorbed
  or fairly distributed.

## Deeper question

**When does a wildfire claim become a safe, affordable, and insurable return
home rather than an aggregate payment, permit, or enforcement milestone?**

This is high learning value because one bounded episode already contains the
major public stages and a clear endpoint gap. The next test can remain
geography-bounded and non-sensitive while checking whether public property and
permit fields can be aligned without re-identifying households.

## Bounded public discussion

Existing LinkedIn records discuss FAIR Plan dependence, wildfire claims,
climate displacement, and smoke-related household/work consequences. EFSN's
survivor advocacy adds a direct collective-action interpretation. These sources
make the public meaning and institutional-response arrow visible, but they are
not representative household recovery data.

## Challenge checks

- Claims, policyholders, properties, permits, units, and households were kept as
  separate denominators.
- Partial payments and aggregate dollars were not treated as adequate recovery.
- Permit issuance, construction stage, finaling, and occupancy approval were not
  treated as household return.
- Advocacy percentages and account counts were labeled source claims, not
  weighted estimates.
- Insurance filings were not treated as available or affordable policies.
- Aggregate county economic effects were not treated as individual welfare.

## Next test

Build a geography-bounded, non-sensitive ledger for Altadena/Eaton or Palisades:

```text
fire area/refresh date | public damage or displacement category | parcel/permit
reference if lawful | debris/removal status | permit stage/date |
occupancy/finaling indicator | claims category/date context | unmatched status |
local assistance/economic context | later public coverage or policy option
```

First report field definitions, refresh dates, suppression rules, denominators,
and unmatched counts. Do not calculate a recovery rate until the source proves
that the numerator and denominator share a unit and geography. A stronger
household claim requires an authorized claim/payment and repair or occupancy
link, not address matching inferred by the atlas.

## Stopping rule

Do not call wildfire insurance effective, recovery complete, or safe return
achieved from claims paid, permits issued, construction stages, occupancy
approval aggregates, complaint recovery, advocacy claims, or market filings
alone. Close this subtest only when one lawful compatible property/household
episode links damage to claim, payment, repair, occupancy, housing stability,
and later coverage choice—or when the source owner confirms those fields are
unavailable.

## Source links

- [California wildfire claims and smoke recovery](../../records/us-california-wildfire-claims-smoke-recovery-2026.json)
- [California FAIR Plan coverage and remedy](../../records/us-california-wildfire-insurance-fair-plan-coverage-remedy-2026.json)
- [LA County rebuilding dashboard](../../records/us-la-county-fire-rebuilding-dashboard-2026.json)
- [LA County insurance legal response](../../records/us-la-county-wildfire-insurance-legal-response-2026.json)
- [EFSN survivor advocacy record](../../records/us-efsn-survivor-insurance-advocacy-recovery-2026.json)
- [Household recovery acquisition map](california-household-recovery-acquisition-map-2026-09-29.md)
- [Wildfire/FAIR Plan discussion](../../social-discussions/records/atlas-batch-0042-fair-plan-linkedin-001.json)
- [Wildfire public discussion](../../social-discussions/records/atlas-batch-0047-wildfire-linkedin-001.json)
