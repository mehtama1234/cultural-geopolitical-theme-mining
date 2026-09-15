# Eldercare time contrasts survive richer composition controls, with annual variation

**Status:** checked · **Checked:** 2026-09-13

## One-sentence finding

After adding household-child status and broad education to the age, sex, and
labor-force standardization, providers still show more care, household work,
and travel time; the paid-work contrast is larger in magnitude but uncertain,
and the social-time contrast weakens in 2025.

## Richer standardized differences

Values are provider minus nonprovider weighted mean minutes per diary day;
standard errors are in parentheses.

| Measure | 2024 | 2025 |
|---|---:|---:|
| Household work | +16.8 (5.1) | +7.4 (5.0) |
| Care for people | +14.8 (4.0) | +12.0 (3.1) |
| Paid work | −19.7 (8.3) | −14.5 (10.0) |
| Travel | +9.7 (3.7) | +7.6 (2.9) |
| Socializing/communication | −18.4 (7.0) | −9.5 (8.1) |
| Secondary childcare | −10.9 (5.5) | −3.0 (5.6) |
| Eldercare | +70.7 (7.1) | +62.4 (6.8) |

The 2024 estimate uses 110 supported cells and 7,470 respondents; the 2025
estimate uses 104 supported cells and 5,895 respondents. Each supported cell
contains both provider statuses. The target controls are age band, sex,
labor-force status, whether `TRCHILDNUM>0`, and broad `PEEDUCA` education band.

## Interpretation

The household-work, care, and travel profile is not explained away by the
first five measured composition dimensions. The social-time difference is
visible in 2024 but imprecise and smaller in 2025. The paid-work difference is
roughly −20 minutes in 2024 and −14 minutes in 2025, but the 2025 uncertainty
is wide enough that this should not be called a stable work-loss effect.

This is a robustness result about the time profile, not a causal care penalty.
Provider status is not a dated or randomized exposure, and the adjustment does
not include health, detailed family structure, recipient need, occupation,
schedule control, or diary timing.

## Evidence path and counterexample

```text
eldercare-roster status
  -> care/time allocation in a selected diary day
  -> profile after age, sex, labor, child, and education standardization
  -> candidate work, mobility, and social-availability mechanism
```

The first two arrows are measured; the final arrow remains open. A useful
counterexample would be a repeated provider or household unit with comparable
care need but preserved work and social time through shared support,
accommodation, or schedule control.

## Limits

- 2024 and 2025 are separate annual samples, not repeated respondents.
- Standardization controls only the named dimensions and excludes unsupported
  cells rather than extrapolating to them.
- A one-day diary does not measure recurring care burden, distance, expenses,
  employer response, health outcome, recovery, trust, or political action.
- Primary activity, secondary childcare, and eldercare are separate currencies;
  they are not combined into a burden score.

The next valid step is richer health/family/recipient adjustment or a repeated
unit with a dated care change, alternatives, schedule control, and follow-up
work or health outcome.

## Sources

- [BLS ATUS 2024 public-use files](https://www.bls.gov/tus/data/datafiles-2024.htm)
- [BLS ATUS 2025 public-use files](https://www.bls.gov/tus/data/datafiles-2025.htm)
- [Machine-readable observation record](../../../records/us-atus-eldercare-provider-richer-standardized-2024-2025.json)
