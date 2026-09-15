# Finding 054: Consumer protection has visible routing but unresolved recovery, remedy, and trust gaps

**Status:** provisional non-pooled consumer-power/recourse bridge · **Checked:** 2026-09-14

## The bounded finding

The consumer-power lane now places four evidence surfaces in one end-to-end architecture:

1. Federal Reserve SHED measures household fraud exposure, conditional loss, recovery failure, and time cost.
2. FTC reports administrative fraud reports and reported losses, with imposter and investment categories separated.
3. CFPB complaint records show a changing published response and narrative-visibility endpoint.
4. A CFPB student-loan audit shows that “untimely company response” and the broader “timely field = no” are different administrative measures.

The defensible synthesis is: **consumer harm can be financially and temporally costly, while institutional visibility and response labels change without proving recovery, remedy adequacy, trust repair, or the ability to switch or exit.**

## Evidence surfaces kept separate

| Stage | Direct evidence | Unit | What remains open |
|---|---|---|---|
| Household burden | SHED reports 21% of adults experienced any financial fraud; among non-credit-card fraud cases, 63% lost money, 32% reported some money not recovered, estimated net consumer loss was $63B, and about 30% spent 10+ hours dealing with recovery. | Survey adults and conditional incident respondents | Verified event, firm responsibility, remedy adequacy, later trust, and exit |
| Administrative visibility | FTC reports approximately 3M fraud reports and $15.9B reported losses in 2025, including more than 1M imposter reports and over $7.9B investment-scam losses. | Administrative reports received by FTC | Population incidence, underreporting, recovery, and final loss |
| Complaint response | CFPB published-record response labels move from 90.71% explanation and 2.91% monetary relief in 2020 to 58.71% explanation and 0.48% monetary relief in 2025; narrative presence falls from 39.24% to 22.43%. | Published complaint records | Account denominators, case selection, verified correction, adequacy, and trust |
| Field-definition boundary | Student-loan complaints show 2025 `company_response_untimely` at 15.92% versus `timely_field_no` at 30.40%, after 0.33% versus 5.64% in 2024. | Product-filtered administrative fields | Elapsed days, borrower harm, servicing transfer, payment status, and remedy |

These objects are intentionally not pooled. A household survey, FTC report count, CFPB published complaint, and administrative timing field do not share a denominator or consumer trajectory.

## The consumer-recourse chain under test

```text
fraud, error, denial, fee, or service failure
  -> money loss, time cost, stress, and reduced room
  -> report, complaint, appeal, correction, or search for help
  -> firm/agency routing, explanation, relief, or delay
  -> verified recovery, repeat effort, switching, trust, or exit
  -> institutional learning, regulation, market discipline, or political demand
```

The evidence reaches household burden, administrative visibility, complaint routing, and field-definition boundaries. It does not close verified remedy, recovery, switching, trust, or institutional learning.

## What the comparison changes

### Report volume and household burden are different denominators

FTC and CFPB records show what reaches institutions; SHED shows what respondents report experiencing. The two systems can move differently because reporting propensity, access, category definitions, and high-value cases differ. Neither administrative volume nor survey prevalence alone is a consumer-loss rate.

### Time is part of the loss

SHED’s recovery-time measure prevents the analysis from treating dollars as the entire burden. Time spent contacting firms, banks, agencies, or platforms can displace work, care, rest, and civic availability. But the survey does not identify the route, number of failed attempts, or whether the time produced an adequate remedy.

### A response label is not a remedy outcome

The CFPB trend shows the visible response surface changing, but explanation, non-monetary relief, monetary relief, narrative publication, and an in-progress category are administrative labels. They do not tell us whether the consumer received the right amount, corrected a record, stopped a fee, recovered money, or regained trust.

### Field audits protect the end-to-end chain from false precision

The student-loan timing divergence is a measurement result. It prevents `timely = No` from being read as the narrower untimely company-response category and prevents either from being read as elapsed days or borrower harm. Correct field definition is part of substantive consumer power.

## Counterexamples kept visible

- A reported fraud loss can be fully recovered while still imposing substantial time cost.
- An administrative complaint can receive an explanation without adequate correction or relief.
- Lower published monetary-relief labels can reflect routing, product mix, coding, or publication changes rather than worse remedies.
- Higher FTC losses can reflect reporting and high-value composition rather than higher population incidence.
- A borrower can experience a delayed response without the `company_response_untimely` label, or receive the label without a measured financial loss.
- Consumers with no reported loss can still bear privacy, time, fear, or account-continuity costs.
- Filing a complaint demonstrates an institutional route, not equal access, persistence, or trust in the institution.

## Next decisive test

Build a lawful same-case or linked household/account ledger containing:

1. incident, account/product, exposure, date, amount, and payment rail;
2. first notice, contact channel, repeat attempts, elapsed time, and effort;
3. firm/agency decision, explanation, correction, monetary/non-monetary remedy;
4. unrecovered loss, time/care/work displacement, and financial follow-up;
5. dependence, switching/exit alternatives, attribution, fairness, and trust; and
6. later institutional response, regulatory action, or collective/political demand.

Do not promote this bridge to “consumer protection improved,” “firms caused the loss,” or “complaints repaired trust” until verified case outcomes and a denominator-aware comparison exist.

## Sources and reproduction

- [Machine-readable cross-source record](../../../records/us-consumer-loss-recourse-recovery-crosssource-2020-2025.json)
- [Federal Reserve household fraud/recovery record](../../../records/us-federal-reserve-household-fraud-recovery-2024.json)
- [FTC 2025 extension record](../../../records/us-ftc-consumer-sentinel-2025-extension.json)
- [CFPB annual response trend record](../../../records/us-cfpb-annual-response-trend-2020-2025.json)
- [CFPB student-loan timing audit record](../../../records/us-cfpb-student-loan-timing-field-audit-2024-2025.json)

**Evidence status:** bounded consumer-loss/recovery/administrative-response comparison; verified remedy, switching, trust repair, and institutional learning remain unestablished.
