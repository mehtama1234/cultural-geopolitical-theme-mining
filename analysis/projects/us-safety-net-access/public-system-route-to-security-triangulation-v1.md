# Public-system route to security: a cross-source triangulation

**Status:** end-to-end synthesis with deliberately non-pooled evidence  
**Updated:** 2026-09-14  
**Question:** What can be said, and what remains open, about the path from SNAP need or eligibility to route completion, receipt, interruption, and material security?  
**Machine record:** `analysis/records/us-public-system-route-security-triangulation-2026.json`

## Why this synthesis exists

The public-system lane now has several evidence types. They answer different questions:

1. official state quality-control measures of processing timeliness;
2. respondent reports of notice, time, paperwork, interview, and interruption;
3. administrative or experimental studies that change route design and observe participation;
4. SIPP person-month transitions paired with following rent/mortgage and utility hardship;
5. WBNS charitable-food participation, access, treatment, and unmet need as a mixed-safety-net route.

The end-to-end program needs these layers read together without pretending they are one dataset. The synthesis below preserves the chain while keeping units, years, denominators, and designs visible.

## The chain and the evidence at each stage

```text
need / eligibility / rule exposure
  -> notice, office, interview, document, deadline, or work-reporting route
  -> approval, procedural denial, recertification failure, churn, or continued receipt
  -> benefit timing and amount
  -> food, housing, utility, work, health, and time security
  -> interpretation, trust, appeal, complaint, political action, or policy response
```

| Stage | Evidence layer | What is observed | What remains open |
|---|---|---|---|
| Administrative route performance | USDA/FNA FY2025 APT/RPT state tables | State-level processing timeliness distributions; APT 61.24–97.22%, RPT 25.23–99.87% across 51 states/DC | Household effort, notice comprehension, exact gap, benefit amount, subgroup concentration |
| Lived route exposure | Urban December 2024 WBNS | 24% reported involuntary interruption; 13% cited inability to recertify on time; notice/time/paperwork/interview barriers | Linked case verification, exact dates, gap days, correction, appeal, amount |
| Route intervention | NBER field and administrative studies | Flexible interviews increased approvals and longer-term participation; office access and work rules changed participation; some work requirements produced exits without employment response | Generalization across states and designs; food, debt, health, trust, and political outcomes |
| Material security after transition | Census SIPP 2024 reference-year person-month pairs | Following-month hardship differs across SNAP entry, exit, stable receipt, and stable nonreceipt; exit is not equivalent to recovery | Same person’s notice, route, amount, remedy, interpretation, and causal program effect |
| Mixed public/private route | Urban 2025 WBNS charitable-food analysis | 16.7% of working-age adults reported charitable-food participation in 2025; 39.5% of food-insecure adults reported participation, while 28.8% reported unmet need; hours, awareness, comfort, variety, transport, safety, and treatment constrain usable access | Provider capacity, exact food adequacy, same-episode SNAP/charitable timing, remedy, trust, and political response |
| Meaning and action | No sufficiently linked public-system layer yet | The specification identifies the needed fields | Fairness, trust, blame, complaint, appeal, turnout, vote, organizing, and agency response |

## What the combined evidence supports

### 1. Participation is not a route-quality score

The state APT/RPT layer shows large route-performance variation that does not order states like the participation rate. The unweighted correlation between FY2025 participation and APT is 0.033; the correlation with RPT is 0.211. These are descriptive ecological screens, not proof that administration has no effect. They establish a measurement boundary: population receipt and case-processing quality are different objects.

### 2. The route is experienced as multiple frictions, not only a delay

The WBNS evidence makes the administrative path concrete. Among the 182 adults who reported an interruption because they could not recertify on time, 40% lacked enough time after receiving a notice, 32% did not receive a notice, 22% found the paperwork too difficult, 16% could not participate in an interview, and 15% reported that an office lost paperwork. Multiple barriers could apply to one respondent. A legal deadline, an agency timeliness score, and a household’s usable time are therefore not interchangeable.

### 3. Route design can change receipt without changing underlying need

The NBER evidence provides stronger mechanism leverage than cross-sectional comparison. In the Los Angeles field experiment, flexible applicant-initiated interviews increased approvals by about 6 percentage points, doubled early approvals, and increased longer-term participation by more than 2 percentage points. Other administrative studies show office closure reducing tract participation by 7–9% over two years, and work requirements reducing SNAP participation without the intended employment response in the studied populations. These results support the proposition that route design can change observed receipt. They do not show that every interruption is agency-caused or that receipt alone equals security.

### 4. Receipt and material security remain separate stages

The SIPP person-month layer found following-month rent/mortgage hardship of 16.40% after no-to-yes SNAP transitions, 11.53% after yes-to-no transitions, 11.98% after yes-to-yes pairs, and 3.86% after no-to-no pairs. Utility hardship was 20.80%, 20.83%, 18.61%, and 5.86%, respectively. The transition groups differ in need and composition; these are not program effects. But the pattern is a direct counterexample to reading exit as recovery or continued receipt as complete security.

### 5. A private or charitable route can supplement help without closing the gap

The 2025 WBNS charitable-food analysis adds a distinct route after or alongside
public assistance. Among working-age adults, 16.7% reported household
charitable-food participation, above the 13.2% reported in 2019. Among adults in
food-insecure households, 39.5% reported receipt but 28.8% reported unmet need.
Among participants, 51.6% reported at least one listed access difficulty. Among
those with unmet need, the most common reported reasons were a site not being
open when available (45.5%), not knowing where to go (42.8%), and not feeling
comfortable getting help (39.9%).

This adds a material and meaning boundary: a household can use a resource and
still lack a usable, adequate, or acceptable route to food. The figures do not
measure pantry capacity, food quantity, SNAP benefit change, or later trust.
They also should not be collapsed into the USDA processing, WBNS SNAP-route, or
SIPP transition denominators.

## The end-to-end interpretation that survives the boundaries

The strongest supported statement is:

> A safety-net benefit is not a single transfer. It is a route through notices, deadlines, interviews, documents, offices, software, renewal decisions, and sometimes charitable substitutes. Route design can alter receipt and interruption; public or charitable receipt can coexist with continuing material hardship and unmet need. The social and political meaning of that experience cannot be inferred until the same episode’s effort, remedy, interpretation, and action are observed.

That statement is intentionally narrower than “administrative burden causes distrust” or “benefit loss causes a vote.” The current evidence does not identify those downstream arrows.

## Counterexamples and falsification tests

The synthesis should be revised if stronger evidence shows that:

- state timeliness differences disappear after comparable case mix and route channel are controlled;
- recipient-reported notice or paperwork barriers are unrelated to actual interruption once cases are linked;
- flexible interviews increase approvals only among cases that were ineligible, rather than changing access among eligible applicants;
- work-requirement exits are consistently followed by improved employment and material security;
- SNAP exits are generally followed by reduced hardship after amount, notice, appeal, and other supports are observed;
- charitable-food participation is generally adequate and unmet need is unrelated to hours, awareness, comfort, variety, transport, safety, and treatment once provider and household conditions are controlled;
- people experiencing the same route burden retain equal fairness, trust, complaint, and civic-action outcomes because remedies work equally well.

## The next acquisition gate

The next high-value design is a de-identified, linked or matched episode table across several states or channels with:

`notice date/channel → route attempts and effort → documents/interview → decision → expected and received amount → gap/interruption days → correction/appeal → food/housing/work outcome → fairness/trust → complaint/action → recovery or reentry`

Until that exists, the atlas should keep the material-to-institutional chain as a sequence of bounded findings rather than a closed causal story.

## Source layers

- [USDA/FNA state route-performance layer](usda-snap-state-route-performance-layer-v1.md)
- [Urban WBNS lived-route layer](urban-wbns-snap-recertification-interruption-layer-v1.md)
- [SNAP administrative-burden paper scan](snap-administrative-burden-paper-scan-v1.md)
- [SIPP transition × following hardship](sipp-snap-transition-outcome-fay-brr-layer-v1.md)
- [SIPP transition reason × following hardship](sipp-snap-transition-reason-outcome-fay-brr-layer-v1.md)
- [WBNS food-insecurity persistence layer](wbns-food-insecurity-persistence-layer-v1.md)
- [WBNS charitable-food access layer](wbns-charitable-food-access-layer-v1.md)
- [Same-episode ledger implementation](same-episode-event-ledger-implementation-v1.md)
