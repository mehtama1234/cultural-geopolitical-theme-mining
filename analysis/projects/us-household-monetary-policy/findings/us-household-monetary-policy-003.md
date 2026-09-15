# A policy signal can move expectations without revealing who changes spending

**Status:** provisional cross-source monetary-policy finding  
**Checked:** 2026-09-14

## The bounded finding

The two household-expectations studies now allow a sharper separation between
three objects:

1. how a respondent interprets a communicated rate decision;
2. what a respondent says they would do with spending or a portfolio; and
3. what a household actually does after a contract, income, or asset-price
   channel changes.

The September 2025 NBER design-comparison study finds that a 25-basis-point
rate cut lowered one-year inflation expectations by 0.833 percentage points in
the full randomized-information treatment, 1.937 points among respondents who
were previously unaware, and 0.721 points in the balanced event-study panel.
The BIS/NBER household study reports much smaller intended durable-spending
responses to a one-percentage-point rate surprise—about −0.05 percentage point
among financially literate/Federal-Reserve-aware respondents for a positive
surprise and +0.08 for a negative surprise.

These estimates should not be ratioed or described as one transmission
coefficient. They use different rate changes, samples, designs, outcomes,
periods, and denominators. Their value is architectural: expectation movement
and intended spending movement are related but not interchangeable stages.

## The evidence kept separate

| Evidence | Unit/design | Direct result | Boundary |
|---|---|---|---|
| NBER W35090 vignette | 4,067 valid one-year-inflation vignette observations | 25 bp cut versus no-change: −2.043 percentage points (SE 0.216) | Hypothetical policy scenario; universal experimental exposure |
| NBER W35090 RCT | 1,308 recontacted respondents; 557 previously unaware, 751 aware | One-year inflation: −0.833 full sample; −1.937 unaware; 0.026 aware | Information treatment after a realized decision; expectation outcome, not spending |
| NBER W35090 event study | 1,308 balanced panel; 6,968 pooled observations | Balanced-panel one-year inflation: −0.721 (SE 0.121); correctly perceived cut: −1.299 (SE 0.080) | Natural exposure includes announcement, media, markets, and other news |
| BIS/NBER W35127 | 26,968 first-wave US residents ages 25–70; 4,461 follow-up | Positive 1 pp information surprise: about −0.05 pp durable spending among financially literate/Fed-aware respondents; negative surprise: +0.08 pp | Quota-based online survey; reported/intended short-run spending, not transactions |

The rates and outcomes cannot be pooled. A 25 bp cut in W35090 is not the same
treatment as a 1 pp surprise in W35127, and a percentage-point change in an
expectation is not a percentage-point change in a spending share. The samples
also differ in field date, age frame, recruitment, weighting, and follow-up.

## The mechanism now visible

```text
rate decision or information
  -> awareness, surprise, and interpretation
  -> inflation / unemployment / activity expectations
  -> intended durable spending or portfolio response
  -> actual contract payment, purchase, saving, debt, work, or care change
  -> trust, fairness judgment, or political action
```

W35090 is strongest on the first two arrows. W35127 adds a short-horizon
intended-spending and portfolio channel, especially among respondents with
financial literacy or Federal Reserve knowledge. Neither source observes the
complete household balance-sheet and transaction path needed to identify who
absorbs the cost or who benefits from the rate change.

## Why borrower/saver exposure is decisive

The same announcement can have opposite material meanings. A variable-rate
borrower may face a higher payment; a depositor may receive more interest; a
fixed-rate homeowner may see little immediate contract change; a renter may
face an indirect housing-supply or credit channel; and a household with low
liquidity may be unable to delay a purchase even if it expects prices to rise.

The studies contain pieces of this heterogeneity—debt, wealth, financial
literacy, assets, and Federal Reserve knowledge—but they do not provide a
single realized borrower/saver event record. The absence of a large average
spending response therefore cannot be read as absence of burden. It may reflect
substitution, timing, offsetting borrower and saver responses, or households
whose contracts did not change during the observation window.

## Counterexamples and limits

- A large expectation revision can coexist with a small intended-spending
  response.
- A small average spending response can conceal large changes in a subgroup or
  opposite borrower/saver movements.
- A respondent who hears and correctly perceives a policy announcement is not
  randomly selected from the population.
- Survey intentions may be constrained by liquidity, existing contracts,
  credit access, care needs, or the timing of a planned purchase.
- A rate announcement can signal the central bank's information about the
  economy, so interpretation is not the same as a pure rate-exposure effect.
- Neither study establishes trust change, voting, collective action, or
  realized household welfare.

## Next end-to-end test

The next empirical pass should join, within a valid common unit or a carefully
matched design:

1. pre-announcement expectations and policy awareness;
2. debt type, fixed/variable rate, deposits, liquid assets, tenure, and income;
3. the actual rate or contract reset and its timing;
4. observed spending, saving, debt payment, refinancing, work, and care
   responses; and
5. later financial security, trust, attribution, or political action.

The strongest counterexample cells are households with similar expectation
revisions but different contract exposure, and households with similar rate
exposure but different liquidity or family support. Until those cells exist,
the program should describe a measured expectations-to-intended-action bridge,
not a completed household-to-politics causal chain.

## Sources and reproduction

- [NBER W35090 machine record](../../../records/us-nber-monetary-policy-information-treatments-2026.json)
- [NBER W35090 detailed finding](us-household-monetary-policy-002.md)
- [BIS/NBER W35127 machine record](../../../records/us-bis-household-monetary-policy-beliefs-2026.json)
- [BIS/NBER cross-source finding](us-household-monetary-policy-001.md)
- [NBER W35090](https://www.nber.org/papers/w35090)
- [NBER W35127](https://www.nber.org/papers/w35127)
- [BIS Working Paper 1354](https://www.bis.org/publications/working-paper-1354-monetary-policy-according-households-perceptions-reactions-and-channels)

**Evidence status:** cross-source mechanism finding using two survey-experiment
families; expectation and intended-action stages are measured separately, while
realized borrower/saver incidence, household welfare, trust, and political
action remain open.
