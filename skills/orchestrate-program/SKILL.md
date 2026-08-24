---
name: orchestrate-program
description: Run an already-approved, multi-session software delivery program with a pilot, capped concurrency, durable state, exact-head verification, continuous landing, and restart recovery. Use only when orchestrate classifies the work as a Standing program.
---

# Orchestrate program

This skill adds program machinery to an approved orchestration. It does not replace the parent proposal or widen its authority.

If there is no approved `orchestrate` proposal with a checkable completion condition, exact authority, PR plan, workspace plan, and intervention points, return to `orchestrate` and stop.

## Create durable state

Read [references/program-state.md](references/program-state.md). Create the program directory in an approved durable location outside tracked project content and announce its absolute path. Record the approved contract before dispatching work.

The coordinator owns program state, integration decisions, developer reports, and proof. It stays out of routine implementation. Use a track coordinator only when the main coordinator cannot process the active work without losing context.

## Pilot before scaling

For novel, expensive, or high-risk unit shapes, take one representative unit through the complete path:

1. Write its bounded brief.
2. Implement it on its assigned branch and workspace.
3. Run its focused checks and realistic behavior proof.
4. Obtain independent review at the exact head SHA.
5. Land it when authorized.

Use pilot evidence to correct the remaining scope, PR size, briefs, and verification method before broad delegation. Skip a dedicated pilot for familiar, cheap, uniform work and record the reason.

## Run a rolling queue

- Default to no more than three active implementation lanes. Lower the limit for overlapping files, schema, persistent data, product decisions, or work that depends on the same unmerged PR.
- Keep one writer per scope, branch, and worktree.
- Prefer fewer, broader workers when splitting would create coordination work without independent value.
- Refill capacity only after a unit reaches a terminal state or frees its lane.
- Queue completion reports while writing a brief, changing a branch base, merging, or updating program state. Process them together after that action ends.
- Include the approved contract, paths allowed and forbidden, acceptance criteria, exact checks, time limit, branch, worktree, dependencies, and report shape in every brief. For production behavior changes, name the accepted public test seam and required red and green evidence when `tdd` applies.
- Do not resume an agent with stale instructions. Send a consolidated current brief.

## Verify and land continuously

Record each verdict by repository, PR, and head SHA. Include reviewer, verification level, commands or runtime proof, verdict, and residual risk.

- A new head SHA invalidates the old verdict.
- CI is supporting evidence, not the verdict.
- Behavior-changing work needs executable or runtime proof proportional to its risk.
- The reviewer must not have implemented the scope.
- A failed verdict produces a bounded fix assignment. It does not produce an automatic review loop.
- Stop reviewing when the final head has no actionable findings.

Land each cohesive PR as soon as it is verified and the approved authority includes merging. Do not advance dependent work until its prerequisite PR passes exact-head review and merges. Do not hold completed work until the end of the program.

## Control scope and developer gates

Fix discoveries that block the approved completion condition or the next prerequisite PR from passing review and merging. Put other discoveries in `follow-ups.md` with evidence and return to the approved work.

Write genuine product decisions, authority gaps, unsafe state, manual steps, and external blockers to `gates.md`. Batch them for the developer and continue unrelated approved work when safe. Never ask whether to keep going while an approved next action remains.

## Recover without guessing

Rebuild state from the stored contract, unit table, repository branches, PR heads, verification table, and decision log. Reconcile late or stalled agents against current heads before accepting their work.

Use bounded retries. Follow repository waiting rules when present. Otherwise stop after three unchanged external checks or ten minutes. Replan a failed unit instead of repeatedly issuing the same command. If recovery changes scope, risk, authority, product behavior, or landing order, return to the developer with a revised proposal.

## Close

Reconcile every unit to done, abandoned, or superseded. Confirm the completion condition on the integrated result. Confirm every landed PR had a passing verdict for the head that landed. Report abandoned work, parked follow-ups, residual risks, and developer actions.

Keep durable program state when it is needed for audit or handoff. Otherwise remove only task-created state after verified completion.
