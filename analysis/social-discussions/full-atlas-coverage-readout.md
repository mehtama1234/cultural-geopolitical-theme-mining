# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **306**
- Exact linked social items: **311**
- Record statuses: `{'augmented': 306, 'documented_access_gap': 1594, 'queued': 78}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 268 |
| `linkedin:documented_access_gap` | 1,632 |
| `linkedin:not_started` | 78 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,860 |
| `reddit:not_started` | 78 |
| `x:documented_access_gap` | 1,900 |
| `x:not_started` | 78 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,899 |
| `youtube:not_started` | 78 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
