# SIPP utility difficulty and reported childcare time lost: a sparse endpoint gate

**Checked:** 2026-09-15  
**Status:** conditional time-loss acquisition diagnostic; not a burden estimate

## Why this gate matters

The broader SIPP bridge uses `EWORKMORE`, which records whether childcare
arrangements prevented work or more work. The more direct `ETIMELOST` field
reports a childcare-related work-time-loss amount, but only within the
`EWORKMORE=1` conditional universe. This gate tests whether that time measure
can be linked to utility difficulty and tenure at the preceding month.

```text
utility difficulty + tenure at November t
  -> childcare prevented work at December t+1
  -> reported childcare-related work time lost at t+1
```

This is an adjacent-month file ordering, not proof that a November utility
event caused December time loss. The care question refers to the fall
reference year and is not a newly observed diary measure.

## Integrity and universe

The calculation uses the 2025 SIPP public-use file for the 2024 reference year,
selects positive-weight people present in both November and December, applies
valid `EAWBGAS`/`AAWBGAS`, tenure, `EWORKMORE`/`AWORKMORE`, and
`ETIMELOST`/`ATIMELOST` conditions, and matches the November pair key to the
official 240-replicate file.

- 379,215 primary rows read
- 27 positive-weight eligible pairs
- 27/27 replicate rows matched
- `ETIMELOST` values retained as numeric hours from 0 through 168
- Fay-BRR standard errors use 240 replicates and perturbation factor 0.5

The small count is the result, not a reason to relax the conditional universe.
Records without a valid time-loss field are not recoded as zero.

## Conditional descriptive output

| Utility condition at *t* | Tenure at *t* | Eligible pairs | Weighted mean reported hours lost | SE | Approx. 95% CI |
|---|---|---:|---:|---:|---:|
| Difficulty | Owner/buyer | 4 | 1.000 | 0.000 | 1.000–1.000 |
| Difficulty | Renter | 3 | 1.515 | 0.315 | 0.898–2.132 |
| No difficulty | Owner/buyer | 12 | 1.232 | 0.118 | 1.001–1.464 |
| No difficulty | Renter | 8 | 1.487 | 0.185 | 1.124–1.850 |

These means should not be interpreted as the average childcare burden of
owners, renters, or households. They describe the selected respondents who
reported both work prevention and a valid time-loss amount. The four-record
difficulty owner cell has no observed replicate dispersion in this calculation,
which does not make it precise or representative.

The time-loss field therefore adds a direct time-sacrifice endpoint but also
reveals a severe selection boundary: it cannot supply a stable comparison with
people whose childcare did not prevent work, because the official universe
does not ask the same time-loss question of that group.

## Arrow status

| Arrow | Status | Boundary |
|---|---|---|
| Utility difficulty at *t* → childcare work prevention at *t+1* | Conditional descriptive screen | Reference-period care field; no dated bill or event |
| Care work prevention → hours lost | Observed only among conditional respondents | No-prevention comparison universe is unavailable |
| Utility difficulty → hours lost | Open | No causal identification and only 7 difficulty pairs |
| Time loss → housing/food/resource outcome | Open | This gate does not establish later security or recovery |
| Time loss → health, trust, action, or exit | Open | No such follow-up fields in the local SIPP slice |

## Counterexamples and limits

- Utility difficulty is not an amount, arrears, shutoff, reconnection, or
  assistance decision.
- `ETIMELOST` is a fall-reference-year childcare measure and should not be
  called a December work absence or diary total.
- A conditional mean among `EWORKMORE=1` respondents is not a population mean
  across all parents or workers.
- Tenure groups differ in composition and are not treatment/control groups.
- The direct time-loss endpoint is too sparse for fine subgroup ranking,
  causal inference, or a general claim about renters and owners.

## Decisive next test

The stronger design must collect or identify a dated care-provider failure,
utility bill/shutoff/assistance event, work schedule, and time-loss follow-up
for the same person or family. It should observe both prevented and protected
cases, retain paid and unpaid care, and measure whether flexible work, family
support, payment help, or a substitute provider prevented time loss.

## Reproduction

- [Machine-readable output](data/sipp-utility-time-loss-following-2024.json)
- [Reproduction script](../../../scripts/analyze_sipp_utility_time_loss.py)
- [SIPP 2025 public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP replicate archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)

Primary slice SHA-256:
`4fe7395d4ecdb2f1a3f2879a394f47d1e809c9bdef3960b60543919b79a61eda`.
Replicate archive SHA-256:
`3bf35c17723de10697d581d1122fda4d7cdecb34c6f9e9dfcb18ddc561c7c6b6`.

**Evidence status:** sparse conditional Fay-BRR time-loss diagnostic; no
population care burden, causal utility effect, recovery, trust, political
action, remedy, or exit claim.
