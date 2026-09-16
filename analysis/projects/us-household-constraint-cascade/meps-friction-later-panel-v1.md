# MEPS institutional-friction to later-panel screen v1

**Checked:** 2026-09-16  
**Status:** strict-window same-person descriptive association; not a remedy or
causal estimate

## Question

Does reported denial or prior-authorization delay (`EQDENY53`) on the same
strict-window event/person frame coexist with different later health and work
transitions?

```text
first event strictly between R3/1 and R4/2
  + round-level denial/prior-authorization report
  -> R4/2 baseline status -> R5/3 health/work transition
```

The later panel adds a persistence clock to the existing friction cascade. It
does not identify a claim, denial date, appeal, response, correction, or
remedy.

## Results

Shares are person-weighted with 128 BRR replicates. Each pair is
denial/delay versus no denial/delay. Transition measures condition on the
corresponding valid R4/2 baseline state.

| Event family | Friction n | Fair/poor health R4 → R5 | Fair/poor resolved | Fair/poor onset | Not employed R4 → R5 | Nonemployment resolved | Nonemployment onset |
|---|---:|---:|---:|---:|---:|---:|---:|
| Office | 227 / 1,562 | 19.90% → 23.13% / 9.93% → 10.83% | 24.11% / 37.57% | 10.02% / 5.11% | 30.19% → 33.49% / 34.68% → 36.02% | 1.41% / 5.09% | 5.83% / 4.63% |
| Emergency room | 165 / 549 | 43.19% → 40.07% / 26.05% → 27.96% | 31.45% / 28.47% | 18.43% / 12.51% | 44.06% → 42.11% / 51.12% → 53.73% | 9.50% / 1.98% | 3.51% / 7.40% |
| Inpatient | 80 / 303 | 50.07% → 50.55% / 27.95% → 27.23% | 22.10% / 34.66% | 23.13% / 12.26% | 53.56% → 60.83% / 62.01% → 63.88% | 5.63% / 1.84% | 22.14% / 7.93% |

The clearest descriptive persistence signal is health: office and inpatient
friction groups have lower health-resolution and higher health-onset shares
than their no-friction comparison groups; the ER contrast is also higher on
health onset but has similar resolution point estimates. Employment transitions
are mixed and the inpatient friction cells are small.

## What this adds to the cascade

This is a bounded institutional-friction → later-status bridge. It shows that
the friction comparison can be carried beyond the R4/2 burden context to a
later R5/3 health/work clock on the same pseudonymous person key. It does not
show that denial caused the later status, that the event initiated the need, or
that an institution repaired anything.

## Boundaries

- `EQDENY53` is a round-level reported denial/prior-authorization indicator;
  it has no claim identifier, decision date, appeal, response, or remedy.
- The strict event window is month-bounded and selects the first observed event;
  the event may follow the initiating need.
- The no-denial group is a comparison, not a counterfactual, and both groups
  can contain other events and unmet needs.
- R5/3 health and employment transitions are not verified recovery from the
  event or denial. Treatment continuity, coverage changes, attrition, severity,
  and baseline selection remain unresolved.
- Inpatient friction cells are sparse and should not be ranked against larger
  office or ER cells.

## Reproduction

- [Machine-readable output](data-meps-friction-later-panel-2024.json)
- [Analysis script](../../../scripts/analyze_meps_friction_later_panel.py)
- [MEPS dated friction cascade](meps-dated-friction-cascade-v1.md)
- [MEPS event six-month follow-up](meps-event-six-month-followup-v1.md)
- [Same-case closure protocol](same-case-closure-protocol-v1.md)

The machine-readable output records SHA-256 hashes and paths for the HC-256,
BRR, and three event inputs, so the local source vintage is auditable without
committing raw files.

Primary HC-256 hash: `b4bde859b39f626345561c05570292bb7264dd92eb76ce0c1a14d6b89076aed5`
BRR hash: `44f1e5a864c1d318327a0fbd3a0ff48a583c74c3a104aae357032cfbfaa5a32e`
Script hash: `1560b36d8cd7dbacd4a588e79c9ca652c6c3c4a1f32dc1c2a4ddc7f420472ba4`
Output hash: `c60aa8a1443cd0bba9afeb3f65a2fb1147a333b241512c3bb5498704cb29b9fc`

**Evidence status:** reproduced later-panel friction association; not a
same-case response, remedy, recovery, trust, political-action, switching, or
exit result.
