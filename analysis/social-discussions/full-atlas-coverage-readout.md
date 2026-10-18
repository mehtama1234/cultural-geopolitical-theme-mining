# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **189**
- Exact linked social items: **194**
- Record statuses: `{'augmented': 189, 'documented_access_gap': 736, 'queued': 1053}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 151 |
| `linkedin:documented_access_gap` | 774 |
| `linkedin:not_started` | 1,053 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 885 |
| `reddit:not_started` | 1,053 |
| `x:documented_access_gap` | 925 |
| `x:not_started` | 1,053 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 924 |
| `youtube:not_started` | 1,053 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
