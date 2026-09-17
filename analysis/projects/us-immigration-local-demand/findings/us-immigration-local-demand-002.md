# Finding 002: Immigration concern can make non-use an essential form of political and institutional behavior

**Status:** provisional cross-sectional cultural and institutional finding · **Checked:** 2026-09-17

## The bounded finding

The December 2025 Well-Being and Basic Needs Survey (WBNS) analysis reports
that immigration concerns coexist with substantial avoidance of essential
activities among adults in immigrant families with children under 19. In the
published subgroup of 1,036 respondents, 23% reported avoiding at least one of
six essential activities during the prior year. Reported avoidance included not
talking to police, not driving, not going to work, not attending religious or
community events, not sending children to school or care activities, and not
visiting a doctor, clinic, or hospital.

The finding is not that a particular policy caused each missed activity. Its
importance for the broad atlas is conceptual and empirical: participation can
be expressed as protective non-use when a family perceives status, surveillance,
or information-sharing risk. That non-use may protect against a feared risk in
the short run while reducing access, income, care, schooling, community
connection, or public visibility.

```text
immigration-status or enforcement concern
  -> perceived surveillance, deportation, or information-sharing risk
  -> protective avoidance or delayed use of essential routes
  -> access, income, health, child well-being, and belonging may change
  -> [open] complaint, trust, collective action, political demand, remedy, or exit
```

## Evidence comparison

| Surface | Reported estimate | Unit and clock | Interpretation boundary |
|---|---:|---|---|
| Any essential activity avoided | 23% | Adults in immigrant families with children; one or more of six activities in the prior year | A reported retrospective composite, not a causal incidence rate |
| Did not talk to police | 14% | Same subgroup and period | Avoidance may be protective, costly, or both; reason, emergency context, and alternative route are not observed |
| Did not drive a car | 13% | Same subgroup and period | Does not identify missed work, school, care, or available transit |
| Did not go to work | 12% | Same subgroup and period | Does not identify days missed, wage loss, employer response, or a substitute job |
| Did not attend religious/community events | 11% | Same subgroup and period | A possible belonging and visibility consequence, not a direct trust or political-action measure |
| Did not send children to school/care/after-school activities | 10% | Same subgroup and period | Does not identify child attendance, care substitution, learning loss, or child choice |
| Did not visit a doctor/clinic/hospital | 10% | Same subgroup and period | Does not identify urgency, treatment delay, later health, or medical alternative |
| Went without public benefits because of concern | Almost 1 in 5 | Same subgroup and period | Broad reported non-use; eligibility, benefit type, amount, and forgone security are not established |
| Avoided safety-net programs over information-sharing concern | 12% | Same subgroup and period | Makes data governance part of access behavior; does not verify actual agency sharing |
| Did not apply for or stopped noncash programs over green-card concern | 16% | Same subgroup and period | A reported concern about public-charge consequences, not a legal-risk determination |
| One or more material hardships | 60% | Same subgroup and prior year | Shows a constrained baseline but does not establish whether hardship preceded avoidance |
| Child emotional distress | 15% overall; 27% in mixed-status families versus 8% in all-citizen families | Adult report of child stress, anxiety, or sadness | A family-status comparison, not a causal estimate or clinical diagnosis |

The published comparison is especially useful because it distinguishes several
types of non-use rather than collapsing them into generalized disengagement.
Avoiding a clinic, a public benefit, work, police, and a community event can
have different meanings and different costs. They should remain separate
currencies of exposure, safety, access, income, care, and belonging.

## What this adds to the broad atlas

This finding advances the migration/place/belonging and public-system lanes in
four ways.

First, it makes the “exit” boundary visible before an administrative exit is
recorded. A family may not apply, may stop using a benefit, may skip a clinic,
or may avoid a community institution without producing a formal closure or
complaint. Administrative caseloads can therefore understate the practical
effect of perceived risk.

Second, it links cultural meaning to consumer and institutional behavior. The
relevant choice is not simply whether a person supports or opposes immigration.
It is whether a person feels safe enough to use a route that supplies health,
income, education, transportation, work, or social connection.

Third, it shows how data governance can become part of everyday political
economy. A concern about information sharing may alter safety-net use even when
the survey does not establish whether sharing occurred. The perceived data
boundary itself can change the option set.

Fourth, the material-hardship result prevents a purely symbolic interpretation.
Sixty percent reported one or more material hardships. Avoidance can therefore
interact with an already narrow set of alternatives; it is not safe to call all
non-use voluntary preference or all participation evidence of trust.

## Counterexamples and limits

- A family may avoid a route because it is genuinely protective in the perceived
  short-run, even if the same choice creates longer-run cost.
- Non-use is not one behavior: avoiding police, work, care, benefits, school,
  transport, and community events has different stakes and alternative routes.
- Immigration concern is self-reported; the survey does not adjudicate legal
  status, eligibility, actual enforcement probability, or whether an agency
  shared information.
- The estimates are retrospective and cross-sectional. They do not establish
  whether concern caused the activity change, whether a policy or incident was
  responsible, or whether the activity change preceded the concern.
- The mixed-status family comparison does not isolate family composition from
  income, language, geography, prior hardship, or other exposures.
- Avoidance is not automatically distrust, political withdrawal, or exit from
  society. Some families may avoid one route while organizing, voting,
  reporting, or relying on trusted community alternatives elsewhere.
- The evidence does not observe remedy, successful substitution, later trust,
  collective action, vote, or institutional response for the same family.

## Coding rule

```text
reported concern       != adjudicated legal risk
non-use                != apathy
non-use                != generalized distrust
protective avoidance   != harmless choice
participation          != trust
material hardship      != consequence of avoidance
family composition     != causal treatment
survey association     != policy effect
```

Code this as **published subgroup evidence that perceived immigration risk is
associated with differentiated protective non-use across essential and
public-system routes, alongside child distress and material hardship; causal
ordering, alternatives, remedy, trust, collective action, and political
consequence remain open**.

## Next decisive test

The smallest stronger design would follow the same family or respondent across
a dated policy, enforcement, workplace, school, health, or benefit encounter:

```text
specific encounter or information exposure
  -> perceived risk and responsible actor
  -> attempted use, avoidance, delay, or substitute route
  -> money, time, health, work, schooling, or belonging consequence
  -> agency/employer response, correction, or remedy
  -> later trust, complaint, organizing, turnout, vote, continued use, or non-use
```

Condition on family status composition, language, income, disability,
geography, prior route use, and material hardship. Record both protective and
sacrificed outcomes so that the instrument can distinguish avoiding danger from
losing access. No pooled “chilling rate” should be created across the different
activities without a common denominator and a defined harm or protection
measure.

## Sources and storage boundary

- [Urban Institute: *Immigration Concerns Disrupted Families’ Essential Activities and Caused Children Emotional Distress in 2025*](https://www.urban.org/research/publication/immigration-concerns-disrupted-families-essential-activities-and-caused)
- [Urban Institute Well-Being and Basic Needs Survey project](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey)
- [ICPSR 2024 WBNS study metadata and access boundary](https://www.icpsr.umich.edu/web/HMCA/studies/39691)
- [Compact local source layer](../wbns-2025-immigration-concerns-essential-activity-chilling-layer-v1.md)
- [Machine-readable local record](../data/wbns-2025-immigration-concerns-essential-activity-chilling-layer-v1.json)

This finding uses the already retained published summary and compact metadata;
no respondent microdata or bulk file was downloaded.

**Evidence status:** published cross-sectional subgroup estimates with explicit
activity-level denominators and family-status comparison. The evidence closes
the reported avoidance surface, not the causal, remedial, trust, or political
action arrows.
