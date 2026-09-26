# Source search: California DROP status and practical data control

**Search date:** 2026-09-22  
**Geography:** California residents, the California Privacy Protection Agency, and data brokers using DROP  
**Status:** bounded pass complete; request visibility is not aggregate proof of deletion

## Working question

What does the official DROP workflow show about the conversion from a consumer
deletion request to visible status and actual data control?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-CPPA-DROP-HOW-2026 | [How DROP works](https://privacy.ca.gov/drop/how-drop-works/) | Describes eligibility, the eight-digit tracking ID, broker status categories, 90-day reporting window, and recurring deletion process. | Official agency guidance | Describes the system and statuses; it is not a public outcome dataset for submitted requests. |
| US-CPPA-DROP-PROCESSING-2026 | [Processing DROP requests](https://privacy.ca.gov/drop-for-data-brokers/process-drop-requests/) | Describes broker downloads, matching, reporting, 45-day cycles, service-provider directions, and ongoing suppression requirements. | Official agency guidance | Does not show broker-level completion rates, downstream audits, or consumer-level outcomes. |
| US-CPPA-DROP-LAUNCH-2026 | [DROP data-broker deletion explainer](https://privacy.ca.gov/2026/07/drop-data-broker-deletions-how-do-they-work/) | Reports one request can reach more than 600 brokers and describes the five visible status categories. | Official agency explainer | The reported sign-up count and workflow description are not a deletion-success rate. |

## First pattern

```text
consumer profile and verified request
  -> request sent to many brokers
  -> broker match or non-match
  -> status: deleted, exempted, opted out, not found, or pending
  -> contractor/dependent action and recurring suppression
  -> reappearance, safety, trust, and practical exit [open]
```

The official workflow makes the route more contestable than a silent opt-out:
the consumer receives an eight-digit ID, can review broker-level statuses, can
add identifiers, and can return to update the request. Brokers must access and
process requests at least every 45 days, report within the cycle, and maintain
requests for future matching.

## Counterpoint to keep visible

This is not simply a nonfunctional route. A visible status, recurring broker
duty, suppression requirement, and ability to add identifiers can create real
practical leverage. But status categories differ: “not found” does not prove no
data exists, “opted out” can mean the broker still holds data, and exemptions or
first-party/public data can remain. The official pages reviewed do not publish a
request-level aggregate table of completed deletion, residual copies, contractor
compliance, or later reappearance.

## Decision rule

Use this source for the conversion from formal privacy right to visible,
contestable administrative status. Do not turn the number of sign-ups, a status
label, or the legal processing cycle into a deletion success rate, universal
privacy improvement, reduced harm, or durable consumer exit.
