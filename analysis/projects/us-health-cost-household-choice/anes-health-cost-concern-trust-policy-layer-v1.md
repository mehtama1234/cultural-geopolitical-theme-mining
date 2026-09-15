# ANES health-cost concern, trust, and policy-demand layer v1

**Checked:** 2026-09-15  
**Status:** official SDA weighted descriptive panel tables; not causal

## Question

Can a repeated ANES respondent-level survey connect concern about paying
health-care expenses to institutional trust and a later health-policy
judgment?

```text
pre-election health-care payment concern
  -> pre-election federal-government trust
  -> post-election demand for government help paying for health insurance
```

This is a concern-to-judgment layer. It is not a dated medical-bill,
care-foregoing, or remedy-to-legitimacy estimate.

## Source and design

The tables use the official ANES 2024 Full Release SDA interface and the
2016–2020–2024 panel subset. The merged panel has nine waves and 2,171 2024
pre-election and 2,070 post-election interviews. SDA reports weighted row
percentages, unweighted case counts, weighted N, and Taylor-series standard
errors using the published stratified-cluster design variables.

## Results

### Health-care payment concern × federal-government trust

Valid cases: 5,189. Pre-election raked weight: `V240107a`. Percentages are
within each health-cost-concern row.

| Concern | Always | Most of time | About half | Some of time | Never |
|---|---:|---:|---:|---:|---:|
| Not at all concerned | 1.3% | 15.4% | 30.1% | 40.6% | 12.7% |
| A little concerned | 0.3% | 11.7% | 34.1% | 43.0% | 10.9% |
| Moderately concerned | 0.9% | 11.2% | 25.6% | 43.6% | 18.7% |
| Very concerned | 2.1% | 11.0% | 22.1% | 42.4% | 22.3% |
| Extremely concerned | 4.4% | 9.7% | 22.8% | 43.0% | 20.1% |

The combined “some of the time” or “never” trust share is 53.3% for the
not-at-all-concerned row and 63.1% for the extremely concerned row. The
pattern is not a simple monotonic trust collapse: the “always” category is
also higher in the smallest, extremely concerned cell.

### Health-care payment concern × post-election health-insurance help

Valid cases: 4,650. Post-election raked weight: `V240107b`. Percentages are
within each pre-election concern row.

| Concern | Increase spending | Decrease spending | No change |
|---|---:|---:|---:|
| Not at all concerned | 57.5% | 15.5% | 27.0% |
| A little concerned | 56.8% | 15.3% | 27.8% |
| Moderately concerned | 60.0% | 14.3% | 25.7% |
| Very concerned | 62.3% | 17.4% | 20.3% |
| Extremely concerned | 61.3% | 14.4% | 24.3% |

Support for increased government help is higher in the very and extremely
concerned rows than in the not-at-all row, but the pattern is modest and not
monotonic. The table measures policy preference, not remedy receipt,
complaint, appeal, vote rationale, or other direct political action.

### Party-identity conditioning

The same trust table was controlled by pre-election party identification
(`V241227x`), with 5,166 valid cases. Among strong Democrats, the combined
“some of the time” or “never” trust share was 32.1% for the not-at-all-
concerned row and 46.7% for the extremely concerned row. Among strong
Republicans, the corresponding shares were 63.5% and 67.5%. Among
independents, they were 71.8% and 73.1%. The extreme-concern cells are small
in several party groups and have large standard errors. The controlled result
therefore weakens any pooled interpretation: prior identity explains much of
the trust level, while the health-cost-concern gradient is not uniform.

### Insurance-status conditioning

The same trust table was controlled by current insurance status (`V241571`),
with 5,182 valid cases. Among insured respondents, the combined “some of the
time” or “never” trust share was 53.6% for those not at all concerned and
64.0% for those extremely concerned. Among uninsured respondents, the
corresponding shares were 49.4% and 61.3%. The uninsured cells are much
smaller and less precise. The direction is similar in both coverage groups,
but this remains descriptive: insurance status does not identify plan
adequacy, a bill, or a care decision.

The health-condition control was also applied to the post-election policy
endpoint, with 4,602 valid cases. Among respondents with no condition
mentioned, support for increased government help was 57.6% in the not-at-all-
concerned row and 57.9% in the extremely concerned row. Among respondents
mentioning a condition, the corresponding shares were 58.4% and 72.1%.
The latter extreme-concern cell is small and imprecise; it is evidence for
stratified testing, not proof that a health need caused policy demand.

### Health-condition conditioning

Controlling the trust table by the reported health-related condition indicator
(`V241574a`) produced 5,126 valid cases. For respondents with no condition
mentioned, “some/never” trust was 53.1% among those not at all concerned and
60.6% among those extremely concerned. Among respondents mentioning a
condition, the corresponding shares were 52.4% and 74.4%. The extreme-
concern condition cell is small, so the larger gradient is a signal for a
health-need mechanism, not a causal estimate.

### Household-income conditioning

Controlling the trust table by the six-category household-income summary
(`V241567x`) produced 4,945 valid cases. The “some/never” trust share among
respondents not at all concerned versus extremely concerned was 50.5% versus
63.8% below $10,000, 53.9% versus 67.7% at $100,000–$249,999, and 42.1%
versus 66.0% at $250,000 or more. The highest-income extreme-concern cell has
only six unweighted cases; income is annual and does not measure liquid room,
deductible exposure, or a medical bill.

The income control was also applied to the post-election policy endpoint.
Support for increased government help among the least versus most concerned
was 48.2% versus 62.0% below $10,000, 55.9% versus 59.5% at $100,000–$249,999,
and 59.6% versus 92.9% at $250,000 or more. The last extreme-concern cell has
only six unweighted cases, and several low-income cells are also small. This
is a precision warning and a design input, not a reliable income gradient.

Party identity was also applied to the post-election policy endpoint, with
4,633 valid cases. Support for increased government help among the least
versus most concerned was 84.6% versus 71.2% for strong Democrats, 30.7%
versus 50.0% for strong Republicans, and 49.0% versus 55.4% for independents.
The direction differs by identity, and several extreme-concern cells are
small. This is evidence that party identity structures policy translation;
it is not evidence that health-cost concern caused the policy preference.

## Interpretation and limits

These tables establish a directly measured same-survey bridge from health-care
payment concern to trust and policy preference, with temporal ordering for the
policy table. They do not establish that health costs caused trust or policy
demand. Concern may reflect income, health status, insurance security,
ideology, party identity, prior government views, or information.

The tables do not connect to MEPS or SHED respondents. They do not observe a
specific bill, amount owed, care delayed or forgone, payment alternative,
provider/insurer response, remedy effort, switching, exit, or direct
attribution. The result strengthens the layered bridge but does not close the
health-cost-to-legitimacy chain.

## Sources and reproducibility

- [Official ANES SDA interface](https://sda.berkeley.edu/sdaweb/analysis/?dataset=anes2024full)
- [Trust table query](https://sda.berkeley.edu/sdaweb/analysis/exec?cflevel=95&ch_color=yes&rowpct=on&dataset=anes2024full&decdeft=3&decpcts=1&decse=1&decstats=2&decwn=1&design=complex&formid=tbf&row=V241573&column=V241229&sdaprog=tables&se=on&unweightedn=on&weightedn=on&weightlist=V240107a)
- [Policy-demand table query](https://sda.berkeley.edu/sdaweb/analysis/exec?cflevel=95&ch_color=yes&rowpct=on&dataset=anes2024full&decdeft=3&decpcts=1&decse=1&decstats=2&decwn=1&design=complex&formid=tbf&row=V241573&column=V242351&sdaprog=tables&se=on&unweightedn=on&weightedn=on&weightlist=V240107b)
- [ANES 2024 codebook](https://electionstudies.org/wp-content/uploads/2026/05/anes_timeseries_2024_userguidecodebook_20260519.pdf)
- [ANES merged panel documentation](https://electionstudies.org/data-center/2016-2020-2024-panel-merged-study/)
- [Party-conditioned trust table query](https://sda.berkeley.edu/sdaweb/analysis/exec?cflevel=95&ch_color=yes&control=V241227x&rowpct=on&dataset=anes2024full&decdeft=3&decpcts=1&decse=1&decstats=2&decwn=1&design=complex&formid=tbf&row=V241573&column=V241229&sdaprog=tables&se=on&unweightedn=on&weightedn=on&weightlist=V240107a)
- [Insurance-conditioned trust table query](https://sda.berkeley.edu/sdaweb/analysis/exec?cflevel=95&ch_color=yes&control=V241571&rowpct=on&dataset=anes2024full&decdeft=3&decpcts=1&decse=1&decstats=2&decwn=1&design=complex&formid=tbf&row=V241573&column=V241229&sdaprog=tables&se=on&unweightedn=on&weightedn=on&weightlist=V240107a)
- [Health-condition-conditioned trust table query](https://sda.berkeley.edu/sdaweb/analysis/exec?cflevel=95&ch_color=yes&control=V241574a&rowpct=on&dataset=anes2024full&decdeft=3&decpcts=1&decse=1&decstats=2&decwn=1&design=complex&formid=tbf&row=V241573&column=V241229&sdaprog=tables&se=on&unweightedn=on&weightedn=on&weightlist=V240107a)
- [Income-conditioned trust table query](https://sda.berkeley.edu/sdaweb/analysis/exec?cflevel=95&ch_color=yes&control=V241567x&rowpct=on&dataset=anes2024full&decdeft=3&decpcts=1&decse=1&decstats=2&decwn=1&design=complex&formid=tbf&row=V241573&column=V241229&sdaprog=tables&se=on&unweightedn=on&weightedn=on&weightlist=V240107a)
- [Income-conditioned policy-demand query](https://sda.berkeley.edu/sdaweb/analysis/exec?cflevel=95&ch_color=yes&control=V241567x&rowpct=on&dataset=anes2024full&decdeft=3&decpcts=1&decse=1&decstats=2&decwn=1&design=complex&formid=tbf&row=V241573&column=V242351&sdaprog=tables&se=on&unweightedn=on&weightedn=on&weightlist=V240107b)
- [Party-conditioned policy-demand query](https://sda.berkeley.edu/sdaweb/analysis/exec?cflevel=95&ch_color=yes&control=V241227x&rowpct=on&dataset=anes2024full&decdeft=3&decpcts=1&decse=1&decstats=2&decwn=1&design=complex&formid=tbf&row=V241573&column=V242351&sdaprog=tables&se=on&unweightedn=on&weightedn=on&weightlist=V240107b)

**Retrieval hashes:** trust query HTML `sha256:6997ea1080f7e585ec3c5da5e4e7646bbc939361c792a415c94d82d5948cb4bd`; policy query HTML `sha256:95c22e3bfa69bd701ee3fe12a6440150aa3d93a7ee40b1e145663cfb42559c4a`; party-conditioned trust query HTML `sha256:e7ab61b4096f960853b6197f658f8f860d012faa1d32d6c97f9992087e11eec3`; insurance-conditioned trust query HTML `sha256:3675e34518b109b00eefa210a82f6cc83e460433766fd6ca31640c1f12f11b36`; condition-conditioned trust query HTML `sha256:b4e6a92dde5d17752d7a01b54cf3b50607a26255e27a7c95cc7c8113f46d500f`; income-conditioned trust query HTML `sha256:8d6f9fb98e04cd561aae6d1436feebdffa31ca5b992298c448bc7660bb6b5d11`; condition-conditioned policy query HTML `sha256:618d6b7ae7671e05300a822ed42250b704b29831f4849ce9bd65bd49a5a29c9c`; income-conditioned policy query HTML `sha256:804896f1506a9ae6b75bfeac1463d719892f1b846d79591efc2a86a64745c804`; party-conditioned policy query HTML `sha256:d8079f90258a273d4fe8c7bcb053a660fb2ab80470598eb1c2278cabfaa58b3b`.
