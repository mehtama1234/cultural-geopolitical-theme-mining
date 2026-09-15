# The visible complaint-response system shifted again in 2025

**Status:** checked · **Checked:** 2026-09-13

## One-sentence finding

Among published CFPB complaint records, the 2025 endpoint contained more
records marked “explanation,” fewer marked non-monetary or monetary relief, and
fewer published narratives than 2024; this is an institutional-record shift,
not evidence that consumer problems became easier or harder to solve.

## What the database records

| Recorded category | 2024 | 2025 |
|---|---:|---:|
| Published records | 2,739,722 | 5,452,107 |
| Explanation | 49.014% | 58.706% |
| Non-monetary relief | 50.062% | 40.633% |
| Monetary relief | 0.869% | 0.480% |
| Narrative present | 29.778% | 22.426% |
| Timely response marked “yes” | 99.717% | 99.549% |

The 2025 response aggregation also contains 0.005% marked “in progress” and
0.176% marked untimely. The response categories are database fields, not
independently verified remedies.

## What changed in the interpretation

The long-run record shows that the visible complaint endpoint is not a fixed
measure of consumer recourse. From 2020 to 2025, the mix of explanation,
non-monetary relief, monetary relief, narratives, products, and publication
conditions changes substantially. The 2025 count is also nearly twice the 2024
count, with credit-reporting complaints still dominant and money-transfer and
checking/savings categories ranking differently than in 2024.

```text
consumer problem
  -> ability and decision to use the CFPB route
  -> publication and product/routing filters
  -> company response label and narrative visibility
  -> possible remedy, correction, repeat effort, exit, or trust change
```

The database observes the middle institutional stages. It does not observe the
full denominator of harmed consumers, failed or abandoned attempts, verified
correction, repeat contact, switching, financial recovery, or meaning.

## Counterinterpretations and limits

- Complaint records are published institutional records, not a representative
  sample of customers or marketplace harm.
- Product mix and complaint propensity can change the pooled response shares;
  credit-reporting complaints dominate both years.
- Publication, routing, company-response, taxonomy, and index timing can change
  the recorded endpoint.
- A timely response is not a verified remedy; explanation or non-monetary relief
  can contain very different consumer outcomes.
- Narrative presence measures public visibility, not voice quality, dignity,
  agreement, or trust.

A stronger end-to-end result requires a linked or repeated case/person design
that follows contact effort, response, correction, repeat contact, financial
outcome, switching or exit, and later trust. Product- and firm-denominated
exposures with account or servicing denominators would also change how much of
the pooled shift can be attributed to institutional practice rather than
composition.

## Sources

- [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [CFPB API field reference](https://cfpb.github.io/api/ccdb/fields.html)
- [Machine-readable annual record](../../../records/us-cfpb-annual-response-trend-2020-2025.json)

The machine-readable record uses the stable trend identifier
`us-cfpb-published-response-endpoint-2020-2025`.
