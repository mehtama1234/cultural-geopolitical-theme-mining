# MEPS event-channel obligation and recovery audit

Status: fiftieth active depth artifact; checked 2026-10-18.

## Purpose

The household-pressure priority asks for a same-person episode that connects a
health or coverage trigger to alternatives, care choice, money/time/work trade-
offs, later recovery, and institutional response. The local MEPS route is the
closest existing public episode surface, but its fields sit on different clocks
and do not identify the full household obligation.

This audit compares the three dated event families already staged in the
repository. It is a stage-coverage result, not a new population estimate and
not a causal comparison of people who did or did not experience an event.

## What we found

Among the first valid event records strictly between the R3/1 and R4/2 endpoint
months, the event families have sharply different observed payment levels and
different surrounding household contexts:

| Event family | Event-window people | Weighted self/family payment mean | Zero self/family payment | Cost-related care delay | Medical debt | Collector contact | Not employed at follow-up |
|---|---:|---:|---:|---:|---:|---:|---:|
| Office | 3,216 | $66.87 | 49.6% | 6.4% (n=3,182) | 16.2% (n=3,144) | 13.1% (n=3,164) | 33.4% (n=2,545) |
| Emergency room | 1,101 | $155.52 | 69.8% | 9.6% (n=1,076) | 24.1% (n=1,067) | 19.8% (n=1,078) | 47.6% (n=987) |
| Inpatient | 545 | $733.03 | 69.4% | 6.8% (n=526) | 16.6% (n=526) | 14.4% (n=531) | 60.1% (n=522) |

The table shows why payment cannot stand in for household burden. Inpatient
events have the highest observed payment, but the emergency-room group has the
highest reported medical-debt and collector-contact shares in this screen.
Office events have the lowest payment and lower surrounding burden shares, but
almost half of the event records carry zero reported self/family payment. A
zero payment can mean coverage, another payer, a timing boundary, missing
obligation, or no household charge; it is not proof of no burden.

The same route also carries a six-month clock. For the emergency-room event
window, fair/poor health was 27.1% at R4 and 26.8% at R5, with 11.6% showing a
new fair/poor-health onset; nonemployment was 32.2% at R4 and 32.9% at R5,
with 6.7% onset. These are context and transition measures, not event-specific
recovery. The prescription-event follow-up provides a counterexample to a
universal worsening story: its event-window fair/poor-health share was 9.3% at
R4 and 9.5% at R5, while 55.3% of the small valid resolution subgroup resolved
fair/poor health. The subgroup has only 71 valid records for resolution and the
prescription event has a different timing and selection rule.

## Evidence ledger

| Stage | Observed local evidence | Still missing |
|---|---|---|
| Dated trigger | First office, emergency-room, inpatient, or prescription event with person-panel identity and strict inter-round timing | The initiating condition, urgency, and whether the event was avoidable |
| Payment signal | Event-specific self/family payment field and payment-band comparisons | Amount owed, due date, deductible/coinsurance obligation, other-payer timing, and household cash/credit room |
| Alternatives | Round-level coverage, poverty, care-delay, denial/prior-authorization, debt, and collector context | Feasible provider, treatment, transport, borrowing, family-care, or non-use alternatives at the event |
| Choice and trade-off | Reported round care delay and surrounding work/debt/bill measures | Which care was delayed or protected, what was sacrificed, and when the trade-off occurred |
| Institutional route | Round denial/prior-authorization and later administrative visibility in related records | Case-level appeal effort, decision authority, correction, receipt, and adequacy |
| Later outcome | R5/3 health and employment levels, onset, resolution, and transitions | Event-specific treatment continuity, debt resolution, household security, and durable recovery |
| Meaning/action/exit | Separate ANES, CES, SHED, and social-discussion benchmarks | Same-person attribution to this event, trust, political action, switching, or exit |

## What this connects to

- **Household room:** the same displayed payment can coexist with different
  coverage, payer, debt, and cash constraints.
- **Care and social reproduction:** a care event may shift cost into unpaid
  family time, work absence, borrowing, or delayed treatment, none of which is
  fully observed in the event row.
- **Institutional legitimacy:** a denial, payment, or later health state does
  not reveal whether the person received a usable remedy or who they blamed.
- **Work and inequality:** event families carry different employment contexts,
  but the current comparison cannot separate selection into event type from
  downstream labor effect.
- **Public and geopolitical capacity:** this is the household-side analogue of
  the defense bridge: a recorded state or provider action is not the same as
  realized user capability or legitimacy.

## Deeper question

**Which part of a health episode becomes the household's real obligation: the
displayed service payment, the uncovered need, the time and work displaced, or
the institutional effort required to obtain a remedy?**

This question has high learning value because the current route already has
large event denominators and multiple clocks, but the apparent burden ranking
changes depending on whether one uses payment, debt, collector contact, care
delay, work status, or later health. A single “cost” variable would hide these
counterexamples.

## Challenge checks

- Event-family denominators and valid-outcome denominators are shown separately.
- Weighted payment means were not treated as bills owed or household totals.
- Zero payment was not treated as zero burden.
- The emergency-room, inpatient, office, and prescription timing rules were not
  pooled into one event type.
- R5/3 health and work fields were not promoted to recovery from the event.
- Small resolution subgroups and selection into event families remain explicit.
- Separate ANES, CES, SHED, and public-discussion evidence is not used as a
  same-person endpoint for the MEPS event.

## Next test

Use the existing keyed event rows as the sampling frame for a privacy-approved
same-unit linkage or UAS acquisition. For each retained episode, seek:

```text
person/episode key | need/diagnosis or coverage trigger | bill/obligation and due date |
coverage and other payer | feasible alternatives | care choice or delay |
money/time/work/family substitution | appeal/complaint effort | decision and remedy |
receipt and adequacy | later treatment/health/work/debt | trust/action/switch/exit
```

Before promotion, require positive weights, a dated event, an event-specific
obligation or defensible non-obligation, a documented alternative, at least one
household trade-off, and a follow-up field. Retain the event-channel comparison
as a counterexample screen rather than forcing a single burden ranking.

## Stopping rule

Do not call the MEPS event a household cost shock, successful recovery, failed
remedy, or legitimacy-changing experience from payment, debt, care delay,
collector contact, employment, or later health alone. Close this subtest only
when one compatible episode supplies the obligation, alternative, choice,
institutional response, verified receipt or non-receipt, and later outcome—or
when the authorized source owner confirms which fields are unavailable.

## Source links

- [MEPS dated cascade event screen](data-meps-dated-cascade-event-screen-2024.json)
- [MEPS staged-ledger stage-coverage audit](meps-staged-ledger-stage-coverage-audit-v1.md)
- [MEPS event six-month follow-up](data-meps-event-six-month-followup-2024.json)
- [MEPS prescription-event six-month follow-up](data-meps-prescription-event-six-month-followup-2024.json)
- [MEPS friction cascade](data-meps-dated-friction-cascade-2024.json)
- [Household constraint cascade project](README.md)
- [Health-cost end-to-end status matrix](../us-health-cost-household-choice/end-to-end-status-matrix-v1.md)
