# Project: US customer service, automation, and the right to reach a person

## Question

When a company uses software or AI to answer, sort, price, or deny, can a customer still understand the decision and reach a person who can change it?

## Short end-to-end goal

Trace customer contact from the firm's tool and business aim to the speed, quality, and fairness of the answer, then to the customer's ability to appeal and the regulator's ability to act.

```text
firm cost or growth goal
  -> automated reply, screen, price, or route
  -> customer gets help, delay, denial, or confusion
  -> trust, purchase, complaint, or exit changes
  -> firm, worker, regulator, or court responds
  -> who has a real way to challenge the result
```

This is one durable lane in the long-term atlas. Its depth increases as records show what the system did and what happened to customers afterward.

## First working idea

Automation may improve service for simple questions while making repeated problems harder to solve. The key issue may not be whether a bot is friendly; it may be whether a customer can get a clear answer, a human review, and a remedy. This is a working idea, not a conclusion.

The first current institutional measurement layer is the [CFPB complaint → response descriptive layer](cfpb-complaint-response-descriptive-layer-v1.md). It records complaint volume and response categories while preserving the limits that a published complaint is not a representative consumer sample and a company response is not necessarily a remedy.

The first place-normalized extension is the [CFPB geography layer](cfpb-state-population-normalized-layer-v1.md), which pairs state complaint counts with Census resident-population estimates and explicitly does not treat the result as a consumer-harm rate.

The [CFPB recourse visibility and remedy layer](cfpb-recourse-visibility-remedy-layer-v1.md)
adds submission channel, narrative presence, and public-response categories.
It shows that a timely company response, a published explanation, non-monetary
relief, and a verified consumer remedy are different institutional outcomes.

The [CFPB 2025 process-scale and screening layer](cfpb-2025-process-scale-shift-layer-v1.md)
adds the institution's own changing data-production problem: complaint volume,
routing, duplicate and fraud screening, company response, and publication are
separate stages. A larger visible complaint total is not automatically a
larger consumer-harm rate.

The [CFPB 2025 product-response asymmetry layer](cfpb-2025-product-response-asymmetry-layer-v1.md)
adds product-specific depth: explanations, monetary relief, non-monetary relief,
administrative responses, prior contact, and untimely responses vary sharply by
financial product. A response category is not a universal remedy probability.

The [CFPB 2025 consumer-financial cultural themes layer](cfpb-2025-consumer-financial-cultural-themes-layer-v1.md)
extracts recurring meanings from the complaint narratives and product summaries:
identity and data control, access to essential money, rule legibility, human
reach, timing, dependence, exit, and explanation versus repair. These are
themes to measure, not representative cultural frequencies.

The [2026-09-13 CFPB aggregation refresh](cfpb-2024-aggregation-refresh-2026-09-13.md)
updates the current API metadata and records a reusable aggregate-only fetch
route. It keeps this institutional-response lane current while preserving the
open verified-remedy, repeat-effort, trust, and exit arrows.

The [2020–2025 annual response trend](cfpb-annual-response-trend-2020-2025-v1.md)
adds time to the complaint-system layer. It shows a changing recorded endpoint
mix, while preserving the product-taxonomy and publication-rule breaks that
prevent a direct consumer-remedy trend claim.

The [2024 case-route sample](cfpb-case-route-sample-2024-v1.md) adds the next
institutional handoff: case-level time from CFPB receipt to company routing,
submission channel, narrative visibility, public-response visibility, and
product-conditioned response labels. It is a capped retrieval-order sample,
so it does not estimate population route rates or verified remedy. The durable
open arrow remains contact/notice → effort → decision → remedy → repeat effort,
trust, switching, and exit.

The [consumer loss and complaint visibility finding](findings/us-customer-automation-recourse-018.md)
now places that institutional handoff beside Federal Reserve/SHED household
fraud and recovery evidence. It preserves the distinct denominators and makes
the missing same-customer remedy and exit link explicit.

The [consumer-outcome field audit](cfpb-consumer-outcome-field-audit-v1.md)
records a fixed public-API probe showing that the current fields do not provide
a usable consumer-dispute, verified-correction, repeat-effort, recovery,
switching, trust, or exit outcome. Response categories therefore remain
institutional endpoints rather than remedy rates.

The [2026-09-14 public event-ledger acquisition audit](cfpb-public-event-ledger-acquisition-audit-2026-09-14.md)
turns 25 public 2024 student-loan records into a validated, de-identified
administrative route ledger. It observes receipt, routing, channel, narrative
visibility, timeliness, and response labels, while explicitly leaving verified
remedy, repeat effort, trust, switching, and exit open.
The same memo is available as the [published HTML reading page](../../../site/cfpb-public-event-ledger-acquisition-audit-2026-09-14.html).
The [committed de-identified event ledger](data/cfpb-student-loan-event-ledger-2024-25.json)
preserves the 25-case route extract for direct contract validation and later
reproduction.

The [bounded event-ledger finding](findings/us-customer-automation-recourse-019.md)
promotes this route-stage evidence into the canonical reading set. It records
what the public API can hold constant on a case while keeping the capped
retrieval-order denominator, response-label boundary, and missing verified
remedy, repeat effort, trust, switching, and exit fields explicit.

The [2026-09-14 API vintage refresh](cfpb-api-vintage-refresh-2026-09-14.md)
confirms that the 2025 route facets are unchanged while the database index
metadata advanced by one day and 8,030 records.

The reader-facing [consumer-recourse visibility and remedy synthesis](consumer-recourse-visibility-remedy-synthesis-v1.md)
connects household fraud/loss evidence to CFPB complaint visibility, product
response labels, routing clocks, API schema changes, and the still-unobserved
customer endpoint: verified correction, repeat effort, trust, switching, and
exit.

The [practical-exit cross-domain synthesis](practical-exit-cross-domain-synthesis-v1.md)
advances this lane as the first broad-program rotation. It compares household
fraud, CFPB recourse, CPSC product safety, and platform-worker remedy without
pooling their units, and defines practical exit as the next consumer-power
outcome to measure.

## Scope

- US customers and firms;
- customer service, subscriptions, financial products, insurance, health, housing, and public-facing tools;
- response time, resolution, repeat contact, denial, appeal, complaint, and exit;
- differences by age, income, disability, language, race, and digital access where measured.

## Writing rule

Use simple words. Say what the customer asked, what the system did, whether a person could help, and what the customer lost or gained. Avoid saying “AI transformed service” when all we know is that a tool was installed.

## Matched evidence pass

The first matched check is [A faster answer is not yet a remedy](../../findings/us-customer-automation-matched-evidence-001.md), with its [HTML reading page](../../../site/us-customer-automation-matched-evidence-001.html) and [claims ledger](claims-ledger-v1.md). It confirms a first-contact speed gain while leaving customer remedy and worker authority open.
