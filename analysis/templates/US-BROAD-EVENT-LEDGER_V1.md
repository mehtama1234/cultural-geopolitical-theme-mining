# US broad end-to-end event ledger v1

**Purpose:** common schema for testing the broad societal chain across a
consumer, household, worker, care, housing, public-program, firm, place, or
infrastructure event. This template does not require every study to contain
every unit. It prevents a narrative from silently jumping between levels.

The machine-readable design is [the broad event-ledger schema](../../manifests/us-broad-event-ledger-schema-v1.json).
Its [simulated fixture](../samples/US-BROAD-EVENT-LEDGER-SIMULATED_V1.json)
is only a validation aid, never research evidence.

## Design rule

Use one row or record per dated event, decision, case, or project milestone.
Keep observed facts, reported experience, comparison, inference, and unknown
in separate fields. The event can be a price change, service failure, care
need, work rule, benefit interruption, housing shock, firm decision, or
infrastructure investment.

## Core event record

| Field | What to record |
|---|---|
| Event ID | Pseudonymous or public record identifier; never put unnecessary personal identifiers in the research table |
| Unit | Person, household, consumer, worker, case, product, firm, place, institution, project, sector, or country |
| Actor initiating change | Firm, employer, agency, insurer, lender, platform, household, local government, state, foreign actor, or unknown |
| Date and time window | Event date, warning/announcement date, effective date, follow-up dates, and exact versus recalled status |
| Condition or decision | Price, rule, technology, failure, need, investment, ownership, policy, or shock |
| Exposure | Who/what was exposed, intensity, location, eligibility, duration, and comparison group |
| Alternatives before action | Cash, time, provider, job, route, home, family, public program, data refusal, supplier, or no practical alternative |
| Immediate burden or benefit | Money, time, access, control, health, status, privacy, safety, energy, land, or information change |
| Choice or response | Buy, substitute, delay, borrow, work, care, complain, appeal, share, switch, stay, move, organize, invest, deny, or go without |
| Person or actor with control | Who could change the rule, price, schedule, decision, remedy, ownership, or exit terms |
| Remedy or institutional response | Repair, refund, approval, denial, benefit, enforcement, redesign, outage response, regulation, or no response |
| Immediate outcome | What changed for the person, household, worker, customer, firm, place, institution, or state |
| Cost/risk transfer | Who paid, waited, lost access, supplied unpaid labor, accepted risk, or gained control |
| Later outcome | Security, health, work, debt, food, housing, service, quality, trust, identity, market, capacity, or political result at defined follow-up |
| Meaning and attribution | What the affected unit says happened, who is blamed/credited, fairness, dignity, belonging, or legitimacy |
| Public/collective response | Complaint, review, contact, organizing, protest, vote, policy demand, market entry, or withdrawal |
| Evidence status | Observed, reported, estimated, compared, inferred, or open |
| Source and uncertainty | Source, universe, weight, method, missingness, recall, attrition, standard error, and disclosure limits |

## Arrow-level table

For each important link, create a separate row. Do not use one status for the
whole event.

| Arrow ID | From | To | Unit held constant? | Time order valid? | Evidence | Status | Counterexample | Remaining gap |
|---|---|---|---|---|---|---|---|---|
| A-01 |  |  |  |  |  |  |  |  |
| A-02 |  |  |  |  |  |  |  |  |

## Required comparison logic

Every event study should identify, where feasible:

1. exposed and less-exposed units;
2. similar need or condition with different alternatives;
3. a case where the predicted downstream outcome does not occur;
4. subgroup distributions by the resources or status that change practical
   choice;
5. the actor who controls the next step;
6. the outcome that is protected and the outcome that is sacrificed;
7. the follow-up window in which recovery, persistence, or further loss is
   measured.

Use a counterexample to test the mechanism, not merely as an anecdote. If the
unit changes from person to county, firm to sector, or project to country, mark
the transition and do not describe it as a same-unit chain.

## Cross-theme field vocabulary

Use the same concepts across themes while preserving their different measures:

- **Room:** cash, savings, credit, time, care capacity, social support, and
  practical alternatives;
- **Control:** authority over price, rule, schedule, data, remedy, ownership,
  and exit;
- **Exposure:** amount, duration, geography, status, resource, and access
  route;
- **Response:** individual, family, consumer, worker, firm, agency, community,
  or state action;
- **Transfer:** money, time, risk, data, debt, energy, land, attention,
  responsibility, or decision power moved to another actor or future period;
- **Meaning:** fairness, dignity, blame, trust, identity, belonging, legitimacy,
  or political demand;
- **Recovery:** whether the original condition, alternatives, security, and
  control return, remain worse, or are unknown.

## Minimum output for a completed pass

```text
condition / decision
  -> exposure and alternatives
  -> money, time, access, control, or status change
  -> response and remedy
  -> distribution of gain, cost, risk, data, and ownership
  -> later security, meaning, trust, action, capacity, or state leverage
```

The report must state which arrows are directly observed, which are reported or
estimated, which are only cross-source comparisons, which are inferred, and
which remain open. A complete ledger may conclude that the end-to-end link is
not established; that is a valid result.

## Privacy and ethics

Use consent and lawful linkage for person-level records. Minimize identifiers,
separate contact information from analysis data, record retention and access
rules, and avoid publishing combinations that could re-identify people,
workers, customers, patients, or small firms. For public records, document
disclosure avoidance and reporting bias.

## Relationship to the program

This is the general instrument behind the 14-theme map and five priority
bridges. The [safety-net event ledger](US-SAFETY-NET-EVENT-LEDGER_V1.md) and
[household calendar ledger](US-HOUSEHOLD-CALENDAR-EVENT-LEDGER_V1.md) are
specialized versions. Use this broader template when the event crosses
household, consumer, firm, place, institution, infrastructure, or geopolitical
levels.
