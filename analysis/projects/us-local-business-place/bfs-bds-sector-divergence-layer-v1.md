# BFS–BDS sector divergence layer v1

**Checked:** 2026-09-13  
**Unit:** national sector, 2023  
**Sources:** Census Business Formation Statistics and Business Dynamics
Statistics  
**Status:** descriptive comparison of early applications and realized flows;
not a firm-conversion, survival, quality, or causal estimate

## The question

Does a large flow of business applications imply the same kind of realized
economic capacity across sectors?

```text
business applications
  -> establishment openings and closings
  -> net job creation or loss
  -> services, work, ownership, prices, and local life
```

The first arrow is a signal of planned or prospective activity. The BDS fields
are realized annual establishment and job flows. Comparing them exposes where
the societal story changes by sector.

## Selected divergence metrics

`Openings per 100 applications` and `net jobs per 100 applications` are
comparison ratios, not conversion rates. BFS and BDS have different timing,
units, and constructions.

| Sector | Applications | Openings per 100 applications | Net jobs per 100 applications | Openings minus closings |
|---|---:|---:|---:|---:|
| Retail trade | 971,630 | 8.0 | 5.4 | 7,733 |
| Professional, scientific, and technical services | 674,660 | 15.4 | 37.0 | 12,002 |
| Construction | 546,160 | 16.6 | 44.5 | 13,468 |
| Health care and social assistance | 325,200 | 30.2 | 271.0 | 28,027 |
| Accommodation and food services | 302,250 | 25.9 | 261.9 | 13,865 |
| Administrative/support and waste management | 407,790 | 12.3 | -32.0 | 4,164 |
| Information | 101,720 | 14.8 | -8.6 | -1,310 |
| Agriculture, forestry, fishing, and hunting | 78,480 | 2.6 | -7.4 | -223 |

Across all 19 sectors, the 2023 file contains 5,356,780 applications. Retail
has the largest application count in the profile, but its net job creation per
100 applications is far below health care/social assistance and
accommodation/food services. Administrative/support shows the sharpest
counterexample: positive establishment entry minus exit alongside negative net
job creation. Information and agriculture also have negative net job creation
despite recorded applications.

## What this adds to the societal trend map

1. **Entrepreneurial attention is not one outcome.** Application volume can
   indicate interest, necessity, or an early pipeline without becoming durable
   employment or service capacity.
2. **Sector meaning is socially uneven.** A health-care or food-services flow
   can matter to everyday access and social reproduction differently from a
   retail application surge, even when the latter is larger.
3. **Entry can coexist with contraction.** Establishment openings and net job
   creation are separate outcomes; the administrative/support example keeps
   turnover and job loss visible.
4. **The firm-power question is distributional.** The next step is not to rank
   sectors as “good” or “bad,” but to ask who receives jobs, services, income,
   ownership, and bargaining room, and who carries closure, churn, or risk.

## Arrow status

| Arrow | Status | Safe conclusion | Missing evidence |
|---|---|---|---|
| Applications → realized establishments | Compared | Application and opening intensity differ by sector | Firm-level matching, timing, survival, and ownership |
| Openings/closings → jobs | Observed in BDS | Entry can coexist with positive, flat, or negative net jobs | Job quality, wages, worker control, and duration |
| Sector flows → local service capacity | Open | Sector activity identifies candidate service and labor systems | Place-level access, prices, quality, and resident use |
| Sector dynamics → cultural/political meaning | Open | Sector change can reorganize work and everyday provision | Ownership, attribution, trust, identity, collective action, and policy response |

## Boundaries and counterexamples

- An application is not a firm, an opening is not a surviving firm, and a job
  is not a good job or a bargaining-power measure.
- BFS and BDS use different statistical constructions and periods; the ratios
  must not be called application-to-opening conversion rates.
- National sectors hide local variation, firm size, ownership, informal work,
  and whether a service reached residents.
- The measured counterexamples are essential: retail has high applications but
  modest net-job intensity; administrative/support has positive establishment
  entry minus exit but negative net jobs; and some sectors with fewer
  applications have much larger net job creation.

## Reproduction

```text
python3 scripts/analyze_bfs_bds_sector_divergence.py \
  --bfs /path/to/naics2.csv \
  --bds /path/to/bds2023_sec.csv \
  --year 2023 \
  --output /tmp/bfs-bds-sector-divergence.json
```

The reusable analysis is [analyze_bfs_bds_sector_divergence.py](../../../scripts/analyze_bfs_bds_sector_divergence.py).
Sources: [Census BFS](https://www.census.gov/econ/bfs/data.html) and [Census
BDS](https://www.census.gov/programs-surveys/bds.html).

Related: [BFS–BDS complete sector profile](bfs-bds-complete-sector-profile-v1.md),
[firm and market power distribution layer](firm-market-power-distribution-layer-v1.md),
and the [broad evidence matrix](../../US-BROAD-EVIDENCE-MATRIX_V1.md).

The eight selected sector observations are preserved in the machine-readable
[trend record](../../records/us-bfs-bds-sector-dynamics-2023.json) for
cross-source comparison. It retains application denominators and explicitly
labels the ratios as comparisons rather than conversion rates.
