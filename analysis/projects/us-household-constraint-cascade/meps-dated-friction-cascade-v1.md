# MEPS dated event plus institutional-friction cascade v1

**Checked:** 2026-09-16  
**Status:** strict inter-round descriptive screen; not causal and not a remedy estimate  
**Machine output:** [dated friction cascade data](data-meps-dated-friction-cascade-2024.json)

## Question

Among people with a first observed office, ER, or inpatient event strictly
between the R3/1 and R4/2 endpoint months, do reported denial or
prior-authorization delays co-occur with different same-person care-delay,
bill, debt, and collector-contact context?

```text
first dated event in a strict inter-round window
  + reported denial/prior-authorization friction
  -> reported care delay, bill problem, debt, and collector contact
```

This is a sharper local test than comparing the event window with everyone
outside it. It still does not identify the denial's date, the event's bill, or
the direction of causation.

## Results

| Event family | Friction group (unweighted n) | Care delay | Bill problem | Medical debt | Collector contact |
|---|---:|---:|---:|---:|---:|
| Office | Denial/delay (227) | 15.62% (SE 2.77) | 23.21% (3.69) | 27.31% (4.07) | 22.01% (3.33) |
| Office | No denial/delay (1,568) | 6.25% (0.73) | 6.95% (0.86) | 14.58% (1.30) | 10.55% (0.91) |
| ER | Denial/delay (166) | 22.30% (4.12) | 30.78% (3.87) | 32.06% (4.52) | 30.58% (4.10) |
| ER | No denial/delay (555) | 6.16% (1.10) | 9.11% (1.30) | 18.84% (2.05) | 14.80% (2.05) |
| Inpatient | Denial/delay (80) | 16.27% (4.78) | 30.64% (5.95) | 26.30% (6.40) | 19.09% (5.37) |
| Inpatient | No denial/delay (306) | 3.38% (1.17) | 5.02% (1.52) | 10.68% (1.88) | 11.31% (2.45) |

Shares use `PERWT24F` and 128 HC-036BRR flags. Counts are unweighted and
outcome-valid counts can differ slightly because of item missingness. The
event-window populations are 3,227 office, 1,096 ER, and 545 inpatient people;
records with codes other than `EQDENY53=1` or `EQDENY53=2` are not assigned to
either friction comparison group.

## Practical-room conditioning

The pooled contrast is not the whole mechanism. Two pre-specified conditioning
surfaces test whether it remains visible among people with any private coverage
and among people who report low confidence paying an unexpected expense:

| Event family / stratum | Denial/delay: care delay; medical debt | No denial/delay: care delay; medical debt |
|---|---:|---:|
| Office / any private coverage | 15.44%; 27.35% (n=131) | 6.11%; 15.40% (n=1,001) |
| ER / any private coverage | 31.16%; 34.56% (n=80) | 5.19%; 24.19% (n=257) |
| Inpatient / any private coverage | 8.49%; 29.67% (n=36) | 0.85%; 13.93% (n=133) |
| Office / not confident paying unexpected expense | 40.91%; 57.65% (n=47) | 15.43%; 29.06% (n=198) |
| ER / not confident paying unexpected expense | 34.57%; 45.11% (n=48) | 11.62%; 25.52% (n=113) |
| Inpatient / not confident paying unexpected expense | 36.51%; 40.04% (n=23) | 9.23%; 15.33% (n=56) |

These intersections are descriptive robustness screens, not separate causal
estimates. Inpatient and friction/room cells are small; the practical-room
variables are annual/person-level measures, not liquid cash or event-specific
deductibles. The result is best read as evidence that nominal coverage does
not erase reported room heterogeneity, not as a plan-generosity effect.

The corresponding denial/delay minus no-denial/delay gaps are:

| Event family / stratum | Care-delay gap | Medical-debt gap |
|---|---:|---:|
| Office / any private coverage | +9.33 percentage points | +11.95 pp |
| ER / any private coverage | +25.97 pp | +10.37 pp |
| Inpatient / any private coverage | +7.64 pp | +15.74 pp |
| Office / not confident | +25.48 pp | +28.59 pp |
| ER / not confident | +22.95 pp | +19.59 pp |
| Inpatient / not confident | +27.28 pp | +24.71 pp |

These are differences between weighted descriptive shares, not treatment
effects. The output retains BRR standard errors for each cell; the difference
itself is not presented as a separately tested contrast, and no multiplicity
adjustment or covariate adjustment is claimed.

## What this adds

The friction contrast is visible across all three event families. In the
strict event window, reported denial/delay is accompanied by higher point
estimates for all four household-response context measures, with the largest
absolute separation for office and ER bill problems and care delay. The
pattern is a useful mechanism signal: institutional friction and household
financial/care pressure appear together on a temporally bounded person/event
frame.

It is not a finding that denial caused debt or delayed care. `EQDENY53` is a
round-level report with no claim identifier or decision date, and a first
observed event may follow an earlier need. Severity, coverage, access,
baseline health, and socioeconomic position can affect both friction and the
outcomes. The no-denial group is a comparison group, not a counterfactual.

## Boundaries

- The event date is month-level and the strict window only establishes bounded
  month ordering relative to round endpoints.
- `DLAYCA42`, `PROBPY42`, `MEDDEBT42`, and `FWDEBT42` are same-person round
  context, not event-specific claims, bills, or treatment outcomes.
- The screen does not observe amount owed, deductible, household payer,
  alternative provider/treatment, appeal, institutional response, correction,
  coverage restoration, or remedy.
- Event-family universes include only people with an observed event; people who
  never reached care are outside these rows.
- Small inpatient friction cells have wide uncertainty and should not be
  ranked against the larger office or ER cells.

## Reproduction

```bash
python3 scripts/analyze_meps_dated_friction_cascade.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  /tmp/cgtm-meps-2024/h36brr/h36brr24.dta \
  --office-file /tmp/cgtm-meps-2024/events/h254g.dta \
  --emergency-room-file /tmp/cgtm-meps-2024/events/h254e.dta \
  --inpatient-file /tmp/cgtm-meps-2024/events/h254d.dta \
  --output analysis/projects/us-household-constraint-cascade/data-meps-dated-friction-cascade-2024.json
```

The [analysis script](../../../scripts/analyze_meps_dated_friction_cascade.py)
was corrected for a pandas index-alignment issue before this output was
accepted. Script SHA-256: `2b9692f8db7166e2d57d4ce315e25eb2d2b489a979e2a22d00d0c2c8c91970b9`.
The compact output SHA-256 is
`034f3b88bd43fa3ae08d9662f8b089fb70779dd10f655c2ac716be27b7a40fa8`.

**Evidence status:** strict-window same-person descriptive comparison; not a
claim-level episode, causal estimate, remedy result, recovery measure, or
trust/action result.
