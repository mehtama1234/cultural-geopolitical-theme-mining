# Source search: US small-business disaster liquidity

**Search date:** 2026-09-11  
**Geography:** United States natural disasters  
**Status:** opening pass; firm effects are measured, household and local-service effects remain open

## Working question

When a small firm survives a shock, who else keeps their options?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-NBER-FIRM-DISASTER-LIQUIDITY | [After the Storm: How Emergency Liquidity Helps Small Businesses Following Natural Disasters](https://www.nber.org/papers/w32326) | Government recovery loans reduced small-business exit and bankruptcy, increased employment and revenue, unlocked private credit and reduced delinquency. The authors connect the effects partly to resolving uncertainty about repairs and find some positive spillovers on local entry. | NBER working paper | It does not show the owner's household spending, job quality or which local customers lose access when a firm exits. |
| US-NBER-OWNER-HOUSEHOLD | [Revenue Collapses and the Consumption of Small Business Owners](https://www.nber.org/papers/w28151) | Linked business and household accounts show that business revenue changes can affect the owner's household consumption. | NBER working paper | The COVID shock differs from a natural disaster and does not measure recovery loans or local workers. |
| US-AFA-2023-FIRM-DISASTER-EFFECT-SIZES | [After the Storm: Direct and Spillover Benefits from Disaster Loans to Small Businesses](https://afajof.org/management/viewp.php?n=42000) | Earlier author version reports effect sizes for exit, deformalization, employment, revenue, private debt, bankruptcy, and local entry. | Effect-size transcription only | March 2023 version; estimates are not assumed identical to the current NBER revision. No PDF or restricted data retained. |
| US-HARVEY-CONSUMER-WELFARE | [Rebuilding After the Storm: Firm Turnover and Consumer Welfare After Hurricane Harvey](https://benklopack.github.io/files/2024_12_11_Harvey.pdf) | Payment-card and consumer-demand evidence links Harvey closures and entry to travel distance and localized consumer-welfare losses. | Author-hosted working paper | Payment-card coverage, model assumptions, and tract-level exposure limit population-wide interpretation; no raw transactions retained. |

## First pattern to test

```text
disaster damage
  -> repair and cash need
  -> recovery loan, insurance, private credit, or no help
  -> firm exit or survival
  -> jobs, revenue, customers, owner household and local services
```

The firm study supports a recovery effect for government credit. The broader worker, customer and household path remains open.

The [effect-size audit](effect-size-audit-v1.md) adds version-labeled
magnitudes from the authors' March 2023 version: a 13-point reduction in exit,
an 18% employment increase in the full sample and 45% among employer firms,
about $18,000 more private debt, and a 3.8-point reduction in bankruptcy. These
are transcription anchors pending a table-level check against the current
NBER revision, not pooled estimates.

## Counterpoint to keep visible

Keeping a firm open can preserve jobs and services, but it can also preserve a weak business or place risk on public funds. Revenue and employment do not reveal pay, safety or service quality.

## Main gaps

- damage, repair cost and insurance payment;
- loan terms, approval and repayment;
- owner household income, debt and spending;
- worker jobs, pay, hours and benefits;
- customer prices, access and local substitution;
- differences by race, place, industry, firm age and disaster type.

## Decision rule

Keep firm survival, revenue, employment, job quality, customer access and household security separate. A lower exit rate is not by itself proof of broad local benefit.
