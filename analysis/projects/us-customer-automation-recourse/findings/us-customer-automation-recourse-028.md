# Finding 028: A public CFPB narrative filter did not close the consumer-power gap

**Status:** provisional API-boundary finding · **Checked:** 2026-09-18

The CFPB public complaint API was tested with and without
`has_narrative=true` on the same credit-card, monetary-relief, date-bounded
query. Both returned 21,425 matching records and the same 25 capped records.
The live response exposed administrative routing and response fields, but no
complaint narrative text or usable narrative-presence field.

The safe conclusion is not that consumers lacked narratives. It is that this
public response shape cannot currently supply narrative meaning, an
alternative/non-use decision, or a linked customer outcome. The existing
`Closed with monetary relief` label therefore remains an administrative
response category, not verified relief receipt or practical exit.

This advances the program by ruling out one tempting but weak acquisition
shortcut and preserving the missingness boundary. The next decisive route is a
lawful consented or account-level follow-up that joins problem, attempted
alternatives, institutional response, remedy, repeat effort, and later
switching or exit at the same episode level.

See the [full API probe](../cfpb-narrative-filter-probe-2026-09-18.md) and its
[machine record](../data/cfpb-narrative-filter-probe-2026-09-18.json).

Source: [CFPB Consumer Complaint Database public API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/).
