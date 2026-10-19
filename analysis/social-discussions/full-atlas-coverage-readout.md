# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **346**
- Exact linked social items: **361**
- Record statuses: `{'augmented': 344, 'documented_access_gap': 1663, 'in_review': 7}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 307 |
| `linkedin:documented_access_gap` | 1,700 |
| `linkedin:not_started` | 7 |
| `reddit:augmented` | 45 |
| `reddit:documented_access_gap` | 1,962 |
| `reddit:not_started` | 7 |
| `x:documented_access_gap` | 2,007 |
| `x:not_started` | 7 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,004 |
| `youtube:not_started` | 7 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
