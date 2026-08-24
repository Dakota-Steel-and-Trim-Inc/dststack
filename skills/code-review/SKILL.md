---
name: code-review
description: Review a branch or pull request against repository standards and the governing request or specification. Use for an independent exact-head verdict before merge or when the user asks to review committed changes. Do not use it to authorize fixes or landing.
---

# Code review

Review the same diff along two separate axes: repository standards and requested behavior. Findings must be actionable, introduced by the reviewed change, and supported by current code.

## Pin the scope

Resolve the repository, base, committed head, merge base, and diff before reviewing. For a pull request, record its number and exact head SHA. For a branch, record its full ref and exact head SHA. Review commit objects, not the mutable worktree. Report any worktree changes as outside the verdict and leave them untouched. A new head invalidates the verdict.

Read the nearest repository instructions and relevant standards. Identify the governing behavior from the developer's request, an approved OpenSpec change or other specification, linked issue, acceptance criteria, and PR description. State when no behavior contract is available instead of inventing one.

## Review independently

The caller is the review coordinator. When delegation is available, it uses two fresh-context reviewers that did not implement the scope. Run them in parallel only when the environment and task allow it. Give each reviewer the repository, base and head SHAs, merge base, diff command, applicable standards, governing contract, and its assigned axis. Axis reviewers must not invoke `code-review` or delegate another review.

Without delegation, the coordinator may review both axes directly only when it did not implement any reviewed change. Otherwise obtain an independent reviewer or stop before landing.

The standards reviewer checks:

- Violations of repository instructions or documented conventions.
- Correctness, security, data safety, and compatibility defects visible in the diff.
- Missing verification for behavior or risk introduced by the change.
- Missing red and green evidence when the repository, governing contract, or implementation brief required `tdd`. Do not require it for work the TDD skill excludes or when no practical public seam exists.
- Unnecessary duplication, scope, or abstraction that makes the change harder to maintain.

The behavior reviewer checks:

- Missing or partially implemented requirements.
- Behavior that contradicts the governing contract.
- Unrequested behavior that materially expands scope or risk.
- Tests or documentation that claim behavior the implementation does not provide.

Skip formatting or mechanical issues already enforced by tooling. Do not report speculative concerns without a concrete failure path or violated rule.

## Verify and report

The main reviewer confirms each finding against the exact diff and surrounding implementation. Keep the two axes separate so one cannot hide failure in the other.

After both axes finish, resolve the current PR head or branch ref again. Discard the verdict if it differs from the reviewed SHA. Before landing, compare the recorded reviewed SHA with that mutable ref once more.

Report findings first, ordered by severity within each axis. Include the file and tight line range, the violated rule or requirement, the failure it causes, and the smallest useful correction. If there are no actionable findings, say so and name any verification limit or residual risk.

Record the base and head SHA with the verdict. This skill does not authorize edits, review comments, thread resolution, commits, pushes, merges, deployments, or cleanup.
