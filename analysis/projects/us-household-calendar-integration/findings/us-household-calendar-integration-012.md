# Eldercare providers show a distinct time profile, but the ATUS contrast is not causal

**Status:** checked · **Checked:** 2026-09-13

## One-sentence finding

In both 2024 and 2025 ATUS annual samples, respondents with an eldercare-roster
record reported more household-work and travel minutes and fewer paid-work and
socializing minutes than respondents without one; the contrast is a descriptive
time-allocation pattern, not evidence that eldercare caused those differences.

## What we directly know

All values are weighted mean minutes per diary day; standard errors are in
parentheses.

| Year / group | Household work | Paid work | Travel | Socializing/communication | Eldercare |
|---|---:|---:|---:|---:|---:|
| 2024 provider (n=1,319) | 142.6 (4.9) | 179.8 (8.0) | 71.8 (3.1) | 264.1 (6.7) | 68.7 (6.6) |
| 2024 nonprovider (n=6,350) | 116.5 (2.3) | 192.8 (3.6) | 63.7 (1.2) | 275.4 (3.2) | 0.0 |
| 2025 provider (n=1,016) | 136.6 (5.5) | 172.9 (11.9) | 67.3 (2.5) | 265.0 (8.1) | 66.8 (7.0) |
| 2025 nonprovider (n=5,130) | 116.8 (2.1) | 188.0 (4.4) | 61.4 (1.5) | 278.1 (3.9) | 0.0 |

Provider status means the respondent had at least one linked eldercare-roster
record. The nonprovider group has zero eldercare minutes by construction of
that classification, not because it proves no eldercare outside the roster or
diary occurred.

## How the result may matter

```text
eldercare connection
  -> care, household production, travel, and paid-work time coexist in one diary
  -> available social time and work room may differ across providers
  -> household, employer, health, and institutional consequences remain open
```

The first arrow is directly measured. The second is a descriptive association.
The final arrow is not measured here. The time profile could reflect age,
employment, health, household composition, recipient need, or selection into
care rather than eldercare causing a loss of paid or social time.

## Counterexamples and limits

- Provider status is not randomized and the cells are not matched on age,
  work, health, family, or recipient characteristics.
- 2024 and 2025 are different annual samples, not repeated respondents.
- A one-day diary does not measure recurring weekly or annual care burden.
- Primary activity minutes omit simultaneous activities; secondary childcare and
  eldercare are retained as separate currencies.
- The roster does not establish distance, expenses, shared support, schedule
  control, employer accommodation, health outcome, recovery, trust, or civic
  action.

The pattern would be weakened as a burden interpretation if adjustment or a
repeated-unit design showed comparable time profiles after accounting for age,
health, work, family composition, recipient need, and diary timing. A stronger
result would require a dated care change, repeated provider/household unit,
alternatives, control, and follow-up work or health outcome.

## Sources

- [BLS ATUS 2024 public-use files](https://www.bls.gov/tus/data/datafiles-2024.htm)
- [BLS ATUS 2025 public-use files](https://www.bls.gov/tus/data/datafiles-2025.htm)
- [Machine-readable observation record](../../../records/us-atus-eldercare-provider-time-2024-2025.json)
