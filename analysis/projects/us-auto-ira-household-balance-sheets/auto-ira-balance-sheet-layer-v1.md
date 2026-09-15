# Auto-IRA household balance-sheet layer v1

**Checked:** 2026-09-14  
**Status:** bounded policy-exposure finding; public-summary extraction, not an independent SIPP replication

## The result is multidimensional

The NBER Working Paper 35373 comparison of Oregon private-sector workers likely
exposed to OregonSaves with similar workers in not-yet-adopting states reports
that automatic workplace retirement saving increased IRA and employer-plan
ownership and assets. A Georgetown Center for Retirement Initiatives summary of
the paper reports a 2.7 percentage-point increase in IRA ownership to 12.7% and
more than $8,500 in IRA balances.

The same summary reports increases in checking/savings ownership and balances,
alongside a roughly 2 percentage-point increase in credit-card-debt incidence
and about a $90 increase in credit-card balances. The important program finding
is therefore not simply “saving rose.” Several balance-sheet margins moved at
once.

## Why the direction is not a net-security score

Retirement assets and checking balances can increase long-run and current
financial room, while credit-card borrowing can provide liquidity or carry
interest and repayment risk. Without contribution rates, withdrawals, cash-outs,
take-home pay, spending, credit limits, utilization, delinquency, and interest
costs, the public summary cannot tell whether the typical exposed household was
better off at the relevant horizon.

The study design is stronger than a simple before/after comparison: it uses SIPP
and compares likely Oregon exposure with similar workers in not-yet-adopting
states, with Oregon employer-size rollout timing contributing to the policy
contrast. The result remains a study-specific policy estimate, not a universal
effect for every state Auto-IRA or every worker.

## End-to-end connection

The supported chain is:

`automatic workplace-saving rule → retirement and liquid-account ownership/assets → credit-card borrowing and household liquidity management → unresolved current-versus-future security trade-off`

This advances the atlas from policy adoption to household balance-sheet
response. It does not yet reach consumption, take-home pay, debt service,
retirement timing, health, family care, trust, or political action.

## Counterexamples and next test

The interpretation should change if the full paper shows that the debt effect is
temporary and costless, that liquid savings do not rise after accounting for
withdrawals and cash-outs, or that gains are concentrated among workers who
already had access to employer retirement plans. It should also change if
low-income or liquidity-constrained workers experience different contribution,
debt, or take-home-pay responses.

The next extraction should obtain the full paper or appendix and preserve the
study's treatment definition, event timing, firm-size rollout, sample counts,
confidence intervals, income/age/job subgroups, and separate outcomes for
retirement assets, liquid accounts, debt, debt cost, and spending.

## Sources and reproducibility

- [Machine-readable record](../../records/us-nber-auto-ira-household-balance-sheets-2026.json)
- [NBER Working Paper 35373](https://www.nber.org/papers/w35373)
- [NBER DOI](https://doi.org/10.3386/w35373)
- [Georgetown Center for Retirement Initiatives state reports](https://cri.georgetown.edu/states/state-reports-and-briefs/)
- [Auto-IRA project source search](source-search-2026-09-11.md)

