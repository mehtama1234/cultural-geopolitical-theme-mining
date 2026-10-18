# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **195**
- Exact linked social items: **200**
- Record statuses: `{'augmented': 195, 'documented_access_gap': 755, 'queued': 1028}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 157 |
| `linkedin:documented_access_gap` | 793 |
| `linkedin:not_started` | 1,028 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 910 |
| `reddit:not_started` | 1,028 |
| `x:documented_access_gap` | 950 |
| `x:not_started` | 1,028 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 949 |
| `youtube:not_started` | 1,028 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
