# NBER W35677 paper-method audit

**Checked:** 2026-09-14  
**Status:** official paper method inspected; exact release/identifier crosswalk remains open

## What the paper establishes

The official W35677 paper supplies the missing conceptual documentation behind
the public task sheets. It says that the Real-Time Population Survey elicits
occupation using the **2018 Standard Occupational Classification (SOC)**,
then uses O*NET work-activity information to show workers the ten most
important Detailed Work Activities associated with that occupation. Workers
report which of those activities they perform and which they use generative AI
to assist.

The paper's measurement appendix also documents the aggregation path:

```text
O*NET task statements and importance scores
  -> O*NET Detailed Work Activities (DWA)
  -> Intermediate Work Activities (IWA)
  -> Work Activities (WA)
  -> Broad Work Activities (BWA)
```

It reports 2,040 DWAs, 332 IWAs, 37 WAs, and 9 BWAs. It explains that DWA
importance is constructed from task importance scores through O*NET
crosswalks, then the ten highest-importance activities are presented for the
respondent's occupation. This establishes that the NBER indexes are O*NET-
derived work-activity measures, not an unrelated activity vocabulary.

## What the paper does not establish

The paper does not, in the inspected method sections, state the exact O*NET
database release used for the public W35677 sheets, nor does it publish a
mapping from each NBER `I##`/`D##` identifier to the current O*NET identifier.
It references 2018 SOC consistency and O*NET crosswalk procedures, but that is
not enough to promote the current 30.3/31.0 label bridge to exact historical
identifier equivalence.

The paper also makes the unit boundary explicit: the public task rates are
worker-reported use among workers who perform the activity. They do not
observe employer implementation, permission, monitoring, productivity, pay,
discretion, bargaining, or household outcomes.

## Reconciliation consequence

The release comparison and paper audit together support this interpretation:

- **Conceptual relationship:** established—NBER task prompts are derived from
  O*NET work activities and use the O*NET activity hierarchy.
- **Current label bridge:** strong—1,653/1,655 DWA labels and 322/322 IWA
  labels match uniquely after normalization.
- **Exact identifier bridge:** unresolved—the structural probe agrees with
  only 1,393/1,653 unique DWA label matches and 269/322 IWA matches.
- **Release explanation tested:** not supported by the first check—O*NET 30.3
  and 31.0 mapping files acquired here are byte-identical.

Therefore the crosswalk is usable for a transparent, label-based measurement
bridge, but every downstream estimate must retain the match class and avoid
describing the NBER and O*NET IDs as interchangeable.

## Source and reproduction

- [NBER W35677 paper](https://www.nber.org/papers/w35677)
- [NBER public task-index data page](https://sites.google.com/view/covid-rps/data)
- [Paper PDF used for this audit](https://www.nber.org/system/files/working_papers/w35677/w35677.pdf)
- Paper PDF SHA-256 at this check: `d292b955d0f3cffaba0122b82b5286adf0dd66fe54bfa1da15e6ed7d93b9b714`
- [Identifier reconciliation audit](data/onet-nber-crosswalk-2026-09-14/onet-nber-identifier-reconciliation-audit-2026-09-14.json)

**Evidence status:** official paper method and public index files inspected;
conceptual O*NET derivation is supported, while exact vintage and identifier
equivalence remain open.
