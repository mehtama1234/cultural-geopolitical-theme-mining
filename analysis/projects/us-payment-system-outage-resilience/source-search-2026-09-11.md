# Source search: US payment-system outage resilience

**Search date:** 2026-09-11  
**Geography:** United States, with comparison evidence from Spain and Sweden  
**Status:** opening pass; payment resilience is measured, essential-needs effects remain open

## Working question

What can a household still buy when the payment network goes down?

## Opening source

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-NBER-PAYMENT-RESILIENCE | [On the Resilience of Payment Methods](https://www.nber.org/papers/w35115) | The study combines outage, weather, transaction, scanner and survey data. Spending rises before disasters as households stock up, often using credit; after outages, digital payments fall and cash use rises. Nearly half of surveyed consumers could not use their preferred electronic payment during an outage, while greater cash access reduced the decline in completed purchases. | NBER working paper | It does not show which households lost food, medicine, fuel or work access, or which payment design works best in every outage. |

## First pattern to test

```text
storm or infrastructure failure
  -> electronic payment unavailable
  -> cash, credit, offline tool, or no transaction
  -> essential purchase completed or missed
  -> household cost, health, work and recovery
```

The source supports payment failure and cash's backup role. It does not show the complete cost of a missed purchase for each household.

## Counterpoint to keep visible

Cash can help when networks fail, but it can be lost or stolen. Offline-capable digital tools may provide another form of backup, and a longer outage can defeat both payment methods through supply shortages.

## Main gaps

- outage length, location and network failure;
- cash access, bank access and merchant acceptance;
- food, medicine, fuel and other essential purchases;
- credit use and later repayment;
- lost work, care and health effects;
- differences by income, age, disability, race, place and broadband access.

## Decision rule

Keep payment availability, purchase completion, essential need and later household loss separate. A payment shift is not itself proof of hardship.
