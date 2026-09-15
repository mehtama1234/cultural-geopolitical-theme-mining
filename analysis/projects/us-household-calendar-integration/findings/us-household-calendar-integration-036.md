# PSID 2023 can support the material/time/care backbone, but not the whole causal chain

**Status:** source and field-audit finding · **Checked:** 2026-09-14

## The finding

The official 2023 PSID documentation confirms that the proposed material,
work, time, care, health, and household-room backbone is real and unusually
rich. The 2023 Family File contains 9,152 records and 3,812 variables. Its
codebook identifies typical-week paid-work hours, housework, personal care,
shopping, child-care, perceived time pressure, health level/change, income,
wealth, home insurance, and utility expenditure fields.

That makes PSID a credible next acquisition for the atlas’s material/time/care
lane. It does not make PSID an already-completed end-to-end result. The fields
are collected on different units and recall frames, use routing and
not-applicable codes, and include imputed material measures. The main interview
also lacks a general repeated 24-hour diary and does not by itself supply a
dated price/bill event, institutional actor, attribution, trust change, or
political action.

The cross-wave codebook check confirms the planned conceptual mapping for
typical-week paid work, Reference Person housework, and outside-work time
pressure across all three waves. The displayed family-file bases differ—9,569
in 2019, 9,207 in 2021, and 9,152 in 2023—so the mapping is a comparability
lead, not evidence of a retained panel or equal denominator.

The official packaged-data route lists the needed 2019, 2021, and 2023 files,
but download requires a registered account and acceptance of the Conditions of
Use. The workspace has not obtained the microdata, so this page is a field and
acquisition audit—not a PSID estimate.

```text
material room / work / care / health fields  [documented in same panel]
  -> valid person-family merge and wave retention [still to audit]
  -> repeated distribution and change             [extract not yet run]
  -> dated trigger / attribution                  [not supplied by core fields]
  -> meaning, trust, action, or recovery           [additional design needed]
```

## What the documentation establishes

| Layer | Verified evidence | Boundary |
|---|---|---|
| File scale | 2023 Family File: 9,152 records and 3,812 variables | File size is not an analytic sample after eligibility, merge, missingness, and weights |
| Paid work | ER82434 measures Reference Person typical-week hours worked for pay | Typical-week recall is not a time diary or a dated employer event |
| Unpaid/time surface | ER82788–ER82792 cover housework, personal care, shopping, and child care; ER82800 measures feeling rushed/pressed for time | These are different activities and response types; do not collapse them into one time-poverty score without testing |
| Health | ER84520 and ER84521 measure general health and change versus two years earlier | Health change is not automatically caused by material or care change |
| Material room | ER85629 income, ER85692 constructed wealth including equity, ER85710 home insurance, and ER85712 utilities are documented | Imputation, generated measures, and expenditure missingness must remain visible |
| Longitudinal structure | PSID follows sample members across family units and documents annual identifiers for merges | Retention, family-unit change, and cross-wave comparability still require an executed audit |
| Cross-wave field map | BC60A, F1A, and F1K retain the planned concepts in 2019, 2021, and 2023 with wave-specific identifiers | Same labels do not prove same universe, retained cases, weights, or equal measurement error |

## Why it matters for the end-to-end program

This closes an acquisition question but opens the correct analysis work. The
atlas can now move from “PSID might contain the fields” to a field-level audit
with a reproducible merge plan. The first substantive release should compare
valid person/family cells across 2019, 2021, and 2023, preserve sample weights,
report attrition and missingness, and show whether work, care, perceived time,
health, and material-room measures move together or diverge.

The result would still be a bounded longitudinal distribution. To make an
end-to-end cultural or political claim, the program needs a dated trigger or
respondent attribution and a follow-up measure of recovery, trust, action, or
exit. PSID’s richness improves the conditioning and counterexample surfaces;
it does not license causal storytelling by itself.

## Counterinterpretations kept visible

- A documented field may be unusable in a cross-wave extract after routing,
  universe, or retention checks.
- The 9,152 family-file records are not the denominator for every person-level
  measure or every longitudinal comparison.
- Imputed wealth and expenditure values can support defined descriptive uses,
  but should not be read as observed cash or payment records without an
  imputation audit.
- Typical-week reports can reveal allocation categories and perceived pressure,
  but cannot reconstruct a full day or identify waiting and sequencing.
- Material/time change may reflect health, family composition, work selection,
  or unobserved shocks rather than a single price, rule, or institution.

## Next decisive acquisition

Download or generate the public 2019, 2021, and 2023 family/individual files;
run the existing wave-file audit; verify the field map against each released
codebook; construct person-wave and family-wave denominators; retain weights,
mode, family-unit status, and missingness; then publish the first descriptive
cells and an attrition/counterexample table.

## Sources and reproduction

- [PSID 2023 User Guide](https://psidonline.isr.umich.edu/data/Documentation/UserGuide2023.pdf)
- [PSID 2019 Family File codebook](https://psidonline.isr.umich.edu/documents/psid/codebook/FAM2019ER_codebook.pdf)
- [PSID 2021 Family File codebook](https://psidonline.isr.umich.edu/documents/psid/codebook/FAM2021ER_codebook.pdf)
- [PSID 2023 Family File codebook](https://psidonline.isr.umich.edu/documents/psid/codebook/FAM2023ER_codebook.pdf)
- [PSID file-structure documentation](https://psidonline.isr.umich.edu/Guide/FileStructure.pdf)
- Local field-audit note: [PSID 2023 source note](../data/psid-2023-material-time-care-field-audit-source-note.md)
- Related specification: [PSID material/time/care extract specification](../psid-material-time-care-extract-spec-v1.md)

**Evidence status:** field availability and panel structure are documented;
cross-wave estimates, valid merged denominators, dated triggers, causal
attribution, recovery, trust, civic action, and geopolitical consequence remain
open.
