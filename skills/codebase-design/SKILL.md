---
name: codebase-design
description: Resolve ownership and interface decisions when changing shared behavior, persistent state, or module boundaries. Use for architecture questions or competing implementations; skip routine edits inside an established pattern.
---

# Codebase design

Find the smallest change that keeps business rules and state under clear ownership. Use the repository's language and architecture. An architecture question is read-only unless implementation is also requested.

## Find the existing owner

Trace the affected request or event through callers, authoritative state, side effects, and consumers. Read the nearest current contract and equivalent call sites. For work across repositories, inspect both sides at the relevant branch or revision; the current directory alone may not contain the governing implementation.

Identify which module owns each changed rule, write, and recovery decision. Distinguish canonical data from caches, projections, and UI state. Separate a technical requirement, such as durable idempotency, from the choice of database that implements it.

Extend the established owner when it satisfies the requirement. If ownership or an accepted contract is unclear, show the concrete alternatives and settle only that decision before dependent work. Keep existing authority and compatibility requirements intact.

## Choose a useful boundary

Prefer a small interface that hides meaningful complexity. Its contract includes inputs, outputs, authorization, errors, ordering, and side effects, not just type signatures.

- Keep behavior that changes together cohesive. Extract when reuse, independent testing, or a distinct responsibility justifies it, rather than to meet a line limit.
- Reuse shared behavior when its invariants and lifecycle agree. Similar syntax alone does not justify coupling unrelated workflows.
- Prefer deterministic calculations and explicit effect boundaries where they clarify the behavior. Accept external dependencies when this improves isolation; avoid interfaces created solely for hypothetical future implementations.
- Keep one authoritative owner of mutable state. For asynchronous changes, identify what happens on stale completion, retry, cancellation, and partial failure. Use the cases relevant to the changed workflow.
- Validate untrusted data at the boundary that receives it. Preserve useful types internally instead of repeatedly converting or weakening the same contract.

Compare a proposed abstraction with extending the existing implementation. If removing the abstraction removes complexity without spreading it into callers, it is probably unnecessary. Preserve intentional legacy/new separation when compatibility requires independent evolution.

## Prove and communicate the decision

Choose evidence at the public behavior or dependency boundary that could disprove the design. Exercise the relevant failure transition, not only the happy path. Keep expected results independent from the implementation being tested.

For a small change, give a brief rationale. For a consequential decision, state the owner, affected callers, preserved invariants, rejected alternative, and required evidence. Reuse an accepted plan rather than producing a second one.

Record a durable decision only when it is costly to reverse, surprising without context, and the result of a real tradeoff. Use the repository's existing documentation authority. Do not create another glossary, architecture tree, or framework merely because this skill was loaded.

This skill does not authorize additional repositories, migrations, external writes, or refactors outside the requested outcome.
