# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **340**
- Exact linked social items: **348**
- Record statuses: `{'augmented': 333, 'documented_access_gap': 1663, 'in_review': 7, 'queued': 11}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 302 |
| `linkedin:documented_access_gap` | 1,702 |
| `linkedin:not_started` | 10 |
| `reddit:augmented` | 41 |
| `reddit:documented_access_gap` | 1,955 |
| `reddit:not_started` | 18 |
| `x:documented_access_gap` | 1,998 |
| `x:not_started` | 16 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,995 |
| `youtube:not_started` | 18 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
