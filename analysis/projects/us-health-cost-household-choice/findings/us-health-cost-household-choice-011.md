# Institutional-friction reporters show mixed round-to-round health and work paths

**Status:** provisional MEPS 2024 longitudinal descriptive comparison  
**Checked:** 2026-09-16

## Bounded finding

The MEPS 2024 HC-256 person file permits a round-to-round screen of reported
insurance denial or prior-authorization delay (`EQDENY53`) against the change
from round 4/2 to round 5/3. Among records with valid perceived-health ratings,
denial/delay reporters show a higher share with worsened perceived health than
people reporting no denial/delay, while improvement occurs in both groups.

| Round-5/3 denial or delay report | Health improved | Health worsened | Health unchanged |
|---|---:|---:|---:|
| Yes | 19.04% (SE 1.14; n=1,574) | 25.11% (SE 1.12; n=1,574) | 55.85% (SE 1.19; n=1,574) |
| No | 20.29% (SE 0.56; n=8,591) | 21.74% (SE 0.57; n=8,591) | 57.97% (SE 0.54; n=8,591) |

Employment transitions are comparatively close: employment was retained for
56.09% of denial/delay reporters and 57.28% of non-reporters; movement from
employed to not employed was 2.61% versus 2.89%, and movement from not
employed to employed was 2.60% versus 2.56%.

These are weighted shares using the person weight. Counts are unweighted and
the health and employment valid universes differ slightly.

The worsening contrast remains visible after separating people by their
round-4/2 health status, although the direction of change is strongly shaped
by baseline status:

| Round-4/2 baseline health | Denial/delay: worsened | No denial/delay: worsened |
|---|---:|---:|
| Good, very good, or excellent | 29.42% (SE 1.43; n=1,156) | 23.57% (SE 0.67; n=7,454) |
| Fair or poor | 11.26% (SE 1.55; n=418) | 6.99% (SE 0.74; n=1,137) |

The lower worsening share among people starting in fair/poor health is a
reminder that regression toward the mean and selective survival/response can
matter; it is not evidence that friction is protective.

## What this adds to the end-to-end chain

```text
reported institutional friction at the final round
  + prior-round health/work context
  -> round-to-round perceived-health direction and employment transition
  -> treatment continuity, payment response, recovery, remedy, trust, or exit
```

The first arrow is a longitudinal descriptive association. It is useful
because it places the institutional-friction report alongside a prior/final
round comparison rather than only a same-round debt or bill-problem cross-tab.
It does not show that the denial or delay caused worsening health, protected or
disrupted employment, or changed household legitimacy judgments.

## Interpretation boundary

`EQDENY53` is a round-level report. It has no claim identifier, decision date,
appeal, insurer response, correction, resolution, or exact treatment episode.
The round-4/2 values are a prior reference endpoint, but the data do not prove
that they predate the denial itself. Underlying illness, severity, medication
need, coverage, access, age, and employment selection can generate both the
reported friction and the later-looking outcome. Perceived health is ordinal,
not a clinical recovery measure, and employment status does not identify
work-time loss or a care-related job decision.

| Arrow | Status | Safe conclusion |
|---|---|---|
| Denial/delay report → round-to-round perceived-health direction | Longitudinal descriptive association | Worsening is more common among reporters in this selected universe; improvement remains common in both groups |
| Denial/delay → employment transition | Longitudinal descriptive association | Retention and transitions are similar in this screen; no work effect is established |
| Denial/delay → treatment continuity, payment, or household substitution | Open | No claim-level remedy, adherence, bill timing, borrowing, or unpaid-care response is observed |
| Institutional route → recovery, trust, action, or exit | Open | Requires a dated case ledger or compatible same-person follow-up with those outcomes |

## Reproduction

The [machine-readable record](../data/us-meps-2024-institutional-friction-followup.json)
preserves the valid denominators, estimates, BRR intervals, and boundary. The
[reproduction script](../../../../scripts/analyze_meps_institutional_friction_followup.py)
reads HC-256 and HC-036BRR, links persons by `DUPERSID + PANEL`, and uses the
128 standard BRR flags with replicate weight `BRR flag × 2 × PERWT24F`.

## Next decisive test

Acquire or construct a dated denial/appeal/remedy record that can be joined to
the intended care or medication episode, payment obligation, treatment
completion, work/time substitution, and later recovery or institutional
judgment. Until then, retain this as a round-to-round friction screen rather than
a causal estimate or a remedy-failure claim.

## Official sources

- [AHRQ MEPS HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes)
- [AHRQ MEPS HC-036BRR variance file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-036BRR&prfricon=yes)
- [Institutional friction across MEPS event channels](us-health-cost-household-choice-006.md)
