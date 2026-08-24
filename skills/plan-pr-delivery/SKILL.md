---
name: plan-pr-delivery
description: Plan a requested change as the smallest safe PR sequence, including branch, worktree, pilot, review, and landing strategy. Use for PR decomposition or as the delivery-planning step inside orchestration.
---

# Plan PR delivery

Produce a read-only delivery plan. Do not create branches, worktrees, commits, or PRs.

## Inspect

Read the request or accepted plan, acceptance criteria, repository instructions, PR workflow, target base, active work, current branch and worktrees, and dirty state. Name the governing contract. Surface conflicts and preserve unrelated work.

## Choose the PR plan

Classify delivery as `No PR`, `Single PR`, or `PR series`.

- Use the smallest number of cohesive, independently reviewable PRs. Judge size by behavior, risk, dependencies, and review burden rather than a fixed line or file limit.
- Split independent behaviors, repository boundaries, schema or data phases, cutovers, and cleanup when each slice can land safely.
- Keep tests and documentation with the behavior they cover. When `tdd` applies, name the public seam and expected red and green proof in the PR checks. Do not create an upfront test-only PR for behavior implemented later.
- Leave the target branch valid and tested after every PR. Keep incomplete behavior additive, compatible, disabled, or gated.
- Prefer independently mergeable sequential PRs. Parallelize only independent scopes. Use stacked PRs only when a safe independent sequence is impractical.
- Allow one larger atomic PR when splitting raises risk. State why and require stronger checks.
- Use separate PRs for separate repositories. State compatibility assumptions, dependency order, and cross-repository checks.

For a novel or risky series, designate the first representative PR as a pilot. Take it through implementation, review, verification, and landing before broad delegation. Skip the pilot when the work is familiar, cheap, and uniform, and state why.

Set a WIP limit. Default to no more than three active implementation lanes. Lower it when work shares files, schema, persistent data, product decisions, or depends on the same unmerged PR.

## Choose the workspace

Choose `No workspace change`, `Existing dedicated branch`, `New branch in current worktree`, or `New worktree with branch`. State the base and reason.

- Use one branch per PR.
- Reuse a branch only when it matches the scope, base, and PR boundary and contains no unrelated work.
- Use a worktree when repository rules require one, current state must remain untouched, or concurrent writers need isolation. A sequential PR series alone does not require one.
- Keep one writer per branch and worktree. Give concurrent writers separate worktrees. Sequential writers may reuse a task worktree after a clean handoff.
- Plan cleanup only for task-created state that is safe to remove and authorized.

## Plan review and intervention

Review each PR before landing with someone who did not implement its scope. The same independent reviewer may cover the series. Add a final integrated review only when risk crosses PR boundaries.

List the actions and exact targets needed for the full lifecycle. Identify product, manual, and external-service intervention points that approval cannot cover. Treat approved authority as one lifecycle permission, not a sequence of per-PR gates. The calling orchestrator owns continuation and approval.

## Return the plan

```markdown
## PR delivery plan

Contract: <request, plan, specification, tickets, and acceptance criteria>
Delivery: <No PR | Single PR | PR series>
Workspace: <strategy, base, and reason>
WIP: <active lane limit and serialized scopes>
Pilot: <pilot PR, or why none is needed>
Authority needed: <actions and exact targets for the full lifecycle>
Intervention points: <decisions or actions that still require the developer>

| PR | Scope | Owner | Depends on | Done when |
|---|---|---|---|---|
| <number> | <cohesive change> | <role> | <dependency> | <checkable result> |

Order: <branch, review, and landing order>
Review: <per-PR and integrated review>
Checks: <focused and cross-PR verification>
Cleanup: <only when needed>
Assumptions: <only when evidence is incomplete>
```

Use the table only for a PR series. Keep `No PR` output to applicable fields. For planning-only work, label the workspace and PR map as provisional and make no changes.
