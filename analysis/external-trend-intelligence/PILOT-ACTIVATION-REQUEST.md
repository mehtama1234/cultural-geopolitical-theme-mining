# Pilot activation request

This is the human handoff for moving one design-only pilot toward approval. It
is not permission to access company data and it does not upgrade an external
candidate.

## Recommended first pilot

Start with `pilot-food-security-service-room-001`, because its linked external
candidate is currently monitored rather than held. The pilot remains blocked
until the rights, decision, privacy, and preregistration gates below are
completed.

## Required information from the company

| Field | Required entry |
| --- | --- |
| Company and business unit | ______________________________ |
| Decision owner and decision deadline | ______________________________ |
| Internal dataset and snapshot/query | ______________________________ |
| Entity or aggregate basis | ______________________________ |
| Geography and period | ______________________________ |
| Primary outcome and denominator | ______________________________ |
| Comparison group and unit | ______________________________ |
| External-to-internal crosswalk | ______________________________ |
| Privacy class and lawful-access basis | ______________________________ |
| Retention and redistribution limit | ______________________________ |
| Analysis owner | ______________________________ |
| Falsifier and stop rule | ______________________________ |

## Required approvals, in order

1. External candidate remains qualified or monitored in the qualification
   matrix.
2. Source-specific rights owner approves the proposed reuse.
3. Company decision owner and business unit approve the question.
4. Internal data contract and crosswalk are complete.
5. Privacy, lawful access, retention, and redistribution review pass.
6. Analysis is preregistered with outcome, comparison, uncertainty, falsifier,
   stop rule, and unmatched-case handling.

Until all six steps are signed, the pilot status must remain
`design_only_external_gate`, `company_data_accessed=false`, and
`approved_test_count=0`.

## Sign-off record

| Role | Person/team | Date | Decision |
| --- | --- | --- | --- |
| External evidence reviewer | __________________ | __________ | hold / pass |
| Rights and privacy owner | __________________ | __________ | hold / pass |
| Company decision owner | __________________ | __________ | hold / pass |
| Analysis owner | __________________ | __________ | preregistered / not ready |
| Release owner | __________________ | __________ | approved test / hold |

The authoritative machine-readable contract remains
`pilot-contract-intake.json`; the validation rules remain in
`PILOT-VALIDATION-PROTOCOL.md` and `internal-bridge-schema.json`.
