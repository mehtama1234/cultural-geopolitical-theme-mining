# Reading guide browser check

Checked with Chromium on 2026-09-11 at 1440 × 1000 and 390 × 844.

- The current page contains eleven topics; the prior opening-state browser check covered the ten topics present at that time.
- The household-cost filter shows three topics.
- A connection from housing to local business reveals its destination even when the destination was filtered out.
- An unmatched search produces zero results and a recovery message; clearing it restores the topics.
- The phone layout has no horizontal overflow.
- No page JavaScript errors occurred during these checks.
- Desktop and phone screenshots were visually inspected for the opening reading layout. The page uses large text, a constrained reading width, and a single column on phones.

This checks the tested interactions and opening layout. It is not a complete accessibility audit or a verification of the research claims. Keyboard and screen-reader testing, full-page visual review, and evidence review remain separate work.

## Reading-path checks

On 2026-09-11, Chromium verified six reading paths containing eighteen topic links. The current page has seven paths and twenty-one topic links; the new path has been checked for valid local links by the static link check, but not yet through a fresh browser interaction. With the cost filter selected, a path link to politics revealed and focused the destination. The page had no horizontal overflow at 390 × 844 or 1440 × 1000, and no JavaScript errors occurred. These additional checks were automated; they do not constitute a new full-page visual or accessibility review.

## UX audit note

The opening desktop and phone states were captured and visually inspected on 2026-09-11. Moving the topic search and theme filter directly below the bigger-picture panel makes the main task visible before the optional reading paths. The opening hierarchy, dark summary panel, two-column desktop cards and single-column phone reflow were clear in the captured states. The long page still needs a full-page reading and accessibility review; this note does not claim WCAG compliance.

The controls are now sticky while a reader scrolls. Chromium checked this at 1440 × 1000 and 390 × 844, including an anchored jump to the work topic and horizontal-overflow checks. The topic remained visible below the control area.
