# Finding 019: Benefit issuance can fail as usable protection when control is stolen

**Status:** bounded SNAP EBT control-and-recovery finding · **Checked:** 2026-09-19

## The bounded finding

SNAP is designed to supplement household income for food purchases, but an
issued benefit is not the same thing as usable food security. GAO reports that
thieves can use skimming, cloned cards, phishing, algorithmic attacks, or
unauthorized terminals to take control of an EBT account. The result can be a
recipient with an active benefit balance but no ability to use it for food.

For the statutory replacement period from October 1, 2022 through December
20, 2024, states reported replacing more than $320 million in stolen benefits
for nearly 679,000 households. GAO warns that this understates theft: the data
include only approved claims, some recipients may not know how to file, and
claimants were limited to two claims per year. The public record therefore
shows a large, institutionally recognized loss of control, not the full number
of affected households or the share that regained food security.

The protection design also shifts work onto recipients. Many available
controls require the recipient to lock a card, change a PIN, monitor an
account, or report an unauthorized transaction. EBT cards historically lacked
the same federal liability protections that apply to ordinary debit cards.
USDA and states have been developing chip cards, mobile-payment pilots,
transaction blocking, real-time monitoring, and other controls, but GAO's
review did not establish that a particular affected household received a
replacement quickly enough, avoided a food gap, or trusted the system again.

## The chain

```text
SNAP eligibility and benefit issuance
  -> EBT account/card exposure
  -> theft or unauthorized transaction
  -> loss of food-purchasing control and possible emergency substitution
  -> claim, replacement, lock/PIN change, or non-use
  -> account-security reform and state/USDA monitoring
  -> restored balance, food access, and next-month stability [open]
  -> trust, reporting, switching, political judgment, or exit [open]
```

This adds a distinct public-system mechanism to the atlas: **formal receipt can
coexist with practical dispossession**. It also shows that fraud prevention is
not only a technical question. A control that blocks suspicious transactions
may protect benefits while adding steps or false positives for recipients who
need to use the account across state lines, online, or through accessible
channels.

## What is and is not observed

| Stage | Evidence status |
|---|---|
| Program scale and intended use | SNAP was expected to provide about $96 billion to roughly 43 million people in FY2025. |
| Exposure and loss of control | GAO documents multiple theft methods and reports more than $320 million in approved replacement claims for nearly 679,000 households during the covered period. |
| Institutional response | Replacement authority existed for the covered period; USDA and states pursued card modernization, recipient controls, pilots, and monitoring. |
| Individual recovery | Not observed: claim filing time, replacement receipt, food gap, substitute borrowing/charity, next benefit, or durable security. |
| Meaning and action | Not observed: trust change, reporting choice, switching behavior, political response, or exit. |

## Limits and next field

- The replacement figures are not a prevalence estimate because they exclude
  unknown theft, unfiled claims, denied claims, and theft outside the covered
  statutory period.
- The data do not identify a common household timeline from theft to claim,
  replacement, food hardship, and later stability.
- The record cannot tell whether recipient-facing controls were usable,
  affordable in time, accessible, or safe for a particular person.
- The next decisive evidence is a privacy-approved, same-episode case route
  with transaction date, theft report, claim decision, replacement date and
  amount, interim food or cash substitute, next-month balance, and later trust
  or continued use.

Source: [GAO-25-107964](https://www.gao.gov/products/gao-25-107964), especially
the report's discussion of approved replacement claims, recipient controls,
and the limits of the theft data.
