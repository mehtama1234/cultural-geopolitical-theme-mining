# MEPS 2024 prescription and person-context reproduction audit

**Checked:** 2026-09-16  
**Status:** acquisition, identity, and event-layer reproduction passed

## Verified current artifacts

The 2024 HC-254A prescribed-medicine event file and HC-256 full-year person
file are present in the temporary working directory and reproduce the current
prescription-payment layer. HC-256’s structural audit also passes against the
released BRR person-ID file.

| Check | Result | Status |
|---|---:|---|
| HC-256 rows / columns | 19,140 / 1,615 | passed |
| HC-256 positive `PERWT24F` rows | 18,683 | passed |
| HC-256 required fields | all present and nonmissing | passed |
| HC-256 person IDs found in BRR file | 19,140 / 19,140 | passed |
| HC-254A event rows | 204,550 | passed |
| HC-254A positive-weight events | 202,902 | passed |
| HC-254A person-context links | 0 missing | passed |
| Estimated prescribed purchases | 3,029.45 million | reproduced |
| Mean total payment per purchase | $233.25 | reproduced |
| Mean self/family payment per purchase | $16.95 | reproduced |

Among under-65 observed purchases, the reproduced mean self/family payment is
$21.83 for private coverage, $4.12 for public-only coverage, and $55.06 for
uninsured purchases. These are event-level payment estimates among recorded
prescription purchases, not affordability or adherence estimates.

## Reproduction commands

```text
python3 scripts/audit_meps_hc256_structure.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  --brr-file /tmp/cgtm-meps-2024/h36brr/h36brr24.dta

python3 scripts/analyze_meps_hc254a_rx_event_layer.py \
  /tmp/cgtm-meps-2024/events/h254a.dta \
  /tmp/cgtm-meps-2024/h256/h256.dta
```

## Input hashes

```text
HC-256 archive       653891861ec18574b07f576915e6f9e423263fc947610dc34e1bd176feff7b40
HC-256 extracted     b4bde859b39f626345561c05570292bb7264dd92eb76ce0c1a14d6b89076aed5
HC-254A archive      8afe0228acf154e08d0c84c425494ce7511be85c1ea0e414b59ec6106717d818
HC-254A extracted    f3c99c0f5908d3988c6267bf5af1ab49a205e55adf000eae7899d41ba49d17a5
```

## Interpretation boundary

The successful key join proves that an observed prescription purchase can be
connected to annual person-level coverage, resources, health, and work fields.
It does not prove that the person needed a medicine but did not purchase it,
that the payment was made at the event, that the medicine was taken, or that a
purchase followed a particular clinical decision. Valid medication start
month/year fields cover only a restricted subset of the prescription events
and are not a complete purchase-date clock.

The next health-cost test must preserve the purchase-event universe separately
from the person-level reported affordability-delay universe, then seek a
same-person follow-up with non-purchase/forgone-fill, adherence, health,
work/time, debt, or recovery evidence. No trust, political-action, remedy, or
geopolitical conclusion follows from this audit.

## Official sources

- [AHRQ MEPS HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes)
- [AHRQ MEPS HC-254A prescribed-medicine file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254A&prfricon=yes)
- [MEPS prescription episode boundary](meps-2024-prescription-episode-boundary-v1.md)
