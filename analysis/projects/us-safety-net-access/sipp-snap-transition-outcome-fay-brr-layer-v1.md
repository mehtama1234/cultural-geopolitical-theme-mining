# SIPP SNAP transition × following material hardship: Fay-BRR layer v1

**Checked:** 2026-09-13
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file; 2024 reference year
**Unit:** identified person, adjacent reference-month pair
**Weight:** `WPFINWGT` from month *t*; `REPWGT1`–`REPWGT240` for variance
**Method:** Fay BRR with `G=240` and perturbation factor `0.5`; descriptive only

## Question

Does material hardship reported in month *t+1* differ across observed SNAP
receipt transitions from month *t* to month *t+1*?

```text
SNAP state at t -> SNAP state at t+1
  -> rent/mortgage or utility hardship reported in t+1
```

This adds a time-ordered material outcome to the public-system layer. It does
not estimate what SNAP caused. The transition groups differ in need,
eligibility, household composition, reporting, and other shocks, and the
hardship variables have their own universes and reference-period limitations.

## Results

The primary slice contained 379,215 person-month rows. The calculation matched
all 346,283 valid adjacent transition pairs to the replicate-weight file. The
table reports the weighted share with a valid code-1 hardship report in the
second month; parentheses are Fay-BRR standard errors in percentage points.

| SNAP transition | Valid pairs | Unable to pay rent/mortgage | Unable to pay utility bills |
|---|---:|---:|---:|
| No → No | 312,418 | 3.86% (0.24), 95% CI 3.39–4.33 | 5.86% (0.31), 95% CI 5.25–6.46 |
| No → Yes | 437 | 16.40% (3.61), 95% CI 9.32–23.48 | 20.80% (3.49), 95% CI 13.96–27.63 |
| Yes → No | 387 | 11.53% (3.14), 95% CI 5.38–17.69 | 20.83% (4.41), 95% CI 12.19–29.46 |
| Yes → Yes | 33,041 | 11.98% (1.13), 95% CI 9.76–14.20 | 18.61% (1.38), 95% CI 15.90–21.32 |

## What the comparison says—and does not say

The entry group has a substantially higher following-month hardship share than
the stable nonreceipt group in both measures. That is consistent with SNAP
entry occurring amid material pressure, but it is not evidence that SNAP
caused the hardship. It may also reflect the fact that the program is reached
by people already facing rent, mortgage, or utility trouble.

The exit group is the important counterexample to a success narrative. Its
following-month mortgage-hardship share is lower than the entry group's, but
still well above stable nonreceipt; its utility-hardship share is essentially
the same as the entry group's within the wide intervals. Exit therefore cannot
be read as restored household security. It may represent higher income, a
time-limit or renewal process, non-collection, family change, reporting change,
or a different unobserved shock.

Continued receipt is also not equivalent to security: the yes → yes group has
11.98% rent/mortgage hardship and 18.61% utility hardship in the following
month. Receipt and material protection are separate stages.

## Public-system interpretation

This strengthens the stage map:

```text
need / material pressure
  -> receipt transition
  -> hardship may remain, rise, or differ by bill
  -> notice, route, amount, timing, and remedy still need measurement
  -> trust, blame, public action, and policy response remain open
```

The two hardship measures also should not be collapsed. A household may be
unable to pay utilities while keeping rent or mortgage current, or may face
both. The system can be helping one part of the budget while leaving another
exposure unresolved.

## Limits and reproduction

- The records are person-month observations and may represent covered members
  of a SNAP unit; they are not household benefit amounts or complete benefit
  spells.
- The hardship outcome is measured in the second month, but the SIPP field
  documentation gives these questions their own universe and reference-period
  structure. “Following month” is the record order, not proof that a new bill
  arrived after the transition.
- Entry and exit are rare in the full valid-pair frame, so their intervals are
  wide and their composition is selected.
- The calculation observes no notice comprehension, application effort,
  benefit amount, appeal, correction, food quantity, health, debt, dignity,
  trust, complaint, turnout, vote, or agency response for the same episode.
- Fay-BRR intervals describe sampling uncertainty; they do not remove
  transition selection or establish program impact.

Reproduction:

```text
python3 scripts/analyze_sipp_snap_transition_outcomes_fay_brr.py \
  --primary /tmp/us-broad-sipp-2025/full-v13/sipp-household-slice.csv \
  --replicate-zip /tmp/us-broad-sipp-2025/rw2025_csv.zip \
  --output /tmp/us-broad-sipp-2025/full-v13/sipp-snap-transition-outcomes-fay-brr.json
```

The raw files and derived JSON remain outside the repository. The reusable
analysis script is [analyze_sipp_snap_transition_outcomes_fay_brr.py](../../../scripts/analyze_sipp_snap_transition_outcomes_fay_brr.py).

The four transition observations are preserved in the machine-readable [trend
record](../../records/us-sipp-snap-transition-following-hardship-2024.json),
including Fay-BRR standard errors and 95% intervals for both hardship measures.
The retrieval hash covers this committed analysis memo because the raw SIPP
files and derived JSON are not committed.

## Next event-level test

For a valid same-episode design, add notice date and channel, effort, deadline,
decision, benefit amount and timing, interruption, appeal, correction, food
and housing result, perceived fairness, trust, complaint, and later recovery.
Keep eligible non-applicants and exits without improvement as counterexamples.
