# Auto-IRA retirement timing and Social Security claiming layer v1

**Checked:** 2026-09-14  
**Status:** bounded policy-exposure finding; primary working-paper extraction with companion issue brief

## The program reaches decisions beyond account ownership

The Georgetown Center for Retirement Initiatives working paper by Manita Rao,
Ngoc Dao, and Zeewan Lee uses Census Survey of Income and Program Participation
data from 2014–2024 for workers ages 55–75. The retirement-timing models contain
1,803,085 population-weighted person-wave observations; the claiming models
contain 1,801,923. The paper compares seven early-adopter states—Oregon,
Illinois, California, Connecticut, Colorado, Maryland, and Virginia—with
non-adopter states using Callaway–Sant'Anna staggered difference-in-differences,
state/year fixed effects, demographic and state controls, population weights,
and state-clustered wild-bootstrap inference.

The reported retirement-timing result is a 1.2 percentage-point reduction in
retirement before age 65 and a 3 percentage-point increase in retirement past
the full retirement age of 67. Retirement before age 67 falls by 0.9 percentage
points. The paper also reports a 3.8 percentage-point rise in IRA ownership and
a 2.3 percentage-point rise in 401(k) ownership, but no statistically
significant change in total retirement assets in the full-controls model.

For Social Security, early claiming between age 62 and full retirement age falls
by 1 percentage point, while claiming at age 70 rises by 1.8 percentage points.
The paper uses a typical-earner illustration to explain the stakes: delaying
from age 62 to 70 is associated with about 77% or $1,028 more in monthly
benefits. That illustration is not the policy's causal income effect.

## What this adds to the balance-sheet layer

The earlier balance-sheet layer showed that retirement and liquid-account
ownership/assets can rise while credit-card debt also rises. This layer adds a
possible life-course channel:

`automatic enrollment → assets, salience, and liquidity → later retirement and Social Security claiming → potentially higher later monthly income`

The mechanism is not identified as one thing. The authors propose a liquidity
channel—savings reduce pressure to claim early—and a behavioral/information
channel—automatic enrollment and account statements make retirement choices more
visible. Both can be true, but the public brief does not separate their shares.

## Why “later” is not automatically “better”

Later retirement can mean more time to accumulate assets and more ability to
delay claiming. It can also mean that a person could not afford to stop, faced
poor health or care obligations, or lacked a viable alternative. A higher Social
Security monthly benefit can improve later income while requiring more years of
work and postponing access to benefits. The finding therefore measures a change
in timing and an associated benefit schedule, not a net-security or wellbeing
score.

The paper's subgroup tables show timing effects concentrated among women and
workers with lower educational attainment, with additional heterogeneity by
race/ethnicity and marital status. For example, the paper reports a 1.8
percentage-point reduction in early retirement among women and a 2.5-point
reduction among workers without a high-school diploma. These are subgroup
estimates, not proof that the mechanism is liquidity or that every member of a
group benefits.

The paper does not observe whether the account is an Auto-IRA or employer
401(k), does not provide a formal mediation decomposition, and does not measure
health, care obligations, job quality, or the welfare value of working longer.

## Evidence boundary and next test

The result supports a bounded policy-exposure estimate between state Auto-IRA
adoption and later retirement/claiming patterns in the paper's SIPP design. It
does not establish improved health, job quality, schedule control, retirement
adequacy, lifetime welfare, or a universal effect across states and workers.
Colorado and Virginia adopted in 2023, so the authors describe incomplete
exposure as making the estimates conservative lower bounds. Event-study plots,
alternative controls, exclusion of late adopters, and a TWFE comparison provide
useful robustness evidence, but do not eliminate all contemporaneous state-policy
confounding.

The next extraction should recover code or additional appendices, replicate the
event-study and wild-bootstrap calculations, and join the timing estimates to
health, care, job quality, account type, debt cost, and household needs. It must
also reconcile this paper's no-significant-retirement-assets and small
unsecured-debt results with the separate NBER balance-sheet summary rather than
pooling the estimates.

## Sources and reproducibility

- [Machine-readable record](../../records/us-georgetown-auto-ira-retirement-claiming-2026.json)
- [Georgetown issue brief](https://cri.georgetown.edu/wp-content/uploads/2026/07/Manita-Rao-et-al.-_Issue-Brief-Beyond-Account-Ownership-.pdf)
- [Underlying Georgetown working paper](https://cri.georgetown.edu/wp-content/uploads/2026/06/CRI_WP_Rao_Dao_Lee_AutoIRA_final.pdf)
- [Related NBER balance-sheet paper](https://www.nber.org/papers/w35373)
- [Census SIPP program](https://www.census.gov/programs-surveys/sipp.html)
- [Auto-IRA project source search](source-search-2026-09-11.md)

The numerical effects and sample/method details are recorded from the Georgetown
working paper, with the issue brief retained as a companion summary. The two
Auto-IRA studies are separate evidence layers with different reported outcomes;
their balance-sheet estimates should not be averaged or treated as one pooled
effect.
