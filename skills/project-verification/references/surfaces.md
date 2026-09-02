# Surface guidance

Use only the sections that match evidence in the repository. Prefer an existing project harness over adding a new dependency.

## Web and desktop UI

Prefer the project's Playwright, Cypress, WebDriver, or native automation setup. Reuse its server lifecycle and stable accessibility or test handles. Isolate ports, browser profiles, storage state, and test accounts. Capture the action and result with a trace, screenshot, console or network failure, and the focused test result when supported.

## HTTP, API, and containers

Prefer read-only health, version, schema, or contract endpoints and existing integration tests. Give task-owned Compose runs a unique project name, profile, ports, volumes, and evidence directory. Never take ownership of a container merely because it belongs to the same repository. Mutating endpoint or database proof requires an approved non-production target and isolated disposable data.

## CLI and TUI

Build with repository commands, then run each drive in a task-owned temporary home, working directory, PTY, or session. Capture the invocation, sanitized transcript, exit code, and filesystem effects. Never point cleanup at the user's home, configuration, credentials, or unverified session.

## Mobile

Use the repository's native integration-test runner and a task-owned simulator or emulator state when available. Record the device identity and ownership before driving or erasing it. Prefer mocked or non-production service boundaries already supported by the application. Physical devices and shared simulators require explicit ownership and must not be reset implicitly.

## Libraries and multi-service integrations

Drive the public API through existing integration or contract tests. For multiple repositories or services, record each tested revision and compatibility assumption. Reuse a running dependency only for read-only checks when its identity and safety are known; otherwise launch an isolated task-owned dependency or fail closed.
