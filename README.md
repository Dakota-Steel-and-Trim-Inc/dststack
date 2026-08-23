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

## The DST flow

`route-work` is the front door for software change requests. It inspects the request and repository, then chooses the lightest path that can finish the work safely.

Agents decide when to load a skill, so automatic routing is best-effort across tools. When you want to guarantee the gate runs, start the request with `$route-work`.

Every route begins with a short decision:

```text
Route: <Quick change | Plan first | Orchestrated delivery | Standing program>
Why: <the fact that determined the route>
Next: <the immediate action or approval point>
```

| Route | Use it when | What happens |
|---|---|---|
| Quick change | The behavior is clear, local, and safe for one agent to finish. | The agent makes the focused change, runs the smallest useful check, and reports the result. |
| Plan first | Requirements remain unsettled or the work changes a durable contract, shared interface, authorization rule, schema, migration, or another repository. | The agent researches unknown facts or prototypes a question that needs executable evidence, then clarifies the contract. It uses OpenSpec only when installed and useful. |
| Orchestrated delivery | The work needs several PRs, workspace decisions, coordinated review, or continued execution after approval. | `orchestrate` proposes the complete delivery contract and waits for one approval. |
| Standing program | The work spans sessions or coordinated tracks and needs recovery state. | `orchestrate` hands the approved delivery to `orchestrate-program`. |

The full flow earns its cost when a mistake could change permissions, corrupt persistent data, break a shared contract, affect several repositories, or hide inside an oversized PR. Skip it for copy changes, one local bug with a clear cause, a focused test adjustment, or another change one agent can finish and verify directly.

### Full-flow example

A developer starts with the work, not a ceremony:

```text
Add an Unlock Orders page under Settings. Admin and management users need role-based site access. The page will call the Customer Portal API and change how logistics database keys are resolved. Take the approved work through reviewed PRs and merge when the required checks pass.
```

`route-work` should answer briefly:

```text
Route: Plan first
Why: This changes authorization, an API contract, and database selection across reviewable concerns.
Next: Settle and approve the behavior contract, then propose orchestrated delivery.
```

The cycle then works like this:

1. The agent inspects repository rules, existing behavior, active work, and acceptance criteria.
2. The agent separates facts from decisions. For example, if the Customer Portal API's supported authorization scopes are unclear, `research` checks the official API contract and returns the finding, sources, and implication. It reports in chat unless durable evidence is warranted.
3. If reading cannot settle whether a state model or UI direction works, `prototype` builds the smallest disposable demo that can answer that question. Its verdict returns to planning, while the throwaway code stays out of production.
4. If the repository uses OpenSpec and it will help, `openspec-explore` uses that evidence to settle open decisions and `openspec-propose` writes the contract. Without OpenSpec, the agent uses `grill-me` or a concise plan. Work never stops because OpenSpec is absent. If an approved contract already exists, skip this step.
5. The developer reviews and approves the behavior contract.
6. `orchestrate` proposes the PR boundaries, branch or worktree choice, checks, merge authority, concurrency, and intervention points.
7. The developer approves that delivery proposal once.
8. The agent implements the pilot, verifies it, uses `code-review` for an independent exact-head verdict, fixes valid findings, and merges when the approved authority and checks allow it.
9. The agent continues through the remaining PRs without routine approval prompts. It stops only for a product decision, missing authority, unsafe state, a required manual action, or an external blocker.
10. The agent verifies the integrated result. If OpenSpec governed the work, it syncs and archives the completed change according to repository policy.

### Quick-change example

```text
Change the Unlock Orders card label from "Order Unlock" to "Unlock Orders" and update its existing test.
```

`route-work` should keep this light:

```text
Route: Quick change
Why: This is one local copy change with a clear expected result and an existing test.
Next: Update the label, run the focused test, and report the result.
```

The agent continues immediately. It does not create an OpenSpec change, orchestration proposal, worktree, or PR series.

## Install globally

You need Node.js 22.20 or newer and GitHub access to this private repository.

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

To update DST Stack, rerun the installation command you used. The installer refreshes every skill from this repository.

The installer supports Cursor, Codex, Claude Code, OpenCode, and many other agents through the same Agent Skills format.

### Optional OpenSpec companion

DST Stack does not require OpenSpec. Install it only if you want durable change proposals and specifications in repositories that benefit from them.

The standard `npx skills` installer cannot ask a repository-specific follow-up question, so OpenSpec remains a separate opt-in step. Install the official [OpenSpec](https://github.com/Fission-AI/OpenSpec) CLI:

```bash
npm install -g @fission-ai/openspec@latest
```

Then install only OpenSpec's six core skills. Do not use `--skill '*'`, which also installs skills meant for OpenSpec's own maintainers.

```bash
npx skills add Fission-AI/OpenSpec \
  --global \
  --agent codex claude-code opencode cursor \
  --skill openspec-explore openspec-propose openspec-apply-change \
          openspec-update-change openspec-sync-specs openspec-archive-change \
  --yes
```

For Cursor only, replace the agent list with `--agent cursor`. In a new repository, `openspec init --tools none` creates the `openspec/` planning structure without copying agent skills into the project. Do not reinitialize a repository that already has an OpenSpec setup.

## Skills

| Skill | Use it when |
|---|---|
| [`route-work`](skills/route-work/SKILL.md) | A new software change request needs the lightest safe route. It explains the choice briefly, keeps small work direct, and selects planning or orchestration only when warranted. |
| [`research`](skills/research/SKILL.md) | A plan depends on an unknown fact that primary sources can settle. It returns evidence to OpenSpec or another planning flow without taking over the decision. |
| [`prototype`](skills/prototype/SKILL.md) | Reading cannot settle a logic, state, or UI question. It builds disposable evidence and returns the verdict to planning without treating the prototype as production code. |
| [`code-review`](skills/code-review/SKILL.md) | A branch or PR needs an independent verdict against repository standards and the governing behavior contract at a committed head. |
| [`orchestrate`](skills/orchestrate/SKILL.md) | A complex change needs a delivery proposal, bounded ownership, coordinated PRs, or continued execution after approval. Skip it for a small local edit. |
| [`orchestrate-program`](skills/orchestrate-program/SKILL.md) | An approved program will span sessions, several coordinated PRs, or enough parallel work to require durable state and recovery. The parent orchestrator normally selects it. |
| [`plan-pr-delivery`](skills/plan-pr-delivery/SKILL.md) | A change needs clear PR boundaries, branch and worktree choices, dependency order, or a landing plan. |
| [`challenge`](skills/challenge/SKILL.md) | Scope, concurrency, review findings, or missing proof suggest that continuing would be hard to review or unsafe. |
| [`unslop`](skills/unslop/SKILL.md) | Any prose needs to sound like a person wrote it. This includes plans, README files, PR descriptions, and user-facing copy. |
| [`grill-me`](skills/grill-me/SKILL.md) | A plan or design feels plausible but still has unresolved decisions. Invoke it explicitly and work through the questions before implementation. |

## Adding a skill

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding one. A new skill should solve a recurring cross-project problem, change an agent's decisions in a useful way, and remain portable across our supported agents.

Run the repository checks before opening a PR:

```bash
python3 scripts/validate.py
```

## Third-party work

`unslop` comes from Lauren Tan's pstack. `grill-me`, `research`, `prototype`, and `code-review` adapt Matt Pocock's skills for the DST flow. Both projects use the MIT License. Exact source commits, modifications, copyright notices, and license text are recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

DST-authored work is available under the [MIT License](LICENSE). Third-party portions remain subject to their original notices.
