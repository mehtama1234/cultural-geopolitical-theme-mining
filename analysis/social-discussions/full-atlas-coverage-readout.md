# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **351**
- Exact linked social items: **368**
- Record statuses: `{'augmented': 349, 'documented_access_gap': 1664, 'in_review': 1}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 312 |
| `linkedin:documented_access_gap` | 1,701 |
| `linkedin:not_started` | 1 |
| `reddit:augmented` | 46 |
| `reddit:documented_access_gap` | 1,967 |
| `reddit:not_started` | 1 |
| `x:documented_access_gap` | 2,013 |
| `x:not_started` | 1 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,010 |
| `youtube:not_started` | 1 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
