# MEPS acute-event context differs by coverage group

**Checked:** 2026-09-15  
**Status:** weighted descriptive subgroup comparison; no causal claim  
**Machine record:** [MEPS event context by coverage](data/us-meps-2024-event-context-by-coverage.json)

## Result

The association between observed care-event presence and reported context is
not uniform across under-65 insurance groups. Acute-event groups generally
show higher medical-bill-problem and fair/poor-health shares within private,
public-only, and uninsured coverage categories, but the size and precision of
the pattern differ. Office-event groups show a smaller health gradient and, in
the private-insurance group, nearly identical bill-problem shares.

| Under-65 group | Event | Bill problem: present vs absent | Fair/poor health: present vs absent |
|---|---|---:|---:|
| Private | ER | 14.43% vs 6.39% | 16.49% vs 5.60% |
| Private | Inpatient | 11.60% vs 7.06% | 23.45% vs 6.08% |
| Private | Office | 7.29% vs 7.03% | 7.72% vs 3.58% |
| Public only | ER | 15.07% vs 9.51% | 35.35% vs 11.74% |
| Public only | Inpatient | 12.01% vs 10.47% | 44.82% vs 13.87% |
| Public only | Office | 11.76% vs 8.31% | 19.57% vs 9.82% |
| Uninsured | ER | 22.14% vs 9.25% | 19.59% vs 8.78% |
| Uninsured | Office | 13.79% vs 8.64% | 16.98% vs 6.26% |

The uninsured inpatient cell has only 16 valid records and is intentionally
omitted from the promoted comparison. All estimates are person-weighted
shares with standard-BRR uncertainty; the machine record retains the standard
errors and valid counts.

## Interpretation

Coverage conditioning improves the counterexample test. It shows that the
acute-event association is not simply an unconditioned private-versus-public
contrast. Yet it does not turn coverage into an explanation. Event groups may
differ in illness, age, severity, provider mix, income, employment, and access
to care. A person without an observed event is not necessarily healthy or
free of unmet need.

The office/private result is especially important: an observed office visit
does not coincide with a higher annual bill-problem share in that subgroup,
even though fair/poor health is more common. This separates utilization,
health status, and reported payment difficulty rather than treating them as a
single burden index.

## End-to-end boundary

This pass now supports a layered sequence:

```text
coverage group + observed event presence
  -> different same-year health and bill-problem context
  -> candidate exposure pattern for deeper episode analysis
```

It still does not observe the event’s bill date, care alternative, delay or
foregoing, borrowing, savings draw, unpaid care, work-time sacrifice,
recovery, remedy, trust, switching, or political action. The next decisive
test remains a valid round-level or linked-source follow-up design, not another
cross-sectional subgroup split.
