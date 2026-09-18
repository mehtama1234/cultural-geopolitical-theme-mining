# CFPB named redress-route recheck: BrightSpeed, Navient, and ADSS

**Checked:** 2026-09-18  
**Status:** current official aggregate/administrator route; individual recovery open

## Current official status

The current CFPB payment-by-case pages were retrieved for three named routes.
BrightSpeed still reports 122,507 eligible consumers, $53,885,244 in
compensable harm, Epiq Systems as administrator, and **July 23, 2024 –
Ongoing: Distribution**. Navient still says affected consumers are receiving
a check, names Rust Consulting as administrator, and states that payments do
not change or reduce affected student loans; its route remains **February 13,
2026 – Ongoing**. American Debt Settlement Solutions (ADSS) reports that
eligible consumers received compensation through two distributions, **May 21,
2014 – December 9, 2015** and **March 4, 2016 – June 2, 2016**; the matter is
closed and payment/check reissue requests are no longer being honored.

These are current official statements about remedy design and distribution
status. Neither page publishes a recipient-level payment file, successful
delivery, amount received, returned payment, balance/credit correction,
remaining loss, trust, switching, or exit.

| Route | Current public stage | Explicit limit |
|---|---|---|
| BrightSpeed | Eligible class, aggregate compensable harm, administrator, ongoing distribution | Issuance, receipt, amount, residual loss, and later behavior are not published |
| Navient | Checks reported as being received by affected consumers; administrator and ongoing route | The page does not identify which consumers received checks, amounts, loan-level correction, remaining burden, or later choice |
| ADSS | Eligible consumers reported compensated; two dated distributions; closed matter | No person-level receipt file, payment amount distribution, remaining loss, or later behavior is published; reissue requests are closed |

The [machine recheck](data/cfpb-named-redress-route-recheck-2026-09-18.json)
preserves the retrieved-page hashes and the exact status boundary. This is a
source-vintage recheck, not a new distribution estimate.

## End-to-end implication

```text
alleged consumer harm
  -> enforcement and settlement
  -> administrator and payment route
  -> aggregate or reported distribution status
  -> [open] person-level issuance, receipt, correction, recovery, trust, or exit
```

The three routes sharpen an important distinction: BrightSpeed exposes an
ongoing class distribution without recipient outcomes, Navient reports checks
to affected consumers but explicitly leaves the underlying student-loan
obligation unchanged, and ADSS exposes a documented closed-distribution state
without a person-level outcome file. Compensation, obligation restoration, and
individual recovery remain separate stages.

## Reproduction and source

```text
curl -sS -L 'https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/brightspeed/' \
  -o /tmp/cfpb-brightspeed-2026-09-18.html
curl -sS -L 'https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/navient/' \
  -o /tmp/cfpb-navient-2026-09-18.html
curl -sS -L 'https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/american-debt-solutions/' \
  -o /tmp/cfpb-adss-2026-09-18.html
sha256sum /tmp/cfpb-brightspeed-2026-09-18.html /tmp/cfpb-navient-2026-09-18.html
sha256sum /tmp/cfpb-adss-2026-09-18.html
```

Primary sources: [BrightSpeed](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/brightspeed/),
[Navient](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/navient/),
[ADSS](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/american-debt-solutions/),
and the [CFPB payment-by-case index](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/).

No administrator file or recipient-level data was downloaded.
