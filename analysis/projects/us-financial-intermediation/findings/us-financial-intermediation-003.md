# Finding 003: Formal bank access coexists with unequal substitution and limited reported switching after fraud

**Status:** provisional 2025 SHED financial-power finding · **Checked:** 2026-09-17

## The bounded finding

The Federal Reserve's 2025 household survey shows that formal banking access,
alternative payment routes, fraud recovery, and provider switching are
different stages of financial power. Six percent of adults were unbanked, but
the rate was 21% below $25,000 of family income versus 1% at $100,000 or more.
Among unbanked adults, 28% used a nonbank check-cashing or money-order route,
versus 11% among banked adults. Among adults experiencing non-credit-card
fraud, 35% reported that some money was not recovered, 67% contacted a
financial provider, and 12% changed banks or financial companies.

This supports a narrower trend than “banking access is failing” or “digital
access solves inclusion”:

> A formal account can be widely available while the practical route through
> which people transact, absorb fraud, recover money, and leave a provider
> remains uneven and only partly visible.

## What the source reports

| Stage | 2025 published measure | Safe interpretation |
|---|---:|---|
| Formal doorway | 6% unbanked overall; 21% below $25,000 versus 1% at $100,000+ | Account ownership is strongly income-patterned; it is not liquidity or usable control |
| Account friction | 12% of banked adults paid an overdraft fee; 17% among banked adults below $25,000 | A formal account can carry short-term cost; this is not a causal fee or hardship estimate |
| Alternative route | 28% of unbanked adults used nonbank check-cashing or money orders versus 11% of banked adults | Substitution is visible, but price, convenience, reliability, and necessity are not |
| Loss and recovery | Among non-credit-card fraud cases, 65% lost money and 35% did not recover some money; median loss before recovery was $500 and after recovery $30 | Recovery is materially incomplete for a reported subgroup; payment method and provider responsibility remain unresolved |
| Provider response | 67% contacted a bank or financial company; 38% reported to an authority, credit bureau, or consumer-complaint agency | Contact and reporting are visible response channels, not verified resolution |
| Switching | 12% changed banks or financial companies after non-credit-card fraud | Reported switching is an endpoint, but its reason, alternative quality, cost, and protection are unobserved |

The source also reports that cryptocurrency transaction use was 6% among
unbanked adults versus 2% among banked adults, while overall cryptocurrency
use for any purpose was 10%. This is a useful counterexample to treating
cryptocurrency use as a general replacement for banking: transaction use
remained a small minority behavior, and the reasons included recipient
preference, speed, privacy, and cost.

## Mechanism map

```text
income / identity / account access
  -> bank, nonbank, or digital payment route
  -> overdraft, fraud, or loss exposure
  -> provider contact, reporting, recovery, or residual loss
  -> stay, switch, or continued use
  -> financial room, trust, and practical exit
```

The 2025 SHED page directly measures the first four surfaces and reports a
switching outcome. It does not follow one person from account access through a
dated transaction, recovery, provider decision, and later use. The record
therefore strengthens the financial-access and consumer-recourse layers but
does not close the same-account end-to-end arrow.

## Boundaries and counterexamples

- Unbanked status includes the respondent and spouse/partner account frame; it
  is not a person-level denial or a measure of whether cash was preferred.
- Nonbank use may be convenient or chosen for a specific transaction; it is not
  automatically exclusion, exploitation, or an inferior substitute.
- An overdraft fee may reflect a temporary timing mismatch, and the survey does
  not show the fee amount, repeat frequency, or whether an alternative account
  was available.
- Fraud losses and recovery are self-reported around the most recent incident;
  multiple payment methods can be selected, and the source does not identify
  provider liability or dispute success.
- Contacting a provider can recover funds without switching. Not switching can
  mean satisfaction, inertia, wage/benefit lock-in, lack of alternatives, or a
  different response; the 12% should not be read as a switching rate for all
  bank customers.

## Next test

The decisive next artifact is a small, lawful account- or case-linked ledger
that preserves: starting provider/product; dated loss or fraud; payment rail;
notice and contact attempts; correction or refund; amount and timing recovered;
replacement route; continued use; closure or switching; and the reason for
staying or leaving. Retain non-reporters and unsuccessful exits where the
denominator permits. Until that exists, the current result remains a
population-level access/substitution/recourse comparison, not a verified
consumer-recovery or trust result.

## Sources

- [Federal Reserve, Banking in the 2025 SHED report](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-banking.htm)
- [Machine-readable observation record](../../../records/us-federal-reserve-banking-substitution-recourse-2025.json)
- [Financial-access route and recourse synthesis](../financial-access-route-recourse-public-capacity-synthesis-v1.md)

**Evidence status:** official 2025 SHED published estimates; reported and
compared population surfaces. No causal account effect, verified recovery,
trust change, or practical-exit claim is made.
