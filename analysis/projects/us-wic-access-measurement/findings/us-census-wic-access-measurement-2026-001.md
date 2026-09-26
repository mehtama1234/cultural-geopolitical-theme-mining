# Finding 001: WIC access is a real estimate, not the same thing as completed protection

**Status:** bounded WIC access and measurement finding · **Checked:** 2026-09-22

## The bounded finding

The Census-FNS-ERS Joint Project links restricted WIC administrative records
with the American Community Survey to estimate who is eligible for WIC, who
participates, and who appears eligible but does not access the program. The
project produces state- and county-level estimates with demographic and
socioeconomic disaggregation. The paper also compares Census and USDA/FNS
estimates and notes that they differ in methodology and measurement scope.

The route is:

```text
eligible woman, infant, child, or household
  -> outreach and application route
  -> agency or clinic approval
  -> WIC participation and benefit receipt
  -> shopping, food security, and maternal/child health [open]
```

The broader social meaning is that public measurement can improve visibility
without closing the practical access gap. A state or county estimate can show
where reach appears unequal, but it does not explain whether the reason is
transportation, clinic capacity, paperwork, stigma, program rules, linkage
error, or household choice.

## What this adds to the broader atlas

This adds a measurement-and-reach version of the atlas's formal-availability
versus usable-protection pattern. It also provides a useful counterexample to
false precision: two official estimates can be statistically reliable while
answering different questions because their denominators and methods differ.

## Limits and counterexamples

- The source is a working paper, not a final reviewed Census publication.
- The public abstract does not provide the numeric state, county, or subgroup
  access rates.
- Estimated eligibility and access are not application completion, benefit
  adequacy, food security, or child health.
- Census and USDA/FNS estimates should not be pooled without aligning their
  definitions and measurement scope.
- Lower measured access can reflect true nonparticipation, route burden,
  program rules, clinic capacity, or linkage and coverage error.

## Next decisive test

The next useful artifact is a protected eligible-person-to-program ledger
joining eligibility, outreach, application, clinic or agency route, approval,
benefit amount, timing, shopping, food security, and maternal or child health.
That would turn a reach estimate into an observable practical-access chain.

## Source

- [Census CES Working Paper: WIC Access and Meaning](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-44.html)
- [Census research profile](https://lehd.ces.census.gov/applications/creat/paper-profile/1433)
- [Machine-readable trend record](../../../records/us-census-wic-access-measurement-2026.json)

**Evidence status:** the official Census working paper documents a linked-data
estimation system for WIC eligibility and access across places and groups;
numeric subgroup reach, route barriers, adequacy, and health outcomes remain
open.
