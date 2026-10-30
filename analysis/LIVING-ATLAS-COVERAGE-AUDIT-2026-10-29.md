# Living atlas coverage audit — 2026-10-29

**Scope:** cultural, social, geographical, technological and geopolitical
theme-mining atlas  
**Baseline:** refreshed through Rotation FS
**Purpose:** verify artifact coverage, index integrity, local link integrity and
the boundary between the current bounded evidence release and the still-active
research goal.

## Verified current state

| Check | Result | Evidence |
|---|---:|---|
| Numbered synthesis propositions | 175 | `CULTURAL-GEOGRAPHICAL-CONVERSION-SYNTHESIS_2026-10-29.md`, propositions 1–175 in strict order |
| Standard rotation markdown packets | 174 | `analysis/ROTATION-*.md` |
| Standard rotation CSV ledgers | 174 | `analysis/ROTATION-*.csv` |
| Register rotation rows | 174 | `NEW-GOAL-THEME-PROMOTION-REGISTER_2026-10-29.md` |
| Local register links | checked after FS; 0 missing | link-target scan of the register |
| Recent packet CSV shape | six rows and nine fields for FS; all six source IDs present | `ROTATION-FS-PRESS-FREEDOM-LOCAL-INFORMATION-PUBLIC-GOOD-2026-10-29.csv` |
| Scoped whitespace validation | passed | `git diff --check` on latest packet, register and synthesis |
| Remote branch | synchronized | `origin/main` at the latest pushed commit |

## Why packet and proposition counts differ

The 175 propositions are conversion propositions in the synthesis. The 174
rotation rows are register entries for the current packet portfolio. They are
not required to be one-to-one because the portfolio includes earlier
cross-rotation and first-pass architecture.

The standard packet directory contains 174 markdown and 174 CSV files, but the
first-pass/source-ledger architecture has three intentional naming pairs:

- `ROTATION-A-FIRST-PASS` ↔ `ROTATION-A-SOURCE-LEDGER`
- `ROTATION-B-FIRST-PASS` ↔ `ROTATION-B-SOURCE-LEDGER`
- `ROTATION-C-FIRST-PASS` ↔ `ROTATION-C-SOURCE-LEDGER`

This is an intentional historical structure, not an untracked missing ledger.
New named conversion rotations use a same-stem markdown/CSV pair.

## Integrity controls now in force

1. Every new conversion rotation requires a markdown packet, a machine-readable
   CSV ledger, a register row, a synthesis proposition, a source boundary and
   at least one counterexample.
2. Each packet must preserve the six clocks: signal, mechanism, operation,
   material consequence, meaning and power.
3. A policy, target, dashboard, installation, enrolment or reported contact is
   not promoted to a later outcome without a named unit, date, geography and
   follow-up evidence.
4. The synthesis proposition index is checked separately from the six-stage
   research table so table row numbers are not mistaken for propositions.
5. Local register links are checked after packet additions; broken links block
   the release of a new rotation until corrected.
6. Parallel-thread worktree changes outside the scoped atlas files are preserved
   and are not included in rotation commits.

## Evidence boundary

The audit verifies repository structure and promotion controls. It does not
claim that all Tier 2 outcomes are closed. The current atlas still contains
source-boundary questions around named daily use, treatment, recovery, receipt,
worker safety, household security, participation, power and remedy. Those are
acquisition targets, not failures of the artifact audit.

## Next research action

Continue with the next distinct or deepening theme only after checking for
duplication against the register. Prioritize source acquisition that closes the
next arrow in a named chain—especially operation to material consequence and
material consequence to meaning or power—while preserving counterexamples,
geography, unit and time.
