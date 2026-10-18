# Service relationships and the data needed to see outcomes

**Status:** ninth active depth artifact in the ongoing program  
**Checked:** 2026-10-18  
**Scope:** rural housing service coordination, youth hubs, school outreach, care navigation, and the difference between visible activity and a realized household outcome

## The question

Who helps a person cross the distance between an eligible service and a usable
result—and can the public system see whether that happened?

The recent passes found the same open link in different settings:

```text
place or institution
  -> trusted relationship
  -> contact, paperwork, transport, or referral
  -> service receipt or problem avoided
  -> household/person outcome
  -> stability, correction, repeat use, or exit
```

The bridge is often small and relational. The data system is often large and
administrative. The mismatch can make an important service look invisible and
can make a reported activity look like an outcome.

## Three source families

| Case | Design and unit | What is observed | What is missing |
|---|---|---|---|
| Rural federally assisted housing | GAO review of rural service coordination, HUD data, selected studies, interviews, and four site visits in Louisiana, New Hampshire, Washington, and Wisconsin | About 56,000 federally subsidized affordable-housing properties and more than 4 million units nationally; 19% of properties and 9% of units were rural in the reviewed inventory; FY2025 service-coordinator appropriations totaled $152m; site stakeholders reported help avoiding eviction and applying for Medicaid | Complete coordinator/property denominator, routine performance analysis, resident-level longitudinal follow-up, completed benefit receipt, avoided eviction, health, and durable housing stability |
| Young Futures Hubs | Interim process evaluation of 8 English Early Adopter sites in 2025–26 | Mobilisation, trusted relationships, open access, warm handovers, referrals, employability/volunteering routes, and early belonging/wellbeing reports | Linked individual journeys, consistent outcome measures, consent/data-sharing infrastructure, youth decision rights, and long-run outcomes |
| Chicago school outreach | Three randomized field experiments in Chicago Public Schools | Personalized calls increased virtual summer-program registration; texts and instructional-aide support had mixed or null primary engagement effects but some secondary/later math gains | Household burden, durable attainment, transfer to other districts, and a universal mechanism connecting contact to learning |

Primary records: [GAO rural housing coordination](../../records/us-gao-rural-housing-service-coordination-data-outcomes-2026.json),
[Young Futures implementation](../../records/comparative-uk-young-futures-hubs-interim-evaluation-2026-implementation-data.json),
and [NBER Chicago outreach](../../records/us-nber-chicago-remote-learning-engagement-rcts-2026.json).

## What the evidence shows together

### 1. Relationships can be infrastructure

GAO’s rural cases show coordinators connecting residents to health care, meals,
transport, and benefits. Young Futures reports trusted staff, co-location, and
warm handovers. Chicago shows that personalized human contact can change the
first practical step: registration.

This supports a bounded interpretation: a service may depend on a person,
relationship, or local knowledge that is not captured by the unit, building,
programme, or platform record.

It does not prove that every coordinator, hub worker, or phone call improves a
later outcome.

### 2. Administrative visibility breaks before the outcome

HUD cannot accurately determine how many multifamily properties have service
coordinators or routinely analyze required performance reports. Young Futures
could measure aggregate reach, attendance, referrals, and support more easily
than a linked journey across universal, targeted, and specialist services.
Chicago had stronger causal design, but even there the outcome depends on which
measure and time period is used.

The recurring pattern is not simply “bad data.” It is that the easiest unit to
count is often the least useful unit for the person’s actual path.

### 3. The same contact can produce different results

Personalized outreach may increase registration without improving use. A warm
handover may make specialist care reachable for one person but fail when the
specialist service has no capacity. A housing coordinator may prevent a crisis
that never appears as a positive event in administrative data.

Therefore, “no recorded outcome” has at least three possible meanings:

- the service did not work;
- the outcome occurred but was not linked or recorded; or
- the person did not reach the next stage because of a different barrier.

The sources do not allow these meanings to be collapsed.

## Hidden infrastructure and unequal access

Relational support may be most valuable where formal options are far away,
paperwork is difficult, transport is limited, a person has a disability or
health condition, or trust in institutions is weak. That also creates a risk:
places with the greatest need may have the thinnest staffing, data capacity,
and funding continuity.

The public records show this tension without proving its size. GAO reports
rural service-coordinator funding and incomplete HUD visibility. Young Futures
reports start-up friction, partnership time, and sustainability concerns.
Chicago shows that a low-cost contact intervention can alter take-up, but not
that contact alone replaces service supply or household capacity.

## Counterexamples and alternative explanations

- A coordinator may be visible because a property has strong management, while
  an unmeasured informal network may do similar work elsewhere.
- Poor administrative linkage may reflect privacy protection or appropriate
  limits, not only weak institutional capacity.
- Mixed study findings may reflect different resident populations, services,
  outcomes, or implementation quality rather than an ineffective model.
- A warm handover may increase service use but also expose unmet demand if the
  receiving service cannot accept the referral.
- A person may avoid eviction or gain benefits because of a coordinator while
  later losing housing for an unrelated rent, health, or employment shock.
- A public system may have excellent data linkage and still fail to deliver a
  reachable or trusted service.

These counterexamples mean the next test needs both data quality and service
quality. One cannot stand in for the other.

## Bounded social discussion

The social records help identify how people understand the missing layer:

- [Youth-centre discussion](../../social-discussions/records/atlas-british-academy-youth-infrastructure-reddit-001.json)
  describes a usable youth centre as safety, connection, and activation, not
  merely a building.
- [Housing relocation discussion](../../social-discussions/records/housing-place-linkedin-001.json)
  treats moving as a bundle of utility, insurance, transport, neighborhood-fit,
  and adaptation costs, showing why a formal housing option may not be usable.
- [Renter adaptation discussion](../../social-discussions/records/housing-place-reddit-001.json)
  describes trading rent, utilities, location, and convenience, but gives no
  verified household denominator or savings outcome.
- [Public-health worker discussion](../../social-discussions/records/atlas-batch-0049-public-health-worker-linkedin-001.json)
  links institutional strain and political hostility to retention risk. It is a
  selected professional interpretation, not a worker panel.

These discussions reinforce the hypothesis that practical service capacity is
relational and place-specific. They cannot verify reach, receipt, or durability.

## The stronger test

The next acquisition should create a privacy-protected, site-level pathway
ledger for one rural housing property or one Young Futures hub:

```text
site and eligible population
  -> coordinator/staff capacity and schedule
  -> contact and reason for contact
  -> barrier: transport, paperwork, cost, trust, language, disability, time
  -> referral or co-designed service decision
  -> completed receipt, non-receipt, or unresolved case
  -> immediate resident/person result
  -> later housing, health, work, education, or wellbeing status
  -> repeat use, correction, stability, or exit
```

Minimum fields are date, site, cohort, contact type, denominator, referral
destination, completion status, outcome window, consent/linkage method, and
missingness reason. Never infer a completed benefit from a referral, or an
avoided crisis from the absence of a later record.

## Current answer

**Answer state: partly answered.** The cross-source evidence supports the idea
that trusted local relationships are a form of public infrastructure and that
administrative systems often see outputs more clearly than outcomes. It does
not yet establish the size, cost-effectiveness, or durability of that bridge.

The most valuable next evidence is not another national summary. It is one
well-defined site with a transparent cohort path and a documented outcome or
documented linkage failure.

Related bridges: [voice to service implementation](../us-cost-trust-politics/voice-to-service-implementation-comparator-v1.md),
[Young Futures to realized outcome](../us-chicago-remote-learning-engagement/young-futures-to-realized-outcome-bridge-v1.md),
and [rural housing service coordination](findings/us-gao-rural-housing-service-coordination-data-outcomes-2026-001.md).

Related operating plan: [ongoing cross-source theme-mining
program](../../ONGOING-GOAL-OPERATING-PLAN_V1.md).
