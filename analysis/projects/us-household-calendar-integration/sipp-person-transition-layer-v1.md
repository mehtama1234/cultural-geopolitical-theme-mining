# SIPP person-transition layer v1

**Run date:** 2026-09-12  
**Source:** 2025 SIPP public-use pipe file, 2024 reference year  
**Method:** [analyze_sipp_person_transitions.py](../../../scripts/analyze_sipp_person_transitions.py) on the 35-field full extraction
**Person-month key:** `SSUID` + `SHHADID` + `PNUM` + `MONTHCODE`  
**Weight:** `WPFINWGT` from the first month of each adjacent pair

## What the identifiers make possible

The rerun identified 31,992 people in the selected slice. Of those, 31,090 had all twelve reference months. There were 346,283 available adjacent-month pairs across the selected people. This establishes an engineering basis for within-SIPP person comparisons without joining unrelated surveys as if they followed the same people.

## The transition diagnostic

| Field | Complete adjacent pairs with nonblank values | Largest observed transition shares |
|---|---:|---|
| `EAWBMORT` unable to pay rent/mortgage | 346,283 | no → no 95.37%; yes → yes 4.63% |
| `EAWBGAS` unable to pay utility bills | 346,283 | no → no 92.95%; yes → yes 7.05% |
| `RFOODS` food-security status | 346,283 | high/marginal → high/marginal 88.58%; low → low 7.07%; very low → very low 4.35% |
| `EFOOD6` hungry but did not eat because of money | 57,532 | no → no 74.42%; yes → yes 25.58% |
| `RMNUMJOBS` monthly number of jobs | 297,861 | one → one 53.37%; zero → zero 40.32%; two → two 4.30%; one → zero 0.49%; zero → one 0.48% |
| `THINCPOV` monthly household income-to-poverty-ratio band | 346,160 | 4x-or-more → 4x-or-more 45.75%; 2–4x → 2–4x 27.95%; 1–2x → 1–2x 13.56%; below 1x → below 1x 9.07% |

## The important interpretation boundary

The apparent persistence of `EAWBMORT`, `EAWBGAS`, `RFOODS`, and `EFOOD6` cannot be called monthly persistence from this run. The Data Dictionary describes these selected questions as annual or reference-period household measures, even though the values appear on monthly person records. Repeating the value across months can reflect survey design and copying, not a new monthly question or a newly observed event.

`RMNUMJOBS` is explicitly a number of jobs held within the reference month, so its adjacent-month transitions are a more appropriate longitudinal diagnostic. Even there, the table is descriptive: it does not show hours, pay, schedule control, benefits, reasons for a job change, or whether a household gained or lost room.

`THINCPOV` is also explicitly monthly. In the transition diagnostic, 3.67% of weighted nonblank adjacent pairs changed income-to-poverty-ratio band, compared with 1.70% of weighted nonblank job-count pairs that changed job-count category. The two percentages are not directly comparable outcomes: they use different valid-pair sets and band definitions. They do show why a household can have a stable job count while its monthly resource position changes, or the reverse.

## Why this matters for the broad program

The person identifier prevents one major error—treating unrelated rows as the same person—but it does not turn every SIPP field into a monthly event series. The broad research chain must distinguish:

- a genuinely monthly condition or decision;
- an annual or reference-period measure copied into monthly records;
- a household measure repeated across members; and
- a person measure with its own age or universe rule.

This is exactly the difference between observing a population pattern and claiming an end-to-end change in daily life. SIPP can provide the population and longitudinal backbone, but exact bills, service contacts, remedies, firm behavior, cultural interpretation, political action, and geopolitical consequences still require other source families or a purpose-built panel.

## Next test

Use the person-month key for fields explicitly defined monthly—income-to-poverty ratio, income, earnings, jobs, employment, and selected program or household-change variables—after adding their status flags and universes. Keep annual food, housing-difficulty, and care questions as reference-period outcomes unless the documentation supports a different timing interpretation.
