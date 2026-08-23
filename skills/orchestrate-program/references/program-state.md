# Program state

Use a task-specific durable directory outside tracked project content. Print its absolute path when the program begins. Every file has one writer.

## Required files

### `contract.md`

Record the approved goal, completion condition, governing request and plans, exact authority, forbidden actions, workspace plan, PR order, WIP limit, pilot decision, checks, and intervention points.

### `units.tsv`

One row per implementation, review, integration, or recovery unit:

```text
id	track	scope	owner	branch	worktree	pr	head_sha	status	depends_on
```

Use `planned`, `active`, `ready-for-review`, `blocked`, `landed`, `abandoned`, or `superseded` as status values.

### `verification.tsv`

One row per verdict:

```text
repository	pr	head_sha	reviewer	level	evidence	verdict	residual_risk
```

Use `focused-check`, `runtime`, or `integrated` as verification levels. Use `pass`, `pass-with-notes`, `fail`, or `blocked` as verdicts. A changed head needs a new row.

### `decisions.tsv`

Record material delivery decisions:

```text
timestamp	decision	evidence	contract_effect
```

Minor refinements may continue when they do not change scope, risk, authority, product behavior, dependencies, or landing order.

### `gates.md`

Record only questions that require the developer. Include the blocked action, exact target, evidence, available choices, and approved work that can continue around it.

### `follow-ups.md`

Record discoveries outside the active contract. Include evidence, impact, and the smallest suggested next step. Do not turn them into active work during the program unless they block completion.

## Drain checkpoint

At each phase change, merge-frontier change, recovery, and developer report:

1. Reconcile completed or stalled units.
2. Update exact PR heads.
3. Invalidate stale verdicts.
4. Record decisions and gates.
5. Refill only the approved WIP capacity.
6. Report counts and blockers from the files instead of reconstructing them from chat history.
