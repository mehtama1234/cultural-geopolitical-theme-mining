# Acquisition log — first bounded wave

**Window:** 2025-10-17 through 2026-10-17  
**Retrieved:** 2026-10-17  
**Method:** public web search with platform-restricted queries; no login,
private-group access, automated account scraping, or claim that search results
are exhaustive.

| Platform | Query family | Result | Boundary |
|---|---|---|---|
| YouTube | `AI jobs future of work 2026` | Two public videos found and normalized in `records/ai-work-control-001.json` and `002.json`. | Search ranking and indexed metadata are not platform-wide exposure. |
| Reddit | `AI jobs workers productivity workplace research 2026` | Public discussion threads found, including career anxiety, job-search experience, and disagreement over displacement. | Search results overrepresent indexed/public threads; removed posts and private communities are invisible. |
| LinkedIn | `AI jobs workers productivity research 2026` | Public posts from research organizations and professionals found, including PwC, ILO, Stanford Digital Economy Lab, HBS AI Institute, and METR. | Public post visibility and author selection are not representative of LinkedIn members. |
| X | `AI jobs future of work 2026 study` | The initial direct-post pass was empty; a later X trending summary was captured as a clearly labeled platform-summary record. | Do not treat the summary as a direct post corpus or representative public opinion. |
| YouTube | `AI companion emotional support 2026` | A public explainer was found; the initial record is retained as a discovery lead pending exact-date/transcript review. | Search metadata and a video description are not a sampled audience or clinical evidence. |
| YouTube | `AI companion emotional support 2026` | A 2026 public video was normalized in `records/ai-companionship-youtube-001.json`. | Search metadata and a video description are not a sampled audience or clinical evidence. |
| YouTube | `quitting social media digital detox 2026` | A 2026 creator experiment was normalized in `records/platform-exit-youtube-001.json`. | Creator self-report and engagement are not causal or population evidence. |
| Reddit | `AI companion emotional support 2026` | Public discussions found on emotional support, continuity, privacy, and relationships; normalized in `records/ai-companionship-003.json` and `004.json`. | Community selection, moderation, and self-report limits apply. |
| LinkedIn | `AI companion emotional support trust 2026 research` | Public research relays and institutional posts found; normalized in `records/ai-companionship-001.json` and `002.json`. | Professional audience and research-relay bias apply. |
| X | `site:x.com/status AI companion emotional support 2026` | Two public X pages found, including a law-firm post and an X trending summary; normalized in `records/ai-companionship-005.json` and `006.json`. | One is organizational speech and the other is an X-generated summary, not a representative discussion sample. |
| X | `site:x.com/status quit social media 2026` | A direct X status and indexed reply mirror were found and normalized in `records/platform-exit-x-001.json`. | Direct X replies may require login; mirror coverage is not a reproducible platform-wide sample. |
| X | `AI layoffs workers 2026` | An X trending summary was normalized in `records/ai-work-control-x-001.json`; it preserves competing efficiency, worker, and demand frames. | This is a platform summary, not a direct post corpus or representative public opinion. |

## Next acquisition pass

Repeat the same protocol for platform attention/exit and AI companionship/trust,
then run a dedicated X pass through directly accessible public URLs or an
authorized API if available. Store the query, date, and failure mode even when
no usable item is found.
