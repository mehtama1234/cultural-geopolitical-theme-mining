# Contestability is unequal: correction requires capacity v1

**Checked:** 2026-09-24  
**Scope:** public benefits, health access, consumer redress, and worker
remedies in the broad atlas

## The finding

Institutions may be highly responsive for people who can notice a problem,
assemble documents, file an appeal, wait, make repeated contact, or request a
reissue. That does not mean the same correction is reachable for everyone
affected.

The key distinction is:

```text
formal right or remedy
  -> ability to notice and contest
  -> effort, knowledge, time, documents, and safety
  -> review or correction
  -> actual receipt and usable result
```

A high success rate among appeals can coexist with a large invisible group that
never appealed. A replacement program can report approved claims while missing
unfiled or rejected losses. A worker remedy can be paid while the people who
cannot sustain the complaint route disappear from the record.

## Evidence across domains

| Route | What looks responsive | What the route still selects out |
|---|---|---|
| Medicare Advantage skilled-nursing authorization | 18% of reviewed denials were appealed and 95% of appealed denials were overturned. | The public record does not show who knew to appeal, could gather documentation, had time or health to wait, or received timely admission after reversal. |
| SNAP EBT theft | States reported more than $320 million in approved replacement claims for nearly 679,000 households. | Approved claims are not all theft; unfiled or denied losses, replacement delivery, interim food access, and next-month security are not linked to recipients. |
| Consumer redress | Some CFPB routes report checks cashed or later reissue payments. | A recipient may need to request reissue, and aggregate cashing does not show which account was corrected or whether the underlying obligation changed. |
| Worker remedies | The Atkins record reports payment to all ten named drivers after court-held funds were released. | Receipt does not show adequacy, residual loss, later work, recurrence, or whether workers had a realistic alternative before or after the remedy. |

These examples do not share a cause or denominator. They share an observation
problem: success is measured downstream of a contest route that itself requires
capacity.

## Digital control: a visible status is not complete control

The newer privacy and safety records add a distinct administrative route. They
make more of the middle observable—request intake, matching or identity
conditions, deadlines, per-request status, denial, and escalation—without
turning a status label into verified data control or restored safety.

| Route | Directly observed administrative stage | Boundary retained |
|---|---|---|
| California DROP | About 500,000 registrants, 654 brokers, a request-tracking route, broker-level statuses, a 45-day processing cycle, and status updates that may take up to 90 days; CalPrivacy reports 99.9% of registrants had a profile deleted by at least one broker and more than 40 brokers for a typical user | At-least-one-broker deletion is not all-broker deletion; broker matches, exemptions, not-found/pending statuses, re-collection, and durable privacy remain unobserved |
| Walmart CCPA metrics | Separate received/completed/denied request counts and median completion times: 1,962 of 3,199 reported deletion requests completed, 1,237 denied, with a 22-day median | Company-reported completion is not verified deletion of all relevant data, an adequate explanation, no reappearance, trust, or switching |
| GM/OnStar order and policy | Formal copy, deletion, opt-out, and some location-disable routes; stated request channels and a possible 45-day window, with model/year and safety exceptions | A formal route does not show request volume, identity-verification burden, actual deletion, residual collection, service trade-off, or mobility outcome |
| TAKE IT DOWN Act / Google Search | A 48-hour covered-platform obligation, duplicate-copy scope, traceability and federal escalation; Google reports simpler request/status and repeat-filtering features | A deadline, request number, or platform status does not establish valid-request completion, full de-indexing/removal elsewhere, recurrence prevention, survivor safety, or exit |

The DROP and Walmart records are especially useful because they prevent two
opposite mistakes. One is to call a request form a result; the other is to call
the absence of perfect public data proof that no control occurred. DROP reports
meaningful system reach and partial implementation surfaces, while Walmart
reports a visible completion/denial split. Neither source supplies a person-
level audit of downstream data, safety, or life after the request.

The digital route is therefore:

```text
discover a right or harm
  -> supply identifiers, identity proof, or a valid request
  -> matching, eligibility, exemption, or platform decision
  -> status, completion, denial, or escalation
  -> [open] verified deletion/removal, no recurrence, usable service alternative,
     safety, trust, switching, or exit
```

Sources: [DROP multi-broker deletion record](records/us-calprivacy-drop-data-broker-deletion-2026.json), [DROP status/contestability record](records/us-cppa-drop-status-contestability-2026.json), [Walmart privacy-request record](records/us-walmart-ccpa-privacy-request-completion-2025-2026.json), [GM/OnStar data-control record](records/us-ftc-gm-onstar-data-control-order-2026.json), [TAKE IT DOWN Act record](records/us-ftc-take-it-down-act-platform-removal-2026.json), and [Google image-removal record](records/us-google-search-explicit-image-removal-control-2026.json).

## Cultural and political meaning

This mechanism changes how non-use and silence should be interpreted. Failure
to appeal may mean satisfaction, but it may also mean no notice, low expected
value, fear, disability, language barriers, care obligations, lack of
documentation, or inability to wait. A successful appeal may strengthen trust
in contestability, but continued enrollment or continued use may instead show
dependence on a system with no safe substitute.

The atlas should therefore keep **contestability**, **correction**, and
**recovery** as separate stages. Do not treat appeal success as a population
correction rate, and do not treat non-appeal as acceptance.

## Minimum fields for a fair denominator

Future same-unit records should retain:

1. exposure and whether the affected unit knew about it;
2. eligibility, notice, language/accessibility, and available help;
3. appeal or complaint attempt, effort, time, documents, cost, and safety;
4. decision, reversal, denial, replacement, or reissue;
5. actual receipt, timing, adequacy, interim substitution, and continuity;
6. later trust, continued use, switching, non-use, or exit only when directly
   observed.

Until those fields exist, the strongest claim is bounded: the institution's
route can correct some contested cases, while the reach of contestability and
the durability of the correction remain unknown.

**Boundary:** this is a cross-domain measurement mechanism, not a claim that
Medicare, SNAP, consumer redress, worker remedies, and digital-control systems
have the same failure rate or social effect.
