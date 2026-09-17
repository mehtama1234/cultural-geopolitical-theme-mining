# UAS health-cost episode and legitimacy acquisition audit v1

**Checked:** 2026-09-17
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

## Access verification (2026-09-16)

The official UAS pages were rechecked on 2026-09-15. USC describes UAS as a
probability-based panel of approximately 15,000 U.S. residents and provides a
public metadata/explorer route. The [data-access
page](https://uasdata.usc.edu/index.php?pid=Data+Access&type=3) states that
downloadable survey files are available to registered data users, while the
[access conditions](https://uasdata.usc.edu/index.php?pid=Terms+and+conditions&type=3)
require an account and the applicable data-use agreement. The [Monthly Panel
page](https://uasdata.usc.edu/index.php?pid=Monthly+Surveys&type=3) continues to
label the file download as registration required. The current [UAS home
page](https://uasdata.usc.edu/index.php) also distinguishes the public
Interactive Data Explorer from research-file access.

The 2026-09-16 page recheck also confirms the substantive fit of the route:
the Monthly Panel description says that each respondent-wave record covers
the preceding month and includes medical expenditures alongside health,
employment, life-satisfaction, and pain measures. The public routing pages for
UAS 537 and UAS 698 expose candidate care-access, bill, outside-help,
provider-experience, and institution-specific trust questions. These are
documented candidate fields only; they do not establish that the files share a
usable respondent-wave overlap, weights, or a complete episode.

### Live endpoint access probe (2026-09-16)

A small live probe of the official Monthly Surveys page returned HTTP 200 and
reconfirmed the public metadata: the Monthly Panel covers October 2023 onward,
uses one respondent-by-wave record, and describes prior-month employment,
health, financial, life-satisfaction, pain, and meaning/purpose measures. The
linked Monthly Panel dataset request returned the UAS login page (the page
identifies itself as `/page/Login` and offers registration), rather than a
data-file response. This is positive evidence that the documentation route is
available and direct evidence that the respondent file remains
registration-gated; it is not a zero-row or failed-data result. No dataset was
downloaded during this probe.

This recheck confirms that public metadata and visualization are available,
but it does not create a public microdata substitute. The UAS terms page is
marked updated 07/09/2026, so the repository records the current access
condition rather than relying on an older description. The UAS data-access
guidance requires a data-user account and submitted agreement.
Accordingly, there is no public-file substitute to add to this repository at
present. The next operational step is to register through the [UAS data
access page](https://uasdata.usc.edu/index.php?pid=Types+Of+Data&type=3), accept
the conditions of use, and then acquire the [Monthly Panel
Dataset](https://uasdata.usc.edu/index.php?pid=Monthly+Surveys&type=3), UAS 537,
and UAS 698 files. This is an access prerequisite, not evidence for any
health-cost result.

### Current access recheck (2026-09-17)

The official Monthly Surveys and Data Access pages were fetched again on
2026-09-17. Both returned HTTP 200 and continued to expose the Monthly Panel
and Older Ages download links. The Monthly Panel dataset link redirected to
the UAS login page and displayed “To complete this action please login first”;
it did not return a data file. The public page still describes the Monthly
Panel as October 2023 to the present and labels the dataset download
registration-required. This is a direct access-boundary observation, not an
empty-file result and not a reason to estimate from the public explorer.

No respondent file was downloaded or retained in this recheck. The route
remains ready for the smallest authenticated acquisition: the Older Ages panel
and codebook first, followed by the broader Monthly Panel or UAS 537/698 only
if the structural key, timing, and candidate episode fields pass.

### Overall-workspace retention search — 2026-09-17

Before treating registration-gated access as the only explanation for the
missing file, a read-only filename search was run across
`/home/mehtama1/git-repo` for retained UAS, Older Ages, Understanding America
Study, and related health-cost data files. It returned no matching data-file
paths. This is a bounded workspace-retention check, not evidence that no copy
exists outside the workspace or under an unrelated filename; it does confirm
that no obvious local substitute is available to the current program. No file
was downloaded, copied, or changed. The acquisition boundary therefore remains
registration/account access plus post-acquisition key, wave, weight, and
missingness checks.

### UAS 537 public metadata recheck — 2026-09-17

The official [UAS 537 survey page](https://uasdata.usc.edu/index.php?r=eNpLtDKyqi62MrFSKkhMT1WyLrYytFwwskuTcjKT9VISSxL1ikuLylIrQTJARcXFmSkgprGVkqmxuZJ1LVwwjUMTrg%2C%2C)
identifies the module as *Future of health care* and exposes separate
utilization, billing, perceptions, satisfaction/access/health-status, and
closing sections. It reports a selected sample of 1,233, 1,136 completed
surveys, 3 started-but-incomplete surveys, 94 non-starts, a 92.13% response
rate, English/Spanish administration, field dates of August 14–October 14,
2023, and an average completion time of 16 minutes. The page also explicitly
requires login to download the data.

This strengthens the route specification in two ways: the module's public
metadata confirms that billing, access, and institutional-perception surfaces
coexist in one respondent-selected survey, and it supplies the response
denominator needed for the later overlap audit. It still does not establish
the exact usable microdata columns, module-to-panel linkage, weights,
respondent-level dates, or a same-episode remedy/action result. The public
metadata therefore advances acquisition readiness, not the health-cost or
legitimacy finding itself. No file was downloaded.

### Older Ages Monthly Events: event-first alternative

The official [Older Ages Monthly Events Panel description](https://uasdata.usc.edu/page/UAS+Monthly+Surveys)
identifies a particularly useful lower-scope route. It covers 52 monthly waves
from June 2019 through September 2023, asks about events in the preceding
calendar month, and includes approximately 5,426 respondents aged 50 or older
who completed at least one wave. The documented panel structure is one
`uasid`-by-`wave` row with a stable respondent key, wave metadata, and a
separate contemporaneous household identifier.

Its event architecture is stronger than a generic annual recall screen: the
description lists 17 monthly event blocks, date fields for event occurrence,
repeat-event confirmation fields for selected events, and monthly measures of
medical expenditures, health, pain, life satisfaction, hours worked, earnings,
and employment changes. The documented medical-expenditure fields include
out-of-pocket medical, hospital, doctor, dental, and other-medical amounts.
This makes it the smallest identified candidate for an event-first screen such
as:

```text
dated illness, financial setback, or medical expenditure
  -> next-wave health, pain, work, earnings, or life satisfaction
  -> linked trust, provider experience, remedy, or action module
```

The age restriction is substantive: this route cannot replace the broader
October 2023–present Monthly Panel for working-age coverage. It also does not
by itself document a provider/insurer trust or verified-remedy endpoint. The
dataset and codebook remain registration-gated, so this is a documented
acquisition priority, not a completed estimate. Once access exists, acquire
only the Older Ages panel and its codebook first, run the key/wave/missingness/
weight audit, and stop before adding UAS 537/698 unless the event and outcome
fields pass.

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
| UAS Older Ages Monthly Events, June 2019–September 2023 | 52 monthly waves; age-50+ respondents; 17 event blocks with event dates and selected repeat-event confirmation; previous-month medical expenditures, work hours/earnings, health, life satisfaction, pain, and employment change | Event-first medical-spending/illness/financial-setback timing to later health, work, and well-being, with a precisely defined older-age universe | No documented same-file political-trust or verified-remedy endpoint in the public summary; link to core/special modules and retain age restriction |

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

### Live public-variable inventory probe (2026-09-16)

A fresh request to the explorer page and its public dropdown endpoint returned
HTTP-success responses without downloading survey microdata. The endpoint
`https://uasvis.usc.edu/monthly/getdropdownsmonthly.php` listed
`cornegfinshock`, `corhealthevent`, overall health, pain, food-security items,
life satisfaction, and `meaningthetas_tscore_3_`, among other aggregate
variables. It did not list `fin3s4` or a medical/dental-expense-specific
equivalent. The retrieved dropdown script was 1,220 bytes with SHA-256
`9fb4fa5bcb8ec168b216dc939535bb28a5ae796e41955688263d85286fc1be69`; the page
was 18,736 bytes with SHA-256
`f34f36f361ad57b007fa9d88fda0582d9a45ac9e3d2f35ced6a019675068b521`.
This is a current public-inventory observation, not evidence that the
registration-gated microdata lack the field. It confirms that the explorer
cannot currently close the medical-expense-to-later-outcome arrow.

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
It also records each file's distinct wave count and observed wave values, making
temporal coverage inspectable before respondent overlap is interpreted.
Pairwise overlap includes the retained share of each file's unique respondents,
so module attrition is visible rather than hidden behind an intersection count.
When both files expose waves, it also reports shared respondent-wave keys and
their shares. This separates same-person overlap from same-period overlap,
which is the minimum temporal check before a module-to-panel sequence is built.

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
- [UAS Older Ages Monthly Surveys page and panel description](https://uasdata.usc.edu/page/UAS+Monthly+Surveys)
- [UAS Older Ages Monthly Events Panel Dataset description and codebook](https://uasdata.usc.edu/index.php?r=eNpodzEEKwjAQheGrDDlAwVwiKOmqWJdSQTzANDPWYDoTmlQR8e6m7t7iez_a2n6S3VoTcWTTJFvvy16G4F1F6paJJWP2KqQvCYq0msIFpz_fbay5thfoA_EM7cgJTir5Ht5wfJYvnFE4QIcZE2foOLnZxzUIKAQHJR5UH1Wkm2m-P3nnMPY%2C)
- [UAS Interactive Monthly Panel Data Explorer](https://uasvis.usc.edu/monthly/monthlyvisualization.php)
- [UAS 537 future-of-health-care questionnaire](https://uasdata.usc.edu/output/paperversion/index.php?r=eNpLtDK2qi62MrFSKkhMT1WyLrYyBLFLk3Iyk_WK8ktLMvPSQaJAweLizBQQ09hKydTYHCZYChE0tFIyVLKuBVwwx5cXVA%2C%2C)
- [UAS 698 health-cost questionnaire](https://uasdata.usc.edu/output/paperversion/index.php?r=eNpLtDK2qi62MrFSKkhMT1WyLrYyBLFLk3Iyk_WK8ktLMvPSQaJAweLizBQQ09hKyczSAiZYChE0tFIyUbKuBVwwyGMXXw%2C%2C)
