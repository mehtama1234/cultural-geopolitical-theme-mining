# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **224**
- Exact linked social items: **229**
- Record statuses: `{'augmented': 224, 'documented_access_gap': 876, 'queued': 878}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 186 |
| `linkedin:documented_access_gap` | 914 |
| `linkedin:not_started` | 878 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,060 |
| `reddit:not_started` | 878 |
| `x:documented_access_gap` | 1,100 |
| `x:not_started` | 878 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,099 |
| `youtube:not_started` | 878 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
