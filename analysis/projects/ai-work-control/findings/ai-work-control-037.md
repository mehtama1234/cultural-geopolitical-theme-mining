# A 2026 opening rate does not restore worker mobility

**Status:** BLS JOLTS partial-year refresh · **Checked:** 2026-09-14

## The bounded finding

The January–July 2026 BLS JOLTS national series shows a 4.3714% average job-
openings rate, a 3.3143% hires rate, a 1.9571% quits rate, and a 3.2714% total-
separations rate. July is preliminary. Compared with the complete 2025 annual
means, openings are somewhat higher, hires are essentially unchanged, and
quits and total separations are lower.

That combination is consistent with a labor market in which vacancies remain
visible while worker movement is not accelerating. It does not establish that
workers have lost bargaining power, that jobs became worse, or that the same
people were unable to move.

## Establishment-rate comparison

| Measure | 2025 annual mean | 2026 Jan–Jul mean | Interpretation boundary |
|---|---:|---:|---|
| Job openings | 4.2750% | 4.3714% | Establishment openings rate; not a worker opportunity set |
| Hires | 3.3167% | 3.3143% | Establishment hires rate; not unique people hired |
| Quits | 2.0167% | 1.9571% | Voluntary-separation rate; not observed willingness or ability to leave |
| Layoffs/discharges | 1.1167% | 1.0714% | Employer-reported rate; not household insecurity |
| Total separations | 3.2917% | 3.2714% | Establishment rate; not a worker transition probability |

The 2026 values are arithmetic means of seven monthly seasonally adjusted
rates, not an annual estimate. The openings series is 4.4% in January, 4.2%
in February and March, 4.6% in April, 4.5% in May, 4.3% in June, and 4.4%
(preliminary) in July. The other rates and their monthly values remain in the
machine-readable record and raw HTML snapshots.

## Publication-vintage check

The BLS July 2026 release, published September 1, is still the latest JOLTS
release available at this checkpoint. BLS schedules the August 2026 release for
September 29. No August observation is therefore imputed or treated as
missing-data evidence; the partial-year comparison remains January–July, with
July preliminary and earlier months subject to revision.

## What this adds to the AI/work-control lane

```text
firm demand for labor
  -> openings and hiring capacity
  -> worker movement, retention, and outside options
  -> bargaining, discretion, pay, and household security
```

The refreshed JOLTS layer reaches only the first two establishment-level boxes.
It can condition the NBER task-adoption and OECD algorithmic-management layers
on a contemporaneous labor-market context, but it cannot turn adoption into
worker control or turn lower quits into a causal bargaining result.

The comparison also preserves an important counterexample: an openings rate
can remain above the prior-year average while quits and hires do not rise. That
may reflect recruiting difficulty, mismatch, sector composition, worker risk
aversion, retirement, or delayed hiring rather than a single “employer power”
mechanism.

## Limits and next test

- JOLTS reports establishments, not unique workers; annual or partial-year
  means do not measure individual transition probabilities.
- July 2026 is preliminary, and earlier months can be revised.
- National total-nonfarm rates conceal industry, occupation, age, race,
  education, place, union, disability, and schedule differences.
- Openings are not necessarily accessible to the workers who want to move;
  qualifications, geography, pay, hours, and care constraints are unobserved.
- No inference is made about AI adoption, algorithmic management, wages,
  dignity, health, bargaining, or household wellbeing from this record alone.

The next test is a sector- and worker-conditioned design linking JOLTS context
to CPS/ATUS worker movement, pay, hours, union representation, task adoption,
monitoring, schedule control, and household outcomes. The design must retain
places where quits remain high despite cooling openings and places where low
quits coexist with stable pay or improved conditions.

## Sources and reproduction

- [2026 YTD JOLTS record](../../../records/us-bls-jolts-national-mobility-2026-ytd.json)
- [BLS JOLTS openings series](https://data.bls.gov/timeseries/JTS000000000000000JOR)
- [BLS JOLTS hires series](https://data.bls.gov/timeseries/JTS000000000000000HIR)
- [BLS JOLTS quits series](https://data.bls.gov/timeseries/JTS000000000000000QUR)
- [BLS JOLTS definitions](https://download.bls.gov/pub/time.series/jt/jt.txt)
- [BLS July 2026 JOLTS release](https://www.bls.gov/news.release/jolts.htm)
- [BLS JOLTS release schedule](https://www.bls.gov/schedule/news_release/jolts.htm)
- [Prior 2020–2025 national record](../../../records/us-bls-jolts-national-mobility-2020-2025.json)

Reproduce the refresh with:

```bash
python3 scripts/fetch_bls_jolts_2026_html.py
```

**Evidence status:** official establishment-based partial-year rate context;
no worker-level mobility, causal bargaining, AI effect, household, or political
outcome estimate.
