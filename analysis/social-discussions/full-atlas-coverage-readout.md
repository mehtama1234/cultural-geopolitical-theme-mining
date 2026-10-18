# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **124**
- Exact linked social items: **129**
- Record statuses: `{'augmented': 124, 'documented_access_gap': 476, 'queued': 1378}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 86 |
| `linkedin:documented_access_gap` | 514 |
| `linkedin:not_started` | 1,378 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 560 |
| `reddit:not_started` | 1,378 |
| `x:documented_access_gap` | 600 |
| `x:not_started` | 1,378 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 599 |
| `youtube:not_started` | 1,378 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
