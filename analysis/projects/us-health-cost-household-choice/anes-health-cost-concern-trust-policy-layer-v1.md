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

**Retrieval hashes:** trust query HTML `sha256:6997ea1080f7e585ec3c5da5e4e7646bbc939361c792a415c94d82d5948cb4bd`; policy query HTML `sha256:95c22e3bfa69bd701ee3fe12a6440150aa3d93a7ee40b1e145663cfb42559c4a`.
