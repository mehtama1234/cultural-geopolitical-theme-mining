# NBER W35090 acquisition audit v1

**Checked:** 2026-09-14  
**Status:** author-hosted full-paper artifact and pre-registration retrieved and audited

## Source

- [NBER paper page](https://www.nber.org/papers/w35090)
- [NBER PDF endpoint](https://www.nber.org/system/files/working_papers/w35090/w35090.pdf)
- [Author-hosted August 2026 PDF](https://www.dropbox.com/scl/fi/31mdzavelzr0fuyw9maym/BGKT_2026.pdf?dl=0&rlkey=fh15qmim9kph8ljrtvt8qjusr&st=z1m94vyy)
- [AEA RCT Registry AEARCTR-0016642](https://www.socialscienceregistry.org/trials/16642)
- Title: *Information Treatments, Hypotheticals, and Event Studies: Comparative Estimates*
- Authors: Carola Binder, Dimitris Georgarakos, Pei Kuang, and Li Tang
- Working Paper 35090; issue date April 2026; revision date September 2026

## Full-paper and registration audit

The official NBER abstract reports a two-wave survey around the Federal
Reserve's September 2025 rate cut. It embeds three designs: randomized
hypothetical scenarios, randomized information provision, and surveys fielded
immediately before and after an actual announcement. The abstract reports the
same qualitative direction across designs—rate cuts are associated with lower
inflation and unemployment expectations and stronger expected economic
activity—but says vignette estimates are substantially larger than average RCT
and event-study estimates. The difference narrows when the comparison focuses
on RCT respondents for whom the decision was new information and on respondents
who knew about the decision before the event study.

The author-hosted August 2026 PDF reports 4,067 valid one-year-inflation
vignette observations, 1,308 recontacted respondents in the RCT, and 6,968
pooled event-study observations with a 1,308-person balanced panel. The key
one-year inflation estimates are −2.043 percentage points for the 25 bp
vignette versus no change (SE 0.216), −0.833 for the full RCT (SE 0.156),
−1.937 among the previously unaware (SE 0.224), −0.721 for the balanced panel
(SE 0.121), and −1.299 among respondents who correctly perceived the cut (SE
0.080). Respondents who did not hear or did not know show −0.058 (SE 0.136).

The registry was initially submitted August 29, 2025 and published September
3, 2025. It planned approximately 4,800 Wave 1 and 2,100 Wave 2 respondents,
approximately 800 per Wave 1 arm and 700 per Wave 2 arm, with individual-level
computer randomization and no clustering. The registered primary outcome is
macroeconomic-expectation updating under hypothetical versus factual policy
information. The registry page states that some information is unavailable, so
the plan is a design benchmark, not a substitute for the final analytic sample
or paper estimates.

The full paper and registry together strengthen the measurement finding: the
same broad expectation direction appears across designs, but the magnitude
depends on hypothetical versus factual information, prior knowledge, and
natural announcement exposure. Neither artifact establishes actual spending,
saving, borrowing, portfolio change, trust, or political behavior.

## Acquisition result and hashes

The official NBER PDF endpoint returned HTTP 403 in this environment. The
author-hosted PDF was retrieved on 2026-09-14 and hashed locally:

```text
sha256:4b3a566790f2b3ddf72ad71a00bdba960fe2a68351dedf36513f753505f399eb
```

The registry page was retrieved and hashed locally:

```text
sha256:23a18640141be2132928a454d87b110d52574ae5545f12632537259b035a6f66
```

## Remaining promotion gate

The structured record and detailed finding now promote the full-paper estimates
with their design-specific denominators, uncertainty, subgroup boundaries, and
hashes. The remaining work is to compare the registered analysis plan with the
paper's final estimands and to connect expectation revisions to borrower/saver
exposure and realized household action. Those are open arrows, not missing
paper-retrieval tasks.
