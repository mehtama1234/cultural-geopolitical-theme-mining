# Navy execution-data request handoff

Purpose: acquire a comparable execution or award outcome for the dry-dock and
cargo-inspection defense lane without treating a budget request as realized
demand.

## Request scope

- **Primary route:** USAspending.gov contract and transaction search/API.
- **Context route:** official Navy/ NAVSEA award notices and maintenance
  execution releases.
- **Period:** FY2024-FY2027, preserving fiscal-year and transaction dates.
- **Geography:** United States; identify facility, shipyard, fleet command, or
  port where available.
- **Entities:** Bath Iron Works / General Dynamics Bath Iron Works, public
  naval shipyards, and other named facilities only when the artifact exposes
  the recipient or site identity.
- **Measures:** obligations, contract/award count, award date, period of
  performance, maintenance availability, completion or delivery milestone,
  and facility/shipyard identifier.

## Required review fields

Record the canonical publisher and exact artifact, query/API URL, retrieval
timestamp, checksum, fiscal-year and transaction-period definitions, award or
availability unit, recipient/facility denominator, suppression or missingness,
and any methodology or revision notes. Preserve the distinction between
budget authority, obligations, awards, planned availabilities, and completed
work.

## Rights and independence boundary

Retain normalized values, query parameters, source locator, checksum, and
attribution. Do not redistribute bulk USAspending downloads, Navy PDFs, or
derived company charts until exact artifact terms and permitted transformation
scope are recorded. The Navy budget is a single-publisher context source;
execution evidence must be lineage-reviewed against the IBIS claim and must
not be called independent merely because it uses a different URL.

## Stop rule

Do not promote the IBIS claim, calculate a dry-dock utilization trend, or
connect company data if the execution artifact lacks a compatible period,
geography, recipient/facility identity, outcome definition, or rights basis.
Budgeted workload is not a realized outcome.

## Current disposition

`request_ready_execution_award_acquisition_only`

The existing Navy artifact remains `official_context_acquired_scope_review_pending`.
This handoff does not grant access, rights, independence, or company-bridge
approval.
