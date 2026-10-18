# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **319**
- Exact linked social items: **324**
- Record statuses: `{'augmented': 317, 'documented_access_gap': 1658, 'queued': 3}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 281 |
| `linkedin:documented_access_gap` | 1,694 |
| `linkedin:not_started` | 3 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,935 |
| `reddit:not_started` | 3 |
| `x:documented_access_gap` | 1,975 |
| `x:not_started` | 3 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,974 |
| `youtube:not_started` | 3 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
