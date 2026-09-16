# Medical debt becomes a visible CFPB complaint category

## The finding

The 2025 CFPB aggregate snapshot contains 8,861 published records in the
nested `Debt collection → Medical debt` subproduct. That is 3.122% of the
283,828 Debt collection records and 0.163% of all 5,452,107 published records
in the snapshot.

This is a measure of institutional visibility: a medical-debt problem has been
categorized within a public complaint system. It is not a medical-debt
prevalence estimate, a complaint rate among people with medical debt, or a
remedy rate.

## What this adds

```text
medical-cost burden
  -> collection/credit institution
  -> public medical-debt complaint category
  -> response, correction, recovery, trust, or exit (not observed here)
```

The medical-specific category gives the health-cost chain a concrete
institutional surface between household debt and the later remedy question.
It complements MEPS person-level medical debt and collection-contact fields,
but the datasets have no compatible person identifier and are not joined.

## Boundary

The CFPB snapshot is a published administrative aggregate. Selection into the
complaint route, product and subproduct coding, publication rules, company
response processes, duplicate screening, and ability to complain all shape the
count. The snapshot does not identify a dated bill, care decision, amount owed,
appeal, verified correction, money recovered, restored care, repeat contact,
switching, trust, or exit.

The next decisive test is a record-level medical complaint extract with a
documented product/subproduct/issue filter and stable case keys, followed by a
lawful same-case or panel design that can observe remedy and later household
outcomes. Until then, this is a visibility layer rather than a completed
health-cost-to-remedy arrow.

## Reproduction

See the [method note](../cfpb-2025-medical-debt-visibility-v1.md),
[machine output](../data/us-cfpb-2025-medical-debt-visibility.json), and the
[canonical trend record](../../../records/us-cfpb-2025-medical-debt-visibility.json).
