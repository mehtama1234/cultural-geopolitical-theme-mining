# Finding 015: AI can make customer service faster without fixing the customer's problem

**Status:** bounded AI-assisted customer-service and recourse finding · **Checked:** 2026-09-22

## The bounded finding

In a randomized field experiment at a meal-delivery company, AI suggestions
helped customer-service agents respond faster and improved measured customer
sentiment. The study covered 138 agents and 256,934 chats from December 2020
through November 2021. The reported gains were larger for less-experienced
agents.

But the result depended on what the customer needed. AI helped more with
subscription-cancellation requests. It was least effective for repeat
complaints because the underlying delivery or operational problem was beyond a
better message. Customers who had first experienced a chatbot-comprehension
failure could also react worse when transferred to a human using AI, apparently
because the rapid reply still felt automated.

```text
customer problem
  -> chatbot or human support route
  -> AI-assisted response
  -> faster interaction and better measured sentiment [in some cases]
  -> actual correction, refund, replacement, continued service, or exit
     [not observed here]
```

## Why it matters

This adds a practical distinction to the digital and consumer lanes: better
communication is not the same as better recourse. A firm can make the support
interaction feel smoother while leaving the delivery failure, billing issue,
or repeat complaint intact.

It also shows that the meaning of “human support” depends on the route before
it. A customer who has already struggled with a bot may interpret a very fast
AI-assisted human reply as another automated barrier rather than as help.

## Limits and counterexamples

- The experiment covers one meal-delivery company and one AI-assistance tool.
- The customer-sentiment measure is automated text analysis, not a complete
  measure of satisfaction, fairness, or remedy adequacy.
- Faster response and higher sentiment do not establish a corrected order,
  refund, replacement, retention, or successful exit.
- Repeat complaints may remain negative because the firm has not fixed the
  underlying operational problem, not because AI assistance is always harmful.
- The public article does not provide every subgroup denominator or a long-run
  customer panel.

## Next test

Follow the same customer case from chatbot contact through human handoff,
correction, refund or replacement, repeat contact, trust, switching, and exit.
Compare AI-assisted and non-assisted routes while recording whether the firm
actually fixed the underlying problem.

## Sources

[Management Science: Engaging Customers with AI in Online Chats](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2022.03920?af=R)

[Harvard Business School summary](https://www.library.hbs.edu/working-knowledge/when-ai-chatbots-help-people-be-more-human)

[Machine-readable trend record](../../../records/us-hbs-ai-customer-service-contextual-recourse-2020-2021.json)

**Evidence status:** randomized field evidence supports contextual speed and
measured-sentiment effects; actual correction, recovery, durable trust, and
practical exit remain open.
