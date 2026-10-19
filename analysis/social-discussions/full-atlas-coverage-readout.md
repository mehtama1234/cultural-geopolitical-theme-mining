# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **339**
- Exact linked social items: **347**
- Record statuses: `{'augmented': 332, 'documented_access_gap': 1663, 'in_review': 8, 'queued': 11}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 301 |
| `linkedin:documented_access_gap` | 1,703 |
| `linkedin:not_started` | 10 |
| `reddit:augmented` | 41 |
| `reddit:documented_access_gap` | 1,954 |
| `reddit:not_started` | 19 |
| `x:documented_access_gap` | 1,997 |
| `x:not_started` | 17 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,994 |
| `youtube:not_started` | 19 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
