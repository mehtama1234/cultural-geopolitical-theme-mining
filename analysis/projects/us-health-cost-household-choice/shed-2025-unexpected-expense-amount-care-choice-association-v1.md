# SHED 2025 unexpected-expense amount and care-choice association v1

## Question and boundary

Among respondents reporting an unexpected major medical expense in the prior
12 months, does the reported amount band coincide with different rates of
cost-related care foregoing, insurance coverage, outside-household help, debt,
borrowing, or delayed major purchases?

This is a same-respondent weighted cross-tab. It narrows the mechanism between
an expense shock and household choice, but it is not a dated episode: the
survey does not establish that the amount, skipped care, debt, help, and
adaptation refer to the same bill or order them in time.

## Result

| Unexpected expense amount | Respondents | Any care skipped | Insured | Medical debt | Outside help | Delayed major purchase | Increased borrowing |
|---|---:|---:|---:|---:|---:|---:|---:|
| $1 to $499 | 455 | 51.55% | 92.13% | 39.21% | 16.79% | 66.72% | 27.04% |
| $500 to $999 | 562 | 49.51% | 92.31% | 43.46% | 9.71% | 62.67% | 24.78% |
| $1,000 to $1,999 | 559 | 38.67% | 94.85% | 42.01% | 10.80% | 59.18% | 21.39% |
| $2,000 to $4,999 | 659 | 39.20% | 96.42% | 45.95% | 8.18% | 57.90% | 21.09% |
| $5,000 or higher | 417 | 39.44% | 93.03% | 54.72% | 10.97% | 59.25% | 24.23% |
| Don’t know | 208 | 44.24% | 85.11% | 49.92% | 8.84% | 58.14% | 24.54% |

The amount gradient is not a simple monotonic care-foregoing gradient. The
smallest known bands have the highest reported foregoing shares, while the
largest band has the highest medical-debt share. This is consistent with more
than one mechanism: a modest bill may still trigger immediate care avoidance
for a household with little room, while a large bill may be absorbed through
coverage or payment but remain as debt. Delayed purchases are high across all
bands, showing a broad household-security trade-off rather than a single
medical endpoint.

Outside-household help is highest in the $1-to-$499 band. That pattern should
not be read as a lower-burden result: help may be a protective alternative,
evidence of social support, or a response to hardship. The survey does not
identify amount transferred, giver, timing, conditions, or whether the help
prevented care foregoing.

## What this moves in the end-to-end chain

This layer moves the amount-to-choice arrow from an unstructured open question
to a reported/compared association. It shows that amount bands separate some
outcomes, but do not determine the household route by themselves. Coverage,
liquid resources, illness severity, plan design, access, and prior debt remain
unmeasured or entangled in this cross-tab.

The next decisive join remains a dated episode or a valid panel: amount owed,
benefit and network context, feasible alternatives, care decision, payment
timing, protected and sacrificed household outcomes, and follow-up health or
work result in one unit.

## Reproduction

```text
python3 scripts/analyze_shed_care_skipping_adaptation.py \
  --input /tmp/cgtm-shed/shed2025.zip \
  --output analysis/projects/us-health-cost-household-choice/data/us-shed-2025-care-skipping-adaptation-association.json
```

## Source

The variables and response universes are documented in the Federal Reserve
[2025 SHED codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2025codebook.pdf).
The public archive is maintained on the Federal Reserve [SHED data page](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
