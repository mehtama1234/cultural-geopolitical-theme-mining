# SHED panel income × financial-condition path layer v1

**Checked:** 2026-09-16
**Unit:** recontacted SHED respondent; 2024 to 2025  
**Sample:** 4,419 recontacted respondents with a valid condition path and 2025 income band
**Method:** descriptive weighted cross-tab using 2025 `panel_weight`; no variance estimate or causal model
**Machine output:** [income × condition path data](data/shed-panel-adaptation-income-path-2024-2025.json)

## Why this layer matters

The earlier panel layer showed that adaptations persist differently when a
respondent's broad financial condition worsens, stays similar, or improves.
The earlier cross-sectional layer showed income differences in adaptation. This
layer puts those two axes together: reported income band × financial-condition
path among the same recontacted respondents.

It is still not a household case study. It is a population-panel comparison
of how resources and changing condition may jointly structure the adaptation
menu.

## Definitions

Income bands use the 2025 reported `ppinc7` categories:

- **under $50k:** less than $10,000 through $49,999;
- **$50k–$99k:** $50,000 through $99,999;
- **$100k or more:** $100,000 through $149,999 and $150,000 or more.

Condition paths order 2024 and 2025 `B2` as finding it difficult, just getting
by, doing okay, and living comfortably. A path is worsened, same broad
condition, or improved. Within each cell, persistence is the share reporting
Yes in 2025 among those reporting Yes in 2024; re-entry is Yes in 2025 among
those reporting No in 2024.

The file contains **4,419** respondents with both a valid condition path and a
valid 2025 income band. Cell counts below are unweighted paired-record counts.

The current storage-light rerun reproduced the 4,419-row frame and wrote the
machine output linked above. It reads the two existing local SHED ZIP files and
does not copy raw respondent rows into Git.

## Persistence among prior adopters

| Income band | Condition path (paired records) | Cheaper products | Used less/stopped | Reduced savings | Increased borrowing | Delayed purchase | Emergency funds |
|---|---:|---:|---:|---:|---:|---:|---:|
| Under $50k | Worsened (217) | 89.9% | 83.9% | 60.2% | 61.5% | 75.2% | 59.8% |
| Under $50k | Same (541) | 83.0% | 80.7% | 65.1% | 65.7% | 75.8% | 70.6% |
| Under $50k | Improved (200) | 70.3% | 72.6% | 52.3% | 48.4% | 58.4% | 68.1% |
| $50k–$99k | Worsened (216) | 87.4% | 86.6% | 76.5% | 57.0% | 72.8% | 70.0% |
| $50k–$99k | Same (681) | 79.1% | 71.6% | 57.7% | 45.6% | 64.1% | 83.8% |
| $50k–$99k | Improved (208) | 62.0% | 57.8% | 53.5% | 40.4% | 58.5% | 81.7% |
| $100k+ | Worsened (371) | 84.1% | 84.2% | 77.3% | 76.9% | 77.4% | 79.6% |
| $100k+ | Same (1,644) | 70.6% | 69.1% | 55.7% | 45.0% | 61.2% | 91.0% |
| $100k+ | Improved (341) | 72.6% | 67.4% | 57.7% | 45.8% | 54.2% | 89.1% |

The broad pattern is that improvement is generally associated with lower
persistence of reduced use, saving cuts, borrowing, and delayed purchases,
while emergency capacity is higher in the higher-income bands. But the cells
are not a simple monotonic law: for example, borrowing persistence among the
high-income worsening cell is high, and some same-condition cells exceed
worsening cells. This is precisely why the table should be read as a
distributional diagnostic, not a mechanical income effect. Financial shocks,
debt, health, household composition, employment, and selective recontact may
be distributed differently within each cell.

## Re-entry among prior non-adopters

| Income band | Condition path | Cheaper products | Used less/stopped | Reduced savings | Increased borrowing | Delayed purchase |
|---|---|---:|---:|---:|---:|---:|
| Under $50k | Worsened | 49.2% | 43.0% | 39.4% | 15.1% | 44.4% |
| Under $50k | Improved | 32.9% | 38.2% | 21.3% | 8.4% | 29.3% |
| $50k–$99k | Worsened | 55.7% | 57.6% | 39.0% | 16.6% | 34.2% |
| $50k–$99k | Improved | 26.6% | 22.1% | 19.8% | 5.1% | 23.3% |
| $100k+ | Worsened | 50.1% | 57.8% | 42.1% | 10.9% | 43.6% |
| $100k+ | Improved | 27.0% | 29.3% | 20.0% | 4.8% | 24.7% |

Among prior non-adopters, worsening paths generally show more entry into
reported adaptations than improving paths. That is consistent with a pressure
response, but it does not identify whether the path caused the adaptation or
whether an unmeasured shock changed both.

## What this adds to the broad societal program

1. **Resources and change interact.** A static income cut and a dynamic
   financial-condition path answer different questions; the intersection
   shows why both are needed.
2. **Adaptation is behavior-specific.** Reduced use, borrowing, saving cuts,
   delayed purchases, and emergency funds do not move as one latent stress
   score.
3. **The same income band contains different trajectories.** A respondent
   below $50k whose condition improves is not equivalent to one whose condition
   worsens, and neither is equivalent to a higher-income respondent on the
   same path.
4. **Demographic inequality is not an explanation.** Income band locates
   resources; the mechanism may be debt, housing, care, health, employment,
   discrimination, place, or family support.
5. **Downstream societal meaning remains open.** The panel does not measure
   who is blamed, whether trust changes, whether a firm is exited, or whether
   political action follows.

## Boundaries and counterexamples

The 2025 income band is reported at the later wave and is not a measure of
wealth or liquid cash. The panel is recontact-selected; `panel_weight` does
not eliminate every nonresponse or attrition mechanism. No replicate-weight
standard errors are calculated here. Adaptation questions refer to a prior
period, not a dated price, bill, firm, policy, or health event. The unusually
high or non-monotonic cells are not errors to smooth away; they are reminders
that composition and sample size matter.

A decisive counterexample is a low-income respondent whose condition worsened
but whose adaptation ended, or a high-income respondent whose condition
improved but who continued borrowing or reduced use because of durable debt,
care, health, or housing needs. Those cases prevent a simple “income causes
adaptation” story.

## Reproduction

```text
python3 scripts/analyze_shed_panel_adaptation_income_path.py \
  --old /path/to/SHED_public_use_data_2024_(CSV).zip \
  --new /path/to/SHED_2025.csv.zip \
  --output analysis/projects/us-household-financial-pressure/data/shed-panel-adaptation-income-path-2024-2025.json
```

The analysis uses the official [Federal Reserve SHED data releases](https://www.federalreserve.gov/consumerscommunities/shed_data.htm). Raw files remain outside the repository; only aggregate JSON is committed.
