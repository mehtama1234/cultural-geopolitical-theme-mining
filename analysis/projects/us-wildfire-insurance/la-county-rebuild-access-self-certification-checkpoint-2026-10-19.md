# LA County rebuild access and self-certification checkpoint

**Status:** bounded administrative-access update; no household recovery claim.

## What changed in the public route

Los Angeles County’s current rebuilding pages expose two additional conversion
stages for Eaton and Palisades survivors:

1. **Plan-review access:** the Building Plan Self-Certification Pilot allows
   eligible California-licensed architects and engineers to self-certify code
   compliance for qualifying replacement single-family homes, garages, and
   ADUs in unincorporated Los Angeles County. The owner and professional must
   sign an acknowledgement for each submission. Other county approvals still
   apply before a permit is issued.
2. **Administrative quality control:** the county says it will randomly audit
   at least 20% of self-certified plans and fully inspect self-certified
   projects at all construction stages. This is a control design, not evidence
   of audit findings or completed construction.
3. **Cost-access route:** qualifying owner-occupants of destroyed or irreparably
   damaged single-family properties may request permit and inspection-fee
   deferral or refund. The page says refunds go to the original payee and are
   usually processed within two to four weeks after a correct request, but it
   publishes no request denominator, issued-refund count, dollar total, or
   household follow-up.

## Conversion boundary

```text
fire damage
  -> eligibility and professional access
  -> self-certified plan / fee-deferral request
  -> permit and inspection controls
  -> [open] payment or refund receipt, construction completion,
           occupancy, safe return, insurance continuity, and later choice
```

The update improves the map of how a qualifying owner can reduce review time
or upfront public fees. It does not establish that a survivor used the route,
received a refund, obtained a permit, completed construction, returned home,
or retained/replaced insurance. It also does not cover renters, multifamily
properties, commercial properties, or all fire-affected jurisdictions.

## Next bounded extraction

### Temporal access boundary

The public semantic model exposes a `Check_In_Date` field for One-Stop Center
visits. Filtered fire-area queries returned 406 Eaton daily rows and 109
Palisades daily rows, which were aggregated into month-level totals. The
result reconciles to the previously observed totals of 32,336 Eaton visits and
789 Palisades visits. The [canonical dashboard record](../../records/us-la-county-fire-rebuilding-dashboard-2026.json)
retains the monthly series and query hashes. This remains an encounter series,
not a unique-visitor or household-outcome panel; October 2026 is partial.

The next public-data test should seek the county’s approved-professional list,
self-certified project count, audit findings, permit issuance, and inspection
completion by fire area and refresh date. Keep the fields at program/project
level unless a lawful public record explicitly provides a non-sensitive project
identifier. Do not infer household recovery from eligibility, a fee request, a
self-certified plan, or a permit.

## Sources

- [LA County rebuilding hub](https://recovery.lacounty.gov/rebuilding/)
- [LA County Building Plan Self-Certification Pilot](https://recovery.lacounty.gov/rebuilding/self-certification/)
- [LA County fee deferrals and refunds](https://recovery.lacounty.gov/rebuilding/fee-deferrals-and-refunds/)
- [LA County permitting progress dashboard](https://recovery.lacounty.gov/rebuilding/permitting-progress-dashboard/)
