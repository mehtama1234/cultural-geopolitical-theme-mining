# CFPB 2025 medical-debt complaint visibility v1

**Checked:** 2026-09-15  
**Status:** published administrative visibility measure; not a household or remedy rate  
**Machine output:** [medical-debt visibility data](data/us-cfpb-2025-medical-debt-visibility.json)

## Result

The committed CFPB aggregate snapshot for complaints received from January 1
through December 31, 2025 contains **8,861** published records in the nested
`Debt collection → Medical debt` subproduct. The snapshot contains 5,452,107
published records overall and 283,828 under the parent Debt collection
product. Medical debt therefore represents:

| Denominator | Medical-debt records | Share |
|---|---:|---:|
| All published records in the snapshot | 8,861 | 0.163% |
| Debt-collection records | 8,861 | 3.122% |

This is a count of records made visible in the CFPB complaint system. It is not
the share of Americans with medical debt, the probability of a medical-debt
problem producing a complaint, or the probability that a complaint received a
remedy.

## What this adds to the health-cost chain

```text
medical-cost burden enters a credit/collection institution
  -> a medical-debt complaint can become a categorized public record
  -> response, correction, recovery, repeat effort, trust, or exit remain open
```

The result gives the institutional-visibility layer a medical-specific product
label. It complements MEPS medical debt, collection contact, bill-problem, and
denial/prior-authorization context without joining those person-level records
to CFPB complaints. It also complements the CFPB medical-collections credit
reporting layer, which describes credit-system visibility and contested policy
response rather than complaint prevalence.

## Boundary and next test

The aggregate snapshot does not include a medical bill, care decision, amount
owed, appeal, verified correction, money recovered, restored care, household
trade-off, repeat contact, switching, trust, or exit for the same person. The
product and subproduct are selected by the complainant and publication system;
the count is not a harm denominator. The next decisive test remains a
record-level medical query with stable case keys and response fields, followed
by a lawful same-case or panel design that can observe remedy and later
household outcomes.

## Sub-product response-route acquisition check

On September 15, 2026, the reusable aggregate fetcher was extended to accept a
repeated `--sub-product` filter. A live request for
`product=Debt collection&sub_product=Medical debt` returned **283,828**
records—the parent Debt collection total—not 8,861. The returned response
aggregations therefore describe the parent product and cannot be promoted as
medical-debt-specific response, timeliness, or remedy rates. This is an API
behavior check, not evidence that the medical-debt category has the parent
product's response profile.

Reproduction command:

```text
python3 scripts/fetch_cfpb_complaint_aggregation.py \
  --date-min 2025-01-01 --date-max 2026-01-01 \
  --product 'Debt collection' --sub-product 'Medical debt' \
  --output /tmp/cfpb-medical-debt-routes.json
```

The next acquisition route must use record-level retrieval or another endpoint
whose returned total and response fields demonstrably respect the sub-product
constraint. Until then, the medical-specific layer remains visibility-only.

## Reproduction

```text
python3 scripts/analyze_cfpb_medical_debt_visibility.py \
  analysis/projects/us-customer-automation-recourse/data/cfpb-2025-aggregation-snapshot-2026-09-14.json \
  --output analysis/projects/us-health-cost-household-choice/data/us-cfpb-2025-medical-debt-visibility.json
```

The input is the [CFPB 2025 aggregate snapshot](../us-customer-automation-recourse/data/cfpb-2025-aggregation-snapshot-2026-09-14.json), whose retrieval and API-vintage boundary are documented in the [CFPB API vintage refresh](../us-customer-automation-recourse/cfpb-api-vintage-refresh-2026-09-14.md).
