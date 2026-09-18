# Finding 002: The atlas has route visibility, but no retained episode yet qualifies as practical exit

**Status:** provisional storage-light event-compatibility finding · **Checked:** 2026-09-17

## The bounded finding

The current U.S.-centered atlas contains many measured pressures, institutional
routes, administrative decisions, and some access-restoration or recovery
signals. A systematic screen of nine retained routes finds **zero** that meet
the program's stronger practical-optionality standard: the same unit must have
a dated trigger, an observed alternative or non-use choice, an institutional
response, a verified protected or sacrificed outcome, and a later behavior or
meaning/action endpoint.

This is a result about observability, not about the absence of remedies or
exits in the world. The current records stop at different points in the chain:

```text
condition or restriction
  -> route, complaint, transition, or market response [often observed]
  -> alternative and effort [usually missing]
  -> verified remedy, recovery, or protected outcome [missing or weak]
  -> continued use, switching, non-use, move, trust, or action [rare/missing]
```

## Qualification screen

| Route | Unit and denominator | What is observed | Critical missing fields | Qualifies? |
|---|---|---|---|---|
| SNAP adjacent-month transition | Person-program spell; 437 entries, 387 exits, 188 classified exits | Program-state transition and following material context | Notice, alternatives, appeal/effort, verified remedy, later security, meaning | No |
| Platform remedy ledger | Case; 27 source-ledger episodes | Attempted route, decision, and 8 source-coded access-restored statuses | Alternative work, receipt, durability, protected outcome, later switch/exit reason | No |
| CFPB student-loan ledger | De-identified complaint case; 25 capped records | Receipt, routing, timing, and company response labels | Account exposure, alternatives, correction/receipt, repeat effort, closure/switch, follow-up | No |
| SHED fraud/recovery | Adult respondent and incident; conditional survey estimates | Fraud exposure, recovery, and time/financial burden reports | Named account, verified remedy, replacement route, continued use/switching | No |
| Housing/insurance market | Policy/property/place records | Nonrenewal and residual-market/backstop movement | Household notice, replacement, claim/repair, payment, move/stay | No |
| Local service capacity | Resident/place/firm records | Presence, entry/exit, shortage, travel context, and public routes | Dated resident attempt, usable substitute, completed use, restoration, later action | No |
| Doxo bill-payment enforcement | Named institutional case; 2 observations | Search-route confusion, alleged fees, subscription friction, and order-stage controls | Payment success, bill status, service continuity, remedy receipt, trust, switching/exit | No |
| Grubhub multisided redress | Named platform program; 640,038 reported recipients | Aggregate checks/PayPal distribution and prospective worker, account, and restaurant controls | Group-specific exposure, individual receipt, restored income/access, alternatives, trust, switching/exit | No |
| VRURC product-recall implementation | Single recall key; notice and later CPSC progress snapshot | Dated hazard, stop-use/replacement instruction, and reported correction counts | Purchaser exposure, notice/replacement receipt, safe restoration, residual cost, trust, switching/exit | No |

The machine-readable [qualification register](../data/end-to-end-event-qualification-register-2026-09-17.json)
preserves the route-level units, denominators, missing fields, and next
minimum field for the nine-route screen. The latest synchronization includes
Doxo, Grubhub, and the VRURC recall implementation bridge. The [practical-exit observability audit](../practical-exit-observability-audit-v1.md)
is the broader cross-domain inventory; this finding applies its promotion rule
to a smaller, explicit candidate set.

## What this establishes for the broad goal

The broad trend question is not only whether people face pressure or whether
an institution responds. It is whether practical alternatives change the
meaning of the response. A complaint marked closed, a platform account marked
restored, a benefit state that changes, or a market that expands a backstop can
all be important institutional events. None alone shows that a person regained
security, could choose a substitute, or left without an unacceptable cost.

The comparison identifies a recurring structural split. The three latest
consumer-remedy cases sharpen it: even when an enforcement or recall record names an
operator and a formal control or payment distribution, it may still omit the
affected unit's usable alternative and lived outcome.

- **Visibility:** the problem enters a public, administrative, survey, or market
  record.
- **Control:** a responsible actor or agency makes a decision.
- **Optionality:** the affected unit can use a workable alternative or refuse
  the route.
- **Protection:** money, time, access, health, work, housing, or safety is
  actually preserved or restored.
- **Meaning/action:** the unit later trusts, blames, complains, organizes,
  switches, stops using, moves, votes, or otherwise acts.

The first two layers are common in the retained evidence. The final three are
not jointly observed. That gap is central to the atlas because it prevents
several tempting but invalid conversions: complaint volume into harm,
response labels into remedy, restoration into autonomy, program exit into
recovery, and market movement into household mobility.

## Counterexamples and limits

- A platform case can show access resumed while payment, durability, and
  alternative work remain unknown.
- A complaint can receive a company explanation or non-monetary relief without
  showing correction, account continuity, or customer recovery.
- A SIPP program exit can be followed by lower resources; that is a warning
  against coding institutional exit as improved security, not a causal estimate
  of harm.
- Self-reported fraud recovery and time burden are valuable respondent
  evidence, but they do not identify a provider-level remedy or later switching.
- Insurance backstop growth and establishment counts describe the option
  environment, not a particular household's usable choice.
- The nine routes use different units, clocks, denominators, and selection
  mechanisms. They cannot be pooled into a practical-exit rate.

## Next qualifying design

The smallest storage-conscious acquisition is one small, lawful event ledger
with stable linkage or a valid repeated-person frame:

```text
dated trigger or notice
  -> actual alternatives and their money/time/access cost
  -> attempted route, effort, decision, and responsible actor
  -> remedy offer versus verified receipt and durability
  -> protected/sacrificed outcome
  -> continued use, switching, non-use, move, trust, complaint, organizing, or vote
```

The first candidate routes remain a public-benefit interruption/appeal case, a
platform remedy case with post-order follow-up, a credit/deposit account event,
or a property/insurance notice. Before any acquisition, verify lawful access,
file size, identifiers, timing, weights, and whether the missing fields truly
exist. Do not download a large respondent archive merely to obtain another
exposure count.

## Coding rule

```text
route visibility       != practical optionality
response label         != verified remedy
access restoration     != autonomy
institutional exit    != recovery
market movement        != household mobility
non-reporting          != satisfaction
```

Code this as **a verified cross-domain observability boundary: the atlas has
route and response evidence, but no retained same-unit episode yet closes
alternative → remedy/recovery → later meaning/action or exit**.

## Sources and storage boundary

- [Practical-exit observability audit](../practical-exit-observability-audit-v1.md)
- [CFPB practical-exit contract dry-run](../cfpb-practical-exit-contract-dry-run-v1.md)
- [Platform-remedy field-availability audit](../platform-remedy-field-availability-audit-v1.md)
- [Broad program next-pass queue](../../../US-BROAD-NEXT-PASS-QUEUE_V1.md)
- [Doxo bill-payment record](../../../records/us-ftc-doxo-bill-payment-hidden-fees-2026.json)
- [Grubhub remedy record](../../../records/us-ftc-grubhub-multisided-remedy-2026.json)
- [VRURC recall implementation record](../../../records/us-cpsc-vrurc-recall-implementation-2023-2026.json)

This finding reads retained local records and audits only. It adds no bulk
download and makes no population-level exit or remedy estimate.
