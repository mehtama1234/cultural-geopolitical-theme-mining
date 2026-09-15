# Source search: US customer service, automation, and the right to reach a person

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** short verification pass; speed and remedy remain separate questions

## Working question

Does automated customer service make simple help faster while making difficult problems harder to understand and challenge?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-HBS-CUSTOMER-AI-2025 | [HBS: When AI Chatbots Help People Act More Human](https://www.library.hbs.edu/working-knowledge/when-ai-chatbots-help-people-be-more-human) | A field experiment with 138 agents and 256,934 chats found faster responses and higher measured customer sentiment when agents received AI suggestions; effects varied by experience and customer intent | Research story describing a randomized field experiment | One meal-delivery company; customer sentiment was measured by an AI tool; the underlying paper needs review |
| US-NBER-GEN-AI-WORK-2023 | [NBER Working Paper 31161](https://www.nber.org/papers/w31161) | AI support increased issues resolved per hour by 13.8%; the reported chat-resolution increase was 1.3 percentage points and customer satisfaction did not change significantly | Quasi-experimental study of about 5,000 support agents at a US software company | The tool supported human agents in one company; appeal, repeat complaints and an agent's power to overturn a decision were not tested |
| US-HBS-HUMAN-CONTACT-2019 | [HBS: Can I Please Speak to an Actual Person?](https://www.library.hbs.edu/working-knowledge/infographic-can-i-please-speak-to-an-actual-person) | HBS research says customers value access to human help even when they do not use it | Research story | Older study and narrow question; access is not the same as successful remedy |
| US-FTC-DONOTPAY-2025 | [FTC order on DoNotPay](https://www.ftc.gov/news-events/news/press-releases/2025/02/ftc-finalizes-order-donotpay-prohibits-deceptive-ai-lawyer-claims-imposes-monetary-relief-requires) | FTC required the company to stop unsupported claims that its chatbot worked like a human lawyer and provide monetary relief and notices | Official enforcement record | One company and one product; does not measure the full market |
| US-FTC-AI-CHATBOTS-2025 | [FTC inquiry into AI companion chatbots](https://search.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions) | FTC requested information on safety testing, monitoring, monetization, disclosures, data use, and effects on children and teens | Official inquiry | Information request is not a finding of harm |
| US-FTC-JOINT-AI-2023 | [Federal agency joint statement on automated systems](https://www.ftc.gov/system/files/ftc_gov/pdf/EEOC-CRT-FTC-CFPB-AI-Joint-Statement%28final%29.pdf) | FTC, CFPB, DOJ, and EEOC said existing laws apply to automated systems in consumer protection, civil rights, fair competition, and equal opportunity | Official policy statement | A statement of enforcement principles, not evidence of a particular customer outcome |
| US-FED-SHED-AI-2025 | [Federal Reserve 2025 employment and job-quality findings](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-employment-and-job-quality.htm) | One in four workers used generative AI at work in the prior month; use was 43% among workers with graduate degrees and 10% among those with a high-school degree or less. Workers with more control over how they complete tasks were also more likely to use it. | Official household survey | This measures worker use and views, not customer remedy or firm-level service quality |

## First pattern to test

```text
firm uses automated service
  -> speed or cost changes
  -> customer resolution, confusion, denial, or repeat contact
  -> trust, complaint, purchase, or exit
  -> human review, enforcement, or no remedy
```

The HBS experiment supports a possible benefit for some service work. The FTC records show why claims, safety, and remedy matter. The customer-side failure path remains open.

## Main gaps

- outcomes for repeat complaints and difficult cases;
- whether a human can actually overturn an automated result;
- differences by disability, language, age, income, and digital access;
- customer complaints matched to the tool or firm;
- worker discretion after AI suggestions are introduced;
- who gets the tool and who keeps control over the work after it arrives;
- data use, error rates, and false claims;
- evidence that automated service improves remedies rather than only speed.

## Decision rule

Find one US firm or agency with public complaint, service, or appeal records and compare automated and human paths. If only company claims are available, record the promise and move on.
## Verification pass: 2026-09-11

The HBS account of a randomized field experiment reports that AI suggestions helped 138 meal-delivery support agents respond 22% faster across 256,934 chats and raised measured customer sentiment by 0.45 points on a five-point scale. The effect was larger for less-experienced agents. The study also found less improvement for repeat complaints and some confusion after very fast transfers from a chatbot to a person.

This gives a sharper question than “does AI improve service?” It may improve the first reply while doing less for the case that needs a second explanation, an exception or a decision changed. The CFPB’s 2025 annual report covers consumer complaints submitted during 2025, but complaint records still need to be matched to service path and remedy before they can show that effect.

[HBS AI and customer service experiment](https://www.library.hbs.edu/working-knowledge/when-ai-chatbots-help-people-be-more-human)

[CFPB 2025 Consumer Response Annual Report](https://www.consumerfinance.gov/data-research/research-reports/2025-consumer-response-annual-report/)

## Current API refresh: 2026-09-13

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-CFPB-CCDB-API-2026-09-13 | [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/) | The official API returned 2,739,722 published records received during 2024; current index metadata reported 17,729,722 records, last updated/indexed 2026-09-13 12:00 ET, with stale and data-issue flags false | Current aggregate API refresh; retrieval hash preserved by the [aggregate fetcher](../../../scripts/fetch_cfpb_complaint_aggregation.py) | Published complaints are not a representative marketplace sample; response categories are not verified remedies and cannot show switching, trust, or consumer harm rates |
| US-CFPB-CCDB-API-DOCS-2026-09-13 | [CFPB complaint database API documentation](https://cfpb.github.io/api/ccdb/api.html) | Documents the trailing-slash API server and query fields used for date and product filtering | Official API documentation | API availability and field definitions can change; preserve the request URL and retrieval hash for each snapshot |

The detailed refresh record is [CFPB 2024 complaint aggregation refresh](cfpb-2024-aggregation-refresh-2026-09-13.md). It advances the institutional-response stage while leaving the same-case verified-remedy, repeat-effort, trust, and exit stages open.

The [2020–2025 annual response trend](cfpb-annual-response-trend-2020-2025-v1.md)
adds comparable annual aggregate snapshots. The visible response mix changes
over time, but taxonomy, routing, publication, and complaint-selection changes
remain counterinterpretations; this is not a consumer-remedy trend.
