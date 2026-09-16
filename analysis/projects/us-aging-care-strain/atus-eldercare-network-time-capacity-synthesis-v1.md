# Eldercare is a distributed time network, not only a household burden

**Checked:** 2026-09-15  
**Status:** bounded cross-source synthesis; no causal work-displacement claim

## The theme

American eldercare is carried through both households and wider kin or
community networks. The current ATUS evidence shows a population of providers
that is large enough to matter for work, time, transport, household
production, and social capacity. It also shows why “care burden” should not be
reduced to hours or assigned only to the recipient's household.

The evidence supports this bounded chain:

```text
aging-related care need
  -> provider enters a household or non-household care network
  -> time is allocated across direct care, household work, travel, and communication
  -> work, rest, social availability, and family coordination occupy different positions
  -> employer, public-service, and household consequences remain to be joined
```

## What the published population layer shows

The BLS 2023–2024 combined ATUS tables identify 38.192 million eldercare
providers, or 14.0% of the civilian noninstitutional population age 15 and
over. The provider rate is highest among people age 55–64 (24.1%), and 23.569
million providers are employed. This makes eldercare simultaneously a later-
life, labor-market, and family-network issue.

On an average day, 27.6% of providers provide care. Averaged over all
providers, eldercare occupies 1.07 hours per day; among providers who give
care on that day, it occupies 3.88 hours. For employed providers the
corresponding figures are 0.61 hours across all providers and 2.84 hours on
care days. These denominators answer different questions: spread of the
burden across ordinary days versus intensity when care is actually performed.

## The network boundary

The 2024–2025 ATUS eldercare-roster extraction adds recipient relationship
structure to the time layer:

| Annual sample | Provider respondents | Listed recipient records | Mean listed recipients/provider | Provider with household recipient | Provider with non-household recipient |
|---|---:|---:|---:|---:|---:|
| 2024 | 1,319 | 1,738 | 1.3263 | 22.7081% | 79.0242% |
| 2025 | 1,016 | 1,429 | 1.4338 | 21.2877% | 79.9918% |

These are provider-level weighted indicators among respondents with at least
one roster record. Recipient records are not independently weighted, and
2024 and 2025 are separate annual samples. The high non-household share is
therefore not evidence that care is easy, remote, or low burden. It establishes
that a household-only frame would omit a large part of the reported care
network.

The household/non-household distinction also changes the plausible mechanism.
Daily-care providers report more household-member care activity, while
several-times-per-week providers show more non-household adult assistance in
the published frequency tables. This is a descriptive contrast in activity
and recipient relationship, not a causal comparison of households.

## What the time allocation does and does not mean

On care days, reported time includes household activities, caring for or
helping household members, caring for or helping non-household members,
travel, communication, and other activities. It is therefore misleading to
call every care-related minute “lost work.” The diary does not observe the
counterfactual schedule, employer permission, wage loss, sleep sacrifice,
replacement care, or whether another caregiver absorbed the task.

The correct interpretation is a set of separate currencies:

| Currency | Visible in current ATUS evidence | Still open |
|---|---|---|
| Direct care time | Care-day and all-provider averages | Intensity across an episode and recipient outcome |
| Household production | Activity categories and household-member help | What task was displaced or shared |
| Travel/coordination | Travel, communication, and related activities | Distance, appointment friction, and administrative effort |
| Paid work | Employment and work activity on diary days | Earnings, schedule control, leave, and job retention |
| Social capacity | Socializing/communication and leisure | Participation loss, isolation, trust, and political action |

## Counterexamples the atlas must preserve

The same reported care exposure can have different consequences when providers
have paid support, flexible schedules, nearby relatives, public services, or
different recipient relationships. Conversely, a non-household recipient can
still require substantial travel and coordination, while a household recipient
may be supported by several caregivers. The annual roster data cannot tell us
which of these configurations occurred.

The 2024–2025 movement in listed-recipient multiplicity is not promoted as a
trend: it may reflect sample composition, reporting, or roster structure. The
published 2.7% work-activity share on care days is not promoted as a care-
caused employment reduction. These are deliberate counterinterpretations,
not footnotes added after the result.

## Smallest next test

The strongest next design is a same-provider, same-household or same-person
panel that combines:

1. recipient relationship and care frequency;
2. care hours, travel, coordination, and replacement support;
3. work hours, schedule control, leave, earnings, and job retention;
4. health, sleep, financial room, and household composition;
5. public or employer care services and their accessibility; and
6. later recovery, social participation, trust, or political action.

ATUS supplies unusually useful time and network structure, but not the
longitudinal endpoint. PSID, SIPP, or a suitably linked UAS/HRS route should
be used to test persistence and adaptation rather than to manufacture a
same-person join across unrelated samples.

## Sources and machine records

This synthesis draws on the official [BLS 2023–2024 unpaid eldercare
tables](https://www.bls.gov/news.release/elcare.toc.htm), the [ATUS 2024–2025
annual time/care comparison](../us-household-calendar-integration/atus-time-care-annual-comparison-2024-2025-v1.md),
and the [2024–2025 eldercare-roster trend record](../../records/us-atus-eldercare-roster-2024-2025.json).
The [published care/work layer](atus-2023-2024-published-care-work-layer-v1.md)
contains the provider, time, and frequency tables. The microdata extraction
preserves archive hashes and respondent-level denominators; no raw archive is
committed.

