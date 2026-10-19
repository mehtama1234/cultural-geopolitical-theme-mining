# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **342**
- Exact linked social items: **354**
- Record statuses: `{'augmented': 340, 'documented_access_gap': 1670, 'in_review': 4}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 304 |
| `linkedin:documented_access_gap` | 1,706 |
| `linkedin:not_started` | 4 |
| `reddit:augmented` | 43 |
| `reddit:documented_access_gap` | 1,967 |
| `reddit:not_started` | 4 |
| `x:documented_access_gap` | 2,010 |
| `x:not_started` | 4 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,007 |
| `youtube:not_started` | 4 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
