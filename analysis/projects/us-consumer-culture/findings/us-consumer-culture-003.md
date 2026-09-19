# Finding 003: Material pressure changes what people search for more than whether they use AI

**Status:** provisional same-round HTOPS consumer-culture finding  
**Checked:** 2026-09-19  
**Field window:** June 2025 HTOPS/HPS 2506 topical file  
**Unit:** responding person, conditioned on household-reported expense difficulty

## The bounded finding

In the June 2025 Census household file, household expense difficulty is not
monotonically related to whether respondents report any recent AI use. It is,
however, strongly related to what people are searching for online: jobs,
housing, food, medical assistance, public benefits, and credit or loans.

The simple reading is not “poor households use more AI.” The stronger and more
interesting reading is: **when room gets tight, search becomes a practical
navigation behavior across several systems at once.** The file cannot tell us
whether the search produced a usable option, whether an AI system was involved,
or whether the person later switched, received help, or recovered.

## Weighted results

Percentages are weighted valid shares within each expense-difficulty group;
numbers in parentheses are successive-difference replicate standard errors in
percentage points. Group `n` is the unweighted respondent count for the broad
valid AI/search universe; the AI-trust measure has a smaller AI-user universe.

| Expense difficulty | n | Any AI use | Job search | Housing search | Food search | Medical search | Benefits search | Credit search | AI-trust statement* | Opted out |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Not at all difficult | 4,416 | 59.0 (0.6) | 20.7 (0.6) | 13.3 (0.5) | 15.9 (0.5) | 10.6 (0.3) | 10.7 (0.3) | 10.0 (0.3) | 12.5 (0.6) | 22.7 (0.5) |
| A little difficult | 2,013 | 52.4 (1.1) | 35.5 (1.0) | 14.6 (0.7) | 22.2 (1.0) | 14.4 (0.8) | 15.6 (0.8) | 18.9 (0.9) | 14.7 (1.1) | 23.7 (0.8) |
| Somewhat difficult | 684 | 53.9 (1.7) | 51.9 (1.7) | 21.8 (1.5) | 24.6 (1.2) | 16.5 (0.9) | 22.9 (1.5) | 24.5 (1.3) | 15.1 (1.7) | 26.7 (1.5) |
| Very difficult | 350 | 58.4 (2.3) | 57.0 (2.7) | 29.1 (2.0) | 32.5 (2.1) | 23.5 (1.7) | 29.0 (2.0) | 27.0 (2.2) | 14.4 (1.8) | 29.1 (2.1) |

\* `AI-trust statement` is the share of valid AI users selecting the statement
“I trust information from AI systems”; it is not a general trust scale.

The clearest gradients are in the search behaviors. Comparing “not at all”
with “very difficult,” job searching rises from 20.7% to 57.0%, food searching
from 15.9% to 32.5%, benefits searching from 10.7% to 29.0%, and credit
searching from 10.0% to 27.0%. Housing and medical searches also rise. By
contrast, any AI use is 59.0% in the first group and 58.4% in the last group,
with lower middle cells. That is not a monotonic adoption gradient.

## What this adds to the broad atlas

### 1. Consumer behavior is often search before purchase

Under pressure, people may be searching for a job, a home, food, care, public
benefits, or credit—not simply buying less. Search is an early-stage behavior
that can reveal constrained option-building before a completed transaction,
application, remedy, or exit is visible.

### 2. Digital navigation is not the same as digital power

The same respondent can search more while still lacking a usable alternative.
Search frequency does not show whether information was accurate, affordable,
accessible, trusted, or acted upon. It is an effort and option-discovery signal,
not a welfare or recovery measure.

### 3. AI adoption and material navigation are different currencies

The pressure gradient is strong for online searches but not for broad AI use.
This warns against using AI adoption as a proxy for economic adaptation. People
may use ordinary search, public-service websites, family networks, or multiple
routes without using an AI system; or they may use AI for work and creative
tasks unrelated to the immediate material problem.

## Need-to-search check

The same-round file also lets us compare a few concrete need flags with the
corresponding search behavior. These are weighted valid shares; standard
errors are in parentheses.

| Current need flag | Targeted online search when need is present | When need is absent |
|---|---:|---:|
| Recent household job loss → job search | 60.5% (2.3) | 29.4% (0.6) |
| Food insufficiency → food search | 35.3% (2.2) | 19.1% (0.5) |
| Energy-bill problem → public-benefit search | 27.8% (1.8) | 13.3% (0.3) |
| Basic-expense cutback → credit search | 31.4% (1.5) | 13.7% (0.4) |
| Housing arrears → housing search | 20.9% (2.0) | 18.2% (3.6) |

This strengthens the interpretation from a general hardship gradient to a
more specific navigation pattern: the search object often matches the current
problem. The housing-arrears comparison is weaker and noisy, so it is retained
as a counterexample rather than folded into a universal rule. The checks remain
same-round associations; they do not show that the search found a resource or
solved the problem.

### 4. Opt-out rises modestly while search rises sharply

Active opt-out moves from 22.7% to 29.1% across the expense categories, while
job and benefit searches rise much more. This is consistent with a tension
between needing more navigation and retaining reservations about digital
systems. The cross-section cannot establish that expense pressure caused either
pattern.

## What this does not establish

- Expense difficulty did not necessarily cause any search behavior.
- The searches may have been made by someone else in the household or for a
  purpose unrelated to the respondent’s own hardship.
- The file does not identify the search engine, result quality, AI involvement,
  provider, price, application, approval, or remedy.
- AI trust is a selected statement among AI users, not trust in a specific
  institution or a measure of successful decision-making.
- Opting out is not the same as abandoning digital services or exiting a
  market.
- This is one June 2025 cross-section, not a panel and not an end-to-end causal
  chain.

## Next decisive test

The stronger route would follow a dated need or search through:

```text
material pressure or service need
  -> search and available alternatives
  -> selected route, effort, time, and cost
  -> completion, abandonment, or institutional response
  -> remedy, usable outcome, trust, switching, or exit
```

The PSID/UAS acquisition routes remain better for later same-person outcomes.
This HTOPS screen adds a useful consumer-culture middle signal while preserving
the distinction between looking for an option and actually obtaining one.

## Reproducibility and storage boundary

The PUF and replicate CSVs were read from temporary storage and are not added
to the repository. The PUF has SHA-256
`938e2a667469cc4e81067f01269967608282f31be0bc0814b07e2667ab0cfba2`; the
replicate file has SHA-256
`c75c291dd260a83eeb5b884193ee119d5fcde60c03b9ecec0ba7706489cfaea7`.

The machine-readable result is [the HTOPS screen](../data/htops-2025-expense-online-search-ai-trust-screen-v1.json).
The reproduction script is
[`analyze_htops_2025_ai_material_search.py`](../../../../scripts/analyze_htops_2025_ai_material_search.py).
The official source is the [Census HTOPS/HPS dataset listing](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html).
