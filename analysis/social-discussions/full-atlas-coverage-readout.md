# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **104**
- Exact linked social items: **109**
- Record statuses: `{'augmented': 104, 'documented_access_gap': 371, 'queued': 1503}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 66 |
| `linkedin:documented_access_gap` | 409 |
| `linkedin:not_started` | 1,503 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 435 |
| `reddit:not_started` | 1,503 |
| `x:documented_access_gap` | 475 |
| `x:not_started` | 1,503 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 474 |
| `youtube:not_started` | 1,503 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
