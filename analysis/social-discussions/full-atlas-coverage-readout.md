# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **227**
- Exact linked social items: **232**
- Record statuses: `{'augmented': 227, 'documented_access_gap': 898, 'queued': 853}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 189 |
| `linkedin:documented_access_gap` | 936 |
| `linkedin:not_started` | 853 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,085 |
| `reddit:not_started` | 853 |
| `x:documented_access_gap` | 1,125 |
| `x:not_started` | 853 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,124 |
| `youtube:not_started` | 853 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
