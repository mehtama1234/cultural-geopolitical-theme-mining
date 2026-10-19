# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **339**
- Exact linked social items: **345**
- Record statuses: `{'augmented': 330, 'documented_access_gap': 1658, 'in_review': 15, 'queued': 11}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 301 |
| `linkedin:documented_access_gap` | 1,702 |
| `linkedin:not_started` | 11 |
| `reddit:augmented` | 41 |
| `reddit:documented_access_gap` | 1,947 |
| `reddit:not_started` | 26 |
| `x:documented_access_gap` | 1,990 |
| `x:not_started` | 24 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,987 |
| `youtube:not_started` | 26 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
