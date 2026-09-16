# Utility difficulty to following-month care and household-security outcomes: SIPP bridge

**Checked:** 2026-09-15  
**Status:** adjacent-month Fay-BRR descriptive bridge; not a causal event estimate

## Question

Can the SIPP person-month spine place utility-payment difficulty and housing
tenure at month *t* beside childcare-related work prevention and household
security outcomes at month *t+1*? This is a stronger timing screen than a
single December cross-tab, but it is not yet a dated bill or shutoff episode.

```text
utility difficulty + tenure at month t
  -> annual fall childcare-work-prevention status at month t+1
  -> rent/mortgage hardship and food insecurity at month t+1
```

The child-care field is an annual fall reference-parent measure copied onto the
following-month record; it is not newly observed care time in month *t+1*.
Utility, mortgage, and food fields may also be reference-period measures that
appear on monthly person records. The arrow is therefore **adjacent in the
file**, not proof of a newly occurring household event.

## Design and integrity

The calculation uses the 2025 SIPP public-use file for the 2024 reference year.
It selects positive-weight people observed in both November and December,
conditions utility difficulty and tenure on November, and evaluates childcare
work prevention plus the two outcomes in December. November `WPFINWGT` and
November replicate weights define the pair estimate. Separate valid universes
are retained for mortgage hardship and `RFOODS` food security.

- 379,215 primary rows read
- 2,600 positive-weight November–December pairs identified
- 2,600 of 2,600 pair keys matched to `rw2025.csv`
- 240 Fay-BRR replicates, perturbation factor 0.5
- Person-pair unit; household fields remain repeated on person records

## Results

### Rent/mortgage hardship at month *t+1*

| Utility at *t* | Childcare prevented work at *t+1* | Tenure at *t* | n | Estimate | SE | Approx. 95% CI |
|---|---|---|---:|---:|---:|---:|
| Difficulty | No | Owner/buyer | 95 | 38.222% | 5.742 | 26.969–49.476 |
| Difficulty | No | Renter | 134 | 57.988% | 5.086 | 48.021–67.956 |
| Difficulty | Yes | Owner/buyer | 10 | 25.314% | 16.125 | 0–56.919 |
| Difficulty | Yes | Renter | 12 | 72.803% | 13.253 | 46.826–98.779 |
| No difficulty | No | Owner/buyer | 1,635 | 0.792% | 0.194 | 0.411–1.173 |
| No difficulty | No | Renter | 642 | 2.958% | 0.707 | 1.571–4.344 |
| No difficulty | Yes | Owner/buyer | 42 | 2.144% | 2.198 | 0–6.453 |
| No difficulty | Yes | Renter | 30 | 12.098% | 7.202 | 0–26.215 |

Among renters with utility difficulty at month *t*, the December mortgage-
hardship share is 72.803% in the tiny childcare-prevention cell versus 57.988%
without that report. The corresponding owner/buyer cells reverse direction,
25.314% versus 38.222%. The intervals are wide, and the table does not
identify whether utilities, care, housing, or an unobserved resource came
first.

### Food insecurity at month *t+1*

Here food insecurity means `RFOODS=2` or `3` (low or very low food security),
with `AFOODS` valid. It is not the same outcome as mortgage hardship.

| Utility at *t* | Childcare prevented work at *t+1* | Tenure at *t* | n | Estimate | SE | Approx. 95% CI |
|---|---|---|---:|---:|---:|---:|
| Difficulty | No | Owner/buyer | 95 | 49.350% | 6.955 | 35.717–62.983 |
| Difficulty | No | Renter | 134 | 50.209% | 4.897 | 40.610–59.808 |
| Difficulty | Yes | Owner/buyer | 10 | 77.500% | 12.689 | 52.631–100.000 |
| Difficulty | Yes | Renter | 12 | 64.642% | 15.696 | 33.877–95.407 |
| No difficulty | No | Owner/buyer | 1,635 | 4.599% | 0.584 | 3.454–5.744 |
| No difficulty | No | Renter | 642 | 18.025% | 1.774 | 14.549–21.501 |
| No difficulty | Yes | Owner/buyer | 42 | 12.471% | 5.213 | 2.254–22.688 |
| No difficulty | Yes | Renter | 30 | 25.748% | 8.183 | 9.709–41.786 |

The food-security surface points in the same general direction for the tiny
renter/difficulty cell—64.642% versus 50.209%—but the interval for the
prevention cell is 33.877–95.407%. The owner/buyer prevention cell is also
small. These are not precise evidence of a childcare-related food-security
difference.

The within-stratum contrasts, calculated from the same replicate-level
estimates, are:

| Utility at *t* | Tenure at *t* | Outcome | Prevention minus no prevention | SE | Approx. 95% CI |
|---|---|---|---:|---:|---:|
| Difficulty | Renter | Mortgage hardship | +14.814 pp | 13.766 | −12.167 to +41.796 |
| Difficulty | Renter | Food insecurity | +14.433 pp | 16.728 | −18.355 to +47.220 |
| Difficulty | Owner/buyer | Mortgage hardship | −12.908 pp | 17.075 | −46.375 to +20.559 |
| Difficulty | Owner/buyer | Food insecurity | +28.150 pp | 14.295 | +0.132 to +56.168 |
| No difficulty | Renter | Mortgage hardship | +9.141 pp | 7.202 | −4.975 to +23.256 |
| No difficulty | Renter | Food insecurity | +7.723 pp | 8.106 | −8.164 to +23.610 |
| No difficulty | Owner/buyer | Mortgage hardship | +1.352 pp | 2.197 | −2.954 to +5.659 |
| No difficulty | Owner/buyer | Food insecurity | +7.872 pp | 5.183 | −2.288 to +18.031 |

The renter/difficulty contrasts both include zero. The owner/buyer/difficulty
food contrast has a lower bound barely above zero, but it is based on only 10
prevention records and a 14.295-point standard error; it should be treated as
a sparse-cell diagnostic, not as a stable difference. Across outcomes, the
most defensible conclusion is that the temporal screen identifies a plausible
joint-constraint hypothesis and a non-monotonic tenure counterexample, not a
resolved care-to-hardship effect.

### Resource-band movement at month *t+1*

The same pair design also compares the November and December monthly
income-to-poverty bands. `changed` means any four-band crossing; `improved`
means an upward crossing and `worsened` a downward crossing. These are
threshold movements, not continuous income changes or household recovery.

| Utility at *t* | Care prevention at *t+1* | Tenure | n | Changed | Improved | Worsened |
|---|---|---|---:|---:|---:|---:|
| Difficulty | No | Owner/buyer | 95 | 2.724% (SE 1.703) | 0.000% (SE 0.000) | 2.724% (SE 1.703) |
| Difficulty | No | Renter | 134 | 5.563% (SE 2.184) | 3.093% (SE 1.772) | 2.470% (SE 1.440) |
| Difficulty | Yes | Owner/buyer | 10 | 8.446% (SE 9.014) | 0.000% (SE 0.000) | 8.446% (SE 9.014) |
| Difficulty | Yes | Renter | 12 | 18.956% (SE 15.779) | 0.000% (SE 0.000) | 18.956% (SE 15.779) |
| No difficulty | No | Owner/buyer | 1,635 | 4.031% (SE 0.677) | 2.586% (SE 0.572) | 1.445% (SE 0.396) |
| No difficulty | No | Renter | 642 | 5.795% (SE 1.329) | 3.408% (SE 1.089) | 2.387% (SE 0.611) |
| No difficulty | Yes | Owner/buyer | 42 | 1.051% (SE 1.138) | 1.051% (SE 1.138) | 0.000% (SE 0.000) |
| No difficulty | Yes | Renter | 30 | 13.423% (SE 6.709) | 4.821% (SE 4.532) | 8.603% (SE 5.514) |

The high renter/difficulty movement in the prevention cell is a useful
follow-up question, not a recovery finding: its approximate 95% interval for
any change is 0–49.881%, and every movement in that cell is downward. A
threshold crossing can reflect a small change near a cutoff, reporting or
annualization, and the SIPP slice does not expose the dated bill, dollar
amount, or reason for movement. The resource surface therefore adds a
possible sacrificed-outcome screen while preserving both upward and downward
counterexamples.

## What this adds

The bridge advances the end-to-end map by adding an explicit adjacent-month
ordering and two household-security endpoints to the joint-constraint screen:

| Arrow | Status | Boundary |
|---|---|---|
| Utility difficulty at *t* → next-month housing/food surface | Ordered descriptive screen | Reference-period fields may be repeated; no bill date or shock |
| Care-related work prevention → next-month hardship | Co-observed on the following record | Annual fall care measure is not a new monthly event |
| Tenure conditions the surface | Descriptive comparison | No composition adjustment; tenure is not a treatment |
| Pressure → protected or sacrificed outcome | Open/diagnostic | No causal identification, detailed time substitution, provider route, or dollar-level recovery; resource-band movement is a threshold screen |
| Outcome → recovery, trust, action, or exit | Open | No later follow-up or meaning/action measure |

The useful result is not a new burden index. It is evidence that a bounded
same-person frame can test joint constraints with design-based uncertainty,
while still showing why the missing middle matters: a dated trigger,
alternatives, care intensity, schedule control, and a later outcome.

## Counterexamples and limits

- People with no reported utility difficulty still show childcare constraints
  and hardship; utility difficulty is not the only route to insecurity.
- Renters and owners/buyers differ in resources, family composition, health,
  work, geography, and access to support. The contrast is not a tenure effect.
- A zero-weight November record can appear in the primary slice but cannot
  contribute to a weighted pair estimate; the estimator excludes it and
  requires complete replicate-key matching.
- `EAWBGAS` is not a bill amount, arrears, shutoff, reconnection, or assistance
  decision. `EWORKMORE` is not care hours, missed shifts, or provider quality.
- The person weight is not a household weight. Household outcomes repeated on
  person records must not be reported as household counts without a household
  selection rule.

## Decisive next test

Acquire a dated utility bill, shutoff warning, payment-plan enrollment, or
energy-assistance decision and link it to the same person/family at one-,
three-, and six-month follow-up. Add paid and unpaid care time, provider and
payment support, work schedule and earnings, food and housing outcomes,
health, and a documented recovery or institutional response. The required
counterexample is comparable exposure with protected outcomes because of a
payment intervention, flexible work, nearby care, family support, or a
substitute provider.

## Reproduction

- [Machine-readable output](data/sipp-utility-care-following-outcomes-2024.json)
- [Reproduction script](../../../scripts/analyze_sipp_utility_care_following_outcomes.py)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [Official 240-replicate archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)

The primary slice SHA-256 is
`4fe7395d4ecdb2f1a3f2879a394f47d1e809c9bdef3960b60543919b79a61eda`; the
replicate archive SHA-256 is
`3bf35c17723de10697d581d1122fda4d7cdecb34c6f9e9dfcb18ddc561c7c6b6`.

**Evidence status:** replicate-weighted adjacent-month descriptive bridge;
no causal bill effect, household-weighted prevalence, recovery, trust,
political-action, remedy, or exit claim.
