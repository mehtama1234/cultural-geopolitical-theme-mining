# Finding 001: Network feasibility may require removing a node, not relaxing one link

**Status:** bounded theoretical infrastructure-design finding · **Checked:** 2026-09-23

## The bounded finding

An NBER working paper models spectrum-repacking constraints as a graph:
stations are vertices and pairwise interference restrictions are edges. It shows
that buying out any one station can reduce the number of channels needed in the
model, even though relaxing any single interference restriction cannot. The
construction establishes that for every `k ≥ 4`, some `k`-vertex-critical graph
has no critical edge.

```text
network feasibility problem
  -> node and link complementarities
  -> buyout, waiver, redesign, or sharing choice
  -> channel capacity and market structure
  -> [open] actual service, prices, concentration, and public value
```

## What this adds to the atlas

This is a reusable infrastructure-governance concept: a remedy can fail when
audited one constraint at a time because the binding problem is the network's
complementarity structure. The choice to remove a node is not automatically a
public benefit; it can trade technical feasibility against ownership,
coverage, employment, local media, competition, and access.

## Limits and next test

- The result is theoretical and does not estimate an actual spectrum auction or
  regulatory decision.
- It does not identify which station should be bought out or who bears the
  resulting service and ownership costs.
- Real spectrum systems include engineering, geography, law, technology,
  public-interest, and market constraints not represented by one graph.

The next decisive test is a named spectrum-repacking proceeding joining the
interference graph, proposed waiver or buyout, auction/compensation terms,
station coverage, ownership, employment, consumer access, prices, and later
service or market outcomes.

## Source

- [NBER Working Paper 35757](https://www.nber.org/papers/w35757)
- [Machine-readable trend record](../../../records/comparative-nber-spectrum-repacking-network-feasibility-2026.json)

**Evidence status:** the network-remedy mechanism is theoretically established;
its regulatory and public consequences remain open.
