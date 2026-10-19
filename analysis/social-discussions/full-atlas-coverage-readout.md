# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **342**
- Exact linked social items: **350**
- Record statuses: `{'augmented': 338, 'documented_access_gap': 1668, 'in_review': 8}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 304 |
| `linkedin:documented_access_gap` | 1,704 |
| `linkedin:not_started` | 6 |
| `reddit:augmented` | 41 |
| `reddit:documented_access_gap` | 1,965 |
| `reddit:not_started` | 8 |
| `x:documented_access_gap` | 2,006 |
| `x:not_started` | 8 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 2,005 |
| `youtube:not_started` | 8 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
