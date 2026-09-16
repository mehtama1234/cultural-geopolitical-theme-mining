# MEPS event to later-panel follow-up screen v1

**Checked:** 2026-09-16  
**Status:** strict-window longitudinal descriptive screen; not verified
recovery and not causal

## What this adds

The existing MEPS event screens stopped at R4/2 context. The cached 2024
person file also contains R5/3 health and employment fields. This pass selects
each person's first valid office, emergency-room, or inpatient event strictly
between the R3/1 and R4/2 endpoint months, then carries the same person to the
later R5/3 panel outcome.

```text
first event in strict R3/1–R4/2 window
  -> R4/2 baseline context
  -> R5/3 later health/work status
```

The `no_event_in_window` comparison includes people without a selected event
in that window; it is not a no-need or causal control. The screen therefore
extends the longitudinal clock while preserving the existing evidence boundary.

## Results

Percentages are person-weighted shares with 128 MEPS BRR replicates. Event and
comparison group counts are valid round-ordered person records; outcome
denominators can be smaller.

| Event family | Event / no-event n | Fair/poor health R4 → R5 | Health worsened R4→R5 | Not employed R4 → R5 | Status changed R4→R5 |
|---|---:|---:|---:|---:|---:|
| Office | 3,277 / 15,414 | 9.11% → 9.94% / 10.75% → 10.97% | 21.34% / 22.21% | 33.42% → 35.24% / 33.63% → 34.59% | 10.07% / 9.35% |
| Emergency room | 1,093 / 17,598 | 27.08% → 26.83% / 9.55% → 9.91% | 24.17% / 21.94% | 47.23% → 49.01% / 32.77% → 33.84% | 11.49% / 9.35% |
| Inpatient | 536 / 18,155 | 33.13% → 33.01% / 9.90% → 10.24% | 23.33% / 22.02% | 59.61% → 62.18% / 32.83% → 33.90% | 11.83% / 9.40% |

The acute-event groups begin with much worse R4/2 health and employment
levels, and those differences remain at R5/3. The event-window versus
comparison contrast in the change indicators is smaller than the level
contrast: for example, inpatient fair/poor health is 33.13% at R4/2 and
33.01% at R5/3, while the comparison moves from 9.90% to 10.24%. This is a
bounded persistence/context result, not evidence that the event caused later
health or employment status.

## Why it matters for the cascade

This closes part of the **adaptation → later outcome clock**: a dated event can
be placed before both an intermediate panel boundary and a later panel outcome
using the same person key. It does not close the remedy or recovery arrow.
Neither R5/3 health nor employment status says whether an insurer, provider,
employer, or household repaired the original problem.

## Boundaries

- R5/3 is a later panel outcome, not a verified one-, three-, or six-month
  recovery measurement from the displayed event.
- The event may be the consequence of an earlier need, and no claim or bill ID
  identifies the household obligation.
- The screen does not measure alternatives, care continuation/foregoing,
  institutional response, remedy, household payer, food/housing trade-offs,
  trust, action, switching, or exit.
- Baseline selection, severity, coverage, treatment continuity, mortality or
  attrition, and event-day ordering remain plausible explanations.
- Health and employment fields are analyzed with valid-code and outcome-specific
  denominators; missingness is not treated as a negative outcome.

## Reproduction

- [Machine-readable output](data-meps-event-six-month-followup-2024.json)
- [Analysis script](../../../scripts/analyze_meps_event_six_month_followup.py)
- [MEPS dated event spine](meps-dated-event-spine-v1.md)
- [Same-case closure protocol](same-case-closure-protocol-v1.md)

Primary HC-256 hash: `b4bde859b39f626345561c05570292bb7264dd92eb76ce0c1a14d6b89076aed5`  
BRR hash: `44f1e5a864c1d318327a0fbd3a0ff48a583c74c3a104aae357032cfbfaa5a32e`  
Script hash: `bed07f22d5478fe3b40222478e35128ea58ad535965cc04ec099d03c331f658e`  
Output hash: `b7a6d4f87b85835a1d9e9b76e9125a03b2d6ec2dfc23aa527f3e41dd2f98e10c`

**Evidence status:** reproduced later-panel follow-up context; not a complete
same-episode remedy, recovery, trust, political-action, switching, or exit
result.
