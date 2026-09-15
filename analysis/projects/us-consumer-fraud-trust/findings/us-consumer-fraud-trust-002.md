# Reported scam losses rose into 2025, but the household recovery path remains unmeasured

**Status:** FTC administrative comparison with Federal Reserve household
context · **Checked:** 2026-09-14

## The bounded finding

The FTC's 2025 testimony to the Joint Economic Committee reports roughly 3
million consumer fraud reports and approximately $15.9 billion in reported
losses. More than 1 million reports concerned imposter fraud, with more than
$3.5 billion in reported losses; investment scams accounted for more than $7.9
billion. The prior 2024 Consumer Sentinel frame reported 2,600,678 fraud
reports and $12.54 billion in reported losses, with 38% of fraud reports
indicating a loss and a $497 median loss among reports with loss.

The comparison establishes a later and larger administrative loss frame. It
does not establish a population incidence trend, because the 2025 testimony
and 2024 Data Book have different presentation frames, contributor coverage,
category definitions, and reporting opportunities.

## What each source measures

| Source layer | Direct result | Denominator and boundary |
|---|---|---|
| FTC 2024 Consumer Sentinel | 2,600,678 fraud reports; $12.54B reported losses; 38% of fraud reports indicated a loss | Administrative reports, not all US consumers; reported loss is not verified loss or recovery |
| FTC 2025 testimony | About 3M reports; $15.9B reported losses; >1M imposter reports; >$3.5B imposter losses; >$7.9B investment-scam losses | Approximate/lower-bound testimony frame; category and coverage comparability to 2024 must be audited |
| Federal Reserve SHED 2024 | Household respondents report exposure, unrecovered money, recovery time, and route-conditioned burden | Weighted adult survey with self-reported conditional outcomes; not an account ledger or verified remedy record |
| CFPB complaint system | Published complaint routes and company-response categories | Published administrative endpoint; does not prove remedy, recovery, trust, or exit |

The FTC source is especially useful for category composition: investment and
imposter scams should not be collapsed into one “fraud” mechanism. The SHED
source supplies the missing household-side questions—whether money remained
unrecovered and how much recovery or consequence time was reported—but it does
not observe the FTC cases. The CFPB layer supplies an institutional contact
and response surface, but a complaint is not the same case as an FTC report or
a SHED respondent.

## The end-to-end interpretation

```text
scam or deceptive contact
  -> payment/account exposure
  -> reported loss
  -> unrecovered money and time cost
  -> dispute, provider decision, or public complaint
  -> verified recovery or continued loss
  -> trust, repeat use, switching, or exit
```

The FTC 2025 extension strengthens the first and third boxes at an
administrative aggregate level. The Federal Reserve strengthens the fourth
box from the household perspective. CFPB records describe one possible
institutional route. No source currently follows the same person or case
through every box.

The central program implication is that a rising reported-loss total can
signal increasing institutional exposure without telling us whether the
typical household lost money, whether the loss was recovered, which provider
controlled the remedy, or whether trust changed. Conversely, a household may
recover money after a costly and time-consuming process; recovery is not the
same as no harm.

## Counterevidence and limits

- Administrative reports are affected by awareness, reporting access,
  contributor coverage, category definitions, duplicate or multiple reports,
  and high-value cases.
- The 2025 testimony uses approximate and “more than” language. Those values
  should not be treated as exact point estimates or mechanically ratioed to the
  2024 Data Book.
- The 2024 age-conditioned loss figures show a useful incidence/severity
  counterexample: younger reported cases had a higher loss-reporting share,
  while older reported cases had a higher median loss. This is not an
  age-specific population-risk estimate.
- SHED outcomes are self-reported and conditional on the relevant fraud and
  account-involved universes. The public file does not establish provider
  liability, technical reversibility, or design-based uncertainty for this
  extraction.
- Neither FTC nor SHED establishes generalized distrust, political action,
  consumer exit, or platform causation.

## What this adds to the atlas

This finding makes the consumer-recourse chain more precise:

1. retain FTC totals and categories as a surveillance/reporting frame;
2. retain SHED as a household burden and recovery-time frame;
3. use CFPB and provider records to observe contact, response, and remedy;
4. construct a same-case ledger with incident date, payment rail, amount,
   notice, contact effort, provider decision, reversal, time cost, and later
   account use; and
5. test whether burden and remedy differ by age, income, disability, digital
   access, payment route, and firm type.

The next test could weaken the proposed mechanism if reported-loss growth is
mostly a reporting or category change, if verified recovery is common despite
high effort, or if trust and account use remain stable after remedy. Those are
empirical alternatives, not rhetorical caveats.

## Sources and reproduction

- [FTC 2025 extension record](../../../records/us-ftc-consumer-sentinel-2025-extension.json)
- [FTC 2025 testimony on the rising scam economy](https://www.ftc.gov/system/files/ftc_gov/pdf/ftc-testimony-jec-hearing-on-the-rising-scam-economy.pdf)
- [FTC 2024 Consumer Sentinel record](../../../records/us-ftc-consumer-sentinel-fraud-loss-2023-2024.json)
- [Machine-readable SHED annual fraud comparison record](../../../records/us-shed-fraud-annual-comparison-2024-2025.json)
- [Federal Reserve household fraud and recovery layer](../federal-reserve-household-fraud-recovery-layer-v1.md)
- [Fraud recovery subgroup finding](us-consumer-fraud-trust-001.md)
- [CFPB response-route layer](../cfpb-response-route-layer-v1.md)

**Evidence status:** administrative reported-loss comparison plus weighted
household-survey context; no population incidence, verified recovery,
same-case remedy, trust, or exit estimate.
