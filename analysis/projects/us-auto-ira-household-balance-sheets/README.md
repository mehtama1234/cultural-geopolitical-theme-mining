# Project: US Auto-IRA and household balance sheets

## Question

When a state makes saving automatic, does a household gain a real buffer or just move money while adding another debt?

## Short first pass

Separate enrollment, account ownership, account balance, credit-card debt, take-home pay, employer choice and retirement security.

## Possible connection

A workplace savings rule can change the household balance sheet without changing wages. It may build savings and bank access while also changing short-run spending or borrowing.

## Decision rule

Move on after one state policy comparison, one observed balance-sheet result, and one measure of take-home pay or debt cost. Do not call a higher account balance an improvement in security without checking the debt and spending side.

The [Auto-IRA balance-sheet layer](auto-ira-balance-sheet-layer-v1.md) now
records the bounded NBER result: retirement ownership/assets and checking/savings
ownership/balances increase alongside a modest rise in credit-card debt. The
[published finding](findings/us-auto-ira-household-balance-sheets-001.md)
keeps current liquidity, debt cost, take-home pay, spending, and retirement
adequacy separate. The full paper or appendix remains required for a complete
subgroup and mechanism analysis.

The [retirement-timing layer](auto-ira-retirement-claiming-layer-v1.md) extends
the question to later work and Social Security claiming. A Georgetown brief
reports lower early retirement/claiming and higher work past age 67/claiming at
70 in a SIPP policy-timing comparison, while leaving the choice-versus-constraint
mechanism, health, job quality, and net lifetime welfare open. Its
[published finding](findings/us-auto-ira-retirement-claiming-001.md) is kept
separate from the balance-sheet result because timing is not a welfare score.

The underlying working paper is now available and records 1,803,085 retirement-
timing person-wave observations and 1,801,923 claiming observations, with
Callaway–Sant'Anna staggered difference-in-differences, population weighting,
state-clustered wild-bootstrap inference, event studies, robustness checks, and
subgroup tables. It reports no statistically significant full-controls change
in total retirement assets and a small unsecured-debt decline. Those estimates
must not be mechanically combined with the separate NBER balance-sheet summary,
which reports different balance-sheet directions; reconciling the two papers is
an explicit next task.

The [cross-paper reconciliation layer](auto-ira-cross-paper-reconciliation-v1.md)
now keeps the NBER Oregon/firm-size balance-sheet estimate separate from the
CRI seven-state retirement-timing estimate. Their reported checking, debt, and
retirement-asset directions are not pooled because the accessible materials do
not establish common samples, variables, treatment intensity, or estimands.

The program-level [automatic-saving multi-currency bridge](../../findings/us-automatic-saving-multi-currency-policy-bridge-001.md)
places both policy studies beside Federal Reserve liquidity/credit and BEA
income/spending context. It makes the end-to-end chain explicit—enrollment,
current liquidity, borrowing, retirement timing, later security, and meaning—
while preserving the cross-paper disagreement as the next harmonization task.
