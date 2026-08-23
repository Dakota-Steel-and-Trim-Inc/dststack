---
name: research
description: Investigate a software question against high-trust primary sources before planning or implementation. Use when an unknown technical, legal, API, or product fact could change an OpenSpec exploration, plan, or decision. Skip preferences and facts already available in the repository.
---

# Research

Resolve the fact that blocks a sound decision. Do not turn research into a second planning process.

When the question needs meaningful reading and delegation is available, give it to a background agent so the main flow can continue. Handle a small lookup directly.

## Investigate

State the question and the decision it informs. Use primary sources such as official documentation, source code, specifications, research papers, and first-party APIs. Follow each material claim to the source that owns it.

Inspect the repository when local behavior matters. Do not ask the developer for a fact that code, tools, or documentation can establish.

If an active OpenSpec change is relevant, read its existing artifacts for context. Do not edit those artifacts. Return evidence to `openspec-explore` or the governing planning flow, which owns the resulting decision.

## Report

Reply in chat by default:

```markdown
Question: <what was investigated>
Finding: <verified answer or unresolved conflict>
Evidence: <primary sources supporting each material claim>
Implication: <how this changes the current decision>
Decision still open: <developer choice, or none>
OpenSpec target: <proposal | design | spec | tasks | none>
```

Separate verified facts, inferences, and recommendations. Say what remains unknown when primary sources conflict or do not settle the question.

Write a Markdown note only when the developer asks or the accepted plan explicitly includes that artifact. Repository convention determines its location, not whether the write is authorized. Do not create an OpenSpec artifact through this skill.

Research does not authorize repository edits, implementation, or external writes.
