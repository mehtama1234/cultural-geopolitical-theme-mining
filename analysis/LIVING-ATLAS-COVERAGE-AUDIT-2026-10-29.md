# Living atlas coverage audit — 2026-10-29

**Scope:** cultural, social, geographical, technological and geopolitical
theme-mining atlas  
**Baseline:** refreshed through Rotation HC
**Purpose:** verify artifact coverage, index integrity, local link integrity and
the boundary between the current bounded evidence release and the still-active
research goal.

## Verified current state

| Check | Result | Evidence |
|---|---:|---|
| Numbered synthesis propositions | 213 | `CULTURAL-GEOGRAPHICAL-CONVERSION-SYNTHESIS_2026-10-29.md`, propositions 1–213 in strict order |
| Standard rotation markdown packets | 212 | `analysis/ROTATION-*.md` |
| Standard rotation CSV ledgers | 212 | `analysis/ROTATION-*.csv` |
| Register rotation rows | 212 | `NEW-GOAL-THEME-PROMOTION-REGISTER_2026-10-29.md` |
| Local register links | checked after HC; 0 missing | link-target scan of the register |
| Recent packet CSV shape | twelve rows and nine fields for HC; all twelve source IDs present after named-case refresh | `ROTATION-HC-CONTRACT-MANAGEMENT-PAYMENT-SERVICE-CONTINUITY-2026-10-29.csv` |
| Refreshed heat packet CSV shape | nine rows and nine fields for HHT; all nine source IDs present after affordability refresh | `ROTATION-X-EXTREME-HEAT-COOLING-PLACE-HEALTH-2026-10-29.csv` |
| Heat outcome-case CSV shape | twelve rows and nine fields for HHT; all twelve source IDs present after named outcome refresh | `ROTATION-X-EXTREME-HEAT-COOLING-PLACE-HEALTH-2026-10-29.csv` |
| Energy-affordability refresh CSV shape | eight rows and nine fields for ENR; all eight source IDs present after IEA/EPA refresh | `ROTATION-Z-ENERGY-INSECURITY-UTILITY-DISCONNECTION-HOUSEHOLD-OPTIONS-2026-10-29.csv` |
| HD packet CSV shape | six rows and nine fields for HD; all six source IDs present | `ROTATION-HD-CLIMATE-MENTAL-HEALTH-PSYCHOSOCIAL-AGENCY-2026-10-29.csv` |
| HE packet CSV shape | eleven rows and nine fields for HE; all eleven source IDs present after Bangladesh outcome/mechanism refresh | `ROTATION-HE-CLIMATE-SCHOOL-CONTINUITY-LEARNING-AGENCY-2026-10-29.csv` |
| DZ packet CSV shape | nine rows and nine fields for DZ; all nine source IDs present after London exposure, mortality and child-health refresh | `ROTATION-DZ-AMBIENT-AIR-POLLUTION-ENVIRONMENTAL-JUSTICE-2026-10-29.csv` |
| DS packet CSV shape | eight rows and nine fields for DS; all eight source IDs present after cultural-relations and peacebuilding case refresh | `ROTATION-DS-CULTURAL-DIPLOMACY-RECIPROCITY-LOCAL-OWNERSHIP-2026-10-29.csv` |
| DU packet CSV shape | eight rows and nine fields for DU; all eight source IDs present after vaccine, Nigeria and diagnostic-transfer case refresh | `ROTATION-DU-MEDICINES-LOCAL-PRODUCTION-SUPPLY-RESILIENCE-2026-10-29.csv` |
| DW packet CSV shape | nine rows and nine fields for DW; all nine source IDs present after named Arctic resupply, port, sealift and Inuit-IMO representation refresh | `ROTATION-DW-ARCTIC-SHIPPING-INDIGENOUS-SOVEREIGNTY-2026-10-29.csv` |
| DV packet CSV shape | eight rows and nine fields for DV; all eight source IDs present after Paris procurement, legacy-asset and Birmingham evaluation refresh | `ROTATION-DV-MEGA-EVENTS-HOST-CITY-LEGACY-DISPLACEMENT-2026-10-29.csv` |
| DM packet CSV shape | eight rows and nine fields for DM; all eight source IDs present after Solomon Islands, Cambodia and Mapuche food-system case refresh | `ROTATION-DM-INDIGENOUS-FOOD-SOVEREIGNTY-CLIMATE-ADAPTATION-CULTURAL-CONTINUITY-2026-10-29.csv` |
| Scoped whitespace validation | passed | `git diff --check` on latest packet, register and synthesis |
| Remote branch | synchronized | `origin/main` at the latest pushed commit |

## Why packet and proposition counts differ

The 213 propositions are conversion propositions in the synthesis. The 212
rotation rows are register entries for the current packet portfolio. They are
not required to be one-to-one because the portfolio includes earlier
cross-rotation and first-pass architecture.

The standard packet directory contains 212 markdown and 212 CSV files, but the
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
