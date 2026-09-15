# Measurement design changes the apparent household response to a rate announcement

**Status:** official NBER full-paper finding; working-paper and survey-outcome boundaries remain active  
**Checked:** 2026-09-14

## The bounded finding

NBER Working Paper 35090 compares three ways of measuring how households
respond to a monetary-policy announcement: hypothetical scenarios,
randomized information provision, and surveys conducted immediately before and
after an actual Federal Reserve rate cut. All three designs point in the same
qualitative direction: respondents associate a rate cut with lower expected
inflation and unemployment and stronger expected economic activity.

The size of the measured response is not design-neutral. The paper's metadata
summary says that hypothetical-vignette estimates are substantially larger than
the average randomized-information and event-study estimates. The differences
shrink when the comparison focuses on randomized-treatment respondents for
whom the decision was new information and on respondents who knew about the
announcement. Expectation revisions also vary with respondent-specific policy
surprises.

The author-hosted August 2026 paper reports 4,067 valid one-year-inflation
vignette observations, 1,308 recontacted respondents in the randomized
information treatment, and 6,968 pooled event-study observations with a 1,308
person balanced panel. This is a measurement and interpretation result, not
evidence that households actually changed spending, borrowing, saving, or
voting.

## What the design comparison adds

| Design | What it asks | What the abstract supports | Boundary |
|---|---|---|---|
| Hypothetical vignette | What would you expect after a stated rate change? | Directionally consistent response, with larger estimated magnitude | Stated response may be more salient and less constrained than a real decision |
| Randomized information | What changes when information about the policy is provided? | Directionally consistent response; average estimate smaller than vignette | Information treatment is not the same as a surprise rate event or a financial exposure |
| Actual-announcement event study | What changes around the September 2025 announcement? | Same qualitative direction in the pre/post comparison | Awareness, concurrent news, prior beliefs, and who answers both waves matter |

The comparison inserts a necessary middle step into the program's monetary-policy
chain:

```text
policy announcement
  -> awareness and perceived surprise
  -> expected inflation, unemployment, and activity
  -> spending, saving, borrowing, portfolio, trust, or political judgment
```

The new evidence reaches the second box. It does not close the action or
meaning boxes.

## What the full paper estimates

The outcome below is the change in expected one-year inflation, measured in
percentage points. Robust standard errors are in parentheses.

| Design and comparison | Estimate | Sample/boundary |
|---|---:|---|
| 25 bp vignette versus no-change scenario | −2.043 (0.216) | Randomized hypothetical scenario; 4,067 valid observations |
| Full randomized information treatment | −0.833 (0.156) | 1,308 recontacted respondents |
| Randomized treatment, previously unaware | −1.937 (0.224) | 557 respondents; new information margin |
| Randomized treatment, previously aware | 0.026 (0.199) | 751 respondents; essentially no average revision |
| Repeated-cross-section event study | −0.815 (0.081) | 6,968 pooled observations |
| Balanced-panel event study | −0.721 (0.121) | 1,308 recontacted respondents |
| Event study, correctly perceived the cut | −1.299 (0.080) | 751 exposed respondents |
| Event study, did not hear/did not know | −0.058 (0.136) | 200 respondents |

The pattern is not simply “vignettes exaggerate and real events are small.”
When the comparison is aligned around information novelty and actual
awareness, the one-year inflation estimates become closer: approximately −2.0
percentage points for the vignette relative to no change, −1.9 for the
previously unaware information-treatment group, and −1.3 for respondents who
heard and correctly perceived the actual cut. The full-sample RCT and event
estimates are smaller partly because they average over people who already knew
the decision or did not encounter it.

The paper also reports that a 25 bp cut is associated with lower five-year
inflation expectations, stronger expected economic activity, and lower expected
unemployment across the designs. The one-year inflation table is the clearest
cross-design numeric anchor; the machine record preserves the full-paper
design, sample, subgroup, and boundary information.

## Registered plan versus analyzed paper

The AEA registration was submitted August 29, 2025 and published September 3,
2025. It planned approximately 4,800 Wave 1 respondents and 2,100 Wave 2
respondents, with approximately 800 per Wave 1 group and 700 per Wave 2 group.
It specified individual-level computer randomization with no clustering and a
primary outcome family of macroeconomic-expectation updating under hypothetical
versus factual policy information.

The final paper reports 4,067 valid one-year-inflation vignette observations,
1,308 recontacted RCT respondents, and 6,968 pooled event-study observations.
These are not silently treated as the same denominator as the registered plan.
The registration page has limited public detail and marks some information
unavailable; a full plan-versus-paper estimand comparison remains an explicit
follow-up rather than an assumption of exact pre-specification.

## Why this matters for the cultural and political atlas

The household does not receive a rate change as a single mechanical price.
People interpret the announcement through awareness, prior information, and
their own policy surprise. A person may hear “lower rates” as lower future
inflation, better employment, cheaper credit, or evidence about whether the
Federal Reserve understands the economy. Those interpretations can coexist or
conflict.

The design comparison also warns against turning a large hypothetical response
into a forecast of household behavior. A vignette can remove the practical
constraints that shape an actual decision: whether the respondent knows about
the announcement, has debt or deposits, can refinance, faces a binding credit
limit, or has a reason to change a purchase. Conversely, a real-announcement
estimate can be smaller because many respondents never receive or process the
information.

These are mechanisms to test, not claims that the paper establishes about any
particular income, debt, age, race, homeownership, or savings group.

The paper's interpretation is especially important: the rate cut may be read as
a signal that the Federal Reserve sees weaker inflationary pressure or a softer
labor market. The event-study response also includes the FOMC statement, press
conference, media interpretation, market reactions, and other news between the
two waves. The estimates therefore concern communicated or observed policy
actions, not a pure structural monetary-policy shock.

## Counterexamples and limits kept visible

- A shared expectation direction does not mean borrowers and savers experience
  the same welfare effect.
- Lower expected inflation is not a lower current price level.
- Stronger expected activity is not realized employment or income.
- Announcement awareness may select people with different financial literacy,
  media exposure, prior beliefs, or interest in the Federal Reserve.
- A policy-surprise gradient does not by itself identify a household's causal
  exposure to the rate change.
- The working paper does not measure realized spending, debt, saving, or
  portfolio changes after the expectation revision.
- The event-study exposure margin is not randomized; people who hear or
  correctly perceive the announcement may differ in attention, financial
  literacy, media use, or prior interest.
- The survey experiment estimates direct expectation responses and excludes
  the indirect and feedback effects of an actual rate change on the wider
  economy.

## Next empirical test

The next pass should acquire the pre-registration and audit its estimand against
the full paper, then extend the action measurement. The action extension should
separate:

1. borrowers, savers, renters, and homeowners;
2. expected inflation from expected borrowing cost and job prospects;
3. policy awareness from actual rate exposure; and
4. stated expectations from observed spending, debt, refinancing, saving, or
   portfolio changes.

The program should pair the result with Federal Reserve price-adaptation and
household-wellbeing evidence, GSS/NBER trust evidence, and financial-record or
credit-market exposure where the units and dates can be aligned. Until then,
the strongest claim is that the research design itself changes the measured
size of the household expectation response.

## Sources and reproduction

- [Machine-readable NBER record](../../../records/us-nber-monetary-policy-information-treatments-2026.json)
- [NBER Working Paper 35090](https://www.nber.org/papers/w35090)
- [Author-hosted August 2026 PDF](https://www.dropbox.com/scl/fi/31mdzavelzr0fuyw9maym/BGKT_2026.pdf?dl=0&rlkey=fh15qmim9kph8ljrtvtq8jusr&st=z1m94vyy)
- [NBER citation/DOI route](https://doi.org/10.3386/w35090)
- [AEA RCT Registry registration](https://www.socialscienceregistry.org/trials/16642)
- [Project source search](../source-search-2026-09-11.md)
- [Project README](../README.md)

The machine record stores the author-hosted PDF hash and the extracted sample,
estimate, uncertainty, subgroup, and design-boundary fields. The PDF is a
working-paper artifact, not a peer-reviewed final publication.

**Evidence status:** full-paper reduced-form survey evidence; expectation
direction, design-sensitive magnitude, prior-knowledge heterogeneity, and
announcement exposure are measured. Realized household action, trust, and
political meaning remain open.
