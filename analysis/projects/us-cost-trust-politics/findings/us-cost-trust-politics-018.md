# Linked HTOPS respondents show material and institutional measures changing on different paths

**Status:** provisional same-respondent descriptive panel finding · **Checked:** 2026-09-14

## The bounded finding

The April and June 2025 HTOPS public-use files can be linked through their
scrambled respondent identifier. Of 8,850 April respondents and 7,485 June
respondents, 6,564 IDs appear in both files: 74.2% of the April file and 87.7%
of the June file. Within that retained linked sample, material conditions show
both persistence and movement. Any difficulty paying usual expenses persisted
for 41.8% of the baseline-weighted valid linked sample and appeared among an
additional 8.4%; 7.5% moved from difficulty to no difficulty. Food insufficiency
was less prevalent and more episodic: 3.9% remained insufficient, 2.7% entered
the condition, and 2.9% exited it.

The panel therefore strengthens the end-to-end architecture by holding a
respondent identifier across two 2025 releases. It does not establish that a
price, energy bill, job loss, or institution caused the transition. The linked
sample is selected, and the April public-use weight is not a documented
attrition-adjusted longitudinal weight.

The new [baseline-retention audit](../data/htops-2025-panel-attrition-audit.json)
shows why that limitation matters: unweighted retention is 69.5% in the
under-$50,000 income bands versus 76.7% in the $100,000-plus bands, 70.8% for
those reporting expense difficulty versus 76.6% for those not reporting it, and
63.0% among the small baseline food-insufficient cell. These are diagnostics of
who remains linkable, not corrections or estimates of attrition bias.

## Selected linked transitions

Percentages use the April person weight among valid linked respondents;
parentheses are approximate standard errors from the April 80-replicate file.

| Measure | No → No | No → Yes | Yes → No | Yes → Yes | Interpretation boundary |
|---|---:|---:|---:|---:|---|
| Any expense difficulty | 42.4 (0.99) | 8.4 (0.55) | 7.5 (0.59) | 41.8 (1.09) | Broad usual-expense measure over a two-month reference period |
| Food insufficiency | 90.4 (1.02) | 2.7 (0.45) | 2.9 (0.88) | 3.9 (0.61) | Seven-day food-sufficiency item, not a full annual food-security panel |
| Unable to pay an energy bill | 84.9 (0.80) | 3.2 (0.37) | 3.4 (0.40) | 8.6 (0.66) | No dollar amount, arrears duration, or correction/assistance outcome |
| Perceived prices increased | 12.0 (0.63) | 5.3 (0.46) | 12.8 (0.80) | 69.9 (1.05) | Perception, not an objective price exposure or household basket |
| Recent household job loss | 87.9 (0.85) | 4.0 (0.46) | 4.8 (0.63) | 3.3 (0.53) | Four-week reported household job-loss item |
| Agreed policymakers need federal statistics | 10.2 (1.01) | 7.9 (0.46) | 7.5 (0.76) | 74.5 (1.15) | This 2025 agreement item is not identical to 2026 federal-statistics trust |
| High confidence in Congress | 77.7 (1.09) | 5.2 (0.52) | 5.3 (0.60) | 11.8 (0.78) | Confidence persistence, not legitimacy, attribution, or political action |

The transition cells are mutually exclusive within each item and sum to the
valid linked denominator. They should not be read as a population transition
rate: the retained panel may differ from nonlinked respondents, and the public
files do not document a longitudinal weight correcting that selection.

## Cross-lagged material-to-outcome screen

The same linked sample supports a more direct but still bounded comparison.
Among respondents reporting baseline expense difficulty, 12.3% later reported
food insufficiency, 21.4% later reported inability to pay an energy bill, and
11.7% later reported household job loss. The corresponding figures among those
without baseline expense difficulty were 1.1%, 2.2%, and 2.9%. These cells are
descriptive follow-up associations among the selected linked sample; they do
not show that expense difficulty caused the later outcome, because both may
reflect an earlier unmeasured shock, household composition, health, debt,
employment, or selection into the linked sample.

The institutional endpoint is different: high Congress confidence in June was
17.2% among the baseline-expense-difficulty group and 16.9% among the group
without baseline difficulty. That near similarity is a useful counterexample
to treating a material-pressure association with later hardship as evidence of
a parallel trust response. Material security and institutional judgment must
remain separate outcomes.

The [cross-lagged audit data](../data/htops-2025-cross-lagged-panel-audit.json)
preserve the cell denominators and replicate-weight standard errors.

## What the linked design adds

### 1. Persistence and movement can be observed together

The broad expense item has a large persistent-difficulty cell and visible entry
and exit. Food insufficiency has smaller cells and more room for sampling and
timing variation. This is the kind of distinction that separate annual or
cross-sectional percentages conceal: the same aggregate prevalence can be
produced by stable hardship, turnover, or both.

### 2. Material and institutional measures are not one synchronized process

The federal-statistics agreement item has high persistence, while Congress
confidence is lower and has a different transition pattern. A respondent can
remain materially pressured while retaining an institutional judgment, change
that judgment without changing the broad expense state, or move through both
without a measured attribution. A linked identifier makes those combinations
testable; it does not explain them.

### 3. The question objects must remain separate

The 2025 federal-statistics item asks whether policymakers need federal
statistics for good decisions. The 2026 item asks whether the respondent tends
to trust federal statistics. They should not be pooled as one trust trend. The
2025 Congress item is comparable in wording to the 2026 confidence item, but
the panel result remains conditional on the selected linked sample and wave
weights.

### 4. The end-to-end bridge is still incomplete

```text
reported price, bill, job, or food condition
  -> same respondent's later condition
  -> institutional judgment
  -> action, recovery, appeal, or exit
```

This pass measures the first two states and selected judgment transitions. It
does not measure objective exposure, alternatives, schedule control, the actor
responsible, remedy, recovery, trust attribution, or political action. Those
remain the next acquisition and design requirements.

## Counterexamples kept visible

- A respondent can remain expense-pressured while food insufficiency resolves;
  general budget room and food endpoint are not interchangeable.
- A respondent can change price perception without a recorded job-loss change;
  perceived prices are not a complete exposure measure.
- A stable institutional judgment does not prove that an institution performed
  well; it may reflect identity, information, or an unrelated experience.
- Linked retention is high enough to inspect transitions but not proof that the
  matched subset represents all April or June respondents.
- A transition can reflect timing, recall, or questionnaire context rather than
  a durable change in the household's material world.

## Next test

First audit linked attrition by baseline income, race/ethnicity, age, sex,
children, region, and baseline pressure. Then condition transitions on a
dated price, energy, job, or benefit event where available, and connect the
same respondent to care/time, health, complaint, remedy, or action measures.
Keep the April-to-June panel separate from the 2026 cross-sectional snapshots;
the design break and question changes are part of the evidence.

## Sources and reproducibility

- [Census 2025 HTOPS/HPS public-use files](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.2025.html)
- [April 2025 PUF ZIP](https://www2.census.gov/programs-surveys/demo/datasets/hhp/2025/topical/HTOPS_HPS_2504_CSV.zip)
- [June 2025 PUF ZIP](https://www2.census.gov/programs-surveys/demo/datasets/hhp/2025/topical/HTOPS_HPS_2506_CSV.zip)
- [Machine-readable linked-panel record](../../../records/us-census-htops-material-trust-panel-april-june-2025.json)
- [Panel record builder](../../../../scripts/build_htops_2025_panel_2504_2506_record.py)
- [Baseline-retention audit data](../data/htops-2025-panel-attrition-audit.json)
- [Baseline-retention audit builder](../../../../scripts/audit_htops_2025_panel_attrition.py)
- [Cross-lagged audit builder](../../../../scripts/build_htops_2025_cross_lagged_panel_audit.py)
- [2026 Census cross-wave comparison](us-cost-trust-politics-017.md)

**Evidence status:** same-respondent linked descriptive transitions with
baseline replicate-weight precision for the retained sample; attrition-adjusted
population inference, dated exposure, causality, recovery, trust mechanism,
and political action remain open.
