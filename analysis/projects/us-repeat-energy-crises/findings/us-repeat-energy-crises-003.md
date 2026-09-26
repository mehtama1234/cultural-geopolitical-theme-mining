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
| Continued housing support | FEMA housing support extended through July 2027; California reported 35,000+ households assisted and $177M+ awarded by June 12, 2026 | Household-level payment, repair or permanent-housing completion, duration, adequacy, and later stability |
| Mortgage/insurance bridge | CalAssist reported 1,100+ homeowners assisted, up to 12 months of mortgage payments and up to $100,000; state urged timely release of insurance funds | Named-home payment, insurer/lender decision, rebuild completion, debt/coverage adequacy, return, and durable housing |

The ratios are descriptive ratios of published aggregate fields, not approval
rates for unique people and not estimates of recovery. HA and ONA categories
may overlap with IHP stages and should not be added to count unique survivors.

## Later persistence and continued housing need

California's June 2026 recovery update adds a later administrative stage:
FEMA approved continued housing support through July 2027 while survivors
rebuild. As of June 12, the state reported that more than 35,000 households
had received assistance and that more than $177 million had been awarded. A
January 2026 Cal OES notice also instructed survivors whose insurance living
expenses had ended, or who had received final insurance settlements but still
had unmet needs, to re-contact FEMA for continued rental assistance or repair
funds.

This is stronger than a one-time registration snapshot because it documents
continued assistance and residual need over time. It still does not show which
households received which amount, whether rental support ended in permanent
housing, whether repairs were completed, or whether the household's work,
health, debt, trust, and repeat-crisis position improved. Continued support is
therefore evidence of a long recovery clock, not proof that recovery failed or
was completed.

The July 2026 California long-term housing bulletin adds a financial-control
stage. It reports that more than 1,100 homeowners had received CalAssist
mortgage relief of up to 12 months, with a maximum of $100,000 and no repayment
required. It also records the Governor urging lenders to release insurance
proceeds promptly and warning that delays or denials can hinder rebuilding.
This shows that recovery depends not only on disaster assistance but also on
the timing and release of insurance and mortgage funds. It still does not show
that a named home was rebuilt, that insurance was paid, or that the household
returned to stable housing and work.

The September 2026 Recovery Support Functions bulletin adds a separate state-
capability clock: California launched the first three FireSat wildfire-
detection satellites, with a planned constellation of more than 50 by 2030.
The bulletin describes faster detection and improved situational awareness as
preparedness benefits, while the Long-Term Housing Recovery group continues
monthly coordination. These are not the same outcome. State capacity to detect
future fires can advance while households from the prior fire remain in rental,
insurance, mortgage, repair, or rebuilding limbo. The bulletin contains no
named-home completion, return, or survivor-wellbeing result, so prevention
capability must remain separate from present recovery.

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
- [California recovery update on FEMA extension](https://www.news.caloes.ca.gov/governor-newsom-welcomes-fema-extension-to-help-los-angeles-fire-survivors-continue-recovery/)
- [California notice on continued temporary housing assistance](https://www.news.caloes.ca.gov/continued-temporary-housing-assistance-still-available-for-la-survivors/)
- [California July 2026 Long-Term Housing Recovery bulletin](https://www.caloes.ca.gov/wp-content/uploads/Recovery/Documents/JULY-LTHR-4.pdf)
- [California September 2026 Recovery Support Functions bulletin](https://www.caloes.ca.gov/wp-content/uploads/Recovery/Documents/RSF-Bulletin-September-2026.pdf)

The retained artifact contains aggregate rows and derived ratios only. No
survivor identifiers, raw application file, payment file, or personally
identifying information was retained.

**Evidence status:** current aggregate delivery-stage finding; no survivor-level
payment, housing, repair, recovery, trust, or political-action estimate.
