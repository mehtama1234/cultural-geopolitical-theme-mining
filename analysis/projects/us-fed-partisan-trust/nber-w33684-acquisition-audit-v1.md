# NBER W33684 acquisition audit v1

**Checked:** 2026-09-14  
**Status:** official metadata and indexed full-text claims verified; reproducible full-paper artifact not locally acquired

## Source

- [NBER paper page](https://www.nber.org/papers/w33684)
- [NBER PDF endpoint](https://www.nber.org/system/files/working_papers/w33684/w33684.pdf)
- Title: *Partisan Trust in the Federal Reserve*
- Authors: Carola Binder, Cody Couture, and Abhiprerna Smit
- Working Paper 33684, issue date April 2025

## What is currently verified

The official NBER abstract reports that, in every year from 2001 through 2023,
trust in the Federal Reserve was highest among respondents sharing the
President's party. It reports that these partisan effects were larger than
other demographic differences in trust, but did not explain the large partisan
gap in inflation expectations.

The paper also reports a survey information experiment conducted before and
after the 2025 presidential inauguration. After a Republican President took
office, Republicans still had lower trust in the Fed than Democrats, while
Republicans had lower inflation expectations than Democrats. Open-ended
responses identified tariffs and President Trump as salient explanations for
how consumers thought inflation would evolve.

These are abstract-level findings. They are sufficient to retain the source in
the search and theme layers, but not sufficient to promote paper-specific
sample sizes, estimates, covariates, treatment timing, or subgroup tables into
the machine-readable trend registry.

## Acquisition result

On 2026-09-13, the PDF endpoint returned HTTP 403 to reproducible command-line
requests, including requests with a normal browser user-agent and the NBER
paper-page referrer. The response was an HTML access-denial document rather
than the paper. No paper hash is therefore recorded, and no local PDF is
claimed.

## Alternate-route provenance check

On 2026-09-14, a search result offered an institutional-repository URL that
appeared to be an alternate copy of the paper. Retrieval succeeded, but the
artifact was a different working paper, *The shadow of polarization is long:
trust in the government and independent institutions after 142 government
changes* (IREA Working Paper 2025/11), not *Partisan Trust in the Federal
Reserve*. Its local SHA-256 was
`70cadb38abac833794a142850286a0a1cd2d061969095df677485eb0a7266973`.
It is deliberately not retained as evidence for W33684 and is not used in the
trend registry.

The official NBER PDF is available to browser-indexed search and its indexed
text is consistent with the official abstract: the historical 2001–2023
partisan trust pattern, the 2025 pre/post-inauguration survey, the divergence
between trust and inflation expectations, and the salience of tariffs and the
president in open-ended responses. Indexed text is retained as a discovery
signal only; without a locally hashed, correctly identified artifact, the
paper-specific sample, table, treatment, and subgroup estimates remain below
the promotion threshold.

## Promotion gate

Before creating a paper-specific structured record, acquire the complete PDF or
an official accessible copy and record its SHA-256 hash. Then extract and
verify:

1. historical data source, years, respondent universe, weights, and missingness;
2. trust and inflation-expectation definitions and units;
3. pre/post-2025 survey dates, sample sizes, treatment, and attrition;
4. party, demographic, and media-source subgroup estimates;
5. standard errors or confidence intervals; and
6. counterexamples where trust and inflation beliefs diverge.

Until that gate is passed, the official abstract remains a source-discovery
and bounded metadata layer, not a substitute for full-text evidence.
