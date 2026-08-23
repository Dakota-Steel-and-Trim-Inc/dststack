---
name: orchestrate
description: Propose, approve, coordinate, review, and finish complex software delivery. Use when a change needs bounded agent ownership, a PR series, or continued execution after one approval. Skip small local changes that one agent can finish directly.
---

# Orchestrate

The main agent owns the proposal, approval gate, integration, and proof. Specialists own bounded work. Use the smallest team that earns its cost. Every run has a two-turn gate.

## Propose

This turn is read-only. Inspect the request or accepted plan, repository instructions, current state, active work, and acceptance criteria. Name the governing contract and surface conflicts instead of choosing silently. An approved OpenSpec change may be the contract. OpenSpec is optional and must never block orchestration when the request or another accepted plan is sufficient.

Classify the work:

- `Inline` when one agent can finish the task directly.
- `Bounded delivery` for one cohesive implementation and PR.
- `Autonomous PR series` for several PRs that fit within one continuous run.
- `Standing program` when delivery will span sessions, needs restart recovery, or has several coordinated tracks. Use `orchestrate-program` after approval.

Use `challenge` before proposing the roster when the work crosses repositories or production boundaries, combines at least three independent behavioral concerns, lacks clear invariants, or competes with too much active work. Use `plan-pr-delivery` for version-controlled implementation or an implementation plan.

When the contract is an approved OpenSpec change, use its requirements and tasks as the behavior boundary. Do not create a second product plan. Use `plan-pr-delivery` only to define delivery boundaries, workspace choices, review order, and landing.

Reply in this shape:

```markdown
## Orchestration proposal

Goal: <one sentence>
Done: <checkable completion condition>
Contract: <request, plan, specification, tickets, and acceptance criteria>
Mode: <Inline | Bounded delivery | Autonomous PR series | Standing program>
Delivery: <No PR | Single PR | PR series>
Workspace: <strategy, base, and reason>
Authority: <actions and exact targets covered by approval>
Continuation: <Run to completion | Checkpointed only when requested>
WIP: <maximum active implementation lanes and what must remain sequential>
Pilot: <first end-to-end slice, or why none is useful>
Intervention points: <decisions or actions outside the proposed authority>

| Agent | Owns | Done when |
|---|---|---|
| <role> | <bounded scope> | <checkable result> |

PR plan: <include the plan-pr-delivery table for a series>
Order: <parallel and sequential dependencies>
Checks: <integration and final verification>
Cleanup: <only temporary task-created state>
Lean option: <smaller roster when the tradeoff is real>

Reply `approve`, `lean`, or describe changes.
```

Recommend inline work when delegation adds no value. Default to no more than three active implementation lanes, and use fewer when scopes share files, schema, data, or product decisions.

Set continuation to `Run to completion` unless the developer asks for checkpoints. End the turn after the proposal. The initial request is not approval. Before approval, make no edits, dispatch no agents, create no ledger, and run no mutating commands.

## Run the approved plan

Approval accepts the proposed contract, roster, delivery plan, workspace, authority, WIP limit, and continuation mode. It authorizes every listed action for the full run after the orchestrator rechecks each exact target. Unlisted actions remain unauthorized.

`Run to completion` means continue across assignments, branches, PRs, reviews, fixes, checks, and authorized merges until the completion condition is true. Do not ask for approval between tasks or PRs. Progress updates do not pause the run.

Stop only for an action outside authority, an unresolved product choice, a material change to contract or risk, unsafe or user-owned state, a required manual step, a blocking challenge gate, or an external blocker past its waiting limit. Batch genuine developer gates and continue unrelated approved work when it is safe.

For a standing program, read and follow `orchestrate-program`. For other modes, keep a compact task ledger in an approved scratch location outside tracked project content. Record the contract, assignments, PR plan, decisions, status, evidence, and open risks.

## Dispatch and integrate

Give each agent the contract, exact ownership, forbidden work, dependencies, expected result, verification, ledger path, and assigned PR, branch, and worktree.

- Keep one writer per scope, branch, and worktree.
- Parallelize only independent work and stay within the approved WIP limit.
- Use worktrees only when the delivery plan calls for them.
- Use installed domain skills when they materially improve the assigned work.
- For behavior changes, capture the expected failing check and the passing check after the smallest implementation. When no practical automated seam exists, use the narrowest executable proof and state the limit.

The orchestrator judges results against the contract, repository evidence, and tests. It stays out of routine implementation. It may make a tiny integration fix when reassignment costs more, but it must disclose and verify the change.

Review every PR before landing with a fresh-context agent that did not implement its scope. Record the repository, PR, head SHA, reviewer, checks, runtime evidence, verdict, and residual risk. A new head invalidates the prior verdict. CI is evidence, not the verdict.

When `code-review` is installed, every independent PR reviewer must use it to keep repository-standards and governing-contract checks separate. Its reviewers must still be independent of the implementation.

Fix valid findings, verify the affected behavior on the new head, and stop when no actionable findings remain. Use `challenge` when review exposes a blocking defect, repeated violations of one invariant, several fresh defects after completion, or a fix that expands scope. Do not add review rounds after actionable findings are resolved.

Land each cohesive PR as soon as it is independently verified and the approved authority includes merging. Do not advance dependent work until every prerequisite PR passes exact-head review and merges. Park discoveries that do not block the current contract as follow-up work instead of expanding the active PR.

## Verify and close

Inspect the integrated result and run fresh checks that match the risk. Account for every acceptance criterion, assignment, review finding, permission boundary, and unresolved risk. An agent's success report is not proof.

Report the result, changed scope, verification evidence, unresolved risks, and required developer action. Remove temporary ledger state after verified completion unless a durable handoff is required. Clean up only approved, task-created branches and worktrees with no user-owned or unmerged work.

When an installed OpenSpec workflow governs the change, keep its artifacts coherent with accepted decisions. Sync and archive only when repository policy allows it, implementation and proof are complete, and no required task remains unchecked.
