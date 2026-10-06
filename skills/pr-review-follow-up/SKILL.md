---
name: pr-review-follow-up
description: Follow GitHub pull requests after they open. Monitor reviews and checks, test reviewer claims against the code and governing plan, handle authorized fixes and replies, verify merges, sync the base branch, and remove authorized feature branches. Use for PR monitoring, CodeRabbit or Codex comments, merge verification, interrupted closeout work, or post-merge cleanup.
---

# PR review follow-up

A reviewer can be wrong. Check every finding before touching the code, and stop where the user's authority stops.

## Start with the facts

Read the nearest `AGENTS.md` and the plan, specification, or acceptance document that governs the PR.

Confirm the repository, PR number, head branch and SHA, intended base, worktree, dirty state, and requested stopping point. Fetch the remote state, then capture:

- the PR state, draft status, head and base refs, head OID, mergeability, review decision, and merge state
- required checks and whether each one is pending or finished
- reviews, issue comments, and every review thread, including resolved and outdated threads
- local, tracking, and remote SHAs for the head and base
- changed files, intended scope, and required tests

Use `gh pr view`, `gh pr checks`, and GitHub GraphQL `reviewThreads` when available. A PR summary, email, or bot overview cannot prove that the review is clean.

When `link_pull_request` is available, register every PR this thread opens or works on, including each layer of a stack.

## Respect the permission boundary

Monitoring is read-only. "Handle this review" permits scoped fixes, pushes, review replies, and thread resolution when the evidence supports it.

Merge, deploy, publish, edit a tracker, or delete a branch only when the user has authorized that action or the repository instructions authorize it without ambiguity. A request to monitor does not grant any of those permissions.

Reuse existing authority only for the same action, exact target, and scope. Record the requested stopping point. In-scope review fixes do not reopen an already-approved delivery; deployment or a different target still needs its own authority.

Preserve unrelated files, commits, stashes, branches, worktrees, and safety refs. Never delete `main`, `dev`, or another user's work.

## Follow the current head

Tie every conclusion to the current head OID. If the head changes, inspect the new diff and replace the old baseline. Rerun checks affected by the new commits. Keep evidence whose inputs did not change.

Trust current-head checks, reviews, and thread state over stale bot summary text. Report the mismatch, but do not let stale editable text block an otherwise clean review.

Trigger only the reviewer named by the user or required by the repository. Use `@coderabbitai review` only when the user requests it or the repository names it as the approved command.

Poll while a review or check is pending. Stop after three unchanged checks or ten minutes unless the user explicitly asked for ongoing monitoring.

For that ongoing monitoring, use `watch_pull_request` when it is available instead of a polling loop, and end the turn. T3 Code wakes the thread when checks finish, someone else comments, or the branch conflicts. Re-read the PR on each wake, re-arm after a push you act on, and call `unwatch_pull_request` once review is done or the wait is no longer authorized. A wake does not grant merge authority. Once every actionable finding is settled, do not manufacture another review round.

When several independent PRs need work, use one writer per PR or repository if delegation is available and useful. Keep coupled changes with one writer. The lead agent still checks the final threads, checks, merge evidence, refs, and preserved user state.

## Judge each finding

Inspect the cited code, surrounding behavior, equivalent call sites, tests, and governing contract. Put the finding in one of these buckets:

- `valid` means the reviewer found a real defect or contract mismatch
- `invalid` means the proposed change conflicts with the intended behavior, architecture, or scope
- `addressed` or `outdated` means the current head no longer has the problem
- `needs user decision` means two reasonable interpretations would change behavior or scope

For a valid finding, make the smallest complete fix. Run the narrow regression first. Broaden testing only when repository rules or shared risk call for it.

For an invalid finding, reply in English with the code or contract evidence that disproves it. Do not change correct code to placate a reviewer.

Resolve a valid thread after the fix and evidence are present on the current head. For an invalid finding, record the evidence and disposition; an independent reviewer should check a material dispute. Do not treat a bot's agreement as an extra merge requirement. Follow repository policy for resolving threads and required approvals: an open thread still blocks when the repository requires its resolution. If a required gate remains unmet at the monitoring limit, report it rather than repeating the argument or bypassing the gate.

After a push, request another review only when the named reviewer does not run automatically and that request remains authorized. Follow a later instruction not to retag a reviewer; report any resulting conflict with a required review gate. Read every thread and check again on the new head.

## Escalate patterns through challenge

Treat CodeRabbitAI and Codex as independent evidence sources when the repository workflow supports both. Do not assume either reviewer is correct, and do not request a reviewer without authorization.

Run `challenge` when a current-head review reveals a blocking or high-severity defect, several fresh defects after the PR was considered complete, the same violated invariant in sibling paths, a fix that expands the contract or scope, or a material disagreement between reviewers. One isolated defect with a bounded fix does not need the gate.

If the result is orange or red, pause merge and deployment work until the required proof, scope split, contract decision, or user authority is present. Do not manufacture another review cycle once all actionable findings are resolved.

## Know when review is done

Review is complete only when the final head shows:

- required checks finished successfully
- every finding has a current-head disposition supported by evidence, and every actionable finding is fixed
- no actionable thread remains open, and repository-required thread resolution and approvals are satisfied
- focused tests pass, along with any final gate the repository requires
- the PR still targets the intended base and contains only the intended changes

A failed, skipped, or unavailable required check blocks the merge. An exception needs both repository support and the user's explicit approval for that exact check.

## Merge, then prove the merge

Merge only with authority. Immediately before the merge, refresh the PR and remote refs. Recheck the repository, PR, base, head SHA, checks, threads, review decision, and required merge method.

A successful merge command is not proof. Confirm that the PR reports the merge commit, the intended remote base contains the expected result, and the checks and reviews belong to the merged head. Make sure the base did not move somewhere unexpected.

For merge commits and fast-forwards, use reachability when the merge method preserves it. A squash merge needs different proof. Check the PR merge record, the expected squash commit, and a fresh comparison showing that the base contains the intended feature changes.

## Stop when GitHub disagrees with itself

Freeze external changes when GitHub API, Pull Requests, Actions, or Git Operations are unavailable, degraded, or contradictory. Preserve reachable refs and state exactly what cannot be trusted.

Resume only after fresh PR data, remote refs, checks, and the intended base agree. A green status page is not enough. Do not recreate or delete branches while the merge state is uncertain unless recovery needs it and the user approves.

## Check plans and trackers

After the merge, inspect the governing plan and relevant issue for stale PR or delivery status. Edit them only when the user or repository workflow authorized the update. Merge permission alone does not cover status edits.

## Sync and clean up

Switch to the base branch only when that preserves the user's worktree. Otherwise leave the checkout alone and report the remaining sync step.

Fast-forward from the intended remote base. Never force, reset, or overwrite unrelated work. Check local, tracking, and remote parity, and separate pre-existing worktree changes from the task.

Delete only authorized feature branches owned by this task. First prove that the verified base contains their intended changes, using evidence that fits the merge method. Remote branch deletion needs its own authority.

Preserve other users' branches, worktrees, and safety refs. After cleanup, check the refs again and report what was removed, what stayed, and how the removed work remains recoverable.

## Report where things stopped

Lead with the result. Include the PR state, final head, merge commit, finding decisions, tests run, base parity, plan or tracker drift, and branch cleanup. Name any outage, missing permission, contradiction, or event needed to continue.

Distinguish merged, synchronized, deployed, and live behavior verified when relevant. Report only stages supported by their own evidence; unrequested stages remain out of scope.

Never call a PR review-clean, merged, synchronized, or cleaned up without fresh evidence for that exact claim.
