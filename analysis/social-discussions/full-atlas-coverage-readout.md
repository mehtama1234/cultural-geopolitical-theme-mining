# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **269**
- Exact linked social items: **274**
- Record statuses: `{'augmented': 269, 'documented_access_gap': 1256, 'queued': 453}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 231 |
| `linkedin:documented_access_gap` | 1,294 |
| `linkedin:not_started` | 453 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,485 |
| `reddit:not_started` | 453 |
| `x:documented_access_gap` | 1,525 |
| `x:not_started` | 453 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,524 |
| `youtube:not_started` | 453 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
