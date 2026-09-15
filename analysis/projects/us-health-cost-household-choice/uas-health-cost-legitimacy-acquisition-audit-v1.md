# UAS health-cost episode and legitimacy acquisition audit v1

**Checked:** 2026-09-15  
**Status:** official documentation route verified; registration-gated microdata not yet acquired; no estimate promoted

## Why this is the next acquisition

The health-cost lane now has strong separate surfaces for cost-related care
foregoing, household adaptation, institutional response, trust, and political
action. It still lacks a source that can preserve one respondent across a
health-cost experience and a later judgment. The Understanding America Study
(UAS) is the strongest currently identified acquisition route because its
respondent identifier can link core, special-topic, and monthly panel files.

The route is not yet a completed finding. UAS data downloads are registration
gated, and the public documentation does not by itself establish the final
usable overlap, response timing, or weight availability. Those are acquisition
checks, not assumptions.

## Documented source architecture

USC describes the UAS Comprehensive File and Comprehensive Panel Dataset as
harmonized multi-wave data. The panel file has one respondent-by-wave record,
supports transitions and panel models, and can be linked to additional UAS
content with the `uasid` identifier. The source page says the latest listed
release was updated in June 2026.

The UAS Monthly Panel Survey covers October 2023 onward. Each record is an
individual-by-wave observation about the previous calendar month and includes
health, financial, employment, and subjective-well-being events, including
health, life satisfaction, pain, stress, and PROMIS meaning-and-purpose
measures. The Older Ages Monthly Events panel covers June 2019–September 2023
for respondents aged 50 and older and documents previous-month medical
expenditures alongside work and health measures.

The source architecture therefore supports a potentially ordered design:

```text
monthly health/financial event or special-module medical-cost experience
  -> care affordability, bill, payment, or foregoing choice
  -> subsequent health, work, financial, pain, or meaning measure
  -> later trust/satisfaction or institutional judgment
```

## Candidate modules and exact fields

| UAS route | Documented fields | What it could close | Boundary to verify after access |
|---|---|---|---|
| UAS 698 health-cost module | Health-care costs in the last two years, out-of-pocket amount, outside help with medical costs/insurance/long-term care, overall satisfaction with quality/cost/convenience, needed-but-not-received care, and reasons including unaffordability, scheduling, transportation, and waiting | Bill/payment burden, alternatives, care foregoing, support route, and satisfaction in the same respondent | Exact field names, dates/recall windows, module-to-core overlap, weights, missingness, and whether trust/action is in the linked wave |
| UAS 537 future-of-health-care module | Recent health-care visits and billing, unaffordable care since March 2020, current ability to afford services, transportation access, household medical bill that was unaffordable or disputed, provider-organization rating, and trust in hospitals and insurers after hospitalization | Direct bill/affordability, access alternative, provider experience, and institution-specific trust | The pandemic-recall window is broad; trust is conditional on hospitalization; verify usable overlap and survey weights |
| UAS Monthly Panel, October 2023–present | Previous-month health, financial, employment, life satisfaction, pain, stress, and meaning/purpose events; `fin3s4` identifies significant medical or dental expenses and `fin1_when_*` dates the financial change | A dated medical-expense-shock-to-subsequent-health/work/wellbeing backbone | The monthly core does not document bill amount, care choice, payment obligation, remedy, or trust; use UAS 537/698 for those fields and enumerate wave coverage |
| UAS Older Ages Monthly Events, June 2019–September 2023 | Previous-month medical expenditures, work hours/earnings, health, life satisfaction, and pain for age 50+ panel members | Monthly medical-spending-to-health/work/meaning timing for an older-age subsample | No documented same-file political-trust endpoint in the public summary; link to core/special modules and retain age restriction |

The questionnaire pages expose additional field-level anchors for the
acquisition script. In UAS 537 these include `avoidcare_cost` (needed care not
obtained because it was unaffordable), `hcb_ever` (a household medical bill
that was unaffordable or disputed), `afford_services`, `hrsntrust_hosp`, and
`hrsntrust_ins`. In UAS 698 the documented anchors include `N215` (money help
for medical expenses), `N333` (out-of-pocket amount for other medical
expenses), `N235` (overall satisfaction with health-care quality, cost, and
convenience), `N492` (needed medical care but did not get it), `N493` (reasons
for that gap), and `N295` (whether care preferences were taken into account).
These names are acquisition targets, not yet verified local columns.

The September 1, 2026 monthly-panel codebook adds a particularly useful
time-ordering anchor: `fin3s4` is the reported cause “significant medical or
dental care expenses for me or a family member,” while `fin1_when_month`,
`fin1_when_day`, and `fin1_when_year` record the date of the financial change.
The same codebook lists `le_hrs001_when_*` for illness timing and repeated
outcomes including `le_hrs_s1` (life satisfaction), `le_hrs_srh1` (overall
health), `le_hrs_p1` (pain), employment-shock fields, and
`meaningthetas_*` (meaning and purpose). This supports a bounded temporal
screen, but “significant medical or dental expense” remains a reported
financial shock—not a linked bill, treatment choice, or verified remedy.
The retrieved PDF was 521,561 bytes with SHA-256
`97af909996e341e99125ca8acd0a7258208a8b5afefeaf4df14ae4968c8af9f5`;
the hash identifies the documentation vintage used for this audit, not a
microdata release.

## Public aggregate-explorer boundary

USC also provides a public Interactive Monthly Panel Data Explorer. Its
published monthly variable inventory includes broad financial-shock and
health/wellbeing measures such as `cornegfinshock`, overall health, pain, life
satisfaction, and meaning. The published dropdown inventory does not expose
`fin3s4`, the medical-expense component required for the focal exposure. The
explorer can therefore provide context or broad time trends, but it cannot
produce the medical-expense-specific transition needed here. This check rules
out aggregate visualization as a substitute for the registration-gated
microdata acquisition.

## Required acquisition and merge test

After registration, acquire the relevant codebooks and data descriptions before
the microdata. Then perform the following checks in order:

1. Confirm `uasid` uniqueness within each file and one-to-many respondent-wave
   structure in the panel files.
2. Inventory exact variable names, value labels, wave dates, field dates,
   recall periods, module eligibility, and item-specific missing codes.
3. Confirm the correct respondent-level or wave-level weights and whether
   replicate/design variables are supplied for the special modules.
4. Match UAS 698 and UAS 537 respondents to adjacent core or panel waves and
   report the overlap and attrition denominator.
5. For monthly files, order the exposure by the previous calendar month and
   require the outcome wave to occur after that exposure; exclude same-period
   ambiguity where the documentation cannot separate event and outcome dates.
6. Preserve non-users and counterexamples: care obtained despite unaffordability
   concern, bills paid without reported sacrifice, unmet care for non-cost
   reasons, trust without a reported bill, and low trust without a health-cost
   exposure.

The September 1, 2026 monthly-panel description reports 35 waves from October
2023 through August 2026. It states that the panel uses `uasid` as the stable
person key, `uashhid` as the original household key, and `survhhid` as the
survey-specific household key; the latter can change when a respondent moves
between households. A valid household analysis must therefore use `survhhid`
only for the contemporaneous household and must not treat it as a permanent
household identity.

The repository contains a first-pass inventory tool at
`scripts/audit_uas_health_cost_legitimacy_files.py`. After registration and
download, run it once per acquired file (the names are analyst-chosen):

```text
python3 scripts/audit_uas_health_cost_legitimacy_files.py \
  --file monthly=/path/to/monthly_panel_latest.dta \
  --file uas537=/path/to/uas537.dta \
  --file uas698=/path/to/uas698.dta \
  --output /tmp/uas-health-cost-legitimacy-audit.json
```

The tool records SHA-256 hashes, format, row/column counts, candidate field
names and labels, key and wave uniqueness, missingness, and value-domain
counts. It is deliberately an acquisition audit; its output cannot by itself
support a causal or longitudinal estimate.

Once the monthly panel file is acquired, the bounded follow-up screen is
available at `scripts/analyze_uas_monthly_medical_expense_followup.py`:

```text
python3 scripts/analyze_uas_monthly_medical_expense_followup.py \
  /path/to/monthly_panel_latest.dta \
  --output /tmp/uas-monthly-medical-expense-followup.json
```

It compares `fin3s4=1` with `fin3s4=2` only when a later observed wave exists,
reports baseline and next-wave weighted means for health, life satisfaction,
pain, and meaning when present, records the input hash and exposure codes, and
does not claim design-based uncertainty. The comparison is a bounded
transition screen, not a bill-level causal estimate.

The follow-up script refuses to analyze a file with missing `uasid` values,
missing or nonnumeric wave values, or duplicate `uasid`-`wave` rows after
numeric normalization. This is a validity gate: a duplicate respondent-wave
record can make the apparent “next wave” depend on row order rather than survey
time. The file inventory audit should be run first so any such problem is
preserved as an acquisition finding rather than dropped during analysis.

The inventory output separately records `unique_person_wave_keys` and
`duplicate_person_wave_rows`. Repeated `uasid` values across different waves
are expected in a panel; repeated `uasid`-`wave` pairs are the structural issue
that must be resolved before a follow-up transition is interpretable.

After the individual file audits, run
`scripts/audit_uas_health_cost_legitimacy_merge.py` across the acquired files:

```text
python3 scripts/audit_uas_health_cost_legitimacy_merge.py \
  --file monthly=/path/to/monthly_panel_latest.dta \
  --file uas537=/path/to/uas537.dta \
  --file uas698=/path/to/uas698.dta \
  --output /tmp/uas-health-cost-legitimacy-merge.json
```

This records hashes, unique respondent counts, and pairwise `uasid` overlap
before any module merge. Overlap is only an acquisition prerequisite; it does
not establish wave alignment, item co-occurrence, or a usable episode.
The merge audit normalizes only an unambiguous trailing `.0` on integral IDs,
so ordinary CSV/Stata numeric formatting differences do not create false
non-overlap while leading-zero identifiers remain unchanged.

## Promotion rule

Promote a UAS result into the health-cost end-to-end finding only if one
respondent can be shown to have, in a documented sequence:

```text
dated or bounded health-cost exposure
  -> care/payment choice or bill dispute
  -> later health, work, financial, or meaning outcome
  -> later provider/insurer trust, satisfaction, complaint, switching, or action
```

The result must report the eligible overlap, denominator, panel retention,
weights, missingness, timing, subgroup, uncertainty, and a counterexample.
UAS 698/537 cross-sectional recall items may be promoted as a same-survey
episode-context layer, but not as longitudinal recovery or causal evidence.
The monthly panel can support a stronger temporal association only when its
codebook confirms the relevant medical-cost and later judgment fields.

## Current conclusion

UAS is the smallest credible next acquisition capable of closing more than
one remaining arrow at once. The monthly panel can test a dated reported
medical-expense shock against subsequent wellbeing and work; UAS 537/698 can
add bounded cost, care choice, alternatives, provider experience, and
institution-specific trust while preserving respondent identity. Until the
registration-gated microdata are acquired and the overlap is measured, the
correct status is **verified acquisition route**, not completed evidence.

## Official sources

- [UAS Comprehensive File and Panel Dataset](https://uasdata.usc.edu/index.php?pid=Comprehensive+File&type=3)
- [UAS Monthly Surveys data page](https://uasdata.usc.edu/index.php?pid=Monthly+Surveys&type=3)
- [UAS Monthly Panel Survey Dataset description and codebook, updated September 1, 2026](https://uasdata.usc.edu/index.php?r=eNodzEEKwjAQQNGrDDlAwVwiXCLTlditIJQeYJoZtZjOhCZRinh3W3d_8fiENX4S7tFFuotrEtbHtcsQRl-x-TKJZsqjKdtbgxFvZuVK058fduj6UwcX0_wIC1xcSSVAV-aXLNBSpiQZWkl-HuO2AVKGs7EMZs8q8s013x-3cS3L)
- [UAS Interactive Monthly Panel Data Explorer](https://uasvis.usc.edu/monthly/monthlyvisualization.php)
- [UAS 537 future-of-health-care questionnaire](https://uasdata.usc.edu/output/paperversion/index.php?r=eNpLtDK2qi62MrFSKkhMT1WyLrYyBLFLk3Iyk_WK8ktLMvPSQaJAweLizBQQ09hKydTYHCZYChE0tFIyVLKuBVwwx5cXVA%2C%2C)
- [UAS 698 health-cost questionnaire](https://uasdata.usc.edu/output/paperversion/index.php?r=eNpLtDK2qi62MrFSKkhMT1WyLrYyBLFLk3Iyk_WK8ktLMvPSQaJAweLizBQQ09hKyczSAiZYChE0tFIyUbKuBVwwyGMXXw%2C%2C)
