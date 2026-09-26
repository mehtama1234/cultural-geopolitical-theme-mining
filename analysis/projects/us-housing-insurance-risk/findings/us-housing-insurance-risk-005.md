# Finding 005: Wildfire insurance can move into partial payment while repairability and safe return remain open

**Status:** bounded California wildfire insurance implementation finding · **Checked:** 2026-09-21

## The bounded finding

California’s Department of Insurance wildfire claims tracker reported, as of
July 6, 2026, 41,727 claims filed for the Eaton and Palisades fires, 40,482
claims partially paid, and $25.2 billion paid to date. The tracker combines
home, business, living-expense, auto, debris-removal, and other disaster
claims, so these are claims-processing and payment stages rather than a
household repair or recovery rate.

The Department’s separate May 2026 State Farm investigation reviewed 220 claims
and found 398 violations in 114 claims, including delayed investigation,
underpayment, repeated adjuster reassignment, and smoke-damage claim delays or
denials. On September 15, 2026, California announced that AB 1795 had become
law, establishing enforceable standards for investigating, testing, and
restoring smoke-damaged homes. The law creates a wildfire-zone presumption for
smoke damage, requires insurers to pay necessary testing and sampling costs,
keeps qualifying additional-living-expense benefits in place until a home is
restored and safe to occupy, requires inspection within 30 days after claim
notice or access, requires repair estimates meeting pre-loss health and safety
standards, and preserves the policyholder's contractor choice.

The route is therefore:

```text
wildfire / smoke damage
  -> claim and living-expense route
  -> partial payment and regulator intervention
  -> claim-handling reform and smoke-restoration standards
  -> completed repair, safe return, adequate coverage, and stable housing [open]
```

## What is visible

| Stage | Public evidence | Still missing |
|---|---|---|
| Exposure | Eaton and Palisades wildfire claims, including smoke and living-expense claims | Same-property loss, habitability, and household circumstances |
| Administrative route | 41,727 claims filed; 40,482 partially paid | Final payment, total loss, delay, and claimant-level denominator |
| Money movement | $25.2B paid to date | Allocation by household, adequacy, deductible, debt, and remaining loss |
| Institutional failure | 398 violations in 114 of 220 State Farm claims reviewed | Population prevalence, other insurers, and each claimant’s remedy |
| Reform | Enacted AB 1795 creates a smoke-damage presumption, testing-cost responsibility, additional-living-expense protection, 30-day inspection timing, health-and-safety repair standards, and contractor choice | Implementation, compliance, repair completion, safe return, and future recurrence |

## Why it matters to the broad atlas

This is a stronger realization stage than a FAIR Plan policy count or a
complaint-closure total. It shows claims entering payment and a regulator
converting observed handling failures into legal standards. But “partially
paid” is not “repaired,” and a state reform is not yet a safe home. The
customer’s remaining problem can move from proving damage to financing the
repair, finding temporary housing, managing health risk, and deciding whether
to stay.

The case also shows two clocks operating together: money can flow while claim
handling remains contested, and a legal standard can be enacted while its
implementation and household effects are still future stages.

The new law is a meaningful shift in who must carry uncertainty. It moves some
proof, testing, timing, and temporary-housing obligations toward insurers, but
it does not itself show that a particular household received testing, an
adequate estimate, continued living-expense payments, a completed repair, or a
safe and affordable place to return to.

## Limits and next test

- The claims tracker combines multiple claim types and does not identify unique households or properties.
- “Partially paid” does not show final settlement, repair completion, or safe habitability.
- The State Farm examination is a sampled insurer-specific investigation, not a statewide violation rate.
- The legislation establishes standards and obligations; it does not yet demonstrate compliance or household recovery.
- The public records do not show who moved, returned, borrowed, delayed repair, or experienced lasting health/work effects.

The next decisive artifact is a lawful property-level ledger joining policy and
loss date, claim decision, payment, repair/testing, temporary housing,
additional living expenses, final habitability, renewal or replacement
coverage, and stay/move outcome.

## Sources

- [California Department of Insurance, LA County Wildfire Claims Tracker](https://www.insurance.ca.gov/01-consumers/180-climate-change/Wildfire-Claims-Tracker.cfm)
- [California Department of Insurance, State Farm claims investigation](https://www.insurance.ca.gov/0400-news/0102-alerts/2026/California-takes-legal-action-against-St.cfm)
- [California Department of Insurance, Smoke Damage Recovery Act](https://www.insurance.ca.gov/0400-news/0102-alerts/2026/California-protects-families-from-hidden.cfm)

**Evidence status:** official claims, regulator-investigation, and legal-
reform stages are reported; property-level payment adequacy, repair, safe
return, durable coverage, stay/move, trust, and political response remain
open.
