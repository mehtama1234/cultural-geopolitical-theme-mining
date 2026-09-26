# Finding 018: Platform privacy controls can exist while practical data control remains uncertain

**Status:** bounded platform-governance and data-control finding · **Checked:** 2026-09-22

## The finding in plain language

An FTC Section 6(b) review of nine large social-media and video-streaming companies found that platforms collected information about users and non-users, shared data broadly with affiliates and third parties, and could retain large amounts of data indefinitely. The FTC also reported that some companies did not delete all user data after deletion requests.

This does not mean every platform failed every request. The review is a company-practice assessment, not a user-level deletion rate. But it shows why a published privacy route or completed request is not enough to establish durable control over personal information.

```text
platform collection
  -> retention and sharing across systems
  -> privacy request or deletion attempt
  -> partial deletion, exception, or continued retention
  -> [open] residual exposure, harm, trust, switching, or exit
```

## What this adds to the broader atlas

This is the system-level counterweight to the Walmart and GM/OnStar findings. Those records show named administrative routes and formal completion or control surfaces. The FTC review shows the wider governance problem underneath them: data may move through affiliates, third parties, inferences, and retention systems that a person cannot easily see or verify.

The broader pattern is:

> A visible request route can improve contestability without proving that the underlying data system has become controllable.

The source also expands the affected population beyond account holders. Non-users can be observed or included in platform data practices, so “user control” does not cover everyone exposed to the system.

## What the source does not show

- It covers nine companies responding to FTC information requests, not every platform or user.
- It does not provide a user-level deletion-failure rate or prove that every request failed.
- Reported retention and sharing practices do not by themselves establish individual harm.
- Legal, security, and trust-and-safety retention exceptions may be legitimate in some cases.
- The review does not measure trust, switching, wellbeing, political effects, or durable exit.

## Next decisive test

Compare a named request from submission through identity verification, deletion across affiliates and vendors, re-collection, appeal, and later user or non-user exposure. The denominator must include failed, exempted, and unobserved requests.

## Source

- [FTC Section 6(b) social-media report](https://www.ftc.gov/system/files/ftc_gov/pdf/Social-Media-6b-Report-9-11-2024.pdf)
- [Machine-readable source record](../../../records/us-ftc-social-media-data-retention-control-2024.json)

**Evidence status:** FTC reports platform-level collection, sharing, retention, and deletion-practice concerns; user-level completion, residual exposure, harm, and exit remain open.
