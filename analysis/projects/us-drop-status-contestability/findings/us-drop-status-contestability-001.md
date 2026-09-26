# Finding 001: A deletion system can make requests contestable while showing partial broker-level control

**Status:** bounded platform and administrative-contestability finding · **Checked:** 2026-09-22

## The bounded finding

California's Delete Request and Opt-out Platform (DROP) lets a verified resident
send one request to more than 600 data brokers. The official workflow gives the
consumer an eight-digit tracking ID and broker-level statuses: deleted,
exempted, opted out, record not found, or pending. Data brokers must begin
processing requests in August 2026, access them at least every 45 days, report
their status, and keep screening for newly collected matching data.

That is a real improvement in visibility and contestability. A later CalPrivacy
implementation update reports that 99.9% of registered consumers had a profile
deleted by at least one broker, and that the typical user had deletion from
more than 40 brokers. This is a meaningful later implementation result, but it
is not an all-broker or person-level audit. The public record still does not
provide the full consumer-broker status table, show how many records remained in
downstream contractors or copies, establish re-collection, or show what
happened to the consumer afterward.
Several statuses also leave data in place: “not found” can reflect a failed
match rather than no data, “opted out” means the broker may still hold data,
and exemptions or first-party/public data can remain.

The route is:

```text
verified consumer request
  -> broker matching
  -> per-broker status
  -> deletion, exemption, opt-out, or no match
  -> contractor/dependent action and recurring suppression
  -> residual data, reappearance, safety, trust, or durable exit [open]
```

## What this adds to the broad atlas

This adds a digital version of the program's recurring distinction:

> Making a process visible can increase a person's ability to contest it while
> leaving the final material outcome unmeasured.

The system is not merely an offer on a webpage. It supplies a tracking ID,
broker-specific states, a route to add identifiers, and recurring obligations.
That gives the consumer a way to see and challenge administrative progress. It
still does not establish that every copy, inference, contractor record, or
future collection was controlled.

## Limits and next test

- The official pages describe system rules and status categories; they are not a
  public microdata file or aggregate completion report.
- A status is not a full data inventory. “Record not found,” “opted out,” and
  “exempted” can leave uncertainty or data in place.
- The pages do not show broker-by-broker completion rates, unmatched-request
  rates, contractor compliance, downstream deletion, data reappearance, or
  consumer harm.
- The system is California-specific and newly operating; the 90-day reporting
  window means early statuses may be incomplete.
- More than 600 reachable brokers, sign-up counts, and the agency's typical-user
  result describe implementation reach; they do not establish complete
  all-broker deletion or improved wellbeing.

The next decisive artifact is a privacy-protected aggregate DROP ledger with
requests, broker matches, statuses, timing, exemptions, contractor actions,
reappearance checks, and later consumer-reported safety or trust. Until then,
the safe claim is that DROP makes deletion more visible and contestable, not
that it has achieved complete or durable data removal.

## Sources

- [California: How DROP works](https://privacy.ca.gov/drop/how-drop-works/)
- [California: Processing DROP requests](https://privacy.ca.gov/drop-for-data-brokers/process-drop-requests/)
- [California: DROP data-broker deletion explainer](https://privacy.ca.gov/2026/07/drop-data-broker-deletions-how-do-they-work/)
- [California: August 2026 DROP implementation update](https://privacy.ca.gov/2026/08/half-a-million-californians-have-signed-up-for-drop-to-delete-their-personal-information-from-data-brokers/)

**Evidence status:** official agency guidance and a later implementation update
establish a trackable recurring process plus reported partial broker-level
deletion reach; complete all-broker deletion, downstream control, reappearance,
harm, trust, and durable exit remain unmeasured.
