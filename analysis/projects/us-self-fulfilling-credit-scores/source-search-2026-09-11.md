# Source search: US self-fulfilling credit scores

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** opening pass; a causal score-to-default effect is measured for a defined higher-risk group, the full housing and service path remains open

## Working question

When does a credit score stop describing a problem and start making the problem harder to escape?

## Opening source

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-NBER-SELF-FULFILLING-SCORE | [Self-Fulfilling Credit Scores](https://www.nber.org/papers/w35508) | Using a rule that treats multiple credit inquiries within 14 days as one, the authors find that an extra counted inquiry lowers scores by about five points without changing the credit report. Default did not change for consumers with clean records, but rose by 3.2 percentage points over two years for consumers with prior derogatory marks. At least 13% of the score-default link for that group appears self-fulfilling. | NBER working paper | The result concerns one score rule and people with prior derogatories. It does not show which lender decision caused the default or the later housing, work or insurance result. |

## First pattern to test

```text
credit inquiry or score rule
  -> score changes without new household fact
  -> lender price or access changes
  -> payment pressure or lost credit
  -> default, housing loss or reduced future access
```

The source supports a causal score-to-default link for a defined group. It does not establish every step in the household path.

## Counterpoint to keep visible

Scores can help lenders sort risk and may prevent some bad matches between borrowers and loans. The study does not show that removing scores would improve outcomes or that every score drop has a harmful effect.

## Main gaps

- the exact lender decision after the score change;
- loan price, credit limit and approval data;
- rent, mortgage, insurance and job effects;
- score recovery and later access;
- differences by income, race, age and place;
- whether a better score rule reduces self-fulfilling defaults.

## Decision rule

Keep score movement, lender action, payment trouble and household loss separate until the same borrower can be followed through each step.
