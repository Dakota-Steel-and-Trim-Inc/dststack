---
name: orchestrate
description: Propose, approve, coordinate, review, and finish complex software delivery. Use when a change needs bounded agent ownership, a PR series, or continued execution after one approval. Skip small local changes that one agent can finish directly.
---

# Orchestrate

The main agent owns the delivery contract, any missing approval, integration, and proof. Specialists own bounded work. Use the smallest team that earns its cost.

## Inspect the contract and authority

Inspect the request or accepted plan, repository instructions, current state, active work, and acceptance criteria before making changes. Name the governing contract and surface conflicts instead of choosing silently. An approved OpenSpec change may be the contract. OpenSpec is optional and must never block orchestration when the request or another accepted plan is sufficient.

Classify the work:

- `Inline` when one agent can finish the task directly.
- `Bounded delivery` for one cohesive implementation and PR.
- `Autonomous PR series` for several PRs that fit within one continuous run.
- `Standing program` when delivery will span sessions, needs restart recovery, or has several coordinated tracks. Use `orchestrate-program` after approval.

For `Inline`, state that direct work is sufficient and return to it within the existing authority. Do not create a roster, ledger, or proposal gate.

For other modes, check whether the conversation already establishes the behavior contract, delivery shape, exact actions and targets, stopping point, and any concurrency limits. An explicit request can supply that authority. Revalidate current state, briefly record the accepted contract, and continue when it is complete. Do not ask the developer to approve the same scope again. Approval of product behavior alone does not authorize an unlisted push, merge, deployment, migration, or deletion.

Use `challenge` before proposing a roster when ownership, compatibility, authority, recovery, invariants, or competing active work leave a material risk unresolved. A settled cross-repository contract does not require another gate. Use `plan-pr-delivery` for version-controlled implementation or an implementation plan.

When the contract is an approved OpenSpec change, use its requirements and tasks as the behavior boundary. Do not create a second product plan. Use `plan-pr-delivery` only to define delivery boundaries, workspace choices, review order, and landing.

## Propose only what remains undecided

When a delivery decision or authority is missing, keep the proposal read-only and use the shape below. Identify only the missing approval and preserve authority already granted. Continue unrelated approved work when safe.

```markdown
## Orchestration proposal

Goal: <one sentence>
Done: <checkable completion condition>
Contract: <request, plan, specification, tickets, and acceptance criteria>
Mode: <Bounded delivery | Autonomous PR series | Standing program>
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

Set continuation to `Run to completion` unless the developer asks for checkpoints. End the proposal turn before executing anything that depends on the missing approval. Do not dispatch agents, create a ledger, or mutate state for the unapproved work. A materially changed scope or target needs a new decision; routine in-scope fixes do not.

## Run the approved plan

Use the accepted contract from the explicit request or approved proposal. It covers the recorded delivery plan, workspace, authority, WIP limit, and continuation mode. Recheck each exact target before acting. Unlisted actions remain unauthorized.

`Run to completion` means continue across assignments, branches, PRs, reviews, fixes, checks, and authorized merges until the completion condition is true. Do not ask for approval between tasks or PRs. Progress updates do not pause the run.

Stop only for an action outside authority, an unresolved product choice, a material change to contract or risk, unsafe or user-owned state, a required manual step, a blocking challenge gate, or an external blocker past its waiting limit. Batch genuine developer gates and continue unrelated approved work when it is safe.

For a standing program, read and follow `orchestrate-program`. For other modes, keep a compact task ledger in an approved scratch location outside tracked project content. Record the contract, assignments, PR plan, decisions, status, evidence, and open risks.

## Dispatch and integrate

Give each agent the contract, exact ownership, forbidden work, dependencies, expected result, verification, ledger path, and assigned PR, branch, and worktree. For work across machines, include the host, repository location, and target environment. Use internal subagents for bounded assignments. Create a separate user-owned task only when the developer requests one.

- Keep one writer per scope, branch, and worktree.
- Parallelize only independent work and stay within the approved WIP limit.
- Use worktrees only when the delivery plan calls for them.
- Use installed domain skills when they materially improve the assigned work.
- For production behavior changes with a practical public seam, use `tdd` at the seam accepted in the contract or brief. Capture the actual failing check and the passing check after the smallest implementation. When no practical automated seam exists, use the narrowest executable proof and state the limit.

The orchestrator judges results against the contract, repository evidence, and tests. It stays out of routine implementation. It may make a tiny integration fix when reassignment costs more, but it must disclose and verify the change.

Review every PR before landing with a fresh-context agent that did not implement its scope. Record the repository, PR, head SHA, reviewer, checks, runtime evidence, verdict, and residual risk. A new head invalidates the prior verdict. It does not invalidate every test result: retain evidence only when its code, dependencies, configuration, and runtime inputs are unchanged, and record why it still applies. Rerun affected checks and any checks the repository requires on the new head. CI is evidence, not the verdict.

`code-review` is required for every committed head submitted for landing, including a head created by review fixes. The orchestrator invokes it once as coordinator. Default to one independent reviewer covering standards and behavior; add distinct perspectives only for concrete risks or repository requirements. Delegated reviewers must not invoke `code-review` again. Every reviewer must remain independent of the implementation. If the skill is unavailable, stop before landing and ask the developer to install it or approve a different review contract.

Use `pr-review-follow-up` for GitHub review monitoring, finding decisions, authorized fixes and replies, merge proof, synchronization, and cleanup. It does not replace the independent `code-review` verdict. Give each review assignment a scope and deadline. At the deadline, collect its findings and unresolved questions; investigate a specific gap instead of restarting the same broad review. Stop when the final head has no actionable findings and all required proof is present.

When the delivery contract requires runtime proof, use existing tests, supported commands, and project documentation. Report missing required evidence without expanding the task into verification infrastructure work.

Land each cohesive PR through `pr-review-follow-up` as soon as it is independently verified and the approved authority includes merging. Do not advance dependent work until every prerequisite PR passes exact-head review and merges. Park discoveries that do not block the current contract as follow-up work instead of expanding the active PR.

## Verify and close

Inspect the integrated result and run fresh checks that match the risk. Account for every acceptance criterion, assignment, review finding, permission boundary, and unresolved risk. An agent's success report is not proof.

Report the result, changed scope, verification evidence, unresolved risks, and required developer action. Remove temporary ledger state after verified completion unless a durable handoff is required. Clean up only approved, task-created branches and worktrees with no user-owned or unmerged work.

When an installed OpenSpec workflow governs the change, keep its artifacts coherent with accepted decisions. Sync and archive only when repository policy allows it, implementation and proof are complete, and no required task remains unchecked.
