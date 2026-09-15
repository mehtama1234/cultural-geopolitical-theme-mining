# MEPS 2024 event payment and annual bill-problem context v1

**Checked:** 2026-09-15  
**Unit:** 2024 MEPS event record linked to HC-256 person context  
**Method:** event-file `PERWT24F` with `VARSTR`/`VARPSU` Taylor linearization and event payment fields; no causal estimate

## Question

Does the amount paid on an observed office, emergency-room, inpatient, or
prescription event move monotonically with the person's report of a medical
bill problem?

This is a deliberately bounded test. It joins a payment-bearing event to an
annual person-level context field, but it cannot identify whether that event
created the bill problem, whether the problem came from another event, or
whether a person skipped care and therefore never appears in the event file.

## Results

| 2024 event type | Annual bill problem reported: self/family payment | No annual bill problem reported: self/family payment | Total events with bill-problem context |
|---|---:|---:|---:|
| Office visit | $48.95 (SE $6.09) | $58.31 (SE $3.33) | 143,797 |
| Emergency-room visit | $118.22 (SE $41.63) | $109.85 (SE $10.61) | 4,214 |
| Inpatient stay | $1,333.28 (SE $657.08) | $612.22 (SE $87.49) | 1,845 |
| Prescription purchase | $13.31 (SE $1.51) | $17.45 (SE $1.27) | 202,325 |

The same comparison for total event payment is also non-monotonic: office
visits average $316.59 versus $307.47, ER visits $1,187.11 versus $1,451.43,
inpatient stays $16,013.86 versus $19,378.97, and prescription purchases
$209.00 versus $236.98 for bill-problem versus no-problem context,
respectively.

The bounded finding is not that bill problems reduce payment. It is that an
annual bill-problem report cannot be read as a simple function of the payment
on the observed event. Direct payment, total allowed/payment, coverage,
deductibles, prior balances, unpaid amounts, household resources, and forgone
care are distinct surfaces.

## Coverage-conditioned check

The same event records were split by the under-65 `INSURC24` categories to
test whether the national comparison was merely a coverage mix. The table
shows self/family payment per event; each cell is an event-weighted mean with
the valid event count in parentheses.

| Event | Private: bill problem / no problem | Public-only: bill problem / no problem | Uninsured: bill problem / no problem |
|---|---:|---:|---:|
| Office visit | $59.17 (5,798) / $77.40 (56,825) | $31.79 (3,828) / $11.13 (19,103) | $217.37 (262) / $98.24 (1,163) |
| Emergency room | $156.85 (214) / $229.41 (1,044) | $11.17 (204) / $15.22 (962) | $907.95 (22) / $234.43 (73) |
| Inpatient stay | $2,270.58 (79) / $1,081.93 (352) | $218.35 (58) / $65.15 (354) | $0.00 (2) / $198.66 (18) |
| Prescription purchase | $18.13 (8,136) / $22.33 (53,843) | $4.73 (7,688) / $3.96 (32,480) | $24.58 (535) / $62.78 (1,961) |

Coverage changes the pattern rather than removing the ambiguity. The private
and public-only inpatient cells are directionally consistent with greater
observed direct payment among bill-problem reporters, but the private
inpatient uncertainty is large. The uninsured ER and inpatient cells are too
small and variable to promote as headline comparisons. These results still
cannot tell whether coverage caused the bill problem, whether the bill came
from the displayed event, or who never entered the observed-event universe.

## Resource-conditioned check

The same surface was also split by the five MEPS poverty categories. This
changes the question from “does payment differ by bill status?” to “does that
comparison hold at different levels of annual household resources?” Selected
self/family payment means (bill-problem / no-problem) are:

| Resource category | Office visit | Prescription purchase | Inpatient stay |
|---|---:|---:|---:|
| Poor/negative | $38.91 / $22.08 | $5.67 / $7.35 | $124.00 / $117.16 |
| Near poor | $17.70 / $29.57 | $6.43 / $9.83 | $0.00 / $76.16 |
| Low income | $58.83 / $38.29 | $11.58 / $12.25 | $4,809.25 / $281.66 |
| Middle income | $46.16 / $45.50 | $14.27 / $20.85 | $688.18 / $856.11 |
| High income | $55.67 / $74.25 | $23.43 / $20.40 | $367.61 / $889.03 |

The resource split is not a monotonic affordability law. Office and
prescription differences change sign across categories, and the low-income
inpatient bill-problem cell is highly variable (51 valid events; Taylor SE
$3,560.64). Poverty category is an annual resource context, not liquid cash at
the event, deductible exposure, or a measure of the amount owed. The table is
therefore a conditioning diagnostic and not a claim that poorer people pay
less or that higher event payments create bill problems.

```text
observed care event + payment
  -> annual bill-problem context
  -> possible household burden
```

The second arrow remains open because the event and the annual context do not
share a bill identifier or causal time window.

## What this adds to the end-to-end program

1. **Payment is not burden.** A lower observed self/family payment can coexist
   with a reported bill problem, while a higher payment can occur without one.
2. **Event selection matters.** These are people with observed events or
   purchases; non-users, delayed care, and forgone prescriptions are absent
   from the event denominator.
3. **Coverage and timing are necessary middle stages.** A stronger chain needs
   the bill, benefit design, balance, payment timing, household resources, and
   later choice or recovery.
4. **The counterexample prevents a false bridge.** Annual bill-problem status
   cannot be used to label every observed event unaffordable or every lower
   payment protective.

## Boundaries

HC-254G, HC-254E, HC-254D, and HC-254A have event-specific populations and
payment definitions. The annual `PROBPY42` field is person-level context, not an
event-level bill key. Payment fields are MEPS edited/imputed expenditure
measures; they do not reveal debt, unpaid balance, payment timing, borrowing,
savings draw, skipped care, or household tradeoffs. Standard errors use the
event-file `VARSTR`/`VARPSU` Taylor design. A few small coverage cells have
limited event counts and unstable estimates; they are not promoted as headline
results. The analysis remains descriptive and subject to event selection,
health need, coverage, and item-specific missingness.

## Reproduction

```text
python3 scripts/analyze_meps_event_payment_bill_context.py \
  --hc256 /path/to/h256.dta \
  --office /path/to/h254g.dta \
  --emergency-room /path/to/h254e.dta \
  --inpatient /path/to/h254d.dta \
  --prescription /path/to/h254a.dta \
  --output /tmp/us-meps-2024-event-payment-bill-context.json
```

The full machine-readable output is preserved in [the project data file](data/us-meps-2024-event-payment-bill-context.json). The official sources are the [AHRQ MEPS HC-256 file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes) and the 2024 [office](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254G&prfricon=yes), [prescription](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254A&prfricon=yes), [ER](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254E&prfricon=yes), and [inpatient](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254D&prfricon=yes) event files.

Related: [MEPS event-context association](meps-2024-event-context-association-v1.md), [bounded episode surface](meps-2024-bounded-episode-surface-v1.md), and [full-year acquisition gate](meps-2024-full-year-acquisition-gate-v1.md).
