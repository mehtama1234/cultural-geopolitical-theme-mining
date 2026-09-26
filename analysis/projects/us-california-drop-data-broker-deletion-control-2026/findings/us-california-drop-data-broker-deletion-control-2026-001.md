# Finding 001: A centralized deletion route can reduce effort while leaving matching and persistence unresolved

**Status:** bounded California privacy-control implementation finding ·
**Checked:** 2026-09-23

## The bounded finding

California’s Delete Request and Opt-Out Platform (DROP) gives consumers one
verifiable request intended to reach every participating data broker holding
related personal information. CalPrivacy reported more than 325,000 consumer
sign-ups and submissions and more than 600 active brokers in July 2026. The
route hashes submitted information, and the agency says raw data are not stored
in DROP or shared with brokers through the mechanism.

The route also makes partial control visible. Public statuses include deleted,
exempted, opted out of sale, not found, and pending. CalPrivacy says matching
depends on the information supplied, optional identifiers may improve results,
and status updates can take up to 90 days. Brokers must access the mechanism at
least every 45 days and process requests subject to legal exceptions.

The safe interpretation is:

> Centralizing a privacy request can reduce repeated consumer effort and make
> administrative failure states legible, while matching, exemptions, waiting,
> residual data, and future re-collection remain determinants of practical
> control.

## Evidence chain

```text
data-broker exposure and privacy concern
  -> single verifiable DROP request
  -> hashed matching and broker processing
  -> deleted, exempted, opted-out, not-found, or pending status
  -> [open] residual data, re-collection, correction, trust, switching, or exit
```

## What it adds to the broader atlas

This advances the practical-exit lane from formal deletion rights to a named
implementation route with a processing clock and explicit partial-success
vocabulary. It complements platform account-exit studies: privacy control can
be centralized without making the underlying data ecosystem fully observable
or durable to the consumer.

## What the source does not show

- The 325,000 figure is a reported program-scale count, not a completed
  deletion count or unique matched-broker outcome.
- The public sources do not show how many requests matched, were deleted,
  exempted, opted out, not found, or remained pending.
- Hashing and a single request do not establish that data stayed deleted or
  that brokers did not retain data under an exception or re-collect it later.
- The case is California implementation evidence, not a U.S.-wide privacy
  outcome, consumer-trust estimate, or wellbeing result.

## Next decisive test

Publish a de-identified consumer-by-broker status panel with request date,
matching fields, processing delay, exemption reason, deletion confirmation,
post-deletion reappearance, and consumer effort. Measure whether the single
route changes repeat requests, confidence, switching, or practical exposure.

## Sources and storage boundary

- [CalPrivacy implementation explanation](https://privacy.ca.gov/2026/07/drop-data-broker-deletions-how-do-they-work/)
- [CPPA broker requirements](https://cppa.ca.gov/data_brokers/)
- [CPPA DROP rulemaking page](https://cppa.ca.gov/regulations/drop.html)
- [Committed official-source extract](../evidence-extract-2026-09-23.md)
- [Machine-readable record](../../../records/us-california-drop-data-broker-deletion-control-2026.json)

**Evidence status:** official California pages support the centralized-request,
hashed-matching, processing-clock, and status-vocabulary pathway; consumer-level
completion, persistence, equal access, trust, and behavioral effects remain
open.
