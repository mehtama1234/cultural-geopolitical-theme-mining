# Utility difficulty and energy assistance beside following-month food insecurity

**Status:** same-person adjacent-month Fay-BRR descriptive layer; not a causal assistance estimate  
**Checked:** 2026-09-16  
**Unit:** identified SIPP person-month pair, exposure screen at month *t* and food-security status at month *t+1*  
**Source:** 2025 SIPP public-use file, 2024 reference year

## Result

The existing local SIPP slice can place utility-payment difficulty and energy-
assistance status beside a following food-security measure for the same
identified person-month pair. The weighted screen finds substantially higher
following food insecurity among reported utility-difficulty pairs than among
no-difficulty pairs. Energy-assistance recipients also have higher following
food insecurity than the no-assistance comparison, but that contrast is
strongly subject to targeting and pre-existing need.

| Month-*t* screen | Eligible pairs | Following food insecurity | Fay-BRR SE | Approx. 95% CI |
|---|---:|---:|---:|---:|
| Utility-payment difficulty | 24,297 | 51.13% | 2.27 pp | 46.68–55.58% |
| No utility-payment difficulty | 321,986 | 8.40% | 0.33 pp | 7.76–9.05% |
| Energy assistance | 13,399 | 32.76% | 2.90 pp | 27.07–38.45% |
| No energy assistance | 178,141 | 16.93% | 0.61 pp | 15.74–18.13% |

These are conditional person-weighted shares with separate field-specific
universes. The utility contrast is a material-pressure surface; the
assistance contrast is a public-support/need surface. Neither says that a
utility condition caused food insecurity or that assistance failed. Assistance
may be more common precisely among households facing greater or more persistent
need.

## What this adds to the broad program

It strengthens the material → public-system → household-security branch with a
same-person adjacent-file screen:

```text
utility difficulty or energy assistance at month t
  → following food-security status at month t+1
  → [open] bill amount, benefit adequacy, recovery, trust, action, or exit
```

The result is more temporally organized than a single cross-tab, but the SIPP
dictionary and file design require caution. Utility and assistance fields are
conditional household/reference-period measures that can repeat on monthly
person records. Food security is also a reference-period measure, not
necessarily a newly occurring event in the following month. The screen is
therefore adjacent in the file, not a dated bill or assistance episode.

## Boundaries and counterexamples

- The 2024 reference year does not identify the exact bill, amount, shutoff
  threat, provider, application, notice, or assistance decision date.
- The assistance comparison is not a treatment/control design. Eligibility,
  need, geography, health, season, and household composition may explain the
  difference.

## Joint burden and assistance screen

Conditioning both screens together shows that assistance is concentrated in
the higher-need surface rather than removing the food-security gradient:

| Utility condition at *t* | Energy assistance at *t* | Eligible pairs | Following food insecurity | Fay-BRR SE | Approx. 95% CI |
|---|---|---:|---:|---:|---:|
| Difficulty | Yes | 3,772 | 61.73% | 5.66 pp | 50.62–72.83% |
| Difficulty | No | 16,879 | 53.81% | 2.79 pp | 48.34–59.28% |
| No difficulty | Yes | 9,627 | 20.99% | 2.71 pp | 15.68–26.29% |
| No difficulty | No | 161,262 | 13.08% | 0.54 pp | 12.01–14.15% |

Within both utility strata, the assistance group has higher following food
insecurity. The most defensible reading is selection/targeting and incomplete
need protection: assistance reaches households with greater underlying need,
and receipt does not imply that food security was restored. This joint screen
is a counterexample to interpreting the unconditioned assistance contrast as a
program failure or effect.

## Severity within the joint screen

The broad food-insecurity indicator also separates the three observed food-
security categories. The joint difficulty-and-assistance cell is not merely
slightly more insecure: its weighted distribution is concentrated in the low
and very-low categories.

| Utility condition at *t* | Energy assistance at *t* | High or marginal | Low | Very low |
|---|---|---:|---:|---:|
| Difficulty | Yes | 38.27% (SE 5.66 pp) | 24.83% (SE 4.61 pp) | 36.89% (SE 5.70 pp) |
| Difficulty | No | 46.19% (SE 2.79 pp) | 27.63% (SE 2.71 pp) | 26.18% (SE 2.34 pp) |
| No difficulty | Yes | 79.01% (SE 2.71 pp) | 11.43% (SE 2.12 pp) | 9.55% (SE 1.72 pp) |
| No difficulty | No | 86.92% (SE 0.54 pp) | 8.67% (SE 0.46 pp) | 4.40% (SE 0.33 pp) |

The most decision-relevant descriptive contrast is the very-low category:
36.89% in the difficulty-plus-assistance cell versus 4.40% in the neither-
screen cell. This does not identify assistance as the cause of severity. It
does establish that a broad assistance receipt flag should not be treated as
evidence of restored household security; targeting, incomplete adequacy, and
persistent material pressure remain live explanations.
- Person-month rows repeat household fields and are not household-prevalence
  estimates; food-security validity is retained separately from exposure
  validity.
- A household may receive assistance and remain food insecure, while another
  household may avoid utility difficulty through savings, family help,
  delayed payment, reduced use, or an unmeasured alternative.
- The layer contains no attribution, institutional trust, political action,
  verified remedy, recovery, switching, or exit outcome.

The decisive next step remains a dated utility or assistance episode with
notice, payment/benefit timing, alternative route, work/care trade-off, food
and health outcome, and a defined recovery follow-up.

## Reproduction

```text
python3 scripts/analyze_sipp_energy_assistance_food_following.py \
  --primary /tmp/us-broad-sipp-2025/full-v18/sipp-household-slice.csv \
  --replicate-zip /tmp/rw2025_csv.zip \
  --output /tmp/sipp-energy-assistance-food-following-v18-severity.json
```

- [Machine-readable record](../../records/us-sipp-energy-assistance-food-following-2024.json)
- [Aggregate output](data/sipp-energy-assistance-food-following-2024.json)
- [SIPP utility-to-work finding](findings/us-household-calendar-integration-028.md)
- [Official 2025 SIPP data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)

**Evidence status:** estimated same-person adjacent-month descriptive transition
with Fay-BRR uncertainty; no causal assistance, food-recovery, trust, or
political-action claim is made.
