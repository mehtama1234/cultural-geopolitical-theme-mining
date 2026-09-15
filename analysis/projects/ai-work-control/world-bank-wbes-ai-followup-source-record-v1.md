# World Bank Enterprise Surveys AI follow-up source record v1

**Checked:** 2026-09-14  
**Status:** acquisition gate rechecked; no estimate promoted  
**Project:** AI, work, and control

## Why this source matters

The World Bank Enterprise Surveys team released 2026 AI-focused follow-up
surveys for the United States, India, Jordan, Kenya, Malaysia, Mexico, Nigeria,
Thailand, and Türkiye. The surveys are designed to capture the impact and
adjustments that AI has brought to private-sector firms. This is the missing
firm-level bridge between the current macro/industry sources and worker,
household, and place outcomes.

The source could test:

- whether adoption differs by firm size, sector, ownership, and country;
- whether firms report productivity, employment, sales, cost, or task changes;
- which firms face finance, infrastructure, skills, data, or management
  constraints;
- whether training, digital infrastructure, and complementary investment
  distinguish adoption from productive use;
- whether US firms show a different adjustment pattern from developing-country
  firms;
- whether firm-reported changes align with worker-reported and industry-account
  evidence already in the atlas.

## Current authoritative source state

The [World Bank data update](https://www.enterprisesurveys.org/en/data/data-updates)
states that eight AI follow-up surveys were released in May 2026. The [World
Bank Enterprise Surveys home page](https://www.enterprisesurveys.org/en/enterprisesurveys)
describes the surveys as nationally representative firm-level data collected
from business owners and top managers. The [WDR 2026 reproducibility package](https://reproducibility.worldbank.org/catalog/624)
identifies the files, including:

```text
United States-2026-AI follow-up data.dta
India-2026-AI follow-up data.dta
Jordan-2026-AI follow-up data.dta
Kenya-2026-AI follow-up data.dta
Malaysia-2026-AI follow-up data.dta
Mexico-2026-AI follow-up data.dta
Nigeria-2026-AI follow-up data.dta
Thailand-2026-AI follow-up data.dta
Turkiye-2026-AI follow-up data.dta
New_Comprehensive_June_4_2026.dta
```

The package metadata says the firm microdata are not redistributed in the
reproducibility package and require access through the [Enterprise Surveys
portal](https://login.enterprisesurveys.org/en/signin). The full WDR package
is listed as a 976.79 MB ZIP. An attempted selective HTTP range retrieval of
the package returned a server-side 500 response, so no partial file is treated
as data and no WBES estimate is invented from the report narrative.

The [2026-09-14 access recheck](world-bank-wbes-ai-access-recheck-2026-09-14.md)
also re-fetched the WBES update page, the WDR catalog, and the public dataset
list workbook. The metadata routes returned HTTP 200 and still confirmed the US
AI follow-up, while the data portal continued to require authentication. This
recheck changes the access evidence, not the estimate state.

## Extraction specification once access is available

1. Authenticate and obtain the US AI follow-up file plus questionnaire,
   sampling documentation, weights, strata, PSU/variance guidance, and the
   comparable economy files.
2. Audit variable labels, missing codes, skip patterns, firm universe, survey
   field dates, size classes, sector definitions, ownership fields, and the
   availability of replicate or Taylor-linearization variance information.
3. Identify AI measures separately for any use, business-function use,
   frequency, organizational integration, task substitution, task
   complementarity, and planned adoption.
4. Preserve firm weights and calculate estimates with the survey design;
   never pool countries or firm sizes before checking comparability.
5. Extract outcomes for employment, sales, productivity, costs, wages or
   training, investment, finance, infrastructure, management practice, and
   reported constraints.
6. Compare US firm results with the existing BEA, BIS, NBER, Census, BLS, and
   World Bank framework evidence by unit and period.
7. Promote only estimates with a denominator, uncertainty method, subgroup,
   counterinterpretation, and source artifact hash into the trend registry.

## Open boundary

The public release announcement establishes that the surveys exist and what
they are intended to measure. It does not establish any adoption rate,
productivity effect, employment effect, distributional result, or US-country
comparison. Those remain acquisition and analysis targets. The dataset is
especially valuable because it can test the current hypothesis that AI gains
are conditional on firm complements and are distributed unevenly, but the
hypothesis must not be promoted until the microdata and survey design are
audited.
