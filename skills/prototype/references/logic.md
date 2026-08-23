# Logic prototype

Use a small executable demo when the question concerns business logic, state transitions, data shape, or an API model that is hard to judge on paper. Default to the repository's native runtime when typing, serialization, concurrency, numeric behavior, or another language semantic affects the answer. Use one self-contained HTML file when a non-developer needs to drive the model interactively.

## Build the demo

1. Put the exact question in a visible introduction.
2. Keep the logic separate from the demo shell. Prefer a pure module when that preserves the behavior under test. Use an explicit stateful module when mutation, identity, or concurrency is the question. When the demo has a page, the page calls the module and the module stays out of the DOM unless DOM behavior is itself under test.
3. Render the full relevant state in domain language after every action.
4. Provide free-play controls and a few guided scenarios that cover the normal path, an awkward edge case, and an illegal action when relevant.
5. Keep an interactive HTML demo self-contained so a non-developer can open it directly. Keep a native-runtime demo to the smallest runnable file or command.

Choose the smallest fitting logic shape: a reducer, explicit state machine, pure functions over plain data, or a small stateful module.

## Judge the result

The useful outcome is the moment the model behaves differently from what the developer or domain expert expected. Record that verdict and the sequence that exposed it.

Do not connect to a real database, add an unrelated framework, generalize for future cases, or ship a prototype shell. If validated logic is later implemented, treat that as production work and add proportional tests.
