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

## Decision rule

Keep modeled welfare, actual claims, prevented eviction and later household security separate. The model is a design clue, not a measured market result.
