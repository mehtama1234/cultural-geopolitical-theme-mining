# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **306**
- Exact linked social items: **311**
- Record statuses: `{'augmented': 306, 'documented_access_gap': 1569, 'queued': 103}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 268 |
| `linkedin:documented_access_gap` | 1,607 |
| `linkedin:not_started` | 103 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,835 |
| `reddit:not_started` | 103 |
| `x:documented_access_gap` | 1,875 |
| `x:not_started` | 103 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,874 |
| `youtube:not_started` | 103 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
