# Payment outage, fraud, recovery, and remedy bridge

**Status:** twenty-second active depth artifact in the ongoing program  
**Checked:** 2026-10-18  
**Scope:** payment infrastructure failure, fraud, household transaction completion, recovery, and public trust

## Question

When a payment system is disrupted or a transaction is fraudulent, can a
household still complete essential purchases, recover money and time, and trust
the institutions that operate or police the rail?

```text
payment availability / fraud exposure
  -> failed or unauthorized transaction
  -> cash, credit, family, merchant, or public alternative
  -> completed need or direct loss
  -> reporting, reimbursement, correction, and time cost
  -> later trust, repeat use, switching, or exit
```

## Evidence ledger

| Stage or link | Comparable observation | Method and unit | Boundary |
|---|---|---|---|
| Outage changes payment method and spending | The NBER disaster study finds hurricanes produce persistent outages and sharply reduce expenditures; digital payments decline and cash use rises, especially where outages occur. Nearly half of surveyed consumers could not use their preferred electronic payment during an outage, while access to cash was associated with completing more transactions and mitigating expenditure declines. | Event studies combining outage/weather, transaction, scanner, and household records with surveys across U.S., Spanish, and Swedish settings. | Source families are not one respondent panel; transaction completion is not proof that food, medicine, fuel, work, or care needs were met. |
| A fast payment rail can grow alongside fraud | UK open-banking payments grew 45% year over year, API calls reached 2.94 billion in July 2026, and cumulative payments passed 1 billion. The ecosystem's reported fraud rate was about one per 6,000 open-banking payments versus one per 2,500 across the wider payments industry; more than two-thirds of reported open-banking fraud cases were authorised push-payment fraud. | Open Banking Limited aggregate activity and fraud monitor; provider data cover more than 60% of open-banking volume. | Ecosystem aggregates are not unique users, payment value, causal safety, reimbursement, or distributional access. Related OBL outputs are not independent population corroboration. |
| Fraud creates both money and time loss | Federal Reserve 2024 SHED estimates find 21% of adults experienced financial fraud; among non-credit-card fraud, 63% lost money, 32% had some money unrecovered, estimated losses were $84 billion with $21 billion recovered, and about 30% spent 10+ hours recovering or dealing with the fraud. | Weighted national adult survey; loss and recovery measures conditional on non-credit-card fraud. | Survey-reported, overlapping categories and estimated dollars; no verified provider liability or later trust outcome. |
| Recovery burden is unequal | In a public-use SHED subgroup analysis, some or all money was unrecovered in 53.8% of other-fraud reporters with income $10,000–$24,999 versus 22.6% among $100,000–$149,999. Among account-involved cases, unrecovered money was 46.1% for P2P versus 28.8% for non-P2P routes. | 12,295 public-use respondent rows with weighted subgroup calculations; conditional route and loss denominators preserved. | Derived survey estimates do not establish payment-route causality, verified firm remedy, disability/digital-access gradients, or switching. |
| Loss can coexist with later material insecurity | A same-respondent April-to-June HTOPS screen found 184 linked respondents reporting exposure and monetary loss; in that sparse subgroup, weighted June food insufficiency was 23.8% and inability to pay an energy bill 43.8%. A smaller exposure/loss/reporting/recovery group had 78.8% unable to pay an energy bill, but only 11 linked respondents. | Exact SCRAMID follow-up with survey weights and explicit sparse-subgroup limits. | Descriptive follow-up, not a dated fraud effect, verified recovery, causality, or general population estimate. The 11-person subgroup is especially unstable. |
| Institutional controls remain incomplete | GAO reviewed 215 federal fraud-risk recommendations, with about 40% still open as of April 2026, and identifies fraud as eroding public trust and hindering mission execution. It states that there is no single national denominator for prevented loss, recovery, or user-level trust. | Federal oversight and recommendation-status review across programs. | Open recommendations do not prove losses or distrust; recommendation status is not household remedy performance. |

## Cross-source finding

The critical distinction is between **rail availability** and **recoverable
agency**. A payment system can be fast and widely used while households still
need cash, credit, family help, or merchant discretion when the network fails.
Likewise, a fraud rate can look low while affected households face unequal loss,
long recovery work, and later energy or food insecurity.

Four outcomes must remain separate:

1. **Access:** the payment rail or fallback is technically available.
2. **Completion:** the household completes the needed purchase or transfer.
3. **Recovery:** money, time, identity, and account control are restored.
4. **Trust:** the household continues using the rail or believes institutions
   will respond fairly next time.

The NBER evidence supplies the outage counterexample to digital-only resilience:
cash is not merely a preference when networks fail. The SHED and HTOPS evidence
supplies the fraud counterexample to transaction-volume optimism: a completed
payment can still begin a long and unequal recovery episode.

## Bounded public discussion

A LinkedIn discussion of FTC fraud-loss data emphasizes that reported losses are
not total incidence and that underreporting or reporting breaks can change the
headline. A World Bank LinkedIn relay on AI and development adds the parallel
infrastructure lesson: adoption depends on electricity, broadband, skills,
computing, local data, and institutions, not a rail alone.

These discussions help identify visibility and complement gaps. They are not
victim samples, public-opinion estimates, or evidence of reimbursement.

## Counterexamples and alternative explanations

- Cash may preserve transactions during an outage but can be unsafe, costly,
  inaccessible, or unavailable to people who rely on digital income.
- A lower observed fraud rate may reflect better controls, different reporting,
  or provider coverage rather than safer consumer experience.
- P2P routes may have greater unrecovered loss because they are used in more
  social-engineering cases, not because the rail itself causes loss.
- A household can recover money but still lose time, credit access, privacy, or
  confidence; monetary reimbursement is not full recovery.
- GAO recommendation closure may improve controls without producing visible
  household trust, while public trust can also change for unrelated reasons.

## Stronger next test

Create named outage and fraud episode ledgers that follow:

1. rail, provider, merchant, weather, or scam trigger;
2. account balance and payment method available at the moment;
3. attempted transaction, essential need, fallback, and completion;
4. loss amount, reporting route, investigation, and reimbursement;
5. hours spent, account restrictions, debt, food/energy/health outcomes; and
6. later repeat use, cash holding, switching, trust, complaint, or exit.

Compare households with and without cash access, credit, disability, stable
connectivity, and institutional support. Use provider and regulator logs where
possible, and keep survey-reported loss separate from verified transaction
records. A resilience measure should reward successful recovery, not only uptime
or transaction throughput.

## Current answer state

**Partly answered.** The corpus shows a route from outage or fraud through
payment-method substitution, incomplete transactions, direct loss, recovery
time, and unequal material consequences. It does not yet follow the same
household through a named failure, verified remedy, and later trust or exit.

## Stopping rule for this rotation

Do not call a payment rail resilient until one episode-level or longitudinal
source observes availability, completed need, recovery/remedy, and later use or
exit with subgroup denominators and a counterexample.

Related: [project README](README.md), [ongoing operating plan](../../ONGOING-GOAL-OPERATING-PLAN_V1.md), and the [digital infrastructure capability bridge](../us-digital-access/digital-infrastructure-interoperability-capability-value-capture-bridge-v1.md).
