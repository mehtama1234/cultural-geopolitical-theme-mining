# MEPS staged ledger stage-coverage audit v1

**Checked:** 2026-09-16  
**Status:** local staging audit; not a promoted population finding  
**Purpose:** make the broad program's end-to-end evidence boundary explicit

## Result

The existing privacy-minimized MEPS 2024 event ledger contains **18,457
observed event rows**: 14,198 office events, 2,868 emergency-room events, and
1,391 inpatient events. The rows are one first valid event per positive-weight
person and event family; they are not a population estimate. Of the rows,
4,868 (26.3748%) fall strictly between the R3/1 and R4/2 endpoint months and
13,589 (73.6252%) do not. That flag establishes temporal context only; it does
not establish causation.

The stage audit shows the precise boundary:

| Stage | Rows | Status | What that means |
|---|---:|---|---|
| Trigger | 18,457 | observed | A dated first event family is present; the initiating need is not identified |
| Practical room and alternatives | 18,457 | observed | Event payment and round coverage/poverty context are present; alternatives are not observed |
| Choice and trade-off | 18,457 | reported | Round care-delay context is present; event-specific choice and household trade-off are not identified |
| Institutional route | 18,457 | reported | Round denial/prior-authorization context is present; response, appeal, and authority are not identified |
| Remedy verification | 18,457 | unknown | Correction, arrangement, coverage restoration, or no remedy is not measured |
| Follow-up outcomes | 18,457 | reported | Round bill/debt/collector and health/employment context is present; event-specific recovery is not measured |
| Meaning and action | 18,457 | unknown | Trust, attribution, civic action, switching, and exit are not measured |

## Why this matters to the broader goal

This is useful across the full societal, cultural, political, consumer,
institutional, financial, firm, infrastructure, and geopolitical atlas because
it separates a real measured condition from a complete social mechanism. A
large event frame can show exposure and practical room while still leaving the
middle and endpoint of the cascade open. The same discipline applies to a
complaint, benefit transition, workplace change, housing-risk event, public
procurement milestone, or geopolitical capability claim.

The ledger therefore supports bounded statements such as “event payment and
round-level financial context coexist with later contextual indicators.” It
does not support “the event caused a household trade-off,” “the institution
failed or remedied the case,” or “the experience changed trust, political
action, switching, or exit.”

## Next evidence target

The next acquisition or linkage should fill the open middle with a dated,
privacy-approved same-unit design containing:

1. the original need or obligation and usable alternatives;
2. the actual choice, delay, substitution, payment timing, or foregone use;
3. the institutional route, effort, appeal, response, and authority;
4. a verified remedy or verified non-remedy; and
5. later recovery, trust, action, switching, or exit.

Until those fields are available, this artifact remains an evidence-boundary
audit rather than a new causal or population trend claim.

## Reproduction

The audit reads the existing local JSONL and downloads nothing:

```bash
python3 scripts/audit_meps_constraint_cascade_stage_coverage.py \
  /tmp/cgtm-meps-2024/household-constraint-cascade-staged-ledger.jsonl \
  --output-json analysis/projects/us-household-constraint-cascade/data/meps-staged-ledger-stage-coverage-2024.json
```

The input SHA-256 is
`8ebaf499e161e8f7f034f6661ae35ad94de6a6e02c8baaae1c30c7e12803f320`.
The machine-readable output is [the stage-coverage audit JSON](data/meps-staged-ledger-stage-coverage-2024.json).
