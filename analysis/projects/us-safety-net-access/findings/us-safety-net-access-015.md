# SNAP transition reasons lead to distinct following-month food-security paths

**Status:** provisional official-universe Fay-BRR comparison  
**Checked:** 2026-09-16

## Bounded finding

The 2025 SIPP public-use file links a recorded month-to-month SNAP transition
reason to the following month’s food-security recode (`RFOODS`). Low or very
low food security is treated as `RFOODS=2` or `3`, with the official `AFOODS`
validity flag. This adds a direct food-security endpoint to the existing
housing and utility hardship reason layer.

| Transition and recorded reason | Valid food-security records | Low/very low food security |
|---|---:|---:|
| Entry: job loss/layoff or wages reduced | 50 | 22.94% (SE 6.38) |
| Entry: loss/reduction of other income | 30 | 20.14% (SE 9.66) |
| Entry: became disabled/unable to work | 21 | 31.73% (SE 14.51) |
| Entry: new child/dependent or pregnancy | 14 | 31.82% (SE 14.04) |
| Entry: other | 46 | 20.43% (SE 8.44) |
| Exit: ineligible because income increased | 53 | 25.69% (SE 7.38) |
| Exit: requirements not met | 7 | 44.51% (SE 20.48) |
| Exit: time limit reached | 10 | 23.28% (SE 14.25) |
| Exit: other | 78 | 14.20% (SE 4.40) |

The entry and exit reason categories are not equally precise. There were 437
observed no-SNAP-to-SNAP entry pairs and 387 SNAP-to-no-SNAP exit pairs, but
only 217 and 188 respectively had a classified reason. Food-security valid
records are smaller still. The table is therefore most useful for preserving
distinct routes and identifying the largest interpretable cells, not for
ranking program performance.

Pooling only the classified reason categories gives 26.12% low/very-low food
security after entry (188 valid records; SE 3.82) and 18.87% after exit (160
valid records; SE 3.51). This is not evidence that exit improved food
security: the entry and exit groups have different composition, reason mixes,
missingness, and unclassified-transition shares, and the food-security field
does not measure change from the pre-transition month.

## What this adds to the end-to-end chain

```text
SNAP entry or exit
  + recorded income, job, disability, family, or administrative reason
  -> following-month food-security condition
  -> benefit amount/timing, notice, effort, remedy, substitution, recovery,
     trust, and action
```

The reason-to-food-security arrow is an adjacent-month descriptive association
on identified person records with Fay-BRR uncertainty. It shows that receipt
entry and exit are not interchangeable states and that a recorded exit—even
one attributed to income increase—does not itself establish food security.

## Interpretation boundary

`RFOODS` is a household food-security recode attached to person records, not a
dated meal-level measure or proof that the SNAP transition caused hunger. The
following month is record order; it does not prove when a bill, benefit,
notice, or food shortage occurred. Recorded reasons do not identify notice
comprehension, application effort, benefit amount, timing, appeal, correction,
or case-level remedy. Household composition, prior food insecurity, health,
income, work, and survey selection can explain both transition reason and
outcome.

| Arrow | Status | Safe conclusion |
|---|---|---|
| Transition reason → following food-security status | Adjacent-month descriptive association | Food insecurity remains visible across several entry and exit routes; route profiles differ but small cells are uncertain |
| SNAP receipt → food-security improvement | Open | No causal counterfactual, benefit amount, or meal-level timing is observed |
| Exit or interruption → recovery, remedy, trust, action, or exit choice | Open | Requires a same-episode case ledger with notice, effort, amount, response, and follow-up |

## Reproduction

- [Reproduction audit](../sipp-snap-reason-outcome-reproduction-audit-2026-09-16.md)

The [machine-readable output](../data/us-sipp-snap-reason-following-food-hardship.json)
preserves the 379,215 primary rows, 378,291 replicate rows, 405 matched
classified transition pairs, classified-reason aggregate summaries, valid
denominators, and 240-replicate Fay-BRR intervals. The [analysis script](../../../../scripts/analyze_sipp_snap_reason_outcome_fay_brr.py)
also retains the prior rent/mortgage, utility, and compound-hardship outcomes;
this pass adds `RFOODS` with `RFOODS=2/3` as the positive food-security outcome.

## Next decisive test

Obtain a same-episode route ledger that records notice, application or renewal
effort, benefit amount and gap days, food acquisition or substitution, remedy,
and later recovery or institutional judgment. Until then, treat reason-specific
food-security cells as mechanism evidence with explicit missingness and not as
a causal SNAP or administrative-burden estimate.

## Official source

- [US Census SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2023-data/2023-panel.html)
- [SIPP SNAP reason and following-hardship layer](../sipp-snap-transition-reason-outcome-fay-brr-layer-v1.md)
