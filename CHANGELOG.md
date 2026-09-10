# Changelog

## Unreleased

- Removed `project-verification`; verification now uses existing project tests and documentation without prescribing a generated adapter.

- Clarified that evidence can reject an invalid bot finding while repository-required approvals and thread resolution remain merge gates.
- Added focused `codebase-design` and `diagnosing-bugs` adaptations for ownership decisions, testable interfaces, and evidence-led diagnosis.
- Made routing and challenge gates depend on unresolved risk, with one independent reviewer by default and bounded follow-up review.
- Separated verifier execution from setup work and favored existing executable commands over repeated shell procedures.

- Reused explicit delivery authority in `orchestrate`, kept inline work direct, and separated a fresh review verdict from rerunning unchanged checks.
- Added host, repository, lifecycle completion, and version-policy context to delivery plans and program recovery.
- Added the existing DST `pr-review-follow-up` workflow and routed GitHub closeout through it.
- Added a read-only installation comparison for skill files and recorded provenance, with focused CLI tests in CI.
- Recorded the September 5 upstream review separately from unchanged third-party import pins and licenses.
- Added `project-verification`, a safe generator and maintenance workflow for repository-owned web, API, container, CLI, mobile, and integration verification adapters.
- Documented canonical skill ownership and duplicate-name policy for mixed global installations.
- Routed realistic runtime proof through project-local verifiers without replacing focused TDD or making OpenSpec mandatory.
- Added Matt Pocock's adapted `tdd` skill for red and green vertical slices at agreed public seams, with routing, orchestration, planning, prototype, and review integration.
- Added Matt Pocock's adapted `research` skill to feed primary-source evidence into planning and optional OpenSpec exploration.
- Added Matt Pocock's adapted `prototype` skill for disposable logic, state, and UI experiments before committing to a production design.
- Added Matt Pocock's adapted `code-review` skill for separate repository-standards and governing-contract review at an exact head.
- Added `route-work` to choose the lightest delivery path before implementation.
- Documented the complete DST Stack flow with quick-change and full-flow examples.
- Added OpenSpec as an optional official companion without copying its skills.
- Allowed orchestration to use an approved OpenSpec change as its governing contract.

## 0.1.0 - 2026-08-23

- Added the initial portable Agent Skills collection.
- Added bounded and program-scale orchestration.
- Added PR delivery planning and risk challenge gates.
- Added the `unslop` writing skill from pstack with attribution.
- Added a self-contained adaptation of Matt Pocock's `grill-me` workflow with attribution.
- Added global installation guidance and repository validation.
