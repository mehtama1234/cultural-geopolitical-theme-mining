# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **265**
- Exact linked social items: **270**
- Record statuses: `{'augmented': 265, 'documented_access_gap': 1210, 'queued': 503}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 227 |
| `linkedin:documented_access_gap` | 1,248 |
| `linkedin:not_started` | 503 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,435 |
| `reddit:not_started` | 503 |
| `x:documented_access_gap` | 1,475 |
| `x:not_started` | 503 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,474 |
| `youtube:not_started` | 503 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
