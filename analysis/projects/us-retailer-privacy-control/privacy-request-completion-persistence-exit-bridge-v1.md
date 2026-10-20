# Privacy request completion to durable control and consumer exit

**Status:** sixty-second active depth artifact in the ongoing program  
**Checked:** 2026-10-19
**Scope:** privacy requests, identity verification, denial, deletion,
centralized data-broker control, residual data, re-collection, trust, and
switching

## What we found

Walmart's 2025 California metrics report 1,914 access requests, of which 1,588
were completed and 326 denied; 3,199 deletion requests, of which 1,962 were
completed and 1,237 denied; and 17,367 sale-opt-out requests, of which 17,276
were completed and 91 denied. Median completion times were 42 days for access
and 22 days for deletion. These are request rows, not unique people, and the
three action types cannot be combined into one control rate.

California's DROP provides a different route. CalPrivacy reported more than
325,000 consumers signed up and submitted requests by July 2026, with more
than 600 active brokers in the described system. One verifiable request can
reach participating brokers, submitted information is hashed before matching,
and brokers must access the mechanism at least every 45 days. Public status
categories include deleted, exempted, opted out of sale, not found, and
pending; status updates can take up to 90 days.

Both routes make administrative handling more visible. Neither proves that a
person's data was fully removed, stayed removed, or stopped being collected.

## What this connects to

| Link | Evidence | What does not transfer |
|---|---|---|
| Privacy right -> administrative route | Walmart reports received, completed, denied, and timing stages; DROP reports a centralized request architecture and status vocabulary. | A submitted or completed request is not verified durable control. |
| Centralization -> lower effort | DROP can replace repeated broker requests with one verifiable request. | One route can still require identifiers, waiting, interpretation of exemptions, or repeated checking. |
| Completion -> practical deletion | Walmart and DROP expose processing stages. | Neither source publishes a person-by-broker deletion panel, residual-data scan, or re-collection outcome. |
| Control -> trust or exit | Privacy control could affect confidence, provider choice, or platform exit. | No source here measures later trust, switching, wellbeing, or non-use. |

## The deeper question

**When does a privacy request create durable consumer control, and when does it
create only a visible administrative completion without reducing practical data
exposure?**

### Why ask it

Privacy rights are often evaluated by whether a request route exists or whether
an organization reports completion. Consumers experience control differently:
whether the request matched the right records, whether exemptions were clear,
whether data reappeared, whether the person had to repeat the effort, and
whether the result changed future exposure or provider choice.

Priority is **high** because the question connects platform power, consumer
recourse, data infrastructure, trust, time, and exit. Effort is bounded to one
consumer-by-broker or request-by-firm panel; scope risk is controlled by not
pooling Walmart's retail metrics with DROP's broker route.

## What we know so far

- Company metrics can show administrative capacity and delay without proving
  complete deletion.
- A centralized public route can reduce repeated effort and expose partial
  states such as not found, exempted, or pending.
- Access, deletion, and sale opt-out are different rights with different
  meanings and should remain separate.
- Matching quality, exemption reason, residual copies, re-collection, and
  consumer understanding are the missing middle.
- A formal privacy route may improve control without changing trust or
  switching, and people may switch without proving deletion.

## Bounded public discussion

The [California Privacy Protection Agency discussion](../../social-discussions/records/atlas-batch-0042-drop-linkedin-001.json)
describes DROP as a centralized deletion route and highlights broker processing.
It is an institutional announcement, not a consumer outcome sample. It supports
the implementation question while preserving the boundary between submission,
broker compliance, and durable deletion.

## What could change the answer

- A high completion rate may reflect effective identity matching and complete
  deletion for most people, even if public aggregates do not prove it.
- Denials may be legitimate responses to verification, exemptions, duplicates,
  or requests outside the legal scope rather than system failure.
- Centralization may improve practical control for people with little time while
  creating new exclusion for people unable to supply matching identifiers.
- Re-collection may be lawful or unavoidable in some business relationships,
  so deletion persistence must be defined by the specific right and purpose.
- Consumers may retain trust because control is improving, or lose trust because
  the route makes persistent data exposure newly visible.

## Challenge checks

- Activity was not treated as outcome: request, verification, completion,
  deletion, persistence, trust, switching, and exit remain separate.
- Correlation was not treated as cause: neither source estimates the effect of
  a route on privacy behavior or consumer welfare.
- Scope was checked: Walmart is a company-reported California request universe;
  DROP is a statewide broker mechanism with reported program-scale counts.
- Sources were not counted as independent replications: Walmart metrics and
  DROP implementation pages describe different systems and denominators.
- Affected people were retained: consumers with limited time, language,
  disability, digital access, identifiers, or ability to appeal; data brokers,
  retailers, and downstream data users.
- The regulator's public post was treated as implementation discussion, not
  proof of compliance.

## Current answer

**Partly answered.** The evidence shows two increasingly visible privacy-control
routes with administrative timing and partial-status information. It does not
yet prove person-level deletion, persistence, equal access, changed exposure,
trust, switching, or exit.

## Latest pass disposition — 2026-10-19

This lane is now treated as an acquisition gap rather than an open source-
collection task. The available public evidence reaches request submission,
status categories, completion, denial, and processing time, but stops before a
linked person/request observation of downstream deletion, re-collection,
appeal, or later behavior. Repeating aggregate Walmart or DROP counts would
not add a missing stage or compatible denominator. The next rotation therefore
moves to a different named platform-control episode.

## What to look for next

Follow one privacy request:

```text
data exposure and consumer concern
  -> request, identity verification, and matching
  -> deleted, denied, exempted, not-found, or pending result
  -> downstream deletion and post-deletion reappearance check
  -> repeat effort, appeal, trust, switching, or exit
```

Record request type, identifiers supplied, broker or firm match, delay, denial
reason, deletion confirmation, residual-data check, re-collection, appeal, and
later consumer behavior. Stop if the source ends at request status; report an
individual-control acquisition gap rather than a durable-privacy finding.

## Source links

- [Retailer privacy project](README.md)
- [Existing Walmart finding](findings/us-walmart-privacy-request-completion-2025-2026-001.md)
- [Walmart request metrics record](../../records/us-walmart-ccpa-privacy-request-completion-2025-2026.json)
- [California DROP record](../../records/us-california-drop-data-broker-deletion-control-2026.json)
- [California regulator discussion](../../social-discussions/records/atlas-batch-0042-drop-linkedin-001.json)

## Stopping rule

Do not call a privacy route effective or consumer-empowering until a
consumer-level or valid linked panel observes request access, matching,
completion or denial, downstream deletion, persistence or re-collection, and
later trust or switching with compatible denominators and a credible
counterexample.
