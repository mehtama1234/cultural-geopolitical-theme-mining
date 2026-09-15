# Utility difficulty, tenure, and next-month work movement v1

**Status:** full-file same-person SIPP conditional comparison  
**Checked:** 2026-09-15  
**Source:** 2025 SIPP public-use file, 2024 reference period  
**Unit:** person-month pair; utility and tenure at month *t*, work movement at
month *t+1*  
**Method:** `WPFINWGT` with 240 Fay-BRR replicate weights, `G=240`,
perturbation factor `0.5`

## Why this pass matters

The earlier utility-to-work screen showed that utility-payment difficulty and
energy assistance sit beside different next-month earnings and hours surfaces.
This pass adds housing tenure as a moderator without treating it as a cause.
It asks whether the work-transition surface differs for renters and
owners/buyers inside the same reported utility condition.

```text
utility-payment condition + housing tenure at month t
        -> earnings and hours movement at month t+1
        -> household room, care, housing, and recovery [open]
```

The result closes only the middle descriptive transition. It does not observe
the exact bill, shutoff threat, work decision, desired hours, care substitution,
or later housing or political outcome.

## Results

Percentages are person-weighted conditional shares. Earnings and hours retain
separate valid-pair universes; parentheses contain Fay-BRR standard errors in
percentage points.

| Utility condition at *t* | Tenure | Eligible pairs | Earnings changed at *t+1* | Hours changed at *t+1* |
|---|---|---:|---:|---:|
| Difficulty | Owned/bought | 11,674 | 80.48% (1.68) | 7.61% (0.71) |
| Difficulty | Rented | 11,871 | 82.46% (1.43) | 7.58% (0.64) |
| No difficulty | Owned/bought | 233,998 | 84.37% (0.29) | 4.93% (0.13) |
| No difficulty | Rented | 81,964 | 83.47% (0.54) | 5.96% (0.24) |

The work-change contrast is more visible by utility condition than by tenure
inside the difficulty cells. Hours changed in roughly 7.6% of both renter and
owner/buyer difficulty pairs, compared with 4.9% among owners/buyers without
reported difficulty and 6.0% among renters without it. Earnings movement is
high in all cells and has wider uncertainty in the difficulty cells.

This is not evidence that utility difficulty caused hours movement. It is a
conditioned descriptive surface showing that the housing moderator does not
turn the result into a simple renter-versus-owner story.

## Measurement and uncertainty

The full primary slice contains 379,215 rows and 31,271 identified person
units after the field and validity filters. The replicate archive contains
378,291 rows, with 153,979 rows matched to the transition keys used by this
analysis. The key is `SSUID + PNUM + SPANEL + SWAVE + MONTHCODE`.

The utility field is a reported household/reference-person condition. It is
repeated on person-month rows according to the SIPP file design; it is not a
newly observed bill event in each month. `ETENURE=1` means owned or being
bought, and `ETENURE=2` means rented. Rent-free tenure is not promoted here
because the comparison is intended to retain the two larger, interpretable
tenure groups.

The hours and earnings outcomes use separate valid pair counts:

- utility difficulty, owned/bought: earnings `n=4,414`; hours `n=4,508`;
- utility difficulty, rented: earnings `n=4,638`; hours `n=4,738`;
- no difficulty, owned/bought: earnings `n=104,742`; hours `n=105,911`;
- no difficulty, rented: earnings `n=38,614`; hours `n=38,801`.

The estimates are not household prevalence rates. Person weights are used for
the person-month transition; household fields repeat across people and should
not be read as independent household observations.

## What this adds to the atlas

1. **Utility-to-work movement can be conditioned on tenure.** This is a more
   precise option-set screen than comparing utility difficulty alone.
2. **Tenure does not supply a single mechanism.** Within reported difficulty,
   renter and owner/buyer hours-change estimates are close; outside difficulty,
   their surfaces differ modestly.
3. **Hours movement remains an incomplete outcome.** It does not reveal
   desired hours, job quality, wage rate, schedule control, or whether a change
   was relief or constraint.
4. **Housing and energy remain linked but distinct.** Tenure may proxy for
   local prices, repairs, insurance, family support, provider reach, or job
   composition; the SIPP transition does not identify which.

## Counterexamples and boundaries

- A renter with unchanged hours may still lose food, savings, health, or care
  room to pay a utility bill.
- An owner with changing hours may be responding to a job or seasonal pattern,
  not utility difficulty.
- A higher earnings-change share does not mean improved security; earnings can
  rise or fall while hours remain unchanged.
- Energy assistance may be targeted to households already facing greater need;
  the comparison cannot estimate assistance effectiveness.
- Utility difficulty is not a dated bill, shutoff, reconnection, health event,
  or political interpretation.

## Next decisive test

The next SIPP pass should retain this tenure split and add a defensible time or
care field only where its official universe is compatible. `ETIMELOST` and
`ATIMELOST` are conditional annual child-care measures and cannot be promoted
as monthly utility-response time. A stronger design would pair a dated bill or
shutoff event with work schedule, unpaid care, health, housing, and a defined
one-, three-, or six-month recovery window.

## Reproduction

```text
python3 scripts/analyze_sipp_utility_work_tenure.py \
  --primary /tmp/us-broad-sipp-2025/full-v16/sipp-household-slice.csv \
  --replicate-zip /tmp/us-broad-sipp-2025/rw2025_csv.zip \
  --output /tmp/us-broad-sipp-2025/full-v16/utility-work-tenure.json
```

The [machine-readable record](../../records/us-sipp-utility-work-tenure-following-2024.json)
preserves the full-file and replicate-archive hashes. The [parent utility/work
reproduction audit](sipp-utility-work-following-reproduction-audit-2026-09-14.json)
preserves the unconditioned comparison.

**Evidence status:** estimated same-person monthly conditional transition with
design-based uncertainty. No causal utility, tenure, household-security,
health, care, trust, political-action, or geopolitical claim is made.
