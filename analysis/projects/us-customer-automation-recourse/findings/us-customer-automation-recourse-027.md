# Finding 027: Digital-health convenience can combine sensitive-data exposure with recurring-billing exit friction

**Status:** provisional named U.S. digital-health consumer-power finding · **Checked:** 2026-09-17

## The bounded finding

The Federal Trade Commission, Utah, and California sued Hims & Hers in July
2026, alleging that the online telehealth company shared consumers' health
information with advertising platforms despite privacy assurances and enrolled
many consumers in prescription subscriptions shortly after intake without
clearly disclosing the timing. The complaint also describes refill deadlines
and cancellation routes that could make avoiding a later charge more difficult.

The accompanying FTC FOIA release contains 203 coded consumer-complaint records
from June through September 2025. Fifty were labeled `RESOLVED`, 128
`ANSWERED`, four `ADMIN JUDGED INVALID`, and 21 had no usable disposition. The
release is heavily concentrated in one BBB channel: 196 records were attributed
to BBB CA Oakland, and all nonblank disposition labels occurred in that channel.

The safe interpretation is:

> A digital-health service can put privacy, treatment access, recurring payment,
> and cancellation on one consumer pathway. A complaint response or pending
> lawsuit makes institutional handling visible, but does not establish the
> prevalence of exposure, unauthorized payment, medical harm, treatment
> interruption, privacy loss, or restored practical exit.

## Event chain

```text
online intake and treatment route
  -> alleged health-data sharing and subscription enrollment
  -> refill deadline / cancellation effort / possible charge
  -> complaint or enforcement route
  -> administrative disposition or pending litigation
  -> [open] refund, data correction/deletion, treatment continuity, trust, and exit
```

## What the public record supplies

| Stage | Observed or reported case evidence | Still open |
|---|---|---|
| Institutional action | FTC, Utah, and California complaint filed July 29, 2026; case was pending at the September 17 check | Final adjudication, settlement, or company compliance finding |
| Alleged privacy mechanism | Complaint alleges sharing of health information with advertising platforms including Meta and Snap despite privacy representations | Account-level exposure, notice, consent, deletion, downstream targeting, or privacy loss |
| Alleged billing and exit mechanism | Complaint describes prescription-subscription enrollment, refill timing, short cancellation deadlines, and multi-step cancellation | Charge incidence, cancellation completion, refund, treatment interruption, or alternative access |
| Complaint visibility | FTC FOIA workbook contains 203 released records; 50 are labeled resolved and 128 answered | Representative customer denominator, underlying allegation, verified remedy, and durable firm change |
| Channel conditioning | 196 records came from BBB CA Oakland; the other seven came from FTC/BBB/blank source fields and had blank dispositions | Whether missing labels reflect pipeline differences, incomplete release, or different outcomes |

The complaint workbook is a selected administrative release, not a customer
sample. Its labels describe complaint handling and do not verify medical,
financial, privacy, or treatment outcomes.

## Why it matters to the broader atlas

This case adds a consumer-power boundary that is not captured by account access
or nominal telehealth availability alone. The service may reduce travel or
appointment friction for some patients while shifting control into disclosure,
refill, payment, and cancellation interfaces. Those interfaces can affect
time, money, sensitive information, treatment continuity, and the ability to
switch, but the public record does not join those stages at the individual
level.

Keep the following states separate:

```text
privacy representation != measured data exposure
subscription enrollment != unauthorized payment
complaint disposition != verified remedy
refund or cancellation != restored treatment continuity
continued use or non-use != unconstrained choice
```

## Next decisive test

The smallest useful follow-up is a lawful, privacy-minimized episode ledger
with notice, consent, intake, refill, charge, cancellation attempt, data-use
request, complaint, correction/refund, treatment continuity, and later trust or
switching. Preserve users who did not complain and complaints without a
disposition; do not convert the 203-record release into a rate for all Hims
customers.

## Sources and storage boundary

- [FTC Hims & Hers enforcement announcement](https://www.ftc.gov/news-events/news/press-releases/2026/07/ftc-states-act-against-hims-hers-deceptive-unlawful-privacy-practices)
- [FTC and states' redacted complaint](https://www.ftc.gov/system/files/ftc_gov/pdf/Hims-Complaint-Redacted-E-Filed.pdf)
- [FTC Hims & Hers case record](https://www.ftc.gov/legal-library/browse/cases-proceedings/hims-hers)
- [FTC FOIA release page](https://www.ftc.gov/legal-library/browse/frequently-requested-foia-records/hims-hers/foia-2025-02172-him-hers-consumer-complaints)
- [Released complaint workbook](https://www.ftc.gov/system/files/ftc_gov/documents/2025-02172him-hers-consumer-complaints.xlsx)
- [Structured source record](../../../records/us-ftc-hims-hers-health-data-billing-cancellation-2026.json)

The analysis retains coded non-text fields from the workbook only; names,
addresses, contact fields, narrative comments, and other personal data were not
retained.
