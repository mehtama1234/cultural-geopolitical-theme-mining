# Finding 032: A repeat refund can confirm prior receipt without proving later recovery

**Status:** bounded recipient-conditioned consumer-remedy finding · **Checked:** 2026-09-19

## The bounded finding

The FTC reports that the ACRO Services debt-relief scheme first sent more than
$3.8 million in refunds in January 2025. Because money remained in the fund,
the FTC then sent **5,685 checks totaling more than $6.2 million** to people
who had accepted the first payment.

This is a stronger endpoint than an announced fund or an aggregate amount
issued: the second distribution is explicitly conditioned on prior acceptance
of the first payment. It still does not establish that the second check was
cashed, that the original credit-card debt or account position was corrected,
or that the household recovered financially.

## The chain

```text
debt-relief deception and upfront fees
  -> first refund accepted
  -> second refund sent to prior recipients
  -> [open] second-check cashing, debt/account correction, residual burden,
     trust, switching, or exit
```

The episode sharpens a useful distinction: prior receipt is evidence about one
remedy stage, not evidence that the underlying harm was repaired. A later
payment can recognize earlier reach while leaving the original debt, credit,
and financial-security problem unresolved.

## Limits and next field

- The FTC reports checks sent, not checks cashed or individual amounts.
- The second-payment denominator is recipient-conditioned and cannot be read
  as the full harmed population or a recovery rate.
- The public page does not report debt balances, account correction, residual
  fees, household adaptation, trust, switching, or exit.

The next decisive record is an authorized claimant/payment follow-up joining
first and second payment status to debt or account correction and later
financial behavior.

Source: [FTC ACRO Services refund page](https://www.ftc.gov/enforcement/refunds/acro-services-refunds).

The [structured event ledger](../data/ftc-acro-second-refund-event-ledger-v1.json)
preserves the recipient-conditioned denominator and open downstream stages.
