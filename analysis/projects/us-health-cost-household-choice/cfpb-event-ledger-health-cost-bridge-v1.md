# CFPB event-ledger contract for the health-cost remedy gap v1

**Checked:** 2026-09-15  
**Status:** implementation bridge; not a medical-complaint estimate

## Purpose

The health-cost lane needs an institutional middle between a household burden
and a later recovery or legitimacy outcome. The CFPB public complaint ledger
shows what a usable administrative event contract looks like. The [medical-
debt query audit](cfpb-medical-debt-event-ledger-audit-v1.md) now demonstrates
that contract on the `Debt collection` / `Medical debt` route, using a bounded
25-case retrieval sample. It is not a medical-burden or remedy estimate and
must not be merged with MEPS respondents.

The bridge is useful because it separates three questions that are often
collapsed:

1. Did a person reach an institutional route?
2. What did the institution record as its response?
3. Did the person receive a correction, recover money or security, switch, or
   change trust?

The public CFPB ledger answers parts of the first two questions. It does not
answer the third.

## Field map

| Health-cost episode requirement | CFPB public ledger field or derived field | Status | Boundary |
|---|---|---|---|
| Dated institutional contact | Complaint receipt date and de-identified case key | Available in the bounded extract | A complaint is a selected route; non-users and abandoned attempts are outside the denominator |
| Route and access | Submission channel, narrative-present flag, product and state | Available in the bounded extract | Channel is not the full cost of effort, digital access, language access, or ability to complete a complaint |
| Institutional handoff | Date sent to company and receipt-to-send lag | Available in the bounded extract | Routing is not proof that the correct institution had authority to fix the problem |
| Response | Timely label, company-response label, public-response flag | Available in the bounded extract | A response category is not an adjudication or verified remedy |
| Health-cost exposure | Medical bill, care need, coverage rule, denial, or treatment episode | Not supplied by the committed student-loan extract | A different product query or linked health source would be required; no medical linkage is claimed here |
| Obligation and household trade-off | Amount owed, due date, payment, debt, work/time, food/housing, or care substitution | Not supplied | Complaint narrative presence is not narrative meaning, and no outcome is inferred from the response label |
| Remedy | Verified correction, money recovered, account change, care restored, or burden removed | Not supplied | “Non-monetary relief” and “closed with explanation” remain administrative labels |
| Persistence and exit | Repeat contact, appeal, switching, continued use from dependence, trust, or exit | Not supplied | Requires same-case follow-up or a valid linked panel with timing and retention |

## How this changes the health-cost design

The public ledger supplies an implementable institutional-route layer for the
episode protocol:

```text
health-cost exposure and choice
  -> complaint receipt and route effort
  -> institutional handoff and response
  -> verified correction or burden transfer
  -> household recovery, repeat effort, trust, switching, or exit
```

Only the middle route and response boxes are directly represented by the
current public administrative contract. MEPS supplies event channels,
annual denial/prior-authorization context, payment, care delay, debt, and
financial-room fields; SHED supplies care-foregoing and adaptation surfaces;
ANES/CES supply separate judgment and action surfaces. Their identifiers are
not compatible with the CFPB complaint ledger, so the arrows between them stay
layered or open.

## Promotion rule for a medical extension

Do not promote a medical CFPB query as a health-cost remedy result unless the
retrieval first demonstrates:

- the exact product, sub-product, issue, and date filter;
- the returned universe and whether the extract is a full query or a capped
  sample;
- stable case keys, receipt and routing dates, response labels, and missingness;
- explicit separation of response category from verified remedy; and
- a documented plan for linking or following the case to amount owed, dispute,
  correction, repeat contact, recovery, switching, or exit.

If those fields are absent, publish the query as an acquisition boundary and
retain the student-loan ledger only as an implementation demonstration.

## Reproduction and related records

The source implementation is the [CFPB public event-ledger acquisition audit](../us-customer-automation-recourse/cfpb-public-event-ledger-acquisition-audit-2026-09-14.md)
and its [de-identified sample ledger](../us-customer-automation-recourse/data/cfpb-student-loan-event-ledger-2024-25.json). The governing health-cost design is the [health-cost episode acquisition protocol](health-cost-episode-acquisition-protocol-v1.md).

The public CFPB database is not a statistical sample of all consumer
experiences. Complaint counts, response labels, and publication visibility
must not be interpreted as medical-burden prevalence, remedy rates, or trust
effects.
