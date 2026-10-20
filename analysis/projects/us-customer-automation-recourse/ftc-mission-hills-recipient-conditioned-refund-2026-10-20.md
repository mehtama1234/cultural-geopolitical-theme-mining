# Mission Hills: recipient-conditioned second refund still stops before debt correction

**Checked:** 2026-10-20  
**Record:** [US FTC Mission Hills repeat refund](../../records/us-ftc-mission-hills-repeat-refund-2026.json)

## What the current official page adds

The FTC reports that its first March 2024 payment round produced more than
$3.4 million in refunds. In February 2026 it announced a second round of
10,138 checks totaling more than $627,000 for people who both cashed the first
check and paid the defendants more than $430. The page says recipients should
cash the new check within 90 days.

This is a stronger reachability signal than a general payment offer because the
second-round population is conditioned on prior cashing. It is still a dispatch
measure, not evidence that the second check arrived, was cashed, or corrected
the underlying student-loan balance.

## End-to-end boundary

```text
debt-relief fee and false promise
  -> enforcement and first refund
  -> first-check cashing + payment threshold
  -> second-check dispatch
  -> [open] second receipt/cashing, balance correction, adequacy, household recovery, trust, exit
```

The public route does not expose the complete harmed denominator, failed
delivery or reissue, individual payment, remaining debt, or borrower-level
financial recovery. The new record therefore advances the remedy stage while
preserving the boundary between reachability and durable recovery.

## Source

- [FTC Mission Hills Federal refunds](https://www.ftc.gov/enforcement/refunds/mission-hills-federal-refunds)
- [How the FTC provides refunds](https://www.ftc.gov/enforcement/ftc-refund-programs/how-ftc-provides-refunds)
