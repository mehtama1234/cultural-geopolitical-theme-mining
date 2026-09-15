# PSID 2023 material/time/care field-audit source note

Sources: [PSID 2023 User Guide](https://psidonline.isr.umich.edu/data/Documentation/UserGuide2023.pdf), [PSID 2019 Family File codebook](https://psidonline.isr.umich.edu/documents/psid/codebook/FAM2019ER_codebook.pdf), [PSID 2021 Family File codebook](https://psidonline.isr.umich.edu/documents/psid/codebook/FAM2021ER_codebook.pdf), [PSID 2023 Family File codebook](https://psidonline.isr.umich.edu/documents/psid/codebook/FAM2023ER_codebook.pdf), and [PSID file-structure documentation](https://psidonline.isr.umich.edu/Guide/FileStructure.pdf).

The official [PSID packaged-data page](https://simba.isr.umich.edu/Zips/ZipMain.aspx)
lists complete main-study waves as ZIP packages containing data, codebooks,
questionnaires, and data-definition programs. The official data page states
that users must register and accept the Conditions of Use before downloading
public-use data; an automated workspace probe was redirected to that warning
and did not obtain a package.

Retrieval: 2026-09-15. The official documents were inspected through their
indexed PDF text. This note records documentation claims and codebook fields;
it is not a data extract or an estimate.

## Verified 2023 file and panel structure

The 2023 User Guide states that the Family Data File has 9,152 records and
3,812 variables, with variable names ER82001–ER85813. The study follows sample
members when they form separate family units and documents family/interview
identifiers needed for longitudinal merges.

## Verified material/time/care fields

The 2023 Family File codebook identifies:

- ER82434, BC60A: typical-week hours spent working for pay by the Reference
  Person; the codebook distinguishes current work, actual hours, 112+ hours,
  don't know, and not applicable/refused.
- ER82788, F1A: Reference Person typical-week housework hours; the question
  covers cooking, cleaning, and other household work and includes routing tied
  to current work and family composition.
- ER82790–ER82792, F1B–F1D: personal care, shopping, and child-care hours.
- ER82800, F1K: frequency of feeling rushed or pressed for time outside work,
  with never/rarely/sometimes/often/almost-always response categories.
- ER84520–ER84521, H1/H1A: general health and whether health is better, the
  same, or worse than two years earlier.
- ER85629 and ER85692: total family money income for 2022 and constructed
  wealth including home equity; wealth variables are imputed/assigned with
  accuracy fields.
- ER85710 and ER85712: home-insurance and total-utility expenditure; the
  codebook identifies generated expenditure variables, imputation/missingness,
  and subcategory fields.

## Cross-wave label check

The official codebooks retain the planned conceptual fields across the three
waves, with wave-specific identifiers:

| Concept | 2019 | 2021 | 2023 |
|---|---|---|---|
| Typical-week paid work | ER72408, BC60A | ER78447, BC60A | ER82434, BC60A |
| Reference Person housework | ER72718, F1A | ER78795, F1A | ER82788, F1A |
| Reference Person personal care | ER72720, F1B | ER78797, F1B | ER82790, F1B |
| Outside-work time pressure | ER72730, F1K | ER78807, F1K | ER82800, F1K |

The 2026-09-15 codebook recheck confirms that the housework and personal-care
fields retain the same Reference Person F1A/F1B concepts and describe typical
weekly hours in all three waves. This is a label-and-wording confirmation
only. It does not establish equal routing, response-code treatment, valid
denominators, imputation handling, or retained three-wave panel overlap.

The codebooks show different family-file bases in their displayed distributions:
9,569 in 2019, 9,207 in 2021, and 9,152 in 2023. These are documentation
and file-base counts, not a retained three-wave person or family panel. Merge,
attrition, routing, and weights still determine the analytic denominator.

## Verified denominator and missingness cautions

The codebook displays the 9,152-record family-file base for many variables but
also records routing, inapplicability, don't-know/refusal, and imputation
categories. Typical-week hours are not a 24-hour diary. Family-file variables
and person-level Reference Person/Spouse variables must not be treated as the
same denominator without a defined merge and eligibility rule.

## Boundary

The documentation establishes that the PSID 2023 family file is a viable
candidate backbone for repeated material, work, time-pressure, health, and
family comparisons. It does not establish cross-wave comparability for every
field, sample retention, weighted estimates, causal triggers, trust/action
outcomes, or an end-to-end household event chain.

The package listing and access requirement establish an acquisition state, not
a substantive finding. No PSID microdata estimate is published from this
documentation audit.
