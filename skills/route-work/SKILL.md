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

### Quick change

Choose this when the behavior is clear, localized, and safe for one agent to finish directly. It should not introduce a shared contract, schema or authorization change, migration, production action, cross-repository dependency, or several independently reviewable concerns.

Implement the smallest complete change and run the narrowest useful verification. Do not invoke OpenSpec, PR planning, or orchestration merely because those skills are installed.

### Plan first

Choose this when requirements are unclear, behavior needs a durable contract, or the change affects shared interfaces, authorization, persistent data, migrations, or more than one repository.

If the request already includes an approved contract, do not reopen planning. Implement one bounded change directly or pass multi-PR delivery to `orchestrate`.

OpenSpec is optional. Use it only when the repository already uses it, the developer requests it, or a durable specification will materially improve the work. If OpenSpec is unavailable, use `grill-me`, the repository's existing planning method, or a concise in-chat plan. Never block delivery because OpenSpec is not installed.

When OpenSpec is warranted:

1. Use `openspec-explore` while important behavior remains unsettled.
2. Use `openspec-propose` to create the change contract.
3. Stop for developer approval of that contract.
4. After approval, implement a bounded change directly or pass a multi-PR change to `orchestrate`.
5. Use `openspec-update-change` only when an accepted decision changes.
6. Sync and archive the change according to repository policy after implementation and proof are complete.

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
