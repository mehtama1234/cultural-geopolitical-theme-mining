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

## Provider comparison

| Provider | Entry route | Who pays | What the provider says it covers | Main unknown |
|---|---|---|---|---|
| [TheGuarantors](https://www.theguarantors.com/products-rent-coverage) | Property sends a conditional or denied applicant to the provider. | Renter, usually as an upfront premium. | A selected amount of missed rent, with optional deposit coverage; terms can vary by state. | Approval rates, actual prices, claims, and recovery outcomes. |
| [Rhino](https://support.sayrhino.com/hc/en-us/articles/360061185252-What-is-Rhino-Renter-Guarantee) | Property manager decides whether to offer the renter guarantee. | Renter; premium and possible reserve. | Landlord protection for missed rent or excessive damage, subject to policy limits. | State-by-state availability, claim recovery, and renewal outcomes. |
| [Leap](https://support.leapeasy.com/hc/en-us/articles/41084838074007-What-is-Rent-Guaranty-coverage) | Renter applies for a provider policy when a personal guarantor is missing. | Renter pays a one-time premium. | Coverage for the operator for the lease term; separate from Leap's deposit-replacement product. | Public terms on exclusions, prices, claims, and tenant repayment. |

The common structure is not yet proof that the companies have equal terms. It is a reason to compare policy documents, state filings, and claim records before treating them as one market.

## State and legal check

| Provider record | What is public | What it means for the map |
|---|---|---|
| [Rhino product disclosure](https://www.sayrhino.com/products/renter-guarantee) | Rhino says its security-deposit alternative is not available in HI, MT, ND, or WY. It lists admitted A- or better carriers in AK, CT, DE, IN, KY, MD, ME, NY, OH, PA, SD, TN, and WV, and says other states may use nonadmitted excess or surplus-lines carriers. | “Nationwide” does not mean one regulatory or policy setting. |
| [TheGuarantors FAQ](https://www.theguarantors.com/faq-for-renters) | TheGuarantors says not all coverages are available in every state. It identifies California lease-guarantee and security-deposit bonds as surplus-lines products and gives a California license number for its agency. | State filing and policy form matter before comparing price or protection. |
| [Leap legal notices](https://leapeasy.com/legal-notices/) | Leap publishes producer licensing information by state and says insurance applications must go through licensed producers; its coverage may be admitted or excess and surplus lines. | A provider's national footprint still needs state-by-state checking. |

The public records support a state-terms table, but not a complete price table. Provider quotes are personalized and the policy forms, filings, and underwriting decisions are not all public in one place.

## Four-state first check

| State | Record found | What it shows | Status |
|---|---|---|---|
| California | [TheGuarantors California bond terms](https://www.theguarantors.com/terms-and-conditions-california) | Bonded leases require an indemnity agreement and paid premium; the term is capped at 24 months; the landlord must try to re-let after default; the surety receives collection rights after payment. | Documented policy terms |
| New York | [NY Department of Financial Services consent order](https://www.dfs.ny.gov/industry_guidance/enforcement_discipline/ea20220628_guarantors) | The regulator described lease rental bonds as landlord-protection products bought by tenants and required approved rate filings after finding a rate-law violation involving nine-month bonds sold for twelve-month leases. | Documented regulatory history; current contract still open |
| Texas | [Texas Property Code, Chapter 92](https://statutes.capitol.texas.gov/DocViewer.aspx?DocKey=PR%2FPR.92&ExactPhrase=False&HighlightType=1&Phrases=can%7Cconstables%7Cserve%7Ccivil%7Cpapers&QueryText=can+constables+serve+civil+papers) | A fee in lieu of a security deposit may fund insurance for damages and unpaid rent, but the fee does not remove the tenant’s duty to pay rent. After a valid insurer payment, the insurer may seek limited reimbursement under the statute. | Documented tenant-protection rule; provider match open |
| Illinois | [Illinois insurance licensing guidance](https://idfpr.illinois.gov/banks/cbt/comcl/btfaqins.html) | Insurance sellers need producer licensing; the page is general guidance and does not identify a rent-guarantee provider, product form, or price. | Licensing context only |

## Decision rule

Keep modeled welfare, actual claims, prevented eviction and later household security separate. The model is a design clue, not a measured market result.
