# Logic prototype

Use one self-contained HTML file when the question concerns business logic, state transitions, data shape, or an API model that is hard to judge on paper.

## Build the demo

1. Put the exact question in a visible introduction.
2. Keep the logic in a small pure module inside the file. The page calls the module; the module never reaches into the DOM.
3. Render the full relevant state in domain language after every action.
4. Provide free-play controls and a few guided scenarios that cover the normal path, an awkward edge case, and an illegal action when relevant.
5. Keep all HTML, CSS, and JavaScript inline so a non-developer can open the file directly.

Choose the smallest fitting logic shape: a reducer, explicit state machine, pure functions over plain data, or a small stateful module.

## Judge the result

The useful outcome is the moment the model behaves differently from what the developer or domain expert expected. Record that verdict and the sequence that exposed it.

Do not connect to a real database, add a framework or bundler, generalize for future cases, or ship the HTML shell. If validated logic is later implemented, treat that as production work and add proportional tests.
