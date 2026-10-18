# From service reach to realized outcome: Young Futures and Chicago outreach

**Status:** eighth active depth artifact in the ongoing program  
**Checked:** 2026-10-18  
**Scope:** public-service access, take-up, engagement, implementation, later outcomes, and the limits of cross-program comparison

## The question

When a public service reaches someone, what must be observed before we can say
that it improved their situation?

The Young Futures Hubs evaluation shows early implementation, trusted access,
warm referrals, and reported belonging. The NBER Chicago experiments show why
those stages cannot be collapsed into one “engagement” measure: personalized
contact changed registration, while other interventions had null primary
engagement effects and some later academic gains.

The shared chain is:

```text
offer and invitation
  -> take-up or registration
  -> attendance and repeat contact
  -> referral or service use
  -> immediate experience or capability
  -> later outcome
  -> durability, correction, re-entry, or exit
```

## What each source contributes

| Source | Design and unit | Observed stage | Boundary |
|---|---|---|---|
| Young Futures Hubs | Interim process evaluation of 8 English Early Adopter sites in 2025–26; stakeholder, young-person, site, and monitoring evidence | Mobilisation, partnerships, open access, trusted relationships, warm handovers, referrals, employability/volunteering routes, some service-design participation, and early belonging/wellbeing reports | No common person-level journey, consistent outcome set, causal estimate, verified decision rights, or long-run education, employment, safety, or wellbeing result |
| Chicago NBER trials | Three randomized field experiments in Chicago Public Schools during remote and summer learning | Personalized phone calls increased virtual summer-program registration; weekly texts had no effect on primary absence/platform-use outcomes but improved a secondary math outcome; instructional-aide support had null primary engagement effects with some later math gains | Chicago-specific settings; intervention effects differ by outcome and timing; no durable attainment, household burden, or broad generalization |

The primary records are the [Young Futures evaluation
record](../../records/comparative-uk-young-futures-hubs-interim-evaluation-2026-implementation-data.json)
and the [NBER Chicago experiment
record](../../records/us-nber-chicago-remote-learning-engagement-rcts-2026.json).
The detailed NBER finding is [school outreach can improve take-up without one
universal engagement effect](findings/us-nber-chicago-remote-learning-engagement-rcts-2026-001.md).

## What the comparison shows

### 1. Reach is not use

Young Futures reports open access and early engagement. Chicago provides a
cleaner test of the first conversion: personalized calls increased registration.
Neither registration nor open-door access proves regular attendance, sustained
use, or a beneficial experience.

### 2. Use is not the same as the intended outcome

In Chicago, weekly texts did not change the primary measures of summer absence
or Khan Academy use, although a secondary math-course result improved. An
instructional aide did not change primary summer attendance or platform use,
while some following-year math outcomes improved. A null proximal measure and a
later positive result can coexist.

Young Futures faces the same measurement problem in a different setting:
attendance, referrals, soft outcomes, and individual journeys should not be
treated as interchangeable evidence of mental-health, employment, safety, or
belonging effects.

### 3. Trusted contact may be a route, not an endpoint

Both sources make human connection matter. Chicago’s personalized call changes
take-up; Young Futures reports trusted staff, co-location, and warm handovers.
But contact may work by information, confidence, practical help, or referral.
The mechanism must be measured separately from the later outcome.

### 4. A stronger design does not remove the last-mile problem

The NBER experiments strengthen causal interpretation for their assigned
interventions and outcomes. They do not provide a universal theory of public
service engagement. Young Futures adds implementation realism but has weaker
common outcome measurement. Together they show why the program needs both:
causal tests where available and implementation ledgers where delivery is
complex.

## What can be compared, and what cannot

The comparison fits on four dimensions: public or publicly supported service,
young people or families as intended users, a first access step, and a later
outcome or outcome-measurement problem. It does not fit on intervention type,
country, age mix, setting, timing, or outcome definition.

Do not calculate a common effect size. Do not call a Young Futures report of
early belonging equivalent to the NBER randomized math result. Do not use the
NBER null platform-use result to conclude that hub attendance has no value.

## Counterexamples and alternative explanations

- A registration increase can reflect better information without more service
  use or learning.
- A null attendance or platform-use result can hide effects on quality,
  confidence, a different course, or a later outcome.
- Young Futures’ reported access may reflect selection into reachable sites or
  unusually strong local partners rather than a general hub effect.
- Early implementation friction may be temporary and improve with shared
  indicators, consent, and data-sharing agreements.
- A human referral can improve trust while failing to resolve the underlying
  service shortage, transport barrier, family time constraint, or employment
  condition.

These alternatives change what the next ledger must record; they do not make
the early signals meaningless.

## Bounded social discussion

The social layer supplies meaning and hypotheses:

- [Youth-centre discussion](../../social-discussions/records/atlas-british-academy-youth-infrastructure-reddit-001.json)
  treats a usable youth centre as safety, connection, and activation—not merely
  a physical asset.
- [Young-men loneliness discussion](../../social-discussions/records/atlas-dcms-young-men-loneliness-linkedin-001.json)
  links trusted relationships and community alternatives to support-seeking,
  but is advocacy rather than outcome evidence.
- [Local organizing discussion](../../social-discussions/records/political-action-reddit-001.json)
  shows how a local issue can combine meetings, site visits, policy work, and
  elections; planned actions still need verification.

These discussions help identify what users and organizers mean by “support” or
“connection.” They do not supply the denominators or follow-up needed for an
effect claim.

## End-to-end ledger specification

For the next Young Futures acquisition, record one site and one defined cohort
using the following fields:

```text
site, cohort, date, access route, barrier, invitation
  -> first contact, attendance, repeat contact
  -> referral, service received, co-design input, decision right
  -> immediate experience, capability, or wellbeing measure
  -> later education/work/health/safety outcome
  -> correction, re-entry, sustained use, or exit
```

Every field needs a unit, denominator, method, source locator, and missingness
note. If the person-level join is not permitted or not collected, preserve the
aggregate result and publish the linkage failure as a finding.

## Current answer

**Answer state: partly answered.** We now have a causal example showing that
personalized contact can move take-up without moving every later engagement
measure, and an implementation example showing that trusted access and warm
referral can exist before linked outcomes are available. The next decisive
evidence is a Young Futures site-level cohort or administrative follow-up that
reaches beyond attendance and referral.

Related bridges: [local issue, voice, response, and efficacy](../us-cost-trust-politics/local-issue-voice-response-efficacy-bridge-v1.md)
and [voice to service implementation](../us-cost-trust-politics/voice-to-service-implementation-comparator-v1.md).

Related operating plan: [ongoing cross-source theme-mining
program](../../ONGOING-GOAL-OPERATING-PLAN_V1.md).
