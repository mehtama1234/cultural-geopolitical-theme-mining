# Source search: US product recalls and household response

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** matched evidence pass complete; household-level notification and remedy linkage remain open

## Working question

When a dangerous product is recalled, do households hear about it, act on it, and recover what they lost?

## Sources

| ID | Source | What it tells us | Limit |
|---|---|---|---|
| CPSC-RECALL-EFFECT | [CPSC: Recall effectiveness](https://www.cpsc.gov/Recall-Effectiveness) | CPSC defines success as reducing the hazard, notifying consumers, and encouraging them to act. | Definition and workshop record do not measure success for every recall. |
| CPSC-RECALL-DATA | [CPSC recalls and warnings](https://www.cpsc.gov/Recalls) | The public data include recall dates, hazards, remedies, and downloadable records; remedy availability can change over time. | A listed remedy is not proof that each household received it. |
| NBER-TOY-RECALLS-15183 | [NBER: Product recalls, imperfect information, and spillovers](https://www.nber.org/papers/w15183) | The 2007 toy recall wave reduced sales of recalled products and changed demand for related toy products; the paper studies imperfect consumer information and reputation effects. | Historical toy recalls are not a current online-marketplace estimate. |
| CPSC-NOTIFICATION | [CPSC: Recall notification types](https://www.cpsc.gov/Business--Manufacturing/Recall-Guidance/Recall-Notification-Types?language=en) | Direct email, retailer loyalty programs, search advertising, social media, and other channels can be used to reach consumers. | Notification plans do not show that the message reached or changed a household. |

## First pattern to test

```text
hazard found
  -> recall notice reaches household or misses it
  -> product is stopped, returned, repaired, or replaced
  -> injury and money loss are reduced or continue
  -> trust in seller, brand, platform, and public system changes
```

## Decision rule

Keep notice reach, household exposure, customer action, remedy completion, injury, and trust separate until household records join them.
