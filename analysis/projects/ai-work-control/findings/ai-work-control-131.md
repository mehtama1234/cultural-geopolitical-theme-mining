# Finding 131: A centralized deletion route can reduce effort before durable privacy control is proven

**Status:** bounded digital-control and consumer-power finding · **Checked:** 2026-09-21

## The bounded finding

California's Delete Request and Opt-out Platform (DROP) lets a consumer send one
verifiable request to more than 600 data brokers. CalPrivacy reported more than
325,000 sign-ups and submitted requests by July 2026. The system hashes the
consumer's information before broker matching, and brokers are required to
access the mechanism at least every 45 days and process matching requests.

The route also makes the missing middle visible: a consumer can see statuses
such as deleted, exempted, opted out of sale, not found, or pending. But the
public material does not show a named consumer's matched-broker denominator,
actual deletion, residual data, status distribution, or durable non-recollection.

```text
privacy concern
  -> one centralized verified request
  -> broker matching and status categories
  -> verified deletion / persistent control / trust / switching [open]
```

## Why it matters for the larger atlas

This is a useful cultural and consumer-power mechanism: privacy control is not
only a legal right; it is also a time-and-effort problem. Centralization can
make a right more usable and observable, while matching quality, exemptions,
optional identifiers, delays, and broker compliance can still distribute
control unevenly. It extends the atlas's privacy route beyond firm-level request
counts toward a system designed to expose the result state.

## Evidence boundary

- The source reports program scale and system design, not individual deletion
  outcomes.
- A status label is not an independent scan proving that all data was removed
  or stayed removed.
- The more-than-325,000 figure is a program-level count, not a completion rate.
- No claim is made about trust, wellbeing, switching, or reduced data exposure.

## Next test

Obtain a privacy-preserving consumer-broker status panel with request date,
matched broker count, status, exemption reason, later reappearance, follow-up
effort, and trust or non-use outcome.

## Sources

[CalPrivacy explanation of DROP](https://privacy.ca.gov/2026/07/drop-data-broker-deletions-how-do-they-work/)

[CPPA data-broker implementation requirements](https://cppa.ca.gov/data_brokers/)

[CPPA DROP rulemaking record](https://cppa.ca.gov/regulations/drop.html)

[Machine-readable trend record](../../../records/us-california-drop-data-broker-deletion-control-2026.json)

**Evidence status:** official program and regulatory implementation sources;
individual deletion, persistence, trust, switching, and wellbeing remain open.
