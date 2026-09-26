# Finding 031: Redress systems persist after distribution, but reachability remains part of the harm

**Status:** bounded consumer-remedy persistence follow-up · **Checked:** 2026-09-19

## The bounded finding

The CFPB's FY2025 Civil Penalty Fund and Bureau-Administered Redress Annual
Report follows three distributions already recorded in the atlas. It reports
$20,809 in direct payments to consumers who requested reissued Premier Student
Loan Center payments, and later redistributions of $129,729 for U.S. Equity
Advantage and $174,178 for SMART Payment Plan.

This adds a genuine later stage: the remedy system did not simply close when
the first distribution ended. Unclaimed or unresolved funds triggered reissue
or redistribution. But the report still does not reveal which people received
the later money, how long they waited, whether their accounts were corrected,
or whether the payment restored financial security.

## The chain

```text
consumer harm
  -> initial distribution
  -> some funds cashed / some funds unclaimed
  -> reissue or redistribution
  -> individual receipt, account correction, adequate recovery,
     trust, switching, or exit [open]
```

The deeper consumer insight is that administrative reachability is itself part
of the remedy. A fund can exist and be redistributed, yet the person still has
to be locatable, eligible, informed, and able to complete the payment route.

## Limits and next field

- The report gives aggregate amounts, not recipient-level receipt or timing.
- “Redistributed” does not establish that the same people harmed by the
  original conduct received adequate compensation.
- No account correction, remaining loss, continued use, switching, trust, or
  exit outcome is reported.
- The next decisive record is an authorized recipient/account follow-up that
  joins reissue effort, receipt, correction, and later financial behavior.

The [CFPB redress ledger](../data/cfpb-named-redress-route-event-ledger-v1.json)
now separates initial distribution, aggregate cashing, and later reissue or
redistribution. Source: [CFPB Civil Penalty Fund and Bureau-Administered
Redress Annual Report FY2025](https://files.consumerfinance.gov/f/documents/cfpb_fy2025-cpf-bar-annual-report_2026-03.pdf).
