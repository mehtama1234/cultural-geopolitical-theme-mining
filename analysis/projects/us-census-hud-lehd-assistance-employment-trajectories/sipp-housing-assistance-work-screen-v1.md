# SIPP monthly assistance and next-month work/security screen v1

**Checked:** 2026-09-25  
**Status:** weighted descriptive cross-lag complete; not causal  
**Source:** 2025 SIPP public-use file, January–December 2024 reference period

## Question and design

The earlier housing audit showed that the main housing-assistance fields are
reference-period or residence-spell measures. This screen therefore uses the
one relevant field that the Census catalog defines as genuinely monthly:
`EOTHAS_MNYN`, whether the person received “other (clothing or housing)
assistance” during the month. It asks what is observed in the next month for
the same identified person:

```text
other assistance at month t
  -> job-count movement at t+1
  -> income-to-poverty-band movement at t+1
  -> reported inability to pay rent or mortgage at t+1
```

The calculation uses `WPFINWGT` from month t and 240 Census Fay–BRR replicate
weights with perturbation factor 0.5. It retains separate valid-pair
denominators for each outcome. The compact machine-readable result is in
[data/sipp-housing-assistance-work-screen-2024.json](data/sipp-housing-assistance-work-screen-2024.json).

## Results

| Month-t assistance | Valid pairs | Job count changed at t+1 | Poverty band changed at t+1 | Unable to pay rent/mortgage at t+1 |
|---|---:|---:|---:|---:|
| Yes | 4,501 | 2.03% (1.30–2.77) | 3.34% (2.43–4.25) | **9.15% (5.89–12.41)** |
| No | 290,313 | 1.71% (1.62–1.79) | 3.48% (3.29–3.67) | **4.17% (3.75–4.58)** |

Intervals are approximate 95% Fay–BRR intervals in percentage points. They are
design-based uncertainty around these person-weighted descriptive cells, not
adjustment for selection into assistance.

## What this adds

This is the first same-person, weighted bridge in this lane that uses a
genuinely monthly assistance indicator and places a later housing-security
measure beside work and resource movement. The descriptive pattern is
specific: the assistance-exposed cell has a higher next-month rent/mortgage
payment-difficulty share, while job-count and poverty-band movement are close.
That is compatible with assistance reaching people already under greater
housing pressure; it does not show that assistance produced the pressure.

The [tenure/resource counterexample audit](sipp-housing-assistance-work-stratified-v1.md)
shows that this pooled contrast is not uniform within comparable contexts.

## Limits and next test

`EOTHAS_MNYN` combines clothing or housing assistance and does not identify a
HUD program, benefit amount, adequacy, application, denial, landlord response,
or exit. `EAWBMORT` is a reported difficulty indicator, not arrears,
eviction, homelessness, or verified recovery. The screen also has no measured
alternative housing, housing quality, care burden, notice/appeal route, or
trust/action endpoint. Repeated household fields are analyzed on person
records; this is not household prevalence.

The result therefore advances the chain only to a bounded descriptive bridge:

```text
monthly other assistance context -> next-month housing difficulty/work/resource context
```

The next end-to-end test still requires a program-specific assistance spell or
exit reason, amount/adequacy, alternatives, institutional response, and a
later stability or recovery outcome for the same retained unit. Keep this
screen separate from the HUD–LEHD and HEARS linked findings.

## Sources

- [Census 2025 SIPP data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [Census SIPP variable catalog](https://api.census.gov/data/2025/sipp/variables.html)
- [SIPP assistance field audit](sipp-housing-transition-field-audit-v1.md)
- [SIPP housing-transition timing report](sipp-housing-transition-timing-report-v1.md)
- [Analysis script](../../../scripts/analyze_sipp_housing_assistance_work_screen.py)
