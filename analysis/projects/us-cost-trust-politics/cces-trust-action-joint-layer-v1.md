# CCES joint trust/action and material-work proxy layer v1

This layer separates trust from civic action by measuring their joint
co-occurrence within four 2024 CCES material/work proxy cells.

| Proxy cell | Federal trust + action | State trust + action | Federal low trust + action |
|---|---:|---:|---:|
| No gig work; no student debt (n=17,954) | 16.42% | 24.85% | 18.66% |
| No gig work; student debt (n=2,853) | 17.22% | 26.33% | 22.65% |
| Gig work; no student debt (n=2,058) | 18.17% | 24.55% | 19.94% |
| Gig work; student debt (n=665) | 30.32% | 33.82% | 16.11% |

The joint high-trust/action share is highest in the smallest gig-work/student-
debt cell, while low federal trust with action is not highest there. This is a
useful counterexample to treating distrust and civic withdrawal as the same
outcome: people can report low trust and still act, and trust/action can
co-occur differently across material/work proxy cells.

The result is descriptive and weighted with `commonpostweight`; no
complex-survey variance estimate is computed. Gig work and student-loan
responsibility are cross-sectional proxies, not dated shocks. Composition,
political identity, age, education, income, selection, and prior trust remain
alternative explanations. The design does not measure attribution, causal
exposure, turnout, vote, remedy, or later material security.

The [machine-readable record](../../records/us-cces-trust-action-joint-material-proxies-2024.json)
preserves the four proxy denominators, joint outcome definitions, source hash,
and open causal/meaning links. Reproduction:
`python3 scripts/analyze_cces_trust_action_joint.py --input
/tmp/cces24-common.csv --output /tmp/cces-trust-action-joint.json`.

Source: [CCES 2024 Harvard Dataverse record](https://doi.org/10.7910/DVN/X11EP6).
