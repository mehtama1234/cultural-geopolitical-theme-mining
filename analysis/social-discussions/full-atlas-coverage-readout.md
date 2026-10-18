# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **100**
- Exact linked social items: **105**
- Record statuses: `{'augmented': 100, 'documented_access_gap': 350, 'queued': 1528}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 62 |
| `linkedin:documented_access_gap` | 388 |
| `linkedin:not_started` | 1,528 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 410 |
| `reddit:not_started` | 1,528 |
| `x:documented_access_gap` | 450 |
| `x:not_started` | 1,528 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 449 |
| `youtube:not_started` | 1,528 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
