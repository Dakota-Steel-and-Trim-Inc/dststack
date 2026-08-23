# DST Stack contributor instructions

This repository is the shared source for Dakota Steel and Trim's portable agent skills.

## Scope

- Keep every skill useful across projects and supported agents.
- Keep shared skills global. Do not add project installation files or generated agent directories.
- Put project-specific rules in that project's `AGENTS.md`, not here.
- Add a skill only after repeated work shows that it belongs in the shared toolbox.

## Skill design

- Prefer the smallest complete instruction set.
- Give each skill a precise name, trigger description, and boundary.
- Assume the agent already knows ordinary software development.
- Keep a skill self-contained. If it requires another skill, include that dependency or remove the dependency.
- Put substantial conditional detail in `references/` and link it from `SKILL.md`.
- Preserve explicit approval boundaries for external writes, merges, deployments, migrations, deletions, and credentials.
- Use one writer per branch, worktree, and overlapping scope.
- Apply `unslop` to prose.

## Repository changes

- Keep the README skill catalog accurate.
- Update `CHANGELOG.md` for a release-worthy change.
- Record copied or adapted work in `THIRD_PARTY_NOTICES.md` with its pinned source and license.
- Do not alter third-party copyright or license terms.
- Run `python3 scripts/validate.py` before completion.

## Delivery

- Use focused branches and pull requests.
- Review the final PR head independently before merge.
- Treat green CI as evidence, not the entire verdict.
- Stop when the requested acceptance criteria are met.
