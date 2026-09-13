# PSID material, time, and care extract specification v1

**Checked:** 2026-09-13
**Scope:** many-family US longitudinal comparison, not a single-household case
**Status:** pre-acquisition specification; core time/care and wellbeing names
are mapped across 2019/2021/2023, while cross-wave universes and remaining
fields still require checks

## Research question

Across repeated PSID families, when material room, employment, or health
conditions differ, how do paid work, unpaid care, household labor, social time,
and perceived time pressure differ—and which outcomes recover, persist, or move
in opposite directions later?

This is a bounded societal comparison. It tests distributions and within-unit
change across many respondents; it does not assume that every change is caused
by a price, employer, policy, or care event.

## Target file architecture

Start with the 2019, 2021, and 2023 main-study family and individual files.
Retain the PSID person identifiers, annual family interview identifiers, family
unit status, interview year, survey mode, and weights before selecting analysis
fields. Merge family-level and individual-level records only using the
year-specific identifiers defined by the PSID file-structure documentation.

The initial analytic unit is the **Reference Person and Spouse/Partner within a
responding family-year**, with a family-year companion record. This preserves
person-level time reports and family-level expenditures, income, housing, and
composition. A person may appear in multiple waves but may not be present in
every family-year; nonresponse, mover-out, and family-composition changes must
remain explicit.

## Candidate field groups

The field-level record is also available as the machine-readable [PSID field
manifest](../../../manifests/us-psid-material-time-care-field-map-v1.json).
The following questionnaire labels are now mapped across the 2019, 2021, and
2023 Family File codebooks where listed. Cross-wave comparability, universes,
response codes, and the remaining work/material/health fields still require
verification before pooling.

| Domain | Candidate questionnaire fields | Derived analytic measure | Unit |
|---|---|---|---|
| Employment timing | Section BC employer records; start/end year, month, and day fields | job start/stop between waves; timing precision flag | person-job-wave |
| Paid work | 2019 `ER72408`; 2021 `ER78447`; 2023 `ER82434` BC60A typical-week paid hours | paid hours and change since prior wave | person-wave |
| Work location/commute | 2019 `ER72197` average commute time; 2021 `ER78200`–`ER78202`; 2023 `ER82183`–`ER82185` BC21B commute/work-from-home fields | home-work indicator where available, commute burden, missing/unknown timing | person-job-wave |
| Work pressure/control proxy | BC60B–BC60E interaction, physical demand, mental demand, and rushed-at-work items | reported work-intensity and time-pressure scale; not labeled control without validation | person-wave |
| Household labor | 2019 `ER72718`; 2021 `ER78795`; 2023 `ER82788` F1A typical-week housework | unpaid household labor hours and change | person-wave |
| Personal health time | 2019 `ER72720`; 2021 `ER78797`; 2023 `ER82790` F1B personal care | self-care time | person-wave |
| Consumer/service effort | 2019 `ER72721`; 2021 `ER78798`; 2023 `ER82791` F1C shopping | shopping/service effort time | person-wave |
| Child care | 2019 `ER72722`; 2021 `ER78799`; 2023 `ER82792` F1D child care; 2023 paid-care fields `ER82818`, `ER82820`–`ER82831` | unpaid child-care time, paid child-care cost, coverage months | person/family-wave |
| Adult care | 2019 `ER72723`; 2021 `ER78800`; 2023 `ER82793` F1D2 adult care | unpaid adult-care time | person-wave |
| Social/civic availability | 2019 `ER72724`, `ER72726`, `ER72727`; 2021 `ER78801`, `ER78803`, `ER78804`; 2023 `ER82794`, `ER82796`, `ER82797` | volunteering, leisure, interaction frequency, shared-meal frequency | person/family-wave |
| Perceived time scarcity | 2019 `ER72730`; 2021 `ER78807`; 2023 `ER82800` F1K feeling rushed outside work | outside-work time-pressure indicators | person-wave |
| Work pressure | 2019 `ER72412`; 2021 `ER78451`; 2023 `ER82438` BC60E rushed while working | work-time-pressure indicator by employment status | person-wave |
| Subjective wellbeing | 2019 `ER72025`; 2021 `ER78026`; 2023 `ER82027` A3 life satisfaction | repeated subjective wellbeing endpoint | person-wave |
| Material room | Section F expenditures; Section G income; Section W wealth/assets | income, selected essential spending, wealth/buffer bands, missingness | family/person-wave |
| Health outcome | H1 general health; H1A change since prior wave and other health fields | health level and direction of change | person-wave |
| Family composition | coverscreen family-unit status, births, moves, spouse/partner, children | care exposure, household change, mover-out/mover-in flags | person/family-wave |

## Core comparison cells

The first release should not attempt a universal causal model. Produce these
descriptive cells after valid sample construction:

1. material-room change × change in paid hours;
2. material-room change × child/adult-care hours;
3. material-room change × housework, shopping, leisure, and rushed-time
   measures;
4. care-time change × work hours, commute/work location, health change, and
   family-meal frequency;
5. work transition × care-time and social-availability change; and
6. similar material or care exposure × different alternatives or family
   support, as the first counterexample comparison.

Stratify, where cell sizes permit, by age, gender, race/ethnicity, education,
children, disability/health, tenure, region, and family composition. Report
unweighted counts, weighted estimates, missingness, attrition, and uncertainty.
Do not collapse all time measures into one “time poverty” score before checking
whether paid work, care, leisure, social interaction, and feeling rushed move
together.

## Arrow ledger for the first extract

| Arrow | Evidence needed | Initial status |
|---|---|---|
| material room → work/care/time allocation | repeated person/family fields and time order | testable after extract |
| work/care/time allocation → health/family/social outcomes | repeated outcomes and composition controls | testable after extract |
| observed change → specific price, rule, or institutional actor | dated external event or respondent attribution | open |
| material/time experience → trust, identity, or political action | direct same-event meaning/action measure | open in main extract |
| adaptation → recovery or persistence | later wave with retained person/family and repeated fields | testable after extract |

## Quality gates

Before publishing any estimate:

- verify every candidate field against the released codebook and universe;
- test whether F1/BC/H fields exist with comparable definitions in all three
  target waves;
- preserve CATI versus WEB mode and questionnaire routing;
- distinguish zero, not applicable, don't know, refusal, and unavailable;
- calculate valid person-wave and family-wave counts before and after each
  merge;
- retain survey weights and the appropriate variance method;
- check whether the same person is still in the family unit at follow-up;
- test nonresponse and attrition by baseline room, care, health, and status;
- report typical-week recall and respondent-level limitations; and
- include a counterexample cell where similar exposure did not produce the
  predicted time or health change.

## What this extract can and cannot say

If the fields survive the codebook and retention checks, the extract can test
whether material room, work, care, and perceived time pressure are repeatedly
distributed together or move differently across many US families. It can also
show whether a reported adaptation persists or reverses.

It cannot, without an additional dated event or attribution design, say that a
particular price, employer, agency, insurer, platform, or policy caused the
change. It cannot turn typical-week reports into a detailed 24-hour diary, and
it cannot infer trust, cultural meaning, collective action, or voting from
volunteering, leisure, or family meals.

Related: the [material/time/care acquisition plan](material-time-care-linkage-acquisition-plan-v1.md),
the [broad event ledger](../../templates/US-BROAD-EVENT-LEDGER_V1.md), and the
[broad next-pass queue](../../US-BROAD-NEXT-PASS-QUEUE_V1.md).
