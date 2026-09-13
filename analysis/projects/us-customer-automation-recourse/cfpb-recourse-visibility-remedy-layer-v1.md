# CFPB recourse visibility and remedy layer v1

**Checked:** 2026-09-12  
**Source:** [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)  
**Window:** complaints received during calendar year 2024  
**Records:** 2,739,722 published complaints  
**Status:** descriptive institutional record; not a harm rate or remedy rate

This layer sharpens the consumer-power question. It separates the ability to
submit a complaint, the speed of a company response, the response category,
the consumer's narrative voice, and the public visibility of the company's
position. None of these alone proves that the underlying problem was solved or
that the consumer regained trust or exit power.

## What the institution records

| Recorded feature | Count | Share |
|---|---:|---:|
| Submitted through the web | 2,700,500 | 98.568% |
| Submitted by phone | 20,318 | 0.742% |
| Referred | 11,089 | 0.405% |
| Submitted by postal mail | 7,815 | 0.285% |
| Company response marked timely | 2,731,969 | 99.717% |
| Company response marked untimely | 7,753 | 0.283% |
| Closed with non-monetary relief | 1,371,550 | 50.062% |
| Closed with explanation | 1,342,858 | 49.014% |
| Closed with monetary relief | 23,797 | 0.869% |
| Untimely response category | 1,504 | 0.055% |
| Complaint includes a narrative | 815,822 | 29.778% |
| Complaint has no published narrative | 1,923,900 | 70.222% |

The timing figures show a very high rate of responses marked timely. The relief
categories show something different: monetary relief is rare in the full
published snapshot, while non-monetary relief and explanation dominate. A
timely response is therefore not the same thing as a remedy, and a response
category is not an independently verified consumer outcome.

## Public explanation is a separate layer

In 59.954% of records, the company response was recorded as: “Company has
responded to the consumer and the CFPB and chooses not to provide a public
response.” Other public-response categories included the company saying it
acted appropriately under contract or law (1.142%), disputing the facts
(0.071%), describing a misunderstanding (0.027%), or identifying an isolated
error (0.014%). These categories are statements about the company's position,
not adjudications of who was right.

The combination of a highly digital submission channel and mostly absent
public narrative means the database is both a valuable institutional trace and
a filtered visibility system. It records people who reached the complaint
route and published records that passed the database's publication rules; it
does not show all failed attempts, nonusers, people unable to narrate the
problem, or consumers who abandoned the process.

## The end-to-end recourse chain

```text
problem or disputed record
  -> ability to reach the complaint channel
  -> effort, information, and narrative submission
  -> company response and timing
  -> monetary/non-monetary relief, explanation, denial, or silence
  -> repeat contact, correction, switching, non-use, trust, or exit
```

The database measures the middle institutional records. It does not measure
the final consumer outcomes in the same record. That missing link is exactly
where consumer power, dignity, trust, and market exit must be tested.

## Product context matters

The earlier product-stratified layer shows why the national response mix is not
a universal remedy probability: credit-reporting complaints make up 86.519% of
published records, while credit-card and checking/savings records have much
higher monetary-relief shares than mortgage or student-loan records. Product,
issue, user base, complaint propensity, and company response practice all shape
the aggregate.

## What this adds to the broad program

- **Consumer power:** access to a complaint route and a response are separate
  from correction, money, switching, and exit.
- **Platforms and data:** a web-dominant route makes digital access and
  narrative visibility part of institutional participation.
- **Trust and cultural meaning:** an explanation, silence, or disputed account
  may be interpreted differently, but the database does not measure that
  interpretation.
- **Firm and market power:** response categories describe company-facing
  institutional behavior, not market share or underlying harm prevalence.
- **Unequal exposure:** nonusers, non-reporters, offline consumers, and people
  unable to complete the route are part of the missing denominator.

## Next bounded test

Link complaint-level records, where legally and ethically possible, to a
separate consumer panel or repeat-case source. Measure prior product use,
digital access, contact attempts, narrative completion, response, correction,
repeat contact, financial recovery, switching, trust, and non-use. Stratify by
product, issue, company exposure, state, age, income, disability, language,
and channel. Do not treat complaint counts as harm rates or merge them with
SIPP/SHED/ANES respondents as if they were the same people.

Reproduction uses the 2024 API aggregation snapshot described in the
[CFPB complaint-response layer](cfpb-complaint-response-descriptive-layer-v1.md);
the current API field definitions are in the [CFPB field reference](https://cfpb.github.io/api/ccdb/fields.html).
