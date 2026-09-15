# O*NET release and crosswalk metadata gate v1

**Checked:** 2026-09-14  
**Status:** official inputs acquired and hashed; structural identifier diagnostic completed; semantic crosswalk validation remains open

## Why this gate exists

The NBER W35677 public indexes use occupation/task identifiers and labels. The
index rates can be reproduced without O*NET, but a worker-level or longitudinal
comparison requires a fixed occupation taxonomy, task identifier definition,
and versioned crosswalk. Otherwise a changed label or occupation composition
can be mistaken for changed AI adoption.

## Official release state

The [O*NET release archive](https://www.onetcenter.org/db_releases.html) and
[O*NET database page](https://www.onetcenter.org/database.html) identify O*NET
31.0, August 2026, as the current production release at this check. The
archive also lists 30.3 (May 2026), 30.2 (February 2026), and 30.0 (August
2025), which bracket the four NBER RPS waves used in W35677. O*NET 31.0 is
available in CSV, JSON, Excel, SQL, and RDF formats under the stated Creative
Commons terms.

This is release metadata, not a claim that the NBER index was generated from
O*NET 31.0. The NBER workbook's task IDs and its own survey/index vintage must
be reconciled to the exact O*NET release before a crosswalk is promoted.

## Required reproducibility fields

| Field | Required treatment |
|---|---|
| O*NET release | Record exact version and release month; do not use “current” as a vintage. |
| File format | Preserve the downloaded file type and a SHA-256 hash. |
| Occupation taxonomy | Record O*NET-SOC version and any SOC crosswalk. |
| Task identifiers | Match NBER DWA/IWA/BWA IDs and labels; report unmatched and duplicate IDs. |
| Changes | Keep a machine-readable diff of additions, removals, relabeling, and occupation updates. |
| NBER index vintage | Preserve the four RPS waves, sheet IDs, row counts, blank-cell rule, and index hashes. |
| Analysis boundary | Keep metadata alignment separate from worker adoption, employer control, pay, and outcome estimates. |

## First audit result

The [machine-readable audit](data/onet-31-0-nber-crosswalk-audit-2026-09-13.json)
compares the acquired NBER sheets with the O*NET 31.0
`gwas_to_iwas_to_dwas.csv` mapping. Exact identifier matches are zero because
the two systems encode the hierarchy differently. Normalized labels match for
1,653 of 1,655 DWA rows and all 322 IWA rows. Two DWA labels do not match the
O*NET 31.0 mapping exactly, and the nine NBER BWA labels are an aggregation
layer not present as exact O*NET GWA labels. This is a useful reconciliation
lead, not a validated crosswalk.

A structural probe that converts NBER's numbered activity/detail components to
the O*NET letter/integer form matches O*NET IDs in 1,510/1,655 DWA rows and
305/322 IWA rows. This is materially weaker than the normalized-label result,
and the two diagnostics disagree for many rows. The conversion is therefore
retained as a structural diagnostic, not promoted as an exact historical
crosswalk.

The official O*NET 30.3 and 31.0 mapping files used in the release check are
byte-identical. This rules out that specific mapping-file revision as the
explanation for the NBER/O*NET identifier disagreement, while leaving open
NBER's source convention, another O*NET file/vintage, or hierarchy assignment.

Because the detailed and intermediate matches are unique after normalization,
the repository now includes `scripts/build_nber_onet_label_crosswalk.py`. It
produces a provisional row-level crosswalk from the externally retained NBER
CSVs and O*NET mapping file. “Provisional” is intentional: normalized labels
are not proof that the two projects used identical taxonomy vintages or
meanings.

The resulting [provisional crosswalk artifact](data/onet-nber-crosswalk-2026-09-14/provisional-label-crosswalk.json)
contains 1,986 entries: 1,977 row-level DWA/IWA entries, with 1,975 unique
normalized-label matches, two unmatched DWA labels, and no ambiguous matches;
plus nine BWA prefix-aggregation entries. The BWA entries retain NBER's
different labels and list the O*NET GWA prefix members—they are not treated as
exact label matches.

## Acquisition completed

The official O*NET 31.0 CSV archive and the three public NBER W35677 index
sheets were acquired on 2026-09-14 into the versioned acquisition directory.
The [acquisition manifest](data/onet-nber-crosswalk-2026-09-14/acquisition-manifest.json)
records URLs, byte counts, and SHA-256 hashes. The [recomputed provisional
crosswalk](data/onet-nber-crosswalk-2026-09-14/provisional-label-crosswalk.json)
reproduces 1,655 DWA rows, 322 IWA rows, and 9 BWA rows: 1,653 DWA and all
322 IWA rows match uniquely after normalization; two DWA labels remain
unmatched; BWA remains a prefix aggregation. The acquisition script is
[`acquire_onet_nber_crosswalk_inputs.py`](../../../scripts/acquire_onet_nber_crosswalk_inputs.py)
and the crosswalk builder remains
[`build_nber_onet_label_crosswalk.py`](../../../scripts/build_nber_onet_label_crosswalk.py).

Each DWA/IWA row now also retains a structural-ID probe, whether that probe
exists in the O*NET mapping, and whether it agrees with the label match; these
fields are diagnostic and are not promoted to exact equivalence.

This closes file retrieval and hash reproducibility, not semantic equivalence.
The [unmatched-label review](data/onet-nber-crosswalk-2026-09-14/unmatched-label-review.json)
narrows the remaining problem: one DWA label has two plausible O*NET candidates,
and the other is a probable typographical match. Neither is promoted to an
exact identifier crosswalk without a documented source-vintage relationship.
The [identifier diagnostic](data/onet-nber-crosswalk-2026-09-14/onet-nber-identifier-reconciliation-audit-2026-09-14.json)
records the structural conversion, its disagreement with label matches, and
the source hashes.

The [paper-method audit](nber-w35677-paper-method-audit-2026-09-14.md) now
resolves the conceptual relationship: W35677 uses O*NET-derived work
activities, 2018 SOC occupation coding, and the DWA → IWA → WA → BWA
aggregation. It does not state the exact O*NET database release behind the
public sheets or publish an NBER-ID-to-O*NET-ID table, so exact identifier
equivalence remains open.

## Next test

Identify the exact NBER-to-O*NET identifier relationship, resolve the two
unmatched DWA labels, and compare against the relevant prior release only after
the IDs and labels are reconciled. The resulting metadata can then support
compatible subgroup or occupation comparisons; it cannot by itself establish
workplace control or worker benefit.

**Evidence status:** official release inventory, file acquisition, byte hashes,
and provisional crosswalk are recorded; semantic exactness and downstream
worker-outcome linkage remain open.
