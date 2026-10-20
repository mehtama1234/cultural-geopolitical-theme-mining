# EBT prevention versus restoration: New Jersey and Connecticut bridge

**Checked:** 2026-10-20  
**Status:** cross-state mechanism bridge; no pooled outcome or causal claim

## Bounded comparison

The current New Jersey and Connecticut records expose two different ways a
public-benefit system can move from theft exposure toward prevention without
showing restored household security:

| Stage | New Jersey | Connecticut | What remains unobserved |
|---|---|---|---|
| Prevention control | Statewide chip/tap-card distribution after a three-county pilot; pilot transaction counts are published | Cardholder lock/unlock and out-of-state transaction blocking through MyDSS or ConnectEBT | Unique activation, control uptake, prevented theft, and access by subgroup |
| Card access | Replacement requests receive chip cards; benefits transfer on activation | Physical card can be replaced; remaining old-card balance transfers | Delivery, activation timing, interruptions, and usable access |
| Loss restoration | State guidance says electronically stolen benefits after December 21, 2024 are not replaceable | State guidance says stolen SNAP or cash benefits are not replaceable | Recovered balance, food-gap duration, adequacy, and appeal result |
| Later outcome | No public household-level follow-up | No public household-level follow-up | Food security, substitution, debt, trust, recurrence, and exit |

The comparison is not a state ranking. New Jersey's infrastructure-scale
rollout and Connecticut's user-controlled lock tools are different prevention
designs, and the public records do not provide a common denominator or a
comparable theft rate. The shared finding is narrower: a prevention mechanism
and a physical-card route can be visible while the conversion from control to
uninterrupted food access, and from loss to recovery, remains unmeasured.

## End-to-end boundary

```text
electronic theft exposure
  -> state prevention or card-control response
  -> physical-card replacement / balance-transfer rule
  -> [open] household activation and usable food access
  -> [open] stolen-benefit restoration or residual food gap
  -> [open] adequacy, trust, recurrence, action, and exit
```

This bridge joins named stages across two state systems for comparison only. It
does not treat either state policy as a causal intervention estimate, combine
their populations, or infer that transaction counts, card issuance, or a lock
feature prevented loss.

## Next decisive evidence

The strongest next input would be a state aggregate or authorized case file
with a common clock: card/control enrollment or activation, theft report,
replacement or denial, time without usable food benefits, and later food
security or household outcome. Without that input, retain the two routes as
bounded prevention-versus-restoration comparators.

## Source records

- [New Jersey EBT chip-card prevention follow-up](nj-ebt-chip-card-fraud-prevention-followup-2026-10-20.md)
- [Connecticut EBT lock-control and nonreplacement follow-up](ct-ebt-lock-controls-nonreplacement-followup-2026-10-20.md)
- [New Jersey structured record](../../records/us-nj-ebt-chip-card-fraud-prevention-2026.json)
- [Connecticut structured record](../../records/us-ct-ebt-lock-controls-nonreplacement-2026.json)

**Evidence boundary:** both states supply official prevention and card-access
machinery. Neither public route supplies individual control use, prevented
theft, restored stolen benefits, food adequacy, trust, or durable exit.
