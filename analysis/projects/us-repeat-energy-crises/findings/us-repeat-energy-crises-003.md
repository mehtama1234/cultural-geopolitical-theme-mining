# Finding 003: FEMA assistance visibility is stronger than survivor recovery visibility

**Status:** provisional current OpenFEMA aggregate delivery finding · **Checked:** 2026-09-19

## The bounded finding

The live FEMA OpenFEMA Registration Intake and Individuals Household Program
dataset provides a current aggregate view for the 2025 Los Angeles County
wildfires (disaster 4856). Across 621 city/ZIP rows, it reports 261,117 valid
registrations, 98,459 IHP referrals, 35,165 IHP-eligible records, and
$182.8 million in IHP amounts. The same rows report separate Housing
Assistance and Other Needs Assistance stages.

The safe conclusion is:

> FEMA's public data can show where registration, referral, eligibility, and
> reported assistance amounts stand for a disaster, but it still does not show
> whether a particular survivor received an adequate payment, completed a
> repair, obtained stable housing, or recovered later.

## Chain under test

```text
wildfire damage and displacement
  -> registration and channel use
  -> IHP referral and eligibility decision
  -> award/payment, repair, or housing placement
  -> usable housing and material recovery
  -> next need, repeat crisis, trust, complaint, or political action
```

The API is an aggregate geography/program surface, not a survivor panel. The
referral and eligibility fields describe different stages and should not be
read as a single person-level funnel without identifiers and stage timing.

## Evidence comparison

| Stage | Current observation | Still missing |
|---|---|---|
| Registration | 261,117 valid registrations across 621 city/ZIP rows | Damage severity, household composition, insurance, duplicate/linked applications, and survivor follow-up |
| IHP referral | 98,459 referrals, or 37.71% of valid registrations in this aggregate snapshot | Referral reason, timing, channel sequence, appeal, and whether the same registrant later received assistance |
| IHP eligibility | 35,165 eligible records, or 35.72% of IHP referrals | Decision explanation, correction, payment issuance, receipt, adequacy, and unmet loss |
| Housing assistance | 74,609 HA referrals; 5,653 HA-eligible records; $81.27M reported HA amount | Placement, repair, rent/lodging outcome, completion, duration, and stable housing |
| Other needs assistance | 94,152 ONA referrals; 35,083 ONA-eligible records; $101.50M reported ONA amount | Need type, timing, payment receipt, protected outcome, and repeat need |

The ratios are descriptive ratios of published aggregate fields, not approval
rates for unique people and not estimates of recovery. HA and ONA categories
may overlap with IHP stages and should not be added to count unique survivors.

## What this adds to the atlas

1. **Administrative visibility can be precise without being lived recovery.**
   FEMA exposes a much sharper registration/referral/eligibility surface than
   the broad GAO total alone, but the endpoint remains an administrative one.
2. **Eligibility is not payment.** A record classified as eligible does not
   establish issuance, receipt, amount adequacy, or completed repair/housing.
3. **Geography does not create a household panel.** City and ZIP rows support
   place-conditioned delivery diagnostics, not survivor-level causal or
   recovery claims.
4. **The missing middle is now explicit.** The next useful file would preserve
   a lawful applicant key and timestamps through decision, payment, repair or
   placement, and later housing/work/health status.

## Counterexamples and limits

- A low referral-to-registration ratio can reflect eligibility rules, incomplete
  referral, duplicate or invalid records, different program universes, or timing;
  it is not automatically exclusion or failure.
- An eligible record may later receive a payment, repair, or housing placement;
  the public aggregate snapshot simply does not expose that linkage.
- Assistance amounts are program-reported totals, not average survivor awards
  and not proof that losses were covered.
- A city/ZIP row can contain heterogeneous damage, insurance, income, housing,
  language, and access conditions.

## Next decisive FEMA test

Acquire or obtain a lawful de-identified applicant-level follow-up that links:

```text
disaster and damage
  -> registration channel and effort
  -> referral, eligibility, appeal, and decision reason
  -> payment/placement/repair and receipt
  -> housing/work/health status and residual loss
  -> repeat need, trust, complaint, or action
```

Until that exists, use the API for delivery geography and stage diagnostics,
not a survivor recovery rate.

## Provenance and storage boundary

- [OpenFEMA RI-IHP dataset description](https://www.fema.gov/es/node/696709)
- [Current filtered API snapshot](../data/fema-la-wildfire-ihp-api-snapshot-2026-09-19.json)
- [GAO FEMA assistance review](https://www.gao.gov/products/gao-26-108154)

The retained artifact contains aggregate rows and derived ratios only. No
survivor identifiers, raw application file, payment file, or personally
identifying information was retained.

**Evidence status:** current aggregate delivery-stage finding; no survivor-level
payment, housing, repair, recovery, trust, or political-action estimate.
