---
name: code-review
description: Review a branch, pull request, or working diff against repository standards and the governing request or specification. Use for an independent exact-head verdict before merge or when the user asks to review changes. Do not use it to authorize fixes or landing.
---

# Code review

Review the same diff along two separate axes: repository standards and requested behavior. Findings must be actionable, introduced by the reviewed change, and supported by current code.

## Pin the scope

Resolve the repository, base, head, merge base, and diff before reviewing. For a pull request, record its number and exact head SHA. A new head invalidates the verdict.

Read the nearest repository instructions and relevant standards. Identify the governing behavior from the developer's request, an approved OpenSpec change or other specification, linked issue, acceptance criteria, and PR description. State when no behavior contract is available instead of inventing one.

## Review independently

When delegation is available, use two fresh-context reviewers that did not implement the scope. Run them in parallel only when the environment and task allow it.

The standards reviewer checks:

- Violations of repository instructions or documented conventions.
- Correctness, security, data safety, and compatibility defects visible in the diff.
- Missing verification for behavior or risk introduced by the change.
- Unnecessary duplication, scope, or abstraction that makes the change harder to maintain.

The behavior reviewer checks:

- Missing or partially implemented requirements.
- Behavior that contradicts the governing contract.
- Unrequested behavior that materially expands scope or risk.
- Tests or documentation that claim behavior the implementation does not provide.

Skip formatting or mechanical issues already enforced by tooling. Do not report speculative concerns without a concrete failure path or violated rule.

## Verify and report

The main reviewer confirms each finding against the exact diff and surrounding implementation. Keep the two axes separate so one cannot hide failure in the other.

Report findings first, ordered by severity within each axis. Include the file and tight line range, the violated rule or requirement, the failure it causes, and the smallest useful correction. If there are no actionable findings, say so and name any verification limit or residual risk.

Record the base and head SHA with the verdict. This skill does not authorize edits, review comments, thread resolution, commits, pushes, merges, deployments, or cleanup.
