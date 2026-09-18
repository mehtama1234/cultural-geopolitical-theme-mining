# Finding 096: Large-load rules can reduce a modeled residential rider while leaving real incidence open

**Status:** provisional named U.S. infrastructure-governance finding · **Checked:** 2026-09-17

## The bounded finding

Virginia's State Corporation Commission moved Dominion Energy Virginia's
large-load governance toward explicit demand, contract, and cost-allocation
requirements. The retained regulatory record reports two large-load drop events
of 1,551 MW in July 2024 and 1,800 MW in February 2025. The 2025 GS-5 framework
sets a 25 MW contracted-demand threshold, minimum demand requirements, and a
14-year minimum contract term beginning January 1, 2027, subject to the stated
eligibility and tariff conditions.

In a separate 2026 Rider T1 proceeding, the SCC describes a projected typical
residential increase of $2.90 per month before an amended allocation method and
$0.94 after it—a 67.5% reduction in the projected increase. These are modeled
reference-customer effects, not observed bills or a data-center-only burden
estimate. Dominion's filing also reports 139 initial GS-5 accounts, 131 of them
classified as data centers; this is a filing snapshot, not a verified current
roster.

The safe interpretation is:

> Regulatory design can move electricity-system risk toward explicit large-load
> obligations and reduce a modeled residential rate effect without proving who
> ultimately pays, whether reliability improved, or whether public costs were
> fully recovered.

## Event chain

```text
large-load growth and operational stress
  -> utility commission review and reported load-drop events
  -> GS-5 threshold, demand, contract, and allocation rules
  -> modeled residential rider effect
  -> [open] actual bills, payments, reliability, local burden, and public response
```

## What the public record supplies

| Stage | Reported evidence | Still open |
|---|---|---|
| Operational stress | Dominion testimony summarized 1,551 MW and 1,800 MW large-load drops | Facility-level exposure, duration, independent reconstruction, and household/service consequences |
| Governance rule | 25 MW threshold, 85% transmission/distribution demand, 60% generation demand, and 14-year minimum contract term | Implementation, exemptions, enforcement, and customer compliance |
| Modeled allocation effect | Projected typical residential Rider T1 increase falls from $2.90 to $0.94 per month | Observed household bills, payments, counterfactual validity, and data-center-only attribution |
| Account composition | Initial filing lists 139 GS-5 accounts, including 131 data centers and eight non-data-center accounts | Current roster, consumption, ownership, location, contracts, and cost causation |

The event, policy, modeled-rate, and filing units are deliberately not pooled.

## Why it matters to the broader atlas

This case advances the infrastructure lane from announced demand to a visible
institutional response. It also supplies a counterexample to a simple
“data-center growth equals household burden” story: a cost-allocation change can
lower a modeled residential effect while leaving other rate pressures and
system costs unresolved. Conversely, a lower projected rider does not prove
that large-load customers bear all grid, reliability, water, land, or public-
service costs.

Keep these states separate:

```text
load-drop event       != household outage or bill
regulatory rule       != implemented payment
modeled rider effect  != observed ratepayer incidence
account roster        != electricity consumption or cost causation
cost allocation       != full public-cost recovery
public participation  != public legitimacy or consent
```

## Next decisive test

Build a matched utility/place ledger linking the large-load account or project
to contracted and actual demand, feeder/transmission investment, tariff and
payment records, residential and business bills, reliability events, water or
land burden, local services, public comments, and later amendments or provider
switching. Preserve ordinary residential customers, non-data-center GS-5
accounts, and places with similar load growth but different allocation rules.

## Sources and storage boundary

- [Structured Virginia large-load record](../../../records/us-virginia-data-center-large-load-governance-2024-2027.json)
- [Virginia SCC SB1239 report](https://www.scc.virginia.gov/media/sccvirginiagov-home/regulated-industries/utility-regulation/responsibilities/scc-report--sb1239.pdf)
- [Virginia SCC data-center initiatives fact sheet](https://www.scc.virginia.gov/media/sccvirginiagov-home/about-the-scc/fact-sheets/scc-data-center-initiatives-02-2026.pdf)
- [Virginia SCC facts and Rider T1 context](https://www.scc.virginia.gov/about-the-scc/scc-facts/)
- [Dominion GS-5 filing](https://www.scc.virginia.gov/docketsearch/DOCS/84sc01%21.PDF)

No customer-bill, feeder, facility-meter, water, or household microdata were
added.
