# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **134**
- Exact linked social items: **139**
- Record statuses: `{'augmented': 134, 'documented_access_gap': 516, 'queued': 1328}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 96 |
| `linkedin:documented_access_gap` | 554 |
| `linkedin:not_started` | 1,328 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 610 |
| `reddit:not_started` | 1,328 |
| `x:documented_access_gap` | 650 |
| `x:not_started` | 1,328 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 649 |
| `youtube:not_started` | 1,328 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
