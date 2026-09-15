# SHED panel adaptation by financial-condition path v1

**Checked:** 2026-09-13
**Unit:** recontacted SHED respondent, 2024 to 2025  
**Panel:** 4,419 records with a shared `shedid` and nonmissing 2025
`panel_weight`  
**Method:** weighted descriptive transitions; no variance or causal estimate

## The question

When a person reports a price adaptation, does that behavior persist differently
when their broad financial condition worsens, stays in the same category, or
improves the next year?

This is a population-level persistence test. It does not reduce society to one
household, and it does not claim that a reported adaptation was caused by one
price, firm, policy, or event.

## How the comparison is defined

The 2024 and 2025 financial-condition categories are ordered as: finding it
difficult, just getting by, doing okay, and living comfortably. A path is
classified as **worsened**, **same broad condition**, or **improved** according
to movement among those categories. Within each path, the table reports the
share who said **Yes in 2025 among those who said Yes in 2024** for the named
adaptation.

## Persistence among prior adopters

| 2024 adaptation | Worsened path | Same broad condition | Improved path |
|---|---:|---:|---:|
| Switched to cheaper products | 86.9% | 75.9% | 68.8% |
| Used less or stopped using products | 84.8% | 72.6% | 66.1% |
| Reduced savings | 71.0% | 58.7% | 55.0% |
| Increased borrowing | 65.1% | 52.0% | 45.0% |
| Delayed a major purchase | 75.2% | 65.9% | 56.6% |

The pattern is consistent with financial adaptation becoming harder to reverse
when the respondent's reported condition moves down. It is also consistent
with selection: people who worsen may already have had more severe or repeated
pressures, different resources, health or employment changes, or different
expectations. The table is therefore a persistence gradient, not a causal
estimate.

The contrast is largest for borrowing and reduced use among prior adopters:
borrowing persists at 65.1% on a worsening path and 45.0% on an improving path;
reduced use persists at 84.8% and 66.1%, respectively. These are different
behaviors. Borrowing may preserve an immediate need while creating a future
record or payment burden; reduced use may protect cash while changing health,
quality, mobility, or participation. They should not be collapsed into one
stress score.

## Re-entry among prior non-adopters

Among people who said **No in 2024**, 2025 adoption was also lower on an
improving path than on a worsening path. For the same five measures, the
worsening-path versus improving-path shares were:

| 2024 non-adopter outcome in 2025 | Worsened path | Improved path |
|---|---:|---:|
| Cheaper products | 51.3% | 28.3% |
| Used less or stopped | 54.7% | 29.6% |
| Reduced savings | 40.7% | 20.3% |
| Increased borrowing | 13.5% | 5.8% |
| Delayed a major purchase | 41.6% | 25.6% |

This is a second descriptive signal: financial-condition movement is related
to both persistence and re-entry. It does not show whether a person improved
because an adaptation ended, or stopped adapting because another resource,
support, or alternative became available.

## What this adds to the broad program

1. **Consumer trends have paths, not only levels.** Annual prevalence can hide
   repeated substitution, reduced use, saving cuts, borrowing, or delay.
2. **Recovery is behavior-specific.** An improving financial category does not
   imply that every adaptation has ended; it is associated with lower reported
   persistence, but substantial persistence remains.
3. **Material adaptation is not political action.** The panel can show repeated
   behavior for the same respondents. It does not measure attribution, trust,
   cultural meaning, civic action, or voting in this comparison.
4. **The next bridge is an event, not another aggregate.** A dated price,
   income, health, housing, employment, or policy event is needed to separate
   cause, selection, and recovery.

## Limits and counterexamples required

- `panel_weight` supports a descriptive recontact estimate, but the [weight
  surface audit](shed-panel-weight-audit-layer-v1.md) confirms that the
  public-use files contain no replicate-weight or variance fields for
  design-based standard errors.
- SHED responses refer to a preceding period and are not linked here to a
  dated purchase, bill, firm, policy, or price series.
- Financial-condition categories are broad. A one-category move can contain
  very different income, debt, health, family, and housing changes.
- Recontact and nonresponse may make the linked sample different from the full
  cross-section; weighting does not identify every selection mechanism.
- The same respondents are followed, but no household-level count is claimed;
  person records may reflect shared household conditions.

The decisive counterexample is a respondent whose condition worsened but whose
prior adaptation ended, or whose condition improved while the adaptation
continued because of debt, care, health, housing, or a durable change in need.
Those cases prevent the path from being read as a mechanical rule.

## Reproduction

```text
python3 scripts/analyze_shed_panel_adaptation_condition_path.py \
  --old /path/to/SHED_public_use_data_2024_(CSV).zip \
  --new /path/to/SHED_2025.csv.zip \
  --output /tmp/shed-adaptation-condition-path.json
```

The calculation uses the official [SHED data releases](https://www.federalreserve.gov/consumerscommunities/shed_data.htm). The raw files and JSON output are not committed. The 2026-09-13 rerun against the official 2024 and 2025 CSV archives is recorded in the [reproduction audit](shed-panel-reproduction-audit-2026-09-13.json); it corrected the reduced-savings and re-entry cells to the values above.

Related: [SHED panel persistence layer](shed-2024-2025-panel-persistence-layer-v1.md), [2025 SHED price-adaptation layer](shed-2025-price-adaptation-layer-v1.md), [economic adaptation, perception, and public action layer](../us-cost-trust-politics/economic-adaptation-perception-action-layer-v1.md), and the [broad event ledger](../../templates/US-BROAD-EVENT-LEDGER_V1.md).
