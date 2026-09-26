# Source search: platform data retention and practical control

**Search date:** 2026-09-22  
**Geography:** United States; nine large social-media and video-streaming companies  
**Status:** bounded pass complete; visible privacy controls do not prove practical data control

## Working question

What did the FTC's 6(b) study find about how major platforms collect, share,
retain, and delete data?

## Opening source

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-FTC-SOCIAL-6B-2024 | [FTC staff report on social-media and video-streaming companies](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-staff-report-finds-large-social-media-video-streaming-companies-have-engaged-vast-surveillance) | Reviews responses from nine companies about data collection, sharing, retention, privacy controls, and treatment of users and non-users. | Official FTC 6(b) study | It is a company-practice review, not a same-person deletion audit or an estimate of every platform's prevalence. |

## First pattern

```text
platform encounter or data collection
  -> profiling, sharing, retention, or inference
  -> privacy request or setting
  -> actual deletion, reduced exposure, safety, trust, or exit [open]
```

The FTC reported that the companies collected and could indefinitely retain
large amounts of data about users and non-users, shared data broadly, and had
privacy controls and data-minimization practices that were inadequate. Some
companies did not delete all user data after a deletion request, and retained
data under legal, trust-and-safety, or business exceptions.

## Counterpoint to keep visible

The study did not audit every company or independently inspect every database.
Retention can sometimes serve legal, security, or safety purposes. A reported
exception is not proof that every deletion request failed, and a policy gap is
not the same as a verified harm to one person.

## Decision rule

Use the FTC study for platform-system practices and control boundaries. Do not
turn it into a prevalence estimate, a same-person privacy-loss rate, or proof
that a particular user could not obtain deletion or safety.
