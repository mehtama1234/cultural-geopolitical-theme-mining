# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **256**
- Exact linked social items: **261**
- Record statuses: `{'augmented': 256, 'documented_access_gap': 1119, 'queued': 603}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 218 |
| `linkedin:documented_access_gap` | 1,157 |
| `linkedin:not_started` | 603 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,335 |
| `reddit:not_started` | 603 |
| `x:documented_access_gap` | 1,375 |
| `x:not_started` | 603 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,374 |
| `youtube:not_started` | 603 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
