---
name: diagnosing-bugs
description: Diagnose a defect, intermittent failure, or performance regression through a focused reproduction and falsifiable evidence. Use when the cause is uncertain; handle an already-understood bounded fix directly.
---

# Diagnosing bugs

Find the mechanism behind the user's symptom before changing behavior. Diagnosis remains read-only unless a fix or temporary instrumentation is authorized.

## Establish the symptom

Identify the expected result, actual result, triggering inputs, and relevant code or runtime revision. Read the responsible path, existing tests, recent changes, and safe logs. Form preliminary hypotheses while inspecting evidence; a missing automated reproduction does not prohibit investigation.

Classify whether the evidence points to product behavior, test setup, missing environment state, an external dependency, or an unresolved cause. Avoid changing application code to compensate for the wrong branch, missing credentials, or a stale generated artifact.

## Build a focused feedback loop

Use the smallest available test, HTTP request, CLI command, browser action, or recorded trace that distinguishes the reported failure from success. Prefer the repository's existing harness. State what the check actually proves.

Keep fixtures isolated and deterministic where practical. Control time, credentials presence, dependency responses, and state only where they affect the symptom. For intermittent failures, use a bounded repetition or controlled event ordering, with an attempt limit and deadline. Report the reproduction rate and uncertainty rather than claiming a random failure is deterministic.

If the runtime is unavailable or the check would need unauthorized effects, continue useful source analysis and identify the exact missing evidence. Do not manufacture a passing substitute or require production access merely to keep investigating.

## Test the cause

Choose the next probe that best distinguishes plausible explanations. State its prediction, change one relevant variable, and inspect the result. One well-supported hypothesis is enough; add alternatives when the evidence leaves competing mechanisms.

For a performance issue, measure the affected operation before choosing a fix. For asynchronous state, inspect the order of events and ownership of the final result. Keep probes proportional to the uncertainty.

A failed probe must change the investigation. Stop after three unchanged checks or ten minutes of unchanged external state unless ongoing monitoring was requested. Preserve findings and state what new evidence would enable progress.

## Fix when authorized

Turn the reproduction into a focused regression check when it protects a meaningful contract. Confirm it detects the original failure, then make the smallest change and rerun the original scenario. Preserve unrelated behavior and keep broader refactoring separate.

Remove only task-created instrumentation and temporary state after verifying ownership. Retain useful, sanitized evidence. Never capture credentials, private payloads, or shared production data as test fixtures.

Report the confirmed mechanism or remaining hypothesis, changed behavior if any, exact verification, and limits. If a required check could not run, say so. A plausible explanation is not a verified fix.
