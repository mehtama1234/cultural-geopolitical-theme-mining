# Material, time, and care linkage acquisition plan v1

**Checked:** 2026-09-13
**Scope:** US societal trend program; material pressure, time transfer, care,
recovery, and meaning  
**Status:** acquisition and identification plan; no end-to-end result claimed

## Why this pass exists

The program already measures several population-level pieces:

```text
financial pressure / care concern
  -> substitution, reduced use, borrowing, saving cuts, or extra work
work, care, travel, paperwork, and social time
  -> security, health, trust, civic availability, or exit
```

Those pieces come from different source populations and are not silently the
same people. The next pass needs a design that holds a person or household
constant long enough to establish time order and measure alternatives.

## Required minimum record

An acceptable candidate must provide, for the same unit and a defined follow-up
window:

| Stage | Required fields | Current local coverage |
|---|---|---|
| Trigger | dated bill, price, care need, work-rule change, or financial shock | SHED has pressure and care measures; exact dated trigger is missing |
| Alternatives | cash/savings, family help, provider or job alternatives, transport, schedule control | SIPP and SHED provide partial resource context; practical alternatives are missing |
| Immediate response | purchase change, delay, borrowing, extra work, paid/unpaid care, travel, waiting, paperwork | SHED covers several money responses; ATUS covers time allocation; no same-unit join |
| Control | who could refuse, switch, appeal, change schedule, or obtain help | Existing sources identify some institutional stages; individual control is mostly open |
| Protected/sacrificed outcome | food, housing, health, rest, family time, social connection, civic availability, or work | Separate sources measure these outcomes; protected-versus-sacrificed pairing is open |
| Later outcome | recovery, persistence, debt, health, work, trust, action, or exit at 1/6/12 months | SHED panel measures selected persistence/reversal; time, meaning, and action follow-up are missing |
| Interpretation | attribution, fairness, dignity, belonging, legitimacy, and perceived efficacy | ANES/Pew and project-specific layers measure population meaning; same-event attribution is open |

## Existing-source fit test

| Source family | Same-unit strength | What it can deepen | What it cannot establish alone | Decision |
|---|---|---|---|---|
| SHED 2024–2025 panel | Repeated respondent; selected repeated variables | Financial-condition path, adaptation persistence, re-entry, and reversal | Exact event date, hours displaced, care recipient outcome, trust/action after the event | Use for recovery and counterexample cells |
| SHED annual care/health layers | Broad weighted adult samples | Care concern, health, unpaid care, and money adaptations across subgroups and years | Same respondent across years; causal event or time diary | Use for distribution, not linkage |
| ATUS 2024 and ATUS-CPS-linked fields | Person diary with work, care, household, and social-time measures | Time allocation, work location, schedule-related contrasts, and social availability | The price/bill/care event that produced the diary; later recovery or political meaning | Use for time measurement and subgroup design |
| SIPP monthly layers | Person/household month and transitions | Resources, work, benefit entry/exit, and recorded transition context | Detailed minutes, waiting, unpaid care, dignity, attribution, and civic response | Use for event timing and material context |
| NHTS/local-capacity layers | Trip/place or county comparison | Reachability, travel, vehicle access, and supply/replaceability context | Same household's service failure, care need, price response, or meaning | Use as matched-place conditioning |

The immediate conclusion is an acquisition gap, not a null result: the current
bundle can triangulate the societal pattern and identify plausible moderators,
but it does not contain every required field in one same-unit design.

## Source check completed

An official-source check identifies the [Panel Study of Income Dynamics
(PSID)](https://psidonline.isr.umich.edu/GettingStarted.aspx) as the highest-
priority candidate for the economic, employment, health, and family backbone.
Its detailed time-use material is supplemental rather than a repeated,
all-adult diary: the PSID documentation lists the Disability and Use of Time
study for older couples in 2009 and 2013, and child time-diary supplements in
selected waves ([PSID documentation index](https://psidonline.isr.umich.edu/Guide/documents.aspx)).
PSID is therefore a strong modular backbone for material
pressure, work, health, and family structure, but it is not yet accepted as
the complete time/care panel.

The [BLS ATUS 2024 files](https://www.bls.gov/tus/data/datafiles-2024.htm)
confirm that ATUS-CPS supplies household-member information collected before
the diary interview and that the activity, who, and eldercare files can be
used for detailed time and care measurement. The [Census SIPP
documentation](https://www.census.gov/programs-surveys/sipp.html) confirms
longitudinal monthly income, employment, household, health-insurance, child-
care, and food-security content. These are acquisition findings, not evidence
that the sources can be joined to one another.

The PSID candidate is now **documented as a viable modular backbone after the
2023 field audit**, while the estimate-level acquisition gate remains open.
The official 2023 Family File confirms the planned work, housework, care,
time-pressure, health, income, wealth, home-insurance, and utility fields, but
the codebook also confirms routing, imputation, and family/person-unit
boundaries. Before acquisition, verify whether the selected main-study waves
and supplements contain: a dated enough financial or care trigger;
repeated time-use and unpaid-care measures for the same adults; work
schedule/control; health and material outcomes; and direct trust, meaning, or
civic-action measures. The current documentation already indicates that the
general all-adult repeated-time requirement may fail. If it does, pair PSID
economic/family waves with the appropriate time/care supplement or an event
ledger, and keep the full end-to-end claim open.

The file-structure audit makes the usable architecture clearer. PSID's
documentation describes single-year family files through 2023 and a cross-year
individual file; the 2023 guide reports 9,152 families in the 2023 family file
and 85,536 persons in the cross-year individual file. The documented family
interview sequence is biennial from 1999 through 2023, with earlier annual
waves. This is substantial longitudinal population infrastructure, but
individual availability varies with family membership and nonresponse.

The packaged-data page exposes the 2019, 2021, and 2023 main Family Files and
a 1968–2023 Cross-year Individual File, plus CDS files through 2024, TAS
through 2023, and DUST for 2009 and 2013. The public ZIP route requires a
registered PSID account and acceptance of the site's conditions of use. The
cross-year individual package can cover the person-level side of the
2019/2021/2023 structural gate; wave-specific family packages remain required
for family-level resources, expenditure, composition, and weights. Until that
account step is completed, the next safe action is documentation and
variable-search work; no local PSID data extract is claimed.

The detailed diary supplements must remain separate in the design. The PSID
index lists child time diaries for 1997, 2002, and 2007, later child/adolescent
supplements, and the Disability and Use of Time study for older couples in
2009 and 2013. These can provide deep time/care observations for defined
subpopulations and periods; they do not create a repeated all-adult diary for
every main-study family. However, the 2019, 2021, and 2023 main questionnaires
also contain repeated stylized time and care measures for Reference Persons
and Spouse-Partners. The distinction is detailed diary versus repeated
typical-week measures, not time-use versus no time-use.

The resource side is now bounded more precisely. The 2019, 2021, and 2023
Family File codebooks identify repeated total family money income and
constructed wealth including equity, alongside utility expenditure and home
insurance fields. These measures supply a family-level resource and fixed-cost
context for the time/care comparison. They are not liquid cash, available
buffer, or proof that a family made a particular choice; the wealth summaries
also require their accuracy flags. Detailed expenditure categories, missing
value treatment, and cross-wave universes remain acquisition checks.

## Main-panel field audit

The 2019, 2021, and 2023 main questionnaires show a promising repeated core:

| Main-panel field | 2023 questionnaire location/measure | Linkage value | Boundary |
|---|---|---|---|
| Employment timing | Section BC records employers and start/end dates, with uncertainty codes for recalled timing | Orders work changes within the two-year interview window | Recall and coarse dates can weaken event timing |
| Paid work and commuting | BC60A typical-week paid hours; commute and work-from-home questions | Measures work-time load and some schedule/location conditions | Does not directly measure schedule control or refusal power |
| Household and care time | F1A–F1G typical-week housework, personal care, shopping, child care, adult care, volunteering, education, and leisure | Directly measures several currencies that can absorb pressure | Stylized respondent reports, not a full diary or complete household time budget |
| Social availability and time pressure | F1H–F1K interaction, physical/mental activity, and feeling rushed outside work | Supplies social/cultural availability and perceived time pressure | Does not identify whether a price, employer, care recipient, or agency caused it |
| Family coordination | F5 family meals; F7 child-care spending and months used | Connects family routine and paid care to household resources | Child-care fields are conditional on child age and household composition |
| Material and health outcomes | Section F expenditures; Section G income/assets; Section H health and change since prior wave | Supports repeated material and health outcomes around work/care conditions | Exact bill, unmet need, remedy, and downstream political meaning remain open |

This changes the source decision. PSID can now support a bounded, many-family
same-unit analysis of **material resources → work/care/time allocation → health,
family, and selected participation outcomes**, using typical-week measures.
It still cannot by itself establish the stronger claim that a specific price or
institutional decision caused a particular sacrifice, restored trust, or
produced political action.

The broader program uses this as one empirical spine among several. The
comparison is intended to show how a condition is distributed across people and
places, how households and workers adapt, and where the burden or control moves
next—to unpaid care, extra work, reduced consumption, firm/customer relations,
public systems, cultural meaning, or political action. PSID can deepen the
resource-to-time-to-wellbeing segment across many families; it cannot by itself
close the institutional, cultural, or political arrows.

**Current acquisition decision:** acquire the 2019, 2021, and 2023 main family
and individual files when account access is available, then test the repeated
F1/BC/H field overlap, valid sample retention, weights, and missingness. Treat
DUST/CDS/TAS as targeted supplements. Describe the main-panel design as a
repeated typical-week material/time/care panel only after the extract verifies
the wave-level overlap; do not call it a detailed time diary or a direct
political-meaning panel.

The planned first extract is specified in the [PSID material/time/care extract
specification](psid-material-time-care-extract-spec-v1.md). It fixes the unit,
candidate fields, comparison cells, arrow statuses, and quality gates before
data access is available.

The first executable post-download step is the [PSID wave-file audit
protocol](psid-wave-file-audit-protocol-v1.md), which checks the three target
wave files against the mapped variable surface and explicit merge keys. A
passing structural audit is a readiness signal only; it does not waive the
universe, missingness, retention, weighting, or comparability gates.

## Current access gate verification

The official [PSID packaged-data page](https://simba.isr.umich.edu/Zips/ZipMain.aspx)
currently lists the 2019, 2021, and 2023 main Family Files and the 1968–2023
Cross-year Individual File. Attempting the 2023 packaged download without an
authenticated session redirects to the official [ZIP download warning](https://simba.isr.umich.edu/Zips/ZipWarnAccess.aspx),
which states that an account must accept the Conditions of Use before generated
data carts or ZIP data can be downloaded. The [PSID getting-started page](https://psidonline.isr.umich.edu/GettingStarted.aspx)
also says that public-use data are free to researchers who register and accept
those conditions.

This is an access prerequisite, not an analytical result. No PSID microdata
are present in the workspace as of this check. The field manifest, codebook
audit, and extract specification therefore remain pre-acquisition assets; no
many-family estimate should be published until the files are obtained and the
wave-level retention, universe, missingness, and weight checks are run.

## Priority acquisition routes

1. **Longitudinal household route:** audit PSID's main waves and supplements
   first, then identify a panel with repeated financial,
   work, care, health, time, and subjective/political measures. Verify the
   variable dictionary and timing before downloading or linking records.
2. **Event-ledger route:** collect dated administrative, consumer, employer,
   or service events and pair them with a consented person/household diary at
   baseline and follow-up. This is the strongest route for alternatives,
   control, interpretation, and remedy, but requires privacy, consent, and
   retention controls.
3. **Modular bounded route:** use SHED panel for financial persistence, an
   ATUS/CPS-compatible time module for work and care, and SIPP for monthly
   resources. Report this as three complementary estimates unless identifiers
   and design actually permit a valid join.

## Go/no-go rules

Promote a material/time/care arrow only if the candidate has:

- a stable person, household, case, or valid matched-place unit;
- an observed or reliably dated trigger and a post-trigger measurement;
- explicit alternatives and at least one control variable;
- separate paid time, unpaid time, money, and outcome fields;
- a comparison or counterexample with similar exposure and different room;
- denominator, missingness, attrition, weight, and uncertainty documentation;
- a defined recovery window; and
- direct meaning/action measures, or an explicit statement that that arrow
  remains open.

If any of these fail, retain the output as reported, estimated, compared, or
open. Do not rename a cross-source alignment as a same-household causal result.

## Connection to the broader program

This pass is one lane in the 14-theme program. Its endpoint is not “what one
household did.” The purpose is to learn, across many units and institutions,
how material conditions reorganize time and care, how the burden is distributed,
and when those experiences become trust, cultural meaning, collective action,
consumer exit, firm response, or political demand.

Related: the [broad end-to-end event ledger](../../templates/US-BROAD-EVENT-LEDGER_V1.md),
the [time/work/care/social participation layer](time-work-care-social-participation-layer-v1.md),
the [price-pressure/time-transfer bridge](price-pressure-time-social-participation-cross-source-bridge-v1.md),
and the [next-pass queue](../../US-BROAD-NEXT-PASS-QUEUE_V1.md).
