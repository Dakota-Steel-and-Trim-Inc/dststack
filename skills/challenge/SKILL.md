---
name: challenge
description: Challenge software work when scope, review findings, verification gaps, or concurrent work indicate that continuing would be hard to review or unsafe. Use before risky implementation or PR integration, and after repeated or high-severity findings. Skip ordinary low-risk changes with clean evidence.
---

# Challenge

Pause risky work long enough to expose the decision that matters. This is a risk gate, not another general code review.

## When to run

Run at the earliest applicable checkpoint.

Before implementation, challenge the plan when:

- Independent behavioral concerns have unresolved dependencies or cannot be verified as one cohesive change.
- Work across repositories, environments, or persistent state has unclear ownership, compatibility, authority, or recovery behavior.
- Intended behavior lacks clear invariants, forbidden changes, or a stop condition.
- More than three active implementation lanes compete for attention, based on current evidence.

Before dispatch or PR integration, challenge the work when:

- The scope combines responsibilities that can be reviewed separately.
- Semantic breadth makes the diff difficult to review. More than 20 meaningful files or 1,000 net handwritten lines is a signal, not an automatic failure. Exclude generated files and mechanical rewrites.
- Production-impacting work lacks proportional rollback, runtime, migration, or contract proof.
- Review or check evidence does not belong to the current head.

After review, challenge the approach when an automated reviewer, CI, or a person reveals:

- A blocking or high-severity defect.
- Several fresh defects after the work was considered complete.
- The same violated invariant in more than one path.
- A proposed fix that expands the behavior contract or requested scope.
- A material reviewer disagreement that code, tests, or the governing specification cannot settle.

Do not run this skill for one isolated, well-understood defect with a bounded fix and a clear regression check.

## Inspect the smallest useful evidence

Use current evidence:

- The governing request, plan, specification, and repository instructions.
- The current diff, branch, PR, and head SHA.
- Unresolved review threads and the implementation behind each claim.
- CI, focused tests, and runtime evidence.
- Deployment, migration, or rollback evidence when relevant.
- The active task ledger when concurrency is part of the concern.

Use `codebase-design` when the uncertainty concerns business-rule, state, or persistence ownership. Crossing a database or repository boundary with a settled contract and sufficient proof is not itself a reason to pause.

Name the load-bearing safety invariant. Inspect the highest-risk path and its failure path. Prove the invariant with executable evidence when practical, or mark it unproven.

## Assign the lowest defensible risk

### Yellow

Continue after stating the concern and adding a focused check, invariant, or rationale.

### Orange

Pause dispatch or integration. Split scope, inspect sibling paths, define the missing invariant, or add the missing proof before continuing.

### Red

Do not merge, deploy, migrate, or perform a destructive action. Ask the developer to decide because a critical defect, irreversible risk, contract conflict, or missing recovery path remains.

## Run one challenge round

1. Collect current facts. Do not rely on stale summaries or comment counts.
2. Group findings by violated invariant or risk category.
3. Assign the lowest risk level supported by the evidence.
4. State the smallest action that reduces the risk enough to continue.
5. Stop after one round unless material new evidence changes the risk.

The developer may override yellow or orange after seeing the evidence. Record the reason and residual risk. Red still requires explicit authority for the blocked action.

Report the challenge in this form:

```markdown
Challenge: <yellow | orange | red>

Evidence
- <current fact>

Load-bearing invariant
- <what must remain true and how it was proved>

Why this is broader than one defect
- <repeated pattern, scope problem, or missing proof>

Required before continuing
- <smallest sufficient action>

Decision available
- <split, add proof, revise the contract, or continue with a recorded reason>
```

If the evidence does not justify yellow, say no challenge is warranted and continue without adding process.

This skill diagnoses risk and recommends a gate. It does not authorize edits, reviews, comments, merges, deployments, migrations, or deletions.
