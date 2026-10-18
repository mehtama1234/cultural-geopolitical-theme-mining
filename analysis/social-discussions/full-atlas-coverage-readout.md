# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **275**
- Exact linked social items: **280**
- Record statuses: `{'augmented': 275, 'documented_access_gap': 1350, 'queued': 353}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 237 |
| `linkedin:documented_access_gap` | 1,388 |
| `linkedin:not_started` | 353 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,585 |
| `reddit:not_started` | 353 |
| `x:documented_access_gap` | 1,625 |
| `x:not_started` | 353 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,624 |
| `youtube:not_started` | 353 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
