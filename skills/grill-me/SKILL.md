---
name: grill-me
description: Run a relentless interview to sharpen a plan, decision, or design. Invoke explicitly when unresolved choices need to be exposed before action.
---

# Grill me

Interview the developer until both sides reach a shared understanding. Map the subject as a design tree. Every decision branches into the decisions that depend on it.

Work through the tree in rounds. The frontier is every decision whose prerequisites are settled, so it can be answered now without guessing about an earlier choice.

Ask the whole current frontier in one round. Number every question and give your recommended answer. Then wait for the developer before computing the next frontier.

Format each question like this:

```markdown
Q1. <Question title>

<Question body and concrete choices>

Recommended: <your answer and why>
```

Each answer reshapes the tree. Settled decisions expose the next questions. A question that depends on an answer still open in the current round belongs in a later round.

Finding facts is the agent's job. Inspect the codebase, tools, documentation, or other available evidence instead of asking the developer for facts that can be discovered. Do not block unrelated frontier questions while research is running.

Product choices, preferences, and consequential tradeoffs belong to the developer. Ask those directly and make the recommendation concrete enough to accept or challenge.

The session ends when the frontier is empty and no material assumption remains hidden. Summarize the resolved plan, decisions, constraints, and open risks. Do not act on the result until the developer confirms shared understanding.
