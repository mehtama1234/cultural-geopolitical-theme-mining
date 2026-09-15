# SIPP material and food-security estimates survive a design-based uncertainty check

**Status:** official-universe Fay-BRR population-layer finding · **Checked:** 2026-09-13

## The bounded finding

The earlier SIPP material/time/care scan was useful but point-only. Re-running
five measures against the official field-status flags and 240 replicate weights
gives a stronger descriptive layer: the estimates carry field-specific
denominators, standard errors, and approximate 95% intervals rather than being
presented as exact population facts.

The analysis uses 379,215 selected person-record/month rows and retains 378,291
with a positive final person weight. It uses the 2024 reference year in the
2025 SIPP public-use release. The replicate file matches all positive-weight
records by `SSUID`, `PNUM`, `SPANEL`, `SWAVE`, and `MONTHCODE`.

## Estimates

| Measure | Estimate | Fay-BRR SE | Approx. 95% interval | Valid records |
|---|---:|---:|---:|---:|
| Unable to pay rent or mortgage | 4.636% | 0.251 pp | 4.144–5.129% | 377,945 |
| Unable to pay utility bills | 7.069% | 0.322 pp | 6.437–7.701% | 377,945 |
| High or marginal food security | 88.978% | 0.365 pp | 88.263–89.694% | 321,883 |
| Hungry but did not eat because of money | 25.597% | 1.176 pp | 23.293–27.901% | 62,808 |
| One job | 54.751% | 0.312 pp | 54.138–55.363% | 321,883 |

These are conditional weighted shares within the applicable official
universes. The intervals describe sampling variance under the Fay-BRR design;
they do not absorb all measurement, nonresponse, coding, or reference-period
uncertainty.

## What this changes

The result is now suitable for calibrated comparisons: utility-payment
difficulty is higher than rent/mortgage difficulty in these separate valid
universes, and the uncertainty bands are narrow relative to that difference.
That comparison still does not show that the same people experienced both
conditions, why they occurred, or what they did next.

The hunger estimate is much less precise because its food-screen universe is
smaller. That difference is analytically important: a broad security measure
and a more specific hardship item cannot be treated as interchangeable. The
one-job measure also describes job count, not hours, schedule control, care
availability, pay, or bargaining power.

## End-to-end route under test

```text
material condition or food constraint
  -> monthly adjustment and available alternatives
  -> work, care, time, debt, health, or consumption outcome
  -> recovery, trust, political judgment, or institutional response
```

This pass strengthens the measurement and uncertainty stage. It does not close
the dated-trigger, same-household time-substitution, interpretation, or
political-action arrows. Household fields are repeated on person records, and
the final person weight is not a household weight.

## Method and limits

The full estimate uses `WPFINWGT`. Each replicate uses `REPWGT1` through
`REPWGT240`, with Census's Fay modified-BRR formula (`G=240`, perturbation
factor `0.5`). Official status flags and age/food-screen universes were
applied. The raw files and generated calculation output remain outside the
repository; the machine-readable result preserves the source hashes and
reported denominators.

The estimates are not a causal SNAP, price, utility, employer, or care effect.
They do not identify a particular bill, notice, remedy, firm decision, time
loss, health change, trust change, or political action. SIPP remains one
longitudinal monthly layer among ATUS, SHED, MEPS, RECS, PSID, administrative,
firm, and geopolitical sources.

## Next test

Extend the same official-universe and replicate-weight treatment to the
field-specific care and work constraints, then define a one-record-per-
household selection rule before making household claims. The stronger
material/time/care result still requires a dated trigger, alternatives,
protected and sacrificed outcomes, and follow-up meaning or action.

**Evidence status:** reproducible design-based person-weighted descriptive
comparison; causal and complete same-unit societal arrows remain open.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)
- [Machine-readable result](../../../records/us-sipp-material-time-care-official-variance-2024.json)
