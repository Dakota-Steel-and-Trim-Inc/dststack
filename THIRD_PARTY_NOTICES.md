# Third-party notices

## Upstream review on 2026-09-05

The source pins below identify the material imported into DST Stack. The reviewed revisions in this table record a later comparison. They do not replace the import pins or mean that newer upstream behavior has been adopted.

| Upstream | Reviewed revision | Result |
|---|---|---|
| [Matt Pocock's skills](https://github.com/mattpocock/skills) | [`3cca18b368ae95cdbdebbff572ccafa662551015`](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015) | The source directories used by DST's five Matt-derived skills are unchanged since the recorded import pin. Upstream added an experimental `retro` skill under `skills/in-progress/` and changed its local linking script. Neither is imported here. |
| [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack) | [`7314f723a487ec406b6369fe5865ba034cfed166`](https://github.com/cursor/plugins/tree/7314f723a487ec406b6369fe5865ba034cfed166/pstack) | This is the latest commit affecting `pstack` in the checked monorepo head, `93b00b89ef425a9c1bac0d0b317dfc49c930ac99`. Since the recorded `unslop` import pin, its only change is `disable-model-invocation: true`. The verification source directories are unchanged. Other changes include the multi-PR checklist, its validator, PR delivery playbooks, and `make-bot-ui`. No skill changes are imported here. |
| [Michael Denyer's pstack port](https://github.com/michael-denyer/pstack-claude) | [`273d217aea3c8e0a743bcc31bd99d585e3ddf9c6`](https://github.com/michael-denyer/pstack-claude/tree/273d217aea3c8e0a743bcc31bd99d585e3ddf9c6) | Historical source pin for the retired `project-verification` adaptation. |

Lauren Tan's pstack lives in `cursor/plugins/pstack`. The Michael Denyer repository is a separate port and remains the recorded import source for DST's adapted verification workflow.

Compare behavior before adopting a newer revision. In particular, pstack's multi-PR playbook prescribes fixed live-verification lanes, model choices, and platform tooling that DST Stack does not require. Its newer `unslop` invocation setting also needs a separate decision from its writing rules.

## pstack project verification

Sources at [`michael-denyer/pstack-claude@273d217aea3c8e0a743bcc31bd99d585e3ddf9c6`](https://github.com/michael-denyer/pstack-claude/tree/273d217aea3c8e0a743bcc31bd99d585e3ddf9c6):

- `plugins/pstack/skills/create-verification-skill/SKILL.md`
- `plugins/pstack/skills/maintain-verification-skill/SKILL.md`

Retired adaptation: the creation and maintenance workflows were combined into the former `project-verification` skill. It discovers the repository's established project-skill location, supports browser, HTTP, container, CLI, mobile, and integration surfaces, removes Claude-specific agents and paths, keeps feature maps optional, and applies DST Stack's explicit authority, process-ownership, secret, production, evidence, and cleanup rules.

MIT License

Copyright (c) 2026 Lauren Tan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## pstack `unslop`

Source: `pstack/skills/unslop/SKILL.md` at [`cursor/plugins@46125561306434d8a1d7745d540d8932ab0cd2a2`](https://github.com/cursor/plugins/blob/46125561306434d8a1d7745d540d8932ab0cd2a2/pstack/skills/unslop/SKILL.md)

Local modification: none.

MIT License

Copyright (c) 2026 Lauren Tan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## pstack `blast-radius` and `benchmark-checklist`

Sources at [`cursor/plugins@df581122cde17e6e27686b5a448bde23e4ad4318`](https://github.com/cursor/plugins/tree/df581122cde17e6e27686b5a448bde23e4ad4318/pstack):

- `pstack/skills/blast-radius/SKILL.md`
- `pstack/skills/benchmark-checklist/SKILL.md`

Local modifications: removed `disable-model-invocation`, replaced references to pstack's `how`, `why`, `arena`, `principle-explain-the-number`, and playbooks with self-contained wording, and dropped `benchmark-checklist`'s section mapping it to pstack's perf playbooks.

MIT License

Copyright (c) 2026 Lauren Tan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Matt Pocock engineering skills

Sources:

- `skills/productivity/grill-me/SKILL.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/productivity/grill-me/SKILL.md)
- `skills/productivity/grilling/SKILL.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/productivity/grilling/SKILL.md)
- `skills/engineering/research/SKILL.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/research/SKILL.md)
- `skills/engineering/prototype/SKILL.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/prototype/SKILL.md)
- `skills/engineering/prototype/LOGIC.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/prototype/LOGIC.md)
- `skills/engineering/prototype/UI.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/prototype/UI.md)
- `skills/engineering/tdd/SKILL.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/tdd/SKILL.md)
- `skills/engineering/tdd/tests.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/tdd/tests.md)
- `skills/engineering/tdd/mocking.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/tdd/mocking.md)
- `skills/engineering/code-review/SKILL.md` at [`mattpocock/skills@5b15a47f2d7150f545fbcacbfe381787fc0230dc`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/code-review/SKILL.md)

Additional sources imported on 2026-09-06 at [`mattpocock/skills@3cca18b368ae95cdbdebbff572ccafa662551015`](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015):

- `skills/engineering/codebase-design/SKILL.md`
- `skills/engineering/diagnosing-bugs/SKILL.md`

Local modifications:

- `codebase-design` keeps small interfaces, cohesive ownership, and public-behavior testing. It adds cross-repository state ownership, preserves repository terminology, and removes mandatory glossary terms, speculative adapters, and automatic architecture artifacts.
- `diagnosing-bugs` keeps the focused reproduction and falsifiable feedback loop. It permits source investigation before a reproduction exists, respects diagnosis-only scope, bounds retries, and removes mandatory hypothesis counts, runtime assumptions, and the human-loop script dependency.

- The `grilling` alias and its interview process are combined into one self-contained `grill-me` skill. The wording was adapted for agents that do not expose a separate Skill tool.
- `research` reports in chat by default, writes durable notes only when warranted, and returns evidence to optional OpenSpec exploration without editing OpenSpec artifacts.
- `prototype` keeps Matt Pocock's logic and UI branches but moves their detail into `references/`, shortens the instructions, allows native-runtime logic demos, and requires explicit authority before commits, pushes, issue updates, merges, or cleanup.
- `tdd` keeps Matt Pocock's public-seam, vertical-slice, test-quality, and boundary-mocking rules. It treats seams accepted by an approved plan or implementation brief as confirmed, adds explicit exclusions, records red and green proof, and keeps detailed examples in `references/`.
- `code-review` keeps the separate standards and behavior axes, removes the dependency on Matt Pocock's issue-tracker setup, and adds exact-head and authority boundaries for DST delivery. One independent reviewer covers both axes by default, with additional reviewers for specific risks and bounded follow-up review when earlier evidence remains applicable.

MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
