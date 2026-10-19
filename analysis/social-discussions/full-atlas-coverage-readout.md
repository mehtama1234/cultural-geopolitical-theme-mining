# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **343**
- Exact linked social items: **355**
- Record statuses: `{'augmented': 341, 'documented_access_gap': 1671, 'in_review': 2}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 304 |
| `linkedin:documented_access_gap` | 1,708 |
| `linkedin:not_started` | 2 |
| `reddit:augmented` | 44 |
| `reddit:documented_access_gap` | 1,968 |
| `reddit:not_started` | 2 |
| `x:documented_access_gap` | 2,012 |
| `x:not_started` | 2 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,009 |
| `youtube:not_started` | 2 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
