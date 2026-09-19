# US broad retained same-unit bridge matrix v1

**Checked:** 2026-09-19
**Purpose:** identify what the strongest retained same-unit routes actually
close in the broad end-to-end model. This is a bridge audit, not a pooled
estimate or a claim that the rows describe the same people.

## Required chain

```text
dated condition or event
  -> alternative / non-use
  -> money, time, access, or control trade-off
  -> institutional response
  -> protected or sacrificed outcome
  -> verified remedy / recovery
  -> persistence
  -> meaning, trust, action, or exit
```

| Retained route | Same-unit evidence actually observed | Strongest closed bridge | Still missing or weak |
|---|---|---|---|
| [MEPS dated event → later panel](projects/us-household-constraint-cascade/meps-event-six-month-followup-v1.md) | Person-level event window before R4/2 context, then R5/3 health and employment levels and conditional transitions; BRR-weighted descriptive denominators | Dated event → later health/work status or transition | Event may follow the real need; no alternative, payer/claim identity, treatment continuity, institutional response, verified remedy, trust, action, or exit |
| [SHED 2024→2025 persistence](projects/us-household-financial-pressure/shed-2024-2025-panel-persistence-layer-v1.md) | Same respondent’s financial condition and reported substitutions, reduced use, borrowing, savings cuts, delayed purchases, and extra work across two waves | Financial pressure/adaptation → persistence or partial reversal | Trigger is not transaction-dated; alternatives, actor, institutional response, protected outcome, remedy, trust, action, and exit are absent |
| [CCES 2010→2014 job-loss panel](projects/us-cost-trust-politics/cces-panel-job-loss-political-followup-v1.md) | Same panel respondent’s earlier reported job loss/benefit cut, later insurance status, Congress judgment, contact, and local political action | Earlier work disruption → later institutional judgment/action | Separation date, employer, alternatives, trade-off, remedy, recovery, attribution change, and causal interpretation are absent |
| [HTOPS April→June fraud follow-up](projects/us-cost-trust-politics/htops-2025-fraud-followup-v1.md) | 6,564 exact SCRAMID links; retrospective exposure, reported loss, agency/law-enforcement reporting, sparse self-reported recovery, then later food, energy, work-loss, and institutional items | Exposure → realized loss/report/reported recovery → later household context | Incident date, actor, alternatives, effort, verified remedy, prior-to-later trust/action change, and switching/exit are absent; recovery cell has 11 respondents |
| [CFPB Ombudsman redress reissue example](projects/us-customer-automation-recourse/cfpb-ombudsman-redress-reissue-route-v1.md) | One illustrative recipient-side case: expired check → reissue request → difficulty obtaining reissue → Ombudsman-facilitated administrator route | Formal remedy access failure → recipient effort/escalation → facilitated institutional response | Final delivery, cashing, amount, adequacy, residual loss, recovery, trust, switching, and exit are absent; illustrative case is not a population estimate |
| [DOJ IER DACA rehire and status repair](projects/ai-work-control/ier-daca-rehire-wage-seniority-record-v1.md) | One agency-reported worker case: document/status problem → termination and lower-wage rehire → worker submission → bilateral agreement → prior wage, $4,712.50 back pay, and seniority restored; complaint withdrawn | Employment-status exposure → worker action → institutional correction → wage and status remedy | Alternatives, independent payment confirmation, benefit use, durable employment, household recovery, trust, recurrence, and exit are absent; selected agency case is not a prevalence estimate |

## What this proves

The broad program has real bridges at six different points in
the chain:

1. **MEPS** supplies event-to-later-outcome timing.
2. **SHED** supplies adaptation persistence and reversal.
3. **CCES** supplies later judgment and action after a prior disruption.
4. **HTOPS** separates exposure, realized loss, reporting, self-reported recovery, and later household context for linked respondents.
5. **CFPB Ombudsman** follows a recipient-side remedy-access failure into effort, escalation, and facilitated reissuance without pretending that facilitation equals receipt.
6. **DOJ IER** supplies a compact remedy-stage case in which worker action is
   followed by restored wage and seniority, while durable employment and later
   meaning remain unobserved.

Together they support a structured research model. They do **not** support
joining medical events, financial adaptation, and job loss into one household
or one population pathway. The missing middle is not merely “more data”; it is
specific fields: usable alternatives, event-specific institutional response,
verified remedy or recovery, and direct meaning/action after the episode.

## Cross-route cultural reading

The six bridges also reject a simple hardship-to-backlash story. MEPS shows
that later health and work movement can run in mixed directions after a dated
medical event. SHED shows that people can improve in broad financial condition
while continuing some substitutions, borrowing, or reduced use. CCES shows
that earlier job loss or insurance insecurity can coexist with different
levels of institutional approval, contact, and local political action. HTOPS
shows that exposure, realized loss, reporting, and reported recovery can be
separated from later food, energy, and work-loss conditions. In
the CFPB Ombudsman example, a formal redress route exists but is not immediately
usable: the recipient must spend effort and escalate before a reissuance route is
facilitated, and the public record still ends before receipt. In
the DOJ IER case, complaint withdrawal follows a reported wage and status
repair, but does not establish durable trust or security. In plain terms: people
do not respond to pressure with one universal sequence.

They may conserve, delay, borrow, work more, stay attached to an institution,
contact it, withdraw from it, or act politically—and these choices are not
interchangeable measures of trust or resistance. The missing same-episode
fields are therefore culturally important: they would show whether a response
was experienced as necessity, dignity-preserving adaptation, resignation,
fairness, betrayal, efficacy, or collective opportunity. The current evidence
supports that as a testable proposition, not as a measured universal meaning.

## Acquisition consequence

The next high-value route must preserve a same-unit key and add at least:

- a dated or bounded trigger and responsible actor;
- the alternative, non-use, or refusal decision;
- money, time, access, or control cost;
- institutional response and remedy receipt or defined outcome follow-up;
- later persistence, trust, action, switching, or exit.

An aggregate exposure, complaint, settlement, or sentiment cross-tab does not
fill these fields. The authorized UAS/PSID/HRS routes remain the strongest
documented acquisition candidates; the retained MEPS, SHED, CCES, HTOPS, and CFPB
Ombudsman routes
remain the comparison anchors and counterexamples.

## Interpretation boundary

All five routes are descriptive or compared designs with source-specific
weights, missingness, selection, and timing limits. A bridge status means the
specified adjacent stages are observed for the same unit; it does not mean the
upstream condition caused the downstream result.
