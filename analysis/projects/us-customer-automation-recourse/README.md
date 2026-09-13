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

This is a short discovery pass. Go deeper only if records show what the system did and what happened to customers afterward.

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

## Scope

- US customers and firms;
- customer service, subscriptions, financial products, insurance, health, housing, and public-facing tools;
- response time, resolution, repeat contact, denial, appeal, complaint, and exit;
- differences by age, income, disability, language, race, and digital access where measured.

## Writing rule

Use simple words. Say what the customer asked, what the system did, whether a person could help, and what the customer lost or gained. Avoid saying “AI transformed service” when all we know is that a tool was installed.

## Matched evidence pass

The first matched check is [A faster answer is not yet a remedy](../../findings/us-customer-automation-matched-evidence-001.md), with its [HTML reading page](../../../site/us-customer-automation-matched-evidence-001.html) and [claims ledger](claims-ledger-v1.md). It confirms a first-contact speed gain while leaving customer remedy and worker authority open.
