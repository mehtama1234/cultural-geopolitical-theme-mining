# Financial recovery, health, and care do not move on one schedule

**Status:** weighted SHED paired-panel finding · **Checked:** 2026-09-13

## The bounded finding

The Federal Reserve's 2024–2025 SHED recontact panel shows that financial
condition, self-rated health, and unpaid adult-care responsibility move
together only imperfectly. Among respondents whose financial condition
worsened, 18.8% reported worse health, 69.0% unchanged health, and 12.2%
improved health. Among respondents whose financial condition improved, 16.5%
reported worse health, 68.8% unchanged health, and 14.6% improved health.

Care transitions also differ by financial path, but not monotonically. Adult-
care entry was 10.6% in the worsened path, 6.5% in the stable path, and 7.5%
in the improved path. Care entry is conditional on no reported unpaid adult
care in 2024; it is not a measure of hours, intensity, or recipient outcome.

The safe interpretation is a same-respondent distribution of paths, not a
financial-condition effect. A household can recover financially while health
remains unchanged or worsens; care can enter while finances improve.

## What is measured

| Layer | Result | Denominator and limit |
|---|---:|---|
| Health after financial worsening | 18.8% worse; 69.0% unchanged; 12.2% improved | 804 paired respondents with valid health paths |
| Health after stable finances | 15.9% worse; 72.9% unchanged; 11.2% improved | 2,866 paired respondents |
| Health after financial improvement | 16.5% worse; 68.8% unchanged; 14.6% improved | 749 paired respondents |
| Adult-care entry after financial worsening | 10.6% | 655 respondents with no 2024 care and valid 2025 status |
| Adult-care entry after stable finances | 6.5% | 2,447 respondents in the same entry universe |
| Adult-care entry after financial improvement | 7.5% | 627 respondents in the same entry universe |

Adult-care exit is a separate universe: among respondents reporting care in
2024, exit was 43.3%, 36.2%, and 45.9% in the worsened, stable, and improved
financial paths respectively. Entry and exit cannot be pooled into one burden
measure.

## The route under test

```text
financial condition changes
  -> health capacity and unpaid-care responsibility may change
  -> paid work, time, consumption, and family coordination may be reallocated
  -> recovery, recipient safety, trust, and political meaning may change
```

The panel directly measures the first transition and two adjacent outcomes.
It does not measure care hours, schedule control, a dated financial shock,
care-recipient outcomes, attribution, institutional remedy, trust, voting, or
collective action.

## Why the counterexample matters

If “financial recovery” is defined as an improved money category, it can hide
health persistence or deterioration. If “care burden” is defined as any care
response, it hides entry and exit and treats a changing social role as fixed.
The stable financial path also includes health worsening and care entry, so
neither outcome can be assigned to financial decline alone.

These are not arguments that finances do not matter. They identify the missing
mechanisms: diagnosis and health need, care intensity, family support, work
schedule, coverage, debt, and the timing of the event.

## Method and limits

The unit is a recontacted US adult respondent observed in the 2024 and 2025
SHED waves. The calculations use the 2025 panel weight for weighted
descriptive transition tables. The panel is self-reported, recontacted, and
not accompanied here by design-based standard errors; broad ordinal financial
condition and health categories are not continuous shocks or clinical
measures. Each endpoint keeps its own valid denominator.

The result does not establish that financial worsening caused health change or
care entry. Reversed timing, common causes, selection into recontact, and
family or health events can all contribute.

## Next test

Add care intensity, schedule control, work hours, health conditions, coverage,
debt, family support, and a dated financial or care event. Then test whether
the same respondent or household protects health and recipient outcomes by
borrowing, unpaid substitution, reduced work, public support, or other means,
and whether the route changes trust or political action.

**Evidence status:** weighted same-respondent panel comparison with explicit
transition universes and counterexamples; no causal or complete material-to-
meaning chain is claimed.

## Sources

- [Federal Reserve SHED data release](https://www.federalreserve.gov/consumerscommunities/shed_data.htm)
- [SHED financial-path health/care layer](../shed-panel-health-care-path-layer-v1.md)
- [Machine-readable trend record](../../../records/us-shed-financial-path-health-care-2024-2025.json)
