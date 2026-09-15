# Finding 067: Task-adoption comparisons depend on taxonomy reconciliation

**Status:** provisional measurement-layer finding · **Checked:** 2026-09-14

## The bounded finding

The acquired NBER W35677 task indexes and official O*NET 31.0 files can be
placed in a reproducible comparison surface, but they are not interchangeable
tables. Their labels align strongly after normalization, while their
identifiers encode different hierarchy conventions. The safe result is a
taxonomy-reconciliation layer, not a direct claim about workers, firms, or
control.

| Input | Observed result | Interpretation |
|---|---:|---|
| NBER DWA labels | 1,655 rows; 1,653 unique normalized matches; 2 unmatched | Strong label-level overlap, with a small unresolved tail |
| NBER IWA labels | 322 rows; 322 unique normalized matches | Broad intermediate-work mapping is complete at the normalized-label stage |
| NBER BWA rows | 9 rows; 9 prefix-level aggregates | Broad work areas are an aggregation layer, not exact O*NET task rows |
| Exact identifier equality | None under the current raw comparison | Identifier mismatch is structural and must not be mistaken for no overlap |

## Identifier diagnostic

A structural probe converts NBER's `I##` activity and `D##` detail components
into the letter/integer form used by O*NET. It is useful as a diagnostic, but
it is not a claimed vintage crosswalk. The transformed IDs matched an O*NET
ID in 1,510 of 1,655 DWA rows and 305 of 322 IWA rows. Among the unique
normalized-label matches, the transformed identifier agreed in 1,393 of 1,653
DWA rows and 269 of 322 IWA rows. The remaining label matches often point to
nearby but different hierarchy positions. This is evidence that label
normalization is doing substantive reconciliation work; it is not just
removing punctuation.

The diagnostic therefore supports a two-layer crosswalk: retain the NBER ID,
the O*NET ID, the label-match class, and the structural-ID result separately.
Never overwrite one identifier with the other or describe the transformed ID
as an exact historical equivalence.

The official O*NET 30.3 and 31.0 `gwas_to_iwas_to_dwas.csv` files acquired for
the release check are byte-identical. That does not prove NBER used either
release, but it does rule out this particular O*NET mapping-file change as an
explanation for the observed disagreements. The remaining explanation space
includes NBER's own hierarchy convention, a different O*NET vintage or file,
or changes in how labels were assigned.

The two unmatched DWA labels are retained rather than silently forced into an
O*NET row. “Clean work areas or facilities.” has two plausible O*NET
candidates, while “Collect payments for good or services.” has a probable
typographical counterpart. Neither is promoted to an exact match without a
source-vintage or identifier confirmation.

## What the reconciliation makes possible

The acquired files and provisional crosswalk now support:

- a documented bridge from NBER DWA/IWA/BWA labels to O*NET 31.0 task and
  hierarchy metadata;
- a transparent count of exact, normalized, candidate-set, and unmatched
  cases;
- a later occupation or subgroup comparison in which task exposure is kept
  separate from adoption, pay, time, discretion, and worker outcomes; and
- a reproducible audit trail for revising the crosswalk when a later O*NET or
  NBER vintage changes a label or hierarchy.

## What it does not establish

The crosswalk does not establish that a task was automated, that a worker used
AI, that a firm implemented a tool, or that work became more or less
controllable. It also cannot identify effects on wages, hours, bargaining,
household security, political meaning, institutional trust, or geopolitical
capacity. The labels describe related measurement objects; they do not supply
a worker, workplace, employer, date-of-change, or implementation key.

In particular, the BWA layer should not be expanded into exact task-level
coverage merely because its prefix aggregates resemble O*NET groupings. A
normalized label match is evidence of semantic proximity, not proof of
identical universe, coding rule, or release vintage.

## Why this matters for the end-to-end program

The program's causal chain needs a stable middle layer:

```text
occupation and task structure
  -> actual tool exposure or adoption
  -> implementation, discretion, and bargaining
  -> pay, time, security, and household adaptation
  -> trust, collective action, institutional response, or state capacity
```

The crosswalk improves the first join in that chain. It does not close any of
the later arrows. Keeping that distinction visible prevents a polished
occupation-to-task merge from becoming an unsupported worker-control story.

## Next decisive test

First confirm the NBER-to-O*NET release relationship and hierarchy identifiers
against the source documentation, then version the crosswalk with explicit
match classes and review decisions. Only after that should the program compare
task measures across occupations or worker subgroups. The next substantive
test must add a worker- or workplace-denominated outcome with date, exposure,
and uncertainty—not infer it from the taxonomy alone.

## Reproduction and sources

- [O*NET release metadata gate](../onet-release-metadata-gate-v1.md)
- [NBER W35677 task-level adoption layer](../nber-w35677-task-level-adoption-layer-v1.md)
- [Acquisition script](../../../../scripts/acquire_onet_nber_crosswalk_inputs.py)
- [Acquisition manifest](../data/onet-nber-crosswalk-2026-09-14/acquisition-manifest.json)
- [Provisional crosswalk](../data/onet-nber-crosswalk-2026-09-14/provisional-label-crosswalk.json)
- [Unmatched-label review](../data/onet-nber-crosswalk-2026-09-14/unmatched-label-review.json)
- [Identifier reconciliation audit](../data/onet-nber-crosswalk-2026-09-14/onet-nber-identifier-reconciliation-audit-2026-09-14.json)
- [O*NET 30.3 comparison mapping](../data/onet-nber-crosswalk-2026-09-14/gwas_to_iwas_to_dwas_30_3.csv)

**Evidence status:** official O*NET 31.0 files and public NBER W35677 index
files acquired and hashed; semantic equivalence and worker-level implications
remain open.
