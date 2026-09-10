# AI in sociological research — NYU Sociology

[Live presentation](https://cjbarrie.github.io/nyu-sociology-ai-research/) · [Co-presenter editing guide](docs/CO_PRESENTER.md)

**Co-presenters: start with [the editing guide](docs/CO_PRESENTER.md).** It includes setup, Claude prompts and the publication workflow.

The primary presentation is a fourteen-scene browser deck with restrained typography, step-by-step workflow slides, expandable evidence tables, CLI walkthroughs and real retrieval playback. Research PDFs open normally. The PDF deck remains a backup; the ordinary file index is at /workshop/index.html.

## Fifteen-minute walkthrough

The opening four minutes cover cognitive-offloading research, agent evaluations, and the 2025/2026 interface comparison. Readings and claim checks are at /workshop/opening.html. The date labels refer to our workshop focus, not invention dates.

1. Three working relationships: delegate a bounded task, guide consequential decisions, and work through an argument with a skeptical coauthor.
2. Reporting motivates the question of chatbot use and support-seeking from friends and family.
3. Open the workshop-authored literature-audit skill, show where it goes and what to type, then inspect the evidence and retrieval records.
4. Open a scripted paired conversation and the actual independent source/methods reviews. Their provenance is clearly distinguished.
5. Open the compiled study protocol and draft diary instrument, including estimands and limitations.

Timed notes: research/speaker-notes.md. The browser index links directly to each output. The study proposal is four pages plus references; no empirical results or validated questionnaire are claimed.

## Provenance and limitations

The initial bounded review was conducted 8 September 2026. The reusable skill and actual agent audits were created during revision on 9 September. The skill codifies the earlier procedure; the original review is not attributed to a recorded invocation of that new skill.

Two separate Codex agents wrote research/audit/source-audit.md and methods-audit.md, then cross-checked each other. The reports are actual output. The researcher dialogue in coauthor-dialogue.md is scripted for teaching. Substantive questions in the protocol remain open.

A fresh local skill demonstration was attempted. The installed Codex CLI had a missing executable; Claude Code returned an expired OAuth session. No authentic skill-invocation recording is claimed. The original source-retrieval and model command recordings remain in research/recordings and are clearly labeled as command-output replays.

The Guardian image is a cropped screenshot of the headline from the linked article, captured 9 September 2026. It does not reproduce the article body. No confidential material or raw third-party papers is included in the delivery archive.

## Rebuild

- Browser development: `npm run dev`
- Production: `npm run build`
- Research proposal: `latexmk -pdf -cd research/protocol/memo.tex`
- Workshop pages and copied outputs: `python scripts/revision_materials.py`
- Slides and timed notes: `python scripts/presentation_pdf.py`
- Archives: `python scripts/package_deliverables.py --local` after the production build

Python authoring dependencies: reportlab, pillow, matplotlib, numpy, pyyaml. LaTeX requires a standard TeX Live installation. The slide script uses Arial and Georgia from macOS. Browser runtime needs no AI API or external fonts.

## Offline use

Unzip local-presentation.zip, run `python3 serve.py`, then open http://127.0.0.1:8765. The index and all workshop outputs work locally. Primary-paper and official-documentation links need Internet. The bundled offline slide PDF uses local links for workshop outputs.

## Archived virtual field study

The new simulation is a transparent design sandbox. Support availability affects outreach and uptake. At a zero causal effect, users can still appear to seek less support. ITT retains the randomized offer groups. It reports point estimates, known finite-population effects, and an optional distribution over 200 assignments. All data and rules are synthetic. Avatar appearance, motion and setting have no analytical meaning.

Source: public/lab/model.mjs. Validation: node scripts/test-lab.mjs. The default assignment yields a users/non-users contrast of about −2.56 requests, ITT −0.12, and known offer effect zero. Across 1,000 assignments, mean ITT is approximately zero while the users contrast remains negative. Tests cover determinism, balanced randomization, noncompliance, potential outcomes, sign boundaries and CSV export.

The neighborhood is AI-generated artwork. The small avatar icons use the operating system emoji font. No faculty likenesses or real participant records are represented.

## Archived support-mechanism simulation

The archived /lab/ page compares two matched worlds with 24 fictional people and 40 support concerns. Animated routes, episode narratives and three-stage playback show concern, support-seeking and follow-up. Presets compare substitution with chatbot-encouraged human contact. Measures distinguish requests, successful human responses, chatbot interactions and concerns with no response. All behavioral rules remain hypothetical and no relationship erosion is claimed. The earlier randomized-study sandbox remains at /lab/selection.html.

Run node scripts/test-mechanisms.mjs for deterministic event/accounting and boundary-case tests. The new model is public/lab/mechanisms.mjs; paired event data can be exported directly from the interface.

Opening sources are recorded in research/opening/sources.json, with a separate BibTeX file. The four-stage agent-harness diagram is an illustrative teaching schematic, not live execution. The timed speaker notes cover all fourteen slides in fifteen minutes.

