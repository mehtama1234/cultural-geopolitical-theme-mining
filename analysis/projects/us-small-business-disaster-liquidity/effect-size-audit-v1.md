# Effect-size audit v1: disaster loans and small firms

**Checked:** 2026-09-17  
**Purpose:** add quantitative scale to the disaster-liquidity finding without
retaining the working-paper PDF, code, or restricted data.

## Version boundary

The official NBER page for Working Paper 32326 currently identifies a revised
September 2026 version and gives directional results. The numerical estimates
below are transcribed from the authors' earlier March 15, 2023 version,
“After the Storm: Direct and Spillover Benefits from Disaster Loans to Small
Businesses,” hosted by the American Finance Association. They are not silently
treated as estimates from the current revision. A later audit should recheck
every number against the revised paper before using it for a pooled estimate.

## Design and denominator

- U.S. SBA business disaster-loan applications from 2005–2017; 167,000 unique
  firms applied.
- SBA provided $5.3 billion to 54,500 firms; applicants collectively had more
  than 230,000 employees at application.
- The causal sample uses 22 owner-FICO approval thresholds across 916
  disasters, with an IV difference-in-differences design and a 29-FICO-point
  bandwidth. The paper reports about 24,000 unique firms in the RDD bandwidth.
- Applications are linked to Census business records and Experian business
  credit reports; outcomes are followed annually from five years before to
  seven years after the disaster.
- The Census match rate is reported as 82% of SBA applicant firms. Outcome
  universes differ: exit and deformalization use firm panels, employment
  excludes nonemployers, revenue is available for a subset, and credit outcomes
  come from annual Experian snapshots.

## Transcribed estimates

| Outcome | Estimate | Unit / comparison | Interpretation boundary |
|---|---:|---|---|
| Firm exit | -13 percentage points | causal effect of receiving a disaster loan | 115% of the sample mean; largest magnitudes appear in years 6–7 |
| Employer → nonemployer transition | -5 percentage points | causal effect | 85% of the mean; a status transition, not proof of job quality |
| Employment, full sample | +18% | causal relative effect; about +0.5 worker | Includes many nonemployer observations in the broader firm sample |
| Employment, employer firms | +45% | causal relative effect; about +5 workers | Employer-firm universe; does not measure wages, hours, safety, or retention |
| Revenue, employer firms | about +200% of mean | causal relative magnitude as described in the paper | Revenue is not household income or customer welfare |
| Non-SBA private debt | +$18,000 | average causal effect; about 200% of mean | Credit expansion may be complementary to recovery but adds obligations |
| Bankruptcy filing | about -3.8 percentage points | causal effect; more than 100% of mean | Filing is not the same as total financial burden or repayment success |
| Local firm entry | about +8 firms | local spillover; about 8% of mean | Positive entry evidence; not a direct customer-access or affordability measure |

The paper also reports suggestive negative spillovers for incumbent neighbor
firms. That result remains a counterweight to the positive focal-firm and entry
effects and should not be collapsed into the local-entry estimate.

## What this changes in the atlas

The case now supports a more precise middle-layer claim: around the approval
thresholds studied, disaster credit changed firm survival, formal employment,
revenue, private borrowing, and bankruptcy at economically large magnitudes.
The estimates still do not identify who received the gains within the firm,
whether customers retained affordable services, whether owners' households
recovered, or whether public legitimacy and political action changed.

The 13-point exit estimate is especially important for the atlas because it is
a firm-level continuation outcome rather than a program-intent statement. The
18% / 45% employment estimates are useful but must remain separate from worker
security: the source does not report pay, hours, benefits, schedule control,
working conditions, or involuntary turnover. The $18,000 private-credit result
also means “recovery” includes a new financial commitment, not only a restored
capacity.

## Reproduction and storage decision

This is a transcription audit, not a replication. No PDF, code, microdata, or
restricted Census/SBA/Experian extract was downloaded or retained locally. The
next validation target is the revised NBER version's tables and appendices; a
small table excerpt or official supplementary artifact is sufficient. Do not
promote a pooled estimate until version, outcome universe, treatment definition,
standard errors, and table location are rechecked.

## Sources

- [Current NBER Working Paper 32326 page](https://www.nber.org/papers/w32326)
- [Authors' March 15, 2023 version hosted by the American Finance Association](https://afajof.org/management/viewp.php?n=42000)
