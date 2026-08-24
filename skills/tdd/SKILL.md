---
name: tdd
description: Implement features and bug fixes through test-first vertical slices at agreed public seams. Use for production behavior changes with a practical executable seam. Skip copy-only, documentation, generated, configuration-only, and disposable prototype work.
---

# Test-driven development

Use a red then green loop to build one observable behavior at a time. Read the nearest repository instructions, `CONTEXT.md` when present, and relevant ADRs before choosing test names or interfaces.

## Set the seam

A seam is the public interface where a caller can observe behavior without reaching into implementation details.

Use a seam already accepted in the request, plan, specification, or implementation brief. When none is named, state the existing public boundary before editing. Ask the developer only when choosing the seam would change a public or module contract, materially change testing cost, or settle an unresolved product decision. Do not interrupt approved orchestration to reconfirm an accepted seam.

If the interface itself remains unsettled, return to planning or use the repository's design process before tests freeze the wrong boundary.

## Run vertical slices

For each behavior:

1. Write one test through the public seam.
2. Run it and confirm it fails because the behavior is missing. An unrelated existing failure is not a valid red result.
3. Add only enough production code to pass that test.
4. Run the focused test to green, then run the neighboring checks required by repository policy or changed risk.
5. Repeat with the next behavior.

Do not write all tests before implementation or anticipate later slices. Refactor only after green, keep it inside the accepted scope, and rerun the affected checks.

## Keep tests useful

- Assert behavior users or callers care about through public interfaces.
- Derive expected values from the contract, a worked example, or another independent source. Do not restate the implementation in the assertion.
- Mock system boundaries such as external APIs, time, randomness, or file systems. Do not mock internal collaborators merely to make a test easy to write.
- Prefer a test database over a database mock when the repository supports one.

Read [test examples](references/tests.md) when choosing a test shape. Read [mocking guidance](references/mocking.md) when the slice crosses a system boundary.

## Report proof

Record the seam, focused command, expected red failure, green result, and any broader verification. If no practical automated seam exists, use the narrowest executable proof and state the limit instead of inventing an implementation-coupled test.

This skill does not grant authority to change scope, external contracts, production systems, commits, pushes, or merges.
