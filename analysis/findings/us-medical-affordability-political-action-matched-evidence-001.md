# Medical-cost hardship can become targeted political contact

## The argument

A respondent can experience trouble affording medical expenses without
responding through one universal political channel. In public 2018 and 2020
Cooperative Election Study (CES) crisis-module extracts, medical-expense
hardship is measured for the same respondents as validated turnout and six
past-year political activities. Responsibility attribution is also measured.

The most consistent action signal in the exploratory extension is targeted
contact with a public official: the adjusted odds ratio is 1.69 in 2018 and
1.80 in 2020 after controlling for other crises, prior validated turnout, and
the supplied demographic covariates. This is a candidate mechanism, not a
causal estimate. The public extracts do not contain a dated bill, a remedy,
or CES design variables sufficient for a reproduced design-based
medical-specific standard error.

## Follow the observed path

```text
trouble affording medical expenses
  -> responsibility attributed to bad luck, choices, the economy, or government
  -> contact, protest, turnout, campaign work, signs, meetings, or donations
  -> [open] remedy, restored room, trust change, or political exit
```

The result is useful because it keeps political action separate from trust and
from disengagement. A household can face a medical-cost problem and contact an
official, while another household under similar pressure may blame bad luck
and take no visible political action. The data do not tell us whether contact
was effective or whether the respondent contacted government about health
care.

## Same-respondent descriptive evidence

The extracts contain 1,000 valid module rows in each year. The exposure is
reported trouble affording medical expenses; the percentages below are
weighted means using the supplied `teamweight`. The counts in parentheses are
unweighted rows reporting the hardship.

| Outcome | 2018 no hardship | 2018 hardship (n=257) | 2020 no hardship | 2020 hardship (n=152) |
|---|---:|---:|---:|---:|
| Validated turnout | 57.2% | 41.7% | 62.3% | 61.2% |
| Contact public official | 21.4% | 23.3% | 17.9% | 28.3% |
| Attend protest | 8.2% | 7.2% | 5.4% | 9.1% |
| Work for campaign | 5.2% | 3.8% | 3.7% | 1.0% |
| Donate | 17.4% | 10.7% | 22.7% | 22.2% |

The raw contrast changes across years: 2018 hardship coincides with lower
turnout and donation, while 2020 hardship coincides with nearly equal turnout,
higher contact and protest, and lower campaign work. That cross-year change
is evidence against a single “hardship causes withdrawal” rule.

## Attribution changes the route

In 2020, among hardship respondents, weighted responsibility shares were
25.4% for the economy and 22.4% for the federal government. Official contact
was 42.7% among those selecting federal-government responsibility and 13.4%
among those selecting bad luck; protest was 23.6% and 4.0%, respectively.
The federal-government and bad-luck cells contain only 32 and 23 unweighted
respondents.

The 2018 questionnaire used separate multiple-response flags, so the
categories can overlap. Federal-government attribution was selected by 27.6%
of hardship respondents and bad-luck attribution by 24.9%; contact was 26.3%
and 21.5%, and protest was 11.1% and 5.4%, respectively. Because the question
formats differ, these are mechanism cross-checks rather than pooled trend
estimates.

Timing within 2020 also matters. Among hardship respondents, official contact
was 27.6% for expenses reported before 2020, 11.9% for January–February 2020,
and 31.1% for March 2020 or later; protest was 10.1%, 0.0%, and 9.7%. The
post-March group contains 93 unweighted respondents and 54.9% of the hardship
group's weight. These are broad retrospective timing categories, not comparable
event cohorts, so they are a context sensitivity rather than a pandemic causal
estimate.

## The adjusted screen

Separate weighted logistic models use medical-expense hardship as the focal
indicator and control for other crisis count, prior validated turnout, sex,
race indicators, age, education, income, marital status, church attendance,
and children under 18. HC1 model-robust intervals are screening diagnostics;
they are not CES Taylor-series intervals.

| Outcome | 2018 odds ratio | 2020 odds ratio |
|---|---:|---:|
| Validated turnout | 0.93 (0.52–1.65) | 1.22 (0.66–2.26) |
| Contact public official | 1.69 (1.11–2.59) | 1.80 (1.02–3.16) |
| Attend protest | 1.15 (0.60–2.22) | 1.28 (0.53–3.12) |
| Work for campaign | 0.73 (0.34–1.53) | 0.22 (0.03–1.61) |
| Donate | 1.15 (0.68–1.95) | 1.05 (0.58–1.92) |

The contact estimate is the only outcome whose model interval excludes one in
both years. That persistence makes it worth testing with a larger, properly
weighted design. It does not establish that medical hardship caused contact:
health, income, insurance, other crises, ideology, prior participation,
question order, and pandemic context can all shape the result.

A pooled 2018–2020 screen estimates contact OR 1.83 (1.22–2.75) across 1,771
complete cases. The hardship-by-2020 interaction is 0.96 (0.49–1.87), so the
screen does not detect a difference between the two year-specific contact
associations. This is model-robust exploratory evidence, not a harmonized
survey-design estimate.

## The deeper finding

The contact result is best read as a possible conversion from private burden
to institution-targeted action, not as proof of generalized political anger.
A person can retain turnout while contacting an official, protest without
changing party identity, or blame a government actor while receiving no
remedy. The action channel may reveal a loss of control or a demand for
attribution before it reveals a change in trust.

## What this does and does not connect

This finding directly joins a reported medical-affordability hardship to
political-action outcomes in the same respondent architecture. It adds an
attribution route that can distinguish government-targeted pressure from
private coping or bad-luck interpretation.

It does not join the medical episode to a quoted price, amount owed, care
delay, payment alternative, debt, treatment outcome, institutional remedy,
trust change, provider switching, or exit. It also does not join the CES
respondents to MEPS, SHED, CFPB, or ANES respondents. The health-cost-to-
legitimacy chain therefore remains layered rather than complete.

## Next decisive test

Use a larger health-cost panel or survey-design extract that records a dated
bill or care need, coverage and alternatives, care received or forgone,
payment and household trade-offs, responsible actor, prior trust or party
identity, contact/complaint/appeal, remedy, and follow-up health and financial
room. Estimate government-attribution × hardship interactions with design-
based uncertainty and retain the negative cases: people who pay without later
harm, people who experience hardship but keep trust, people who contact
officials without receiving a remedy, and people who withdraw without a
measured medical-cost exposure.

## Reproduction

Acquire and analyze the public inputs with:

```text
python3 scripts/acquire_ces_personal_crisis_replication.py \
  --output-dir /tmp/cgtm-cces-personal-crisis
python3 scripts/analyze_ces_medical_affordability_political_action.py \
  --input-2018 /tmp/cgtm-cces-personal-crisis/CCES18_crisis_vv.tab \
  --input-2020 /tmp/cgtm-cces-personal-crisis/CCES20_crisis_vv.tab \
  --output /tmp/ces-medical-affordability-action.json
```

The [full acquisition and limitation audit](../projects/us-health-cost-household-choice/politics-personal-crisis-medical-affordability-participation-audit-v1.md)
preserves variable definitions, file hashes, attribution coding, and the
reason this finding is not promoted to a causal medical-specific estimate.

## Reading rule

A medical-cost hardship can be associated with political contact without
proving distrust, remedy, or electoral change. Keep exposure, attribution,
action, and institutional effect as separate links.
