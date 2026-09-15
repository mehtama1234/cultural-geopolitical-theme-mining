# Project: US consumer fraud, recovery, and trust

## Question

When a consumer loses money through a scam or payment fraud, who carries the loss, who can recover it, and what happens to trust in the firm or public system involved?

## Short first pass

Use the Federal Reserve for household exposure and unrecovered losses, the FTC for reported categories and payment routes, and CFPB complaint records for the response after a problem. Separate credit-card fraud protections from direct bank-transfer or investment losses.

## Matched evidence pass

- [The loss is only the first part of a fraud victim's experience](../../findings/us-consumer-fraud-trust-matched-evidence-001.md)
- [Reader-friendly HTML](../../../site/us-consumer-fraud-trust-matched-evidence-001.html)

The [FTC Consumer Sentinel 2024 layer](ftc-consumer-sentinel-2024-layer-v1.md)
adds a time-ordered administrative report comparison: fraud report volume,
reported loss incidence, dollar loss, payment/contact channels, and age-split
loss incidence versus severity. It is not a survey, prevalence estimate,
verified recovery measure, or same-case trust outcome. Its [trend record](../../records/us-ftc-consumer-sentinel-fraud-loss-2023-2024.json)
enters the shared atlas.

The [Federal Reserve household fraud and recovery layer](federal-reserve-household-fraud-recovery-layer-v1.md)
adds a weighted 2024 household-survey view of exposure, direct loss,
unrecovered money, and recovery time. It complements the FTC administrative
report frame and CFPB response-route frame without sharing their denominators.
The [SHED fraud subgroup layer](shed-fraud-subgroup-layer-v1.md) maps the
codebook variables to age, income, and account-route outcomes. It finds a
nonmonotonic income pattern in unrecovered money and higher descriptive burden
in P2P account cases, while keeping small cells, selection, and missing digital
access/disability measures explicit.

The [SHED annual fraud comparison](shed-fraud-annual-comparison-layer-v1.md)
repeats the age and income definitions in the 2025 public file. The income
pattern remains nonmonotonic, but the age ordering changes between annual
samples; this weakens a simple age trend claim and keeps annual composition and
reporting differences visible.

The detailed [fraud recovery burden finding](findings/us-consumer-fraud-trust-001.md)
now surfaces the subgroup result as a reader-facing memo. It keeps adult
exposure, conditional unrecovered money, recovery time, and P2P route cells
separate; the next missing stage remains a case-level provider response and
verified recovery record.

The [FTC 2025 extension](ftc-consumer-sentinel-2025-extension-v1.md) adds a
later administrative comparison from official congressional testimony: roughly
3 million fraud reports and $15.9B in reported losses, with imposter and
investment scams separated as distinct categories. It extends the reporting
series, not household prevalence or recovery.

The [2025 reported-loss and recovery-path finding](findings/us-consumer-fraud-trust-002.md)
puts that extension beside the 2024 FTC baseline, Federal Reserve household
recovery measures, and CFPB response routes. It keeps reported scale,
household burden, provider remedy, trust, and exit as separate stages.

## Possible connection

Fraud joins the service and credit paths at the moment a person needs an answer, reversal or human decision. It can turn a private loss into a public question about whether the payment system, bank, platform or government can protect ordinary users.

## Decision rule

Move on after one household loss measure, one reported market trend, one recovery or complaint measure, and a counterpoint about under-reporting or protection differences.
