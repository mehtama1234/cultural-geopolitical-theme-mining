# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **23**
- Exact linked social items: **26**
- Record statuses: `{'augmented': 23, 'documented_access_gap': 6, 'in_review': 21, 'queued': 1928}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 2 |
| `linkedin:documented_access_gap` | 27 |
| `linkedin:not_started` | 1,949 |
| `reddit:augmented` | 22 |
| `reddit:documented_access_gap` | 7 |
| `reddit:not_started` | 1,949 |
| `x:documented_access_gap` | 29 |
| `x:not_started` | 1,949 |
| `youtube:documented_access_gap` | 29 |
| `youtube:not_started` | 1,949 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
