# WBNS public-use route acquisition audit v1

**Checked:** 2026-09-16; browser-capable ICPSR metadata, Urban catalog, and access guidance rechecked during continuation pass
**Status:** public-use acquisition identified and metadata independently verified; data-file access still requires an authenticated free account; no new estimates promoted yet  
**Purpose:** prepare a reproducible 2024 WBNS extraction that joins lived SNAP route experience to food, housing, work, health, and financial-security measures.

## Access finding

The 2024 WBNS round is catalogued by ICPSR as **Well-Being and Basic Needs Survey, United States, 2024 (ICPSR 39691)**. The catalog identifies an individual-level, cross-sectional survey of the household population ages 18–64, collected in December 2024, with an approximately 7,500-person stratified KnowledgePanel sample and post-stratification weights. The catalog states that public-use files are available to the general public without ICPSR-member affiliation; restricted variables are separate.

The latest direct transport recheck is preserved in the [machine-readable
access record](data/wbns-access-recheck-2026-09-15.json). Unauthenticated
requests to the official ICPSR study/version routes and the Urban Data Catalog
returned HTTP 403 HTML challenge pages. This is a session transport result,
not evidence that the public-use files or route fields are absent.

The current pass verified the catalog metadata through the ICPSR study page and
downloaded the official 2024 questionnaire. The catalog identifies the study as
version 1, released June 4, 2026, collected in December 2024, with an
approximately 7,500-person stratified KnowledgePanel sample, an individual unit
of observation, a household-population age 18–64 universe, a cross-sectional
design, and weights post-stratified to age/gender, race/ethnicity, education,
children, region, metro status, homeownership, family income/FPL, family
composition, language, and internet access. It did **not** download or analyze
the microdata, so this packet remains an acquisition control record, not a trend
estimate.

## Transport recheck

Two public-facing routes were tested during the continuation pass:

| Route | Result | Interpretation |
|---|---|---|
| ICPSR 39691 study/data-documentation endpoints | HTTP 403 Cloudflare challenge from the current non-browser session | Transport failure in this environment; not evidence that the public-use files do not exist |
| Urban Data Catalog WBNS page | HTTP 403 Cloudflare challenge from the current non-browser session | Catalog metadata is independently discoverable through indexed search, but attachments were not treated as downloaded |

The [ICPSR metadata documentation](https://icpsr.github.io/metadata/icpsr_metadata_api/) says the catalog tracks public-use versus restricted access at the system level, and the [39691 study page](https://www.icpsr.umich.edu/web/HMCA/studies/39691) states that public-use files are available to the general public. The page also says the collection is distributed as survey data with online analysis metadata and a roughly 3–4% cumulative response rate. The local acquisition state therefore remains **identified and metadata-verified but not retrieved**. An account/browser-capable file retrieval or a supplied package is still required before the validator can run.

The current ICPSR series page lists the 2024 study as **partially restricted**,
while HMCA access guidance says data-file access requires a free
Researcher Passport/login even when documentation is viewable without login.
Therefore “public-use available” is retained as a catalog metadata claim, not
as proof that this environment can download every file or that all fields
needed for the route ledger are public. The unauthenticated study endpoint was
retested during this pass and returned HTTP 403.

The Urban Data Catalog was rechecked on 2026-09-14. It currently exposes
published WBNS tables through 2025—including material hardship and unmet
personal-assistance tables modified August 20, 2026—but it does not expose the
2024 respondent-level route file needed for `Q53A`/`Q110`/`Q54` episode
extraction. Those published tables can extend descriptive context, but they
cannot substitute for the route microdata or create the missing notice,
effort, amount, remedy, and follow-up linkage.

## Browser-capable metadata and access recheck

The official [ICPSR 39691 study page](https://www.icpsr.umich.edu/web/HMCA/studies/39691)
was rechecked through a browser-capable source on 2026-09-14. It confirms the
2024 version date of June 4, 2026; December 2024 collection; an approximately
7,500-person stratified KnowledgePanel draw of adults ages 18–64; individual
observation; a cross-sectional design; Census-region geographic scope; and
post-stratification benchmarks including age/gender, race/ethnicity, education,
children, region, metro status, homeownership, income/FPL, family composition,
language, and internet access by age. The page also confirms the broad topic
coverage needed for the planned route ledger: safety-net participation, food,
housing, employment, income, financial security, disability, health, and
discrimination.

The official [HMCA access guidance](https://www.icpsr.umich.edu/sites/hmca/find-data)
states that data-file access requires login with a free ICPSR Researcher
Passport or an existing Google, LinkedIn, or ORCID account, while
documentation does not require login. This resolves an ambiguity in the older
“public-use available” wording: the file is catalogued for general public
access, but the current workspace has no authenticated download session. The
recheck therefore strengthens the acquisition specification without changing
the evidence state: no respondent-level route fields, weights, or estimates
have been retrieved here.

The official study page also exposes an **Analyze Online (SDA)** surface, and
the WBNS series catalog currently lists 8 studies and 5,220 indexed variables.
This is a useful intermediate route, but the official ICPSR online-analysis
guidance also requires login and terms-of-use acceptance. It therefore lowers
the software/download burden without removing the authentication gate. No
SDA crosstab or frequency has been retrieved in this workspace. Once an
authenticated route is available, inspect question wording, universe, weights,
cell-size suppression, variance support, and whether the 2024
`Q53A`/`Q110`/`Q54` fields are actually available. Until then, the evidence
state remains metadata-verified and respondent-file/not-online-output not
retrieved.

The catalog metadata used for this gate is preserved in the
[machine-readable WBNS 39691 record](data/wbns-39691-catalog-metadata-v1.json).
It fixes the study identity, version date, collection month, individual unit,
18–64 universe, approximate sample, post-stratification benchmarks, response
rate note, and route fields that still require file-level verification. The
record intentionally does not promote the catalog's availability labels into
a successful local download or an estimate.

## Current-vintage universe boundary

The current [Urban WBNS project description](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey)
states that the 2017–2024 rounds sampled more than 7,500 adults ages 18–64
per round, while the 2025 round expanded the sample to approximately 2,500
adults age 65 and older. The [Urban Data Catalog](https://datacatalog.urban.org/dataset/well-being-and-basic-needs-survey)
also exposes published WBNS tables through 2025, including 2025 material-
hardship and unmet-personal-assistance tables. These are useful current context
but do not establish that a 2025 respondent-level route file, identical
question universe, or comparable weight is available.

The age-frame expansion is now a mandatory harmonization control: do not pool
2025 with 2017–2024 or describe a change as a time trend until age eligibility,
sampling frame, route-field availability, weights, and question wording are
verified. For the immediate route-ledger gate, the 2024 ICPSR 39691 file
remains the primary target and its 18–64 universe remains separate from the
2025 expansion.

ICPSR's public study search also exposes an **online-analysis** filter and
indexes variable-level documentation across its holdings. The search result
confirms that WBNS 2024 is classified in that online-analysis surface, but it
does not by itself expose the route-variable labels, code values, weights, or
usable output. The next reproducible check is therefore an authenticated
variable/codebook inspection, not a claim that the search index supplies the
data needed for estimation.

An exact-label search for the mapped fields `Q53A`, `Q110A`, and `Q54R` did not
return public indexed results in the current pass, and the direct ICPSR
variable-search endpoint returned HTTP 403. This does not show that the fields
are absent from the study; it establishes only that the public search surface
did not make their codebook details verifiable here.

## Route variables identified in the questionnaire

| Variable | Field | Role in the end-to-end ledger |
|---|---|---|
| `Q53A` | Family received SNAP in the past 12 months | Program-exposure universe |
| `Q110` | Family had to recertify SNAP in the past 12 months | Episode eligibility for recertification route |
| `Q110A` | How difficult/easy recertification was | Perceived route burden |
| `Q110B` | Preferred communication channel with SNAP staff | Channel preference and possible mismatch |
| `Q110C` | Who helped complete application/recertification | Assistance route |
| `Q54` | Benefits stopped or interrupted, even for a month | Interruption event |
| `Q54N` | Whether the interruption was chosen | Voluntary/involuntary distinction |
| `Q54O` | How the respondent learned of interruption | Notice, EBT, balance-check, or other discovery route |
| `Q54P` | Why benefits stopped/interrupted | Eligibility, recertification, or other route |
| `Q54Q` | Reasons told no longer eligible | Earnings/assets, work requirement, reporting, immigration, household change |
| `Q54R` | Reasons unable to recertify on time | Notice receipt, time, knowledge, paperwork, interview, lost documents, other |

The 2024 questionnaire also contains food, housing, transportation, utility, health, employment, financial-security, discrimination, and help-seeking fields. Those domains can support the material-outcome and meaning/action portions of the ledger, subject to their own universes and timing. No respondent-level estimate is promoted from the 2026-09-15 recheck.

## Planned extraction contract

The first extraction should produce four separate tables or clearly separated outputs:

1. **Route exposure:** `Q53A`, `Q110`, `Q110A`, `Q110B`, `Q110C`.
2. **Interruption and discovery:** `Q54`, `Q54N`, `Q54O`.
3. **Reported route reasons:** `Q54P`, `Q54Q`, `Q54R`, preserving multi-response indicators.
4. **Material and meaning cross-tabs:** route/interruption cells crossed with pre-specified food, housing, utility, work, health, financial-security, perceived-fairness, and assistance measures where the 2024 public-use file exposes them.

Every output must retain the survey weight, unweighted records, missing/refused codes, item-specific universe, question wording, response options, and whether a field is retrospective or current. No route reason should be interpreted as agency fault without corroborating administrative evidence.

## Go/no-go gates

- **Go:** public-use file and codebook are downloaded, hashes recorded, and all route variables map to documented fields.
- **Go with bounds:** a field is available but its material outcome is cross-sectional or retrospectively timed; report it as association, not episode causality.
- **Hold:** a variable is restricted, missing from the public-use file, or its universe cannot be reconstructed.
- **Do not pool:** 2024 WBNS with the Urban brief’s published estimates unless the exact sample, weights, item wording, and universe are aligned. The brief and the public-use file are source-linked but are not automatically identical analytic products.

## Open acquisition gap

The missing step is a reproducible public-use download and codebook-backed analysis. Once obtained, the highest-value test is whether reported interruption and route barriers differ by work, children, income-to-poverty, race/ethnicity, language, disability, housing, food insecurity, and financial buffer—while preserving the cross-sectional and retrospective limits. This would materially strengthen the route → material security and unequal-exposure arrows without claiming same-person causality over time.

### Earlier-wave fallback check

The 2023 round (ICPSR 39462) was checked as a possible earlier time point.
Its official catalog describes the same individual, cross-sectional, US adults
18–64 design, approximately 7,500-person KnowledgePanel sample, post-
stratification weights, and the relevant food, housing, employment, program,
financial-security, and disability domains. It also states that public-use
files exist, while separately noting restricted files. The ICPSR HMCA access
guidance and the study's SDA route still require an authenticated free account,
so no 2023 file or estimate is promoted here. If an authenticated package is
later supplied, 2023 should be used as a distinct cross-sectional comparison,
not merged with 2024 before question wording, weights, sample, and route-field
universes are harmonized.

The first file-level gate is implemented in [`validate_wbns_public_use_route_file.py`](../../../scripts/validate_wbns_public_use_route_file.py). It accepts CSV, SAS, Stata, SPSS, and XPORT files; checks the expected route fields and multi-response prefixes; inventories missingness and raw codes; and refuses promotion when the requested weight column is absent or nonpositive. It is a schema audit, not an estimate.

## Sources and retrieval controls

- [ICPSR 39691 study page](https://www.icpsr.umich.edu/web/HMCA/studies/39691)
- [ICPSR 39462 2023 public-use study](https://www.icpsr.umich.edu/web/HMCA/studies/39462)
- [Urban 2024 WBNS questionnaire](https://www.urban.org/sites/default/files/2025-08/WBNS_2024_questionnaire.pdf)
- [Urban WBNS Data Catalog](https://datacatalog.urban.org/dataset/well-being-and-basic-needs-survey)
- [WBNS project page](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey)
- [HMCA WBNS series catalog](https://www.icpsr.umich.edu/sites/hmca/view/collections/1861)
- [HMCA find-data access guidance](https://www.icpsr.umich.edu/sites/hmca/find-data)
- [WBNS series catalog and online variable index](https://www.icpsr.umich.edu/sites/hmca/view/collections/1861)
- [ICPSR online-analysis guidance](https://www.icpsr.umich.edu/sites/nahdap/find-access-data/online-analysis)
- [ICPSR HMCA studies with online analysis](https://www.icpsr.umich.edu/web/HMCA/search/studies?FORMAT_FACET=Online+analysis)

Local retrieval checks for this pass:

- questionnaire SHA-256: `sha256:85ba1003337b3c56451b2c53d9bd6b706cc4d6a1b51516378ff65c672e55be55`
- catalog response SHA-256: `sha256:2baa7fc720f4ad99d66df0026348506b1e69f0a0e411535fba13db5735d7dedd`
