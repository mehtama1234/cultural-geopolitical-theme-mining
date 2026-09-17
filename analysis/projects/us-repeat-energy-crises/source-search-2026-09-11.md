# Source search: US repeat energy crises

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** matched evidence pass complete; cause of repeat need remains open

## Working question

When a household needs energy help more than once, is the cause a short cash gap, a failing home, or a problem that one payment cannot fix?

## Sources

| ID | Source | What it tells us | Limit |
|---|---|---|---|
| HHS-LIHEAP-PERFORMANCE | [HHS: LIHEAP performance measures](https://stage.liheappm.acf.hhs.gov/what-are-pm/) | Federal reporting separates benefit targeting, energy burden, restoration of home energy service, and prevention of loss of service. HHS defines prevention as the number of times service would have been lost without assistance. | The measures show program performance and avoided loss, but do not by themselves identify why the same household returns. |
| HHS-LIHEAP-DATA | [HHS: LIHEAP performance data warehouse](https://stage.liheappm.acf.hhs.gov/performance-measures) | The warehouse provides reports by grant recipient and includes data on energy burden and continuity of service. | Public program totals do not automatically create a person-level or household-level repeat history. |
| HHS-LIHEAP-FY24 | [HHS/ACF: FY24 LIHEAP annual report spotlight](https://ocsannualreport.acf.hhs.gov/annual-report-fy24/priorities-and-fy24-spotlights) | FY24 LIHEAP helped nearly 6 million households or families and reported 279,000 instances of restored home energy. | Reach and restoration are not the same as months of later stability or absence of repeat crisis. |
| EIA-RECS-2024-HC11.1 | [EIA: Household energy insecurity, 2024](https://www.eia.gov/consumption/residential/data/2024/hc/pdf/HC11.1_2024.pdf) | Preliminary 2024 estimates count unsafe temperatures, skipped food or medicine, shutoff notices, and unusable heating or cooling equipment. | Categories can overlap and do not show whether the problem was temporary, repeated, or repaired. |
| GAO-HUD-UTILITY-ALLOWANCE | [GAO: HUD rental assistance and utility allowances](https://www.gao.gov/products/gao-24-105532) | Utility costs can still make assisted households rent-burdened when allowances do not fully cover reasonable costs. | The finding concerns assisted housing and does not explain every repeat energy crisis. |

## First pattern to test

```text
first energy crisis
  -> payment, restoration, repair, or weatherization
  -> next bill and home condition
  -> repeat crisis or stable service
```

Repeat need should trigger a different question from first need: what remained unchanged after the first intervention?

## Delivery recheck

On 2026-09-16, targeted requests to the official LIHEAP performance-measure
definition page and performance warehouse returned HTTP 502 responses from the
staging host. This is recorded as a delivery/access failure, not an empty
performance dataset and not evidence that any state or grant recipient had no
reported restoration or prevention measure. The stable FY2024 annual-report
spotlight remains the currently usable public aggregate; recipient-level
performance extraction stays open until the official warehouse is reachable.
