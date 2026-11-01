# Feeding America Map the Meal Gap data request

This is a human acquisition handoff for the request-gated Map the Meal Gap
dataset. The public national page is already captured in
`feeding-america-map-meal-gap-2026-national.json`; this request is for the
underlying county/state release needed to test the IBIS community-food-services
claim.

## Request scope

- Release: latest Map the Meal Gap release reflecting 2024 estimates;
- geography: county, congressional district, state, and national rows;
- measures: overall and child food-insecurity rate, estimated population,
  program-eligibility bands, meal cost, and food-budget shortfall;
- metadata: model vintage, source inputs, missingness, imputation, suppression,
  uncertainty or interval guidance, and any methodology break;
- provenance: exact file name, publisher owner, retrieval date, checksum, and
  whether values are modeled or directly observed; and
- rights: exact license or written permission for storage, transformation,
  derived charts, redistribution, and company-facing use.

## Required review before acquisition is counted

1. Preserve the request response, exact artifact, checksum, terms, and source
   locator in a source-specific register.
2. Reconcile Feeding America’s modeled individual denominator with USDA’s
   household denominator; do not subtract or average the two rates.
3. Map the model’s CPS-FSS, ACS, BLS/LAUS, and food-price inputs to existing
   source lineage and mark shared inputs as dependence, not corroboration.
4. Preserve the 2023/2024 model and question changes before any time-series
   comparison.
5. Acquire a provider-side utilization or capacity outcome separately; Map the
   Meal Gap alone does not measure visits, meals served, wait time, capacity,
   or provider revenue.

## Current disposition

`request_ready_public_snapshot_only`

The public map supports a citable national context snapshot. The underlying
dataset remains request-gated, rights are not cleared for redistribution, and
the IBIS claim remains held. No company data may be connected from this handoff.

## Stop rule

If the exact file, rights terms, model inputs, denominator, or uncertainty
documentation cannot be obtained, retain the public snapshot as context only
and leave the comparison at `non_pooled_directional_context_only`.

