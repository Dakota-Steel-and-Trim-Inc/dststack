# Contributing to DST Stack

DST Stack should stay small enough that a developer can understand why every skill is here.

## When a skill belongs

A good candidate solves a problem that has appeared in more than one project or delivery run. It changes how the agent makes a decision, proves work, or communicates. It should not duplicate an installed tool with a different name.

Keep project-specific workflows in the project repository. Keep personal experiments outside DST Stack until the team has evidence that they help.

## Make a change

1. Create a focused branch from `main`.
2. Add or update one cohesive behavior.
3. Keep every skill under `skills/<skill-name>/` with a `SKILL.md` entrypoint.
4. Update the README catalog when skill names, triggers, or installation behavior change.
5. Update the changelog when the installed behavior changes.
6. Run `python3 scripts/validate.py`.
7. Open a PR that explains the problem, the decision the skill changes, and the evidence used to verify it.

## Write a useful skill

- Use lowercase letters, digits, and hyphens for the folder and skill name.
- Write a description that says what the skill does and when it should run.
- Include instructions that change decisions. Remove generic advice.
- State meaningful exclusions so a broad skill does not take over small tasks.
- Keep authorization requirements close to the action they govern.
- Use supporting references only when conditional detail would otherwise make the entrypoint hard to scan.

## Import third-party work

Check the license before copying anything. Pin the source commit, preserve the required notice, describe local modifications, and update `THIRD_PARTY_NOTICES.md`. Do not copy a wrapper without the dependency it calls.

## Keep installations global

Documentation in this repository must use the `--global` installer flag. Do not add instructions that copy DST Stack into application repositories. A shared application repository should contain only its own rules and genuinely project-specific skills.
