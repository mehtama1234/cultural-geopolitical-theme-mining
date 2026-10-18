# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **300**
- Exact linked social items: **305**
- Record statuses: `{'augmented': 300, 'documented_access_gap': 1525, 'queued': 153}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 262 |
| `linkedin:documented_access_gap` | 1,563 |
| `linkedin:not_started` | 153 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,785 |
| `reddit:not_started` | 153 |
| `x:documented_access_gap` | 1,825 |
| `x:not_started` | 153 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,824 |
| `youtube:not_started` | 153 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
