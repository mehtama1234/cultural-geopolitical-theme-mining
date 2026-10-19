# Digital payment adoption, fraud recovery, and practical-exit audit

**Status:** active depth artifact; cross-source stage audit, not a pooled fraud rate  
**Checked:** 2026-10-18  
**Scope:** payment adoption -> usable transaction -> fraud or outage -> reporting and remedy -> recovery, fallback, switching, or exit

## What we found

Payment systems are becoming ordinary infrastructure faster than their recovery
routes are becoming visible. Scale, speed, and preference do not prove that a
person can complete a necessary transaction, reverse a loss, obtain a human
answer, or leave a provider without sacrificing access.

```text
payment access and use
  -> transaction or exposure
  -> outage, scam, fee, or account problem
  -> report, dispute, correction, reimbursement, or fallback
  -> restored room, continued use, switching, non-use, or exit
```

The strongest supported result is a stage gap, not a universal digital-failure
claim: payment adoption is observable at ecosystem or diary level, while
individual receipt of remedy and durable financial recovery usually is not.

## Comparable evidence ledger

| Source and unit | Adoption or exposure | Remedy/fallback surface | What it establishes | Main limit |
|---|---|---|---|---|
| [NBER payment-method resilience paper](../../records/us-nber-payment-method-resilience-disaster-outages-2026.json), outage/event-study, transaction and survey sources | Disasters and outages reduce expenditure and digital-payment use; cash use rises; nearly half of surveyed consumers could not use their preferred electronic payment during an outage | Greater cash access is associated with more completed transactions; cash acts as a fallback | A widespread digital rail can fail at the point of need, and fallback availability changes transaction completion | Source families are not one respondent panel; completion is not an adequate food, medicine, fuel, work, or care outcome; causal assumptions and full outcome tables remain bounded |
| [Federal Reserve SHED fraud record](../../records/us-federal-reserve-household-fraud-recovery-2024.json), US adults, 2024 | 21% reported any financial fraud; among non-credit-card fraud cases, 63% lost money and median pre-recovery loss was $423 for ages 18–44 versus $600 for ages 60+ | 32% of adults with non-credit-card fraud reported some money not recovered; 30% spent at least ten hours dealing with recovery; estimated loss was $84 billion and estimated recovered amount $21 billion | Loss, recovery failure, and time cost are distinct household burdens | Self-report, most-recent-incident framing, estimated dollars, no verified provider liability, no case-level remedy receipt, trust, or exit |
| [ASEAN GSMA scam record](../../records/comparative-asean-gsma-consumer-scam-2026-resolution-recovery-digital-trust.json), six-country consumer survey, previous 12 months | 8% reported being scammed; 68% of victims reported financial loss; messaging apps appeared in 41% of reported experiences and social media in 36% | 82% of money-losing victims recovered none and only 10% recovered all; 69% of scam victims reported incidents, but 45% of reported cases remained unresolved; affected consumers were more than twice as likely to switch accounts or providers | Reporting can coexist with unresolved cases; loss and switching can be linked to digital trust | Sample size, weights, case definition, resolution timing, and administrative validation are not available in the accessible release; switching is a reported association, not completed exit |
| [OECD consumer-finance risk monitor](../../records/comparative-oecd-consumer-finance-risk-monitor-2026-scams-digital-exclusion-remedy.json), authorities in 60 jurisdictions representing 107 ministries/authorities | 85% of reporting authorities named scams/fraud among major operating risks and 69% said scams increased in 2025; phishing/vishing/smishing was selected by 83% of applicable responses | The monitor describes complaint systems, supervisory coordination, outreach, comparison tools, and conduct supervision | Consumer protection increasingly depends on detecting, contesting, and correcting harm across institutional boundaries | Authority perceptions and policy descriptions are not consumer prevalence, implementation quality, compensation, or durable recovery |
| [UK Open Banking record](../../records/comparative-uk-open-banking-limited-2026-api-payments-users-fraud.json), ecosystem aggregates, 2025–26 | Payments grew 45% year over year; July 2026 had 2.94 billion API calls and more than 19 million monthly active connections; more than 1 billion payments occurred since inception | Open-banking fraud was reported at about 1 per 6,000 payments in 2025, with more than two-thirds of cases being authorised push-payment fraud | Routine scale can coexist with concentrated fraud exposure; payment volume is not consumer protection | Connections and API calls are not unique people; coverage is incomplete, payment value, loss severity, reimbursement, switching, and welfare are not measured; publisher outputs are related, not independent corroboration |
| [Brazil Central Bank Pix diary](../../records/comparative-brazil-bcb-pix-2023-payment-diary-digital-barriers.json), 1,228 diaries and 11,023 recorded payments in 2023; 1,500-person survey | Cash fell from 76.6% of recorded payments in 2019 to 40.5% in 2023; Pix was 24.9% of recorded payments; 64.9% named Pix among their two preferred methods | 17.3% had not used Pix in the prior year; among nonusers, 37.3% cited lack of knowledge; 24.2% sometimes chose another method because of internet access difficulty; cash remained a preferred method for 55.7% | Preference and actual use can coexist with knowledge, connectivity, and offline-resilience barriers | Different conditional denominators, sample waves, and survey/diary frames; no fraud, remedy, welfare, or causal Pix effect |
| [NBER payment-convenience record](../../records/us-nber-payment-convenience-depositor-activeness-2026.json), transaction-level data from millions of US depositors and county-level Zelle rollout | Faster transfers are associated with more transfers and lower deposit growth; transfer delays raise deposit demand | Payment speed changes liquidity management and the deposit channel through which payment infrastructure reaches banks and monetary transmission | Faster payment is not only a convenience outcome; it can change account behavior and bank funding conditions | The abstract does not disclose effect sizes or full dates; transaction, county, depositor, and bank units remain separate; lower deposit growth is not automatically lower household resilience |

## What this connects to

Four stage distinctions matter.

1. **Access is not completion.** NBER's outage evidence and Brazil's Pix
   barriers show that a rail can exist and be preferred while a person cannot
   execute a needed payment at the relevant time.

2. **Exposure is not loss.** The Federal Reserve separates any fraud,
   money-losing fraud, unrecovered money, and time spent. These should not be
   collapsed into a single “fraud burden” number.

3. **Reporting is not remedy.** The ASEAN record reports high reporting but
   unresolved cases and little recovery. OECD policy infrastructure identifies
   possible routes but does not show that a household received correction or
   reimbursement.

4. **Switching is not restored agency.** A provider switch may protect a
   consumer, impose new setup costs, or reflect loss of trust without restoring
   the money or access that was lost. No current source follows the same case
   through both reimbursement and durable alternative use.

5. **Speed is not the same as security.** The new NBER payment-convenience
   evidence shows that faster transfers can increase transaction activity and
   reduce deposit growth, while delays can raise deposit demand. This adds a
   bank-funding and liquidity-management pathway, but it does not establish
   that faster payments improve household welfare, resilience, or recourse.

## Bounded public discussion

Public discussion supplies interpretation and route hypotheses, not prevalence:

| Record | Discussion signal | Use and limit |
|---|---|---|
| [Refund-support discussion](../../social-discussions/records/consumer-recourse-002.json) | A delayed refund and inability to reach a human are framed as reasons to stop using a platform; replies describe both automation frustration and ways to reach an agent | Makes human fallback and practical exit visible; anecdotal, self-selected, and not an administrative outcome |
| [Public bank-support reply](../../social-discussions/records/consumer-recourse-004.json) | A bank-support account says charges were reversed and finance charges adjusted after a complaint | Shows a visible case-specific response; customer identity, original complaint, and final outcome are not independently verified |
| [Card-terms discussion](../../social-discussions/records/atlas-batch-0048-card-terms-linkedin-001.json) | Discussion interprets credit terms as a two-tier system and raises the counterargument that rate caps may reduce access or shift costs into fees | Preserves distributional disagreement; comments are not representative borrower evidence |
| [Human-support-in-finance discussion](../../social-discussions/records/atlas-batch-0038-yougov-ai-finance-linkedin-001.json) | Participants emphasize human support, accountability, and accessibility as AI enters financial services | Identifies a recourse expectation; it does not show complaints, switching, or improved outcomes |

The social layer strengthens the practical question: people judge payment systems
not only by speed but by reversibility, explanation, human access, and whether
they can remain secure while changing providers. It does not prove that those
expectations were held by any survey subgroup or that they changed behavior.

## Missing links and challenge checks

- Do not use API calls, payment counts, or connections as unique-person adoption.
- Do not compare conditional scam-loss percentages as if they share one
  denominator.
- Do not treat cash fallback as proof of affordability, adequate purchase, or
  household resilience.
- Do not treat a complaint, a public reply, or an authority framework as
  verified reimbursement.
- Keep payment fraud, authorised scams, outages, hidden fees, and credit
  exclusion as distinct exposures until a common case design supports joining.
- Treat provider switching as a separate behavior from account closure, payment
  replacement, non-use, and practical exit.
- Keep publisher-related ecosystem reports from being counted as independent
  corroboration.
- Do not infer a consumer benefit from faster transfer or a consumer harm from
  lower deposit growth without observing liquidity needs, balances, interest,
  payment completion, and later recovery.

## Stronger next test

The next high-value record is a lawful, identifier-bearing payment episode with:

1. payment purpose, date, amount, channel, and available alternatives;
2. outage, scam, fee, or account event and responsible provider/actor;
3. report, contact attempts, human/automated route, and time to response;
4. correction, reimbursement, charge reversal, or fallback transaction;
5. amount received, residual loss, time cost, and essential outcome; and
6. continued use, provider switch, non-use, trust, and later financial room.

If no single source exposes these fields, the program should preserve the
cross-source stage comparison and seek one small administrative or panel route,
not infer practical exit from aggregate switching or complaint counts.

## Deeper question

**When does a payment failure become a durable loss of practical choice, and
which combination of fallback, human recourse, reimbursement, and provider
competition restores enough financial room to stay or leave?**

## Stopping rule

This pass is sufficient when adoption, completion, exposure, reporting, remedy,
recovery, fallback, switching, and exit have been separated by unit, date,
denominator, method, and limit; the discussion layer is bounded; and the
same-case missing middle is explicit. The broader 14-theme program remains
active.

## Sources

- [NBER payment-method resilience](../../records/us-nber-payment-method-resilience-disaster-outages-2026.json)
- [Federal Reserve household fraud recovery](../../records/us-federal-reserve-household-fraud-recovery-2024.json)
- [GSMA ASEAN consumer scam report](../../records/comparative-asean-gsma-consumer-scam-2026-resolution-recovery-digital-trust.json)
- [OECD consumer-finance risk monitor](../../records/comparative-oecd-consumer-finance-risk-monitor-2026-scams-digital-exclusion-remedy.json)
- [UK Open Banking ecosystem and fraud monitor](../../records/comparative-uk-open-banking-limited-2026-api-payments-users-fraud.json)
- [Brazil Central Bank Pix payment diary](../../records/comparative-brazil-bcb-pix-2023-payment-diary-digital-barriers.json)
- [NBER payment convenience and depositor activeness](../../records/us-nber-payment-convenience-depositor-activeness-2026.json)
- [Refund support discussion](../../social-discussions/records/consumer-recourse-002.json)
- [Public bank-support reply](../../social-discussions/records/consumer-recourse-004.json)
- [Card-terms discussion](../../social-discussions/records/atlas-batch-0048-card-terms-linkedin-001.json)
- [Human-support in finance discussion](../../social-discussions/records/atlas-batch-0038-yougov-ai-finance-linkedin-001.json)
