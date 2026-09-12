# Source search: US rent-guarantee insurance

**Search date:** 2026-09-11  
**Geography:** United States housing-market model  
**Status:** opening pass; modeled gains are clear, actual market effects remain open

## Working question

Who can buy protection before a rent shock, and who is left with the loss?

## Opening source

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-NBER-RENT-GUARANTEE | [Rent Guarantee Insurance](https://www.nber.org/papers/w32582) | The model covers a limited number of rent payments after an income or health shock. It finds higher welfare, smaller security deposits and less homelessness. Unrestricted access is not financially viable; private insurers would target better-off renters, while public insurance would focus on people most at risk. | NBER working paper | This is a quantitative model, not a broad US rollout. It does not measure premiums, take-up, claims, landlord response or later credit. |

## First pattern to test

```text
income or health shock
  -> rent cannot be paid
  -> insurance claim, public aid, legal help, or no protection
  -> landlord receives payment or starts a case
  -> housing and credit path
```

The model supports a risk-sharing case for rent insurance. It also gives the main warning: a private product may be viable only for renters who are already better able to pay, while public coverage faces a different cost and targeting problem.

## Counterpoint to keep visible

Insurance can reduce the need for a large deposit and may prevent a severe loss. But a premium, deductible, exclusion or screening rule can create a new barrier before the crisis begins.

## Main gaps

- actual US product availability and take-up;
- premium, claim and exclusion rules;
- landlord response to insured tenants;
- who is denied or cannot afford coverage;
- housing, credit, work and health after a claim;
- public cost compared with direct rental aid.

## Market check

| Source | What it tells us | Status | Limit |
|---|---|---|---|
| [TheGuarantors renter FAQ](https://www.theguarantors.com/faq-for-renters) | The product is bought by the renter, names the landlord as beneficiary, can help a renter qualify, is priced from rent, property requirements and financial information, and is paid as an upfront non-refundable premium. If the company pays a landlord, the renter still owes the company. | Provider description | A provider page does not show take-up, claim frequency, approval rates, or tenant outcomes. |
| [TheGuarantors: behind on rent](https://help.theguarantors.com/im-behind-on-rent.-can-you-help-me-pay) | Rent Coverage does not pay the tenant's monthly rent as relief. It pays a landlord claim for an outstanding balance and then seeks reimbursement from the tenant. | Provider help page | It describes one product's terms, not the whole market. |
| [Rhino Renter Guarantee](https://support.sayrhino.com/hc/en-us/articles/360061185252-What-is-Rhino-Renter-Guarantee) | The property manager decides whether to offer the product. Coverage can include missed rent or damage; price uses personal and lease information; a reserve may be required; the tenant repays a claim. | Provider help page | It does not report approval, pricing distribution, claims, or later housing results. |
| [Columbia Business School research brief](https://business.columbia.edu/research-brief/rent-guarantee-insurance-housing-crisis) | The research brief describes private RGI as a product offered by fintech firms and says private providers are likely to serve middle-income renters, while public coverage could reach higher-risk renters. | Research summary | It summarizes the model and does not measure provider performance. |

## Market finding to test

The real products found so far protect the landlord's lease decision more clearly than they protect the tenant's balance sheet. They may open a door for a renter who lacks a conventional guarantor, but a claim can become a new debt to the provider. This is a different product from insurance that absorbs the tenant's loss.

## Decision rule

Keep modeled welfare, actual claims, prevented eviction and later household security separate. The model is a design clue, not a measured market result.
