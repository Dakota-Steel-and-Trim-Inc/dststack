---
name: project-verification
description: Create or maintain a repository-specific verify-<project> skill or runbook for realistic runtime proof. Use when a project lacks reliable launch, readiness, drive, evidence, isolation, failure, and cleanup instructions, or when those instructions have drifted. Inspect the repository before choosing web, HTTP, container, CLI, mobile, or integration tooling.
---

# Project verification

Build or maintain the smallest project-local verification adapter that proves the repository through its real supported surface. This skill owns the portable method; the project owns exact commands, selectors, endpoints, devices, and prerequisites.

Use it when realistic runtime proof is warranted by the change or delivery contract. Keep focused tests and `tdd` as the fast development loop. Do not replace them with broad end-to-end runs, and do not introduce OpenSpec unless the project independently benefits from a durable contract.

## Set the boundary

Read the nearest `AGENTS.md`, repository documentation, package and task scripts, test configuration, container files, existing verification instructions, and current git and runtime state. Search for an existing `verify-<project>` skill or canonical runbook before creating one. Maintain or extend the existing authority instead of duplicating it.

Derive the project name from its canonical repository name. Follow the repository's established project-skill location. If no location is established, propose one that each supported agent can discover without copying the shared DST Stack skills into the repository. Ask only when choosing the location would create a new repository convention.

Identify from evidence:

- The user-facing surfaces: web, API, containerized service, CLI or TUI, mobile app, library integration, or a combination.
- The repository-owned commands to install, build, launch, seed, test, and stop the application.
- A read-only readiness check that distinguishes the intended build and task-owned instance from an unrelated process.
- The existing harness: Playwright or another browser suite, HTTP clients and contract tests, Compose profiles, PTY helpers, simulators, integration tests, or native tooling.
- Required credentials, data, services, devices, ports, profiles, and safe non-production substitutes.
- Observable proof and a secret-free evidence location.

Do not assume Playwright, Docker, a browser, a database, or a writable external service. Read [surface guidance](references/surfaces.md) only for the surfaces present.

## Write or maintain the adapter

Keep the adapter concise and executable. Its frontmatter or heading must identify it as `verify-<project>`, and it must contain these sections with repository-specific commands and no placeholders:

### Launch

State prerequisites and the exact task-owned launch command. Use isolated ports, data directories, Compose project names and profiles, simulator state, or temporary homes where the repository supports them. Record the PID, container set, session, worktree, and start time needed to prove ownership before cleanup.

### Doctor

Provide read-only checks for dependencies, configuration presence without values, build or revision identity when available, readiness, and ownership of the runtime being driven. A port answering is not proof that the task owns it. Fail closed if the check cannot distinguish a safe instance.

### Drive

Use the repository's existing harness and stable public handles. Describe representative commands through real routes, accessible names, API paths, CLI syntax, device automation, or integration seams. Exercise user-visible behavior rather than internal setters or test-only backdoors.

### Evidence

Name the task-specific evidence directory and what each proof retains: commands and exit codes, sanitized response metadata or bodies, traces, screenshots, logs, files, or test reports. Capture the action and resulting state. Verify side effects only inside approved isolated state. Never record tokens, cookies, connection strings, environment values, personal data, or production payloads.

### Failure handling

After an unexpected result, stop driving, preserve safe evidence, rerun Doctor, and reset only task-owned state. Distinguish product failure, adapter drift, missing prerequisite, environment failure, and unsafe shared state. Retry only after a different corrective action; otherwise report the exact blocker.

### Cleanup

Stop only processes, sessions, containers, simulators, and temporary state created by the verification run after rechecking ownership. Never kill by process name or port, stop shared Compose projects, delete user data, or remove evidence. If ownership is uncertain, leave the runtime untouched and report it.

## Enforce authority

- Default to local or explicitly approved non-production targets. Never drive production by default.
- Treat login, emails, payments, hosted-provider mutations, database writes, deployments, migrations, and other external effects as writes requiring an existing authority envelope and isolated test data.
- Check only that required secrets exist. Never print, copy, commit, or capture them.
- Do not install dependencies, change hosted configuration, start shared services, or modify product code unless the active request separately authorizes it.
- A dry-run label is not proof of safety. Confirm its observable effects before relying on it.

If safe verification requires credentials or external state not already authorized and available, preserve the guard and return a precise prerequisite. Do not weaken the adapter to manufacture a pass.

## Prove the adapter

For a new adapter, run Launch, Doctor, one representative Drive, Evidence, and Cleanup end to end. Confirm afterward that task-owned runtime state is gone and evidence remains. For maintenance, compare the adapter with current source and scripts, then exercise each materially distinct surface affected by drift; do not edit product behavior to make the adapter pass.

Report one outcome:

- `ready`: the adapter and representative proof passed.
- `updated`: drift was corrected and the changed path passed.
- `blocked`: name the exact unsafe state or missing prerequisite and the last safe proof.

Adapter creation or maintenance does not authorize commits, pushes, PRs, merges, deployments, migrations, credentials, production access, or cleanup of state the task did not create.
