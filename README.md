# DST Stack

DST Stack is the shared agent toolbox for software work at Dakota Steel and Trim. It collects the skills that have earned a place in our project flow and gives every developer the same way to plan, challenge, deliver, and explain work.

We do not measure an agent by how much code it produces. We care whether the change solves the right problem, stays understandable, passes review, and works when someone uses it. This repository turns that standard into reusable instructions.

## Why we keep this

Agent-assisted development moves fast. The bad version is familiar. Five branches stay open, one PR becomes impossible to review, automated reviewers keep finding the same missing rule, and one person reconstructs the whole change late at night.

DST Stack exists to prevent that pattern. It sets the contract before implementation, keeps work inside reviewable boundaries, and lets an approved delivery continue without asking for permission at every PR. It also gives the agent a clear point where human judgment is still required.

This toolbox will grow, but slowly. A skill belongs here after real project work proves that the team will use it again. "Complete" means this is the one trusted place for our shared skills. It does not mean collecting every interesting prompt we find.

## How we work

- Build the smallest complete solution.
- Prefer code another developer can follow without reconstructing hidden context.
- Reuse existing components, types, and patterns before adding another layer.
- Keep each PR focused on one behavioral concern when the work can be separated safely.
- Limit active work. More agents do not help when they compete for the same files or decisions.
- Find facts in the code and running system. Ask people for product choices and consequential authority.
- Verify the real behavior before claiming completion. Green CI supports a verdict, but does not replace one.
- Once a delivery plan is approved, own it until it is complete or developer intervention is genuinely required.
- Preserve production data, credentials, unrelated changes, and user-owned branches.
- Keep shared project repositories clean. DST Stack is installed globally, not copied into each project.

## Install globally

You need Node.js 18 or newer and GitHub access to this private repository.

Install DST Stack for Codex, Claude Code, OpenCode, and Cursor:

```bash
npx skills add git@github.com:Dakota-Steel-and-Trim-Inc/dststack.git \
  --global \
  --agent codex claude-code opencode cursor \
  --skill '*' \
  --yes
```

Install it only for Cursor:

```bash
npx skills add git@github.com:Dakota-Steel-and-Trim-Inc/dststack.git \
  --global \
  --agent cursor \
  --skill '*' \
  --yes
```

Keep `--global`. Omitting it installs skills inside the current project, which creates copies that drift and clutter repositories shared by the team. Project rules belong in that project's `AGENTS.md`. A project-local skill belongs there only when it is specific to that codebase and the team agrees to maintain it.

Reload the agent after the first installation. Confirm the global skills with:

```bash
npx skills list --global
```

Update the installed DST Stack skills with:

```bash
npx skills update challenge grill-me orchestrate orchestrate-program plan-pr-delivery unslop \
  --global \
  --yes
```

The installer supports Cursor, Codex, Claude Code, OpenCode, and many other agents through the same Agent Skills format.

## Skills

| Skill | Use it when |
|---|---|
| [`orchestrate`](skills/orchestrate/SKILL.md) | A complex change needs a delivery proposal, bounded ownership, coordinated PRs, or continued execution after approval. Skip it for a small local edit. |
| [`orchestrate-program`](skills/orchestrate-program/SKILL.md) | An approved program will span sessions, several coordinated PRs, or enough parallel work to require durable state and recovery. The parent orchestrator normally selects it. |
| [`plan-pr-delivery`](skills/plan-pr-delivery/SKILL.md) | A change needs clear PR boundaries, branch and worktree choices, dependency order, or a landing plan. |
| [`challenge`](skills/challenge/SKILL.md) | Scope, concurrency, review findings, or missing proof suggest that continuing would be hard to review or unsafe. |
| [`unslop`](skills/unslop/SKILL.md) | Any prose needs to sound like a person wrote it. This includes plans, README files, PR descriptions, and user-facing copy. |
| [`grill-me`](skills/grill-me/SKILL.md) | A plan or design feels plausible but still has unresolved decisions. Invoke it explicitly and work through the questions before implementation. |

## How orchestration works

1. `orchestrate` inspects the request and current repository without making changes.
2. It proposes the contract, run mode, PR plan, workspace, authority, concurrency limit, checks, and intervention points.
3. The developer approves that complete delivery plan once.
4. The agent implements, reviews, fixes, verifies, and merges every authorized PR without asking for approval between them.
5. The agent stops only when the approved contract is complete or a genuine product, authority, safety, manual, or external blocker requires intervention.

Ordinary work stays light. Program machinery appears only when a task cannot fit comfortably in one run and needs durable state, a pilot, or restart recovery.

## Adding a skill

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding one. A new skill should solve a recurring cross-project problem, change an agent's decisions in a useful way, and remain portable across our supported agents.

Run the repository checks before opening a PR:

```bash
python3 scripts/validate.py
```

## Third-party work

`unslop` comes from Lauren Tan's pstack. `grill-me` adapts Matt Pocock's `grill-me` and `grilling` skills into one self-contained skill. Both projects use the MIT License. Exact source commits, modifications, copyright notices, and license text are recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

DST-authored work is available under the [MIT License](LICENSE). Third-party portions remain subject to their original notices.
