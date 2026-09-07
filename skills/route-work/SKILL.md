---
name: route-work
description: Evaluate a software change request before implementation and choose the lightest DST Stack path. Use at the start of a new coding task or when its scope materially changes. Route small changes directly, use OpenSpec only when available and justified, and use orchestration only when delivery complexity earns it.
---

# Route work

Choose the lightest process that can finish the request safely. The purpose of this gate is to prevent both rushed large changes and unnecessary ceremony.

## Inspect the request

Read the request, the nearest repository instructions, current state, and any accepted plan or specification. Identify the behavior being changed, its risk, the likely review boundary, and whether a developer decision is still missing.

Do not add a delivery workflow to an answer, review, explanation, or diagnosis unless the user also asks for changes.

## Choose a route

Routing chooses the delivery process, not the implementation method. For a feature or bug fix with a practical public test seam, use `tdd` and work in red then green vertical slices. Skip it for copy-only, documentation, generated, configuration-only, and disposable prototype work. When no useful automated seam exists, use the narrowest executable proof and state the limit.

For a defect with an uncertain cause, use `diagnosing-bugs` to establish the mechanism. When a change introduces or relocates shared behavior, state, or persistence, use `codebase-design` to identify the existing owner and affected callers before choosing a new boundary. Neither skill creates a separate approval gate for an already-settled contract.

### Quick change

Choose this when the behavior is clear, localized, and safe for one agent to finish directly. An established database or API call does not by itself require planning. New shared contracts, schema or authorization decisions, migrations, production actions, or unresolved cross-repository dependencies need their relevant risk and authority checks.

Implement the smallest complete change and run the narrowest useful verification. Use the existing project-local verifier or canonical runbook when the change needs realistic runtime proof. Use `project-verification` to create or repair one only when setup changes are in scope; otherwise use safe existing commands and report any missing proof. Do not invoke OpenSpec, PR planning, or orchestration merely because those skills are installed.

### Plan first

Choose this when requirements or consequential ownership decisions remain unsettled, or when changed interfaces, authorization, persistence, migrations, or cross-repository compatibility need a durable contract. Reuse a settled contract instead of replanning merely because these areas are involved.

If the request already includes an approved contract, do not reopen planning. Implement one bounded change directly or pass multi-PR delivery to `orchestrate`.

Separate discoverable facts from developer decisions. Use `research` when an unknown technical, legal, API, or product fact could change the contract. Return its evidence to planning. Do not research preferences or facts that the repository can answer directly.

Use `prototype` when reading cannot settle a logic, state, or UI question and a disposable executable answer is cheaper than choosing a production design. Return its verdict to planning. A prototype is evidence, not implementation.

OpenSpec is optional. Use it only when the repository already uses it, the developer requests it, or a durable specification will materially improve the work. If OpenSpec is unavailable, use `grill-me`, the repository's existing planning method, or a concise in-chat plan. Never block delivery because OpenSpec is not installed.

When OpenSpec is warranted:

1. Use `research` for unknown facts that could change the contract. It reports evidence but does not edit OpenSpec artifacts.
2. Use `prototype` only when the remaining question needs executable or visual evidence. It returns a verdict but does not become production code.
3. Use `openspec-explore` while important behavior remains unsettled.
4. Use `openspec-propose` to create the change contract.
5. Stop for developer approval of that contract.
6. After approval, implement a bounded change directly or pass a multi-PR change to `orchestrate`.
7. Use `openspec-update-change` only when an accepted decision changes.
8. Sync and archive the change according to repository policy after implementation and proof are complete.

### Orchestrated delivery

Choose this when delivery needs several PRs, branch or worktree decisions, coordinated ownership, repeated review and merge steps, or continuous execution after one approval. Use `orchestrate`. An approved OpenSpec change may be its governing contract, but OpenSpec is not required.

### Standing program

Choose this when work will span sessions, needs restart recovery, or has several coordinated tracks. Start with `orchestrate`; it decides whether `orchestrate-program` is warranted.

## State the decision

Before implementation, report no more than three short lines:

```text
Route: <Quick change | Plan first | Orchestrated delivery | Standing program>
Why: <the concrete fact that determines the route>
Next: <the immediate action or approval point>
```

For a quick change, continue immediately after the route statement. Do not ask for approval that the task does not otherwise require. For a heavier route, name the one meaningful approval point and avoid routine checkpoints after approval.

Re-evaluate only when the requested behavior, risk, authority, or delivery size materially changes.

## Boundaries

- Skill selection is best-effort across agents. If automatic selection does not happen, the developer can invoke `$route-work` explicitly.
- Routing does not grant authority to commit, push, merge, deploy, migrate, delete, or change credentials.
- Preserve repository-specific rules and accepted specifications.
- Prefer direct work when additional process would produce no new decision or evidence.
- Keep focused tests as the fast loop. Add project-local runtime proof only when the changed surface or blast radius warrants it.
