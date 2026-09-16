# Platform-remedy implementation-depth audit v1

**Status:** source-coded implementation-stage audit; no remedy rate or welfare
estimate  
**Checked:** 2026-09-16  
**Source:** 27 records in the committed platform-remedy case ledger  
**Machine-readable audit:** [implementation-depth audit](data/platform-remedy-implementation-depth-audit-v1.json)

## Question

How far do the existing platform-remedy records travel beyond a decision and
into actual access, work, payment, and durable protection?

## Result

The ledger contains several kinds of remedy evidence, but they are not
interchangeable:

| Stage | Count | Interpretation |
|---|---:|---|
| Formal reactivation/restoration order | 7 | An adjudicated order is observed |
| Access resumed without merits remedy | 1 | Access resumption is reported, but not as a final merits remedy |
| Continued work after restoration | 1 | One primary record reports more than 150 later trips |
| Payment or lost-earnings stage observed | 6 | A rule, entitlement, order, or wage consequence is recorded |
| Verified payment receipt | 0 | Not observed in the ledger |
| Durable access or non-retaliation | 0 | Not observed in the ledger |

The counts overlap. A case may have both a reactivation order and a payment
order. They are stage counts, not percentages of workers or independent
outcomes. The continued-work record is the Hotak case; it does not establish
net income, payment receipt, later access, or protection from retaliation.

## Remedy chain

```text
deactivation
  -> explanation/review
  -> legal or institutional challenge
  -> restoration order or voluntary access resumption
  -> actual work or service access
  -> payment receipt and income recovery
  -> durable access, corrected record, and non-retaliation
```

The local evidence reaches the middle of this chain, unevenly. It is strongest
for formal decisions and orders, weaker for operational access, and absent for
verified payment receipt and durable protection. The appropriate broad-program
finding is therefore not that remedies fail; it is that public remedy records
expose institutional action more readily than lived recovery.

## Why this matters for the broad goal

This audit supplies a reusable coding rule across consumer, worker, and public
systems:

```text
order != implementation
implementation != receipt
receipt != durable recovery
continued use != unconstrained choice
```

It also preserves the counterexample: Hotak shows that a worker can regain
access and perform substantial subsequent work while lost remuneration and
durable protection remain open. Formal remedy and practical recovery can move
on different clocks.

## Smallest decisive next test

For one already identified case, obtain a dated worker-side or platform-side
record of actual restoration, payment receipt, later access, and recurrence.
For the broader case set, retain source type and case selection while adding
post-order implementation documents; do not convert order counts into
recovery rates.

## Reproduction

```text
python3 scripts/audit_platform_remedy_implementation_depth.py
```

The script reads the committed ledger only and downloads nothing.

