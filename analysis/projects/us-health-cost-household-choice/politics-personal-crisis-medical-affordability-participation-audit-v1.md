# Medical-affordability crisis to political participation acquisition audit v1

**Checked:** 2026-09-15  
**Status:** public-replication exploratory descriptive layer; not causal and not a standalone published medical-crisis coefficient

## Why this source matters

The health-cost lane still needed a same-respondent link from a concrete
medical-cost hardship to political action. The Politics of Personal Crisis
study is a strong acquisition candidate because its Cooperative Election Study
(CES) crisis modules ask whether respondents had trouble affording medical
expenses and also measure validated turnout plus six non-voting political
acts. The module extracts additionally carry responsibility-attribution items
for the medical-expense crisis.

The paper's primary models use the total number of personal crises, rather
than publishing a standalone coefficient for the medical-expense item. This
audit therefore separates three claims:

```text
medical-expense hardship is measured in the same respondent architecture
    -> descriptive turnout / participation contrasts can be computed
    -> the published paper supports a broader crisis-to-participation result
    -> a medical-specific causal or adjusted political effect remains open
```

## Primary source and public files

- Ojeda, Michener, and Haselswerdt, “The Politics of Personal Crisis: How
  Life Disruptions Shape Political Participation,” *Political Behavior*.
  [Publisher article](https://link.springer.com/article/10.1007/s11109-024-09933-x)
- [Harvard Dataverse replication package DOI](https://doi.org/10.7910/DVN/PJQ57U)
- The package's Stata programs are `crisis_rep_2018common.do`,
  `crisis_rep_2018module.do`, `crisis_rep_2020common.do`, and
  `crisis_rep_2020module.do`.

The public module extracts used for this audit are `CCES18_crisis_vv.tab` and
`CCES20_crisis_vv.tab`. Although the Dataverse metadata labels these files as
`.tab`, they are Stata release-118 data files. The downloaded-file hashes are:

| File | Bytes | SHA-256 |
|---|---:|---|
| `CCES18_crisis_vv.tab` | 4,411,279 | `c61ccc59c7f9232cbb7abd420654b907cb0997433c80ce0efe391d4f257d3d58` |
| `CCES20_crisis_vv.tab` | 5,829,247 | `10fe9927942f345b9b39f58b4c07daa130baa997537f4cecfe76e6d7c024cd1e` |
| `crisis_rep_2018common.do` | 3,207 | `7c68771b9caff0e12c2d534b2d1459f9b95445828cc2f7aae0131c0682e4e292` |
| `crisis_rep_2020common.do` | 4,617 | `932c52db9f85c769353c91b90d5adc66f93b7235b72794f3b862dd8b20353e7e` |

The file sizes above are acquisition metadata, not analysis denominators; the
authoritative denominator for the calculations below is the number of valid
rows read from each Stata file.

## Variables and design

The key fields are:

- `crisis_medexp`: “Trouble affording medical expenses” / “Had trouble
  affording medical expenses.”
- `voted_valid`: validated vote indicator.
- `part_meeting`, `part_sign`, `part_work`, `part_protest`, `part_contact`, and
  `part_donate`: past-year non-voting political activities.
- `teamweight`: the module weight used by the supplied replication programs.
- `voted2016_valid`: prior validated turnout, available for a future adjusted
  model.
- 2018 module attribution fields include `resp_medexp_badluck`,
  `resp_medexp_choices`, `resp_medexp_economy`, `resp_medexp_federal`,
  `resp_medexp_state`, and `resp_medexp_local`.
- 2020 module fields include `UTK356` (responsibility attribution for medical
  expenses), `UTK315` (timing), and `UTK302_2` (the medical-expense crisis
  item).

The descriptive rates below are weighted means of each binary outcome within
the medical-expense-crisis indicator, using `teamweight`. The denominators
reported are unweighted valid rows. No new survey-design standard errors are
claimed here: the small public extracts and the absence of a reproduced
survey-estimation run make these acquisition contrasts appropriate for
triage, not final inference.

## Same-respondent descriptive bridge

### 2018 CES module extract

There are 1,000 rows and 1,000 valid medical-expense-crisis indicators; 257
respondents report trouble affording medical expenses and 743 do not.

| Outcome | No medical-expense crisis | Medical-expense crisis |
|---|---:|---:|
| Validated turnout | 57.2% | 41.7% |
| Attend local political meeting | 10.8% | 6.4% |
| Put up political sign | 11.6% | 10.5% |
| Work for candidate/campaign | 5.2% | 3.8% |
| Attend protest/march/demonstration | 8.2% | 7.2% |
| Contact public official | 21.4% | 23.3% |
| Donate to candidate/campaign/organization | 17.4% | 10.7% |

The raw descriptive pattern is consistent with lower turnout and several
lower participation rates among respondents reporting medical-expense
hardship, with a small higher contact rate. That is not evidence that the
medical hardship caused disengagement: the crisis may proxy income, health,
age, prior participation, employment, insurance insecurity, or other crises.

### 2020 CES module extract

There are 1,000 rows and 1,000 valid medical-expense-crisis indicators; 152
respondents report trouble affording medical expenses and 848 do not.

| Outcome | No medical-expense crisis | Medical-expense crisis |
|---|---:|---:|
| Validated turnout | 62.3% | 61.2% |
| Attend local political meeting | 6.0% | 6.9% |
| Put up political sign | 17.0% | 13.7% |
| Work for candidate/campaign | 3.7% | 1.0% |
| Attend protest/march/demonstration | 5.4% | 9.1% |
| Contact public official | 17.9% | 28.3% |
| Donate to candidate/campaign/organization | 22.7% | 22.2% |

The 2020 extract shifts toward targeted contact and protest among hardship
respondents while showing lower sign and campaign-work rates. Turnout is
nearly equal. The cross-year contrast is useful: a medical-cost hardship does
not map to one universal political response, and the action channel may be
more targeted than general electoral participation.

## 2020 attribution mechanism screen

Among the 152 respondents reporting medical-expense hardship, the responsibility
item (`UTK356`) distributes as follows. Percentages use `teamweight`; counts
are unweighted and are shown so sparse cells remain visible.

| Attribution | Unweighted n | Weighted share |
|---|---:|---:|
| Bad luck | 23 | 14.9% |
| Personal choices | 14 | 8.7% |
| The economy | 44 | 25.4% |
| Federal government | 32 | 22.4% |
| State government | 15 | 14.1% |
| Local government | 1 | 0.2% |
| None of these | 23 | 14.4% |

The attribution split changes the political interpretation of the hardship
signal. Weighted contact with a public official was 42.7% among the federal-
government attribution group and 13.4% among the bad-luck group. Protest was
23.6% versus 4.0%, respectively. These are raw within-hardship contrasts,
not mediation estimates: the federal-government cell has only 32 unweighted
respondents, the bad-luck cell has 23, and attribution is itself a respondent
judgment that can be shaped by ideology, prior participation, question order,
and the surrounding 2020 context.

The result is still useful for the end-to-end architecture because it
distinguishes generalized hardship from institution-targeted response:

```text
medical affordability problem
  -> responsibility assigned to federal government
  -> higher observed contact/protest in this small cell
  -> candidate route toward pressure or legitimacy judgment
```

The final arrow remains open. The data do not measure whether contact or
protest produced a remedy, improved affordability, changed trust, or caused
political exit.

### 2018 attribution cross-check

The 2018 questionnaire uses separate yes/no attribution flags rather than the
2020 single-choice `UTK356` item, so categories can overlap and their shares
must not be summed. Among the 257 hardship respondents, the weighted flag
shares were 24.9% bad luck, 13.1% personal choices, 29.1% the economy, 27.6%
the federal government, 21.0% the state government, 9.1% local government,
and 19.2% none of these. Official contact was 26.3% for respondents selecting
federal-government attribution and 21.5% for those selecting bad-luck
attribution; protest was 11.1% versus 5.4%.

This cross-check points in the same direction as 2020 for
government-attribution contact and protest, but it is not a clean replication:
the 2018 categories permit multiple selections, while 2020 reports one
attribution category, and the question wording/context differ. The two years
therefore support an attribution-aware test design, not a pooled estimate.

### Timing sensitivity inside 2020

The 2020 timing item also argues against treating the year as one homogeneous
shock. Among hardship respondents, the weighted official-contact rate was
27.6% for expenses reported before 2020, 11.9% for January–February 2020, and
31.1% for March 2020 or later. The corresponding protest rates were 10.1%,
0.0%, and 9.7%. The post-March group represents 54.9% of the hardship
group's weight and contains 93 unweighted respondents. These timing cells are
descriptive and not comparable event cohorts: the question asks about a broad
prior period, the election-year action window differs from the hardship window,
and pandemic conditions may alter both need and political opportunity.

## Basic adjusted extension

As a sensitivity screen, I fit separate weighted logistic models for validated
turnout and each participation act. The focal indicator is `crisis_medexp`;
the models also include `total_crises - crisis_medexp`, prior validated turnout,
sex, Black indicator, Hispanic indicator, other-race indicator, age, education,
income, marital status, church attendance, and presence of a child under 18.
The supplied `teamweight` is used as a frequency weight. Standard errors are
HC1 model-robust standard errors, not CES Taylor-series design estimates.

The table reports the odds ratio for medical-expense hardship, with a model
95% interval in parentheses. Each outcome uses its own complete-case sample;
2018 models use 883 rows and 2020 models use 888 rows.

| Outcome | 2018 OR (95% model interval) | 2020 OR (95% model interval) |
|---|---:|---:|
| Validated turnout | 0.93 (0.52–1.65) | 1.22 (0.66–2.26) |
| Attend local meeting | 0.75 (0.40–1.43) | 1.36 (0.53–3.46) |
| Put up political sign | 1.27 (0.74–2.19) | 0.51 (0.27–0.97) |
| Work for campaign | 0.73 (0.34–1.53) | 0.22 (0.03–1.61) |
| Attend protest | 1.15 (0.60–2.22) | 1.28 (0.53–3.12) |
| Contact public official | 1.69 (1.11–2.59) | 1.80 (1.02–3.16) |
| Donate | 1.15 (0.68–1.95) | 1.05 (0.58–1.92) |

The most stable-looking result in this exploratory screen is the contact
outcome: the medical-hardship indicator is positively associated with official
contact in both years after basic adjustment. The 2020 sign estimate points
downward, while turnout and most other actions remain imprecise or cross one.
This supports a targeted-pressure hypothesis more than a universal
disengagement hypothesis, but the model is not a causal estimate and the
intervals are not design-based. The contact result should therefore be treated
as a candidate for a properly weighted survey-design replication.

A pooled model combining the two extracts gives a medical-hardship contact odds
ratio of 1.83 (HC1 model-robust 95% interval 1.22–2.75; 1,771 complete cases).
The hardship × 2020 interaction is 0.96 (0.49–1.87; p=0.896), so this screen
does not distinguish the 2018 and 2020 contact associations. The corresponding
protest interaction is 1.06 (0.38–2.93; p=0.917). This is a stability screen,
not a pooled population estimate: the extracts have different survey contexts,
the weights are not harmonized into a longitudinal design, and uncertainty is
model-robust rather than survey-design based.

## What the published paper establishes

The paper analyzes CES Common Content/Module data from 2018 and 2020, along
with the Democracy Fund VOTER Survey. It reports that personal crises generally
dampen validated turnout, while some forms of non-voting participation can
increase, especially targeted action. Its principal explanatory variable is
the aggregate count of crises, and the authors explicitly caution that the
design is not causal: crises are measured at one point, the paper controls for
prior turnout but not prior crisis levels, and crisis exposure is not randomly
assigned.

That published result closes an important architecture gap but not the
medical-specific inference gap. The replication programs confirm that
`crisis_medexp` enters the crisis inventory and that the participation
outcomes are modeled from total crises. A future model can use the public
files to estimate medical-expense hardship alongside other crises and prior
turnout, but it should be labeled as an analyst-produced extension.

## Attribution and legitimacy path

The module variables make the next bridge unusually concrete:

```text
trouble affording medical expenses
  -> who respondents blame (bad luck, choices, economy, federal/state/local government)
  -> whether they contact officials, protest, vote, donate, or disengage
  -> whether the response is targeted institutional pressure or generalized exit
```

This is the most promising next test for the health-cost lane. It should use
the 2018 and 2020 module files, retain `teamweight`, include prior turnout and
the supplied demographic controls, and report outcome-specific estimates with
confidence intervals. The model should not collapse blame into a single
“trust” score: blaming government, blaming economic conditions, and blaming
oneself imply different legitimacy and remedy pathways.

## VOTER companion-file boundary check

The replication package also distributes `VOTER_2019vv_crisis.tab`, a 9,548-row
Democracy Fund VOTER Survey panel extract with institutional-confidence and
government-trust variables. A metadata audit of the pinned public file found
no `crisis_medexp` field and no medical-expense hardship field under an
equivalent name. The file therefore cannot produce a same-respondent
medical-hardship-to-trust estimate, despite containing useful general trust
and confidence measures.

This negative result matters for the end-to-end boundary: the CES module
extracts support hardship-to-action and hardship-to-attribution links, while
the VOTER extract supports a separate trust context. Combining them would be
a cross-source bridge, not matched evidence. The episode-level chain
`medical bill -> care/payment adaptation -> institutional remedy -> trust or
exit` remains open.

## Limits and next action

- The 1,000-row extracts are public module extracts, not the full CES files;
  do not generalize their raw weighted contrasts beyond the documented module
  design.
- The contrasts are not adjusted regressions and have no reproduced design-
  based standard errors in this audit.
- The paper's strongest published coefficient is for total crisis exposure,
  not the medical-affordability item alone.
- The 2018 and 2020 questions refer to the prior year, so the temporal link to
  the participation measures is broad rather than event dated.
- Attribution categories are sparse in the 2020 hardship group, especially
  local-government attribution; no category-level ranking should be treated
  as stable without a larger design-based replication.
- The adjusted extension uses model-robust rather than CES design-based
  uncertainty; its intervals are screening diagnostics only.
- The VOTER companion extract does not contain the medical-expense hardship
  item needed to match its trust variables to the CES medical-cost exposure.
- The result does not observe a bill amount, care delayed, payment plan,
  collections, insurer/provider remedy, or institutional response.

Next, run a pre-registered medical-specific extension over the public module
files: medical-expense hardship as the focal exposure; total other crises,
prior validated turnout, and the supplied demographic controls as covariates;
each political action as a separate outcome; and attribution categories as
mediator/heterogeneity candidates. Preserve the raw contrasts above as the
descriptive baseline and do not promote the extension into the atlas until
its design-based uncertainty and exact coding are validated.

The current screening implementation is preserved in
`scripts/analyze_ces_medical_affordability_political_action.py`:

```text
python3 scripts/acquire_ces_personal_crisis_replication.py \
  --output-dir /tmp/cgtm-cces-personal-crisis

python3 scripts/analyze_ces_medical_affordability_political_action.py \
  --input-2018 /tmp/cgtm-cces-personal-crisis/CCES18_crisis_vv.tab \
  --input-2020 /tmp/cgtm-cces-personal-crisis/CCES20_crisis_vv.tab \
  --output /tmp/ces-medical-affordability-action.json
```

`acquire_ces_personal_crisis_replication.py` pins the Dataverse file IDs and
refuses to complete if any downloaded file's SHA-256 differs from the checked
replication package. The acquisition manifest preserves the file-level hashes
and byte counts for later refresh audits.
