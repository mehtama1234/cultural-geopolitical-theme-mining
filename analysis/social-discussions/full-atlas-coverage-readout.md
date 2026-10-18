# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **21**
- Exact linked social items: **24**
- Record statuses: `{'augmented': 21, 'documented_access_gap': 6, 'in_review': 23, 'queued': 1928}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 2 |
| `linkedin:documented_access_gap` | 25 |
| `linkedin:not_started` | 1,951 |
| `reddit:augmented` | 20 |
| `reddit:documented_access_gap` | 7 |
| `reddit:not_started` | 1,951 |
| `x:documented_access_gap` | 27 |
| `x:not_started` | 1,951 |
| `youtube:documented_access_gap` | 27 |
| `youtube:not_started` | 1,951 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
