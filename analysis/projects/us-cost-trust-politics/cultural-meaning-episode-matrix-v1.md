# Cultural-meaning episode matrix v1

**Checked:** 2026-09-17
**Purpose:** compact audit of existing local evidence against the broad program’s cultural-meaning end-to-end chain
**Scope:** no new acquisition; rows are not joined into one dataset

## Coding contract

Each row is coded at the strongest unit actually supported by the source. A
stage marked “partial” means the source contains a related measure but not a
dated, episode-specific observation. “Open” means the source does not support
that stage. Adjacent sources are not treated as the same people.

| Candidate route | Unit and clock | Condition/exposure | Interpretation or meaning | Action/behavior | Response/outcome | Strongest conclusion |
|---|---|---|---|---|---|---|
| [HTOPS material-to-judgment panel audit](htops-2025-panel-linkage-audit-v1.md) | Same selected respondent; April → June 2025 | Material transitions and expense difficulty | Congress confidence and statistics-trust judgment | Open | Open | Best temporal material → judgment bridge; no action or actor response |
| [ANES financial-worry panel](anes-2024-panel-judgment-action-layer-v1.md) | Same panel subset; pre-election worry → post-election report | Financial worry | Government judgment and institutional trust | Reported vote | Open | Temporal worry → judgment/action ordering, but no direct material episode or attribution |
| [CES medical-affordability modules](../us-health-cost-household-choice/cces-medical-affordability-action-reproduction-audit-2026-09-16.md) | Respondent/module year; 2018 and 2020 | Medical-expense crisis | Federal responsibility attribution | Turnout, official contact, protest | Open | Attribution-conditioned action menu; no remedy or later recovery |
| [CCES material/trust/action subgroup layer](cces-material-trust-action-subgroup-layer-v1.md) | Respondent; 2024 post-election | Gig-work and student-loan proxies | Federal/state trust | Six civic-action indicators | Open | Rich cross-sectional comparison; proxies are not dated episodes |
| [SIPP SNAP transition-reason layer](../us-safety-net-access/sipp-snap-transition-reason-layer-v1.md) | Person-month; adjacent transition | SNAP entry or exit and recorded reasons | Open | Program participation transition | Following hardship/resource context | Strong transition/reason/material context; no meaning or political action |
| [SHED coverage-transition panel](../us-health-cost-household-choice/shed-panel-coverage-care-foregoing-paths-v1.md) | Same recontact respondent; panel wave | Coverage path | Perceived health and financial judgment | Care entry/persistence and deferred purchases | Debt/savings/health context | Same-person middle chain; no dated bill, remedy, or political meaning |
| [Pew smartphone time-control layer](../us-digital-habits-attention/pew-2026-smartphone-time-control-wellbeing-layer-v1.md) | Same survey respondent; May–June 2026 | Smartphone use and perceived excess | Utility, overuse, self-control, and well-being interpretation | Cutback attempt and reported success | Perceived sleep/productivity/mood/connection effects | Closes several adjacent self-reported stages; no logged behavior or platform response |
| [Pew diversity/workplace layer](pew-2026-racial-diversity-cultural-workplace-meaning-layer-v1.md) | Same survey respondent; Nov–Dec 2025 | Perceived national diversity | Cultural impact, workplace obligation, fairness | Open | Open | Strong meaning and legitimacy surface; no workplace episode |
| [Gallup moral-values layer](gallup-2026-moral-values-government-role-cultural-polarization-layer-v1.md) | Same survey respondent; May 2026 | Perceived moral decline and issue conditions | Government influence, legitimacy, religious influence, acceptability | Open | Open | Strong attribution/legitimacy surface; no observed conduct or policy action |
| [Pew religious identity layer](pew-2025-religious-affiliation-switching-cultural-identity-layer-v1.md) | Same survey respondent; 2023–24 RLS | Childhood/current affiliation and switching | Spirituality, cultural/family connection, practice | Open | Open | Strong identity/meaning surface; no linked community or political episode |

## Coverage result

No retained row closes the entire chain:

```text
dated condition -> interpretation -> distinct action -> actor response
  -> outcome/recovery -> later trust, identity, or exit
```

The closest partial designs are complementary rather than combinable. HTOPS
and ANES supply temporal ordering; CES and CCES supply attribution or action;
SHED and SIPP supply material or program transitions; smartphone, diversity,
moral-values, and religion supply rich meaning measures. None supplies all of
those stages for the same unit.

## Next acquisition decision

Prioritize one lawful repeated or event-compatible source that contains at
least three adjacent stages and a usable clock. The preferred schema is:

```text
unit_id, event_date, exposure, alternative, identity, interpretation,
action, actor_response, outcome, recovery_or_exit, missingness, weight
```

Do not acquire PSID, restricted panels, or large platform logs until access,
variable presence, permitted use, and a concrete estimand are confirmed. A
source that only adds another attitude percentage should not outrank a compact
source that closes an adjacent same-unit arrow.

## Boundary

This matrix is a design and observability audit, not a meta-analysis. It does
not estimate prevalence, causal effects, or the proportion of Americans who
follow any route. “Open” is an evidence gap, not evidence that the stage does
not occur.
