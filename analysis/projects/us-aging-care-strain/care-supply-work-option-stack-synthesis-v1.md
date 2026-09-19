# Care supply, household adaptation, and work option-stack synthesis v1

**Checked:** 2026-09-18  
**Scope:** US child-care and unpaid-care evidence across household,
same-person, provider-workforce, and institutional units

## The defensible chain

The retained evidence now supports a staged care-to-work map:

```text
care need or disruption
  -> paid care, unpaid support, work-plus-supervision, delay, or non-use
  -> money, time, hours, leave, job-search, savings, or housing strain
  -> provider workforce and institutional response
  -> [open] dependable staffed slot and preserved work/family outcome
  -> [open] recovery, trust, collective action, or policy feedback
```

The evidence is intentionally not pooled into a single “care burden” rate.
The strongest recurring pattern is that care constraints are converted into
different currencies depending on outside options: households with more money
can buy paid care or leave, while households with fewer options may transfer
the problem into unpaid time, work withdrawal, or later hardship.

## Evidence by stage

| Stage | Retained result | Status and boundary |
|---|---|---|
| Household care demand and payment | About 30.4 million households reported a child age 13 or younger; 23.9% used paid care, and payer households spent about $10,520 on average, 5.6% of income | Reported household cross-section; paid use is not adequate care or subsidy receipt |
| Care disruption and work adaptation | Households reporting inadequate-care problems lost an average 65.8 days of work time; responses included leave, hour cuts, quitting, non-search, and working while supervising | Reported adaptation menu; categories overlap and do not establish job causation |
| Same-person following hardship | In the small stable-SNAP SIPP cell, child-care work prevention was followed by 43.7% rent/mortgage hardship versus 12.0% without prevention; the prevention cell had 23 pairs | Compared same-person month transition with wide uncertainty; annual care timing is not a dated episode |
| Unpaid adult-care time | ATUS standardized contrasts show eldercare providers spent about 70.7 more primary-activity minutes per diary day in 2024 and 62.4 more in 2025 than comparison respondents | Standardized annual samples, not a panel; care onset, recipient outcome, and job retention remain open |
| Provider workforce capacity | DOD employed about 19,000 nonappropriated-fund child-care workers serving nearly 172,000 children; 4,955 recruitment/retention incentives were reported for three services in 2024 | Institutional case, not civilian generalization; incentives are not hires, slots, or shorter waits |
| Institutional conversion | GAO reports lengthy military-family waitlists despite benefits and incentives | Reported mechanism; waitlist duration, staffed-slot reliability, family use, and work outcome are not linked |

## What is interesting here

Care is not one price. The household layer sees payments; the time layer sees
unpaid work and reduced paid-work opportunity; the SIPP layer shows a
same-person hardship signal after reported work prevention; and the provider
layer shows that subsidies or institutional benefits can coexist with worker
shortages and waitlists.

That creates two counterexamples worth preserving:

1. **Low paid-care spending is not low care burden.** It can reflect unpaid
   substitution, work withdrawal, non-search, or a household unable to buy
   care.
2. **A care benefit is not a dependable slot.** A fee discount or worker
   incentive can lower a nominal price or support recruitment while a family
   still waits for a staffed place.

## Arrow ledger

| Arrow | Evidence | Status | Open requirement |
|---|---|---|---|
| Care constraint → work/time adaptation | Census household adaptations, ATUS time contrasts, SIPP work-prevention fields | Compared / reported | Dated trigger, hours actually lost, employer response |
| Work prevention → following material hardship | Same-person SIPP November–December transition | Compared, small cell | Larger repeated/event design and causal timing |
| Provider workforce pressure → waitlist pressure | GAO institutional review and DOD administrative reporting | Reported | Installation-year vacancies, turnover, waitlist entry/exit |
| Benefit/incentive → dependable care | Not established | Open | Staffed slots, family eligibility/use, wait, alternative provider |
| Care route → recipient/child outcome | Not established | Open | Safety, continuity, development/health, and completed care |
| Care strain → trust/action/exit | Not established | Open | Same-unit meaning, complaint, organizing, policy response, or exit |

## What this changes in the broader atlas

The care lane now has a stronger middle than a simple “care is expensive”
story: the relevant mechanism is option conversion. Money can buy relief only
where providers, schedules, eligibility, and staffed capacity exist. Family
support can protect work or conceal the burden by shifting time to another
adult. Work can remain formally intact while hours, attention, savings, or
housing security narrow.

This also explains why national paid-care averages and provider counts should
not be interpreted as access. The decisive unit is a recurring care need with a
reachable, affordable, dependable alternative and a later outcome.

## Next test and stopping rule

The next stronger artifact is a care-event ledger with provider availability,
price or subsidy, schedule, informal support, work hours, and later care/work
outcome in the same household or installation-year unit. Do not add another
national care-spending cross-tab unless it adds a second period, a valid
matched design, or a verified institutional outcome. If no such record is
available, retain this boundary and rotate to the consumer/work lane.

## Sources

- [Census child-care challenges and work adaptation](census-2025-childcare-challenges-work-adaptation-layer-v1.md)
- [SIPP work/care/room record](../../records/us-sipp-work-care-room-nonpooled-2024.json)
- [Care/time/material/mobility record](../../records/us-care-time-material-mobility-crosssource-2022-2025.json)
- [ATUS care/work layer](atus-2023-2024-published-care-work-layer-v1.md)
- [GAO military child-care workforce capacity](gao-2026-military-childcare-workforce-capacity-layer-v1.md)
