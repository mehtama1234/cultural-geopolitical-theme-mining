# SHED 2024–2025 panel persistence layer v1

**Checked:** 2026-09-12  
**Unit:** recontacted SHED respondent, 2024 to 2025  
**Panel:** 4,419 records with a shared `shedid` and nonmissing 2025
`panel_weight`  
**Method:** weighted descriptive transitions; no variance or causal estimate

This is the first same-respondent longitudinal depth pass attached to the
broad program. It tests whether financial condition and price adaptations
persist or reverse. It does not yet connect the same respondents to later
trust, attribution, civic action, or voting.

## Financial condition transitions

Each row is the respondent's 2024 condition; cells are weighted row shares in
2025.

| 2024 condition | Difficult in 2025 | Just getting by | Doing okay | Comfortable |
|---|---:|---:|---:|---:|
| Finding it difficult to get by | 53.2% | 32.3% | 11.8% | 2.7% |
| Just getting by | 16.2% | 48.4% | 31.7% | 3.8% |
| Doing okay | 2.2% | 14.6% | 64.8% | 18.3% |
| Living comfortably | 0.4% | 2.0% | 23.0% | 74.5% |

The pattern shows persistence at both ends, with movement between adjacent
conditions. It does not establish why a respondent moved: prices, wages,
health, debt, family change, housing, or other events may contribute.

## Persistence of reported price adaptations

The table reports the share who said “Yes” in 2025 among respondents who said
“Yes” or “No” in 2024. The first column is re-entry among 2024 non-adopters;
the second is persistence among 2024 adopters.

| Reported action or buffer | No in 2024 → Yes in 2025 | Yes in 2024 → Yes in 2025 |
|---|---:|---:|
| Switched to cheaper products | 32.8% | 76.6% |
| Used less or stopped using products | 32.9% | 73.6% |
| Reduced savings | 23.4% | 60.2% |
| Increased borrowing | 7.8% | 53.2% |
| Delayed a major purchase | 25.2% | 65.6% |
| Worked more or got another job | 9.1% | 44.0% |
| Had three months of emergency funds | 20.2% | 84.8% |

These transitions are not a single “stress” index. Persistent substitution,
reduced use, borrowing, lost savings, extra work, and emergency capacity have
different social meanings and may protect or reduce future room in different
ways. The high persistence among prior adopters is evidence of repeated
reported states, not proof of a permanent condition or a particular price
cause.

## 2024 adaptation and 2025 financial condition

The panel also lets us compare next-year condition by whether a respondent
reported an adaptation in 2024. These are row percentages, not causal effects.

| 2024 report | Difficult in 2025 | Just getting by | Doing okay | Comfortable |
|---|---:|---:|---:|---:|
| Increased borrowing: No | 5.0% | 14.4% | 41.4% | 39.1% |
| Increased borrowing: Yes | 23.5% | 35.5% | 32.9% | 8.1% |
| Reduced savings: No | 5.0% | 11.9% | 37.6% | 45.5% |
| Reduced savings: Yes | 11.7% | 25.7% | 43.7% | 18.8% |
| Delayed major purchase: No | 4.0% | 11.4% | 37.1% | 47.4% |
| Delayed major purchase: Yes | 12.4% | 25.0% | 43.8% | 18.9% |
| Used less/stopped: No | 3.4% | 10.9% | 36.5% | 49.2% |
| Used less/stopped: Yes | 10.6% | 22.0% | 42.5% | 24.9% |

The largest descriptive separation is around borrowing: respondents who
reported increased borrowing in 2024 were more concentrated in difficult or
just-getting-by conditions in 2025 than respondents who did not report that
adaptation. This could reflect prior financial position, a continuing shock,
reverse causation, other household events, or reporting differences. It is a
mechanism signal for the event ledger, not proof that borrowing caused the
later condition.

## Price impact transitions

Price impact also shows persistence. Among respondents who said prices made
their finances **much worse** in 2024, 30.9% gave that answer again in 2025 and
41.1% said somewhat worse. Among those who said **little or no effect** in
2024, 54.4% gave that answer again. The remaining respondents were distributed
across the separate categories: 5.7% much worse, 33.7% somewhat worse, 5.0%
somewhat better, and 1.2% much better. The full transition matrix is retained
in the reproduction JSON rather than turning this measure into a binary stress
label.

## What this adds to the broad societal program

1. **Consumer trends can be durable.** A one-year prevalence number hides
   whether people are repeatedly substituting, delaying, borrowing, or working
   more.
2. **Recovery is unequal.** Financial condition remains concentrated in the
   same broad state for many respondents, especially at the difficult and
   comfortable ends, while middle states show movement in both directions.
3. **Adaptation is part of culture and politics, but is not political action by
   itself.** Repeated buying changes may later affect dignity, trust, blame,
   identity, or public demand, but those arrows require their own measures.
4. **The panel is a bridge, not the destination.** It now supports exposure →
   repeated adaptation or reversal for the same respondent. Attribution,
   information, trust, civic action, remedy, and later security remain open.

## Limits

- SHED questions are self-reported and annual; “because of price increases”
  refers to the preceding period and is not a dated transaction record.
- The panel weight makes the recontact sample useful for descriptive population
  estimates, but this pass does not calculate design-based standard errors.
- Recontact and nonresponse can make panel respondents differ from the full
  cross-section; the panel weight adjusts observed characteristics but does not
  identify every selection mechanism.
- The 2024 and 2025 files are linked by respondent ID, not joined to a specific
  bill, price series, firm, policy, news source, vote, or later outcome.

## Reproduction

```text
python3 scripts/analyze_shed_panel_price_persistence.py \
  --old /path/to/SHED_public_use_data_2024_(CSV).zip \
  --new /path/to/SHED_2025.csv.zip \
  --output /tmp/shed-panel-persistence.json
```

The calculation uses the official [SHED data releases](https://www.federalreserve.gov/consumerscommunities/shed_data.htm), the 2024 [codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2024codebook.pdf), and the 2025 codebook. The raw files and JSON output are not committed.

Related: [2025 SHED price-adaptation layer](shed-2025-price-adaptation-layer-v1.md), [economic adaptation, perception, and public action layer](../us-cost-trust-politics/economic-adaptation-perception-action-layer-v1.md), and the [broad event ledger](../../templates/US-BROAD-EVENT-LEDGER_V1.md).
