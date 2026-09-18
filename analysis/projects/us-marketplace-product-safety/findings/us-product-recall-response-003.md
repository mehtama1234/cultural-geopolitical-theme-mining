# Finding 003: A recall key links correction progress without proving consumer recovery

**Status:** verified single-recall implementation bridge; consumer recovery open  
**Checked:** 2026-09-17

## The bounded finding

Recall key `23-238` creates a compact product-level episode across two CPSC
surfaces. The July 6, 2023 notice identifies VRURC OD-B7 portable chargers,
about 190,000 units sold through Amazon, a fire hazard, one reported fire, and
four smoke-inhalation hospital transports. The August 21, 2026 Monthly
Progress Report (MPR) snapshot uses the same recall key and reports 64,963
consumer-level corrections and 65,293 total corrections.

This is a meaningful implementation bridge:

```text
hazard and injury signal
  -> dated public notice and stop-use instruction
  -> free replacement remedy
  -> later firm-reported correction counts
  -> [open] purchaser notice, replacement receipt, safe restoration, residual loss, trust, or exit
```

The bridge does not turn a recall-level correction count into a consumer
recovery rate. The API notice and MPR snapshot report different product
denominators, and CPSC says the consumer-level percentage uses a consumer-held
denominator that can differ from total products recalled.

## The joined episode

| Stage | Compact observation | Safe interpretation |
|---|---|---|
| Product and timing | Recall `23-238`; notice dated 2023-07-06; OD-B7 chargers sold July 2021–May 2023 for $30–$40 | A dated product-level hazard episode is identifiable |
| Exposure scale in notice | About 190,000 units; exclusively Amazon.com | Notice-level product scale, not unique purchasers or households |
| Harm signal | One reported fire during a commercial flight; four flight attendants hospitalized for smoke inhalation | Reported injury signal, not population incidence or purchaser risk rate |
| Offered remedy | Stop use and contact VRURC for a free replacement | Remedy availability and required action are visible |
| Later MPR snapshot | 256,845 products recalled; 64,963 consumer corrections; 65,293 total corrections; reported consumer and total percentages 29% and 25% | Firm-reported cumulative implementation progress under MPR definitions |
| Individual recovery | Not present | Notice receipt, contact, replacement receipt, timing, safe use, and residual cost remain unknown |

The MPR numbers are still valuable. They show that the institutional response
has an operational reporting stage beyond merely publishing a notice. They do
not reveal whether one correction equals one consumer, whether a corrected
product was safely replaced, when the correction occurred, or whether an
affected household had to buy a substitute before receiving it.

## The denominator reconciliation is part of the finding

The API’s “about 190,000” and the MPR’s `256,845 products recalled` cannot be
silently combined. The difference is 66,845 products, or roughly 35.2% of the
MPR figure. That arithmetic is not an estimate of under-reporting or exposure
failure. It identifies a version, scope, or denominator question.

The MPR notes that the starred consumer percentage uses products consumers
have or had in their possession, which can differ from the total products
recalled. The public record therefore contains at least three possible units:

```text
units described in notice
  != products recalled in progress workbook
  != consumer-held denominator for reported percentage
  != unique purchasers or households
```

The correction count is consequently best coded as **reported implementation
progress**, not “29% of consumers recovered.” This is exactly the kind of
measurement boundary the broad atlas needs when moving from institutional
capacity to lived consumer outcome.

## What the bridge establishes

| Arrow | Status | Safe conclusion |
|---|---|---|
| Hazard → public notice | Observed | A dated recall notice identifies product, hazard, market, and remedy |
| Notice → required consumer action | Reported | Stop-use and contact instructions are explicit |
| Notice → offered replacement | Reported | A free replacement route is offered |
| Recall key → later correction snapshot | Observed | The same key joins notice metadata to MPR progress fields |
| Correction count → unique consumer completion | Open | Product counts and firm-reported fields do not identify unique completed cases |
| Correction → replacement receipt or safe restoration | Open | Receipt, timing, safe use, and residual hazard are not observed |
| Safety event → household cost or behavior | Open | No purchaser, substitute purchase, disposal, work, care, trust, or switching field exists |

The bridge therefore closes one institutional stage while preserving the
central open arrow. It is stronger than a notice-only design and weaker than a
consumer-level longitudinal remedy ledger.

## Why it matters to the broad goal

Product safety is a useful consumer-power test because the public system can
appear highly active while the final burden remains private. The regulator and
firm can publish a notice, specify a remedy, and report correction progress;
the consumer may still need to discover the notice, identify the model, stop
using an essential device, contact the firm, wait for a replacement, and bear
temporary cost or risk.

The same staged logic applies across the atlas:

```text
institutional announcement
  != usable remedy
usable remedy
  != completed correction
completed correction
  != protected outcome
protected outcome
  != trust, repurchase, switching, or exit
```

The result connects consumer recourse, household room, firm reporting, public
systems, unequal exposure, and institutional legitimacy without pooling their
units or inferring political meaning from a correction percentage.

## Limits and next decisive test

- The API and MPR are live or versioned sources; later rechecks may change the
  wording, counts, or remedy status.
- The API injury signal is a reported event, not a denominator-based injury
  incidence estimate.
- MPR values are firm-reported cumulative progress and may contain blanks or
  fields not yet due, not provided, processed, or barred from disclosure.
- The recall key joins product-level records, not individual purchaser rows.
- A free replacement can still involve delay, interruption, disposal, or
  temporary substitution; none is measured here.

The smallest qualifying extension is a lawful, recall-key-compatible consumer
ledger containing notice reach, contact/claim date, replacement receipt,
temporary substitute or residual cost, and a later safety, trust, continued-
use, switching, or non-use outcome. Until such a ledger exists, the safe claim
is implementation visibility—not consumer recovery or exit.

## Reproduction and storage boundary

This finding reads two compact derived JSON artifacts already retained in the
repository and downloads no new raw archive. The [canonical machine-readable
record](../../../records/us-cpsc-vrurc-recall-implementation-2023-2026.json)
preserves the staged measures, denominator warning, source URLs, and hashes.

Related evidence:

- [Current CPSC remedy-design finding](us-product-recall-response-002.md)
- [Recall-key bridge audit](../data/cpsc-vrurc-recall-key-bridge-2026-09-17.json)
- [MPR bounded sample](../data/cpsc-mpr-bounded-sample-2026-08-21.json)

**Evidence status:** one dated product-level hazard-to-implementation bridge is
verified; purchaser exposure, remedy receipt, safe restoration, residual cost,
trust, repurchase, switching, and exit remain unobserved.
