# Source search: US cash policy and public mood

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** opening pass; policy and sentiment link is supported, political behavior remains open

## Working question

Can the loss of a household benefit change how people read the economy?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-NBER-CTC-SENTIMENT | [When Policy Shapes Perception](https://www.nber.org/papers/w35059) | Using monthly consumer-sentiment data and variation in household benefit loss, the study estimates that each $1,000 lost from the expanded Child Tax Credit reduced sentiment by 1.7 points, with larger effects among lower-income families with multiple children; the effect persisted nearly two years. | NBER working paper | Sentiment is not a vote, trust measure or direct spending outcome. |
| US-NBER-CTC-HOUSING | [The 2021 Child Tax Credit, Living Arrangements and Housing Affordability](https://www.nber.org/papers/w31339) | The monthly credit was associated with less back-owed rent or mortgage and changes in living arrangements among low-income parents. | NBER working paper | It studies housing and arrangements, not political mood. |
| US-HBS-CASH-CONTROL | [More Proof That Money Can Buy Happiness](https://www.library.hbs.edu/working-knowledge/more-proof-that-money-can-buy-happiness) | HBS reports that more money can give people more control over daily problems and reduce stress. | HBS Working Knowledge | The article does not study the Child Tax Credit or national sentiment. |

## First pattern to test

```text
benefit starts or ends
  -> household cash and housing room change
  -> people judge their own financial position differently
  -> consumer sentiment changes
  -> spending, trust, blame, or voting may change
```

The NBER sentiment study gives a direct policy-to-perception result. It does not prove that a person spent less, lost trust or voted differently. Those are the next links to test.

## Counterpoint to keep visible

People may feel worse after a benefit ends because their cash really fell, not because they formed a new political view. A lower sentiment score can also coexist with stable work, housing or long-term plans.

## Main gaps

- actual spending and saving after benefit loss;
- trust in government and perceived fairness;
- news, party identity and local economic conditions;
- vote choice, turnout and political contact;
- effects after the initial loss fades;
- differences by income, family size, race and state.

## Decision rule

Keep sentiment as its own outcome. Only connect it to spending, trust or voting when the same study or linked data measure the next step.
