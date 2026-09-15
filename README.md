# AI in sociological research — NYU Sociology

**Christopher Barrie and Bart Bonikowski**

[Live presentation](https://cjbarrie.github.io/nyu-sociology-ai-research/) · [PDF slides](https://cjbarrie.github.io/nyu-sociology-ai-research/artifacts/presentation.pdf) · [Co-presenter editing guide](docs/CO_PRESENTER.md) · [Presenter notes](research/speaker-notes.md)

The current presentation has **18 slides**, timed to **15 minutes plus five minutes of discussion**. It demonstrates agent-assisted research through the question: do AI chatbots reduce support-seeking from friends and family?

## Current slide order

| Slides | Content |
|---|---|
| 1 | Title: “Some ways we can use these tools.” |
| 2–4 | Coxon, Amodei and Trump images, inside the deck’s normal frame |
| 5–8 | Cognitive offloading, research agents, the chat window and the agent environment |
| 9–11 | Three working relationships: delegate, steer and collaborate with a challenging coauthor |
| 12 | The chatbot and support-seeking research question |
| 13 | Skill walkthrough: add the skill, give the assignment, run a script, inspect the files |
| 14 | Search outputs: nine study records, retrieval record and bibliography |
| 15 | Paired discussion of the research question |
| 16 | Source and methods agents reviewing one another’s work |
| 17 | Compiled research proposal, LaTeX and bibliography |
| 18 | Discussion: influence on research questions, reproducibility and deep reading |

Use the arrow keys to move, **N** for presenter notes and **F** for full screen. Slide 13 has four clickable steps. Research PDFs and source files open directly. The removed phone-app finale is not part of this repository.

## Materials for presenters

- [Research files](https://cjbarrie.github.io/nyu-sociology-ai-research/workshop/index.html)
- [Evidence table](https://cjbarrie.github.io/nyu-sociology-ai-research/workshop/evidence.html)
- [Skill example](research/skills/literature-audit/SKILL.md) and [setup instructions](research/workshop-howto.md)
- [Source review](research/audit/source-audit.md) and [methods review](research/audit/methods-audit.md)
- [Research proposal PDF](https://cjbarrie.github.io/nyu-sociology-ai-research/artifacts/study-protocol.pdf)
- [Closing discussion talking points](research/discussion-notes.md)
- [How the proposal was made](https://cjbarrie.github.io/nyu-sociology-ai-research/workshop/production.html)
- [Offline presentation download](https://cjbarrie.github.io/nyu-sociology-ai-research/artifacts/local-presentation.zip)

The final slide asks what norms we should develop for ourselves, coauthors and students. Its reading question is: “How do we preserve sustained engagement with sources when AI mediates what we read?” Fuller discussion prompts and possible practices to debate are included in the presenter notes.

## What was executed, and what is illustrative

The bounded literature search was conducted on **8 September 2026**. Separate source and methods agents reviewed and cross-checked the work on **9 September**, when the original proposal was compiled. Its production note was added on **15 September**; the literature search has not been refreshed. The proposal is four pages plus references, with no recruited participants, estimated effects or validated questionnaire.

The workshop-authored `literature-audit` skill codifies the earlier workflow; it did not generate the original review through a recorded invocation. Its `allowed-tools` header illustrates Claude Code permissions, including specific Bash PDF commands. Permission handling differs between agent environments.

The Python-search command on slide 13 is an **illustrative example**. That script is not included or claimed to have run. The paired coauthor dialogue is scripted, rather than a transcript of Christopher’s statements. The source/methods reports and saved retrieval/compilation command records are actual outputs. Recordings replay command output with adjusted playback timing. The agent-harness diagram is a teaching schematic.

Opening images were supplied for the presentation. Study screenshots, citations and publication versions are retained with the research materials. These excerpts and third-party materials are not presented as original work by the presenters.

## Edit and preview

Start with [docs/CO_PRESENTER.md](docs/CO_PRESENTER.md), which includes a file map and prompts for Claude or another coding assistant. Assistants should also read [AGENTS.md](AGENTS.md); [CLAUDE.md](CLAUDE.md) points to the same instructions.

Requires Node.js 22.13 or newer:

```sh
npm ci
npm run dev
```

Open the local address printed in the terminal. No AI API key is required to run the presentation. The main browser source is `app/page.tsx`; opening research slides are in `app/opening.tsx`; styles are in `app/globals.css`.

## Build and publish

`npm run build` creates the static export. The GitHub Actions workflow builds pull requests and publishes changes to `main` through GitHub Pages. `scripts/github_pages.py` adapts resource paths and PDF links to the repository’s Pages address. Check the Actions deployment result before sharing an update.

The older private ChatGPT-hosted Site is a separate deployment and is not updated by GitHub pushes. The live GitHub Pages link above is the current presentation.

Browser slides and PDF slides have separate sources. For PDF slides, install `reportlab`, `pillow` and `pypdf`, then run:

```sh
python scripts/presentation_pdf.py
```

The PDF generator currently uses Arial and Georgia from macOS; configure equivalent installed font paths on other systems. It regenerates the PDF and timed notes, appending `research/discussion-notes.md`. Commit the generated files along with source changes.

The research proposal requires TeX Live: `latexmk -pdf -cd research/protocol/memo.tex`. Copy the compiled PDF to `public/artifacts/study-protocol.pdf` and update its public LaTeX copy and preview if the proposal changes. `npm run build` does not regenerate PDFs.

After rebuilding, `python scripts/package_deliverables.py --local` refreshes the research and offline archives. It requires `pypdf`. Run `scripts/revision_materials.py` only when intentionally regenerating its workshop outputs; inspect it first because it rewrites multiple files. Historical analysis scripts may additionally require matplotlib, numpy and pyyaml.

## Offline use and archived work

Unzip `local-presentation.zip`, run `python3 serve.py`, and open `http://127.0.0.1:8765`. Do not open the HTML using `file://`. External paper and documentation links still need Internet.

Earlier hypothetical simulations remain under `public/lab/` and `research/` as archived development work; they are outside the current walkthrough and are not empirical findings. The phone diary app and its downloadable study server were removed. Do not restore those files through old archives.
