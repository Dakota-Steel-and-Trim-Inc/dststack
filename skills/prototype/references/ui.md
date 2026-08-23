# UI prototype

Use several structurally different variants when the question is what a page or interaction should look like.

## Place the variants

Prefer an existing route so each option uses the real shell, data density, parameters, and read-only data. Switch variants with a shareable `?variant=` search parameter. Create a clearly named prototype route only when no existing page can host the work.

## Build the comparison

1. State the design question and default to three variants. Never exceed five.
2. Make the variants disagree about layout, information hierarchy, or the primary action. Color and copy changes do not count as separate directions.
3. Use the project's component library and styling system, but avoid a shared layout that makes every variant the same.
4. Add one small floating switcher that changes the URL parameter and shows the active variant. Arrow-key navigation is useful when it does not intercept typing.
5. Keep mutations stubbed or pointed at disposable data. The prototype evaluates the UI, not the backend.

## Judge the result

Give the developer the route and variant keys. Record the chosen direction, useful pieces from other variants, and why the choice won.

Do not promote prototype code directly. Rebuild the accepted direction through the normal implementation and verification workflow, then remove the switcher and losing variants under the approved cleanup authority.
