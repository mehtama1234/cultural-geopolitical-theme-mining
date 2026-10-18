# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **313**
- Exact linked social items: **318**
- Record statuses: `{'augmented': 313, 'documented_access_gap': 1637, 'queued': 28}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 275 |
| `linkedin:documented_access_gap` | 1,675 |
| `linkedin:not_started` | 28 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,910 |
| `reddit:not_started` | 28 |
| `x:documented_access_gap` | 1,950 |
| `x:not_started` | 28 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,949 |
| `youtube:not_started` | 28 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
