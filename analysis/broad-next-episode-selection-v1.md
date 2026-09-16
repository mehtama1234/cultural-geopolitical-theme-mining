# Broad next-episode selection v1

**Status:** ranked local-route decision; no new estimate
**Checked:** 2026-09-16
**Machine record:** [next-episode selection](data/broad-next-episode-selection-v1.json)

## Decision

Use the existing MEPS 2024 staged event ledger as the primary next depth route.
Its local staged input is approximately 54 MB and contains 18,457
privacy-minimized person/event rows with a dated first event-family record and
exact person linkage to payment, coverage, health, employment, and bill context.
It is the strongest available local surface for the material → care/health →
household-security bridge.

Keep the CFPB/platform records as the remedy counterexample, not as a substitute
for MEPS. They provide stronger institutional response and partial remedy
evidence, but far fewer cases and sparse alternatives, receipt, durability,
trust, and exit. Keep SHED and HTOPS as panel context; do not join any of these
sources into one person or household story.

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

If the fields are absent, the result is a verified acquisition gap—not a reason
to infer a bill-to-recovery chain from round-level context. The platform route
then becomes the next small remedy-focused comparison, while the broad 14-theme
rotation continues through other lanes.

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
