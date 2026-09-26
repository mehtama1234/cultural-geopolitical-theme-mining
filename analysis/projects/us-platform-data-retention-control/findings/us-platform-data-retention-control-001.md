# Finding 001: A deletion request can exist while practical data control remains uncertain

**Status:** bounded platform-data finding · **Checked:** 2026-09-22

## The bounded finding

The FTC's 6(b) staff report reviewed nine large social-media and video-streaming
companies. It found that companies collected and could indefinitely retain
large amounts of data, including information about users and non-users; shared
data broadly; and used privacy, minimization, and retention controls that the
FTC described as inadequate. Some companies did not delete all user data after
deletion requests and retained data under legal, trust-and-safety, or business
exceptions.

The route is:

```text
platform use or observation
  -> collection and inference
  -> sharing and retention
  -> user request or privacy setting
  -> actual deletion, reduced exposure, safety, trust, or exit [open]
```

## What this adds to the broad atlas

This adds a platform-control subtheme:

> Making a privacy action visible does not prove that the underlying data,
> copies, inferences, or downstream access were actually controlled.

It sharpens the difference between formal control and practical agency. A user
can receive a button, policy, or request route while the company retains data
for multiple purposes or cannot show complete deletion.

## Limits and next test

- The report covers nine companies and their responses to FTC information
  demands; it is not a census of platforms or users.
- It does not follow one person's request through every copy, inference,
  affiliate, broker, or downstream recipient.
- Retention exceptions can be lawful or safety-related; their existence does
  not prove misuse in every case.
- The study does not measure a user-level harm rate, behavior change, trust,
  or exit.

The next decisive artifact is a privacy-protected deletion ledger linking a
request to confirmation, data categories, copies, retention exceptions,
downstream recipients, reappearance, and later user action. Until then, the
safe claim is about structural control limits, not universal deletion failure.

## Sources

- [FTC staff report announcement](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-staff-report-finds-large-social-media-video-streaming-companies-have-engaged-vast-surveillance)
- [FTC social-media 6(b) report](https://www.ftc.gov/system/files/ftc_gov/pdf/Social-Media-6b-Report-9-11-2024.pdf)
- [FTC privacy and security enforcement](https://www.ftc.gov/news-events/topics/protecting-consumer-privacy-security/privacy-security-enforcement)

**Evidence status:** official company-response review shows structural collection,
sharing, retention, and deletion-control gaps; user-level deletion, harm,
safety, trust, and exit remain unmeasured here.
