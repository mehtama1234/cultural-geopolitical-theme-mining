# Basic composition control preserves part of the eldercare time profile

**Status:** checked · **Checked:** 2026-09-13

## One-sentence finding

After standardizing eldercare providers and nonproviders to the pooled
age-band×sex×labor-force-status composition, providers still show more
household work and travel and less socializing time in both 2024 and 2025;
the paid-work difference is smaller and imprecise.

## Standardized differences

Values are provider minus nonprovider weighted mean minutes per diary day;
standard errors are in parentheses.

| Measure | 2024 | 2025 |
|---|---:|---:|
| Household work | +15.1 (5.5) | +9.0 (5.0) |
| Care for people | +8.6 (3.9) | +10.7 (3.4) |
| Paid work | −8.8 (8.9) | −8.0 (10.5) |
| Travel | +11.8 (4.6) | +8.3 (2.8) |
| Socializing/communication | −19.4 (7.0) | −23.9 (8.7) |
| Secondary childcare | −19.4 (5.9) | −5.8 (8.0) |
| Eldercare | +64.2 (6.7) | +64.0 (7.5) |

The 2024 standardization uses 30 supported cells and the 2025 standardization
uses 33. The supported samples include 1,319 provider and 6,316 nonprovider
respondents in 2024, and 1,016 provider and 5,110 nonprovider respondents in
2025. Unsupported cells are excluded from the standardized target rather than
silently extrapolated.

## What this changes

The raw provider/nonprovider contrast was not only an age or labor-force
composition artifact. Basic composition control preserves a household-work,
travel, and social-time profile across two annual samples. It does not justify
the stronger statement that eldercare caused those differences: the paid-work
contrast is compatible with zero at this precision, and health, family
structure, recipient need, occupation, schedule control, and diary timing are
still unmeasured or uncontrolled.

## Evidence path

```text
eldercare-roster provider status
  -> observed care and time allocation in one diary day
  -> age/sex/labor-force standardized profile
  -> candidate household, work, and social-availability mechanism
```

The first two arrows are measured. The last arrow remains a hypothesis. This
is an adjusted descriptive association, not an event study or causal estimate.

## Limits and counterexample

- Provider status is based on a linked roster record, not a dated care onset or
  randomized assignment.
- 2024 and 2025 are separate annual samples, not repeated respondents.
- Standardization covers age, sex, and labor-force status only.
- A one-day diary does not measure recurring care burden, travel distance,
  expenses, employer accommodation, or schedule control.
- Primary activity, secondary childcare, and eldercare remain separate
  currencies; they are not combined into a burden score.

The result would weaken if a richer adjustment for health, family structure,
recipient need, occupation, schedule, and diary timing removed the pattern. A
stronger end-to-end result requires a repeated provider or household unit with
a dated care change, alternatives, control, and follow-up work or health
outcome. Providers who maintain comparable social and work time through shared
support are an important counterexample to a burden interpretation.

## Sources

- [BLS ATUS 2024 public-use files](https://www.bls.gov/tus/data/datafiles-2024.htm)
- [BLS ATUS 2025 public-use files](https://www.bls.gov/tus/data/datafiles-2025.htm)
- [Machine-readable observation record](../../../records/us-atus-eldercare-provider-standardized-2024-2025.json)
