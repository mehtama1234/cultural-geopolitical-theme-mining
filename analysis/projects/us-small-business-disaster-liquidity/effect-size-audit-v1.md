# Effect-size audit v1: disaster loans and small firms

**Checked:** 2026-09-18
**Purpose:** add quantitative scale to the disaster-liquidity finding without
retaining the working-paper PDF, code, or restricted data.

## Version boundary

The official NBER page identifies a September 2026 revision, and the current
paper PDF was checked at the table level on 2026-09-18. The current estimates
below are transcribed from Table 4 (real outcomes), Table 5 (credit outcomes),
and the current Appendix F heterogeneity tables. The earlier March 15, 2023
author version remains useful only as a labeled historical anchor; it is not
silently pooled with the current revision.

## Design and denominator

- U.S. SBA business disaster-loan applications from 2005–2017; the current
  paper reports 167,202 distinct firms and approximately 1,900 disasters.
- SBA provided $5.3 billion to 54,500 firms; applicants collectively had more
  than 230,000 employees at application.
- The causal sample uses 13 owner-FICO approval thresholds across the disaster
  application records, with an IV difference-in-differences design and a
  29-FICO-point bandwidth. Table 4 reports outcome-specific panel observation
  counts, not one common firm denominator.
- Applications are linked to Census business records and Experian business
  credit reports; outcomes are followed annually from five years before to
  seven years after the disaster.
- The Census match rate is reported as 82% of SBA applicant firms. Outcome
  universes differ: exit and deformalization use firm panels, employment
  excludes nonemployers, revenue is available for a subset, and credit outcomes
  come from annual Experian snapshots.

## Current September 2026 table-level estimates

| Outcome | Estimate | Unit / comparison | Interpretation boundary |
|---|---:|---|---|
| Firm exit, all firms | -13.2 percentage points (SE 4.13 pp) | Table 4 Panel A IV estimate; mean 11.5% | Persistent firm-level survival effect; not household recovery |
| Employer → nonemployer transition, all firms | -5.15 percentage points (SE 2.81 pp) | Table 4 Panel A IV estimate; mean 5.9% | Formal-status transition, not proof of job quality |
| Log employment, all firms | +0.170 log points (SE 0.0831) | Table 4 Panel A IV estimate; mean log employment 1.042 | Approximately 18% relative; does not measure pay, hours, or security |
| Log revenue, all firms | +0.196 log points (SE 0.143; not starred) | Table 4 Panel A IV estimate; mean log revenue 4.384 | Current all-firm estimate is not statistically distinguishable from zero at the displayed convention |
| Firm exit, employer firms | -16.9 percentage points (SE 6.41 pp) | Table 4 Panel B IV estimate; mean 8.4% | Employer-firm universe; not worker-level retention |
| Log employment, employer firms | +0.376 log points (SE 0.183) | Table 4 Panel B IV estimate; mean log employment 1.413 | About 2.25 workers in the paper's interpretation, not five |
| Log revenue, employer firms | +0.719 log points (SE 0.254) | Table 4 Panel B IV estimate; mean log revenue 6.025 | Roughly 100% of mean in the paper's discussion; not household income |
| Bankruptcy filing | -3.8 percentage points (SE 2.2 pp) | Table 5 Panel A IV estimate; mean 2.8% | Filing is not total financial burden or repayment success |
| Non-SBA private debt | +$17,712 (SE $3,432) | Table 5 Panel B IV estimate; mean $7,934, in $000s | Credit expansion may complement recovery but adds obligations |
| Days late on all contracts | -34.996 days (SE 9.676) | Table 5 Panel A IV estimate; mean 16.675 days | Financial performance measure, not household liquidity or job quality |
| Local firm entry | +7.901 firms (SE 4.382) | Appendix I Table I2 neighbor-spillover estimate | Marginal spillover; not direct customer affordability or access |

The current Appendix F results also sharpen heterogeneity: the paper does not
find significantly stronger exit or private-debt effects for several pre-existing
credit-constraint groups, while capital-intensive firms show a large exit
effect. These subgroup results are mechanism evidence, not a general ranking
of who benefits from disaster credit.

The paper also reports suggestive negative spillovers for incumbent neighbor
firms. That result remains a counterweight to the positive focal-firm and entry
effects and should not be collapsed into the local-entry estimate.

## What this changes in the atlas

The current revision supports a more precise middle-layer claim: around the
approval thresholds studied, disaster credit changed firm survival, formal
employment, private borrowing, delinquency, and bankruptcy, with the strongest
current real-outcome evidence concentrated in survival and employer-firm
outcomes. The all-firm revenue estimate is not statistically distinguishable
from zero in Table 4. The estimates still do not identify who received the
gains within the firm, whether customers retained affordable services, whether
owners' households recovered, or whether public legitimacy and political action
changed.

The 13.2-point exit estimate is especially important for the atlas because it is
a firm-level continuation outcome rather than a program-intent statement. The
18% full-sample and roughly 2.25-worker employer-firm employment estimates
must remain separate from worker security: the source does not report pay,
hours, benefits, schedule control, working conditions, or involuntary turnover.
The roughly $17,700 private-credit result also means “recovery” includes a new
financial commitment, not only restored capacity.

## Reproduction and storage decision

This is a transcription audit, not a replication. The current NBER PDF was
read transiently and not retained; no code, microdata, or restricted
Census/SBA/Experian extract was downloaded or retained locally. The current
PDF SHA-256 is recorded in the canonical record. Version, outcome universe,
treatment definition, standard errors, and table locations are now explicit;
the result must still not be promoted to a pooled estimate across outcome
universes.

## Sources

- [Current NBER Working Paper 32326 page](https://www.nber.org/papers/w32326)
- [Current September 2026 NBER PDF](https://www.nber.org/system/files/working_papers/w32326/w32326.pdf)
- [Authors' March 15, 2023 version hosted by the American Finance Association](https://afajof.org/management/viewp.php?n=42000)
