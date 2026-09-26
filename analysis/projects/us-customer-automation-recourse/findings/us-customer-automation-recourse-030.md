# Finding 030: Consumer redress can be measured at the cashing stage without proving recovery

**Status:** bounded aggregate consumer-remedy follow-up · **Checked:** 2026-09-19

## The bounded finding

The CFPB's FY2024 Financial Report gives a stronger remedy-stage measure than
an ongoing payment announcement. For three completed Bureau-administered
distributions, it reports checks mailed and the percentage of distributed funds
cashed: Premier Student Loan Center, $19.975 million and 17,099 checks with
69% of funds cashed; U.S. Equity Advantage, $900,000 and 11,785 checks with
86% cashed; and SMART Payment Plan, $1.5 million and 18,750 checks with 88%
cashed.

This establishes aggregate payment use, not individual recovery. It does not
show whether a particular person's account was corrected, whether the money
was adequate, whether residual loss remained, or whether the consumer stayed,
switched, trusted the institution, or exited.

## The chain

```text
consumer financial harm
  -> CFPB redress allocation
  -> checks mailed
  -> some distributed funds cashed
  -> account correction, adequate recovery, trust, switching, or exit [open]
```

The important insight is that “payment sent,” “payment cashed,” and “harm
repaired” are separate clocks. The cashing rate closes one administrative
stage while leaving the lived consumer outcome unresolved.

## Limits and next field

- The rates are aggregate percentages of distributed funds, not percentages of
  consumers fully recovered.
- The report does not provide recipient identifiers, individual amounts,
  account correction, residual loss, or later behavior.
- These are completed distribution cases, but no same-consumer follow-up is
  available.
- The next decisive test is a lawful recipient/account-linked record with
  payment receipt, account correction, later burden, and continued use or
  switching.

The [CFPB redress ledger](../data/cfpb-named-redress-route-event-ledger-v1.json)
now keeps ongoing, closed, and completed-with-cashing-rate routes distinct.
Source: [CFPB Financial Report FY2024, Tables 17–18](https://files.consumerfinance.gov/f/documents/cfpb_financial-report-fy-2024.pdf).
