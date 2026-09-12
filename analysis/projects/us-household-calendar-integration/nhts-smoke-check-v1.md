# NHTS smoke check v1

**Run date:** 2026-09-12  
**Source:** [2022 NHTS CSV V2.1 archive](https://nhts.ornl.gov/downloads)  
**Documentation:** [2022 NHTS user guide](https://nhts.ornl.gov/assets/2022/doc/2022%20NextGen%20NHTS%20%20User%27s%20Guide%20V1_PubUse.pdf)

## What was verified

The extractor read the four linked CSV members and selected the transportation fields without expanding or modifying the archive. The bounded run read 1,000 rows from each member:

| File | Rows | Distinct households |
|---|---:|---:|
| Household | 1,000 | 1,000 |
| Person | 1,000 | 478 |
| Trip | 1,000 | 215 |
| Vehicle | 1,000 | 502 |

This shape is expected from the hierarchy: one household can have several people, vehicles, and trips. The shared `HOUSEID` is therefore necessary for a valid join.

The smoke rows contained both urban/rural codes and multiple vehicle, worker, trip-purpose, mode, travel-time, and travel-mile values. The person file also contained recent-rideshare fields and travel-limitation fields.

## What the missingness check showed

Rideshare and travel-limitation fields were often marked with special survey codes in the bounded rows, rather than ordinary yes/no values. Those codes must be decoded from the official codebook and kept separate from blank or not-applicable values. The same rule applies to trip and vehicle fields.

The extractor records raw category values but does not guess their meaning. That is deliberate: a number such as `01`, `02`, or `-1` is not a finding until the codebook definition and universe are attached.

## What this does not prove

The first 1,000 rows of each file are an engineering smoke sample, not a weighted estimate and not a random sample. They do not show the national share of rideshare use, transit access, or car ownership. Population estimates require the survey weights, replicate weights, codebook, and appropriate variance calculation.

NHTS also captures a travel day or recent travel questions, not a twelve-month household cost history. It cannot by itself show the fare paid, the paycheck or bill date, a missed shift, a failed ride, or recovery in the following month.

## Reproduction

```bash
python3 scripts/extract_nhts_transport_slice.py \
  --archive /path/to/csv.zip \
  --output /tmp/nhts-smoke/slice \
  --report /tmp/nhts-smoke/report.json \
  --max-rows 1000
```

The derived CSVs were removed after inspection. No raw NHTS data or derived row file is committed.

