# CFPB named redress-route recheck: BrightSpeed and Navient

**Checked:** 2026-09-18  
**Status:** current official aggregate/administrator route; individual recovery open

## Current official status

The current CFPB payment-by-case pages were retrieved for two named routes.
BrightSpeed still reports 122,507 eligible consumers, $53,885,244 in
compensable harm, Epiq Systems as administrator, and **July 23, 2024 –
Ongoing: Distribution**. Navient still says affected consumers are receiving
a check, names Rust Consulting as administrator, and states that payments do
not change or reduce affected student loans; its route remains **February 13,
2026 – Ongoing**.

These are current official statements about remedy design and distribution
status. Neither page publishes a recipient-level payment file, successful
delivery, amount received, returned payment, balance/credit correction,
remaining loss, trust, switching, or exit.

| Route | Current public stage | Explicit limit |
|---|---|---|
| BrightSpeed | Eligible class, aggregate compensable harm, administrator, ongoing distribution | Issuance, receipt, amount, residual loss, and later behavior are not published |
| Navient | Checks reported as being received by affected consumers; administrator and ongoing route | The page does not identify which consumers received checks, amounts, loan-level correction, remaining burden, or later choice |

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

The paired routes sharpen an important distinction: BrightSpeed exposes an
ongoing class distribution without recipient outcomes, while Navient reports
checks to affected consumers but explicitly leaves the underlying student-loan
obligation unchanged. Compensation and restoration remain separate stages.

## Reproduction and source

```text
curl -sS -L 'https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/brightspeed/' \
  -o /tmp/cfpb-brightspeed-2026-09-18.html
curl -sS -L 'https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/navient/' \
  -o /tmp/cfpb-navient-2026-09-18.html
sha256sum /tmp/cfpb-brightspeed-2026-09-18.html /tmp/cfpb-navient-2026-09-18.html
```

Primary sources: [BrightSpeed](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/brightspeed/),
[Navient](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/navient/),
and the [CFPB payment-by-case index](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/).

No administrator file or recipient-level data was downloaded.
