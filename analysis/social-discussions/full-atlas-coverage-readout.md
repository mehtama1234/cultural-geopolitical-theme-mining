# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **69**
- Exact linked social items: **74**
- Record statuses: `{'augmented': 69, 'documented_access_gap': 181, 'queued': 1728}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 31 |
| `linkedin:documented_access_gap` | 219 |
| `linkedin:not_started` | 1,728 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 210 |
| `reddit:not_started` | 1,728 |
| `x:documented_access_gap` | 250 |
| `x:not_started` | 1,728 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 249 |
| `youtube:not_started` | 1,728 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
