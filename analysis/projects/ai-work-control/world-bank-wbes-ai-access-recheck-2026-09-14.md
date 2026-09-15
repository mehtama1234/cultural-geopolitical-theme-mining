# World Bank Enterprise Surveys AI follow-up access recheck

**Checked:** 2026-09-14  
**Status:** metadata and catalog reverified; firm microdata still not retrieved

## What changed in the source check

The current World Bank Enterprise Surveys data-updates page now carries a July
2026 update and continues to identify the May 2026 release of eight AI
follow-up surveys, including the United States. The current page directs users
to the authenticated Enterprise Surveys data portal for datasets and
documentation. The World Development Report 2026 reproducibility catalog is
reachable and still describes the separate AI replication package; it does not
make the Enterprise Survey firm microdata downloadable without the portal
access route.

| Artifact | Retrieval result | SHA-256 |
|---|---|---|
| WBES data-updates page | HTTP 200; July 2026 page; May 2026 entry names the US AI follow-up | `f3f2c7eb463db4e1006f27838e8b879d6ce0a2cd1d0a21105f4c062d183e604b` |
| WDR 2026 reproducibility catalog 624 | HTTP 200; package metadata and data inventory reachable | `f8f5ec12afad9b778fc038f7f84daf57edfae977086d683ec7e988a592c9faf0` |
| Enterprise Surveys `DataDetails.xls` | HTTP 200; dataset-list workbook retrieved, but no authenticated US AI microdata package | `2b88ef960078381b9ecdc439bd57a5f1c1e06da81cb9caac21f16b9cfca343c3` |
| Enterprise Surveys data portal | Sign-in route reachable; authentication still required | not treated as data |

The current unauthenticated probe of the sign-in route returned HTTP 200 after
redirecting to `https://login.enterprisesurveys.org/en/signin`. This confirms
that the access surface is reachable, not that an account can enter or that a
United States AI follow-up file can be downloaded.

The catalog and update page are source-existence and access evidence only. No
AI adoption, employment, sales, productivity, training, or firm-complement
estimate is promoted from them.

## Public indicators versus firm-level files

The current official [WBES FAQ](https://www.enterprisesurveys.org/en/about-us/frequently-asked-questions)
clarifies that registered users can download the raw data and the corresponding
survey questionnaire from the data portal. Its indicator documentation says
that public website indicators are aggregated across firms using the survey
weight `w_median`; these indicators are not equivalent to the respondent-level
AI follow-up file, and the public page does not by itself supply the AI
questionnaire, skip patterns, firm-level missingness, or the complete variance
instructions needed for the planned extraction.

The public indicator layer is real and useful, but it is not yet the AI bridge:
the current custom-query interface explicitly supports economy/subnational
indicators with subgroup standard errors and observation counts, while the
published indicator catalogue exposes the established formal-survey topics
(including jobs, performance, infrastructure, and technology). The current
public topic/economy surface does not expose the newly released AI follow-up
question set as a separately documented indicator family. Therefore it can
support a bounded baseline/context layer, but not an AI-adoption estimate from
the follow-up.

This sharpens the gate: a public indicator export could support a bounded
economy-level descriptive comparison only if it exposes the AI follow-up
variables, definitions, standard errors, and observation counts. It cannot
substitute for the registered microdata when the question requires firm size,
sector, ownership, finance, infrastructure, training, or joint outcome cells.
The future pass must record whether an AI indicator is an official weighted
aggregate or a microdata estimate and must not combine the two without a
documented common universe.

## Reproduction routes

- [WBES data updates](https://www.enterprisesurveys.org/en/data/data-updates)
- [WBES public indicator/custom-query layer](https://www.enterprisesurveys.org/en/data/custom-query)
- [WBES indicator definitions](https://www.enterprisesurveys.org/content/dam/enterprisesurveys/documents/methodology/Indicator-Description.pdf)
- [WBES FAQ: raw data, questionnaires, and indicator construction](https://www.enterprisesurveys.org/en/about-us/frequently-asked-questions)
- [World Bank WDR 2026 reproducibility catalog 624](https://reproducibility.worldbank.org/catalog/624)
- [WBES data portal](https://login.enterprisesurveys.org/content/sites/financeandprivatesector/en/signin.html)
- [Existing AI follow-up source record](world-bank-wbes-ai-followup-source-record-v1.md)

## Next gate

An authenticated user must download the United States AI follow-up file,
questionnaire, sampling documentation, weights, and variance guidance. The
first local action after receipt remains a file-level schema and codebook
audit. Until that gate passes, the atlas retains only the source-existence and
access boundary and does not infer a firm result from the report narrative.
