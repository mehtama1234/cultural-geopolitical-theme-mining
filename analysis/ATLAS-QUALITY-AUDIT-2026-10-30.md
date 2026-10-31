# Atlas quality audit — 2026-10-30

**Scope:** structural audit of the current cultural/geographical theme-mining
atlas after the portfolio-synthesis evidence refresh. This is a repository
quality snapshot, not a claim that the substantive evidence is complete.

## Verified invariants

| Check | Result | Interpretation |
|---|---:|---|
| CSV files under `analysis/` | 337 | Includes packet ledgers and older control/audit tables. |
| CSV data rows | 2,678 | Counts exclude headers and do not imply comparable units. |
| Files with internally inconsistent row widths | 0 | Every CSV has a consistent width within its own file. |
| Registered Markdown packet links | 362 | The register contains repeated links across its historical and current sections. |
| Unique registered packet paths | 332 | Deduplicated path count. |
| Missing registered packet files | 0 | Every registered `.md` packet path resolves under `analysis/`. |
| Master synthesis propositions | 461 | Numbered propositions before the evidence-boundary section. |
| Proposition sequence | strict 1–461 | No missing or duplicate proposition number in the current range. |

## Intentional schema families

The atlas does not force every CSV into one schema because older packet types
capture different evidence contracts. Current internally consistent widths are:

- 229 files with 9 columns;
- 99 files with 8 columns;
- 4 files with 10 columns;
- 4 files with 7 columns;
- 1 file with 16 columns.

The invariant is therefore **row-width consistency within each ledger**, not
one universal header. New conversion packets should use the eight-column
schema unless they require a clearly documented packet-specific contract.

## Substantive limitations that remain open

- Structural validity does not establish source accuracy, causal identification,
  representative sampling or outcome completeness.
- A registered packet can be current in the repository while its external URLs,
  policy status or real-world outcomes change; source refresh remains required.
- The master proposition sequence is complete as numbering, not as end-to-end
  evidence. Many propositions deliberately stop at operation, governance or
  aggregate outcomes.
- Repeated register links are historical/current section reuse, not missing-file
  errors; future register refactoring should preserve provenance before removing
  historical entries.
- Parallel worktree edits outside the scoped audit files remain outside this
  snapshot and were not staged or altered.

## Re-run contract

Re-run the audit by checking, for every `analysis/*.csv`, that all rows have the
same number of fields; extract every Markdown packet link from the promotion
register and test that the target exists; and parse proposition numbers before
`## What the evidence does not support` for strict consecutiveness. Any future
repair should record the affected file, original width, corrected width and why
the correction preserves the evidence meaning.
