# Finding 001: A retailer can report request completion without proving complete data control

**Status:** bounded platform-control and consumer-recourse finding · **Checked:** 2026-09-22

## The finding in plain language

Walmart's California privacy metrics make the administrative route visible. For 2025, Walmart reported:

- 1,914 access requests: 1,588 completed and 326 denied;
- 3,199 deletion requests: 1,962 completed and 1,237 denied;
- 17,367 sale-opt-out requests: 17,276 completed and 91 denied.

The reported median completion time was 42 days for access requests and 22 days for deletion requests. These are company-reported request rows, not unique people, and the action types cannot be pooled into one completion rate.

The useful distinction is that access, deletion, and sale opt-out are different forms of control. A completed sale opt-out does not mean that data was deleted. A completed deletion request does not by itself prove that every copy was removed, that an exemption was not applied elsewhere, or that the data will not be collected again.

```text
consumer request
  -> identity or authorization check
  -> completed, denied, or delayed
  -> [open] complete deletion, residual exposure, re-collection, appeal, trust, or exit
```

## What this adds to the broader atlas

This is a concrete platform version of the recurring pattern:

> A formal route can produce a visible administrative completion while practical control remains partly unverified.

It adds more than a privacy policy announcement because the company reports request volumes, completions, denials, and timing. But the result is still an administrative endpoint, not a person-level privacy outcome.

The denial share is also not automatically evidence of institutional failure. Verification, legal exemptions, duplicate requests, authorization, or the scope of the requested action may explain some denials. The source does not provide enough detail to separate those mechanisms.

## What the source does not show

- The request rows are not a unique-person denominator.
- Company-reported completion does not verify that all copies or downstream records were removed.
- The metrics do not show denial reasons, appeals, re-collection, or consumer understanding.
- Access, deletion, and sale opt-out are different actions with different meanings.
- The source does not measure trust, switching, wellbeing, discrimination, or durable privacy.

## Next decisive test

Obtain a privacy-protected request ledger that follows one request from submission through identity verification, denial reason or completion, downstream deletion, re-collection, appeal, and later consumer behavior. Compare firms only when definitions and denominators match.

## Sources

- [Walmart California privacy metrics](https://corporate.walmart.com/privacy-security/california-privacy-rights/metrics)
- [Machine-readable source record](../../../records/us-walmart-ccpa-privacy-request-completion-2025-2026.json)

**Evidence status:** Walmart reports administrative request stages and timing; individual deletion, residual exposure, and lived consumer control remain open.
