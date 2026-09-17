# Broad next-episode selection v1

**Status:** ranked route decision; promotion gate applied; no qualifying local end-to-end route
**Checked:** 2026-09-17
**Machine record:** [next-episode selection](data/broad-next-episode-selection-v1.json)

## Decision

The existing MEPS 2024 staged event ledger was the primary local depth route.
Its 18,457 privacy-minimized person/event rows provide a dated first
event-family scaffold with payment, coverage, health, employment, and bill
context. The completed stage audit shows that the local representation lacks
the initiating need, usable alternatives, event-specific response, verified
remedy, and meaning/action endpoint.

The next primary route is therefore the registration-gated UAS acquisition
specified in the [UAS health-cost episode audit](projects/us-health-cost-household-choice/uas-health-cost-legitimacy-acquisition-audit-v1.md).
UAS is the smallest identified candidate that could connect a reported
medical-expense event to later health/work/well-being measures and, through
UAS 537 or 698, add care choice, bill, provider-experience, and
institution-specific trust fields. No UAS respondent files are currently
retained or acquired.

Keep the CFPB/platform records and the named Cash App, BrightSpeed, and
Navient redress records as storage-light remedy counterexamples and fallback,
not as a substitute for the missing UAS/MEPS middle. They provide stronger
institutional response and partial remedy or distribution evidence, but sparse
alternatives, receipt, durability, trust, and exit. Keep SHED and HTOPS as
panel context; do not join any of these sources into one person or household
story.

## Promotion-gate result

No currently retained route qualifies for promotion to a new end-to-end
finding. The governing gate requires both (a) an episode-level alternative or
non-use observation and (b) a receipt or outcome follow-up. MEPS fails both
requirements in its staged rows. The CFPB/platform route supplies formal
response and redress comparators, but not recipient-level receipt or a defined
post-remedy outcome. SHED/HTOPS supply persistence or adaptation context, but
not a dated actor-linked remedy episode. UAS is the best next acquisition
candidate for a same-respondent health-cost route, but its files are not yet
available and its documentation does not establish a verified remedy field.

The next pass may be promoted only after an acquired or lawfully linked source
demonstrates both gate fields, reports their denominators and missingness, and
preserves the distinction between institutional response and lived outcome.
Until then, the correct output is an acquisition boundary or route-specific
comparator—not a new causal or pooled trend claim.

## Required MEPS depth test

Before promoting another finding, inspect whether the staged MEPS rows contain:

```text
dated event
  -> initiating need and usable alternative
  -> care choice/delay and payment timing
  -> work, unpaid-care, food, housing, or debt trade-off
  -> provider/insurer/employer response and verified remedy
  -> later health, security, trust, action, switching, or exit
```

If the UAS fields or overlap fail the acquisition gates, the result is a
verified acquisition gap—not a reason to infer a bill-to-recovery chain from
round-level context. The CFPB/platform route remains the next small
remedy-focused comparison, while the broad 14-theme rotation continues through
other lanes.

## Why this is the right broad-program move

The choice preserves breadth and depth simultaneously. MEPS can deepen the
household, care, health, work, financial, and institutional themes; the CFPB
and platform cases preserve consumer power and recourse; SHED/HTOPS preserve
adaptation, persistence, trust, and political context. The sources remain
layered evidence surfaces, not a fabricated end-to-end case.

## Reproduction

```text
python3 scripts/validate_broad_next_episode_selection.py
```

No new raw data are downloaded by this decision artifact.
