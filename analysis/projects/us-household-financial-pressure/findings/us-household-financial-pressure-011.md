# Financial-condition paths carry different work, borrowing, health, and care paths

**Status:** same-respondent SHED panel synthesis · **Checked:** 2026-09-14

## The bounded finding

The recontacted 2024–2025 SHED panel shows that material adaptation, work,
health, and unpaid adult care do not move on one schedule. Among prior adopters,
reported work-more, borrowing, and reduced-use behaviors persist more often on
a worsened financial-condition path than on an improved path. At the same time,
most respondents in every financial path report unchanged health, and adult-care
entry and exit occur in both worsening and improving paths.

This supports a same-respondent persistence pattern—not a causal household
story:

> Financial deterioration is associated with more persistent reported
> adaptations, but “recovery” in a broad money category does not imply that
> work, health, or care responsibilities have recovered in the same period.

## Joint panel surfaces

The panel contains 4,419 paired respondents with a valid 2024–2025 financial-
condition path and a nonmissing 2025 panel weight. The following persistence
shares are among respondents who reported the named adaptation in 2024.

| 2024→2025 financial path | Work more / got another job | Increased borrowing | Used less / stopped |
|---|---:|---:|---:|
| Worsened | 48.1% (n=146) | 65.1% (n=140) | 84.8% (n=488) |
| Same broad condition | 43.7% (n=384) | 52.0% (n=318) | 72.6% (n=1,584) |
| Improved | 41.2% (n=186) | 45.0% (n=173) | 66.1% (n=544) |

The denominators in parentheses are unweighted valid prior-adopter pair counts;
the percentages are weighted 2025 “Yes” shares. These are separate outcomes,
not a combined stress index. Working more can preserve cash while consuming
time; borrowing can preserve immediate consumption while creating later
repayment exposure; reduced use can protect money while changing quality,
health, mobility, or social participation.

## Health and unpaid adult-care paths

| 2024→2025 financial path | Health worsened | Health unchanged | Health improved | Adult-care entry | Adult-care exit |
|---|---:|---:|---:|---:|---:|
| Worsened | 18.8% | 69.0% | 12.2% | 10.6% (n=655) | 43.3% (n=149) |
| Same broad condition | 15.9% | 72.9% | 11.2% | 6.5% (n=2,447) | 36.2% (n=419) |
| Improved | 16.5% | 68.8% | 14.6% | 7.5% (n=627) | 45.9% (n=122) |

Health percentages use the valid health-direction universe within each financial
path. Care-entry denominators are respondents with no adult care in 2024;
care-exit denominators are respondents with adult care in 2024. Care is a
reported unpaid-adult-care status, not hours, intensity, relationship, or
recipient outcome.

The counterexample is central: 69.0% of respondents on the worsened financial
path reported unchanged health, while 16.5% on the improved path reported
worsened health. Financial path and health path are related surfaces, not
identical outcomes. Care entry also occurs among improved respondents, and care
exit occurs among worsened respondents.

## Interpretation across the end-to-end program

```text
financial condition path
  -> repeated adaptation, work-more, borrowing, or reduced use
  + health direction and unpaid-care entry/exit
  -> time, family, work, and security consequences
  -> trust, attribution, civic action, or institutional response (not measured)
```

The panel strengthens the material-to-adaptation-to-health/care segment because
the respondent is followed across two waves. It still does not provide a dated
price, bill, care event, work-rule change, employer, insurer, or public-system
episode. It cannot identify schedule control, care intensity, family support,
recipient safety, remedy, trust, political action, or causal direction.

## Counterexamples and safeguards

- Improving financial condition can coexist with persistent borrowing, reduced
  use, worse health, or new care responsibility.
- Worsening financial condition can coexist with ended adaptation, unchanged or
  improved health, or care exit.
- A broad condition category can change because of income, debt, health,
  housing, employment, family, prices, or expectations; the panel does not
  decompose those causes.
- Recontact selection and the absence of replicate weights limit inference.
  The public-use panel weight supports descriptive weighting but not claimed
  design-based standard errors in this pass.

## Next decisive test

Add care intensity, paid and unpaid work hours, schedule control, debt/service
cost, family support, coverage, and a dated financial or care event. Then test
whether a defined support or alternative protects health, recipient outcomes,
work continuity, and later recovery for the same respondent or household.

## Sources and reproduction

- [SHED adaptation-condition record](../../../records/us-shed-panel-adaptation-condition-path-2024-2025.json)
- [SHED financial-path health/care record](../../../records/us-shed-financial-path-health-care-2024-2025.json)
- [SHED panel reproduction audit](../shed-panel-reproduction-audit-2026-09-13.json)
- [SHED panel persistence layer](../shed-2024-2025-panel-persistence-layer-v1.md)
- [SHED financial-condition path layer](../shed-panel-adaptation-condition-path-layer-v1.md)
- [SHED health/care path layer](../shed-panel-health-care-path-layer-v1.md)
- [Official Federal Reserve SHED releases](https://www.federalreserve.gov/consumerscommunities/shed_data.htm)

**Evidence status:** weighted same-respondent descriptive panel evidence with
exact rerun hashes; no causal estimate, design-based uncertainty estimate,
dated trigger, institutional remedy, trust, political action, or geopolitical
consequence is claimed.
