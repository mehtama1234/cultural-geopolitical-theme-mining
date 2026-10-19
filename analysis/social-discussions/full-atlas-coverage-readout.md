# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **338**
- Exact linked social items: **343**
- Record statuses: `{'augmented': 320, 'documented_access_gap': 1658, 'in_review': 25, 'queued': 11}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 300 |
| `linkedin:documented_access_gap` | 1,694 |
| `linkedin:not_started` | 20 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,938 |
| `reddit:not_started` | 36 |
| `x:documented_access_gap` | 1,978 |
| `x:not_started` | 36 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,977 |
| `youtube:not_started` | 36 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
