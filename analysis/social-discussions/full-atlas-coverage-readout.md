# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **322**
- Exact linked social items: **327**
- Record statuses: `{'augmented': 320, 'documented_access_gap': 1658}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 284 |
| `linkedin:documented_access_gap` | 1,694 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,938 |
| `x:documented_access_gap` | 1,978 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,977 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
