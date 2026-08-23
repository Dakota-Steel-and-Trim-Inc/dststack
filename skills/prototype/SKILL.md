---
name: prototype
description: Build a disposable prototype to answer one design question. Use when reading and discussion cannot settle whether logic, state, or a UI direction works. Do not use it as a shortcut to production implementation.
---

# Prototype

A prototype is throwaway code that answers one named question. The question determines its shape.

## Choose the prototype

- For logic, state transitions, or data shape, read [references/logic.md](references/logic.md).
- For visual structure or interaction direction, read [references/ui.md](references/ui.md).

If the question is ambiguous, inspect the surrounding code. Ask the developer only when choosing the wrong form would waste meaningful work.

## Keep it disposable

- Put it in an isolated, task-created location near the relevant code and name it clearly as a prototype.
- Make it trivial to run. Prefer one command or one self-contained file.
- Keep state in memory unless persistence is the question being tested. Never use production data.
- Build only enough behavior and polish to answer the question. Do not add production abstractions, hardening, or a full test suite.
- Expose the relevant state or variant so the developer can see what changed.

## Return the evidence

Report the question, how to run the prototype, the observed result, the resulting recommendation, and what remains uncertain. Return that evidence to `openspec-explore` or the governing planning flow. Do not edit OpenSpec artifacts through this skill.

A prototype is not production implementation. Reusing a validated idea or isolated logic requires the normal implementation and verification workflow.

Do not commit, push, open or update an issue, merge, or delete prototype files without explicit authority. Never land throwaway prototype code on the target branch.
