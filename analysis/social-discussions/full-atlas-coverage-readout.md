# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **110**
- Exact linked social items: **115**
- Record statuses: `{'augmented': 110, 'documented_access_gap': 415, 'queued': 1453}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 72 |
| `linkedin:documented_access_gap` | 453 |
| `linkedin:not_started` | 1,453 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 485 |
| `reddit:not_started` | 1,453 |
| `x:documented_access_gap` | 525 |
| `x:not_started` | 1,453 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 524 |
| `youtube:not_started` | 1,453 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
