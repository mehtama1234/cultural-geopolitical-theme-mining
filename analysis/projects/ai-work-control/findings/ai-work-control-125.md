# Finding 309: A centralized privacy request can scale control before deletion is verified

**Status:** bounded platform/data and consumer-power finding · **Checked:** 2026-09-20

## The bounded finding

California's Delete Request and Opt-out Platform (DROP) lets an eligible
consumer send one request to more than 600 data brokers. CalPrivacy reported
that more than 325,000 consumers had signed up and submitted requests by July
2026. The system hashes the submitted information rather than storing or
sharing raw data with brokers, and gives consumers a DROP ID to track broker
statuses.

This is a real privacy-control infrastructure stage: the state lowers the
effort of contacting many brokers and makes the response categories visible.
It still does not show how many broker records matched, were deleted, exempted,
merely opted out of sale, or remained unresolved for any individual.

```text
data-broker exposure
  -> centralized deletion/opt-out request
  -> broker matching and status route
  -> verified deletion / residual exposure / trust / switching [open]
```

## Why it matters for the larger atlas

The case adds a digital version of the infrastructure-to-lived-distribution
problem. A privacy right becomes easier to exercise, but the meaningful outcome
still depends on matching, exemptions, timing, re-collection, and whether the
person can verify that the data is actually gone. Control effort and control
result are separate currencies.

## Evidence boundary

- The source reports more than 325,000 sign-ups and requests, not completed
  deletion or a representative outcome rate.
- The page lists five broker-level statuses: deleted, exempted, opted out of
  sale, not found, and pending.
- Matched deletions are described as occurring on a rolling 45-day basis,
  subject to exemptions; the source does not report how often matching occurs.
- A record can be opted out of sale while still held by a broker, so “sale
  stopped” and “data deleted” must remain separate.

## Next test

Obtain an authorized aggregate or de-identified DROP status extract by broker,
including request date, match status, deletion or exemption outcome,
re-collection, and later consumer confidence or switching. Do not infer
privacy restoration from enrollment alone.

## Sources

- [California Privacy Protection Agency explanation of DROP](https://privacy.ca.gov/2026/07/drop-data-broker-deletions-how-do-they-work/)
- [Machine-readable trend record](../../../records/us-calprivacy-drop-data-broker-deletion-2026.json)

**Evidence status:** reported centralized control route, participation, and
status design; verified deletion and lived privacy outcome remain open.
