# MEPS 2024 episode closure audit: stop extending the payment spine until the missing middle is acquired

**Checked:** 2026-10-20  
**Status:** bounded closure audit; no new causal estimate  
**Scope:** US MEPS 2024 full-year person and event files already acquired in this project

## Decision

The MEPS 2024 route now has enough repeated analysis to establish a stable
bounded spine:

```text
person and panel identity
  -> observed office / ER / inpatient / prescription event
  -> event-family payment and coverage context
  -> month-level relation to the R4/2 endpoint
  -> annual health, employment, bill-problem, debt, and care-delay context
```

The route does **not** yet supply the episode fields needed to claim:

```text
dated need or bill -> feasible alternative -> care/payment choice
  -> money/time/work/family trade-off -> remedy or recovery -> trust/action/exit
```

The correct next move is therefore a source acquisition or authorized linkage
that contains the missing middle. More MEPS payment bands, event-family
cross-tabs, or annual associations would refine the existing spine but would
not close the episode.

## Stage audit

| Required stage | MEPS 2024 status | Safe use | Closure requirement |
| --- | --- | --- | --- |
| Defined person/household unit | **Joined** through `DUPERSID + PANEL`; household context is available only where the relevant file supplies it | Keep person/event-family universes separate and preserve weights | A same-unit household key if the outcome is household burden |
| Dated need or bill | **Open**; event month identifies observed service timing, not the underlying need or bill date | Describe before/same/after `ENDRFY42`/`ENDRFM42` without day-level ordering | A dated medical/dental need, bill, denial, or payment obligation |
| Coverage and observed payment | **Joined for observed events**; self/family payment and coverage categories are available | Compare channels and coverage with event-specific denominators | Amount owed, deductible/coinsurance rule, payment timing, and unpaid balance |
| Care decision and alternative | **Open**; event files condition on observed care and do not identify forgone alternatives | Pair with SHED/MEPS care-delay layers as separate evidence | Reported seek/delay/substitute/forego choice and feasible alternative |
| Household adaptation | **Annual/contextual only**; work, bill problem, debt, savings, and care-delay fields are not tied to one event | State selection and timing limits; do not call them post-bill outcomes | Same-unit money, time, work, food, housing, debt, or unpaid-care response |
| Follow-up remedy or recovery | **Open**; later health/work context is not a remedy record | Use inter-round and month-ordered screens as bounded follow-up context | Treatment continuity, correction, receipt, adequacy, durability, or recovery endpoint |
| Meaning/action/exit | **Open**; no same-person legitimacy endpoint in the acquired MEPS files | Use ANES/CES/UAS as separate or acquisition routes | Same-person trust, switching, collective action, or durable non-use |

## What the existing MEPS evidence closes

The [full-year acquisition gate](meps-2024-full-year-acquisition-gate-v1.md),
[bounded episode ledger](meps-2024-bounded-episode-ledger-v1.md),
[event/payment context](meps-2024-event-payment-bill-context-v1.md),
[month-ordered follow-up](meps-2024-month-ordered-event-followup-v1.md), and
[institutional-friction follow-up](meps-2024-event-institutional-friction-v1.md)
jointly establish that the 2024 files can support reproducible person/event
screens with explicit denominators, weighting, coverage, payment, health,
employment, bill-problem, and timing boundaries.

They also establish why payment is not the missing household-burden variable:
zero self/family payment can coexist with illness, time, transport, premiums,
deductibles, or unpaid care, while positive payment does not identify
unaffordability, debt, delay, or a later sacrifice. The event files are
observed-care files, so their non-users and forgone-care counterfactuals are
outside the event universe.

## Smallest next acquisition

Prioritize one authorized source or linkage with the following minimum row
contract:

1. a stable person or household identifier;
2. a dated need, bill, denial, or payment obligation;
3. coverage/benefit and feasible-alternative fields;
4. a reported care, payment, delay, substitution, or foregoing decision;
5. a follow-up observation of money, time, work, health, debt, treatment, or
   household security; and
6. a later remedy, recovery, trust, switching, or action field, with weights,
   missingness, and retrieval evidence.

The current strongest route is the registration-gated UAS design documented in
the [UAS health-cost legitimacy acquisition audit](uas-health-cost-legitimacy-acquisition-audit-v1.md),
provided access is authorized and the released files actually contain the
specified overlap. Until then, preserve MEPS as a bounded bridge and do not
promote it to a completed affordability or recovery episode.

## Re-entry rule

Reopen the MEPS route only when one of these changes:

- a newly acquired MEPS file adds a dated bill/need, alternative, or remedy
  field;
- an authorized same-unit linkage supplies the missing episode fields; or
- a new source can be joined without pretending that separate respondents,
  annual clocks, or event universes are one episode.

This audit is a stopping rule for repeated MEPS refinement, not a stopping rule
for the broader long-running program.
