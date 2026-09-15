# GSS 2024 financial position, trust, and political orientation layer v1

The 2024 General Social Survey supplies a new meaning-and-politics layer for
the material-pressure program. It places financial satisfaction and perceived
financial trajectory beside generalized trust, fairness expectations,
ideological self-placement, and 2024 presidential vote intention in the same
cross-sectional respondent file.

| Financial position | Can trust most people | People try to be fair | Liberal/slightly liberal | Conservative/slightly conservative |
|---|---:|---:|---:|---:|
| Pretty well satisfied | 32.47% | 58.71% | 34.33% | 39.02% |
| More or less satisfied | 27.72% | 46.54% | 27.70% | 33.11% |
| Not satisfied at all | 14.90% | 24.15% | 22.09% | 35.67% |

Among respondents reporting their financial situation as better, 26.66% said
most people can be trusted and 44.22% said people try to be fair. Among those
reporting a worse financial situation, the corresponding estimates were 24.68%
and 35.73%. In the valid combined 2024 vote-intention universe, Trump
intention/report was 29.85% in the better-finances group and 50.08% in the
worse-finances group; Harris intention/report was 43.34% and 22.24%.

The key interpretation is relational rather than causal. Financial
dissatisfaction coexists with lower generalized trust and fairness expectations,
while financial trajectory coexists with a different political orientation.
But the pattern may be jointly structured by party identity, ideology, age,
education, race, health, media, local conditions, and retrospective judgment.
The survey does not establish that financial experience produced trust or vote
intention.

Estimates use `WTSSNRPS`, the 2024 GSS person post-stratification weight
adjusted for nonresponse. Trust and fairness are module-specific and have
smaller valid universes than the full respondent file; every estimate retains
its own valid-field count. The candidate measure combines the two 2024 form
versions (`WHOVOTE24` and `WHOVOTE24A`), which ask the corresponding presidential
vote-intention question before and after the July form update. It is not
verified turnout or a completed vote.

The 2024 GSS is multi-mode and has design changes and module-specific missingness.
This record should not be treated as a direct unadjusted time trend with older
GSS years; a separate harmonization audit is required for that. It also does
not measure a dated bill, local exposure, institutional remedy, household time
allocation, consumer exit, or geopolitical action.

[Machine-readable record](../../records/us-gss-financial-trust-politics-2024.json)  
Analysis script: `scripts/analyze_gss2024_finance_trust_politics.py`

Sources: [NORC GSS data page](https://gss.norc.org/get-the-data.html) and
[2024 GSS codebook](https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook%20R3.pdf).
