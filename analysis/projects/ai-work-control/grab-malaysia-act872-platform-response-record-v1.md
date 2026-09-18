# Grab Malaysia Act 872 platform-response record v1

**Status:** company-reported implementation and commitment layer; independent
worker use and outcome open  
**Checked:** 2026-09-18

## Bounded finding

Grab Malaysia's Act 872 page publishes a platform-side response to the new
Malaysian gig-work regime. It says Grab has or will provide clear service
agreements, an earnings framework, a strike system before termination, appeal
and dispute-resolution channels, SOCSO co-contribution or onboarding, and
strengthened appeal and discipline processes. The page also describes more
than RM10 million in partner-protection and empowerment commitments.

These are company-reported policies, commitments, or program descriptions. The
page does not provide a worker-level implementation ledger, appeal caseload,
decision changes, reactivation record, payment receipt, SOCSO enrollment
denominator, or evidence that the reported GrabCar Tribunal claimant used any
of these channels.

## Stage coding

| Stage | Evidence | Safe code |
|---|---|---|
| Platform response to Act 872 | Grab publishes an Act 872 response page, stated as updated 27 March 2026 | `reported_platform_response` |
| Service terms and earnings | Clear Terms of Service and fair/transparent earning framework are claimed | `reported_commitment` |
| Adverse-decision process | Strike system, appeal channels, and strengthened discipline process are claimed | `reported_commitment` |
| Social protection | SOCSO co-contribution and onboarding/deduction support are described | `reported_program` |
| Worker uptake | No enrollment, use, appeal, or claimant denominator | `not_observed` |
| Changed decision or access | No worker-level correction, reactivation, or account outcome | `not_observed` |
| Payment and recovery | No worker-level payment, earnings change, or recovery record | `not_observed` |
| Durability, trust, exit | No recurrence, non-retaliation, worker meaning, switching, or exit outcome | `not_observed` |

## Relationship to the GrabCar proceeding

The company page and the reported first Tribunal hearing are different evidence
units. The page describes a platform-wide response; the hearing report describes
one proceeding involving Saver Trips, cashback incentives, and Advance Booking.
The public record does not connect the claimant's dispute to a specific Grab
policy, appeal channel, earnings change, or Tribunal outcome.

```text
Act 872 in force
  -> platform publishes response and commitments
  -> reported GrabCar Tribunal hearing
  -> [open] channel use, changed decision, payment, correction, recurrence,
           worker trust, continued use, switching, or exit
```

The correct interpretation is not that Grab complied or failed to comply. It
is that a company-reported response layer now exists between statutory design
and verified worker outcome.

## Sources

- [Grab Malaysia Gig Hub / Act 872 response](https://www.grab.com/my/gigbill/)
- [Malaysia Act 872 official-route recheck](malaysia-act872-official-route-recheck-2026-09-18.md)
- [GrabCar first-hearing case record](malaysia-grabcar-tribunal-first-hearing-case-record-v1.md)
- [Machine-readable record](data/grab-malaysia-act872-platform-response-record-v1.json)

**Storage boundary:** only Grab's public page was reviewed; no partner,
appeal, earnings, or SOCSO records were downloaded or retained.
