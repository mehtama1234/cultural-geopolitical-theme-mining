# Finding 001: Emergency disaster loans can preserve firms and employment without proving household or customer recovery

**Status:** causal firm-level research summary · **Checked:** 2026-09-17

## The bounded finding

The NBER study *After the Storm* follows more than 167,000 firm loan
applications across approximately 1,900 US disasters, merging applications with
Census records and business credit reports for up to seven years. The authors
report that government recovery loans reduce firm exit and bankruptcy, increase
employment and revenue, unlock private credit, and reduce delinquency. They
also report no capital reallocation away from neighboring firms and some
positive spillovers on local entry.

The mechanism proposed by the authors is that emergency liquidity resolves
uncertainty about whether repairs are feasible, allowing firms that struggle to
obtain private credit to continue operating.

## Event chain

```text
disaster damage or disruption
  -> repair and working-capital financing gap
  -> government recovery loan
  -> lower firm exit/bankruptcy, higher employment/revenue, private-credit access
  -> [open] worker pay/quality, customer prices/service, owner recovery,
         local meaning/action, and durable community security
```

## What the study contributes

| Stage | Supported by the paper summary | Still open for the broad atlas |
|---|---|---|
| Shock | Distinct natural disasters and post-disaster firm distress | Household exposure, disaster severity by customer/worker, insurance adequacy |
| Public intervention | Government-provided recovery loans | Approval, amount, rate, collateral, timing, and unequal access for each firm |
| Firm outcome | Lower exit/bankruptcy; higher employment/revenue; lower delinquency | Job quality, wages, hours, safety, worker bargaining, and repayment burden |
| Local system | No detected capital reallocation from neighboring firms; some positive local entry spillovers | Service availability, affordability, customer switching, local prices, and community trust |
| Household/political outcome | Not measured in the retained summary | Owner/worker household recovery, displacement, attribution, political action, and exit |

## Why it matters to the broad atlas

This is a useful causal middle layer between disaster exposure and local
economic capacity. It shows that public liquidity can alter firm survival and
employment rather than merely provide a stated program route. But firm survival
is not the same as public security: a surviving firm may still carry debt, offer
poor-quality work, raise prices, or remain inaccessible to households. The
study therefore strengthens the firm/state/finance lane while making the
worker, customer, owner-household, and meaning/action joins more precise.

Because the current repository retains the official abstract-level result and
not the working-paper data or code, the atlas does not claim effect sizes or
reproduce the design. The canonical record is a directional evidence anchor
and acquisition target for a later full-paper audit.

## Coding consequence

```text
loan receipt                 != firm welfare for every borrower
firm survival               != worker security
employment increase         != better pay or job quality
local entry spillover       != customer affordability or access
public liquidity success    != owner-household recovery or political legitimacy
```

Code this as **causal firm-level emergency-liquidity evidence with survival,
employment, revenue, credit, and delinquency outcomes; worker, customer,
owner-household, trust, action, and geopolitical consequences open**.

## Next decisive test

Obtain the smallest full-paper appendix or lawful replication artifact needed to
record treatment timing, loan amount/terms, effect sizes, uncertainty, firm
size/sector/place heterogeneity, and disaster severity. Then link firm outcomes
to worker pay/quality, customer prices/service continuity, owner household
spending, and local public capacity only where identifiers and dates permit.

## Sources and storage boundary

- [NBER Working Paper 32326](https://www.nber.org/papers/w32326)
- [SBA disaster assistance context](https://www.sba.gov/funding-programs/disaster-assistance)
- [Committed source packet](../source-search-2026-09-11.md)
- [Machine-readable trend record](../../../records/us-small-business-disaster-liquidity-causal-2024.json)

Only the official paper page and existing local source packet were used. No
working-paper PDF, code archive, or microdata was downloaded or retained.
