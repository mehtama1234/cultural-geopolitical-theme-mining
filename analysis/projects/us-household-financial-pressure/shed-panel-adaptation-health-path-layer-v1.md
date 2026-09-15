# SHED panel adaptation by health direction v1

**Checked:** 2026-09-15  
**Unit:** recontacted US adult respondent, 2024 to 2025  
**Panel:** 4,163 paired respondents with a valid 2024→2025 self-rated-health path and a valid 2025 panel weight  
**Method:** weighted descriptive transitions; no design-based variance or causal estimate

## Question

The existing SHED panel work showed that financial-condition paths align with
health and care transitions, and that reported price adaptations persist or
re-enter at different rates. This pass changes the conditioning axis: it asks
whether adaptations reverse when the same respondent's self-rated health
improves, and whether they intensify or newly appear when health worsens.

```text
health direction
  -> reduced use, saving cuts, borrowing, delay, or extra work
  -> recovery or persistence of household room
  -> possible care, work, trust, and public-action consequences
```

The final arrow is not measured here. The health path is an annual ordinal
self-report, not a dated diagnosis, bill, or treatment episode.

## Results

The table reports the 2025 share still answering “Yes” among 2024 adopters of
each adaptation. These are persistence rates, not probabilities that health
caused an adaptation.

| 2024→2025 health path | Cheaper products | Used less/stopped | Reduced savings | Increased borrowing | Delayed purchase | Worked more/got job |
|---|---:|---:|---:|---:|---:|---:|
| Worsened (671 pairs) | 75.1% | 74.3% | 62.7% | 59.0% | 69.3% | 39.3% |
| Unchanged (3,000 pairs) | 76.8% | 72.9% | 60.3% | 50.5% | 64.7% | 45.5% |
| Improved (492 pairs) | 78.0% | 74.9% | 56.9% | 56.4% | 66.3% | 48.8% |

The strongest recovery signal is in reduced savings: persistence is 56.9% in
the improved-health path versus 62.7% in the worsened-health path. Borrowing
and delayed purchases, however, remain common after health improvement and
are close to the worsened-health path. Health improvement therefore does not
equal financial recovery; durable debt, prices, care obligations, or other
constraints may keep a household adaptation in place.

Entry among 2024 non-adopters is also substantial. In the improved-health path,
2025 entry is 9.8% for borrowing, 29.1% for delayed purchases, and 36.7% for
using less or stopping use. Those figures show that a respondent can report
better health and still newly adopt a financial adaptation in the same annual
interval.

## Interpretation for the end-to-end program

1. **Recovery is multidimensional.** Health, financial condition, and
   adaptation can move on different schedules; no single “recovered” label is
   sufficient.
2. **Adaptations have different reversibility.** Savings cuts show more health
   gradient than borrowing or delayed purchases, suggesting that balance-sheet
   and commitment constraints may outlast a health change.
3. **The panel identifies selection and timing problems.** Annual health paths
   do not establish whether the health change preceded the adaptation, whether
   a third shock affected both, or whether the adaptation affected reported
   health.
4. **The missing bridge is still concrete.** The next stronger design must add
   dated medical events or bills, coverage and payment burden, care intensity,
   hours, and a later recovery or remedy outcome.

## Boundaries and counterexamples

The public-use panel has main and panel weights but no replicate-weight fields;
these are weighted descriptive percentages without design-based standard
errors. Health is self-rated and ordinal. The adaptation questions do not
identify the product, price, quantity, creditor, care need, or work schedule.
Recontact selection and item-specific valid denominators remain relevant.

Counterexamples are visible in the table: many respondents with worsened health
did not continue each adaptation, while many with improved health did. A
health improvement can coexist with persistent borrowing or a delayed purchase;
a health worsening can coexist with adaptation exit. Neither pattern alone
establishes mechanism.

## Reproduction

```text
python3 scripts/analyze_shed_panel_adaptation_health_path.py \
  --old /path/to/SHED_public_use_data_2024_(CSV).zip \
  --new /path/to/SHED_public_use_data_2025_(CSV).zip \
  --output /tmp/shed-panel-adaptation-health-path.json
```

The calculation uses the official [Federal Reserve SHED data release](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
Raw files and generated JSON are not committed. The full machine-readable
surface is preserved in [the project data output](data/shed-panel-adaptation-health-path-2024-2025.json).

Related: [SHED panel health and care paths](shed-panel-health-care-path-layer-v1.md),
[SHED panel persistence](shed-2024-2025-panel-persistence-layer-v1.md), and the
[financial-pressure recovery synthesis](financial-pressure-adaptation-recovery-synthesis-v1.md).
