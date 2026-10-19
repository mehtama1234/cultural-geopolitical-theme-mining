# Finding 001: The ACA's ban on health underwriting helped low-income, high-risk, and older applicants most

**Status:** bounded health-insurance access and distributional finding · **Checked:** 2026-10-18

The Affordable Care Act banned health underwriting and rejection for
pre-existing conditions and introduced large premium subsidies for low- to
middle-income individuals. A new NBER study uses a proprietary dataset of
pre-ACA insurance applications and underwriting decisions to observe a margin
that is often missing from post-ACA enrollment data: who would have been
rejected or disadvantaged before the reform.

The paper estimates that the ACA's benefits were concentrated among low-income,
high-risk, and over-50 individuals.

The route is:

```text
pre-ACA health risk, age, and income
  -> underwriting or rejection and premium exposure
  -> ACA ban plus subsidies
  -> changed practical insurance option
  -> [open] enrollment persistence, network access, treatment, job mobility, and household security
```

## Current Marketplace scale and affordability stage

CMS's [2026 Open Enrollment report](https://www.cms.gov/newsroom/press-releases/exchange-coverage-remains-near-record-high-23-1-million-enroll-2026-reflecting-continued-strength)
reports **23.1 million** consumers selected or were automatically re-enrolled
through the federal and state-based Marketplaces for plan year 2026. CMS's
reporting separates **19.5 million returning consumers** from new selections.
Its 2026 plan-and-price fact sheet projects an average post-tax-credit premium
of **$50 per month** for the lowest-cost plan for eligible enrollees, but says
only 60% of eligible re-enrollees have access to a plan in their chosen
category at or below $50, compared with 83% in 2025.

This adds a national enrollment and nominal affordability stage to the ACA
option-value route. It does not prove that a plan selection became effectuated
coverage, that the premium was paid, that the chosen network contained a usable
provider, or that treatment occurred. CMS's [public-use files](https://www.cms.gov/data-research/statistics-trends-reports/marketplace-products/2026-marketplace-open-enrollment-period-public-use-files)
provide state, county, income, assistance, metal-level, and switching fields,
but they do not provide claims or treatment continuity.

## Bounded public discussion

The [coverage-denial discussion](../../../social-discussions/records/atlas-batch-0049-coverage-denials-linkedin-001.json)
frames prior authorization and denials as a route from clinical recommendation
to delay, appeal work, financial exposure, and trust loss. It is useful for
identifying the lived meaning of the missing middle between coverage and care,
but it is advocacy and selected LinkedIn discussion, not a prevalence estimate
or an ACA enrollment evaluation.

## What this adds to the atlas

This strengthens the program's distinction between formal coverage expansion
and actual distribution of practical options. The relevant counterfactual is
not only whether someone enrolled after the ACA; it is whether the person could
previously have been rejected or priced out because of health risk.

It also adds a distributional mechanism to the health-cost lane: the same legal
change can have much larger option value for high-risk, lower-income, and older
applicants. That does not mean that those groups automatically received care or
became financially secure.

## Limits and next test

- The public abstract does not disclose the full sample, model specification,
  subsidy assumptions, or every effect estimate.
- The proprietary underwriting data describe the pre-ACA application margin;
  they do not by themselves establish later enrollment, premium payment, or
  continuous coverage.
- Network adequacy, appointment access, treatment continuity, health, job
  switching, and household financial outcomes remain unmeasured here.
- CMS plan selections and automatic re-enrollment do not establish effectuated
  coverage, premium payment, provider use, claims, or treatment continuity.
- This should not be merged with the separate ACA dependent-coverage job-lock
  finding; both concern insurance and work but use different populations and
  mechanisms.

The next decisive artifact is a protected applicant-to-care ledger linking
pre-policy underwriting or rejection risk, post-policy plan choice, subsidy,
premium payment, network and appointment access, treatment continuity, job
choice, medical cost, and later household security. The CMS 2026 public-use
fields can supply the plan-selection and affordability context, but not the
same-person care endpoint.

## Sources

- [NBER Working Paper 35692](https://www.nber.org/papers/w35692)
- [CMS 2026 Marketplace enrollment report](https://www.cms.gov/newsroom/press-releases/exchange-coverage-remains-near-record-high-23-1-million-enroll-2026-reflecting-continued-strength)
- [CMS 2026 Marketplace public-use files](https://www.cms.gov/data-research/statistics-trends-reports/marketplace-products/2026-marketplace-open-enrollment-period-public-use-files)
- [CMS 2026 Marketplace plans and prices](https://www.cms.gov/newsroom/fact-sheets/plan-year-2026-marketplace-plans-prices-fact-sheet)
- [Bounded coverage-denial discussion](../../../social-discussions/records/atlas-batch-0049-coverage-denials-linkedin-001.json)
- [Machine-readable record](../../../records/us-nber-aca-underwriting-heterogeneous-effects-2026.json)

**Evidence status:** proprietary pre-ACA underwriting data and modeled reform
effects identify heterogeneous option value; enrollment persistence, care,
health, work, and household outcomes remain open.
