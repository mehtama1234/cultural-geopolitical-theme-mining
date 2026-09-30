# LA County rebuilding dashboard: damage is becoming an operating pipeline, not yet household recovery

## Finding

The public 2025 Fire Rebuilding dashboard exposes a useful middle layer between
wildfire damage and lived recovery. Its September 29, 2026 refresh reports an
estimated 7,417 damaged/destroyed unincorporated units and 6,571 parcels. Its
construction-stage view contains 1,752 visible stage records: 69 pre-
construction, 706 at early inspection/location/setbacks, 401 at framing, 329
at exterior lath/insulation/drywall, 19 at exterior utilities, 25 at final
inspection, and 203 finaled or ready for a certificate of occupancy.

Permit-type cards show a larger administrative pipeline—for example, 2,229
single-family permits issued, 1,702 in construction, and 161 completed; 347
detached-ADU permits issued, 223 in construction, and 42 completed; and 672
single-family-with-attached-ADU permits issued, 471 in construction, and 14
completed. These are dashboard measure strings, not a denominator-safe
completion rate.

The same refresh reports 4,052 rebuild applications received, 3,786 zoning
reviews cleared, 3,402 full building plans received, 4,160 plans approved,
3,811 building permits issued, 2,396 new-residential projects in construction,
and 217 completed. It also reports 128.75 business days with the applicant,
30.75 business days in county review, and 159.5 business days to permit
issuance. These are not a common-denominator funnel and the waiting measures
are administrative workflow time, not household time burden.

The County DEO/LAEDC June 8, 2026 economic update adds a broader recovery
check: 26.7% of destroyed structures had received rebuild permits, but only
0.47% had completed reconstruction and occupancy approval. It also reports that
38% of survivors had exhausted or were nearing exhaustion of displacement
assistance, Metro routes most affected by the fires remained 17.7% below the
adjusted pre-fire baseline, and annual localized spending losses were estimated
at $79 million in the Palisades and $73.6 million in the Eaton area. These are
official multi-indicator aggregates, not a same-household insurance-to-occupancy
panel; they make the conversion gap visible without identifying its binding
mechanism for each household.

## Cross-domain mechanism

```text
wildfire damage and displacement
  -> public damage/parcel estimate
  -> permit application and review
  -> inspection / construction stage
  -> finaling or certificate readiness
  -> [open] occupancy, insurance payment adequacy, mortgage continuity,
           household room, stay/move, and later insurance choice
```

This closes an important operational middle stage. A state can report billions
of dollars paid and a county can report permits advancing, while the same
household's safe return, temporary-housing burden, mortgage status, and renewed
coverage remain unknown.

## Method and boundary

The [machine-readable record](../../records/us-la-county-fire-rebuilding-dashboard-2026.json)
was reproduced from the dashboard's public Power BI semantic schema and
aggregate visual queries. The public schema contains address and permit-number
fields, but this pass intentionally extracted no address-level or permit-level
rows. Damage estimates, construction-stage records, permit cards, insurance
claims, and households are retained as separate units.

The dashboard is an administrative operating surface, not a claims file or
household panel. A finaled permit or certificate readiness is not proof of
occupancy, safe return, affordability, insurance payment, or durable recovery.

## Next test

The strongest next public extraction is a geography-bounded, non-sensitive
ledger joining dashboard refresh date, fire area, parcel/permit stage, and
public rebuilding status. It should report unmatched counts and revision dates
before any stage conversion. A true household recovery claim still requires
lawful claim/payment, repair, temporary-housing, mortgage, occupancy, and later
insurance-status linkage.

## Sources

- [LA County permitting progress dashboard](https://recovery.lacounty.gov/rebuilding/permitting-progress-dashboard/)
- [LA County data and recovery tools](https://recovery.lacounty.gov/data-recovery-tools/)
- [Metric definitions](https://file.lacounty.gov/SDSInter/dpw/recovery/1203584_2025FireRebuildingMetricDefinitions.pdf)
- [California DOI wildfire claims tracker](https://www.insurance.ca.gov/01-consumers/180-climate-change/Wildfire-Claims-Tracker.cfm)
- [LA County DEO/LAEDC wildfire economic update, June 8, 2026](https://lacounty.gov/2026/06/08/la-county-deo-and-laedc-release-latest-economic-update-on-the-2025-wildfire-recovery/)
