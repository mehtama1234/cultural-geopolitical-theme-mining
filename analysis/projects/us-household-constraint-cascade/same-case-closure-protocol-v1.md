# Same-case closure protocol for the household constraint cascade v1

**Checked:** 2026-09-16  
**Status:** research-design and promotion gate; no new data acquired

## Purpose

The project currently has strong descriptive layers, but they are not one
person- or household-level causal episode. This protocol defines the smallest
evidence package that may be promoted from a cross-source bridge to an
end-to-end case. It is designed to work with an already-authorized panel or a
consented/matched episode file while preserving the project's storage limit.

The governing test is:

```text
dated pressure
  -> practical room and feasible alternatives
  -> protected and sacrificed need
  -> work / care / childcare / food / health / housing / debt consequence
  -> institutional route and verified remedy
  -> one-, three-, and six-month persistence or recovery
  -> trust / legitimacy / action / switching / exit
```

No arrow is promoted merely because its endpoints appear in the same dataset.
The event must be dated, the unit must remain identifiable through the relevant
window, and the interpretation must distinguish observation from comparison,
inference, and causal estimation.

## Minimum episode record

One record must contain, or explicitly mark as unknown, all of the following:

| Gate | Required observation | Minimum acceptable evidence |
|---|---|---|
| Trigger | What happened and when | Bill, renewal, denial, shutoff warning, care need, coverage change, or comparable dated report with recall window |
| Obligation | What was owed or required | Amount band or rule, payer, due/decision date, and whether payment was required to preserve service or care |
| Room | What could realistically be done | Liquid-resource band plus schedule control, family/help access, credit/borrowing, and coverage or assistance alternatives |
| Choice | What was protected and sacrificed | Received, delayed, skipped, substituted, borrowed, reduced, or transferred outcome with stated reason |
| Consequence | What changed afterward | At least one directly dated work, unpaid-care, childcare, food, health, housing, or debt outcome |
| Route | What institution did | Contact/appeal/complaint, responsible authority, response date, disposition, and repeat effort |
| Remedy | Whether the problem was repaired | Correction, refund, payment plan, restored coverage/service, care continuation, denial upheld, partial remedy, or verified no remedy |
| Follow-up | Whether the household recovered | Same outcome measured at one, three, and six months, with persistence distinguished from successful repair |
| Meaning/action | What followed institutionally or politically | Prior and later trust/attribution plus action, non-use, switching, dependence, or exit; not inferred from satisfaction alone |
| Design | Why the estimate is interpretable | Weight, eligibility, attrition, missingness, uncertainty, source hash, and at least one credible counterexample |

An unknown value is valid only when its missingness, denominator, and reason are
recorded. It cannot be silently converted into “no,” “no remedy,” or “no
action.”

## Promotion gates

Promotion requires all gates below. If one fails, publish the result as a
bounded bridge and retain the failed gate as the next acquisition requirement.

1. **Identity and timing:** a stable pseudonymous unit links exposure, route,
   and follow-up; exposure precedes the measured consequence; recall windows are
   documented.
2. **Choice and alternatives:** the record shows what the household could have
   done, not only what it eventually did. A no-friction or higher-room
   comparison is retained.
3. **Institutional specificity:** the responsible institution and response are
   identifiable. A complaint receipt, automated message, or satisfaction score
   alone is not a remedy.
4. **Repair test:** remedy is measured separately from response, and recovery
   is measured separately from remedy. For example, a credit-record change is
   not presumed to restore care, food, housing, or health.
5. **Meaning/action ordering:** prior trust or identity is measured before the
   episode, and later trust/action is measured after the route or remedy. A
   cross-sectional political benchmark cannot close this gate.
6. **Design and falsification:** weights, uncertainty, attrition, subgroup
   sparsity, and at least one counterexample are reported. The analysis states
   which alternative explanations remain plausible.

## Analysis sequence

The first executable analysis should be descriptive and pre-registered in the
record before any causal claim:

- define the episode and eligible baseline window;
- estimate exposure-to-choice and choice-to-consequence transitions;
- stratify by practical room, schedule control, support, and institutional
  route;
- estimate remedy receipt and verified repair separately;
- compare one-, three-, and six-month persistence/recovery;
- report later meaning/action only for units with valid prior and post measures;
- run negative-control, alternative-window, and no-friction comparisons; and
- preserve weighted denominators, replicate variance or an appropriate
  design-based alternative, and missingness at every arrow.

The causal layer may be added only where assignment, timing, or a credible
quasi-experimental contrast supports it. Otherwise the output remains a
weighted longitudinal description with explicit selection limits.

## Storage-conscious execution plan

Before acquiring data, retain only documentation needed to verify field names,
wave dates, eligibility, weights, keys, and file sizes. Then acquire the
minimum overlap files, inventory them, and stop before analysis if any required
gate fails. Extract only required columns into a compact keyed file outside the
repository; commit the extraction script, schema, hashes, aggregate records,
and writeup. Do not commit raw microdata or an unreviewed bulk archive.

## Current result against this protocol

The MEPS and SIPP layers satisfy useful portions of the trigger, context,
choice-adjacent, and consequence surfaces, but fail the same-case obligation,
alternatives, verified remedy, recovery, and prior/post meaning gates. The
CES/ANES action and trust material remains a cross-source benchmark; the
2026-09-16 cache audit found no local raw files for rerunning it. The project
therefore remains correctly classified as **not closed**, and the next
legitimate promotion is an approved compatible panel or consented/matched
episode—not another disconnected endpoint benchmark.
